---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: Cromlin (update to existing location-cromlin, revision 12)

*(**Revision, not a new location.** `location-cromlin` is at **revision 11**, which landed the #402 sub-location work on 13 August 2026: the ten village features are now written out in full and **the Dirty Lizard has been trimmed off the parent**, now that `location-dirty-lizard` and `location-passks-shack` exist as their own records. None of that is reopened here. This revision adds the two things revision 11 still does not have: **where Cromlin sits relative to Nibenay**, and **what it is currently being used for**.)*

## Current record in mk-sandbox

*Read-only snapshot of `locations/cromlin.json` (revision 11, updated 2026-08-13).*

| Field | Current value |
|---|---|
| `region` / `terrain` | **Silt Coast west of Giustenal** / settlement |
| `control` / `population` | faction-house-shom / **1200** |
| `danger` | null |
| `resources` | trade major, silt skimmer access |
| `connections[]` | klarbu, quel-nash, break-shore — all with real route ids |
| `mapHex` | Black Spine regional map, column 8, row 1 |
| `features[]` | ten entries: the twenty-mile position west of Giustenal · the timber piers and berth fees · the House Shom pier and the *Firewind* · the locked warehouse and its sentry patrols · Crost's lodge and walkway · the barracks, thirty soldiers and the troubleshooter post · the marketplace and Crost's ten-percent share · House M'ke's yard and slave-crafters · the homes, the exile elves and the absence of street patrols · the silt scarves |
| `activeSituations[]` | `situation-cromlin-black-wake-war` — Black Wake against the Sky Singers |
| `factionPresence[]` | house-shom, sky-singers, tenpugs-band, house-mke, black-wake |
| `tags[]` | trading-village, sea-of-silt, house-shom, silt-skimmers, black-wake, pirate-war, contested-routes |

## Proposed changes

1. **Position: Cromlin is north of Nibenay.** The record fixes it against Giustenal only — "about 20 miles west" — which places it relative to one neighbour and leaves it floating against the city-state the campaign actually travels from. **`mapHex` column 8, row 1 already sits at the north edge of the regional map and agrees; no hex change is proposed.**
2. **Cromlin is being used as a slave-holding point for deliveries to Dregoth.** The population taken from **Zharvek** on the night of day 114 was brought here and held, and **most have already been delivered** onward to Giustenal. **Two prisoners remain** — **Talek Vos** and **Damak of Zharvek**. Proposed as an `activeSituations[]` entry alongside the Black Wake war, not as a feature: it is a live state with people in it, not a permanent characteristic of the village.
3. **`faction-silt-stalkers` belongs in `factionPresence[]`** — or does not, and that is precisely the question below. They are moving consignments through a House Shom village of 1,200 people.
4. **The Dirty Lizard is already handled — nothing owed.** `location-dirty-lizard` and `location-passks-shack` both exist at revision 1, and revision 11 has already trimmed the tavern off the parent's feature list. What is still worth adding is a **`subLocations[]` pointer** on this record: the 13 August ruling asks for references **both ways**, and the parent currently has none.

## Summary of the change
Where Cromlin is, and what is currently happening inside it.

## Position

- **About 20 miles west of Giustenal** *(retained — printed, Chapter Two).*
- **North of Nibenay** *(new — campaign owner, 13 August 2026).*
- Regional map hex column 8, row 1 *(retained, and consistent with both bearings).*

## The holding operation

*(GM input, 13 August 2026. Entered through MK-Sandbox #189.)*

- Silt Stalker raiders under **Luubarra Fire Dagger**, **operating for `actor-zarron`**, emptied **Zharvek** on the **night of day 114** and brought the captives to **Cromlin**. *(Ruled 13 August 2026: "Zharvek was destroyed by Zarron's pirates" and "the raid was Luubarra's Silt Stalkers" describe one event at two levels of one chain.)*
- **That makes the holding site far less anomalous.** Cromlin already carries `situation-cromlin-black-wake-war` and `faction-black-wake` in `factionPresence[]`. Zarron's people are not strangers smuggling prisoners through a House Shom town — they are already fighting an open war over its routes and anchorages.
- **Most of the consignment has already been delivered** to **Dregoth**. Cromlin is twenty miles from the buried city — the last stop before it.
- **Two prisoners are still held here:** **Talek Vos**, a House Shom envoy, and **Damak of Zharvek**, the dwarf who oversaw the settlement.
- No release, delivery or death is recorded for either.

## Player-Safe Arrival Description
*(Unchanged.)* A working silt port of about twelve hundred people under House Shom, piers twenty feet tall against the dust, an open-air market behind a stacked stone fence, and scarves over every face against the choking silt.

## Dangers
The record carries `danger: null`. **This revision proposes no number** — but the reason it is worth revisiting is now on the table: a village with no street patrols, an open pirate war offshore, and a slave consignment moving through it is not a neutral trade stop.

## Actors and factions that resolve
- `actor-hurdll-crost`, `actor-garreth-brodden`, `actor-captain-gaff`, `actor-jaksot-han`, `actor-passk` — existing records, retained in `notableActors[]`.
- `actor-talek-vos` — **held here.** Revision filed alongside this one.
- `actor-damak-of-zharvek` — **held here.** New actor nominee filed alongside this one.
- `actor-luubarra-fire-dagger` — running the delivery. Revision filed alongside this one.
- `faction-silt-stalkers` — existing record; **proposed** for `factionPresence[]`, subject to the question below.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two: Giustenal Environs — Cromlin; Cromlin Locations 1–10
  - Printed page: **15–20**
  - Source type: official
  - Adaptation note: The twenty-mile distance west of Giustenal and the village's House Shom control are printed. **Nothing about the holding operation is printed** — Cromlin's printed role is trade and silt piracy.
- Title: `locations/cromlin.json`
  - Section: full entry, revision 10 · Source type: campaign record (read-only)
  - Adaptation note: The record being revised. Not edited locally.
- Title: `locations/zharvek.json`
  - Section: `features[]` and `unresolvedDetails[]`, revision 8 · Source type: campaign record (read-only)
  - Adaptation note: The other end of the same event.
- Title: campaign owner ruling, 2026-08-13
  - Section: Cromlin north of Nibenay; the Zharvek captives held here for delivery to Dregoth
  - Source type: GM input
  - Adaptation note: Entered through MK-Sandbox #189. No confirmed event record is claimed here.
