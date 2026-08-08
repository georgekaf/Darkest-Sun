---
entryType: actor
entrySubtype: player-character
authorGM: "Ghost"
visibility: mixed
---

# Actor: Sepsis (update to existing actor-sepsis, revision 3)

*(Revision of existing actor `actor-sepsis`. Stub record — no ancestry, class, level, stat block, goals, relationships or knowledge.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/sepsis.json` (revision 3, updated 2026-07-22).*

| Field | Current value |
| --- | --- |
| `actorType` / `controlType` | agent / player-character |
| `partyName` | Altar of Dust |
| `role` | Altar of Dust adventurer **and interpreter** |
| `locationId` / `status` | location-kharanok / active |
| `goals[]` | **empty** |
| `campaignContinuity` | firstConfirmedDay 109, lastConfirmedDay **110** |
| `sourceRefs[]` | Day 109 (Feathers and Horns); Day 110 (The Shared Dream) |

**Proposed changes, all unapproved:**

1. `goals[]` empty; no ancestry, class, level or stat block. Propose **Human Necromancer 4** from the sheet.
2. **`role` calls him an interpreter.** Interpreting has since passed to Relo and then to Sylvar. Propose either recording *which* language he interprets, or dropping the label.
3. **`lastConfirmedDay: 110` is correct** — he does not appear in ad4 (111), ad5 (112), ad6 (115) or ad7 (117).
4. **`status` must change from `active` to `inactive`. GM ruling, 2026-08-09: Sepsis's inactivity is correct.** This matches the precedent already set on `actor-ugo`, whose record carries the note *"absent from the later rosters; no death or departure was confirmed."* Propose the same note shape here, keyed to day 110.

## One-Sentence Summary
A necromancer with the highest Charisma in the party and no confirmed appearance in seven in-world days — the second of two soul-workers in a party that is about to walk into a city made of the dead.

## Classification
- Subtype: player-character — sandbox shape `actorType: agent` + `controlType: player-character`
- Control: player-character — party *Altar of Dust*
- Status: **inactive** *(GM ruling, 2026-08-09)* — the sandbox record still says `active` and needs correcting. No death or departure was ever confirmed; he is simply not in play.
- Current location: Kharanok (`location-kharanok`)
- Role: Necromancer — and interpreter, per the existing record

## Player-Safe Description

### Appearance
Leather harness, a chatkcha. CHA 19 — the highest of any character on record in this party.

### Manner and Voice
Not recorded.

### Public Reputation
Not recorded.

## Confirmed Facts
- Present in the campaign record for **day 109** ("Feathers and Horns") and **day 110** ("The Shared Dream").
- **Not present** in ad4 (day 111), ad5 (112), ad6 (115) or ad7 (117).
- No death, departure or explanation is recorded anywhere.

## Goals
1. Description: *(Proposed — nothing has been stated at the table.)* Unstated.
   - Priority: — · Secret: unknown · Status: unknown

## Traits and Pressures
- Ambition: Unmeasured.
- Caution: Unmeasured.
- Loyalty: Unmeasured — he has not been present to demonstrate any.
- Cruelty: Unmeasured.
- Wealth: Ordinary kit.
- Status: **The party's most persuasive character on paper, absent for a week of in-world time.**

## Resources and Capabilities
- **Necromancer spellcasting**, two Spellcasting Advantage talents, +1 on Spellcasting Checks.
- **Death Sense** and **River of Death** — class abilities that would matter enormously at Giustenal.
- **Withermark**, **Ghoul Touch**, Bane, Protection From Evil, Turn Undead.
- **Psionic Sense** on the sheet.

## Relationships
- Player character: **Parias** — *Same class.* Two necromancers, levels 7 and 4, both currently absent from play.
- No other relationships recorded.

## Knowledge
Nothing recorded.

## Current Activity
None. **Inactive since day 110** by GM ruling. The record still reads `active` at Kharanok until the field is corrected.

## GM-Only Secrets
- **Death Sense and River of Death in the ruins of Giustenal** is the strongest untouched hook in the party's roster. The city is two thousand years of murdered dead and a group consciousness formed from them; a necromancer who senses death would not need to be told something is wrong there.
- He has **Psionic Sense**. Under the Caller's selection rules that plus a human ancestry makes him a target — unlike Gur-da or Rhazek, whom it ignores.

## Proposed Developments
All unapproved. Either his absence gets an in-world explanation or the record should follow Ugo's precedent and mark him inactive.

## Stat Block or Rules Notes
- System: **Shadowdark** — sheet `fvtt-Actor-sepsis-pJYZG1V6JJtyNnlM.json`
- Class: **Necromancer** · Ancestry: **Human** · Level **4**, XP 0 · Alignment neutral
- HP **13/16** — currently wounded on the sheet · AC **9**
- STR 12 · DEX 9 · CON 11 · INT 14 · WIS 11 · CHA **19**
- Spells: Withermark, Ghoul Touch, Bane, Protection From Evil, Turn Undead
- Class abilities: **Death Sense**, **River of Death**, Psionic Sense
- Talents: Spellcasting (Necromancer), Spellcasting Advantage ×2, +1 on Spellcasting Checks, Ambitious, Diplomats
- Gear: Leather Harness, Chatkcha, Rope 60', Rations, Oil Flask, Torch ×2, Water

## Sources
- Title: `Downloads/fvtt-Actor-sepsis-pJYZG1V6JJtyNnlM.json`
  - Section: Foundry VTT Shadowdark player sheet · Source type: system export (9 August 2026)
  - Adaptation note: Ancestry inferred **Human** from Ambitious/Diplomats. Class UUID matches Parias's — Necromancer.
- Title: `mk-repos/mk-sandbox/actors/sepsis.json` — revision 3, read-only. The record this nominee revises.
- Title: Darkest Sun Campaign Record — Days 109 and 110 · campaign-history
  - Adaptation note: The only confirmed appearances.

## Unresolved Questions
- **Where is he, in-world?** Seven days unaccounted for, no departure recorded. Being inactive is now confirmed; *why* is not.
- ~~Should `status` become inactive, as Ugo's did on the same evidence?~~ **Answered 2026-08-09 by GM ruling: yes.**
- What language he interprets — the role field asserts it without saying.
- Whether the HP 13/16 on the sheet reflects a real injury from day 110.
