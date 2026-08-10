---
entryType: actor
entrySubtype: player-character
authorGM: "Ghost"
visibility: mixed
---

# Actor: Relo (update to existing actor-relo, revision 4)

*(Revision of existing actor `actor-relo`. The sandbox record is a stub: it has no ancestry, no class, no stat block, no goals, no relationships and no knowledge. Everything below is a change **against these values**.)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/relo.json` (revision 4, updated 2026-08-04, event-traced to `event-day-0117-dawn-001`).*

| Field | Current value |
| --- | --- |
| `id` | actor-relo |
| `actorType` | agent |
| `controlType` | player-character |
| `partyName` | Altar of Dust |
| `role` | Psionic Altar of Dust adventurer |
| `status` / `canonStatus` | active / campaign-original |
| `locationId` | location-kharanok |
| `factionId`, `routeId` | null |
| `goals[]` | **empty** |
| `simulation` | proposalMode `excluded` — "Player characters act only through GM-confirmed table play." |
| `campaignContinuity` | firstConfirmedDay 109, lastConfirmedDay **117**, party Altar of Dust |
| `sourceRefs[]` | Campaign Record Day 109 (Day at Kharanok); Day 110 (The Shared Dream) |

**Proposed changes, all unapproved:**

- **`goals[]` is empty** — propose the two goals below, both drawn from play.
- **No ancestry, class, level or stat block** is stored. Propose recording Elf / Psionicist / level 4 from the Foundry export, in whatever field shape the schema allows.
- **`sourceRefs[]` stops at day 110.** Days 115 and 117 are the two most consequential sessions he has had (Zharvek recruitment; the second contact with the cave creature). Propose adding ad4–ad7.
- **No relationships or knowledge are recorded.** Propose the entries below — in particular the cave creature contact, which is the only open channel any PC has to a non-human intelligence.

## One-Sentence Summary
An elf psionicist abandoned at birth who has made himself the party's negotiator, tracker and interrogator — and who has twice now opened his own mind to something older and stronger than he is, once to bargain with it and once to be pinned to a wall by it.

## Classification
- Subtype: player-character — stored in the sandbox as `actorType: agent` + `controlType: player-character`
- Control: player-character — played by **Mpelos**, party *Altar of Dust*
- Status: active
- Faction or allegiance: none; de facto voice of the Altar of Dust party
- Current location: Kharanok (`location-kharanok`)
- Current route, when traveling: none standing
- Role: Psionicist — The Way, tracking, and every conversation that matters

## Player-Safe Description

### Appearance
Elf, in a leather harness, composite bow across his back. Carries little; he cannot bear much weight.

### Manner and Voice
Speaks first and speaks for everyone — announces the party as envoys of the Cannibal King, offers shelter and food to the willing and death to the hostile, in the same breath. Threatens freely and follows through rarely.

### Public Reputation
In Kharanok: the one who talks. In Zharvek: the man who offered seven starving people a way out and kept the offer.

## Confirmed Facts
- **ad4:** turns a stone into a needle with a psionic spell and drives it under the captive Gith's fingernail to make him talk, while claiming Shaka has already eaten pieces of his dead companions — presenting him as the fearsome **"Cannibal King"** to increase the pressure. The captive breaks and reveals further tunnels beneath the mines.
- **ad4:** translates for Shaka in the interrogation, before Sylvar existed.
- **ad5:** hollows the ground so the wild kanks stumble, then — remembering the sound Sira the village animal handler taught him — calms the two surviving kanks instead of fighting them, walking them home tame. Voted MVP of the episode.
- **ad6, day 115:** senses an indistinct presence, human or Gith, north in the Zharvek ruins; the party moves quietly and passes unnoticed. Later senses seven human presences around the dry well, opens the negotiation, and brings **Tzala and six others** back to Kharanok as crafter, recruits and workers.
- **ad6:** tries and fails to frighten the giant snake by projecting images of destruction into its mind.
- **ad7, day 117:** tracks the missing Dorak through the mines with The Way — direction only, no detail.
- **ad7:** threatens to enter Dorak's mind and take what he wants; Dorak refuses him permission and says he is not Gith, to be treated that way. Relo shapes a stone into a needle again and turns it on him.
- **ad7:** recognises Breck as the gate guard who once refused him entry to Kharanok, and afterwards confronts him — telling him he will be watched from now on. Breck does not flinch.
- **ad7:** finds the hollow flagstone that hides the library of thirty to forty rolled hides, and fetches Zephyr down to read them.
- **ad7:** asks Ranni to carry the Crystal Dust because he cannot bear the weight.
- **ad7:** reaches out with The Way for any activity akin to his own and touches **the bound cave creature** again, inside a Kharanok built from his own memories. It refuses his offer, tells him it felt the one who holds its binding among the party that day, and describes what came through the gate: something that hunts people to replace its dead and sounds like the voices of thousands, which it heard once thousands of years ago and could not itself face. When Relo lets slip too much about Nibenay and tries to close his mind, **it lifts him into the air and pins him against the shade houses**, warning him that he came alone and opened his own mind.
- **ad7:** asks Breck what deadline the Veiled Alliance gave, and is told that taking on a Sorcerer King as they are is suicide — they need an army or another Sorcerer King as an ally.

## Goals
1. Description: Get the party — and himself — out of Kharanok with something to show for it.
   - Priority: 4
   - Progress: ongoing
   - Secret: no
   - Status: active
2. Description: *(Proposed, from play.)* Learn what the cave creature is and what freeing it would cost.
   - Priority: 5
   - Progress: he has its terms and has not accepted them
   - Secret: partly — the party knows the offer, not his appetite for it
   - Status: active

## Traits and Pressures
- Ambition: High, and increasingly aimed at Nibenay.
- Caution: **Selective.** Careful in the field, reckless with his own mind.
- Loyalty: To the party. He does the talking so they do not have to.
- Cruelty: **Instrumental** — torture as leverage, twice, both times to open a mouth rather than to hurt.
- Risk tolerance: High.
- Wealth: Nothing of note.
- Status: The party's public face.

## Resources and Capabilities
- **The Way** — psionic sensing of minds and activity at range, direction-finding, and contact with non-human intelligences.
- **Matter shaping** — stone to needle, ground to hollow, used both as tool and as threat.
- **Mind Blank** and **Psionic Sense** as class abilities.
- **Charm and Speak** — the social spells that back up the negotiating.
- Literacy, which almost nobody in Kharanok has.

## Relationships
- Existing actor or faction ID: `actor-breck`
  - Attitude: **Watchful, declared**
  - Reason: Told Breck to his face he would be watching him; Breck told him to watch as long as he likes.
- Existing actor or faction ID: `actor-dorak`
  - Attitude: **Coerced, then courted**
  - Reason: Threatened him with a stone needle, then offered to leave Kharanok together. Dorak laughed at the idea of travelling with an elf.
- Existing actor or faction ID: `actor-kalia`
  - Attitude: Working
  - Reason: Takes her tasks and returns her people.
- Player character: **Ranni** (Fantasias Giorgos)
  - Attitude: Trusts her with the stores
  - Reason: He cannot carry weight; she can.
- Player character: **Shaka** (Proskopos)
  - Attitude: Interpreter before Sylvar, ally after
  - Reason: Built the Cannibal King persona around him and has used it in negotiations since.
- **The bound cave creature** (unnamed, no id)
  - Attitude: **Open channel, unequal terms**
  - Reason: Two contacts. It builds a Kharanok out of his memories to speak in; the last exchange ended with him pinned to a wall.

## Knowledge
- Subject: What came through the gate
  - Claim: Something that hunts people to replace its dead, sounding like the voices of thousands, which the cave creature heard once thousands of years ago and cannot face.
  - Source: the cave creature
  - Learned day: 117
  - Confidence: certain that it was said
  - Truth status: **true — it is the Caller in Darkness**, which he does not know. See [[The Caller in Darkness]].
  - Secret: he told the whole party
- Subject: The cave creature's terms
  - Claim: It will show him the road he must take if he brings what binds it — and that road runs through where the energy came from.
  - Source: direct
  - Learned day: 117
  - Confidence: certain
  - Truth status: unverified
  - Secret: no
- Subject: The Veiled Alliance's assessment
  - Claim: A Sorcerer King cannot be opposed without an army or another Sorcerer King.
  - Source: Breck
  - Learned day: 117
  - Confidence: high
  - Truth status: consistent with everything else on record
  - Secret: no

## Current Activity
In Kharanok, planning the return trip through the gate to Giustenal.

## GM-Only Secrets
- He has opened his mind to the cave creature twice and been warned about it once, in the most physical way available to a thing with no body. A third contact is his own decision, and it will not be gentler.
- He told a bound ancient entity that there is a Sorcerer King who must die. That information is now outside the party.

## Proposed Developments
All unapproved.
- The party assumes **Breck** holds the creature's binding. **They are wrong — [[Dorak]] holds it** *(GM disclosure, 2026-08-09: a lion's-head medallion of almost fire-red gemstone, casts fireball, bonded to the creature)*. Relo has pointed his surveillance at the wrong man and threatened the right one, twice, without ever finding out. The creature's price — *bring me what binds me* — is currently in the pocket of the person operating his only route out of Kharanok.
- The creature's road "runs through where the energy came from" points at Giustenal, which is also where the Caller found Ranni. Two threads, one destination.

## Stat Block or Rules Notes
- System: **Shadowdark** — from the Foundry the character's Foundry sheet
- Class: **Psionicist** (resolves to `system/classes/psionicist.json`) · Ancestry: **Elf** · Level **4**, XP 24 · Alignment neutral
- HP **15/15** · AC **10** · Luck spent
- STR 11 · DEX 14 · CON 14 · INT 11 · WIS 9 · CHA 14 (a **+2 to Charisma** talent is on the sheet)
- Spells: Hand 1: Interact · Matter 1: Shape · Matter 2: Conform · Voice 1: Speak · Voice 2: Charm · Mind 1: Lash · Eye 1: Sense
- Class abilities: Psionic Sense, Mind Blank
- Talents: Spellcasting (Psionicist), Literacy, Never Ride, Runners, Wasteland Ambusher, Farsight
- Boon: **Misery — abandoned at birth** · Effect: **Scar (DEX)**
- Gear: Leather Harness, Composite Bow, Arrows, Water, Torches

## Sources
- Title: Foundry VTT Shadowdark character sheet (GM-supplied)
  - Section: character sheet export
  - Printed page: —
  - Source type: system export (9 August 2026)
  - Adaptation note: Level, HP, abilities, spells, talents, boon, scar and gear verbatim. Ancestry confirmed **Elf** — the sheet's ancestry UUID is the same one Ranni carries, and the roster lists both as elves.
- Title: Darkest Sun — Altar of Dust, ad4 "It's Raining Bats and Bugs"
  - Section: the Gith interrogation
  - Printed page: —
  - Source type: campaign-original (actual play, 25 July 2026)
- Title: Darkest Sun — Altar of Dust, ad5 "The Bug Whisperers... Finally!"
  - Section: the kank hunt
  - Printed page: —
  - Source type: campaign-original (actual play, 26 July 2026)
- Title: Darkest Sun — Altar of Dust, ad6 "The Sand Also Rises"
  - Section: Zharvek — the snake, the survivors, the recruitment
  - Printed page: —
  - Source type: campaign-original (actual play, 31 July 2026, in-world day 115)
- Title: Darkest Sun — Altar of Dust, ad7 "City by the Silt Sea"
  - Section: the hunt for Dorak; Breck; the gate room; the second contact with the cave creature
  - Printed page: —
  - Source type: campaign-original (actual play, 7 August 2026, in-world day 117)
- Title: the campaign character roster
  - Section: Altar of Dust roster
  - Printed page: —
  - Source type: campaign reference doc
  - Adaptation note: Roster lists Elf Psionicist **level 3**; the sheet export gives **level 4**. The sheet is the newer record.
- Title: `mk-repos/mk-sandbox/actors/relo.json`
  - Section: full entry, revision 4
  - Printed page: —
  - Source type: campaign record (read-only)
  - Adaptation note: The record this nominee revises. Event-traced to `event-day-0117-dawn-001`; stub-level detail only.

## Unresolved Questions
- Whether Relo intends to free the cave creature, and whether he has told the party the whole of what it offered.
- What the creature meant by the road running "through where the energy came from".
- Whether the party confronts Breck about the binding, and whether Relo leads that.
- Roster level (3) is stale against the sheet (4) — worth correcting in `character_roster.md`.
