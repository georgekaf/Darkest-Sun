---
title: "Kharanok — Changelog"
tags: [kharanok, meta]
---

## v1.2 — Below Kharanok, MC2 pp119-130, Greek Arena

**New location: Below Kharanok**
- `Hidden/Kharanok- The Altar of Dust/Below Kharanok/01. Obsidian Mines AKA The Cannibal Caves/` — full location with map images (cave grid/no-grid, water overlay, POI visual guide, 12 numbered points of interest)
- North Entrance, River Walk, Bridge Crossing, Main Excavation, West Galleries, Deep Lake, Lower Pools, Foreman's Office, Barracks, Storehouse, Workshop, South Access Shaft

**New books: 28 Dark Sun novels/expansions**
- `Hidden/Books/` — Air Earth Fire Water, Arcane Shadows, Asticlian Gambit, Beyond the Prism Pentad, Black Flames, Black Spine, City State of Tyr, Dark Sun Box Set Original, Defilers and Preservers, Dragon Kings, Dragon's Crown, Dune Trader, Elves of Athas, Forest Maker, Freedom, Marauders of Nibenay, Merchant House of Amketch, Mind Lords of the Last Sea, Monstrous Compendium Appendix II, Psionic Artifacts of Athas, Road to Urik, Slave Tribes, The Complete Gladiator's Handbook, The Ivory Triangle, The Will and the Way, Thri-Kreen of Athas, Valley of Dust and Fire, Veiled Alliance, Windriders of the Jagged Cliffs

**Monstrous Compendium II expanded**
- pp119-130: t'liz undead (Nevarli, Kedomir), Athasian wraith (Nikolos, Crimson Knights), xerichous, thinking zombie (Evirdel Ironhand, Claktor Bloodfist, Beli Iton, Levgar Giantslayer), special undead powers & weaknesses tables

**NPC fixes**
- `Elder Yethras.md`: Half-elf → Human
- `Jessix the Wanderer.md`: Added `- [City by the silt sea]` subtitle
- `Dorak.md`: Removed stray blank line after frontmatter

**Greek**
- `greek/Kharanok- The Altar of Dust/Quests/Πλαινό - Η Αρένα.md` — new Greek quest file (Arena)

**Housekeeping**
- `Classes/Ranger.md`: Trailing newline fix
- `Hidden/Books/OSE_Players_Guide.md`: Blank line fix
- Deleted stale `Untitled.md`

---

## v1.1 — LegendKeeper JSON Sync

**Source:** `Darkest Sun.json` exported 2026-06-05 (exportId `j53w7j70`, 148 resources)

**Script:** `json_to_obsidian.py` — full rewrite; handles ProseMirror nodes: `paragraph`, `heading`, `rule`, `bulletList`, `orderedList`, `listItem`, `blockquote`, `panel` (→ Obsidian callout), `table` (with header separator), `taskList` (→ `- [ ]`/`- [x]`), `mediaSingle`/`media` (→ image embed), `mention` (→ plain text), `layoutSection`/`layoutColumn` (transparent), `bodiedExtension` (`block-secret` → callout), `extension`/`inlineExtension` (skipped). Marks: `strong`, `em`, `underline`.

**131 files written** across:

- `Journal/` — 26 session entries (01. FREEDOM → 25. Black Wind, Fire and Steel)
- `Classes/` — 11 class files (Druid, Fighter, Wizard, Ranger, Necromancer, etc.) + index
- `Rules/` — Hex Crawling, Food & Water, Conditions, Vision & Darkness, Luck Tokens, Poisons, Mounts, Misery, Downtime Activities, Downtime, Fast Travel, Shadowdark RPG, Βασικοί Όροι, Χαρακτήρες, Μάχη, Δημιουργία Χαρακτήρων, Defiling, Psionics, Ancestries + 8 ancestry files
- `The World/` — 17 lore files (Greek + English)
- `Map/` — 16 location files (city-states, forts, settlements)
- `Languages/` — Languages index + Halfling (Rhulka)
- `Kharanok- The Altar of Dust/` — 13 location pages
- `Campaign Map/` — 3 pages (Campaign Map, Misery & Sorrow, Ras'Godai Monastery)
- Root — Darkest Main, Timeline, Character - Soldier, Advancement, Πλάσματα της Ερήμου, 00. Welcome to Darkest Sun, Untitled

**Protected (untouched):** `NPCs/`, `Monsters/`, `Hidden/`, `greek/`

**Stale root files to delete** (superseded by subdirectory paths):
- `obsidian/Misery.md` → now `Rules/Misery.md`
- `obsidian/Mounts.md` → now `Rules/Mounts.md`
- `obsidian/Downtime Activities.md` → now `Rules/Downtime Activities.md`
- `obsidian/Old Quarry Yard.md` → now `Kharanok- The Altar of Dust/Old Quarry Yard.md`
- `obsidian/Journal/14. TRADERS OF ASSASSINS-.md` → now `Journal/14. TRADERS OF ASSASSINS.md`

---

## v1.0 — OSE GMG + Players Guide Continued Corrections

**`OSE_Game_Masters_Guide.md`** — additional pages fixed after v0.9:

- p37: Desert Giant + Plain Giant — `Wo Pio Bio Si2`→`W9 P10 B10 S12`, stat blocks reformatted bold
- p79: City Districts generator — heavy two-column merge resolved, all 4 district tables reformatted as markdown
- p85: Ruin Inhabitants + Unique Feature + Room Purpose — 3 tables fully rewritten

**`OSE_Players_Guide.md`** — corrections from PDF source:

- p4–5: Table of Contents — fully rewritten as structured markdown tables; heavy OCR garble (`cenier'`, `epee`, `PSIONICISE... cee seeeee`, `{Equipment`, `Vehiicles`) resolved
- p25: Bard Level Progression — garbled saving throw columns corrected, `nu`→`11`, `=9d.4+4*`→`9d4+4*`, `22[+7]`→`12[+7]`, `74`→`7d4`, `ist`→`1st`, "uth Level"→"11th Level"
- p49: Halfling Level Progression — all saving throw columns corrected, `746`→`7d6`, `wl+5]`→`14[+5]`, `YoU`→`11`, `4oUu`→`11`, garbled rows fixed
- p70: Poison table — fully rewritten; `id2`→`1d2`, `ad4`→`1d4`, `3dio`→`3d10`, `sdio`→`5d10`, `vet`→`+2`, `no`→`110`, `oo`→`700`

---

## v0.9 — OSE GMG Manual Page Corrections

**`OSE_Game_Masters_Guide.md`** — combined file restructured and pages rewritten from PDF source.

### ✅ Completed

**Structure (pages 1–4):**
- p1: Cover restored (`Game Master's Guide / By Lixu`)
- p2: Foreword + Credits reformatted
- p3: Table of Contents — fully rewritten as markdown tables, page numbers corrected, Appendix L → Appendix I
- p4: Chapter 1 divider — `Runnings dventures&SS` → `Chapter 1: Running Adventures`

**Special pages:**
- p12: Merchant's Calendar — entirely garbled; rewritten with calendar table (15 months/festivals), constellations, festival weeks
- p18: Chapter 3 divider restored
- p32: Full-page illustration noted (winged demon/beast)

**Monster pages (fully rewritten):**
- p21: Aarakokra + Anakore
- p22: Baazrag + Belgoi
- p23: Braxat + Brambleweed
- p24: Cactus + Sand Cactus *(B'rohg removed — page mismatch)*
- p25: Hunting Cactus + Spider Cactus
- p27: Cilop + Cistern Fiend
- p28: Cloud Ray + Cordlu
- p30: Air Drake + Earth Drake
- p31: Fire Drake + Water Drake
- p33: Dragon of Tyr
- p34: Dwarf + Dwarf Banshee
- p36: Gaj + Beasthead Giant
- p38: Gith + Half-Giant *(was mislabelled p36 by user)*
- p39: Halfling + Hej-kin
- p40: Id Fiend + Inix
- p41: Jozhal + Kank
- p42: Megapede + Mekillot
- p43: Mul + Nightmare Beast
- p44: Pterran + Pterrax
- p46: Pyreen
- p47: Razorwing + Sand Bride
- p49: Silt Runner + Athasian Sloth
- p50: So-ut + Crystal Spider
- p51: Ssurran + Syllk Wyrm
- p52: Tarek + Thri-kreen
- p53: Tohr-kreen + Thrax
- p54: Villichi + Zhackal
- p55: Misc. Monsters (Hurrum, Critic Lizard, Floater, Kes'trekel)

**Rules/generator pages:**
- p62: NPC Encounters — bullets fixed, tables reformatted
- p69: Magic items (fruits, oils, Ring of Animal Influence) — bullets and table artifacts fixed
- p77: City-state Generator — `~=©— Butte` resolved, all tables reformatted
- p82: Athasian Settlement Generator — fully rewritten as markdown tables
- p84: Ruin Generator — fully rewritten as markdown tables
- p88: Vegetation + Hydrography Generators — fully rewritten, duplicate heading corrected

**Recurring fixes on all rewritten pages:**
`Bis`→`B15`, `Sio`→`S10`, `Diz`/`Di2`→`D12`, `id[X]`→`1d[X]`, `ad[X]`→`2d[X]`, `NA o(N)`→`NA 0(N)`, `AC o[N]`→`AC 0[N]`, two-column merges resolved, stat blocks reformatted bold.

---

**Page footer numbers retained** — stray page numbers preserved throughout as reference anchors. Truncated footers corrected: p17 `7`→`17`, p58 `5`→`58`, p71 `1`→`71`, p73 `13`→`73`, p75 `15`→`75`, p78 `18`→`78`.

---

## v0.8 — Full OCR Pipeline Cleanup

**4 books processed** — per-page + `Hidden/Books/` combined files:

**`°`→`'` (feet symbols):** ~50 fixes across all books — distances, ranges, sizes, infravision, movement rates
**`°`→`-` (table dashes):** 7 fixes in OSE GMG (treasure, magic item, terrain tables)
**`¢`→`•` (bullet points):** 15 fixes in OSE PG (spell lists, feature lists)
**`¢p`/`c¢p`→`cp` (copper pieces):** 10 fixes in OSE PG (equipment, wages, hirelings tables)
**`o`→`0` / `l`/`I`→`1` (digit OCR):** `4o`→`40`, `dioo`→`d100`, `dl0`→`d10`, `1410`→`1d10`
**`@`→`a`/digit:** 5 fixes in MC2 (`@ baazrag`→`a baazrag`, `@'-4'`→`3'-4'`, etc.)
**Class table rewrites:** 13 pages in OSE PG — Fighter, Gladiator, Ranger, Thief, Cleric, Druid, Templar, Defiler, Preserver, Psionicist, Elf, Half-giant, Mul
**Full page rewrites:** MC2 Water Elemental Beasts (p42), Racked Spirit (p87); GMG Elf/Erdlu (p35)
**Border artifact cleanup:** 4 pages in MC2 — artifact lines deleted, sections rewritten clean

---

## v0.7 — OCR Typo Fixes

**`Hidden/Books/`** — OCR misreads corrected:

- `Monstrous_Compendium_II.md` — 25 fixes: `Id`→`1d`, `244`→`2d4`, `4dl0`→`4d10` across stat blocks
- `OSE_Players_Guide.md` — 2 fixes: `19l0]`→`19[0]`, `1I5¢P`→`15 cp`
- `Terrors_of_the_Desert.md` — 2 fixes: `ld6`→`1d6`, `Id12`→`1d12`

---

## v0.6 — Potions/Poisons Reference Compilations

**New root files** — poisons and potions from all book sources consolidated:
- `Poisons.md` — 13 craftable poisons (OSE Players Guide), 8 campaign poisons (Shadowdark), 26 monsters with poison/venom attacks (all books), poison classes A–J, delivery methods, antidotes
- `Potions.md` — 4 magic fruits, 2 oils, Tree of Life Sap, Life Sap variants, crafting rules, Protection from Poison spell

---

## v0.5 — Hidden Folder Reorganization

**New `Hidden/` folder** — reference material archived out of active vault:
- `Hidden/BookLocations/` — 61 English location files moved from `BookLocations/` (Giustenal, New Giustenal, Cromlin, Kragmorta, Sea of Silt, and 56 others)
- `Hidden/greek/BookLocations/` — ~60 Greek location file translations moved from `greek/BookLocations/`
- `Hidden/Books/` — all 7 book reference files moved from `Books/`
- `Hidden/Kharanok- The Altar of Dust/` — Kharanok location, NPC, and quest files mirrored into archive

**Line-ending normalization**
- CRLF → LF applied across `NPCs/`, `Monsters/`, and Greek NPC files (no content changes)

---

## v0.4 — Books Reference Folder

**New `Books/` folder** — 7 reference documents added to vault root:
- `City by the Silt Sea.md` — AD&D Dark Sun campaign expansion (TSR #2432), OCR'd from scan
- `City by the silt sea campaign book.md` — campaign book companion
- `Guide_to_Shadowdark_Monster_Statistics.md` — Shadowdark monster stat conversion guide
- `Monstrous_Compendium_II.md` — Dark Sun Monstrous Compendium Appendix II (TSR #02433)
- `OSE_Game_Masters_Guide.md` — OSE Dark Sun Game Masters Guide
- `OSE_Players_Guide.md` — OSE Dark Sun Players Guide
- `Terrors_of_the_Desert.md` — Dark Sun MC12 Appendix I: Terrors of the Desert (TSR #2405)

---

## v0.3 — Acts & Structure Tree

**Quest restructure**
- Renamed all quest files from "Set N" to "Act N" (`Set 1–6` → `Act 1–6`); updated `Kharanok Quest Chain.md` links accordingly
- Overview table now shows 3 hooks per act and a linear ASCII flow diagram
- Added `Structure Tree.md` — full visual ASCII tree of all 6 acts with hooks listed per node

**Fixes**
- Corrected `NPCs/Freiha.md` page reference: `p. 61` → `p. 84–85` (English + Greek)

---

## v0.2 — Greek Translation & Bidirectional Links

**NPC pages (Greek)**
- Created `greek/Kharanok- The Altar of Dust/NPCs/` with full translations of all 9 NPC files: Πρεσβύτης Γέθρας, Μπρεκ, Σίρα, Ντόρακ, Γέλκα, Όρεν, Τζέσικ ο Περιπλανώμενος, Μούουτον, Τζέσαρην
- Created `Συμβουλές Ρόλου.md` (Roleplay Tips translation)
- Sections translated: Ιστορικό, Ατζέντα, Επιθυμίες & Ανάγκες, Στόχοι, Σημειώσεις Ρόλου, Σχέσεις

**Quest pages (Greek)**
- Created `greek/Kharanok- The Altar of Dust/Quests/` with full translations of all 8 quest files:
  - Αλυσίδα Αποστολών Kharanok
  - Σετ 1 – Μάτια Ανοιχτά
  - Σετ 2 – Καθαρίστε το Βουνό
  - Σετ 3 – Ανοίξτε τους Δρόμους
  - Σετ 4 – Φέρτε τους Εμπόρους
  - Σετ 5 – Το Πρόβλημα του Νερού
  - Σετ 6 – Ταΐστε το Χωριό
  - Τελικό – Ανεφοδιασμός των Μαντριών

**Bidirectional links**
- Added `Ελληνικά:` links to all 9 English NPC files, Roleplay Tips, and all 8 English quest files
- Added `English:` back-links on all new Greek files
- Added `Kharanok:` links on global Greek NPC files (`greek/NPCs/Τζέσικ ο Περιπλανώμενος`, `Μούουτον`, `Τζέσαρην`)

---

## v0.1 — Initial Commit

**NPC pages (English)**
- Created `Kharanok- The Altar of Dust/NPCs/` with 9 NPC files: Elder Yethras, Breck, Sira, Dorak, Yelka, Oren, Jessix the Wanderer, Muuton, Jessareen
- Created `Roleplay Tips.md` with generic GM guidance for running Kharanok NPCs
- Each NPC file includes: Background, Agenda, Wants & Needs, Goals, Roleplay Notes, Relationships

**Quest links (English)**
- Added NPC wiki links throughout all 8 quest files (Kharanok Quest Chain + Sets 1–6 + Final)
- Local NPCs linked with short path; outsider NPCs (Jessix, Muuton, Jessareen) linked with full vault path to disambiguate from global NPC files
