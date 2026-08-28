-- ============================================================================
-- GANZA CONSULTING — analytics schema for Supabase (PostgreSQL)
--
-- Run this ONCE in Supabase → SQL Editor → New query → Run.
-- It creates: the events table, security rules, indexes, reporting views
-- and a retention function.
--
-- Security model
--   * the website writes with the public anon key and can ONLY insert
--   * nobody can read with the anon key — reading requires a logged-in user
--   * no cookies, no personal data, no cross-site identifiers are stored
-- ============================================================================

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------------------
-- 1. TABLE
-- ---------------------------------------------------------------------------
create table if not exists public.events (
  id            bigint generated always as identity primary key,
  ts            timestamptz  not null default now(),
  event         text         not null,
  visitor_id    uuid         not null,   -- stable per browser (localStorage)
  session_id    uuid         not null,   -- resets after 30 min of inactivity
  path          text,                    -- e.g. /blog/when-not-to-automate/
  lang          text,                    -- en | ru
  page_type     text,                    -- home | blog-index | article | other
  title         text,
  referrer      text,
  referrer_host text,
  utm_source    text,
  utm_medium    text,
  utm_campaign  text,
  device        text,                    -- mobile | tablet | desktop
  os            text,
  browser       text,
  viewport_w    int,
  viewport_h    int,
  target        text,                    -- what was clicked / which section
  target_href   text,
  section       text,                    -- nearest section id
  value         numeric,                 -- scroll %, seconds, step number
  seq           int,                     -- position of the page in the session
  meta          jsonb,

  -- guardrails: the anon key is public, so keep rows small and well-formed
  constraint events_event_ck check (event = any (array[
    'page_view','click','outbound','scroll','section','engagement',
    'lang_switch','builder','cta','error'
  ])),
  constraint events_len_ck check (
    coalesce(length(path),0)        <= 300 and
    coalesce(length(title),0)       <= 300 and
    coalesce(length(referrer),0)    <= 500 and
    coalesce(length(target),0)      <= 200 and
    coalesce(length(target_href),0) <= 500 and
    coalesce(length(section),0)     <= 100
  ),
  constraint events_ts_ck check (ts > now() - interval '1 day' and ts < now() + interval '1 hour')
);

comment on table public.events is
  'Raw first-party analytics events written by js/analytics.js. Insert-only for anon.';

-- ---------------------------------------------------------------------------
-- 2. INDEXES
-- ---------------------------------------------------------------------------
create index if not exists events_ts_idx        on public.events (ts desc);
create index if not exists events_event_ts_idx  on public.events (event, ts desc);
create index if not exists events_session_idx   on public.events (session_id, ts);
create index if not exists events_path_idx      on public.events (path, ts desc);
create index if not exists events_visitor_idx   on public.events (visitor_id);

-- ---------------------------------------------------------------------------
-- 3. ROW LEVEL SECURITY
-- ---------------------------------------------------------------------------
alter table public.events enable row level security;

drop policy if exists "anon can insert events"      on public.events;
drop policy if exists "authenticated can read"      on public.events;

-- the site may write ...
create policy "anon can insert events"
  on public.events for insert
  to anon, authenticated
  with check (true);

-- ... but only a signed-in user may read
create policy "authenticated can read"
  on public.events for select
  to authenticated
  using (true);

-- ---------------------------------------------------------------------------
-- 4. REPORTING VIEWS
--    security_invoker = on  →  the RLS policies above still apply, so these
--    views are readable only by a signed-in user, never with the anon key.
-- ---------------------------------------------------------------------------

-- 4.1 One row per visit: entry, exit, length, depth --------------------------
create or replace view public.v_sessions with (security_invoker = on) as
with base as (
  select
    session_id,
    min(visitor_id::text)::uuid                                as visitor_id,
    min(ts)                                                    as started_at,
    max(ts)                                                    as ended_at,
    extract(epoch from (max(ts) - min(ts)))::int               as duration_sec,
    count(*) filter (where event = 'page_view')                as pageviews,
    count(*) filter (where event = 'click')                    as clicks,
    count(*) filter (where event = 'outbound')                 as outbound_clicks,
    coalesce(sum(value) filter (where event = 'engagement'),0)::int as engaged_sec,
    max(value) filter (where event = 'scroll')                 as max_scroll,
    min(lang)                                                  as lang,
    min(device)                                                as device,
    min(referrer_host)                                         as referrer_host,
    min(utm_source)                                            as utm_source,
    min(utm_medium)                                            as utm_medium,
    min(utm_campaign)                                          as utm_campaign
  from public.events
  group by session_id
),
edges as (
  select distinct on (session_id) session_id, path as entry_path
  from public.events where event = 'page_view' order by session_id, ts asc
),
exits as (
  select distinct on (session_id) session_id, path as exit_path
  from public.events where event = 'page_view' order by session_id, ts desc
)
select b.*, e.entry_path, x.exit_path,
       (b.pageviews <= 1 and b.engaged_sec < 15) as is_bounce
from base b
left join edges e using (session_id)
left join exits x using (session_id);

-- 4.2 Daily traffic ----------------------------------------------------------
create or replace view public.v_daily with (security_invoker = on) as
select
  date_trunc('day', started_at)::date          as day,
  count(*)                                     as sessions,
  count(distinct visitor_id)                   as visitors,
  sum(pageviews)                               as pageviews,
  round(avg(engaged_sec))                      as avg_engaged_sec,
  round(100.0 * count(*) filter (where is_bounce) / nullif(count(*),0), 1) as bounce_pct
from public.v_sessions
group by 1
order by 1 desc;

-- 4.3 Page performance -------------------------------------------------------
create or replace view public.v_pages with (security_invoker = on) as
select
  e.path,
  min(e.lang)                                                          as lang,
  min(e.page_type)                                                     as page_type,
  count(*) filter (where e.event = 'page_view')                        as pageviews,
  count(distinct e.session_id) filter (where e.event = 'page_view')    as sessions,
  round(avg(e.value) filter (where e.event = 'engagement'))            as avg_engaged_sec,
  round(avg(e.value) filter (where e.event = 'scroll'))                as avg_scroll_pct,
  count(*) filter (where e.event = 'click')                            as clicks
from public.events e
where e.path is not null
group by e.path
order by pageviews desc;

-- 4.4 What gets clicked ------------------------------------------------------
create or replace view public.v_clicks with (security_invoker = on) as
select
  coalesce(target, target_href, '(unlabelled)') as target,
  target_href,
  path,
  section,
  count(*)                     as clicks,
  count(distinct session_id)   as sessions,
  max(ts)                      as last_click
from public.events
where event in ('click','outbound','cta')
group by 1,2,3,4
order by clicks desc;

-- 4.5 How far people scroll (where they stop) --------------------------------
create or replace view public.v_scroll with (security_invoker = on) as
select
  path,
  count(*) filter (where value >= 25)  as reached_25,
  count(*) filter (where value >= 50)  as reached_50,
  count(*) filter (where value >= 75)  as reached_75,
  count(*) filter (where value >= 100) as reached_100,
  count(distinct session_id)           as sessions
from public.events
where event = 'scroll'
group by path
order by sessions desc;

-- 4.6 Time spent per section (where attention actually goes) -----------------
create or replace view public.v_sections with (security_invoker = on) as
select
  path,
  section,
  count(*)                  as views,
  round(avg(value))         as avg_seconds,
  round(sum(value))         as total_seconds
from public.events
where event = 'section' and section is not null
group by path, section
order by total_seconds desc;

-- 4.7 Movement through the site: from → to -----------------------------------
create or replace view public.v_flow with (security_invoker = on) as
with pv as (
  select session_id, ts, path,
         lead(path) over (partition by session_id order by ts) as next_path
  from public.events
  where event = 'page_view'
)
select
  path                          as from_path,
  coalesce(next_path,'(exit)')  as to_path,
  count(*)                      as transitions,
  count(distinct session_id)    as sessions
from pv
group by 1,2
order by transitions desc;

-- 4.8 Where sessions end -----------------------------------------------------
create or replace view public.v_exits with (security_invoker = on) as
select exit_path as path,
       count(*)                                                        as exits,
       round(100.0*count(*)/nullif((select count(*) from public.v_sessions),0),1) as pct_of_sessions
from public.v_sessions
where exit_path is not null
group by exit_path
order by exits desc;

-- 4.9 Traffic sources --------------------------------------------------------
create or replace view public.v_sources with (security_invoker = on) as
select
  coalesce(nullif(utm_source,''), nullif(referrer_host,''), '(direct)') as source,
  coalesce(nullif(utm_medium,''), 'referral')                           as medium,
  utm_campaign                                                          as campaign,
  count(*)                                                              as sessions,
  round(avg(engaged_sec))                                               as avg_engaged_sec,
  round(100.0*count(*) filter (where is_bounce)/nullif(count(*),0),1)   as bounce_pct
from public.v_sessions
group by 1,2,3
order by sessions desc;

-- 4.10 Project-builder funnel + contact CTAs ---------------------------------
create or replace view public.v_funnel with (security_invoker = on) as
select
  event,
  coalesce(target,'(none)')   as step,
  count(*)                    as hits,
  count(distinct session_id)  as sessions
from public.events
where event in ('builder','cta','outbound')
group by 1,2
order by sessions desc;

-- ---------------------------------------------------------------------------
-- 5. RETENTION — keeps the free tier (500 MB) comfortable
--    Call manually, or schedule with pg_cron if it is enabled on your project:
--      select cron.schedule('prune-events','0 3 * * *','select public.prune_events(180)');
-- ---------------------------------------------------------------------------
create or replace function public.prune_events(keep_days int default 180)
returns bigint
language plpgsql
security definer
set search_path = public
as $$
declare removed bigint;
begin
  delete from public.events where ts < now() - make_interval(days => keep_days);
  get diagnostics removed = row_count;
  return removed;
end;
$$;

revoke all on function public.prune_events(int) from public, anon;
grant execute on function public.prune_events(int) to authenticated;

-- ---------------------------------------------------------------------------
-- 6. GRANTS
-- ---------------------------------------------------------------------------
grant insert on public.events to anon, authenticated;
grant select on public.events to authenticated;
grant select on
  public.v_sessions, public.v_daily, public.v_pages, public.v_clicks,
  public.v_scroll, public.v_sections, public.v_flow, public.v_exits,
  public.v_sources, public.v_funnel
  to authenticated;

-- ============================================================================
-- READY-MADE QUERIES (paste into SQL Editor, or save as a Supabase Report
-- chart: Reports → New report → add block → SQL)
-- ============================================================================
-- Traffic, last 30 days:
--   select * from v_daily where day > current_date - 30 order by day;
--
-- Best-performing articles:
--   select path, pageviews, sessions, avg_engaged_sec, avg_scroll_pct
--   from v_pages where page_type = 'article' order by pageviews desc limit 20;
--
-- What people actually click:
--   select target, target_href, clicks, sessions from v_clicks limit 30;
--
-- Where people stop reading a given article:
--   select * from v_scroll where path like '/blog/%' order by sessions desc;
--
-- Attention by section on the landing page:
--   select section, views, avg_seconds from v_sections where path = '/' order by total_seconds desc;
--
-- Movement through the site:
--   select from_path, to_path, transitions from v_flow order by transitions desc limit 40;
--
-- Sessions that reached Telegram:
--   select count(distinct session_id) from events where event = 'outbound' and target_href like '%t.me%';
