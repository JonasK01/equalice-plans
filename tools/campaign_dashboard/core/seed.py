"""Seed the creative pipeline from the 5 HYDROSHIELD briefs.

Runs once: if no creatives exist yet, create the 5 items we authored in
.tmp/dr_denese_hydroshield_creative_briefs.md so the pipeline isn't empty.
"""

from __future__ import annotations

from . import store
from .models import CreativeItem

_BRIEF_REF = "dr_denese_hydroshield_creative_briefs.md"

_SEED = [
    dict(id="ad1-cream-stopped-working",
         title="Why Your Cream Stopped Working",
         angle="Problem-Solution / Authority", funnel_stage="TOF",
         format="9:16 Reel (Founder-Led)", status="Brief",
         notes="Skalier-Kandidat — baut auf dem Gewinner-Stil (Founder ROAS 3,0) auf."),
    dict(id="ad2-does-topical-absorb",
         title="Does Topical Even Absorb?",
         angle="Contrarian / Mechanismus", funnel_stage="Retargeting",
         format="9:16 Founder-Led", status="Brief",
         notes="Conversion-Fix für #1-Einwand (Kollagen absorbiert nicht); RT-ROAS 1,1."),
    dict(id="ad3-23-years",
         title="23 Years, Never Without It",
         angle="Social Proof / Story (Loyalty-UGC)", funnel_stage="MOF",
         format="9:16 / 4:5 UGC", status="Idea",
         notes="Echte Langzeit-Kundin; 223 Loyalitäts-Kommentare als Basis."),
    dict(id="ad4-crepey-arms-neck",
         title="Crepey Arms & Neck",
         angle="Problem-Solution (unterversorgt)", funnel_stage="TOF",
         format="9:16 Reel", status="Idea",
         notes="Frischer Angle, neue Audience. Body-Policy beachten (keine Closeups)."),
    dict(id="ad5-restock",
         title="Bring-Back / Restock",
         angle="Scarcity / Demand", funnel_stage="Retargeting",
         format="9:16 / 4:5 Static", status="Idea",
         notes="Reaktivierung — eingestellte Produkte = größter Frustpunkt."),
]


def seed_if_empty() -> bool:
    if store.list_creatives():
        return False
    for d in _SEED:
        store.save_creative(CreativeItem(brief_ref=_BRIEF_REF, **d))
    return True
