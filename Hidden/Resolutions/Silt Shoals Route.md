# Resolution draft — Silt Shoals Route

**Record:** `routes/silt-shoals.json` · `route-silt-shoals` · revision 1 · status *open but hazardous*
**Printed source:** *City by the Silt Sea* — Campaign Book pp. 15, 18, and the Adventure Book
**Twin records:** `location-cromlin`, `location-break-shore`, `location-house-mke-village`, `actor-captain-gaff`

---

## 1. "The route's precise distance, navigation procedure, and water cost are not established."

Three clauses, and they do **not** share a verdict. The middle one is answered outright, and answered in a way that changes how the route should be modelled.

### Navigation procedure — **ANSWERED**

> *"A great deal of trade takes place between the merchants of Cromlin and those in Raam, due mostly to the so-called 'Silt Shoals.' The navigators and skimmers (Athasian silt sailors) believe that there are a series of shoals that form a winding path through the Silt Sea between Cromlin and Break Shore on the other side. Only a brave few know the route to the House M'ke village, however, and these navigators are in high demand. **None of them ever make a map of the Silt Shoals, for to do so would endanger their livelihood, or at least reduce the exorbitant wages they command.**"*

That is a procedure, and a hard one:

- The route runs **Cromlin ↔ Break Shore**, a **winding path** across the Silt Sea, and it is what makes the **Cromlin–Raam** trade work.
- It is **pilot knowledge, not a map.** Passage requires **hiring one of the few navigators who know it**, and they command **exorbitant wages**.
- **No map exists, and that is deliberate** — the navigators refuse to make one to protect their livelihood.
- The shoals are a **pirate hunting ground**: pirates *"utilize silt skimmers to ambush other vessels plying the Silt Shoals"*, from a base *"hidden in a large cavern to the west of the village."*
- Even the *Firewind* is described by whether it **is or is not "crossing the silt shoals"** — the region's largest skimmer runs this route as routine business.

**The unmappability is the point.** A party cannot buy their way past this with cartography; they must hire a person, and that person is a scarce, expensive, bribable, killable NPC. Modelling this as a route with a distance and a water cost misses what the printed source actually makes it: **a gated route whose gate is a hireling.**

### Precise distance — **PRINTED SILENCE**

No mileage, no travel time, no hex count anywhere. The book gives a direction and two endpoints and stops. Under *silence stays silent*, this closes; if the campaign needs a number it is a **GM DECISION**, not a research task.

### Water cost — **PRINTED SILENCE**

Never stated for this crossing.

---

## Proposed changes

1. **Add the navigator gate** — a `conditions[]` entry recording that passage requires hiring one of the few navigators who know the winding path, at exorbitant wages, and that **no map of the shoals exists by design**.
2. **Add the pirate ambush risk**, tied to the base in the cavern west of Cromlin, and cross-reference `plot-black-wake-war`, which already runs over these routes.
3. **Confirm the endpoints** — `location-cromlin` ↔ `location-break-shore`, with House M'ke village as the destination the navigators are hired for, and note the Cromlin–Raam trade this route carries.
4. **Retire the distance and water-cost clauses** as printed silence; if the campaign wants numbers, raise them as a GM decision rather than leaving them looking like unfinished research.

---

## Flagged separately — a possible name problem

The Campaign Book renders Passk's skimmer as **"Silt Sheer"** at p. 20 while the sandbox and the rest of the text use **"Silt Slicer"**. The book text here is OCR and this looks like an OCR artefact rather than a second name, **but it has not been verified against a clean copy.** Not proposed as a change; recorded so the next person does not "correct" the sandbox to an OCR error.

---

## Summary

| clause | Verdict |
|---|---|
| Navigation procedure | **ANSWERED** — pilot knowledge, unmapped by design, hired at exorbitant wages |
| Precise distance | **PRINTED SILENCE** → GM decision if a number is needed |
| Water cost | **PRINTED SILENCE** |

**Net:** the item as written implies three research gaps. One is a substantial printed rule the record is missing, and the other two are silence. The route should carry a hireling gate, not a distance.
