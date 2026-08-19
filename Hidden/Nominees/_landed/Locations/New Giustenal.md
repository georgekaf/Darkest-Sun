---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: New Giustenal (update to existing location-new-giustenal, revision +1)

*(**Revision, not a new location.** `location-new-giustenal` exists and already carries the dray population, the dragon-bone construction, the Blackjaw and Little Blackjaw, self-sufficiency and the enchanted stalactites. This nominee adds the city's numbered areas that have vault pages but no representation on the record — filed as **features of the parent**. The distinct sites among them — Dread Palace, Temple of the Dragon, College of Blackspire, Sharg Island, Upside-Down Forest, Akrag's Pools — are filed separately as their own location nominees.)*

## Summary of the change
Six of the campaign book's numbered New Giustenal areas are infrastructure rather than destinations. They belong on the parent record, and one of them — the Blackjaw's monster — changes how the city currently functions.

## Features to add

### 1. Central Gates
- **Two towers staggered behind two massive gates**, the only entryway into the city.
- Gates built from **stone and dragon bones**.
- **Each tower is manned by four 4th-level templars** — eight in total.
- **Five bone golems stand at attention in front of the inner gates**, commanded by the templars. *(Bone golem: AC 0, MV 12, HD 14, hp 70 each, THAC0 7, damage 3d8, half damage from edged and piercing weapons.)*

### 3. The Blackjaw River *(extends the existing feature)*
- The water **steams constantly as it passes over a magma flow beneath its bed**. Not hot enough to harm; the hot-blooded dray find it relaxing.
- **A great bridge of dragon bones spans it**, with docks on both banks housing the barges.
- **Two huge caves channel the water.** Fishermen will enter them but never so far as to lose sight of the openings.
- **The dray never developed sailing or rowing vessels** — barges are dragged up and down the river with large nets in tow, taking blackjaw fish three or four at a time. Slow, and profitable: **blackjaw and crabs are the only sea-meats available.**
- **A sharg entered the river several months ago** and is depleting it. See the separate nominee for [[Sharg Island]].

### 5. Fishing Shacks
- Large buildings on both banks, used to sort, prepare and store the catch.
- **The dray here are openly making their own plans to deal with the sharg** should the templars keep ignoring it.

### 6. Fanner Fields
- A scrubby field in the **southern section** where **fanners** are raised for meat: fat beasts the size of cattle, single horn on a bull-like face, named for the collar of skin that fans out when they feel threatened — a display evolved against predators **on whatever plane Dregoth took them from**.

### 7. Fungi Fields
- A variety of growths cultivated as a supplement to the dray diet.

### 8. Common Section
- Simple, comfortable homes for the common people, **many built around the great central pillar — a column of stone running from the cavern floor to the ceiling high overhead.**
- These dray work the fields or do other manual labour, **as New Giustenal has no slaves.**

## Continuity worth flagging
**"New Giustenal has no slaves"** is printed, and it sits oddly beside a sorcerer-king's city preparing an army. If the sandbox ever models dray labour, that line is the constraint.

## Actors that resolve
- `actor-dregoth`, `actor-mon-adderath`, `actor-high-priest-absalom` — existing records.
- `actor-freiha`, `actor-gatlakk`, `actor-casskka`, `actor-lodgden` — proposed; all four filed as issues, all four live in this city.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Five: The Ruins Below — New Giustenal, areas 1, 3, 5, 6, 7, 8
  - Printed page: **81–84**
  - Source type: official
  - Adaptation note: Gate construction, templar and golem counts, golem statistics, the magma flow, the dragon-bone bridge, the two caves, the barge-and-net method, the blackjaw-and-crab diet, the fanners' description and origin, the fungi, the central pillar and the no-slaves line are all printed.
- Title: `mk-repos/mk-sandbox/locations/new-giustenal.json`
  - Section: full entry
  - Printed page: —
  - Source type: campaign record (read-only)
  - Adaptation note: The record being revised. Not edited locally.

## Unresolved Questions

*(Both answered by the campaign owner, 13 August 2026.)*

- ~~Whether the fishermen's plans against the sharg should become a clock~~ — **an escalation ladder, starting as a hook.** (1) By default a **hook only**: the fishermen are openly planning "should the templars continue to ignore the situation", and the templars will not act because **Dregoth ordered the sharg left alone until he can control the creature he brought to Athas himself**. (2) **If the players ignore it**, a clock opens **on the sharg** — more barges destroyed, more dray dragged from the shore. (3) **If it is still ignored**, the clock moves **here**, to the city: the fishermen act without the templars.
- ~~Whether the bone golems and gate templars belong on the location or on a faction record~~ — **split, with links both ways.** The **five bone golems** stay here as a fixed installation at the inner gates (AC 0, HD 14, 70 hp each, 3–24 damage, half damage from edged and piercing weapons, always at attention). The **eight gate templars** go on the dray church faction record as rotating personnel — `faction-new-giustenal` exists and is the natural home. This record names the faction that mans the gate; that record names the post. Neither reads correctly alone.
