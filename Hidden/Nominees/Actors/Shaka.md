---
entryType: actor
entrySubtype: player-character
authorGM: "Ghost"
visibility: mixed
---

# Actor: Shaka (update to existing actor-shaka, revision 4)

*(Revision of existing actor `actor-shaka`. The sandbox record is a stub — no ancestry, class, level, stat block, goals, relationships or knowledge.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/shaka.json` (revision 4, updated 2026-08-04, event-traced to `event-day-0117-dawn-001`).*

| Field | Current value |
| --- | --- |
| `actorType` / `controlType` | agent / player-character |
| `partyName` | Altar of Dust |
| `role` | Halfling Altar of Dust adventurer |
| `aliases[]` | **Saka** — "current report spelling is Shaka; Saka remains an alias pending a final ruling" |
| `locationId` / `status` | location-kharanok / active |
| `goals[]` | **empty** |
| `campaignContinuity` | firstConfirmedDay 109, lastConfirmedDay **117** |
| `sourceRefs[]` | Day 109 (Feathers and Horns); Day 110 (The Shared Dream) |

**Proposed changes, all unapproved:** `goals[]` empty; no ancestry/class/level/stat block; `sourceRefs[]` stops at day 110 while `lastConfirmedDay` is 117 — ad4 through ad7 are missing; no relationships, though he is the party's decision-maker.

## One-Sentence Summary
A banished halfling thief whom the party has deliberately built into a legend — the "Cannibal King" — and who has leaned into it hard enough to cut a prisoner's ear off, chew it, and hand it back.

## Classification
- Subtype: player-character — sandbox shape `actorType: agent` + `controlType: player-character`
- Control: player-character — played by **Proskopos**, party *Altar of Dust*
- Status: active
- Current location: Kharanok (`location-kharanok`)
- Role: Thief — archer, scout, and the party's authority

## Player-Safe Description

### Appearance
Halfling in a leather harness, composite bow, wrist razor.

### Manner and Voice
Speaks only halfling. Everything he says reaches the party through an interpreter — Relo before ad7, **Sylvar** since — and Sylvar edits him upward, so the party often hears courtesy where he issued an order.

### Public Reputation
**The Cannibal King.** Built by Relo during an interrogation and then made true by Shaka himself.

## Confirmed Facts
- **ad4, day 111:** Relo presents him to the captive gith as the Cannibal King who has already eaten the man's dead companions. Shaka then asks permission, **cuts off the captive's ear, chews a piece and spits it back into his hand**, and sends him away wounded as a warning that Kharanok is under their protection.
- **ad4:** goes invisible and kills a wild kank with his bow; later cuts down three bats attacking the largest syggra in a single strike.
- **ad6, day 115:** ends the giant snake fight in the Zharvek ruins with a shot through the creature's open mouth and out the other side, while it is blinded.
- **ad7, day 117:** orders the party to search the side rooms — Sylvar relays it as a polite request to "the worthy water clerics". Sends Sylvar to fetch Tzala. Promises Dorak a share of anything valuable.
- **ad7:** pulls Ranni off the gate plate and asks her curtly, in his own language, whether that was everything she saw — she hears it translated as praise for a brave young water priestess.
- **Name:** the sandbox carries **Saka** as an alias, pending a ruling.

## Goals
1. Description: *(Proposed, from play.)* Keep the Cannibal King reputation working — it has done more than his bow has.
   - Priority: 4 · Secret: no · Status: active
2. Description: *(Proposed.)* Hold Kharanok as the party's protectorate, by intimidation where possible.
   - Priority: 4 · Secret: no · Status: active

## Traits and Pressures
- Ambition: Directive. He assigns other people tasks.
- Caution: Fights from stealth, at range, with a backstab bonus stacked three times.
- Loyalty: To the party. He is the one who decides what the party does.
- Cruelty: **Demonstrated and deliberate** — theatre with a real ear.
- Risk tolerance: Moderate; he is fragile (13 HP at level 6).
- Status: Banished from his hometown (Misery on the sheet).

## Resources and Capabilities
- **Backstab, +3 damage dice total**, plus Brutalize.
- Stealth and invisibility in practice — repeatedly the one who is not seen.
- Thievery, Agile, Know Direction.
- A reputation that does work no roll could.

## Relationships
- Player character: **Sylvar** (DarkRhapsode) — *Interpreter and dependency.* Without him Shaka cannot speak to the party at all. Sylvar softens him.
- Player character: **Relo** (Mpelos) — *Co-author of the persona.* Relo invented the Cannibal King; Shaka made it real.
- Existing actor: `actor-dorak` — *Bought off.* Promised him a share rather than threatening him.
- Existing actor: `actor-kalia` — no direct dealings recorded; she deals with Relo and Sylvar.

## Knowledge
- Subject: The gate room and everything said in it
  - Claim: The full scene, relayed by Sylvar on the walk out.
  - Source: Sylvar · Learned day: 117 · Confidence: certain · Truth status: true · Secret: no

## Current Activity
In Kharanok, directing the party's next move toward Giustenal.

## GM-Only Secrets
- Every social scene he is in passes through **one** interpreter. Removing Sylvar silences the party's decision-maker.
- The gith he mutilated was released alive to carry the story. That story is now somewhere in the gith camps.

## Proposed Developments
All unapproved. The Cannibal King reputation is an asset and a liability that has never been tested against anyone who could check it.

## Stat Block or Rules Notes
- System: **Shadowdark** — the character's Foundry sheet
- Class: **Thief** · Ancestry: **Halfling** · Level **6**, XP 30 · Alignment neutral
- HP **13/13** · AC **13**
- STR 9 · DEX 16 · CON 9 · INT 8 · WIS 11 · CHA 10
- Talents: Backstab +1 Damage Dice ×3, Brutalize, Stealthy, Agile, Backstab, Thievery, Know Direction
- Boon: Misery — banished from hometown
- Gear: Composite Bow, Arrows, Wrist Razor, Leather Harness · Ancestry ability: Bite

## Sources
- Title: Foundry VTT Shadowdark character sheet (GM-supplied)
  - Section: character sheet export · Source type: system export (9 August 2026)
  - Adaptation note: Ancestry inferred **Halfling** from the Bite/Agile traits and from his speaking halfling in play; the sheet's ancestry UUID does not resolve locally.
- Title: `mk-repos/mk-sandbox/actors/shaka.json` — revision 4, read-only. The record this nominee revises.
- Title: Darkest Sun — Altar of Dust, ad4 "It's Raining Bats and Bugs" · campaign-original, in-world day **111**
- Title: Darkest Sun — Altar of Dust, ad6 "The Sand Also Rises" · campaign-original, in-world day **115**
- Title: Darkest Sun — Altar of Dust, ad7 "City by the Silt Sea" · campaign-original, in-world day **117**

## Unresolved Questions
- **Saka vs Shaka** — the alias ruling is still open in the sandbox record.
- Whether the mutilated gith's story has reached the gith leadership.
- Whether Shaka knows how much Sylvar edits him.
