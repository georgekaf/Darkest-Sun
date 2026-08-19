---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: Tenpug's Temple (update to existing location-tenpugs-temple, revision 4)

*(Revision of existing location `location-tenpugs-temple`. **This is the "ancient temple" referred to across the Giustenal nominees** — the Campaign Book states plainly that Tenpug's Band makes its headquarters in an ancient temple hall. No second temple record is needed.)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/locations/tenpugs-temple.json` (revision 4, updated 2026-07-22).*

| Field | Current value |
| --- | --- |
| `id` | location-tenpugs-temple |
| `region` / `terrain` | West of Cromlin near the Sea of Silt / ruins |
| `control` | faction-tenpugs-band |
| `danger` | **2** |
| `connections[]` | empty |
| `localClocks` | `clock-temple-discovered` — 6 segments, progress 1, "Enemies identify the temple as Tenpug's permanent headquarters", gm, active |
| `features[]` | Ancient temple from the Time of Magic · Hidden chambers · Lion-headed giant statues representing Taraskir's Lion Guard · Faded frescoes showing ancient Giustenal beside water · Hidden refuge and workshop community of escaped-slave artisans · Funeral pyres after the gith night attack · Starting point of the band's expedition toward the Black Spine |
| `notableActors[]` | actor-tenpug, actor-danya, actor-arcus, actor-sala, actor-roi, actor-lynth, actor-raxxon |
| `relatedLocationIds[]` | location-cromlin, location-black-spine-mountains, location-nibenay |

**Proposed changes, all unapproved:**

1. **`actor-nallan` died here, and the record does not say so.** He is found in this temple with a bone dagger in his heart and an empty sheath on his belt — a **confirmed kill by the Caller in Darkness**, which drives its victims to take their own lives.
2. **`actor-caller-in-darkness` is not listed anywhere on this record.** The band's headquarters sits in a place where the Caller has demonstrably reached someone.
3. **`danger: 2` is questionable** given point 1. Not proposing a number — proposing the question be answered.
4. `relatedLocationIds[]` omits **`location-giustenal-ruins`**, which is the temple's own context.

## Summary
An ancient temple hall from the Time of Magic, held by Tenpug's Band of escaped slaves as a hidden refuge and workshop — and the room where the Caller in Darkness left a body to be found.

## Classification
- Location subtype: ruin, occupied
- Region: west of Cromlin, near the Sea of Silt
- Terrain: ruins
- Parent location: —
- Status: occupied, hidden
- Controller: `faction-tenpugs-band`
- Contested by: gith, who have already attacked once at night

## Player-Safe Arrival Description
A temple hall older than anyone's reckoning. Lion-headed giant statues stand along it — Taraskir's Lion Guard. The frescoes have faded, but the city they show still straddles open water.

## Physical Features
*Retained in full from the existing record.* Proposed addition: the temple is where **Nallan's body** was found, and the frescoes' drowned city is the same Giustenal now half-buried in silt a short way east.

## Population and Occupants
Tenpug's Band — escaped-slave artisans, a working refuge rather than a camp. Named members already on the record: Tenpug, Danya, Arcus, Sala, Roi, Lynth, Raxxon.

## Resources
- Water: not recorded.
- Food: not recorded.
- Trade: workshop output; the band deals through Cromlin.
- Guards: the band itself.

## Important Areas
- The temple hall and its hidden chambers.
- Wherever Nallan was found — the source places him in the ancient temple.

## Important Actors and Factions
Retained, plus proposed: **`actor-nallan`** (deceased, here) and **`actor-caller-in-darkness`** (as a danger, not an inhabitant).

## Dangers
- The existing discovery clock — enemies identifying this as Tenpug's permanent headquarters.
- Gith, who have attacked at night before and left the band raising pyres.
- **The Caller.** It killed here. Any band member who is a psionicist or wild talent, of a qualifying ancestry, is a candidate — and the band lives here permanently.

## Opportunities
- An escaped-slave community with workshops, already disposed against the same enemies the party fights.
- Roi is already a campaign contact — the ad3 line about the Ghodan brothers came from him.

## Connections
- Destination: **Cromlin** — `location-cromlin`. Retained.
- Destination: **Black Spine Mountains** — `location-black-spine-mountains`. Retained; the band's expedition started from here.
- Destination: **Nibenay** — `location-nibenay`. Retained.
- **Propose adding: Ruins of Giustenal** — `location-giustenal-ruins`. The temple's frescoes are of that city and the Caller's reach covers the ground between.

## Local Clocks and Pressures
`clock-temple-discovered` retained unchanged, 1/6.

## GM-Only Secrets
- The band is living inside the hunting ground of something that selects for psionic minds and does not need to enter a building to reach one.
- Nallan's death is presented in the source as a discovery, not an event — the body is found. Whoever finds it learns nothing about what did it.

## Proposed Developments
All unapproved.
- If a band member is a wild talent, the discovery clock is not the band's most urgent problem.

## Sources
- Title: `mk-repos/mk-sandbox/locations/tenpugs-temple.json`
  - Section: full entry, revision 4
  - Printed page: —
  - Source type: campaign record (read-only)
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two — Tenpug's Band
  - Printed page: **10**
  - Source type: official
  - Adaptation note: *"The band makes its headquarters in an ancient temple hall. Faded frescoes show a city straddling the edge of the [water]."* This is the sentence that identifies the temple as the ancient temple.
- Title: City by the Silt Sea — Adventure Book
  - Section: Giustenal ruins — the ancient temple, Nallan's body
  - Printed page: —
  - Source type: official
  - Adaptation note: Nallan found with a bone dagger in his heart and an empty sheath — the Caller's method, not a murder.
- Title: DSE2 Black Spine
  - Section: Clash by Night and Cry Vengeance: Funeral Pyres
  - Printed page: —
  - Source type: official
  - Adaptation note: Retained from the existing record.

## Unresolved Questions
- **Is `danger: 2` still right** for a location with a confirmed Caller kill in it?
- Does the band know how Nallan died, or only that he was found?
- Are any of Tenpug's named members psionicists or wild talents? That single fact decides whether this refuge is safe or bait.
