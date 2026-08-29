// ============================================================================
// submit-lead — приём заявки с формы обратной связи.
//
// Зачем отдельная функция, а не прямая вставка из браузера:
//   1. anon-ключ лежит в исходнике страницы. Если разрешить ему писать в
//      leads, таблицу набьют в обход формы.
//   2. IP-адрес виден только здесь — из него считается ip_hash, по которому
//      работает ограничение частоты в базе. Браузер такое прислать не может,
//      точнее может, но соврёт.
//   3. Письмо отправляется тут же, без вебхука и второго сервиса.
//
// Переменные окружения (Supabase → Edge Functions → Secrets):
//   SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY  — проставляются платформой
//   IP_SALT        — любая длинная случайная строка; без неё хеш обратим
//   RESEND_API_KEY — ключ Resend
//   MAIL_TO        — куда слать письмо (george@ganzaconsulting.com)
//   MAIL_FROM      — проверенный отправитель на своём домене
//   ALLOWED_ORIGIN — https://ganzaconsulting.com
//
// Деплой:  supabase functions deploy submit-lead --no-verify-jwt
// ============================================================================
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.4";

const ORIGIN = Deno.env.get("ALLOWED_ORIGIN") ?? "*";

const cors = {
  "Access-Control-Allow-Origin": ORIGIN,
  "Access-Control-Allow-Headers": "content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { ...cors, "content-type": "application/json" },
  });

async function sha256(s: string) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

const str = (v: unknown, max: number) =>
  typeof v === "string" ? v.trim().slice(0, max) : "";

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return json({ error: "method" }, 405);

  let b: Record<string, unknown>;
  try { b = await req.json(); } catch { return json({ error: "body" }, 400); }

  // Honeypot: поле спрятано от человека, его заполняют только боты.
  if (str(b.company, 100)) return json({ ok: true });   // молча принимаем и выбрасываем

  const name = str(b.name, 120);
  const contact = str(b.contact, 200);
  const message = str(b.message, 4000);
  const consent = b.consent === true;

  if (!consent) return json({ error: "consent" }, 400);
  if (name.length < 1 || contact.length < 3 || message.length < 10) {
    return json({ error: "fields" }, 400);
  }

  const kind = contact.includes("@") && contact.includes(".") && !contact.startsWith("@")
    ? "email" : "telegram";

  const ip = req.headers.get("x-forwarded-for")?.split(",")[0].trim() ?? "";
  const ipHash = ip ? await sha256(ip + (Deno.env.get("IP_SALT") ?? "")) : null;

  const db = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  const row = {
    name, contact, contact_kind: kind, message,
    lang: str(b.lang, 5) || null,
    path: str(b.path, 300) || null,
    utm_source: str(b.utm_source, 100) || null,
    utm_medium: str(b.utm_medium, 100) || null,
    utm_campaign: str(b.utm_campaign, 100) || null,
    session_id: str(b.session_id, 64) || null,
    ip_hash: ipHash,
  };

  const { error } = await db.from("leads").insert(row);
  if (error) {
    // Ограничение частоты приходит сюда как check_violation из триггера.
    const limited = (error.message || "").includes("rate limit");
    return json({ error: limited ? "rate" : "db" }, limited ? 429 : 500);
  }

  // Письмо. Заявка уже сохранена, поэтому падение почты не теряет её.
  const key = Deno.env.get("RESEND_API_KEY");
  if (key) {
    const esc = (s: string) =>
      s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    try {
      await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: { authorization: `Bearer ${key}`, "content-type": "application/json" },
        body: JSON.stringify({
          from: Deno.env.get("MAIL_FROM"),
          to: Deno.env.get("MAIL_TO"),
          reply_to: kind === "email" ? contact : undefined,
          subject: `Заявка с сайта — ${name}`,
          html:
            `<p><b>${esc(name)}</b> · ${esc(contact)} (${kind})</p>` +
            `<p style="white-space:pre-wrap">${esc(message)}</p>` +
            `<hr><p style="color:#666;font-size:13px">${esc(row.path ?? "")} · ${esc(row.lang ?? "")}` +
            ` · ${esc(row.utm_source ?? "прямой заход")}</p>`,
        }),
      });
    } catch { /* заявка в базе, дашборд её покажет */ }
  }

  return json({ ok: true });
});
