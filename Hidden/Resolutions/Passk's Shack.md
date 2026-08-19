# Resolution draft — Passk's Shack

**Record:** `locations/passks-shack.json` · `location-passks-shack` · revision 1
**Printed source:** *City by the Silt Sea* — Campaign Book pp. 20–21
**Twin record:** `actors/passk.json`, which carries the same question as its own item 4

---

## 1. "Whether Passk joins an expedition, the Silt Slicer is repaired, or the map is used remains unresolved."

**PLAY-DEPENDENT** — all three clauses. None of them can be settled before a party acts, and the book does not script an outcome.

**But the terms are printed and the record does not carry them**, which is what makes this item look emptier than it is:

> *"Passk hints that he has a map of the walls of Giustenal and a beached silt skimmer that can be repaired. He won't sell the map or the skimmer. He'll only give them to the group in exchange for taking him on the voyage."*

So the three clauses are not three independent unknowns. **They are one transaction with a fixed price**, and the price is passage:

- The skimmer **is repairable** — that is stated, not speculative.
- **Neither map nor skimmer is purchasable at any price.**
- Both transfer **only** in exchange for taking Passk along.
- Therefore *"whether the Silt Slicer is repaired"* and *"whether the map is used"* both collapse into *"whether the party takes Passk"*. One decision, not three.

The map's content is also printed, from Cromlin rumour: *"Said he used to walk into the ruins from the north to avoid the tar pits."*

**Proposed change:** replace the single vague item with the recorded terms, and reduce the open question to the one that is genuinely open — whether a party takes him. Add the northern approach as a feature, since it is the map's actual value and it bears on `location-giustenal-ruins`, which already carries a tar-pit approach.

Also worth fixing while the record is open: its `status` field currently reads *"Dilapidated home of Passk, beside his damaged beached skimmer"*, which is a description sitting in a status field.

---

## Summary

| # | Item | Verdict |
|---|---|---|
| 1 | Expedition / skimmer / map | **PLAY-DEPENDENT** — but three clauses collapse to one, and the printed terms are recordable now |

**Net:** the item stays open by design, but stops being three unknowns and becomes one decision with a known price. A `status` field misuse is worth correcting in the same revision.
