# GENIUS Kids & Teens — verified source notes

Sources: client "02" data dump (label artwork in `assets/`, listing) + manufacturer
site https://nutripur.com/ca/product/genius-kids-teens-capsules-chewables-tablets/
(fetched 2026-06). Use exact claim wording below — NPN-compliant.

## SKUs (Nutripur GENIUS Kids & Teens)
- **Chewables — 180 caps** · ASIN **B010FGTMPW** · amazon.ca · 45-day supply @ 4/day. (this folder)
- **Chewables — 90 caps** · same formula, smaller size (label art in `assets/labels_90caps/`).
- **Liquid — 114 ml orange** · ASIN **B00CORKASE** → separate product `../genius_liquid_114ml/`.

## Formula (minimal daily dose = 4 capsules) — confirmed on label panel
Wild fish oil (Thunnus alalunga, TG form) 1060 mg · Borage oil (20% GLA) 320 mg ·
Organic flax seed oil 200 mg · Soy lecithin 200.8 mg.
Providing: DHA 264 mg · EPA 52 mg · ALA 104 mg · GLA 64 mg · ARA 20 mg ·
Phosphatidylcholine 18 mg · Vitamin E 54 IU / 36.36 mg.

## Health Canada NPN 80001375 — approved claim wording (verbatim, safe to put on-image)
- "Helps support development and mental function in children such as memory, perception and problem solving capacities"
- "Helps in the management of Attention Deficit Disorder with or without Hyperactivity (ADD/ADHD)"
- "Helps improve concentration in children with ADD/ADHD"
- "Provides structural components for healthy brain and eyes"
- "Helps in the development of the nervous system"

## Differentiators / credentials
- Omega-3 in **natural triglyceride (TG) form** — enhanced absorption (no competitor leads with this).
- "Provides 90% of the essential fatty acids the brain needs."
- **IFOS 5/5 Star** (per-lot tested) · **Health Canada NPN** · **GMP** · **Made in Canada / Since 1989** · **PA-free borage oil** · molecularly distilled.
- **Alive Magazine Awards 2021–2025** (Silver/Bronze).
- Free from: artificial colours/flavours/sweeteners/preservatives, lactose, GMO, gluten, alcohol.
- Award-winning **organic orange** flavour; chew OR swallow.

## Dosing
Children 4+. Younger kids 4 caps/day; teens 6 caps/day. Can split AM/PM.

## Taglines / softer benefit angles (site)
"Support your child's focus, attention, and learning—naturally" · "Reach their full cognitive potential."
Also claimed: supports emotional balance, calms childhood anxieties, supports better recuperative sleep.

## Visual reality (from label photos in assets/)
White bottle, blue/teal GENIUS branding, bilingual EN/FR panels. NPN + IFOS + GMP +
Canada-leaf marks present on pack. Real bottle renders available in `assets/` — use these
as the hero product reference (don't invent a bottle).

## NEVER (brand + compliance)
No kid faces · no "cure/treat/prevent" · no "best/#1/guaranteed" · no competitor comparisons ·
no sugar/candy/gummy aesthetic · no cartoon mascots.

## Competitor main-image analysis (kids omega-3) — pulled via analyze_category_visuals.py
Sampled mains: Honibe Omega-3 Honey Gummies (B07LC3NKWG), KidStar Omega 3 (B0BJHHY19F),
Nordic Naturals Omega-3 Gummies (B01J4HBVJS). Images in `.tmp/competitor_images/`.

What the category does:
- All three are **gummies / candy format** (sugar). Two of three use **cartoon / illustrated kids**
  (KidStar astronauts, Nordic elf-kids); Honibe leans honey/candy aesthetic.
- NPN is present but **tiny**; nobody leads with the regulator credential.
- Nobody leads with **potency-per-dose** (mg DHA) or a **clinical / no-sugar** positioning.

White space Nutripur OWNS (use on the main/hero):
1. **Clinical-natural, no cartoon, no sugar** — the opposite of the gummy crowd (matches no-gos).
2. **Health Canada NPN as a visible hero badge** — nobody else does it.
3. **Potency**: 6 brain nutrients / 264 mg DHA (chewable) · 730 mg DHA per tsp (liquid) — dwarfs gummies.
4. **IFOS 5/5 + Made in Canada** credential stack.
=> Validates image plan #1's hero options (NPN badge + 6-nutrient stack + capsules shown).

Note: scraper works on amazon.com; amazon.ca returned HTTP 404 for the tested ASINs (those ASINs
aren't all live on .ca). For true .ca competitor mains we need .ca-live ASINs or a paid scrape API.
