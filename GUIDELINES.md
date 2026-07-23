---
title: "Kharanok — Vault Editing Guidelines"
tags: [kharanok, meta]
---

Conventions for editing this vault, established through actual practice (Altar of Dust continuity pass, 2026-07-23).

## Wikilinks over backticks
Always use `[[Note Name]]` (no file extension) to reference another note inside this vault — not backtick-wrapped filenames. Backticks are for referencing things *outside* the vault (e.g. `` `session_schedule.md` ``, which lives in `transcripts and summaries/`, not in Obsidian).

## Canon consolidation — one source of truth per topic
Put full detail in the single most-specific/canonical file for that topic (e.g. a dungeon's room layout belongs in that location's own map file, not scattered across session preps). Other docs (session preps, quest files, NPC files) reference it with a `[[wikilink]]` instead of duplicating the content. If you find the same detail written out in two places, trim the duplicate and point it at the canonical one.

Example: the Obsidian Mines' hidden room connections live in `Below Kharanok/01. Obsidian Mines AKA The Cannibal Caves.md`. The session prep that first surfaced them just links there instead of repeating the details.

## NPC background corrections
When actual play (or a direct GM/user clarification) contradicts a pre-written NPC background, the confirmed/actual backstory wins outright. Rewrite the conflicting sections of the NPC file — don't leave the old lore sitting alongside the new as if both are true, and don't just append a correction note on top of an unchanged background.

## Quest Act/Hook progress notes
`Quests/Act N - <title>.md` files keep their original hook design as written. Actual-play progress gets appended as a `**Progress (as of ad<N>, <date>):**` line under the relevant hook — this supplements the hook, it doesn't replace it, unless the hook's premise is directly contradicted by what happened (see NPC background corrections above for that case).

## Session prep format
Each `Hidden/Session prep/<NNNN> - Session Prep <date>.md` follows one shared structure:
```
---
title: "Session Prep — <date> (ad<N> «<title>»)"
tags: [kharanok, session-prep, altar-of-dust]
---

# Session Prep — <date> (ad<N>)

*<in-world date/time, if known>*

## Goals
<what the GM wanted to happen going into the session>

## Related Quests
<[[wikilinks]] to the relevant Act quest files>

## Done
<bullet list of what actually got accomplished>

## Not done / left unfinished
<which of the stated Goals did NOT happen — distinct from "Left to do" below>

## Summary
<bullet list, short factual recap of events>

## Left to do
<open threads going forward — GM planning notes for the next session go here too, not in a separate section>
```
A new file is created for each new Altar of Dust session, numbered with the 4-digit prefix convention above.

## LegendKeeper JSON → Obsidian sync
`D:\Darkest Sun\json_to_obsidian.py` converts a LegendKeeper export into this vault's markdown. Workflow for a new export:
1. New export lands in `Downloads/` as `Darkest Sun.json`. Back up the current `D:\Darkest Sun\Darkest Sun.json` first (e.g. `Darkest Sun.json.bak-<old-export-date>`), then move the new one into place.
2. Run the script: `python json_to_obsidian.py` from `D:\Darkest Sun`.
3. It only **writes** — never deletes. `PROTECTED = {"NPCs", "Monsters", "Hidden", "greek", "Books"}` folders are always skipped (`protected_skipped` count in the output confirms this — 0 just means the export didn't touch those resource IDs, not that protection failed).
4. Console `WRITE` lines may show mojibake for Greek filenames — that's a terminal codepage display issue only; the actual files on disk are UTF-8 correct. Verify with `ls`/`Read` if unsure, not by trusting the console output.
5. Bump `CHANGELOG.md` after a sync — see Changelog discipline below.

Script path constants (`SRC`, `VAULT`) are hardcoded to `D:\Darkest Sun\...` — if this ever runs in a different environment, fix those two lines first rather than passing args (the script doesn't accept any).

## File naming for ordered series
When a folder holds a numbered sequence of files whose names don't sort correctly on their own (e.g. session prep dates without zero-padding), prefix with a 4-digit number reflecting the actual order: `0001 - ...`, `0002 - ...`. Update any internal cross-references (wikilinks, backtick mentions) to the new filenames when renaming.

## Changelog discipline
See `AGENTS.md` → "Changelog Rules" for the base rule (bump = new version with everything since last bump; never retroactively edit an already-bumped version). In-session refinement: if a version was bumped and then immediately superseded by a closely-related follow-up before anything else referenced it, they can be merged into one entry on request — but once a version is a genuine, separate unit of work (or something else has been bumped after it), don't merge backward.

**Scope: obsidian/ only.** `CHANGELOG.md` tracks changes to files *inside* the `obsidian/` vault. Work in `transcripts and summaries/` (Περίληψη files, `fixes/*.json`, `session_schedule.md`, `summary_rules.md`, raw transcripts) does **not** get a changelog entry on its own, even in the same work session — that directory isn't part of this vault. If a single pass touches both, only the obsidian-side portion is changelog-worthy; describe that part on its own rather than bundling in the non-obsidian work.

**Committed changes only.** Don't bump the changelog for edits sitting uncommitted in the working tree — `git status`/`git diff` first. Only bump once the obsidian-side changes are actually committed.
