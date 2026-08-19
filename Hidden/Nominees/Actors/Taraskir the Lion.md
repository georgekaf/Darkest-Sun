---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Taraskir the Lion (update to existing actor-taraskir, revision 5)

*(Update to existing actor `actor-taraskir`. **⚠ This file resolves an open Black Spine question — see the Cross-Campaign Resolution below.**)*

## ⚠ Cross-Campaign Resolution — the Lion Temple

The Black Spine nominees flagged an unresolved geography and identity question: **who built the "temple of lion-headed giants" that Tenpug's Band occupies, and where is it?** See Tenpug, Unresolved Questions.

**City by the Silt Sea answers it outright:**

- The temple **dates back to the Time of Magic** and **was originally dedicated to a forgotten god worshipped by Taraskir and his followers.**
- **The lion-headed statues are representations of Taraskir's Lion Guard, his elite warriors.**
- **After Dregoth killed Taraskir, much of Giustenal's remaining demihuman population — and some of the humans — began to worship Taraskir as a god.** This ended shortly after the fall of Giustenal, **and the temple was lost to the sand and silt until Tenpug's Band came across it a few years back.**
- The temple **lies to the west of Cromlin and the ruins of Giustenal**, near the shore of the Silt Sea.
- **As most of Giustenal's ruins are decorated with dragons, none of Tenpug's Band have connected the temple to the ancient city.** The only clues are **faded frescoes in the great hall** showing a city on the edge of a *choppy and motive* sea — Giustenal before Dregoth's rebuilding, **with a waterfall** most Athasians cannot even recognise as such.

**Therefore:** the Black Spine "lion-headed giants" are **Taraskir's beast-head giant Lion Guard**, the temple is **his**, and it sits **near Giustenal, not near Nibenay.** The two sandbox records `location-lion-temple` and `location-tenpugs-temple` are **the same site**, and the Silt Sea placement wins.

## Current record in mk-sandbox

*Read-only snapshot of `actors/taraskir.json` (revision 5, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-taraskir |
| `name` | Taraskir the Lion |
| `actorType` | named-npc |
| `status` | dead |
| `role` | Ancient giant-king of Giustenal |
| `locationId` | location-sunken-city |
| `description` | A beloved beast-headed giant who ruled harmonious Giustenal during the Green Age. Taraskir was a master of the Way, but Dregoth defeated and killed him at the opening of the Cleansing Wars. |
| `traits` | {"presence": 5, "psionicPower": 5, "leadership": 5} |
| `resources` | {"historicalLegacy": 5} |
| `relationships` | `actor-dregoth` -5 |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Stories of Ages Past; The Coming of the War-Bringer (pp. 5-8) |
| `simulation` | {"proposalMode": "excluded", "reason": "Historical dead actor; retained for lore and site relationships."} |

## One-Sentence Summary
The beast-head giant who ruled Giustenal in the Time of Magic, was killed by Dregoth during the Cleansing Wars, and was then worshipped as a god by the survivors of the city he lost.

## Classification
- Subtype: named-npc — **historical**
- Control: —
- Status: **dead** — killed by Dregoth during the Cleansing Wars
- Faction or allegiance: Giustenal, under his own rule
- Current location: `location-taraskirs-tomb`; his temple is `location-lion-temple` / `location-tenpugs-temple`
- Current route, when traveling: —
- Role: Ruler of Giustenal before Dregoth; posthumous god

## Player-Safe Description

### Appearance
**A beast-head giant** — the lion-headed form reproduced in the **huge statues flanking his temple's main doors: giants with the heads of lions, mouths just beginning to open in a kind of snarl, sharp fangs jutting out, weathered by centuries of wind and sand until they are as smooth as bone.**

### Manner and Voice
No dialogue survives. What survives is a reputation: **a beast-head giant of great presence and personal power.**

### Public Reputation
**Ruler of Giustenal**, and afterwards **a god** — worshipped by much of the city's remaining demihuman population and some of its humans, until the fall of Giustenal ended the cult.

## Confirmed Facts
- **Taraskir the Lion, a beast-head giant of great presence and personal power**, ruled Giustenal during the **Time of Magic**.
- **Dregoth, Third Champion of Rajaat the War-Bringer, Ravager of Giants, took his title very seriously, gathered an army, and marched on Giustenal.**
- **Taraskir and his lion warriors were not able to stop the psionics and sorcery of Dregoth.**
- **The Ravager killed Taraskir and slaughtered his chief followers. Then he declared himself Sorcerer-King of Giustenal, and the Cleansing Wars moved into full swing.**
- His **elite warriors were the Lion Guard**, whose likenesses are the statues at his temple.
- **After his death, much of Giustenal's remaining demihuman population began to worship Taraskir as a god.** **This ended shortly after the fall of Giustenal.**
- His temple **was lost to sand and silt until Tenpug's Band came across it a few years back.**
- Vault record: `location-taraskirs-tomb` exists as a distinct location.

## Goals
*(Historical.)*
1. Description: Hold Giustenal against the Ravager of Giants.
   - Priority: 5
   - Progress: **failed**
   - Target: —
   - Deadline day: —
   - Secret: no
   - Status: **ended**

## Traits and Pressures
- Ambition: He ruled a great city of the Time of Magic.
- Cruelty: Unrecorded.
- Status: **King, then god, then forgotten.** All three within the memory of a single ruin.
- **Presence:** the one trait the source names — *great presence and personal power.*

## Resources and Capabilities
*(Historical.)*
- **The Lion Guard** — his elite warriors, beast-head giants, memorialised in stone at his temple.
- Rule of Giustenal at its height, before the dragon-decoration and before the walls Dregoth built.
- A cult that outlived him.

## Relationships
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **Killed by**
  - Reason: Dregoth's title was **Ravager of Giants**, and Taraskir was a giant who held a city. **Taraskir's death is the founding act of Dregoth's kingship.**
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: **Unknowing tenant**
  - Reason: Tenpug's Band occupies his temple. **They take great pains not to anger the old god without knowing whose god it is.**
- Existing actor or faction ID: `actor-rajaat`
  - Attitude: Killed on his orders, at one remove
  - Reason: Dregoth marched on Giustenal to fulfil the title Rajaat gave him.

## Knowledge
Not applicable.

## Current Activity
Dead, and thoroughly forgotten — **including by the people living in his temple.**

## GM-Only Secrets
- **Tenpug's Band is squatting in the tomb-temple of a giant king murdered by the thing living under the ruins next door.** They fear the temple's spirits, keep an offering bowl, and forbid searching the sealed rooms — and they have **no idea** whose house it is or that his killer is still active five miles away. **That is the single best dramatic irony either module produces, and neither one states it.**
- **The frescoes are the only clue and they are unreadable by design.** The great hall's murals show Giustenal *before Dregoth* — lower walls, no central spire, ornamental architecture, **and a waterfall**, which requires an **Intelligence check at −10** to even recognise. **Halflings from the Forest Ridge make it with no modifier.** A halfling PC standing in that hall is the intended key.
- **The dragon decoration is the disconnect.** *As most of Giustenal's ruins are decorated with dragons, none of the members of Tenpug's Band have connected the temple to the ancient city.* Dregoth's obsession with draconic imagery **erased Taraskir from the record so thoroughly that a temple twenty miles away reads as unrelated.**
- **He was worshipped as a god and the cult died with the city.** Whether anything is left of that — in the tomb, in the temple, or in whatever Tenpug's people have been feeding the offering bowl for years — **is entirely open.**
- *(Proposed.)* The offering bowl works. Tenpug's Band has been making offerings to a dead giant-king for years, in his own temple, and the campaign has never asked whether anyone is receiving them.

## Proposed Developments
- **Recommended: adopt the Cross-Campaign Resolution above** and fold `location-lion-temple` and `location-tenpugs-temple` into one record near Giustenal.
- Put a halfling in the great hall and let them recognise the waterfall. It is a printed, earnable revelation with a −10 penalty attached for everyone else.
- Tell Tenpug whose temple it is. The band's entire superstitious relationship with the place changes when the god acquires a name and a killer.
- `location-taraskirs-tomb` exists as a separate vault record — **worth deciding whether the tomb is inside the temple, beneath it, or elsewhere in Giustenal.**

## Stat Block or Rules Notes
**Taraskir is dead before recorded campaign time and has no printed stat block.**

If the campaign needs him — a vision, a fresco-borne memory, a guardian spirit in the temple, or a Dregoth flashback:

- Ancestry: **beast-head giant** (lion)
- Class: Fighter, with psionics
- Level: 10 — he held a city of the Time of Magic and lost only to a Champion of Rajaat
- Armor Class: 17
- Hit Points: 90
- Movement: near
- Strength +4, Dexterity +1, Constitution +4, Intelligence +2, Wisdom +2, Charisma **+4**
- Alignment: Neutral
- Morale: 14
- Attacks: 2 attacks per round.
  - *Great weapon* +10, 2d8+4
  - *Bite* +10, 2d6+4
- **Great Presence:** the one attribute the source names. Advantage on any check to command, awe or rally.
- **Lion Guard:** his elite beast-head giant warriors. If the campaign ever fields them, treat as Huge fighters with reach.
- **Conversion note:** **no printed stat block exists.** The module names him, describes his rule, and kills him in a single paragraph. Everything above is constructed. The statue description is drawn from *Black Spine*, Adventure One, area 5.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Taraskir the Lion, an Athasian beast-head giant king, standing upright in a neutral token pose. Enormous humanoid giant, twelve to fifteen feet tall, powerfully built, with the head of a great lion — heavy mane, broad muzzle, sharp fangs slightly bared in a fixed snarl, golden eyes. Wears ornate ancient armor of the Time of Magic in bronze and dark stone tones, layered with ceremonial cloth in deep reds and golds, heavy shoulder pieces, arm rings. Carries a huge great weapon held upright at rest. Regal, commanding, imposing bearing — a king rather than a beast. Dark Sun inspired, gritty desert fantasy realism, archaic and pre-sorcerer-king in aesthetic. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter One: Giustenal's History — The Coming of the War-Bringer; Chapter Two: Giustenal Environs — Tenpug's Band
  - Printed page: 7, 10
  - Source type: official
  - Adaptation note: **No stat block.** His rule, his Lion Guard, his death at Dregoth's hands, the posthumous cult, and the temple's identity and location are all printed. **This is the source that resolves the Black Spine lion-temple question.**
- Title: DSE2 *Black Spine*, Book One
  - Section: Clash by Night — Tenpug's Camp, area 5 "Statues"; "Inside the Temple", areas 15–20 "Murals"
  - Printed page: 14–15, 20
  - Source type: official
  - Adaptation note: Source of the statue description and the temple murals of lion-headed giants as smiths, weavers and sculptors, and later as soldiers at war with an unseen enemy.
- Title: mk-sandbox `actors/taraskir.json`
  - Section: —
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: This nominee proposes an update.
`actor-taraskir`, `actor-dregoth`, `actor-tenpug`, `actor-rajaat`, `location-lion-temple`, `location-tenpugs-temple` resolve to real sandbox/vault records. **Correction:** `location-taraskirs-tomb` do **not** exist in mk-sandbox and are proposed ids, not existing records.
