"""Module 3 — Influencer-CRM: roster, contract/script/product tracking, capacity."""

import math

import pandas as pd
import streamlit as st

from core import store
from core.models import (
    Influencer, Deliverable, INFLUENCER_STATUS, INFLUENCER_TIERS, FEE_MODELS,
    SCRIPT_STATUS, PRODUCT_STATUS, DELIVERABLE_STATUS,
)


def render():
    st.header("🤝 Influencer-CRM")
    roster = store.list_influencers()

    _capacity_widget(roster)
    st.divider()

    tab_roster, tab_edit = st.tabs(["📋 Roster", "➕ Anlegen / Bearbeiten"])
    with tab_roster:
        _roster_table(roster)
    with tab_edit:
        _editor(roster)


def _capacity_widget(roster):
    settings = store.load_settings()
    st.subheader("Kapazität & Bedarf")
    c = st.columns(4)
    with c[0]:
        target = st.number_input("Ziel: Videos/Monat", min_value=0,
                                 value=int(settings["monthly_video_target"]), step=1)
    with c[1]:
        per_inf = st.number_input("Videos je Influencer/Monat", min_value=1,
                                  value=int(settings["videos_per_influencer_per_month"]),
                                  step=1)
    with c[2]:
        managed = st.number_input("Influencer je Manager", min_value=1,
                                  value=int(settings["managed_per_person"]), step=1)
    # persist if changed
    if (target != settings["monthly_video_target"]
            or per_inf != settings["videos_per_influencer_per_month"]
            or managed != settings["managed_per_person"]):
        settings.update(monthly_video_target=target,
                        videos_per_influencer_per_month=per_inf,
                        managed_per_person=managed)
        store.save_settings(settings)

    needed = math.ceil(target / per_inf) if per_inf else 0
    active = [i for i in roster if i.status in ("contracted", "active")]
    gap = max(0, needed - len(active))
    managers = math.ceil(len(active) / managed) if managed else 0

    with c[3]:
        st.metric("Benötigte Influencer", needed, delta=f"{-gap} Lücke" if gap else "gedeckt")

    m = st.columns(4)
    m[0].metric("Aktiv/unter Vertrag", len(active))
    m[1].metric("Lücke", gap)
    m[2].metric("Manager nötig", managers)
    # open management load
    open_scripts = sum(1 for i in active if i.script_status in ("needed", "drafted"))
    open_products = sum(1 for i in active if i.product_status in ("needed", "requested"))
    m[3].metric("Offene To-dos", open_scripts + open_products,
                help=f"{open_scripts} Skripte offen · {open_products} Produkt-Sendungen offen")


def _roster_table(roster):
    if not roster:
        st.info("Noch keine Influencer. Lege im Tab Anlegen/Bearbeiten welche an.")
        return
    f1, f2 = st.columns(2)
    status_filter = f1.multiselect("Status", INFLUENCER_STATUS, default=[])
    tier_filter = f2.multiselect("Tier", INFLUENCER_TIERS, default=[])

    rows = []
    for i in roster:
        if status_filter and i.status not in status_filter:
            continue
        if tier_filter and i.tier not in tier_filter:
            continue
        rows.append({
            "Name": i.name, "Tier": i.tier, "Status": i.status,
            "Fee": f"{i.fee:,.0f} ({i.fee_model})",
            "Skript": i.script_status, "Produkt": i.product_status,
            "Deliverables": len(i.deliverables),
            "Vertrag bis": i.contract_end or "—",
        })
    st.dataframe(pd.DataFrame(rows), width='stretch', hide_index=True)


def _editor(roster):
    by_slug = {f"{i.name} ({i.slug})": i.slug for i in roster}
    choice = st.selectbox("Bearbeiten oder neu", ["➕ Neuer Influencer"] + list(by_slug.keys()))
    existing = None if choice == "➕ Neuer Influencer" else store.load_influencer(by_slug[choice])

    with st.form("inf_form", clear_on_submit=False):
        name = st.text_input("Name *", value=existing.name if existing else "")
        c = st.columns(3)
        tier = c[0].selectbox("Tier", INFLUENCER_TIERS,
                              index=INFLUENCER_TIERS.index(existing.tier) if existing else 1)
        status = c[1].selectbox("Status", INFLUENCER_STATUS,
                                index=INFLUENCER_STATUS.index(existing.status) if existing else 0)
        contact = c[2].text_input("Kontakt (Mail/Agent)", value=existing.contact if existing else "")

        c2 = st.columns(3)
        ig = c2[0].text_input("Instagram URL",
                              value=existing.handles.get("instagram", "") if existing else "")
        tt = c2[1].text_input("TikTok URL",
                              value=existing.handles.get("tiktok", "") if existing else "")
        yt = c2[2].text_input("YouTube URL",
                              value=existing.handles.get("youtube", "") if existing else "")

        st.markdown("**Vertrag & Vergütung**")
        c3 = st.columns(4)
        fee = c3[0].number_input("Fee ($)", min_value=0.0,
                                 value=float(existing.fee) if existing else 0.0, step=50.0)
        fee_model = c3[1].selectbox("Modell", FEE_MODELS,
                                    index=FEE_MODELS.index(existing.fee_model) if existing else 0)
        cstart = c3[2].text_input("Vertrag von (YYYY-MM-DD)",
                                  value=existing.contract_start if existing else "")
        cend = c3[3].text_input("Vertrag bis (YYYY-MM-DD)",
                                value=existing.contract_end if existing else "")
        contract_link = st.text_input("Vertrags-Link",
                                      value=existing.contract_link if existing else "")

        st.markdown("**Skript & Produkt-Seeding**")
        c4 = st.columns(3)
        script_status = c4[0].selectbox("Skript-Status", SCRIPT_STATUS,
                                        index=SCRIPT_STATUS.index(existing.script_status) if existing else 0)
        product_status = c4[1].selectbox("Produkt-Status", PRODUCT_STATUS,
                                         index=PRODUCT_STATUS.index(existing.product_status) if existing else 0)
        product_tracking = c4[2].text_input("Tracking-Nr.",
                                            value=existing.product_tracking if existing else "")

        notes = st.text_area("Notizen", value=existing.notes if existing else "")
        submitted = st.form_submit_button("💾 Speichern", type="primary")

    if submitted:
        if not name.strip():
            st.error("Name ist erforderlich.")
            return
        slug = existing.slug if existing else store.slugify(name)
        handles = {k: v for k, v in
                   {"instagram": ig, "tiktok": tt, "youtube": yt}.items() if v}
        inf = Influencer(
            slug=slug, name=name.strip(), tier=tier, status=status,
            handles=handles, fee=fee, fee_model=fee_model,
            contract_start=cstart, contract_end=cend, contract_link=contract_link,
            deliverables=existing.deliverables if existing else [],
            script_status=script_status, product_status=product_status,
            product_tracking=product_tracking,
            linked_creative_ids=existing.linked_creative_ids if existing else [],
            contact=contact, notes=notes,
            created_at=existing.created_at if existing else "",
        )
        store.save_influencer(inf)
        st.success(f"✅ {name} gespeichert.")
        st.rerun()

    if existing:
        _deliverables_editor(existing)
        if st.button("🗑️ Influencer löschen"):
            store.delete_influencer(existing.slug)
            st.rerun()


def _deliverables_editor(inf):
    st.markdown("**Deliverables**")
    creatives = store.list_creatives()
    creative_opts = ["—"] + [c.id for c in creatives]
    if inf.deliverables:
        st.dataframe(pd.DataFrame(inf.deliverables), width='stretch',
                     hide_index=True)
    with st.form(f"deliv_{inf.slug}", clear_on_submit=True):
        d = st.columns(4)
        dtype = d[0].text_input("Typ", value="Reel")
        count = d[1].number_input("Anzahl", min_value=1, value=1)
        due = d[2].text_input("Fällig (YYYY-MM-DD)", value="")
        brief_ref = d[3].selectbox("Creative", creative_opts)
        dstatus = st.selectbox("Status", DELIVERABLE_STATUS)
        if st.form_submit_button("➕ Deliverable hinzufügen"):
            inf.deliverables.append(Deliverable(
                type=dtype, count=int(count), due_date=due, status=dstatus,
                brief_ref="" if brief_ref == "—" else brief_ref).__dict__)
            store.save_influencer(inf)
            st.rerun()
