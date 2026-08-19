---
entryType: location
entrySubtype: tunnel network
authorGM: "Ghost"
visibility: mixed
---

# Location: Giustenal Under-Region Tunnels (update to existing location-under-region-tunnels, revision +1)

*(**Revision, not a new location.** `location-under-region-tunnels` exists and already carries the Blue Age origin, the Green Age modifications, the bound-psyche transport and the connection from surface ruins to the subterranean cities. This nominee adds the **seven lettered tunnels** and the mechanics of the orbs — the part that decides where a party can actually get to.)*

## Summary of the change
The network is currently one paragraph. It is seven distinct passages with different states, different guardians and different destinations, and two of them are gated by intelligent psyches who decide whether anyone passes.

## Features to add

### The tunnels themselves
- **Forty-foot-wide tubes of solid, smooth rock** — not rock to the touch at all. Even the vertical shafts have **no handholds, no ladder rungs, no stairs.**
- **Spherical indentations every 500 feet.** A successful stonemasonry check shows they were **carved in later**, with rougher edges than the original surface.
- The indentations held **obsidian orbs** made during the Green Age, when the Way was all-powerful: **the psyches of psionically talented individuals were placed inside them** and used to power the conveniences of the day. Some survive intact and still work; many are shattered.

### Tunnel A
- Quarter-mile long, **collapsed at the end** where the city sank. **One intact orb**, which levitates travellers and then drops them when it loses power.

### Tunnel B
- Once ran to the **island settlements** of Vakura, Pelcunal and Liuss. **Stretches almost a mile before ending in a jumble of fallen stone.**
- A few orbs still operate: light from the walls, a burst of fresh air, and a fast trip to the end — **for those who respond favourably to the intelligent psyche trapped here.**
- **[[Kataal the Mover]]**, once a halfling of the Green Age, still controls this transport. He knows the tunnel is destroyed short of the islands. He offers the trip regardless, and **floods those who refuse with visions of Athas's history** — which is what happened to [[Jessareen]].

### Tunnel C
- Once connected the Groaning City to the other subterranean cities. Vertical shafts run up to the surface and down toward Kragmorta and New Giustenal.
- **Every orb receptacle is empty — Dregoth took them.**

### Tunnel D
- A vertical drop from a cave connected to **Dregoth's Tower**, descending roughly **a mile** before levelling into the Groaning City cavern.
- **Orbs smashed by demihumans**; **spikes pounded into the stone** for climbing.

### Tunnel E
- Runs to the **Kragmorta** cavern. No spherical receptacles at all.
- **A lava river, 25 feet wide and 6 feet deep, crosses the tunnel about a quarter-mile before the cavern.**

### Tunnel F
- Descends to the lowest level, **New Giustenal**. Cruder receptacles, holding **orbs stolen from Tunnel C**.
- **Primik the Mover guards it and transports only those carrying Dregoth's holy symbol**, alerting the guards to anyone else.

### Tunnel G
- Also leads to New Giustenal, lit by **continual light stones**. **Four 4th-level dray templars** are stationed here and **their duty is lax.**

## Actors that resolve
- `actor-kataal-the-mover` — existing record, status inactive. Tunnel B.
- `actor-jessareen` — existing record; the casualty of refusing him.
- **Primik the Mover has no record.** A second bound psyche, with a working access rule, guarding the way into Dregoth's city — worth its own nominee.

## Connections this establishes
- `location-giustenal-ruins` → the network, via the palace ante-chamber stairs.
- `location-sunken-city`, `location-groaning-city`, `location-kragmorta`, `location-new-giustenal` — all four already exist as records and all four are reached through these tunnels.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Five: The Ruins Below — the tunnel network, Tunnels A–G
  - Printed page: **58–62**
  - Source type: official
  - Adaptation note: Tunnel width and surface, the 500-foot indentations and their later carving, the orbs' Green Age origin and psyche contents, and every per-tunnel detail above are printed. Tunnel G's lax guards and Tunnel F's holy-symbol rule included.
- Title: `mk-repos/mk-sandbox/locations/under-region-tunnels.json`
  - Section: full entry
  - Printed page: —
  - Source type: campaign record (read-only)
  - Adaptation note: The record being revised. Not edited locally.

## Unresolved Questions

*(All three answered by the campaign owner, 13 August 2026.)*

- ~~Whether this network and the Kharanok gate network are the same system~~ — **separate, for now.** Two unrelated technologies converging on one city: Crystal Dust and spoken Gith or Draxian on the Kharanok side, Green Age obsidian orbs and bound psyches on this one. Neither record asserts a link, and the resemblance stays available as a later reveal.
- ~~Whether Primik the Mover should be filed as an actor~~ — **yes.** `actor-primik-the-mover`, filed the same way as Kataal the Mover: the bound psyche guarding Tunnel F, with its access rule (Dregoth's holy symbol) and its alarm behaviour. Nominee owed.
- ~~Whether each tunnel wants to be a sub-location or stay a feature~~ — **sub-locations.** Tunnels A–G each get their own record, **back-linked to this parent page**, with the parent carrying a pointer to each. They are separately reachable and several hold their own inhabitants — Kataal in B, Primik in F — so they are places you travel to, not rooms you pass through.
