---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: House M'ke Village

*(New location. **No record exists in mk-sandbox** — verified 2026-08-12 against `locations/` on the default branch. Proposed id `location-house-mke-village`. `location-cromlin` and `location-raam` resolve; both already mention House M'ke.)*

## Summary
A House M'ke village somewhere out across the Silt Shoals, whose value is that almost nobody can find it — the navigators who know the route are in high demand and have every reason never to draw a map.

## Classification
- Location subtype: merchant house settlement
- Region: across the Sea of Silt, off the Silt Shoals
- Terrain: silt coast — precise position unrecorded
- Parent location: —
- Status: active
- Controller: **House M'ke**
- Contested by: silt pirates, in the shoals rather than at the village

## Player-Safe Arrival Description
Not recorded. The book withholds the village itself; what it describes is the difficulty of getting there.

## Physical Features
- Not recorded.

## Population and Occupants
- House M'ke personnel. Numbers not given.

## Resources
- Trade: **silt skimmer construction and maintenance** is House M'ke's known speciality — few vessels are built each year, but each commission is worth a great deal.
- Water, food, guards: not recorded.

## Important Actors and Factions
- `faction-house-mke` — **needs checking; House M'ke is named in `cromlin.json` and `raam.json` but may have no faction record.**
- `actor-garreth-brodden` — existing sandbox record. House M'ke's Master Trader in Cromlin, and the campaign's live contact with the house.

## Dangers
- **The route, not the destination.** Silt pirates work the shoals; the navigators who know the way to the village are few.

## Opportunities
- **The navigators are the asset.** Only a brave few know the route, none of them will map it, and their wages reflect it. Anyone who acquires that knowledge acquires the house's exposure.

## Connections
- Destination: **Cromlin**
  - Existing location ID: `location-cromlin`
  - Travel notes: via the Silt Shoals, which the book treats as a single winding path between Cromlin and Break Shore, with the M'ke village branch known to very few.
- Destination: **Break Shore** — a feature of the shoals route rather than its own record.

## GM-Only Secrets
- None printed. The secrecy *is* the entry.

## Proposed Developments
All unapproved.
- **A route record, not a location record, may be the right answer for the Silt Shoals** — it has two endpoints, a hazard profile and a secrecy premium. This nominee assumes the village is a place and the shoals are the way there.
- Garreth Brodden is the obvious way in: he respects Crost and House Shom openly, and does what he likes quietly.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two: Giustenal Environs — the Silt Shoals; House M'ke
  - Printed page: **15**, with the skimmer-construction trade at **18**
  - Source type: official
  - Adaptation note: The village's existence, the branch route, the few navigators, their refusal to map it and their wages are printed, as is House M'ke's skimmer-building business.
- Title: `mk-repos/mk-sandbox/actors/garreth-brodden.json`
  - Section: full entry, revision 3
  - Printed page: —
  - Source type: campaign record (read-only)
  - Adaptation note: The house's factor in Cromlin already exists. Not edited.

## Unresolved Questions

*(All three answered 13 August 2026.)*

- ~~Where the village actually is~~ — **deliberately unmapped, and that is the recorded fact.** It lies out on the Silt Sea off the shoal path between **Cromlin and Break Shore**. The book: "Only a brave few know the route to the House M'ke village… **None of them ever make a map of the Silt Shoals**, for to do so would endanger their livelihood, or at least reduce the exorbitant wages they command." Reaching it means hiring one of those navigators.
- ~~Whether `faction-house-mke` exists~~ — **it does**: `faction-house-mke`, revision 2, status active. Cite it as controller.
- ~~Whether the Silt Shoals belong in `routes/`~~ — **yes: a route** (owner's ruling, 13 August 2026; an earlier "location" call was reversed the same day). `route-silt-shoals` carries the crossing between Cromlin and Break Shore — distance, travel turns, water cost, hazards — while **this village stays a location** whose only access runs along it, reachable solely by hiring one of the navigators who refuse to map it.
