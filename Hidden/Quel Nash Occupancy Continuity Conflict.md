---
entryType: history
entrySubtype: continuity-record
authorGM: "Ghost"
visibility: gm
---

# Historical Record: Quel Nash — Cross-Campaign Continuity Conflict

## Subject and Period

- Subject: Quel Nash — occupied by a Belgoi war band in the Dune Runners' account, empty and available as shelter in House Markon's, on days that overlap
- Exact day or approximate period: House Markon is at Quel Nash from dusk of day 106 through the night of day 107; the Dune Runners reach it at noon of the day recorded as 106 in s3 ep.24
- Historical status: disputed

*Raised 17 August 2026 while writing the s3 ep.24 summary. Cross-flagged in the ep.24 summary's Σημειώσεις and in the pending worldbuilding issues list.*

## Account

Two campaigns arrive at the same abandoned settlement inside the same two-day window and find it in incompatible states.

| | **House Markon** (`events/day-0106.json`, `day-0107.json`) | **Dune Runners** (s3 ep.24) |
|---|---|---|
| Day | 106 dusk through 107 night | 106, noon to late afternoon |
| Who holds it | Nobody. The company shelters inside the abandoned village | More than 30 Belgoi and 5 Braxat, using it as a forward base; sentries on the walls |
| Threats present | Two b'rohg outside, killed on approach; a gaj-like psionic horror and two more predators on the night of 107 | A patrol of 3 Braxat and 7 Belgoi three hours out; 3 Braxat and 6–7 Belgoi come out of the gates and give chase |
| Outcome | The party rests there two nights and a relief party joins them | The party never enters. It hides in the rift, climbs out at a narrow point outside the walls, and is chased toward the mountains |
| Record state | `locations/quel-nash.json` rev. 7: population 0, *"no permanent living population as of Day 117, Dawn"*, status *abandoned and hazardous*. No Belgoi anywhere in the record | Not yet filed |

Thirty-odd Belgoi holding the walls and a House Markon company sleeping inside the same buildings cannot both be true on days 106–107.

## Affected Elements

- Location: `location-quel-nash` (population, status, features, notableActorIds)
- Factions: the Belgoi, and the Braxat they drive; the baazrag tribe already recorded in the tunnels beneath
- Actors: Nazur, Sarek and the House Markon company for days 106–107; the whole Dune Runners party for ep.24
- Timelines: House Markon days 106–107 and Dune Runners days 105–106 as printed in the summaries
- Records already carrying the flag: the ep.24 summary, the pending worldbuilding issues list

## The Second Half of the Problem — Day Numbering

The two campaigns may not be counting the same days.

| Event | Summary date line | mk-sandbox event date |
|---|---|---|
| Spider Witch killed (s3 ep.18) | 105th day | `event-day-0106-dawn-004` — **day 106** |
| Karand-Vath explored, red altar found, ankhegs (s3 ep.21) | 105th day | `event-day-0107-dawn-004` — **day 107** |
| Karad II rises and the party flees (s3 ep.24) | 106th day (user-supplied, 17 August 2026) | not yet filed |

Both Dune Runners summaries print **105th day** for events the sandbox files on **106** and **107**. If the sandbox numbering is the correct one, ep.24 is **day 108**, not 106 — and the whole conflict dissolves, because House Markon would have left Quel Nash on the morning of day 108 and the Belgoi would have walked into an emptied village behind them.

This is the cheapest explanation and it needs no retcon of anything that happened at either table. It does require re-dating the ep.18, ep.21 and ep.24 date lines, and it contradicts the day the user supplied for ep.24.

## Conflicting Accounts

- **House Markon.** Direct party observation across two sessions and two nights spent inside the village; recorded in the sandbox as GM-confirmed events with a population figure explicitly carried forward to day 117.
- **Dune Runners (s3 ep.24).** Direct party observation from about 150 feet in the noon glare, plus the GM's own narration — he states outright that the patrol they met earlier may now be using Quel Nash as a temporary base, and then brings Belgoi out of the gates in force. This is authorial narration, not a guess by the players.
- **Reliability note.** Neither account is hearsay. The distance and the heat haze weaken the Dune Runners' *identification* slightly, but not the pursuit that followed.

## Candidate Resolutions

**1 — The Dune Runners' day numbering is behind; ep.24 is day 108.** Re-date ep.18 → 106, ep.21 → 107, ep.24 → 108 to match the sandbox. House Markon leaves, the Belgoi move in.
*Cost:* three date lines change, and the user's answer of 106 for ep.24 is overridden. Nothing narrated at either table is touched. **Recommended.**

**2 — Keep day 106 and let the Belgoi arrive after House Markon leaves.** Requires the occupation to begin later than day 106, which is exactly what the episode denies — they are already installed at noon.
*Cost:* contradicts the episode as played. Not viable as stated.

**3 — Keep day 106 and treat House Markon's stay as the mistaken record.** Move the b'rohg fight and the psionic-horror night off Quel Nash.
*Cost:* very high. The sandbox is the owner's record, read-only from our side, and `locations/quel-nash.json` carries the population statement forward to day 117. Two Markon sessions would have to be re-narrated.

**4 — Both true, different parts of the site.** House Markon shelters in one ruined building on the far side while a Belgoi band holds the walls.
*Cost:* strains both accounts. The Markon company spends a whole night fighting predators inside with fire and burning oil; thirty Belgoi would not sleep through it.

**Working position: none applied.** No record changed, no date line moved, both accounts left as they stand. The decision is the user's.

## Unresolved Questions

- Which numbering is authoritative for the Dune Runners — the summaries' or the sandbox's? Every Dune Runners date line downstream depends on the answer.
- How long have the Belgoi held Quel Nash, and are they the same band the party met on the road three hours earlier?
- What happened to the fourteen Klarbies left behind in the chase — killed, or taken as slaves into Quel Nash? The Belgoi trade in slaves, so the second is live plot.
- The twenty Klarbies still hidden in the shaded spot near Quel Nash are a return hook regardless of how the dating resolves.

## Sources

- Title: Darkest Sun, s3 ep.24 "Welcome to Klarbie Town"
  - Section: the march from Klarbu, the Quel Nash approach, and the chase
  - Source type: campaign-original (actual play, 13 August 2026)
  - Adaptation note: Dune Runners account.
- Title: mk-sandbox `events/day-0106.json`, `events/day-0107.json`
  - Section: `event-day-0106-dusk-003`, `event-day-0107-day-002`, `event-day-0107-night-003`
  - Source type: gm-confirmed-event
  - Adaptation note: House Markon account; read-only.
- Title: mk-sandbox `locations/quel-nash.json` revision 7
  - Section: population, status, features
  - Source type: gm-confirmed-event
  - Adaptation note: Records the settlement as abandoned with no permanent living population as of day 117.
