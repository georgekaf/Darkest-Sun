---
entryType: actor
entrySubtype: player-character
authorGM: "Ghost"
visibility: mixed
---

# Actor: Parias (update to existing actor-parias, revision 3)

*(Revision of existing actor `actor-parias`. Stub record — no ancestry, class, level, stat block, goals, relationships or knowledge.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/parias.json` (revision 3, updated 2026-07-22).*

| Field | Current value |
| --- | --- |
| `actorType` / `controlType` | agent / player-character |
| `partyName` | Altar of Dust |
| `role` | **Psionic** Altar of Dust adventurer |
| `locationId` / `status` | location-kharanok / active |
| `goals[]` | **empty** |
| `campaignContinuity` | firstConfirmedDay 109, lastConfirmedDay **110** |
| `sourceRefs[]` | Day 109 (Day at Kharanok); Day 110 (The Shared Dream) |

**Proposed changes, all unapproved:**

1. **`role` says "Psionic".** The sheet says **Necromancer** — shadow magic and soul work, not The Way. Propose correcting to "Necromancer Altar of Dust adventurer", or confirming he is both.
2. **`lastConfirmedDay: 110` is stale.** He is in the ad5 party on **day 112**.
3. `goals[]` empty; no ancestry, class, level or stat block; no relationships.
4. **He is the highest-level character in the party at 7**, and the record does not say so.

## One-Sentence Summary
A necromancer who kills with beams of shadow, walks through gates of his own making, and has already stepped through one to come back as something called Erebos.

## Classification
- Subtype: player-character — sandbox shape `actorType: agent` + `controlType: player-character`
- Control: player-character — party *Altar of Dust*
- Status: active
- Current location: Kharanok (`location-kharanok`)
- Role: Necromancer — the party's heaviest caster

## Player-Safe Description

### Appearance
Scale mail and the **Staff of Omid +1**. CHA 18 — the second most commanding presence in the party after Sepsis.

### Manner and Voice
Not recorded in detail.

### Public Reputation
Not recorded outside the party.

## Confirmed Facts
- **ad4, day 111:** kills a wild kank outright with **a beam of shadow**. Later, in the bat fight, **passes through a gate of shadow and transforms into a ghost — Erebos.**
- **ad5, day 112:** with the party for the kank hunt. **This is later than the sandbox's `lastConfirmedDay`.**
- **ad6, ad7:** not present.

## Goals
1. Description: *(Proposed — the sheet's Gate progression implies a direction the table has not stated.)* Open the next gate.
   - Priority: 4 · Progress: Second, Third and Fourth Gate are all on the sheet · Secret: unknown · Status: active

## Traits and Pressures
- Ambition: The gate progression suggests a lot of it. Unstated at the table.
- Caution: Unmeasured.
- Loyalty: Present from day 109 to 112, then absent.
- Cruelty: Unmeasured — but Reap The Soul and Lamentation are on the sheet.
- Risk tolerance: He walked through a shadow gate and came back changed.
- Wealth: A named magic item, which almost nobody else has.

## Resources and Capabilities
- **Necromancer spellcasting** with two Spellcasting Advantage talents and two +1 on Spellcasting Checks.
- **Second Gate, Third Gate, Fourth Gate** — a progression, not a single spell.
- **Reap The Soul**, **Lamentation**, **Withermark**, **Bane**, Blink, Protection From Evil, Turn Undead.
- **Staff of Omid +1**, with Fly and Wither modes.
- 34 HP — the toughest caster in the party.

## Relationships
- Player character: **Relo** (Mpelos) — fellow caster, both present ad4–ad5.
- Player character: **Sepsis** — *Same class, same discipline.* Two necromancers in one party, one at level 7 and one at level 4; nothing at the table has explored whether they trained together.

## Knowledge
- Subject: The shadow gates
  - Claim: He can open them and pass through, and has come back from one as Erebos.
  - Source: direct · Learned day: 111 · Confidence: certain · Truth status: true · Secret: no

## Current Activity
Unconfirmed since day 112. Presumed in Kharanok.

## GM-Only Secrets
- **Erebos is unexplained.** The ad4 summary names it as what he becomes on the far side of a shadow gate. Whether that is a form, a name, or something that has its own intentions has never been established.
- A necromancer at level 7 in a party where the next-highest is 6 is the single biggest capability in Kharanok, and he has not been at the table since day 112.

## Proposed Developments
All unapproved. If the party takes the gate to Giustenal — a city of two thousand years of murdered dead — the party's necromancers are the two characters that place was built to interest.

## Stat Block or Rules Notes
- System: **Shadowdark** — sheet `fvtt-Actor-parias-SIORi5J1vpNmoG8c.json`
- Class: **Necromancer** · Ancestry: **Human** · Level **7**, XP 24 · Alignment neutral
- HP **34/34** · AC **12**
- STR 13 · DEX 8 · CON 12 · INT 7 · WIS 14 · CHA 18
- Spells: Second Gate, Third Gate, Fourth Gate, Reap The Soul, Lamentation, Withermark, Bane, Blink, Protection From Evil, Turn Undead
- Talents: Spellcasting (Necromancer), Spellcasting Advantage ×2, +1 on Spellcasting Checks ×2, +2 to Charisma, Ambitious, Diplomats
- Gear: Scale Mail, **Staff of Omid +1** (Fly, Wither), Holy Water, Oil Flask ×2, Firekit, Rations ×2, Water

## Sources
- Title: `Downloads/fvtt-Actor-parias-SIORi5J1vpNmoG8c.json`
  - Section: Foundry VTT Shadowdark player sheet · Source type: system export (9 August 2026)
  - Adaptation note: Ancestry inferred **Human** from Ambitious/Diplomats. Class UUID matches Sepsis's — Necromancer. **This contradicts the sandbox `role` field, which says "Psionic".**
- Title: `mk-repos/mk-sandbox/actors/parias.json` — revision 3, read-only. The record this nominee revises.
- Title: Darkest Sun — Altar of Dust, ad4 — the shadow beam; the gate; Erebos · campaign-original, in-world day **111**
- Title: Darkest Sun — Altar of Dust, ad5 · campaign-original, in-world day **112**

## Unresolved Questions
- **Psionic or necromancer?** The sandbox role and the sheet disagree.
- **What is Erebos?**
- Whether Parias and Sepsis have a shared history, given the identical class.
- Why he has been absent since day 112.
