---
entryType: location
entrySubtype: settlement
authorGM: ""
visibility: mixed
---

# Location: Obsidian Mines (Below Kharanok, Level 1)

## Summary
The mine below Kharanok, officially named for its obsidian vein but also the village's illegal source of Crystal Dust — its upper level, from the North Entrance down to the South Access Shaft.

## Classification
- Location subtype: dungeon / mine level
- Region: Black Spine Region
- Terrain: underground mine, cave tunnels, underground river
- Parent location: location-kharanok
- Coordinates or map reference: entrance sits within Kharanok proper; see [[Below Kharanok]] for the full 31-area dungeon graph and distance table
- Status: partially explored, mine door opened, active gith access shaft, deeper ancient tunnels beyond it
- Controller: Kharanok (contested — gith still active in the deeper reaches)
- Contested by: gith raiders/warband using the South Access Shaft route

## Player-Safe Arrival Description
The North Entrance is a narrow cave mouth, gith heads mounted on spears out front as a warning. Inside, the passage follows an underground stream south, past a wooden bridge crossing fast-moving water, toward the worked stone of the main excavation.

## Physical Features
Twelve keyed areas: North Entrance, River Walk, Bridge Crossing, Main Excavation, West Galleries, Deep Lake, Lower Pools, Foreman's Office, Barracks, Storehouse, Workshop, South Access Shaft. An underground stream runs from the entrance down through the Deep Lake, where Crystal Dust actually forms — shards dragged down by water and deposited in the lake bed, recoverable once it dries out at noon; clearer, higher-quality crystals are found past the lake, deeper in, where Bulette and other monsters roam. The South Access Shaft is a ~1.92km descent — a ~180m wooden rope elevator (currently broken, cut ropes; needs tar and someone who knows how to work it, per Roi's assessment, or 50 scraps) followed by a ~1,735m rock-carved staircase, roughly 10,200 steps — continuing down to [[02. The Rat-Folk Tunnels]].

## Population and Occupants
No permanent population. Formerly a gith watch position; seven gith were killed and one captured during the ad3 expedition. Dorak (Kharanok's ex-mine foreman, a former gith slave) knows the upper workings and currently guides the party through them.

## Resources
- Water: The underground stream and Deep Lake.
- Food: Deeper mushroom fields identified as a possible food source (unconfirmed in play as harvested).
- Trade: Clean Crystal Dust extracted from the Deep Lake; mining/trading Crystal Dust is illegal, so the site is publicly known only for its obsidian vein.
- Verdance: None notable.
- Guards: None currently stationed; Kharanok has no spare hands to garrison the mine.
- Other: Metal mining tools and one piece of obsidian recovered from the mine (Day 110).

## Important Areas
- **Deep Lake (#6)** — where Crystal Dust actually forms and is harvested.
- **Foreman's Office (#8)** — supervisor's room, doubles as the "quartermaster chambers"; hidden crate-door from the Storehouse (#10); stairs down to Level 2 sit at this junction.
- **Storehouse (#10)** — two rooms; one holds the hidden crate-door to the Foreman's Office, the other (by the elevator shaft) holds a hidden passage to a one-way teleportation room. Dorak found an old parchment on a Gith raider describing this route — kept secret, unused, and unconfirmed to actually work.
- **Barracks (#9)** — reached via two illusionary walls; a second, separate hidden route to the same one-way teleportation room. Portal costs 10 Crystal Dust to activate, 1 per use after (see [[Portal Activation]]).
- **South Access Shaft (#12)** — the route down to [[02. The Rat-Folk Tunnels]]; broken lift needs repair.

## Important Actors and Factions
- [[Dorak]] — ex-mine foreman, guide, former gith slave; knows the upper workings.
- Roi — one-armed dwarf craftsman, assessed the broken lift's repair needs.
- Gith raiders/warband — hold the deeper reaches and the South Access Shaft route.

## Dangers
Bulette and other monsters past the Deep Lake, toward the higher-quality Crystal Dust deposits. Active gith presence in the deeper tunnels and along the South Access Shaft. An unresolved "dream presence" and the cause of a reported madness among villagers who lingered near the mine at night (screaming, jumping into the canyon, self-harm) — not yet explained in actual play.

## Opportunities
Crystal Dust extraction (illegal but valuable). The hidden teleportation room, once its portal is activated, offers a one-way shortcut. Mushroom fields deeper in as an unexploited food source. The broken lift, once repaired, restores fast access to Level 2.

## Connections
- Destination: Kharanok (surface)
  - Existing location ID: location-kharanok
  - Existing route ID: —
  - Travel notes: North Entrance opens directly within Kharanok.
- Destination: The Rat-Folk Tunnels (Below Kharanok, Level 2)
  - Existing location ID: — (not yet nominated)
  - Existing route ID: —
  - Travel notes: via the South Access Shaft (#12), currently slowed by the broken lift.

## Local Clocks and Pressures
Broken elevator at the South Access Shaft — blocks fast travel to Level 2 until repaired (tar + a skilled operator, or 50 scraps).

## GM-Only Secrets
The unknown presence behind the shared dream reported by the Altar of Dust group (claiming imprisonment nearby for thousands of years) and the true cause of the villagers' mine-induced madness are both unresolved as of ad5 — flagged as open GM material, not yet explained at the table.

## Proposed Developments
- New location entry — no existing `location-obsidian-mines` in MK-Sandbox; this level's detail currently lives only inside `location-kharanok`'s `resourceStatus.mining` and `features` fields. Proposing a dedicated location entry to hold the room-level detail instead of keeping it folded into Kharanok's own record.
- Level 2 ([[02. The Rat-Folk Tunnels]]) and the rest of the 31-area dungeon graph are separate, not-yet-nominated locations — see [[Below Kharanok]].

## Sources
- Title: `Hidden/Kharanok- The Altar of Dust/Below Kharanok/01. Obsidian Mines AKA The Cannibal Caves/01. Obsidian Mines AKA The Cannibal Caves.md`
  - Section: full page (room list, connections, hidden passages)
  - Printed page: —
  - Source type: campaign-original
  - Adaptation note: —
- Title: existing `location-kharanok.json` (revision 10)
  - Section: `resourceStatus.mining`, `features` (mine-related entries)
  - Printed page: —
  - Source type: campaign-original, prior MK-Sandbox submission
  - Adaptation note: —
- Title: `Hidden/Session prep/0003 - Session Prep 16-7-2026.md`
  - Section: lift repair note
  - Printed page: —
  - Source type: campaign-original design doc
  - Adaptation note: —
- Title: `Rules/Portal Activation.md`
  - Section: full page
  - Printed page: —
  - Source type: campaign-original confirmed rule
  - Adaptation note: —
- Title: Altar of Dust Session ad3 "Minecraft in Kharanok"
  - Section: mine expedition, bulettes, gith prisoner, deep shaft, lift
  - Printed page: —
  - Source type: campaign-original (actual play, 16 July 2026)
  - Adaptation note: GM Kostasgk's table.
- Title: Altar of Dust Session ad4 "It's Raining Bats and Bugs"
  - Section: opening scene — the party enters the mine and takes spare rope from the immobilized broken-elevator platform at the South Access Shaft (#12), leaving the rest intact so the platform stays repairable
  - Printed page: —
  - Source type: campaign-original (actual play, 25 July 2026)
  - Adaptation note: GM Kostasgk's table. The Syggra-recovery cave visited later in this session is a separate, unnamed nearby cave outside this level's keyed area — not part of the Obsidian Mines proper.
- Title: Altar of Dust Session ad5 "The Bug Whisperers... Finally!"
  - Section: mid-session mine work with Dorak — two gith guards chased down and killed/interrogated, three pieces of obsidian extracted, a glimpse of the Crystal Dust pool, and a Bulette (Land Shark) ambush while leaving
  - Printed page: —
  - Source type: campaign-original (actual play, 26 July 2026)
  - Adaptation note: GM Kostasgk's table.

## Unresolved Questions
- Whether this should stay a standalone location entry or fold back into `location-kharanok` as a sub-area — depends on how deep MK-Sandbox wants dungeon-level detail to go.
- The dream-presence/madness mystery has no resolution yet to record.
