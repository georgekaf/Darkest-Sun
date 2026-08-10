---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: Ruins of Giustenal (update to existing location-giustenal-ruins, revision 4)

*(Revision of existing location `location-giustenal-ruins`. Everything below is a change **against these values**.)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/locations/giustenal-ruins.json` (revision 4, updated 2026-07-22).*

| Field | Current value |
| --- | --- |
| `id` | location-giustenal-ruins |
| `region` / `terrain` | Sea of Silt coast / ruins |
| `control` / `population` | null / null |
| `danger` | 5 |
| `resources` | verdance 0 |
| `connections[]` | **empty** |
| `features[]` | Ruined city partly buried by silt and bordered by tar pits · Northern sections sank into the ancient sea · Haunted by the Caller in Darkness · Contains Dregoth's ruined palace and tower · Accesses ancient under-regions |
| `tags[]` | ruined-city, sea-of-silt, caller-in-darkness, dregoth |
| `notableActors[]` | actor-caller-in-darkness |
| `artifactIds[]` | artifact-dregoths-telescope |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Approaching the Ruins; The Ruins Above (pp. 28–57) |

**Proposed changes, all unapproved:**

1. **`connections[]` is empty, and that is now wrong.** A working teleport gate links the ruins to Kharanok, used in both directions on **day 117**. This is the single most important gap in the record.
2. **`notableActors[]` lists only the Caller.** Jessix the Wanderer and the Loyal work these ruins permanently; Tenpug's Band is nearby.
3. **`features[]` says "Haunted by the Caller in Darkness"** without the mechanism that makes the place playable — the five-mile search net and the victim-selection rule.
4. **`danger: 5` is right but undifferentiated.** The danger is selective: it does not apply equally to every party composition.

## Summary
A ruined city on the Sea of Silt coast, half-buried in silt and ringed by boiling tar, with dragon statues before it and Dregoth's ruined palace inside it — hunted over by a psionic storm made of its own murdered dead, and, as of day 117, reachable from Kharanok in a single step.

## Classification
- Location subtype: ruined city
- Region: Sea of Silt coast
- Terrain: ruins
- Parent location: —
- Coordinates or map reference: about 20 miles east of Cromlin
- Status: ruined, inhabited
- Controller: none above ground. **Below it, `faction-new-giustenal` under Dregoth.**
- Contested by: nothing organised — the Caller is not a faction

## Player-Safe Arrival Description
From a rise: an enormous abandoned city half-sunk in mud, dragon statues standing before it, lakes of tar boiling further out. The light is blinding and the heat is not the heat of the deep desert. *(Ranni's account, day 117.)*

## Party Contact To Date

**[[Ranni]] is the only player character who has ever been here.** Day 117, alone, for a few minutes, hidden and too frightened to memorise the ground — she could not fix the gate structure's position relative to the city. No other PC has set foot in the ruins.

Everything the party believes about this place therefore rests on **one frightened witness who was there briefly and by accident**, plus Zephyr's reading of the scrolls. That includes the belief that people live there, which comes from a single shout she heard while leaving.

## Physical Features
*Existing, retained:* partly buried by silt and bordered by tar pits · northern sections sank into the ancient sea · Dregoth's ruined palace and tower · access to the ancient under-regions.

**Proposed additions:**
- **Dragon statues** flanking the approach — the first thing a newcomer sees, and confirmed in play.
- **The ancient temple hall** occupied by Tenpug's Band — see `location-tenpugs-temple`, which is that temple.
- **A functioning teleport plate** somewhere in a structure above the ruins, on a rise overlooking the city. **Exact placement not established** — Ranni could not memorise the spot.

## Population and Occupants
- No settled population above ground.
- **Jessix the Wanderer and the five Loyal** patrol the environs and escort travellers out.
- Sky Singer guides from the Twilightcatchers clan will take money to lead people in, and abandon them at the first sign of the Caller.
- Predators live here **unmolested**, in numbers the terrain would not otherwise explain.
- Fifteen thousand dray beneath it, in New Giustenal.

## Resources
- Water: none.
- Food: none.
- Trade: none. What comes out is loot.
- Verdance: 0 — retained.
- Guards: none.
- Other: **Crystal Dust is the entry cost, not a resource found here** — ten handfuls to wake the gate, five per trip to hold it open.

## Important Areas
- Dregoth's ruined palace and tower.
- The ancient temple — Tenpug's Band headquarters, and where Nallan was found dead.
- The under-region access.
- The gate structure above the ruins *(campaign-original, day 117)*.

## Important Actors and Factions
- `actor-caller-in-darkness` — retained.
- **Propose adding:** `actor-jessix-wanderer`; `faction-the-loyal`; the proposed `actor-varesh`, `actor-kethen`, `actor-nyrra`, `actor-saelis`, `actor-tharek`.
- `faction-tenpugs-band` — via the temple.
- `faction-sky-singers` — guides in, and out again fast.
- `actor-dregoth`, below.

## Dangers
- **The Caller in Darkness, and it is not an encounter.** It sweeps a **five-mile** psionic net around the ruins, permanently.
- **It selects.** Only full psionicists and wild talents, and only minds of the ancestries that lived here when Dregoth died — humans, elves, half-elves, dwarves, halflings. It ignores thri-kreen, muls, half-giants, gith and the dray. **A party's roster decides how dangerous this place is for them.**
- **Only those who die inside the walls are taken.** It herds rather than kills at range.
- Boiling tar, blackwashes, and predators that are here precisely because nothing hunts them.

## Opportunities
- Loot from the first expedition's depth — Dregoth's templar chambers were reached once and survived.
- The Loyal as potential allies for anyone the band decides is worth protecting.
- The gate: a one-step supply line for anything the party wants to carry out.

## Connections
- Destination: **Kharanok**
  - Existing location ID: `location-kharanok`
  - Route ID: **`route-kharanok-giustenal-gate`** — proposed, must exist before this connection can be filed. The schema requires a real `routeId` per connection.
  - Travel notes: **teleport plate, hard-paired and two-way.** Both ends are wholly intact, so the route activates from either side. **10 Crystal Dust** crushed, mixed with water and used to fill the inscriptions activates both members; **5 + 5** across the two ends does the same. One round standing on it teleports you and deactivates both; a further **5** keeps them active. Full mechanics in [[Portal Activation]] (GM ruling, 10 August 2026). Established day 117 from the scroll library under the Kharanok mines, read by Zephyr.
- Destination: **New Giustenal**
  - Existing location ID: `location-new-giustenal`
  - Travel notes: through the under-regions. Directly below.
- Destination: **Cromlin**
  - Existing location ID: `location-cromlin`
  - Travel notes: about 20 miles west, per the Cromlin record.

## Local Clocks and Pressures
**Propose one:** the Loyal now know something appeared inside the ruins out of nothing and vanished the same way, and are watching that spot. That is a clock, not a mood.

## GM-Only Secrets
- **The gate arrival point is inside the Caller's search net.** Anyone stepping through who qualifies as a target is being probed within minutes, before they have oriented.
- **Ranni was already contacted there on day 117** and does not know it. See [[The Caller in Darkness]] and [[Ranni]].
- Dregoth and the Caller are the campaign's great unwritten relationship: his murder created it, and he lives directly beneath it.

## Proposed Developments
All unapproved.
- The party intends to return through the gate. Two separate parties already know they were there — the Caller and the Loyal — and neither knows what the other is.

## Sources
- Title: `mk-repos/mk-sandbox/locations/giustenal-ruins.json`
  - Section: full entry, revision 4
  - Printed page: —
  - Source type: campaign record (read-only)
  - Adaptation note: The record this nominee revises.
- Title: City by the Silt Sea — Campaign Book
  - Section: Approaching the Ruins; The Ruins Above
  - Printed page: 28–57
  - Source type: official
  - Adaptation note: Retained from the existing record.
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Three — The Caller in Darkness; Fear; Running the Caller in Darkness
  - Printed page: 30–31
  - Source type: official
  - Adaptation note: The search net, the selection rule, the herding, and why predators go unmolested.
- Title: City by the Silt Sea — Campaign Book
  - Section: Jessix the Wanderer / the Loyal
  - Printed page: 11–13
  - Source type: official
- Title: Darkest Sun — Altar of Dust, ad7 "City by the Silt Sea"
  - Section: Ranni's transit; the gate mechanics; the shout of "Jessix, someone is here!"
  - Printed page: —
  - Source type: campaign-original (actual play, 7 August 2026, in-world day 117)
  - Adaptation note: The gate connection, the arrival description, and the first confirmed contact between this campaign and the ruins.

## Unresolved Questions
- Where exactly the gate structure stands relative to the ruins — Ranni could not fix the spot.
- Whether the gate connection belongs in `connections[]` as a route or needs a new link type; there is no road between Kharanok and Giustenal.
- Whether `danger: 5` should be qualified by party composition, given the Caller's selection rule.
- Whether the Loyal's watch on the arrival point becomes a clock.
