---
entryType: actor
entrySubtype: player-character
authorGM: "Ghost"
visibility: mixed
---

# Actor: Ugo (update to existing actor-ugo, revision 3)

*(Revision of existing actor `actor-ugo`. Stub record — and the only Altar of Dust PC the sandbox has already marked **inactive**.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/ugo.json` (revision 3, updated 2026-07-22).*

| Field | Current value |
| --- | --- |
| `actorType` / `controlType` | agent / player-character |
| `partyName` | Altar of Dust |
| `role` | Altar of Dust adventurer |
| `locationId` | location-kharanok |
| `status` | **inactive** |
| `goals[]` | **empty** |
| `campaignContinuity` | firstConfirmedDay 109, lastConfirmedDay **109** — *"Ugo is absent from the later Day 109 and Day 110 rosters; no death or departure was confirmed."* |
| `sourceRefs[]` | Day 109 (Day at Kharanok — Find the GOAT) |

**Proposed changes, all unapproved:**

1. `goals[]` empty; no ancestry, class, level or stat block. Propose **Half-Giant Fighter 5** from the sheet.
2. **The record and the sheet disagree about whether this character is in play.** The sandbox says inactive since day 109. The sheet says **level 5, XP 9, masterwork helmet and masterwork gloves, weapon mastery** — that is a character who has been advanced well past a single day's play. **Propose the owner reconcile this.**
3. `lastConfirmedDay: 109` should stand until someone confirms an appearance; the sheet is not an in-world event.

## One-Sentence Summary
A half-giant fighter carrying the best equipment in the party, marked inactive in the world record since day 109 — a character who has clearly kept levelling somewhere the campaign record cannot see.

## Classification
- Subtype: player-character — sandbox shape `actorType: agent` + `controlType: player-character`
- Control: player-character — played by **Nio**, party *Altar of Dust*
- Status: **inactive** in the sandbox; the sheet suggests otherwise
- Current location: Kharanok (`location-kharanok`)
- Role: Fighter — heavy melee and hauling

## Player-Safe Description

### Appearance
Half-giant in large bone plate with a masterwork helmet, masterwork gloves, a great club, a warhammer and a bone shield. STR 17.

### Manner and Voice
Not recorded. INT 5.

### Public Reputation
Not recorded.

## Confirmed Facts
- Present in the campaign record for **day 109** ("Day at Kharanok — Find the GOAT").
- **Absent from the later day 109 and day 110 rosters.** No death and no departure were ever confirmed — the sandbox note says so explicitly.
- Not present in ad4 (111), ad5 (112), ad6 (115) or ad7 (117).
- The sheet shows him at **27 of 33 HP** — wounded, and not from anything on record.

## Goals
1. Description: *(Proposed — nothing stated at the table.)* Unstated.
   - Priority: — · Secret: unknown · Status: unknown

## Traits and Pressures
- Ambition: Unmeasured.
- Caution: Unmeasured.
- Loyalty: Unmeasured.
- Cruelty: Unmeasured.
- Wealth: **The best-equipped character in the party** — two masterwork items and a warhammer.
- Status: Vanished without an in-world explanation.

## Resources and Capabilities
- **Half-giant frame**: Giant's Grip, Huge Body, Durability, +2 to Strength.
- **Fighter talents**: Weapon Mastery, Grit (Strength), Hauler, +1 to Melee and Ranged Attacks ×2.
- **Phase** — on a fighter sheet, and unexplained.
- Warhammer, great club, bone plate, bone shield, grappling hook.

## Relationships
None recorded. He left the roster before the current party formed.

## Knowledge
Nothing recorded.

## Current Activity
Unknown. The world record has him inactive at Kharanok since day 109.

## GM-Only Secrets
- **This is a continuity hole, not a retired character.** A named PC left the roster mid-day with no death, no departure and no explanation, and has been quietly advancing ever since. That is either an unrecorded absence to be explained or a character due to walk back in.
- **Phase** on his sheet is unexplained, exactly as Telekinetic Grasp is on Gur-da's. Both are half-giants with an ability their class does not obviously grant.
- **Ugo has never been to Giustenal.** *(GM confirmation, 2026-08-09.)* [[Ranni]] is the only player character who has been there. Wherever his missing days went, they did not go there — and the Caller in Darkness **ignores half-giants**, so if he ever does go, it will not target him.

## Proposed Developments
All unapproved.
- The simplest in-world explanation — he was hauling for someone, somewhere, and is owed wages — costs nothing and closes the hole.
- Returning him fully equipped at level 5 is a gift to a party that is short on melee since Gur-da and Rhugor stopped appearing.

## Stat Block or Rules Notes
- System: **Shadowdark** — the character's Foundry sheet
- Class: **Fighter** · Ancestry: **Half-Giant** · Level **5**, XP 9 · Alignment neutral
- HP **27/33** — wounded · AC **10**
- STR 17 · DEX 11 · CON 11 · INT 5 · WIS 10 · CHA 10
- Talents: Giant's Grip, Huge Body, Durability, Weapon Mastery, Grit (Strength), Hauler, +1 to Melee and Ranged Attacks ×2, +2 to Strength, **Phase**
- Gear: Bone Plate (Large), Bone Shield, Masterwork Helmet, Masterwork Gloves ×2, Great Club, Warhammer, Grappling Hook, Rope 60', Rations ×2, Torch ×2, Firekit

## Sources
- Title: Foundry VTT Shadowdark character sheet (GM-supplied)
  - Section: character sheet export · Source type: system export (9 August 2026)
  - Adaptation note: Ancestry inferred **Half-Giant** from Giant's Grip / Huge Body, matching Gur-da's ancestry UUID exactly.
- Title: `mk-repos/mk-sandbox/actors/ugo.json` — revision 3, read-only. The record this nominee revises, including the inactive status and its note.
- Title: Darkest Sun Campaign Record — Day 109, "Day at Kharanok — Find the GOAT" · campaign-history

## Unresolved Questions
*(All four answered by the campaign owner, 13 August 2026.)*

- ~~Is Ugo in play or not?~~ — **ruled: he is an occasional player character.** In play, with a player who attends now and then; the record should read as an active PC with intermittent presence, not as inactive or retired. Squares with the 11 August note that "Ugo simply hasn't been active, he just does stuff around Kharanok".
- ~~Where the level 5, the XP and the masterwork gear came from~~ — **ruled: the level and XP come from the sessions he played.** **Masterwork items are built by the characters themselves, spending downtime and gold** — a general campaign rule, so no supplier or loot source needs inventing.
- ~~Where Phase comes from~~ — **ruled: it is his wild talent.** Not a class grant, so nothing about his class needs explaining.
- ~~What wounded him~~ — **ruled: some fight, and it does not matter.** Ordinary unhealed damage from play around Kharanok; the record carries no cause.
