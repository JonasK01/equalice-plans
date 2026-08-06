"""Module 2 — Creative-Pipeline: board by status, linked to influencers + briefs."""

import streamlit as st

from core import config, store
from core.models import (
    CreativeItem, CREATIVE_STATUS, FUNNEL_STAGES,
)


def render():
    st.header("🎬 Creative-Pipeline")
    items = store.list_creatives()
    influencers = store.list_influencers()
    inf_labels = ["—"] + [f"{i.name} ({i.slug})" for i in influencers]
    slug_by_label = {f"{i.name} ({i.slug})": i.slug for i in influencers}

    # --- board grouped by status ---
    cols = st.columns(len(CREATIVE_STATUS))
    for col, status in zip(cols, CREATIVE_STATUS):
        with col:
            group = [it for it in items if it.status == status]
            st.markdown(f"**{status}**  ·  {len(group)}")
            for it in group:
                flag = " 🚩" if it.compliance_flag else ""
                who = f"  ·  👤 {it.assigned_influencer_slug}" if it.assigned_influencer_slug else ""
                st.caption(f"{it.title}{flag}\n\n`{it.funnel_stage}`{who}")

    st.divider()

    # --- editor ---
    tab_edit, tab_new = st.tabs(["✏️ Bearbeiten", "➕ Neues Creative"])
    with tab_edit:
        if not items:
            st.info("Keine Creatives.")
        else:
            label_by_id = {f"{it.title} [{it.status}]": it.id for it in items}
            sel = st.selectbox("Creative", list(label_by_id.keys()))
            _edit_item(store.load_creative(label_by_id[sel]), inf_labels, slug_by_label)
    with tab_new:
        _new_item()


def _edit_item(it: CreativeItem, inf_labels, slug_by_label):
    cur_inf_label = next((lbl for lbl, slug in slug_by_label.items()
                          if slug == it.assigned_influencer_slug), "—")
    with st.form(f"edit_{it.id}"):
        c = st.columns(3)
        status = c[0].selectbox("Status", CREATIVE_STATUS,
                                index=CREATIVE_STATUS.index(it.status))
        stage = c[1].selectbox("Funnel", FUNNEL_STAGES,
                               index=FUNNEL_STAGES.index(it.funnel_stage)
                               if it.funnel_stage in FUNNEL_STAGES else 0)
        inf_label = c[2].selectbox("Influencer", inf_labels,
                                   index=inf_labels.index(cur_inf_label)
                                   if cur_inf_label in inf_labels else 0)
        c2 = st.columns(2)
        fmt = c2[0].text_input("Format", value=it.format)
        angle = c2[1].text_input("Angle", value=it.angle)

        st.markdown("**Live-Verknüpfung (ab Status 'Live')**")
        c3 = st.columns(3)
        live_campaign = c3[0].text_input("Campaign-ID", value=it.live_campaign_id)
        live_ad = c3[1].text_input("Ad-ID", value=it.live_ad_id)
        roas = c3[2].number_input("Ist-ROAS", min_value=0.0,
                                  value=float(it.result.get("roas", 0.0)), step=0.1)

        compliance_flag = st.checkbox("⚠️ Compliance-Risiko", value=it.compliance_flag)
        compliance_notes = st.text_input("Compliance-Notiz", value=it.compliance_notes)
        notes = st.text_area("Notizen", value=it.notes)
        if st.form_submit_button("💾 Speichern", type="primary"):
            it.status = status
            it.funnel_stage = stage
            it.assigned_influencer_slug = slug_by_label.get(inf_label, "")
            it.format = fmt
            it.angle = angle
            it.live_campaign_id = live_campaign
            it.live_ad_id = live_ad
            it.result = {**it.result, "roas": roas}
            it.compliance_flag = compliance_flag
            it.compliance_notes = compliance_notes
            it.notes = notes
            store.save_creative(it)
            st.success("Gespeichert.")
            st.rerun()

    if it.brief_ref and (config.TMP_DIR / it.brief_ref).exists():
        with st.expander("📄 Brief-Referenz"):
            st.markdown((config.TMP_DIR / it.brief_ref).read_text())
    if st.button("🗑️ Löschen", key=f"del_{it.id}"):
        store.delete_creative(it.id)
        st.rerun()


def _new_item():
    with st.form("new_creative", clear_on_submit=True):
        title = st.text_input("Titel *")
        c = st.columns(3)
        stage = c[0].selectbox("Funnel", FUNNEL_STAGES)
        status = c[1].selectbox("Status", CREATIVE_STATUS)
        fmt = c[2].text_input("Format", value="9:16 Reel")
        angle = st.text_input("Angle")
        notes = st.text_area("Notizen")
        if st.form_submit_button("➕ Anlegen", type="primary"):
            if not title.strip():
                st.error("Titel erforderlich.")
                return
            cid = store.slugify(title)
            if store.load_creative(cid):
                cid = f"{cid}-{len(store.list_creatives())+1}"
            store.save_creative(CreativeItem(
                id=cid, title=title.strip(), funnel_stage=stage, status=status,
                format=fmt, angle=angle, notes=notes))
            st.success(f"{title} angelegt.")
            st.rerun()
