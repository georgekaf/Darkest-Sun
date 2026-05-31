---
title: "Kharanok — Changelog"
tags: [kharanok, meta]
---

## v0.9 — OSE GMG Manual Page Corrections *(in progress)*

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
- p44: Pterran + Pterrax

**Recurring fixes on all rewritten pages:**
`Bis`→`B15`, `Sio`→`S10`, `Diz`/`Di2`→`D12`, `id[X]`→`1d[X]`, `ad[X]`→`2d[X]`, `NA o(N)`→`NA 0(N)`, `AC o[N]`→`AC 0[N]`, two-column merges resolved, stat blocks reformatted bold.

---

### 🔲 Remaining — Monster pages (needs PDF text)

| Page | Monsters | Key issues |
|---|---|---|
| p40 | Id Fiend + Inix | `id6`, two-column merge, `$14` |
| p41 | Jozhal + Kank | `Diz`, `Bis` |
| p42 | Megapede + Mekillot | `ad6`×2 (= `2d6`) |
| p43 | Mul | `Di2 W313`, `Bis` |
| p46 | Pyreen | `AC o[20]` |
| p47 | Sand Bride | `AC o[20]` |
| p49 | Silt Runner + Athasian Sloth | `Diz`, `Sio`, `NA o(id4)` |
| p50 | So-ut + Crystal Spider | `Sio`, `Diz`, `Bis` |
| p51 | Ssurran + Sylk Wyrm | `ad6`, `Diz`, `Bis` |
| p52 | Tarek + Thri-kreen | `Di2 W123`, `Bis`, `idq4` |
| p53 | Tohr-kreen + Thrax | `NAi(id4)` |
| p54 | Villichi | `idq` |
| p55 | Floater + Kes'trekel | `AC o[11]` |

### 🔲 Remaining — Rules/generator pages (fixable without PDF)

| Page | Issue |
|---|---|
| p62 | `e@` bullets → `•`; `id3` in NPC table |
| p69 | `e@` bullets → `•`; `~—` table artifacts |
| p77 | `3 ~=©— Butte` — needs PDF |
| p82, p84, p88 | Standalone `id4`, `id6`, `id8_` in generator tables |

### 🔲 Remaining — Bare page number artifacts only (auto-fixable)

Pages: 10, 11, 14–17, 19, 20, 29, 37, 45, 48, 56, 58–61, 63, 65–68, 70–73, 75, 78–81, 83, 85–87, 89–93

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
