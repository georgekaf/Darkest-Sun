---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: Zharvek (update to existing location-zharvek, revision 5)

*(Revision of existing location `location-zharvek`. Everything below is a change **against these values**. The cross-campaign conflict itself is **not resolved here** — see the continuity record and MK-Sandbox #121.)*

## Current record in mk-sandbox

*Read-only snapshot of `locations/zharvek.json` (revision 5, updated 2026-08-04, event-traced to `event-day-0117-dawn-001`).*

| Field | Current value |
| --- | --- |
| `region` / `terrain` | Black Spine Region / ruins |
| `locationType` | ruined roadside settlement and former animal market |
| `control` / `population` | null / null |
| `danger` | 3 |
| `status` | "ruined and largely abandoned; seven survivors departed with Altar of Dust on Day 116, and no remaining inhabitants were confirmed" |
| `connections[]` | nibenay, sul-nok, lion-temple, quor-anok — all with real route ids |
| `mapHex` | Black Spine regional map, column 3, row 6 |
| `features[]` | Damak oversees the settlement · animal market, five kanks bought Day 110 · gith waiting for Eskar's escort · five more gith arrived Day 110 · whether they were the escort is unresolved |

**The record has already taken a position the conflict issue has not.** By carrying one `location-zharvek` that is both the day-110 animal market and the day-115 ruin, it treats the two accounts as **one place**. That is effectively option 4 of the continuity record, applied silently. Worth making explicit or backing out — but not by inference from a schema convenience.

## Proposed changes

1. **The `features[]` array mixes two eras with no temporal marking.** "Damak, a dwarf exiled from Nibenay… **oversees** the settlement" is present tense on a record whose `status` says ruined and abandoned. Either he died, was taken, or fled, and the record should not read as though he is still running a village that no longer exists. Propose date-stamping every feature and adding his fate as explicitly unknown.
2. **Days 113–116 are missing.** The record jumps from day 110 to the survivors' departure on day 116.
3. **`danger: 3` predates the sack.** A settlement that was destroyed and emptied of people is not the same risk as the market it used to be — in either direction.
4. **`control: null` is right but uninformative.** Damak's authority ended; nothing replaced it.

## Summary
A roadside settlement and animal market on the Black Spine caravan road, hosted by the dwarf Damak — and, by day 115, broken doors and empty houses with its people carried off. The two states are eight days apart in the record and the campaigns disagree about where it stands.

## Classification
- Location subtype: ruined roadside settlement and former animal market *(retained)*
- Region: Black Spine Region · Terrain: ruins
- Status: ruined and largely abandoned since some point between days 113 and 115
- Controller: **none.** Damak's authority ended with the settlement; fate unrecorded
- Contested by: unresolved — see GM-Only Secrets

## Player-Safe Arrival Description
Broken doors, empty houses, no movement anywhere. Whatever happened here took the people and left the buildings.

## Physical Features

**Proposed: date-stamp what exists, and add what is missing.**

- *Through day 110* — **Damak**, a dwarf exiled from Nibenay after trying to free a slave, oversees the settlement.
- *Day 110* — an **animal market**; House Markon bought five trained kanks here.
- *Day 110* — **gith visitors** stated indirectly that they were waiting for **Eskar's escort** and did not intend an immediate attack; five more gith arrived that morning, causing alarm. Whether they were the expected escort is still unresolved.
- *Day 113* — **Talek Vos** sets out for Zharvek with six guards to observe the gith unrest. **His arrival was never shown.**
- *By day 115* — broken doors, empty houses, no sign of life. **Most inhabitants taken as slaves into the mountains**, per survivor testimony.
- *Day 116* — **seven survivors depart with the Altar of Dust party**, among them **Tzala**, who now lives in Kharanok.

## Population and Occupants
None confirmed. Seven survivors left on day 116; one of them died before reaching Kharanok, so **six** arrived. Damak is unaccounted for.

## Resources
- Trade: **ended.** The animal market is gone with the population.
- Water, food, guards: none recorded.

## Dangers
Whatever emptied it has not been identified in play, and nothing indicates it will not return to the road.

## Connections
Retained as recorded — Nibenay, Sul-Nok, Lion Temple, Quor'Anok, each already through a real route id.

**Geography stays open.** House Markon reached it in nine hours' march **northeast** of Kharanok on the road toward Nibenay; Altar of Dust reached it travelling **south past the Salt Sea**. The `mapHex` places it at column 3, row 6 of the Black Spine map, which represents one of those and not the other. **This revision proposes no change to the hex** — the direction conflict is the part of #121 that remains genuinely unresolved.

## Local Clocks and Pressures
**Proposed:** whether anyone goes looking for Talek Vos. He is an envoy of an unnamed patron who set out for this place and did not report back.

## GM-Only Secrets

*(Proposed 2026-08-11, from the printed source. Not a ruling — offered as the mechanism the record has been missing.)*

- **The raid was a slave delivery to Dregoth.** *City by the Silt Sea* pp. 14–15: the **Silt Stalkers** are an elf raiding tribe who "delight in attacking travelers and **small settlements**". **Luubarra Fire Dagger**, their master defiler, bargained with Dregoth — the whole tribe to Giustenal in exchange for the powers of a sorcerer-king, a promise he has no intention of keeping, though "he will take all the elves she sends him". Her **Fire Dagger clan already serves him as undead warriors**. Chief **Eevuu** still refuses to send the rest, and the book's own hook is that "**if he continues to refuse, Luubarra will take matters into her own hands**."
- Zharvek's people being **carried off as slaves** is therefore printed faction behaviour, not invention. It explains the survivors' account without contradicting any session.
- **What it costs to accept:** only the survivors' estimate of *when*. Move the sack into the **day 113–115** window and no session is contradicted and no date shifts. Frightened refugees misjudging "about two weeks" is the exact weakness the continuity record already attributes to their testimony.
- **Talek Vos is proposed as a victim of the same raid** — himself and his six guards taken with the rest. His arrival was never shown, his patron never named, his report never made, and his own record notes that all three "require later confirmed events". Seven more bodies is precisely what Luubarra needs while Eevuu keeps refusing.
- **Damak's fate is the other open question.** He was the settlement's authority; he is not among the seven survivors.
- **This does not touch the geography.** Northeast versus south past the Salt Sea remains unexplained and should stay that way until ruled.

## Proposed Developments
All unapproved.
- Somebody eventually notices an envoy under terracotta and beige dragonfly banners never came home. That is the cheapest way to force the question at the table.
- Tzala lives in Kharanok now. If anyone asks her where she came from and which way she walked, the direction conflict surfaces on its own.

## Sources
- Title: `mk-repos/mk-sandbox/locations/zharvek.json`
  - Section: full entry, revision 5 · Source type: campaign record (read-only)
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
  - Adaptation note: The sack date within it is **survivor testimony**, not narration.
- Title: City by the Silt Sea — Campaign Book
  - Section: The Silt Stalkers; Luubarra Fire Dagger
  - Printed page: **14–15**
  - Source type: official
  - Adaptation note: Source of the proposed mechanism. Nothing about Zharvek itself appears in the book.
- Title: the campaign continuity record for Zharvek
  - Section: full record · Source type: campaign continuity record
  - Adaptation note: **Unresolved.** Four options recorded, working position "option 4-adjacent, held open".

## Unresolved Questions
- **Direction.** Northeast of Kharanok, or south past the Salt Sea? Untouched by this revision.
- **When exactly was it sacked?** The proposal needs only that it fall between days 113 and 115.
- **What happened to Damak?**
- **Does anyone come looking for Talek Vos?**
- Whether keeping one `location-zharvek` for both states should be made an explicit ruling rather than a silent one.
