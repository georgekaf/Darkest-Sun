---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: Zharvek (update to existing location-zharvek, revision 9)

*(Revision of existing location `location-zharvek`, now at revision 8. Everything below is a change **against those values**. The three questions this issue carried on 12 August 2026 — direction, sack window, one record or two — were ruled then and are already merged into revision 8; they are not reopened here. What follows is the campaign owner's ruling on the two questions deliberately left open.)*

## Current record in mk-sandbox

*Read-only snapshot of `locations/zharvek.json` (revision 8, updated 2026-08-13, event-traced to `event-day-0115-dusk-003`, `event-day-0115-dusk-004`, `event-day-0117-dawn-001`).*

| Field | Current value |
| --- | --- |
| `region` / `terrain` | Black Spine Region / ruins |
| `locationType` | ruined roadside settlement and former animal market |
| `control` / `population` | null / null |
| `danger` | 3 |
| `status` | ruined and largely abandoned by Day 115 after repeated raids beginning around Day 101 and final emptying during the Day 113–115 window |
| `connections[]` | nibenay, sul-nok, lion-temple, quor-anok — all with real route ids |
| `mapHex` | Black Spine regional map, column 3, row 6 — confirmed correct |
| `features[]` | eleven entries, all date-stamped; one place across both eras; bearings confirmed; Damak oversaw the settlement Days 109–110; Talek Vos departed Day 113, arrival not recorded |
| `unresolvedDetails[]` | exact day/watch and attackers · **Damak's fate and whether anyone will search for Talek Vos** · whether House Markon's Day 110 departure mattered causally |

**Revision 8 is sound and this revision leaves nearly all of it alone.** Three of its `features[]` and two of its three `unresolvedDetails` are untouched below.

## Proposed changes

1. **Both open fates are answered.** Talek Vos and Damak were taken alive and are **imprisoned at Cromlin**, held for delivery to Dregoth by **Luubarra Fire Dagger**. The rest of Zharvek's people **have already been delivered**.
2. **The final emptying now has a timestamp: Day 114, Night.** Revision 8 records the Day 113–115 window with "the exact day and watch remain unknown". That clause can be retired.
3. **The attackers are identified, and the survivors were not wrong.** Feature 9 records survivor testimony attributing the raid to *gith*. **Gith were genuinely raiding Zharvek.** What the testimony does not capture is that **Zarron's pirates — the Silt Stalkers under Luubarra Fire Dagger — took advantage of the chaos** and carried off the population on the night of Day 114. Two forces, one settlement, and the villagers only saw the one that had been attacking them for weeks. The testimony stands as accurate about what it witnessed and incomplete about what happened.
4. **`danger: 3` is left alone.** Nothing in this ruling bears on it.

## Summary
A roadside settlement and animal market on the Black Spine caravan road, emptied on the night of Day 114 by Silt Stalker raiders feeding Dregoth's slave demand. Its people are gone to Giustenal. Two of them — the dwarf who ran the place and a House Shom envoy who rode in at the wrong moment — are still alive at Cromlin, waiting their turn.

## Classification
- Location subtype: ruined roadside settlement and former animal market *(retained)*
- Region: Black Spine Region · Terrain: ruins *(retained)*
- Status: ruined and abandoned; emptied **Day 114, Night**
- Controller: **none** *(retained)*
- Raiders: **`faction-silt-stalkers`**, under Luubarra Fire Dagger

## Player-Safe Arrival Description
Broken doors, empty houses, no movement anywhere. Whatever happened here took the people and left the buildings.

## Physical Features

**Proposed: revision 8's eleven features are retained. Three change, two are added.**

Changed:

- *Feature 8* — the settlement endured repeated raids from roughly Day 101 onward and was **finally emptied on the night of Day 114**. The window language and "the exact day and watch remain unknown" are retired.
- *Feature 9* — by Day 115 the settlement had broken doors, empty houses and no visible activity. Survivor testimony attributed the disappearance to **a gith raid**, and **gith were in fact raiding the settlement**. The testimony is retained as accurate, with the addition that **the people were carried off by Zarron's pirates, who exploited the chaos of the gith raiding**.
- *Feature 10* — Talek Vos departed on Day 113 with six guards to investigate gith unrest. **He reached Zharvek and was taken in the Day 114 raid.** His arrival, unrecorded in play, is confirmed by the ruling on his fate.

Added:

- *Day 114, Night* — the settlement is emptied by **Silt Stalker raiders under Luubarra Fire Dagger**, gathering slaves for delivery to **Dregoth** at Giustenal.
- *After Day 114* — the captives are **taken to Cromlin** and held there. **Most have already been delivered.** **Damak of Zharvek** and **Talek Vos** are still held.

## Population and Occupants
None on site. Seven survivors left on Day 116 and six reached Kharanok. The rest of the population is **accounted for**: taken to Cromlin, and delivered onward to Dregoth except for the two named prisoners.

## Resources
Unchanged from revision 8.

## Dangers
The raiders are now named. `faction-silt-stalkers` took this settlement and has a standing reason to take more: Luubarra owes Dregoth a tribe she does not command, and Chief Eevuu keeps refusing to supply it. Every settlement on this road is a substitute.

## Connections
Unchanged. Nibenay, Sul-Nok, Lion Temple, Quor'Anok, each through a real route id. The bearings confirmed in revision 8 stand.

**A new link is owed, but not as a `connections[]` route.** Zharvek's people went to **Cromlin**, and from Cromlin to **Giustenal**. That is a slave-traffic relationship, not a road this settlement offers travellers, and it belongs on the two actor records and on `location-cromlin` rather than in this location's route list.

## Local Clocks and Pressures
- **The delivery clock.** Two prisoners remain at Cromlin and the rest of the consignment is already gone. Whatever interval Luubarra runs her deliveries on is the interval in which they stop being rescuable.
- **Nobody is looking yet.** Talek Vos's patron is **House Shom**. **Vasara is dead** and cannot raise the question. **Doren Shom will eventually wonder** — proposed, not scheduled.

## GM-Only Secrets

*(Ruled by the campaign owner. The mechanism below was proposed on 2026-08-11 from the printed source; it is now confirmed as what happened.)*

- **The raid was a slave delivery to Dregoth, and it is Luubarra's.** *City by the Silt Sea* pp. 14–15: the **Silt Stalkers** are an elf raiding tribe who "delight in attacking travelers and **small settlements**". **Luubarra Fire Dagger**, their master defiler, bargained with Dregoth — the whole tribe to Giustenal in exchange for the powers of a sorcerer-king, a promise he has no intention of keeping, though "he will take all the elves she sends him". Her **Fire Dagger clan already serves him as undead warriors**. Chief **Eevuu** still refuses to send the rest, and the book's hook is that "**if he continues to refuse, Luubarra will take matters into her own hands**." Zharvek is her taking matters into her own hands.
- **Cromlin is the staging point.** The captives are held there and delivered onward. Cromlin is a House Shom trading village of 1,200 about twenty miles west of Giustenal — the last stop before the buried city, and a place where a slave consignment can sit without looking unusual.
- **Two prisoners are still alive there: Damak and Talek Vos.** Why these two were held back when the rest went forward is not stated.
- **Two forces, and the survivors only saw one of them.** Gith were genuinely raiding Zharvek — they had been present on Day 110 and had alarmed the village four days before the end. **Zarron's pirates took advantage of the ensuing chaos** and took the people. From inside the village that is indistinguishable from a gith raid that finally succeeded, which is exactly what the refugees reported. **Nothing in their account needs correcting; it needs completing.**
- **The gith raiding is therefore not background.** It is the cover the slave-taking operated behind, and it may not have been coincidental.
- **Talek Vos was riding for House Shom.** His patron is confirmed; the dragonfly banners are still unexplained.

## Proposed Developments
All unapproved.
- **Doren Shom eventually wonders.** He is a bastard son proving his worth against legitimate siblings; a House Shom envoy who never reported is either a problem he can solve visibly or a failure that attaches to someone else. No day is proposed.
- Tzala lives in Kharanok and watched her village emptied by people she believes were gith. If she ever sees a Silt Stalker, she will not recognise them — and if she ever sees a gith, she will.
- Anyone tracing the consignment backwards from Giustenal arrives at Cromlin while two prisoners are still in it.

## Sources
- Title: `locations/zharvek.json`
  - Section: full entry, revision 8 · Source type: campaign record (read-only)
  - Adaptation note: The record this nominee revises.
- Title: Darkest Sun, s3 ep.11 "The Shadow King"
  - Section: the stay at Zharvek, Damak, the gith waiting for Eskar's escort
  - Source type: campaign-original (actual play, in-world days **109–110**)
- Title: Darkest Sun, s3 ep.19 "Bloody Red Oasis"
  - Section: Talek Vos rides for Zharvek with six guards
  - Source type: campaign-original (actual play, in-world day **113**)
- Title: Altar of Dust, ad6 "The Sand Also Rises"
  - Section: the ruined settlement, the seven survivors, the night departure
  - Source type: campaign-original (actual play, in-world days **115–116**)
  - Adaptation note: The raid attribution within it is **survivor testimony**, and this revision records it as accurate but incomplete — gith were raiding; the pirates took the people.
- Title: City by the Silt Sea — Campaign Book
  - Section: The Silt Stalkers; Luubarra Fire Dagger
  - Printed page: **14–15**
  - Source type: official
  - Adaptation note: Source of the mechanism the owner has now confirmed. Nothing about Zharvek itself appears in the book.
- Title: campaign owner ruling, 2026-08-13
  - Section: Talek Vos and Damak's fate; the Day 114 Night timestamp; House Shom as Vos's patron
  - Source type: GM input
  - Adaptation note: Supplied as GM input. Under `rules/03-input-time-and-world.md` §9 it enters through this issue; no confirmed event record is claimed here.
