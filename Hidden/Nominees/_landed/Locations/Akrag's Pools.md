---
entryType: location
entrySubtype: site
authorGM: "Ghost"
visibility: mixed
---

# Location: Akrag's Pools

*(New location. **No record exists in mk-sandbox** — verified 2026-08-12 against `locations/` on the default branch. Proposed id `location-akrags-pools`. Its owner is already a vault nominee: [[Absalom]] (`actor-high-priest-absalom`, which resolves to a real sandbox record).)*

## Summary
The public baths of New Giustenal — darker and seedier than any other, with a reputation for the assassinations that happen in its steaming pools, and run by a dray called Akrag who is in fact Dregoth's High Priest wearing another face.

## Classification
- Location subtype: bathhouse / public establishment
- Region: New Giustenal, area 11
- Terrain: subterranean city district
- Parent location: `location-new-giustenal` — **resolves to an existing sandbox record** (revision 5). **Linked both ways** per the owner's ruling of 13 August 2026: this record names New Giustenal as parent, and `location-new-giustenal` gains a `connections[]`/`features[]` pointer back to `location-akrags-pools`. The pointer on the parent is filed with the New Giustenal revision, #410.
- Status: open and operating
- Controller: "Akrag", a dray — in truth [[Absalom]]
- Contested by: nobody openly

## Player-Safe Arrival Description
Steam, low light, and water that stays hot without anyone tending a fire. The pools are darker than the rest of the city and nobody minds. Talk here is quiet, and it stops when strangers walk in.

## Physical Features
- Public bathing pools, steaming, dimly lit.
- **Water drains** running out of the baths and into the Blackjaw River — the disposal route for at least one body.

## Population and Occupants
- Akrag, the owner, present and hands-on.
- Bathers: any dray. No guard force recorded.

## Resources
- Water: abundant and hot — remarkable on Athas, unremarkable in New Giustenal.
- Trade: bath fees, unrecorded.
- Guards: none recorded, which is itself the point.

## Important Actors and Factions
- `actor-high-priest-absalom` — **the owner, under the name Akrag.** The sandbox record exists (revision 3) but carries no aliases, so nothing on it connects him to the baths. The Absalom revision nominee now proposes adding the alias `"Akrag"` and `location-akrags-pools` to his `associatedLocationIds[]`, so the two records point at each other. **The disguise is live** — owner's ruling, 13 August 2026.
- Dregoth's templar corps — one of their own was murdered here.

## Dangers
- **Assassination is what this place is known for.** Several have happened in the pools.
- A mid-level templar was recently murdered while bathing; the body went out through the water drains into the Blackjaw River and was never seen again.
- Anyone the High Priest wants to overhear is overheard here.

## Opportunities
- The single best place in New Giustenal to hear something that was not meant to be said aloud.
- A party that works out who Akrag is holds a genuinely dangerous secret.

## Connections
- Destination: **Blackjaw River**
  - Proposed location ID: `location-blackjaw-river`
  - Travel notes: not a route — the bath drains empty into it. That is how the templar left.
- Destination: **Temple of the Dragon** — Absalom's other workplace. Proposed id `location-temple-of-the-dragon`.

## GM-Only Secrets
- **Akrag is Absalom**, Dregoth's trusted High Priest and the first dray. The module directs the DM to the cardstock sheets supplied with the boxed set for his statistics and for role-playing him while in the guise of Akrag.
- The baths are therefore not a seedy business that attracts killers; they are an intelligence operation with a body-disposal system plumbed into the river.

## Proposed Developments
All unapproved.
- The murdered templar is an unclosed case with a named suspect the party cannot possibly suspect.
- If Absalom ever needs to meet the party without the Temple watching, this is where he does it.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Five: The Ruins Below — New Giustenal, area 11 "Akrag's Pools"
  - Printed page: **84**
  - Source type: official
  - Adaptation note: Owner, reputation, the assassinations, the murdered templar, the drains into the Blackjaw, and the Akrag/Absalom identity are all printed. Nothing here is invented.
- Title: `mk-repos/mk-sandbox/actors/high-priest-absalom.json`
  - Section: full entry
  - Printed page: —
  - Source type: campaign record (read-only)
  - Adaptation note: The owner resolves to an existing actor. The Akrag identity is not currently on that record.

## Unresolved Questions
- Whether the campaign wants the Akrag disguise live, or whether Absalom's cover has already lapsed.
- Who killed the templar, and on whose instruction.
- Whether `location-new-giustenal` should gain a `subLocations` or `features` entry for the baths, or whether the baths stand as their own record.
