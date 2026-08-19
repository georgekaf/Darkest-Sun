# Resolution draft — the Square of Gurdek as a faction

**Not a record.** This sheet resolves **one structural question that appears as an unresolved item on at least four separate records**, so that it is answered once instead of four times.

**Affected records:** `actors/slate.json`, `actors/ranza.json`, `actors/pargo.json`, `actors/gurdek.json` — and by extension `actors/mefse.json`, `actors/ari-evan.json`, `actors/olton.json`, `actors/morlah.json`, all of which belong to the group and none of which can carry a `factionId` while it does not exist.

The item appears in these words:

- *"The Square of Gurdek is not a separately registered faction, so no factionId is asserted."* — Ranza
- *"The Square of Gurdek is not a separately registered faction; no factionId is asserted."* — Pargo
- *"The Square of Gurdek has no separately registered faction; its formal faction record remains a design choice."* — Slate

**Verdict: GM DECISION — and the printed material makes the case for yes.**

## What the source establishes about it as a body

- **It has a name its founder chose**: *"Slate has kept his crew together, naming it the Square of Gurdek."*
- **It has a defined internal structure**, and the name encodes it: *"The term 'Square' comes from their habit of sitting in a square when they gather in groups of more than four. The most important members form the corners, with lower-status characters in between them."*
- **It has a fixed, named membership of seven** — Slate, Pargo, Mefse, Ari Evan, Ranza, Olton, Morlah — with classes, levels and genders all printed.
- **It has a doctrine**: the gith are *"descendants of 'earth spirits' and the rightful rulers of all Athas."*
- **It has a recruitment method**, and it is not persuasion: members *"succumbed to Slate's charm spell"*, screened at Wisdom 17–18, under a leader *"immune to charm spells"* himself.
- **It has a seat**: Yathazor, and the location bearing its name contains the vertical tunnel breach the gith use.
- **It acts on the world**: Slate *"helped the gith excavate a wide path to Zigath's Nest"*, materially assisting the gith war effort.
- **It has external reputation**: captured gith elsewhere *"know about the Square of Gurdek… who are helping the gith"*, and others have *"heard about"* it without visiting.
- **It has a posture toward the party**: *"fanatic earth clerics who seem friendly, but are only waiting for the first opportunity to destroy the PCs."*

Name, hierarchy, membership, doctrine, recruitment, territory, external actions, reputation, and a stance toward the PCs. By any test the sandbox applies elsewhere, that is a faction.

## Recommended shape

- `faction-square-of-gurdek`, seated at `location-yathazor`
- **leader** `actor-slate`; members Pargo, Mefse, Ari Evan, Ranza, Olton, Morlah
- doctrine, the charm-spell recruitment, and the corner-seating hierarchy as features
- relationship to the gith: **active collaborator** — the excavation to Zigath's Nest is a confirmed material contribution
- posture toward outsiders: feigned friendliness pending an opportunity

## What filing it would close

The four items quoted above stop being open questions, and seven member records gain a resolvable `factionId` instead of a note explaining why they have none.

**One caution.** Filing this touches every member record, so it should go **after** the Ari Evan level ruling and **with** the Gurdek record's malformed-item deletion, rather than as a separate wave. See `Ari Evan.md` and `Gurdek.md`.
