---
entryType: location
entrySubtype: ruin
authorGM: "Ghost"
visibility: mixed
---

# Location: Dregoth's Palace

*(New location. **No record exists in mk-sandbox** — verified 2026-08-12 against `locations/` on the default branch. Proposed id `location-dregoths-palace`. Parent `location-giustenal-ruins` resolves. Not to be confused with `location-dread-palace` (proposed), which is his **current** palace in the city below.)*

## Summary
The abandoned seat of Dregoth's power in the ruins above — sixteen mapped rooms of looted grandeur on the edge of the Sea of Silt, with the only staircase to his tower rising out of its ante-chamber.

## Classification
- Location subtype: ruined palace, dungeon-scale
- Region: Giustenal ruins, area 7 — the centre of the city
- Terrain: silt-buried ruin on the Silt Sea edge
- Parent location: `location-giustenal-ruins`
- Status: ruined and looted; structurally standing
- Controller: nobody
- Contested by: silt creatures, scavengers, and whatever the Caller sends

## Player-Safe Arrival Description
The great doors are shattered and the dust inside is knee-deep. On the east wall of the entrance hall, a mural shows this city beside blue water. The throne at the north end has crumbled.

## Physical Features — the sixteen rooms
1. **Grand Entrance** — shattered doors, knee-deep dust, the blue-water mural east, an engraved templar mural west, crumbled throne, secret passage to room 3.
2. **Banquet Hall** — cracked northern wall, a mammoth cupboard of shattered plates. **A sink worm attacks through an opening in the north wall, out of the Silt Sea.** [[Nallan]] retrieved pottery here.
3. **Preparation Room** — where Dregoth met his High Templar. Locked at **−20% to pick locks**. A metal telescope (30 gp), silver bowls and mirrors (15 gp).
4. **Kitchen** — corpses shackled beneath rubble; hole in the roof.
5. **Storeroom** — looted almost bare.
6. **Ballroom** — a 40-foot carved table, 24 gp if removed and restored.
7. **Templars' Apartments, low rank** — four beds each, looted; a dragon medallion, Dregoth's holy symbol, can be found.
8. **Templars' Apartments, high rank** — two beds each; a collapsed room with Type C treasure under the rubble.
9. **Dining Hall** — great wooden tables at 15 sp each; 5% per turn of finding plate or cutlery worth 2d6 sp.
10. **Baths** — dry, silt-filled.
11. **Barracks** — dust and bones.
12. **Spire Ante-Chamber** — Cleansing Wars artifacts; a tapestry of Dregoth against [[Taraskir the Lion]]; the graffito **"The Lion-King Lives!"**; stairs down to the tunnels; a secret door, now easily spotted; two pedestals holding a marble dragon and a shattered bust of Dregoth; **the only staircase to Dregoth's Tower.**
13. **High Templar's Chamber** — [[Mon-Adderath]]'s room, barely damaged. Gray marble table, turquoise-inlaid desk (turquoise 2 gp; desk and table 3 gp each).
14. **Guest Room** — looted; a corpse with **ring of protection +2**, ribs cracked as if by a dull blade.
15. **High Priest's Quarters** — incense of meditation in a jammed drawer. **The high priest's body is staked to the tower outside.**
16. **Slave Quarters** — pillows, wine pitchers, leather bonds, a few corpses.

## Population and Occupants
- None living. A sink worm at room 2; undead and scavengers elsewhere in the ruins.

## Resources
- Trade: none. Salvage only, itemised above.
- Water: none. The baths are dry.

## Important Actors and Factions
- `actor-dregoth`, `actor-mon-adderath`, `actor-high-priest-absalom` — existing records; the palace's former occupants, all three now below.
- `actor-taraskir` — existing record; the tapestry and the graffito are about him.
- `actor-nallan` — proposed id, filed; his pottery run reached room 2.

## Dangers
- The sink worm in the banquet hall, entering from the Silt Sea — **a single encounter, not a resident** (owner's ruling, 13 August 2026). If the party drives it off rather than killing it, it stays a standing danger for any return visit.
- The staircase to the tower is damaged higher up — see [[Dregoth's Tower]].
- The Caller in Darkness reaches everywhere in these ruins.

## Opportunities
- **"The Lion-King Lives!"** — someone wrote that after the city fell, and the campaign already has Taraskir's corpse.
- The ante-chamber stairs are one of the surface entrances to the tunnel network.

## Connections
- Parent: `location-giustenal-ruins`.
- Destination: **Dregoth's Tower** — proposed `location-dregoths-tower`; reached only from room 12.
- Destination: **The under-region tunnels** — `location-under-region-tunnels`, existing record; the ante-chamber stairs descend to them.

## GM-Only Secrets
- Mon-Adderath packed his belongings when he and Dregoth withdrew beneath the city. The palace was abandoned deliberately, not overrun.

## Proposed Developments
All unapproved.
- The graffito is an unclaimed hook: who wrote it, and are they still alive.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Four: The Ruins Above — Dregoth's Palace, areas 1–16
  - Printed page: **49, 51–55**
  - Source type: official
  - Adaptation note: Room contents, values, the lock modifier, the treasure types and the tower staircase are printed. Nothing is invented.
- Title: `mk-repos/mk-sandbox/locations/giustenal-ruins.json`
  - Section: full entry, revision 6
  - Printed page: —
  - Source type: campaign record (read-only)
  - Adaptation note: The parent record. Not edited.

## Unresolved Questions

*(All three answered by the campaign owner, 13 August 2026.)*

- ~~Sixteen rooms in one record or a sub-location per wing~~ — **one record.** The split rule covers places people travel to, not rooms inside one building. The sixteen stay as features of `location-dregoths-palace`.
- ~~Whether the sink worm is a resident threat~~ — **a one-time encounter, unless it is not killed.** It comes once through the north-wall opening in the Banquet Hall, out of the Silt Sea. If it survives the party, it remains on the record as a live threat for later visits; if killed, the record says so. Relevant now that the ruins are reachable through the Kharanok gate.
- ~~Who wrote the graffito~~ — **left open for the players.** "The Lion-King Lives!" stays unattributed; the table decides what it believes.
