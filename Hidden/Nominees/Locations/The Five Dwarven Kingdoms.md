---
entryType: location
entrySubtype: regional node
authorGM: "Ghost"
visibility: mixed
---

# Location: The Five Dwarven Kingdoms — Karand-Vath, Durak-Kal, Karum-Draz, Kurad-Mor and Dras-Karan

*(**New index record.** Proposed id `location-five-dwarven-kingdoms`. No record exists — verified 16 August 2026 against `locations/` on the default branch: 97 records, no match on filename, `id`, `name`, `aliases[]` or `titles[]`. The four kingdoms other than Karand-Vath appear in exactly two files, `events/day-0103.json` and `locations/klarbu.json`, and nowhere else.)*

## Summary
Five dwarven kingdoms, of which Karand-Vath beneath Klarbu is the only one located. The other four are names in a single account, given thousands of years after the fact by the being who outlived them.

## Classification
- **Origin: campaign-original**, introduced in play by the Dune Runners (`party-dune-runners`) — episode 15, in-world **day 103**. Kemalok, Borys and Rajaat are published Dark Sun material; the five kingdoms and their names are not.
- `canonStatus`: **campaign-original**
- Historical status: **disputed** — single-source testimony, explicitly unverified
- Region: Black Spine Region for Karand-Vath; **unknown for the other four**
- Members: **Karand-Vath**, the only located member, beneath `location-klarbu` — filed separately as issue #493. Durak-Kal (#499) · Karum-Draz (#500) · Kurad-Mor (#501) · Dras-Karan (#502) — location unknown, state unknown.

## The account

Where it currently lives: `locations/klarbu.json` revision 20, `subterraneanComplexes[0].revealedHistory` —

> **summary:** *"The undead guardian identified Karand-Vath as one of five dwarven kingdoms scattered after Borys, Champion of Rajaat, massacred Kemalok thousands of years ago."*
> **kingdoms:** `["Karand-Vath", "Durak-Kal", "Karum-Draz", "Kurad-Mor", "Dras-Karan"]`
> **sourceStatus:** *"Guardian testimony; not independently verified in play"*

**Reliability.** One witness — the undead guardian of Karand-Vath, who dissolved into sand at the end of episode 15 and cannot be asked again. The party could not speak to him directly, so every name passed through Pogona-Barbata's broken Dwarven.

## Previously established campaign facts this touches
- **Kemalok** is already in the sandbox as the source of `artifacts/kemalok-iron-golem` — *"an iron golem brought from Kemalok and hidden by the player characters to keep it from Kalak and other powers."*
- **Karand-Vath** is inhabited, partly mapped, and currently shelters Klarbu's survivors.

## Connections
- **Parent of:** Durak-Kal (#499), Karum-Draz (#500), Kurad-Mor (#501), Dras-Karan (#502)
- **Also a member:** Karand-Vath (#493)
- **Where the testimony lives:** `location-klarbu` → `subterraneanComplexes[0].revealedHistory`

## Sources
- Title: `events/day-0103.json`
  - Section: the guardian's testimony; the five kingdoms; the deferral of their locations and present states · Source type: campaign record (read-only)
- Title: `locations/klarbu.json`
  - Section: `subterraneanComplexes[0].revealedHistory`, revision 20 · Source type: campaign record (read-only)
- Title: `artifacts/kemalok-iron-golem.json`
  - Section: provenance of the golem, for the Kemalok cross-reference · Source type: campaign record (read-only)
- Title: Darkest Sun, s3 ep.15 "Fear of the Dark!"
  - Section: the necropolis behind the gate, the guardian, the five kingdoms, the inherited oath
  - Source type: campaign-original (actual play, in-world day **103**)
