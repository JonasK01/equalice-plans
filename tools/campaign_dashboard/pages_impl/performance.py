"""Module 1 — Live Ad-Performance + gated budget editing."""

import pandas as pd
import streamlit as st

from core import config, store, meta_api


@st.cache_data(ttl=300, show_spinner=False)
def _accounts():
    return meta_api.list_accounts()


@st.cache_data(ttl=180, show_spinner=False)
def _account_insights(account_id, preset):
    rows = meta_api.insights(account_id, date_preset=preset, level="account")
    return meta_api.summarise(rows[0]) if rows else None


@st.cache_data(ttl=180, show_spinner=False)
def _campaign_insights(account_id, preset):
    rows = meta_api.insights(account_id, date_preset=preset, level="campaign")
    return [meta_api.summarise(r) for r in rows]


@st.cache_data(ttl=180, show_spinner=False)
def _daily(account_id, preset):
    rows = meta_api.insights(account_id, date_preset=preset, level="account",
                             time_increment=1)
    return [meta_api.summarise(r) for r in rows]


@st.cache_data(ttl=300, show_spinner=False)
def _campaigns(account_id):
    return meta_api.campaigns(account_id)


PRESETS = {
    "Gestern": "yesterday",
    "Letzte 7 Tage": "last_7d",
    "Letzte 14 Tage": "last_14d",
    "Letzte 30 Tage": "last_30d",
}


def render():
    st.header("📈 Performance & Budget-Pacing")
    settings = store.load_settings()

    # --- account + period pickers ---
    try:
        accounts = _accounts()
    except Exception as e:
        st.error(f"Meta-API nicht erreichbar: {e}")
        return

    acc_options = {f"{a.get('name','?')}  ({a['id']})": a["id"] for a in accounts}
    default_label = next((lbl for lbl, aid in acc_options.items()
                          if aid == settings["account_id"]), None)
    c1, c2 = st.columns([3, 2])
    with c1:
        label = st.selectbox("Ad-Account", list(acc_options.keys()),
                             index=list(acc_options.keys()).index(default_label)
                             if default_label else 0)
        account_id = acc_options[label]
    with c2:
        period = st.selectbox("Zeitraum", list(PRESETS.keys()), index=3)
    preset = PRESETS[period]

    if account_id != settings["account_id"]:
        settings["account_id"] = account_id
        store.save_settings(settings)

    # --- KPI cards ---
    summary = _account_insights(account_id, preset)
    if not summary:
        st.info("Keine Insights-Daten in diesem Zeitraum.")
    else:
        cur = summary["currency"]
        k = st.columns(5)
        k[0].metric("Spend", f"{summary['spend']:,.0f} {cur}")
        k[1].metric("Umsatz", f"{summary['revenue']:,.0f} {cur}")
        k[2].metric("ROAS", f"{summary['roas']:.2f}")
        k[3].metric("Käufe", f"{summary['purchases']:,}")
        k[4].metric("CTR", f"{summary['ctr']:.2f}%")

    # --- daily trend ---
    daily = _daily(account_id, preset)
    if daily:
        df = pd.DataFrame(daily).sort_values("date_start")
        df = df.set_index("date_start")
        st.subheader("Verlauf")
        t1, t2 = st.columns(2)
        with t1:
            st.caption("Spend / Tag")
            st.bar_chart(df["spend"])
        with t2:
            st.caption("ROAS / Tag")
            st.line_chart(df["roas"])

    # --- campaign table ---
    st.subheader("Kampagnen")
    camps = _campaign_insights(account_id, preset)
    if camps:
        cdf = pd.DataFrame(camps).sort_values("spend", ascending=False)
        cdf = cdf[["name", "spend", "revenue", "roas", "purchases",
                   "ctr", "cpc", "cpa"]]
        st.dataframe(cdf, width='stretch', hide_index=True)
    else:
        st.caption("Keine aktiven Kampagnen mit Spend im Zeitraum.")

    # --- gated budget editing ---
    _budget_editor(account_id, settings)

    _context_panels()


def _budget_editor(account_id, settings):
    st.subheader("💰 Budget anpassen")
    st.caption("Schreibt live ins Meta-Konto — nur nach ausdrücklicher Bestätigung.")
    try:
        live = [c for c in _campaigns(account_id)
                if c.get("effective_status") == "ACTIVE" and c.get("daily_budget")]
    except Exception as e:
        st.warning(f"Kampagnen-Budgets nicht ladbar: {e}")
        return
    if not live:
        st.caption("Keine aktiven Kampagnen mit Tagesbudget.")
        return

    opts = {f"{c['name']}  (${int(c['daily_budget'])/100:,.0f}/Tag)": c
            for c in live}
    sel = st.selectbox("Kampagne", list(opts.keys()))
    camp = opts[sel]
    cur_daily = int(camp["daily_budget"]) / 100

    col1, col2 = st.columns(2)
    with col1:
        new_daily = st.number_input("Neues Tagesbudget ($)", min_value=1.0,
                                    value=float(round(cur_daily)), step=5.0)
    with col2:
        pct = (new_daily - cur_daily) / cur_daily * 100 if cur_daily else 0
        st.metric("Änderung", f"{new_daily:,.0f} $",
                  delta=f"{pct:+.0f}%")
    if pct > 30:
        st.warning("⚠️ >30 % auf einmal kann die Kampagne in die Learning Phase "
                   "zurückwerfen (ROAS-Dip).")

    confirm = st.checkbox("Ich bestätige die Live-Budget-Änderung")
    if st.button("Budget anwenden", type="primary", disabled=not confirm):
        try:
            after = meta_api.set_daily_budget(camp["id"], new_daily)
            applied = int(after.get("daily_budget", 0)) / 100
            store.append_audit({
                "account_id": account_id, "campaign_id": camp["id"],
                "campaign_name": camp["name"], "from": cur_daily, "to": applied,
            })
            _campaigns.clear()
            st.success(f"✅ Budget gesetzt: {cur_daily:,.0f} → {applied:,.0f} $/Tag")
        except Exception as e:
            st.error(f"Fehlgeschlagen: {e}")

    log = store.list_audit()
    if log:
        with st.expander(f"Audit-Log ({len(log)} Änderungen)"):
            st.dataframe(pd.DataFrame(log[::-1]), width='stretch',
                         hide_index=True)


def _context_panels():
    with st.expander("📋 Persona & Learnings (Kontext)"):
        for label, path in [("Buyer-Persona", config.PERSONA_MD),
                            ("Meta-Learnings", config.LEARNINGS_MD)]:
            if path.exists():
                st.markdown(f"### {label}")
                st.markdown(path.read_text())
