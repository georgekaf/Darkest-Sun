---
entryType: location
entrySubtype: ruin
authorGM: "Ghost"
visibility: mixed
---

# Location: Ruins of Giustenal — districts (update to existing location-giustenal-ruins, revision 7)

*(**Revision, not a new location.** `location-giustenal-ruins` exists at revision 6 and already carries the silt burial, the sunken northern sections, the Caller in Darkness, the ruined palace and tower, the under-region access and the Kharanok gate pairing. This nominee adds the district breakdown, Dregoth's Arch and the tar-pit approach — all **features of the parent**, since none of them is a separate explorable site.)*

## Summary of the change
The ruined city has eleven mapped districts with distinct contents and hazards, an approach that has its own mishap table, and a landmark at the gates. None of it is currently on the record.

## Features to add

### 2. Dregoth's Arch
- **Two great arches of black obsidian, as tall as the city walls**, greeting anyone who comes through the gates.
- **A huge dragon head on each keystone**, in the same black obsidian.
- Another monument Dregoth dedicated to himself; ominous against the lighter stone used everywhere else in the city.

### The districts
- **4. Merchant District** *(south-east)* — stone buildings, thoroughly pillaged. Sustained searching turns up random **Type A** treasure. **A pack of zhackals lairs in the cellar of a large tavern in the northern part**; the doors are open and the metal locks on the cellar door are worth 3 sp.
- **5. Grand Plaza** — huge stone basins that once held topiaries, now full of ash. A large crack runs through the plaza toward the palace. Skeletons lie where they fell.
- **6. Arena** — built to appease the nobles. **Slave pens under the southern seating hold dozens of mummified bodies.** The Caller in Darkness manifests its worst illusions here.
- **8. Warrens of the Poor** *(south-west)* — baked clay, piled stone and fabric, blackened by soot off the tar pits. **Survivors knew it was the poor quarter, so almost nobody looted it** — Type M treasure after four hours' searching.
- **9. Freemen District** — sturdier construction than the Warrens, and thoroughly looted.
- **10. Gardens** — surround the palace; plant life burned to ash, six inches of silt over a foot of it. **Two templar bodies in the smaller garden, each with a steel long sword and gold earrings.**
- **11. Public Cisterns** — wells on both sides of the palace; only the southern ones remain, now dried mud. **A dormant bog wader hibernates in one.**
- **12. Nobles' District** — richly appointed buildings near the Silt Sea. **Silt is especially deep here and silt creatures are a serious danger.**
- **13. Traders' District** — permanent stores along the caravan road, magically damaged; some **Type D** treasure remains.
- **14. Templar District** — east of the palace, devastated by magic. Silt horrors frequent the shores; **a pack of silt runners lairs in the south-east corner.**
- **15. Slave Pen** — a compound behind 15-foot walls, full of dead slaves. **Four undead gladiators reside among the corpses.**

### The tar pits *(extends the existing "bordered by tar pits")*
- **A smouldering barrier across the southern approach**, with few safe routes. Crossing calls for a check, and a guide's map removes the modifier.
- Mishap table, d20: **1–5 misstep** (fall into tar, 3d8 then 1d8 per round) · **6–9 blinded** by smoke, 1d10 minutes · **10–13 heat exhaustion**, −2 to Wisdom and Intelligence proficiency rolls · **14–16 severe**, as above plus 1d6 hp per check · **17–18 pit snatchers**, 1–3 attack · **19–20** stumble across a dying creature.
- **Two people are known to hold a route:** [[Passk]], and [[Jessix the Wanderer]], who will draw a map only for someone genuinely sympathetic to his past.

## Actors that resolve
- `actor-jessix-wanderer` — existing record. **His black-stained hands are from a pit snatcher**, in the encounter that delayed him from reaching Slinnasia in time.
- `actor-passk` — proposed; filed as an issue.
- The Caller in Darkness — `actor-caller-in-darkness`, existing record, already on the parent.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Four: The Ruins Above — areas 2, 4–15
  - Printed page: **48–51**
  - Source type: official
  - Adaptation note: Arch description and keystones, district contents, treasure types, the zhackal lair and lock value, the bog wader, the silt runners and the undead gladiators are printed.
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Four — the tar pit approach and its encounter checks
  - Printed page: **39–41**
  - Source type: official
  - Adaptation note: Source of the mishap table and of the map removing the modifier.
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two — Jessix the Wanderer
  - Printed page: **13**
  - Source type: official
  - Adaptation note: Jessix's route knowledge, his reluctance, and the pit snatcher that stained his hands.

## Unresolved Questions
*(All three answered by the campaign owner, 13 August 2026.)*

- ~~Whether eleven districts belong as features or as sub-locations~~ — **ruled: split all eleven into their own location records**, with references kept **both ways** — each district names `location-giustenal-ruins` as parent, and the parent carries a pointer to each district. This revision therefore shrinks to Dregoth's Arch, the tar-pit approach and the eleven pointers.
- ~~Whether the arena's illusions should be modelled as a hazard~~ — **ruled: follow the book.** The Arena is where the Caller in Darkness lures victims for the final act, so the Arena's record carries that as a hazard in its own right. `actor-caller-in-darkness` remains a city-wide presence; the Arena is its killing ground, not the limit of its reach.
- ~~Whether Passk's map and Jessix's map are the same route~~ — **ruled: it does not matter.** Either map grants safe passage across the tar pits and removes the check modifier, whether or not they describe the same crossing.
