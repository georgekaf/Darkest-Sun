---
title: "Kharanok — Changelog"
tags: [kharanok, meta]
---

## v1.26 — Prep 0007 Renamed to the Real Play Date

**`Hidden/Session prep/0007 - Session Prep 3-8-2026.md` → `Hidden/Session prep/0007 - Session Prep 7-8-2026.md`.** The session was prepped for 3 August and played on the 7th. The filename, the `title:` field and the H1 heading all now carry 7 Αυγούστου 2026, the date the game actually happened, and the "*Actually played on Friday, 7 August 2026.*" line under the calendar block was removed as redundant. Git records this as a delete plus an add of the new file.

**`transcripts and summaries/summary_rules.md` — the prep-file rule reversed.** The rule added alongside v1.24 said to keep the scheduled filename and note the real date at the top, which left prep files recording when play was *planned* instead of when it *occurred*. It now reads: if a session slips, rename the prep file, its `title:` and its heading to the real play date.

**`.obsidian/workspace.json`** — Obsidian UI state only (open panes and tabs), no content.

---

## v1.25 — Sylvar Canonical, The Loyal Filed as a Band, Two GM Truths Behind ad7

**Canonical spelling: Sylvar, not Silvar.** The ad7 newcomer's name is spelled **Sylvar** and was corrected everywhere it had already landed — the episode summary (17 places), the working transcript (12), `character_roster.md`, `session_schedule.md`, `Hidden/Session prep/0007`, and the v1.24 entry below. `fixes/silvar.json` was renamed to **`fixes/sylvar.json`** with its target updated, so the ASR variants «Σίλβαρ» / «Σίλβαν» / «Σίλβαρντ» now normalise to Sylvar on every future pass. Fixer re-run to idempotency; `repair_artifacts.py --dry-run` clean.

**The Loyal now file as a band.** The five followers were renamed to a shared prefix — `The Loyal - Varesh`, `- Nyrra`, `- Kethen`, `- Saelis`, `- Tharek` — across both the player-facing `NPCs/` pages and the `Hidden/Nominees/Actors/` sheets, with headings updated to match (`# The Loyal — Varesh`, `# Actor: The Loyal — Varesh`). `NPCs/The Loyal.md` links were repointed. **Jessix keeps his own name**: he leads the band, he is not filed inside it.

**`Hidden/Nominees/README.md` — Batch E added** under City by the Silt Sea, listing the five with the note that the source leaves them unnamed and that names, personalities, appearances and levels are campaign-original (Thief 6, Fighter 5, Preserver 5, all below Jessix). The batch total now reads **36 City by the Silt Sea actor nominees** — 31 from the source, 5 campaign-original.

**`Hidden/Session prep/0007` — two GM truths recorded**, both marked as unknown to the players:

- **The Caller in Darkness reached out to Ranni.** The voice on the far side of the gate, speaking as the childhood friend she lost to the sandstorms, was the Caller making contact — not a coincidence of proximity. Its warning and its accusation ("why did you leave me") are the Caller wearing a dead voice, which is what it does. This is also what the cave creature felt come through the gate: the thing that hunts people to replace its dead and sounds like the screaming of thousands.
- **One of the Loyal saw Ranni** in the moment before she teleported back — the shout of "JESSIX, SOMEONE IS HERE!" was that member calling their leader. Varesh is put forward as the natural candidate, being the band's scout, but the GM may assign it to whoever suits the next scene. The consequence holds either way: Jessix now knows something appeared inside the ruins out of nothing and vanished the same way, and the Loyal will be watching that spot when the party comes through.

The episode summary was deliberately **not** changed for either — both are GM-side and unconfirmed in play, and its Σημειώσεις already flag the shouted name as probably Jessix.

---

## v1.24 — ad7 «City by the Silt Sea», Teleport Gates Under Kharanok, Sylvar Joins, Prep 0007 Filled

**`transcripts and summaries/Περίληψη - ad7 - City by the Silt Sea.md` (new)** — the Altar of Dust session of Friday 7 August 2026, covering the whole of in-world **day 117** (Macro 27th · al-Dun-Du · eighth Or'Dom · Nar'Ai), verified against both calendars and continuous with ad6's closing line. Party: Relo, Shaka, Cypoul, Ranni and the newly arrived Sylvar. The session establishes three things that change the campaign's reach: a **hidden room under the Kharanok mines holding two hexagonal Gith gate-plates**, the **working mechanics of those gates** (10 handfuls of Crystal Dust to activate both ends, 5 per trip to keep one open, otherwise it transports once and dies), and the confirmed destination of the intact plate — **Giustenal**, reached and returned from by Ranni within minutes. Also recorded: Breck revealed as an old Veiled Alliance member carrying Sadira's request for support to House Markon; a cache of 30–40 leather scrolls read by Zephyr in Draxian; and a second contact from the cave creature, which now wears Kalia's form, rejects Relo's earlier offer, and warns that something came *through* the gate — a thing that hunts people to replace its dead and sounds like the screaming of thousands.

**`Hidden/Session prep/0007 - Session Prep 3-8-2026.md` — completed.** Done, Not done, Summary and Left to do filled from the finished summary; Goals left untouched as the record of what was planned. The real play date (7 August) is noted at the top rather than renaming the file. Standing failures carried forward explicitly: the 3 obsidian shards remain unsold for a third session, the Crystal Dust pond is still unharvested, and neither ad5 rumor lead was followed.

**`transcripts and summaries/npc_roster.md` — new "Altar of Dust / Kharanok" section.** The ad campaign's NPCs had no home in the roster and were scattered or absent. Now recorded: **Dorak** (last miner of Kharanok, ex-Gith slave, admits half the corpses in the canyon are his — and **deliberately teaches the new workers wrong** so nobody learns the craft and takes his job, marked as a permanent trait); **Breck**; **Tzala**; **Zephyr**; and **the cave creature**, which **has no gender** and is written in the neuter throughout, borrowing a different form each contact.

**`transcripts and summaries/character_roster.md` / `session_schedule.md`** — **Sylvar (DarkRhapsode)** added to the Altar of Dust group: elderly traveller out of Nibenay, druid by the abilities he uses, and the only halfling-speaker present, which makes him **Shaka's interpreter from ad7 on**. DarkRhapsode plays Altar of Dust only and appears in neither the House Markon nor the Dune Runners tables.

**Six new `fixes/*.json` rules** — `relo`, `dorak`, `kalia`, `tzala`, `silvar`, `sandbloom`. All boundary-anchored regex, census-checked against the whole corpus for Greek-word collisions before being applied; the fixer was re-run to idempotency and `repair_artifacts.py --dry-run` reports no artifacts. Four of these names had been passing through the pipeline untouched for six sessions.

**`transcripts and summaries/summary_rules.md` — eight new rules**, each from a correction made during this write-up rather than collected afterwards:

- **Transitional scenes are never dropped, not even for length** — the "how we got from A to B" is a scene, not filler, and the 400–700 word figure is a target, not a ceiling. Closing check added: for every pair of consecutive paragraphs, can you explain how the characters got from one to the next?
- **What was said and what was translated are not the same thing** — when a line passes through an interpreter, record both levels, never just the polite version as the speaker's words.
- **A momentary casting posture is not a lasting state** — eyes closed to reach for The Way, then walking normally, is not "walking with his eyes closed".
- **Short scene-breaking shouts get capitals** inside quotes («ΤΕΛΟΣ! ΣΤΑΜΑΤΗΣΤΕ!»), for real shouts only.
- **Colloquial one-word retorts** (κανόνισε, άσε μας) are written as meaning, not carried into indirect speech as words.
- **Crafting *threads* → «ίνες»**, never «κλωστή», which reads as sewing thread rather than a harvested resource.
- **User-confirmed permanent traits also go to `npc_roster.md`** when the subject is an NPC, including stated motives and gender rules.
- **Session prep files are written in English** (only the header date is Greek) and are filled in from the finished summary after each ad session.

**Source verification — the Ghodan tar pits.** *City by the Silt Sea*, Giustenal Environs → The Tar Mine, places Durex and Haltham Ghodan's operation **about two miles due south of Cromlin**, House Shom's trading village, with caravans to Cromlin twice a month. The ad7 party briefly placed the brothers at Giustenal and Dorak corrected them in play; the summary follows the book and its Σημειώσεις record that ad3's «πηγές έξω από το ερειπωμένο Giustenal» is an NPC statement by Roi that the source does not support. ad3 was left as written.

**`Hidden/Nominees/` — 101 new actor sheets**, taking the nominee set well beyond Kharanok. `README.md` was restructured to match, splitting Actors into campaign groups:

- **Black Spine (DSE2)** — the full NPC cast of the seven-adventure campaign, sourced from `Hidden/Books/Black Spine.md` and grouped by adventure: Tenpug's band (Tenpug, Raxxon, Arcus, Danya, Lynth, Roi, Sala and the rest, plus the three chieftains the source leaves unnamed), Cry Vengeance (Vakskra, Askai, Kalisore, Drak, Jacles), Zigath's Nest (Zigath, Haza, Toogo, Durdon, Tormar, the Hejkin Preserver), Yathazor's Square of Gurdek, and onward. Stat blocks are **Shadowdark**, with the printed 2e line preserved in each file under *Conversion note*. Several are updates to existing sandbox records rather than new actors — including **Raxxon**, whose spelling supersedes the printed "Rakskon", **Danya**, flagged campaign-divergent, and **Zigath**, flagged for an appearance conflict.
- **City by the Silt Sea / Giustenal** — Jessix the Wanderer, Jessareen, Slinnasia, the Caller in Darkness, Dregoth, the Lich-Queen, Durex and Haltham Ghodan, Captain Gaff, Abdaleem, Mon-Adderath, Taraskir the Lion, the Spirit of Kragmorta, Eevuu Silt Stalker, Guvaano Twilightcatcher and others.
- **`Hidden/Nominees/Actors/Kalia.md`** gained a *Current record in mk-sandbox* block — a read-only snapshot of `actors/kalia.json` (revision 3) at the top of the sheet, so every proposal in the file is legible as a change *against stated current values* rather than as free-floating text. mk-sandbox itself was not written to.
- **`_sandbox-comparison.md` and `check_against_sandbox.py`** now travel with the nominees, so a sheet claiming to update an existing actor can be checked against the real record before submission.

**The Loyal, named and statted.** The Campaign Book gives Jessix five followers and no names. Five campaign-original members now exist as both player-facing NPC pages and nominee actor sheets: **Varesh** (thief, scout), **Nyrra** (preserver), **Kethen** (thief), **Saelis** (preserver, youngest) and **Tharek** (fighter, skirmisher), each with appearance, manner, goals, relationships, GM-only secrets and a token-art prompt. Levels are set from what the band survived rather than from their youth — **Thief 6, Fighter 5, Preserver 5** — reasoned from two Giustenal expeditions (the first into Dregoth's templar chambers, the second the one that killed Slinnasia) and permanent work in a Danger 5 region, while staying below Jessix. Every file states plainly that the names are campaign-original and that the source leaves all five unnamed. `NPCs/The Loyal.md` now lists them.

**`Hidden/BookLocations/Giustenal Maps.md` + `Giustenal Maps/` (7 images)** — a GM-side index matching every Giustenal map on hand to the location page it serves, including a player handout with no keys or insets. The maps are fan cartography from athas.org, not the printed poster maps, and the page states the precedence rule outright: **where they disagree with the book, the book wins.** Originals stay in `athas.org/` with their own descriptions and image-generation prompts.

**Two continuity conflicts written up**, both reached through the mandatory cross-campaign pass and both pointed to from `Hidden/Pending Worldbuilding Issues.md`:

- **`Hidden/Vareth Continuity Conflict.md`** — Vareth stands in two campaigns on the same in-world day: at Zharvek with Altar of Dust in ad6, and in the Nibenay undercity with House Markon in s3 ep.20, both on day 116. **Resolved** (2026-08-05): the campaign leader ruled Agis teleported him, and no dates moved. Left open for the GM: how often Agis will do that, since it quietly collapses the distance between the two campaigns.
- **`Hidden/Dhojakt Continuity Conflict.md`** — mk-sandbox's `actor-dhojakt` credits his mother's spells (or the Pristine Tower) for his transformation; the GM at the table in s3 ep.20 said **Nibenay** did it and the mother resisted. **Open** (2026-08-06).

**`Rules/Identifying Magic Items.md` (new)**, linked from `Rules/Rules.md`.

**`The World/NPC Roster - WIP.md`** — Siemhouk's Greek phonetic gloss («Σιέμ Χουκ») dropped in favour of the Latin name alone, per the standing rule that established names keep their Latin form inside Greek text.

---

## v1.23 — Mind Seal, Breck Promoted to the Veiled Alliance, ad6 Human-Fix Merge, MK-Sandbox Viewer

**`Rules/Mind Seal.md` (new)** — a worn ward against the prying mind. While worn, the wearer's thoughts cannot be read and they can neither send nor receive telepathic messages; psionic creatures still sense that *something* is blocking them, so the wearer is concealed but not hidden — the seal announces its own presence. Linked from `Rules/Rules.md`.

**`Hidden/Nominees/Actors/Breck.md` — promoted to a senior Veiled Alliance member and restatted as a level 10 Fighter.** Kharanok's last gate guard is now the **Warden of the Kharanok chain**, the ranking Alliance figure east of Nibenay, under the veil-name **"Breck of the Open Gate"** — built in the naming style of the existing agents (Saren of the Dry Leaves, Melketh the Blind Seer, Hessan Under-the-Sack). Deliberately not a preserver: the faction's own doctrine opens with "protect preservers and those who shelter them" and calls for using "overlooked workers to move messages," so a veteran soldier with no arcane signature holding the only road in fits the doctrine better than another hidden wizard. Stat block benchmarked against Melketh, the existing *senior* handler at level 5 — Breck at level 10, AC 15, HP 62, two attacks, plus **Hold the Line** (DC 15 Strength to get past him in a gateway), which turns the character into a mechanic.

Nothing in the Confirmed Facts block changed; the promotion reframes what is already recorded rather than contradicting it. The ad1 refusal to let Relo pass becomes screening rather than stubbornness, and the dormant "corrupt former captain" hook becomes load-bearing — the captain was selling Alliance transits, which is why Breck wants him found and cannot be seen looking. All new material sits in secret goals, GM-Only Secrets and a sourced GM-revision entry.

*Continuity consequence recorded in the nominee's Proposed Developments, not applied:* `faction-veiled-alliance-nibenay` lists its presence as Nibenay, Kheth's Field, Black-Thread Hollow and Thornmouth — **Kharanok is not among them** — and no `actor-breck` record exists in `actors/`. Both live in MK-Sandbox, which was **not written to**. Also noted in the file: `actor-oren` and `actor-elder-yethras` are proposed ids, since those two are nominees themselves; `actor-melketh-blind-seer`, `actor-saren-dry-leaves` and the faction id resolve to real records.

**`transcripts and summaries/Περίληψη - ad6 - The Sand Also Rises.md` — human-fixed body merged** from `Downloads/ad6 - human fixed.txt`. Six of eight body paragraphs differed, amounting to five substantive edits plus one repeated name fix:

- **Relo, not Rello** — 8 occurrences in the body and one in the roster line. Every other Altar of Dust summary, `character_roster.md`, `player_characters.md` and MK-Sandbox (`actor-relo`) already used Relo; ad6 was the lone outlier.
- **Kanks** — the party returned **with** two kanks, instead of one. Previously written as returning *the two kanks the Gith were holding*, which is a different event.
- **The warning's direction reversed** — sent **to the Gith, from** the Cannibal King and Lord Parias, not *to* those two. Consistent with Relo later announcing himself an emissary of the Cannibal King.
- **Zharvek was spotted to the east**, not the north.
- **Relo, not Vareth**, fails to frighten the giant snake with projected mental images — Relo is the psion; Vareth casts Magic Missiles later in the same paragraph.
- **"άπoδο" dropped** from the snake's description; the word also carried a Latin `o` in place of a Greek `ο`.

The download was body text only, so the header, roster line, `## Περίληψη` heading and the full calendar line were preserved and the body transplanted beneath them. Two missing accents in the fixed text were repaired (`αντι` → `αντί`, `ανατολικα` → `ανατολικά`). Previous version kept alongside as `.bak`.

*Two of these corrections resolve standing contradictions with `Hidden/Session prep/0006`,* which already recorded 2 kank brought back alive and a Gith ultimatum sent — both of which the old summary text contradicted and the corrected text now agrees with.

**New: `tools/mk-sandbox-viewer.html`, `tools/mk-sandbox-viewer-bundled.html`, `tools/build-viewer.py`** — an offline reader for the read-only MK-Sandbox, built outside the vault. The bundled file carries all 597 records (518 json + 79 md) baked in, so it opens with no folder picking and no server. Renders records as prose rather than raw JSON, with a Tree and Raw view alongside. Cross-references resolve: all **1167** ids including the 676 defined inside parent records, entity names linked inside prose, path references, campaign-day numbers linked to that day's event bundle and report, and provenance tokens that nothing defines (`gm-input-*`) linked to a citation list. Twelve colour schemes including five drawn from `resources/faction-banner-prompts.md` (Nibenay, Kharanok, House Shom, Veiled Alliance, Silt Stalkers), a statistics panel, viewer history, back/forward navigation and `#path` deep links. `build-viewer.py --check` reports broken references without writing anything; MK-Sandbox is only ever read.

---

## v1.22 — Terrain Glossary

**`Rules/Hex Crawling.md` — new Terrain Glossary section**, with the region map (`Rules/tyr region and beyond.png`, copied into the vault) embedded as its source. Records the canonical terrain vocabulary from the map legend — 14 terrain types and 7 marker types — so our own maps use those names rather than invented synonyms. Spells out the distinction that keeps getting blurred: **Rocky Badlands** are sharp, broken terrain (gullies, twisting canyon mazes) ringing the feet of mountains, around Tyr, the Tablelands and the ranges; **Stony Barrens** are flat weathered bedrock shelves or hard-packed red earth, out in open desert away from mountains. Not interchangeable — badlands vertical and broken, barrens flat and hard.

*Two open items noted in the page rather than decided:* Stony Barrens has no travel-speed row (proposed as Gravel/Uneven, 2 miles/hour, pending a ruling), and the Terrain Key says "Sand Wastes" where the map legend says "Sandy Wastes" — the map spelling flagged as canonical but the table row left alone.

---

## v1.21 — ad6 GM Corrections, Salt Gathering Rules, ad7 Prep

A pass of GM corrections against ad6, the rules page one of them called for, and the next session's prep opened on the corrected timeline.

**`Rules/Salt Gathering.md` (new, draft)** — ad6 reached the Salt Sea and the party discussed harvesting salt, but there were no rules for it, so nothing happened. Proposed: 1 hour per character for 1 load on a **DC 12 CON** check, disadvantage during peak heat, DC 16 and half yield bare-handed; 1 load preserves one large creature's meat for 2 weeks against one day unsalted; shore salt is dirtier than inland-flat salt unless rinsed; open flats are highly visible, so roll wandering encounters as travelling rather than camped. **Marked draft pending GM approval** — the numbers are a proposal, not canon. Linked from `Rules/Rules.md`.

**ad6 timeline corrected** — the session runs **days 115–117**, not 114. Days 113 and 114 were downtime after ad5 (day 112). The party set out on the 115th; heat pinned them at Zharvek through all of the 116th, so they searched the ruins, left only in the evening, and marched back overnight, reaching Kharanok at dawn on the **117th**. The Done list in `0006` had the earth-spirit ambush recorded *before* the departure it followed — reordered to the actual sequence. Date line recomputed to Macro 25th / al-Qor-Keth.

**ad6 factual corrections:**
- **The oasis spirits' terms were refused.** Earlier drafts recorded a compromise being reached, with the party resting and drinking while Rhazek waited outside. No deal was struck — the offer was a means of getting the fire priest alone and close to the spirits, and the party turned it down and left. Downstream text that assumed they had rested there was removed.
- **No salt was gathered.** "Gathered salt to preserve meat" was an intention discussed, never an action performed.
- **House Markon, not "House Marku", and no causal claim.** The survivors report that Markon's people passed through earlier and that Gith trouble worsened after they left. They assert no connection between the two; the earlier phrasing had the caravan *triggering* the raid.
- **Rensort survivors are northeast, at Quel'Nash** — previously recorded as scattered south.

**`Hidden/Zharvek Continuity Conflict.md` reassessed** — the House Markon correction above materially strengthens the case that both campaigns describe one place. Each independently reports the same causal chain: House Markon visits Zharvek → Gith trouble escalates after they leave. The Markon sessions show that escalation as a live, unexplained mystery (Talek Vos rides to investigate it in ep.19); ad6 shows its endpoint, a sacked village. Option 1 (coincidental name) downgraded to weakest as a result, Option 4 strengthened. Also noted: the ad6 account is hearsay from starving refugees, which remains a cheap escape hatch on direction or identity if one is ever wanted. Decision still **left open**.

**`summary_rules.md`** — three new standing rules, all from this pass: stated terms are not a struck deal (require explicit acceptance in the transcript before writing «συμβιβασμός»/«συμφωνία», and don't carry the benefits over either); a discussed intention is not a performed action (find the transcript line showing execution, not just intent); and where the transcript gives an NPC's motive for an offer, write it, or a trap reads as a good-faith concession.

**New: `Hidden/Session prep/0007 - Session Prep 3-8-2026.md`** — opened for the next Altar of Dust session, starting on the **117th day** (Macro 27th; al-Dun-Du, eighth Or'Dom, Nar'Ai), the morning the party arrives back at Kharanok from Zharvek. Goals carried over from ad6's "Left to do" per the established pattern: the Obsidian trade destination (now untouched two sessions running), the Crystal Dust pond, settling the 7 new arrivals (Tzala as a crafter, 3 would-be fighters, 2 laborers), and one of the two standing rumor leads. The continuity line carries the wounded earth spirit forward as a live threat — it is still at large and has already shown it will take stragglers on that road — alongside the unanswered Gith ultimatum and the loose Bulette. Post-session sections left empty pending play. **Filename date is provisional** (3-8-2026 placeholder), to be renamed once the real session date is known.

**Naming question still open:** `Quel Nas` (the destroyed Dune Runners village) and `Quel'Nash` appear as separate names in the corpus. Same place with drifting spelling or two places — undecided, and `fixes/` treatment depends on the answer.

---

## v1.20 — ep.18/ep.19 Summaries, ad6 Session Prep, Name-Authority Reorder

Most of this entry covers `transcripts and summaries/`, which sits outside the vault but feeds it.

### Episode summaries

**New: `Περίληψη - s3 ep.18 - Royal Necropolis.md`** — Dune Runners, 105th day (Macro 15th, al-Dun-Keth). Written from the full diarized transcript, then merged with a user-supplied corrected draft: sarcophagus-crack timing, Viole's reasoning, the Spider Witch's walked-back curse promise, Pogona's wasp-shift motive, and the near-death climax. **Mirabel confirmed a PC** (Aquarellah's replacement for the dead Dardanne), not an NPC companion.

**New: `Περίληψη - s3 ep.19 - Bloody Red Oasis.md`** — House Markon (Ougk, Banga-Ranga, Mirage, Sando Feet), 113th day (Macro 23rd, al-Qor-Traa). Source video transcribed and diarized via `fast_transcribe_speakers.py`, then passed through `fix_transcript.py`. The Red Oasis formally handed over by the Black Wake; a dracolisk kills a House Kapoul caravan and petrifies Mirage; Melketh fails a Restoration and keeps her overnight; **Siemhouk's first direct appearance** ends in a bargain — the party descends beneath Nibenay against **Zwuun** in exchange for free access to build the Dark Lens, with the Dark Lens revealed as aimed specifically at Borys, not the Sorcerer Kings at large. Zwuun established as born of Defiler and Preserver blood spilled in the old-city sewers, immune to both magic and psionics.

**`Περίληψη - s3 ep.17 - Blood Omen.md`** — reconciled against an external human-written draft found in `Downloads/`, resolved discrepancy-by-discrepancy: sarcophagi origin phrasing, Neriah's mount purchase, Doren's profit-share offer, Varek/Zarron's "Pirate King" title, and the two-front siege plan. A merged copy was written back alongside the Downloads original, which was left untouched.

### Name authority and reference files

**Canonical NPC name priority reordered** — MK-Sandbox promoted to first, ahead of the GM's live Foundry chat text, with the Actor compendium export last. Applied to the `fix_transcript.py` docstring and `summary_rules.md`. The priority governs **name spelling only**; plot facts still come exclusively from the verified raw transcript, since MK-Sandbox stops at `day-0112`/ep.17. MK-Sandbox is also now documented as strictly **read-only** — never written to, even where its records are stale.

**Stale paths corrected** — `fix_transcript.py` pointed at a non-existent `C:/Users/giorg/projects/MK-Sandbox`, and `summary_rules.md` at a non-existent `D:\Darkest Sun\foundry-exports`. Both repointed to their real `K:` locations.

**"Sando o'feet" → "Sando Feet"** — the apostrophe spelling was invented. Corrected across `character_roster.md`, `player_characters.md`, and the ep.6/8/9 summaries; `fixes/sando_ofeet.json` replaced by `fixes/sando_feet.json`.

**`fixes/`** — new entries for `karad_vath`, `talek_vos`, `ranni`, `aiwin`, `rensort`. A corrupted regex in `shadow_king.json` was repaired (a prior global rename had eaten into the pattern). The old duplicate monolithic `K:\Darkest Sun\fix_transcript.py` was deleted in favour of the modular `fixes/*.json` system.

**`character_roster.md` / `session_schedule.md`** — Mirabel added as a PC; **Rhazek** (slos/Giannis, fire Priest) added, previously misspelled "Razek"; attendance rows added for ep.18, ep.19 and ad6, with ep.16/17/19 corrected against the authoritative player list.

**`summary_rules.md`** — a batch of new standing rules drawn from corrections made during writing: NPC offers must reflect their final walked-back position; incapacitated characters cannot act until the transcript shows recovery; every named-NPC scene with substantial dialogue gets its own paragraph in the first draft; the full Merchant/Draxian date line is mandatory and never abbreviated to "Day N"; and several Greek register/redundancy constraints.

### Vault

**`Journal/` flattened duplicates removed** — the 27 loose episode files at the top of `Journal/` (`01. FREEDOM` → `25. Black Wind, Fire and Steel`, plus `12.5 STONE DOOR` and the stray hyphenated `14. TRADERS OF ASSASSINS-.md`) were deleted, along with the four index pages `Journal.md`, `Season 1.md`, `Season 2.md` and `Season 3.md`. These were stale copies left behind after the journal was reorganized into `Journal/Season 1/` (26 entries), `Journal/Season 2/` (7) and `Journal/Season 3/` (19) — no content was lost, the season subfolders hold the current versions. 214 lines removed in total.

**Not yet tracked:** `Journal/Season 3/Επεισόδιο 15- «Fear of the Dark!».md` and `Επεισόδιο 16- «An offer you can't refuse...».md` exist in the vault but have never been committed.

**New: `Hidden/Session prep/0006 - Session Prep 31-7-2026.md`** — ad6 "The Sand Also Rises" (31 July 2026): Goals carried over from ad5's "Left to do" (Obsidian trade destination, Crystal Dust pond, the southeast old-god-believers and the Rensort-survivor lead northeast at Quel'Nash). Extreme heat pushes the party south to the Salt Sea instead; a spirit-guarded oasis demands Rhazek (a fire-server) be surrendered as atonement and the party refuses its terms outright; ruined **Zharvek** searched, a giant legless snake killed, and 7 exhausted survivors — including **Tzala**, a self-taught alchemist — recruited back to Kharanok by posing as emissaries of the Cannibal King. A corrupted earth spirit nearly buries Shaka on the night march, then resurfaces and kills one of the new laborers. All three ad5 goals close unmet and roll forward. New PC **Rhazek** (slos/Giannis) present; Rhugor and Ranni absent.

**New: `Hidden/Zharvek Continuity Conflict.md`** — standalone write-up of the **Zharvek cross-campaign conflict**, linked from `Hidden/Pending Worldbuilding Issues.md` as a one-line tracker entry. ad6's Zharvek is an abandoned ruin south of Kharanok toward the Salt Sea, sacked ~day 100; House Markon's Zharvek (s3 ep.11/13/19) is a thriving inn-village northeast toward Nibenay under Damak, still standing as of ep.19 — opposite direction, and intact nine days *after* ad6 says it fell. The entry lays out a side-by-side comparison, the Gith thread common to both accounts, and four candidate resolutions (coincidental name / retcon ad6 / retcon Markon / make the contradiction diegetic) with costs for each. **Decision: left deliberately unresolved**, no retcon applied to either campaign; also cross-flagged in `Session prep/0006`'s "Left to do" and `transcripts and summaries/locations.md`.

---

## v1.19 — Nominee Actor Stat Blocks

**`Hidden/Nominees/Actors/`** — `Breck.md`, `Sira.md`, `Dorak.md`, `Oren.md`, `Elder Yethras.md`, `Kalia.md`: filled in `## Stat Block or Rules Notes` (AC, HP, Movement, ability modifiers, Alignment, Level) for all six nominee actors. `Dorak.md` had a duplicate `## Stat Block or Rules Notes` heading from an earlier layout glitch — both filled identically pending cleanup.

---

## v1.18 — Token Art Prompt Heading Fix

**`Hidden/Nominees/Actors/`** — `Kalia.md`, `Elder Yethras.md`, `Dorak.md`, `Sira.md`, `Breck.md`: "Token art prompt (Banana Pro / image-gen reference):" changed from a bold inline label to a proper `##` heading. `Nominees/README.md` workflow rule updated to match.

---

## v1.17 — Session Prep Date Fixes

**`Hidden/Session prep/0001` through `0004`** — day-context lines updated to the full Merchant/Draxian calendar format already used in `0005`. `0001`/`0002` also had a stale placeholder ("Macro 13") corrected to the actual computed date (Macro 19th, day 109). `0002` further updated to note the session spans two in-game days — starts 109th day, runs into the night of the 110th, when the party first encounters the entity beneath Kharanok in a shared dream.

---

## v1.16 — Kharanok Nominees: Quest-Giver Actors, The Loyal Faction, Obsidian Mines Location

**New: `Hidden/Nominees/`** — draft actor proposals for the MK-Sandbox repo, per [[Living Campaign]]'s Guest GM Entry Guidelines. Not canon until submitted and approved upstream (submission URL: https://github.com/fchrysoulas/MK-Sandbox/issues).

**New actor files (canonical actor template):** `Elder Yethras.md`, `Breck.md`, `Sira.md`, `Dorak.md`, `Oren.md`, `Kalia.md` (field update to existing `actor-kalia`, folding in her maiden name Yelka and cistern-overseer duties as the same person, not a separate NPC). Each includes a Player-Safe appearance paragraph, a preserved raw Banana Pro token-art prompt under Stat Block/Rules Notes, and — for Yethras and Kalia — a GM-written sample introduction scene under Manner and Voice.

**`Nominees/README.md`** — index of nominated actors plus a new workflow-rules section for how appearance prompts and intro scenes get folded into actor files (natural prose for `### Appearance`, raw prompt preserved verbatim as a labeled blockquote, single `## Stat Block or Rules Notes` header, template shape re-checked after each edit).

**New: `Hidden/Nominees/Factions/The Loyal.md`** — faction proposal (update to existing `faction-the-loyal`) adding "Vindicate Jessix's name" to doctrine/goals and the Slinnasia-witness backstory to sources, since the existing JSON's doctrine/goals never captured the band's actual motive. Confirmed the existing `followers: 5` count is already correct, no change needed there. README.md updated with a new Factions index section.

**New: `Hidden/Nominees/Locations/Obsidian Mines.md`** — location proposal (new entry, no existing `location-obsidian-mines` in MK-Sandbox) for Below Kharanok Level 1: room layout, connections, hidden teleportation route, Crystal Dust mechanics, and dangers, pulled from the level's own map page plus `location-kharanok`'s mining fields and sessions ad3–ad5. Notes the ad4 Syggra-recovery cave is a separate, unnamed cave outside this level's keyed area. README.md updated with a new Locations index section.

---

## v1.15 — Hunter Mode XP Calculator + New Rules Pages + ad5 Session Prep

**New: `hunter-mode-xp-calculator/index.html`** — interactive tool for the Hunter Mode XP rule: enter party levels, hireling count, and enemy groups (level + count) for a live breakdown of which groups clear the half-average-level threshold, the total XP pool, and XP per participant (rounded down). Styled with an Athasian palette — obsidian-black grounds, crimson/blood-orange sun accent, bone-toned text — in place of the earlier generic amber theme.

**`Advancement.md`** — linked the new calculator from the Hunter Mode section.

**New Rules/ pages:**
- **`Water Sources.md`** — worldbuilding constraint: any two water sources (oases, wells, springs) must be at least 24 miles apart.
- **`Renown.md`** — fame/infamy tracking system (Cursed Scroll 6 — City of Masks): starts at CHA modifier, gained/lost through public events, four tiers with carousing/reaction bonuses.
- **`Awarding XP.md`** — documents the Hunter Mode XP system in use (per-encounter, combined enemy level split evenly, half-average-level-or-under enemies worth 0 XP), links the new calculator.
- **`Taming Wild Kank.md`** — the soothing-sound technique from actual play (ad5) for calming wild kank instead of fighting them (DC 18 CHA).
- **`The Merchants' Code.md`** — the seven-point code merchant-house members are expected to uphold.
- **`Psicrystals.md`** — homebrew psicrystal/psionic blade supplement (creation, attunement, loss/destruction, rarity tiers, blade properties).
- **`Portal Activation.md`** — Crystal Dust cost for the one-way teleportation room below Kharanok's Obsidian Mines (10 to activate, 1 per use).
- **`Rules.md`** — index updated to link all of the above.

**`Hidden/Kharanok- The Altar of Dust/Below Kharanok/01. Obsidian Mines AKA The Cannibal Caves.md`** — added the portal's Crystal Dust activation cost to the Barracks (#9) teleportation-room note.

**New: `Hidden/Session prep/0005 - Session Prep 26-7-2026.md`** — ad5 "The Bug Whisperers... Finally!" (26 July 2026): new PC Ranni (Elf Priest) joins after healing Gur-da; heat/sandstorm forces a mining detour instead of the planned kank hunt; two Gith scouts caught and interrogated (Relo withholds his identity as "the nobody," Shaka eats a heart to intimidate), survivor released with a trade-or-else ultimatum; a Land Shark (Bulette) ambush fought off and left wounded; sandstorm-shelter rumors from refugees Aiwin and Kia; afternoon kank hunt ends in taming instead of a fight (2 kank led home peacefully instead of the 1 originally needed), Relo voted MVP.

**New: `Hidden/Pending Worldbuilding Issues.md`** — GM-only tracker for open worldbuilding questions; first entry flags an unresolved question around The Loyal/Jessix the Wanderer.

---

## v1.14 — Below Kharanok Distances + ad4 Session Prep + Advancement Fix

**`Below Kharanok.md`** — merged in a standalone isometric-map page (created then folded back into the main hub): embedded overview image, link to the interactive pan/zoom HTML (`kharanok dungeon/isometric-map/index.html`), and a new **General Info** section with a full distance table (mi/ft/km) for every connection in the dungeon graph, plus a short read on which links run longest/shortest and why.

**New `isometric-map-labeled.png`** — rendered from the interactive HTML via headless Chrome (scale forced to 1, header/zoom controls stripped) so all 31 pin labels are baked into a single static image; replaces the earlier unlabeled embed.

**Distance methodology:** pin pixel-positions read off the isometric layout, scaled against the "~6 miles top to bottom" footprint claim (≈8.11 ft/px) — explicitly flagged as a schematic estimate, not surveyed geography, since the node layout itself is user-supplied. Distance-table links use full `[[wikilink]]`s to each numbered area's note.

**New: `Hidden/Session prep/0004 - Session Prep 25-7-2026.md`** — ad4 "It's Raining Bats and Bugs" (25 July 2026): captive Gith interrogation and release, Kalia's rope refusal (she'd already given the party Zephyr, a new NPC priest of air ally, and had nothing left to offer), a wild kank fight over drunk Syggra in kank territory, a near-fatal giant bat swarm ambush, and Parias's shadow-spell ghost transformation ("Erebos") saving an unconscious Gur-da by possessing a kank. 3 of 5 missing Syggra recovered alive, 2 died in the fighting; the Kank itself was never recovered, only consolation Feed Globules.

**`01. Obsidian Mines AKA The Cannibal Caves.md`** — South Access Shaft (#12) given a concrete depth split: ~180m/590ft rope elevator, then ~1,735m/5,693ft of rock-carved staircase (~10,200 steps) to make up the full 1.92km shaft. Also added the in-world reason the site keeps the "Obsidian Mines" name despite also yielding Crystal Dust: Crystal Dust mining/trading is illegal, so the obsidian vein is the cover story.

**`Advancement.md` (Hunter Mode)** — clarified the XP rule that was previously just "combined enemy level, split evenly": any enemy at half the party's average level (rounded down) or lower is "no challenge" and worth zero XP, per actual table-play precedent.

---

## v1.13 — Below Kharanok: Full 31-Level Dyson MegaDelve Build-Out

**New: `Below Kharanok/02.` through `31.`** — stub pages for all 31 areas of Dyson Logos's "Dyson MegaDelve" map pack, each with source map images, a Dyson blog source link (shown both as a markdown link and as visible canonical `dysonlogos.blog` plain text — the original `rpgcharacters.wordpress.com` links all 301-redirect there), a parsed flavor-text summary (fetched from each area's actual Dyson post), and a Connections section. `01. Obsidian Mines AKA The Cannibal Caves` (already played/keyed) is unchanged and remains the entrance.

**Numbering:** areas ordered 01–31 by actual walkthrough connectivity, not raw visual position — built from a full connection graph (passages, staircases, collapsed/impassable routes, shafts) supplied over the session, then cross-checked against Dyson's own original node map (OCR'd) and corrected where it revealed missed edges (e.g. Marble Hall ↔ Venomous Hall, Necropolis ↔ Crypts direct, Mushroom Cavern ↔ Hematite Mines, Ogre Base ↔ Mushroom Cavern).

**Floors:** areas grouped into 8 depth floors (user-supplied), documented in `Below Kharanok.md`.

**Harpy Tower correction:** originally connected to the Necropolis (campaign guess); Dyson's own source text places it above the dwarven city instead, linked by a (destroyed) staircase down to Gates of the City — realigned to match Dyson's source, Necropolis connection removed.

**New: `Wandering Monster Tables/`** — backup pages for Dyson's die-drop encounter tables for the Mushroom Cavern and Under the Mushroom Cave, cross-linked from both area pages.

**Geography:** dungeon situated in the Blackspine Mountains; Obsidian Mines confirmed as the entrance below Kharanok itself; Necropolis of Bryn Mynnyd's surface exit specifically leads to Quor'Anok, other surface exits lead elsewhere in the range.

---

## v1.12 — Session Prep Detail Pass (ad1–ad3)

More detail added across all three session preps:

- **ad2 (`0002`):** nat 20 stabilize rolls for Rhugor/Shaka saving Relo and Sepsis; Dorak's camping condition reframed as "see for yourselves what happens at night"; explicit note that players have no way of knowing what a moonbeast is (in-fiction knowledge gap, not just "unresolved")
- **ad3 (`0003`):** the Gith captors were trying to ambush Kharanok again through the subterranean caves when found; the party staked the beheaded Gith's heads on spikes as a deterrent (not just "beheaded as a warning"); captive Gith's planned answer clarified — "moon" and "beast" as two separate words, not a single "moonbeast" reveal
- Minor formatting cleanup (blank line after frontmatter removed) across `0001`–`0003`

---

## v1.11 — Truncation Bug Recovery + ep.1/ep.6 Naming Fixes

**Real corruption found and fixed:** the editing tool used for several recent commits was silently clipping long lines (~150 chars) and saving the literal text `[...]` in their place. Found 7 truncated lines in `0003 - Session Prep 16-7-2026.md` and 1 in `0002 - Session Prep 10-7-2026.md`. Recovered the full original text for all 8 from git history (`git show` on pre-truncation commits) — no content guessed or invented, all restored verbatim from prior commits.

**Naming fixes** (continuing the Foundry-canon verification pass):
- `Επεισόδιο 1- «Βωμός της Σκόνης»`: Zarakai → **Zharakai**
- `Επεισόδιο 6- «Θυσία στη Φωτιά»`: Zarakai → **Zharakai**
- `Altar of Dust, Session ad1- «Find the... GOAT!»`: Quel Nas → **Quel Nash**

**Session preps (`0002`, `0003`):** the "water spirits want a companion" thread re-sourced — the actual explicit request (a permanent guardian-caretaker, protected by the spirits, no food needed) is in ep.6, after a second fire-priest drowning settled the original debt, not just inferred from Duunesh's ep.1 death.

**`GUIDELINES.md`:** added the "committed changes only" changelog rule (don't bump ahead of what's actually committed) alongside the existing obsidian-only scope rule.

---

## v1.10 — Obsidian Mines Canon Layout + New Vault Guidelines

**`Below Kharanok/01. Obsidian Mines AKA The Cannibal Caves.md`** established as the canonical map reference:
- New **Room Connections** section tracing the full layout from the POI map image (1→2→3 fork into either 4/5/6/7 via the water, or 8/9/10/11/12 via the built room complex)
- New **Hidden Connections** section: crate-hidden door from Storehouse (#10) to Foreman's Office/quartermaster (#8, locked from the other side, stairs down to Level 2); hidden passage in the elevator-shaft storage room to a one-way teleportation room; two illusionary walls from the Barracks (#9) as a second route to that same teleportation room
- Deep Lake (#6) POI expanded with Crystal Dust formation lore: shards deposited by water, recoverable when it dries at noon, quality gradient (cloudy/mineral-heavy near the lake, clearer higher-grade deeper in where Bulette roam and the passage narrows)
- Elevator/tar cross-reference fixed to a proper `[[wikilink]]`

**`0003 - Session Prep 16-7-2026.md`** — "party chose not to risk going past the broken elevator" corrected: it wasn't a choice, gith can jump the shaft but players need the (broken) mechanical elevator. GM map reference section trimmed to point at the now-canonical cave file instead of duplicating the room details.

**New `obsidian/GUIDELINES.md`** — vault-wide editing conventions, independent from `summary_rules.md`: wikilinks over backticks for in-vault refs, one-canonical-source-per-topic pattern, NPC background correction protocol, quest Act/Hook progress-note pattern, session prep format (inlined), file naming for ordered series, LegendKeeper JSON→Obsidian sync workflow, changelog discipline.

---

## v1.9 — Session Prep Files Renamed for Sort Order

`Hidden/Session prep/` files were sorting wrong alphabetically ("10-7" and "16-7" both sort before "2-7"). Renamed with a 4-digit numeric prefix reflecting session order:
- `Session Prep 2-7-2026.md` → `0001 - Session Prep 2-7-2026.md`
- `Session Prep 10-7-2026.md` → `0002 - Session Prep 10-7-2026.md`
- `Session Prep 16-7-2026.md` → `0003 - Session Prep 16-7-2026.md`

Internal cross-reference in `0002` (pointed to the old ad3 filename) updated to match.

---

## v1.8 — Altar of Dust Continuity Pass (Session Preps, Quests, NPCs)

**Session prep files unified** — `Hidden/Session prep/Session Prep <date>.md` (ad1, ad2, ad3) rewritten to a single shared format: Goals → Related Quests → Done → Not done/left unfinished → Summary → Left to do. Format documented in `summary_rules.md` for future preps.

**ad3 prep (16-7-2026) filled in from GM Discord planning:**
- Corrected Syggra count: 4/10 recovered ad1, 1 of remaining 6 has since died → 5 left, located in a Wild Kank nest cave near a Gith camp neutral toward Kharanok
- Stolen Food Producing Kank: traded by hostile Gith to the Aarakocra, not yet recovered
- Captive Gith's planned interrogation answers — corroborates (doesn't first-reveal) that the dream-entity is a **moonbeast**
- Gate/watchtower status: 50/200 scraps, obsidian piece secured for signal mirror, warband for shifts still never recruited
- New open threads: 10 Crystal Dust recovered but no alchemist to brew potions; elevator needs tar *and* someone who can work it
- New GM map reference section: unexplored Level 1 storage rooms — hidden door behind crates → locked quartermaster chambers → stairs to Level 2; hidden passage in the elevator-shaft storage room → one-way teleportation room; barracks next to quartermaster; two illusionary walls as a second route into the same teleportation circle room

**`Kharanok- The Altar of Dust/Quests/Act 1 - Eyes Open.md`** — progress notes added to all 3 hooks (watchtower mirror, gate repair, Syggra/Kank) reflecting ad1–ad3 actual play.

**`Kharanok- The Altar of Dust/Quests/Act 2 - Clear the Mountain.md`** — Hook 2 ("The Seal Is Failing") restructured: the shared-dream path confirmed as the real, in-progress path. Quest Giver is [[Dorak]] — he doesn't know what's trapped down there, but he's the one who sets the trigger, refusing to guide anyone deeper without first making them camp a night atop the quarry; it was during one such night (before ad2) that the moonbeast reached out. The physical-investigation path (exterior seal markings chipped from outside) is reassigned from Dorak to Oren, consistent with his established treachery.

**NPC corrections:**
- `Dorak.md` — background rewritten: he's a former gith slave forced to work the mines (matches his ad3 reveal), not the original written "30-year seal-keeper" — that framing conflicted with actual play and is removed. Added relationship note on the quarry-camping test he sets and what it actually triggered.
- `Oren.md` — sharpened: he broke the watchtower's obsidian signal mirror specifically (not just misused it), core motivation reframed as plain cowardice/wanting peace of mind

**`session_schedule.md`** (transcripts and summaries) — added missing ad3 row (Thursday, July 16, 2026), footer note updated to cover the full ad1–ad3 player pool.

**Obsidian Journal headers fixed** — `Altar of Dust, Session ad1/ad2` headers still had the old wrong names "Rougor"/"Saka" (character_roster.md had already corrected these everywhere else) — fixed to "Rhugor"/"Shaka".

---

## v1.7 — LegendKeeper Resync (2026-07-23 export)

**Source:** `Darkest Sun.json` exported 2026-07-23, moved in from `Downloads/`; prior 2026-06-05 export kept as `Darkest Sun.json.bak-2026-06-05`

**Script fix:** `json_to_obsidian.py` had hardcoded sandbox paths (`/sessions/sleepy-peaceful-pascal/mnt/...`) left over from a previous environment — `SRC`/`VAULT` updated to `D:\Darkest Sun\Darkest Sun.json` / `D:\Darkest Sun\obsidian`.

**164 files written** across Rules, Classes, The World, Kharanok- The Altar of Dust, Campaign Map, and root (Darkest Sun.md, Advancement.md, Psionics.md, Character - Soldier.md, Untitled.md).

**Protected (untouched, verified):** `NPCs/` (46 files), `Monsters/` (28 files), `Hidden/`, `greek/`, `Books/` — 0 protected_skipped reported since the new export doesn't touch those resource IDs.

---

## v1.6 — Session Prep Folder

**New `Hidden/Session prep/`**
- `Session Prep 2-7-2026.md` — session notes (2 July 2026)
- `Session Prep 10-7-2026.md` — session notes (10 July 2026)

---

## v1.5 — NPC Rename: Yelka → Kallia Yelka

**NPC renamed**
- `Hidden/Kharanok- The Altar of Dust/NPCs/Yelka.md` → `Kallia Yelka.md`
- All references updated: quest files (Act 1/4/5/6, Set 1/4/5, Kharanok Quest Chain, Final, Structure Tree), Roleplay Tips, Kharanok_Quest_Chain.md, Greek link in `Γέλκα.md`, CHANGELOG.md
- Workspace.json path auto-updated by Obsidian

---

## v1.4 — Shadowdark PDF → Markdown Import

**New Markdown files from PDF conversion**
- `Shadowdark RPG - V4-4.md`
- `Cursed Scroll 1 - Diablerie V4-3.md`
- `Cursed Scroll 2 - Red Sands V2-2.md`
- `Cursed Scroll 3 - Midnight Sun V3-5.md`
- `Cursed Scroll 4 - River of Night V1.md` (+ horizontal pages version)
- `Cursed Scroll 5 - Dwellers in the Deep V1.md`
- `Cursed Scroll 6 - City of Masks V1-1.md` (+ horizontal pages version)
- `Player's Guide to the Western Reaches V1.md`

All 10 PDFs converted via pdfplumber, paginated with separators, and imported into vault.

---

## v1.3 — AI Battlemaps, Foundry Macros, Prompt Library

**`.gitignore` added** — ignores `Untitled.md` globally (covers root + subdirectory copies)

**New `Gists/` folder**
- `Psionicist Foundry macros.md` — Shadowdark macros: Psionicist "Improved" (active effect + level bonus to attacks/checks), Defensive Flurry (roll attack as AC for 1 round via ActiveEffect), Reset Defensive Flurry
**AI image generation pipeline**
- `Prompts for nano banana pro 2.md` — prompt library referencing 3 battlemap scenes via embedded PNG + TXT pairs
- Root images: `cave inside.png`, `desert night.png`, `temple.png` — no-grid JRPG combat maps (Greg Capullo / Gerald Brom / Darkest Dungeon style)
- Root prompts: `cave inside.txt`, `desert night.txt`, `temple.txt` — matching prompt texts (underground cavern, desert wastes night, obsidian temple interior)

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
- Created `Kharanok- The Altar of Dust/NPCs/` with 9 NPC files: Elder Yethras, Breck, Sira, Dorak, Kallia Yelka, Oren, Jessix the Wanderer, Muuton, Jessareen
- Created `Roleplay Tips.md` with generic GM guidance for running Kharanok NPCs
- Each NPC file includes: Background, Agenda, Wants & Needs, Goals, Roleplay Notes, Relationships

**Quest links (English)**
- Added NPC wiki links throughout all 8 quest files (Kharanok Quest Chain + Sets 1–6 + Final)
- Local NPCs linked with short path; outsider NPCs (Jessix, Muuton, Jessareen) linked with full vault path to disambiguate from global NPC files
