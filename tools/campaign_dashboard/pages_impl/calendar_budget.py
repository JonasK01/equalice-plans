"""Module 4 — Content-Kalender + Budget-Pacing."""

import pandas as pd
import streamlit as st

from core import store, meta_api
from core.models import CalendarEvent, EVENT_TYPES, EVENT_STATUS


@st.cache_data(ttl=180, show_spinner=False)
def _daily_spend(account_id, preset):
    rows = meta_api.insights(account_id, date_preset=preset, level="account",
                             time_increment=1)
    return [meta_api.summarise(r) for r in rows]


def render():
    st.header("🗓️ Content-Kalender & Budget-Pacing")
    tab_cal, tab_pace = st.tabs(["🗓️ Kalender", "💵 Budget-Pacing"])
    with tab_cal:
        _calendar()
    with tab_pace:
        _pacing()


def _calendar():
    events = sorted(store.list_events(), key=lambda e: e.date)
    creatives = store.list_creatives()
    influencers = store.list_influencers()
    cr_opts = ["—"] + [c.id for c in creatives]
    inf_opts = ["—"] + [i.slug for i in influencers]

    if events:
        df = pd.DataFrame([{
            "Datum": e.date, "Titel": e.title, "Typ": e.type,
            "Status": e.status, "Creative": e.creative_id or "—",
            "Influencer": e.influencer_slug or "—",
        } for e in events])
        st.dataframe(df, width='stretch', hide_index=True)
    else:
        st.info("Noch keine Events.")

    with st.expander("➕ Event anlegen"):
        with st.form("new_event", clear_on_submit=True):
            c = st.columns(3)
            date = c[0].date_input("Datum")
            etype = c[1].selectbox("Typ", EVENT_TYPES)
            estatus = c[2].selectbox("Status", EVENT_STATUS)
            title = st.text_input("Titel *")
            c2 = st.columns(2)
            creative_id = c2[0].selectbox("Creative", cr_opts)
            influencer_slug = c2[1].selectbox("Influencer", inf_opts)
            notes = st.text_area("Notizen")
            if st.form_submit_button("➕ Anlegen", type="primary"):
                if not title.strip():
                    st.error("Titel erforderlich.")
                else:
                    eid = store.slugify(f"{date}-{title}")
                    store.upsert_event(CalendarEvent(
                        id=eid, date=str(date), title=title.strip(), type=etype,
                        status=estatus,
                        creative_id="" if creative_id == "—" else creative_id,
                        influencer_slug="" if influencer_slug == "—" else influencer_slug,
                        notes=notes))
                    st.success("Event angelegt.")
                    st.rerun()

    if events:
        del_id = st.selectbox("Event löschen", ["—"] + [e.id for e in events])
        if del_id != "—" and st.button("🗑️ Löschen"):
            store.delete_event(del_id)
            st.rerun()


def _pacing():
    settings = store.load_settings()
    account_id = settings["account_id"]
    st.caption(f"Account: `{account_id}`")

    try:
        daily = _daily_spend(account_id, "last_30d")
    except Exception as e:
        st.error(f"Meta-API nicht erreichbar: {e}")
        return
    if not daily:
        st.info("Keine Spend-Daten.")
        return

    df = pd.DataFrame(daily).sort_values("date_start")
    df["kumuliert"] = df["spend"].cumsum()
    total = df["spend"].sum()

    monthly_target = st.number_input("Monats-Budget-Ziel ($)", min_value=0.0,
                                     value=float(settings.get("budget_targets", {})
                                                 .get(account_id, round(total))),
                                     step=500.0)
    bt = settings.get("budget_targets", {})
    if bt.get(account_id) != monthly_target:
        bt[account_id] = monthly_target
        settings["budget_targets"] = bt
        store.save_settings(settings)

    c = st.columns(3)
    c[0].metric("Spend 30 Tage", f"{total:,.0f} $")
    c[1].metric("Ziel", f"{monthly_target:,.0f} $")
    pace = total / monthly_target * 100 if monthly_target else 0
    c[2].metric("Pacing", f"{pace:.0f}%",
                delta="über Ziel" if pace > 100 else "im Ziel")

    chart_df = df.set_index("date_start")[["spend", "kumuliert"]]
    st.caption("Täglicher Spend")
    st.bar_chart(chart_df["spend"])
    st.caption("Kumulierter Spend (vs. Ziel-Linie gedanklich)")
    st.line_chart(chart_df["kumuliert"])
