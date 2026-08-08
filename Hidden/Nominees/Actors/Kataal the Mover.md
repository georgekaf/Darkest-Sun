---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: Kataal the Mover (update to existing actor-kataal-the-mover, revision 4)

*(Update to existing actor `actor-kataal-the-mover`. **This file answers an open question flagged on [[Jessareen]] — what Kataal put in her mind.**)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/kataal-the-mover.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-kataal-the-mover |
| `name` | Kataal the Mover |
| `actorType` | named-npc |
| `status` | inactive |
| `role` | Disembodied psyche controlling an ancient transport system |
| `locationId` | location-under-region-tunnels |
| `description` | The surviving psyche of a Green Age halfling, housed in a psionic device beneath Giustenal. |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Kataal the Mover (pp. 5-7) |
| `simulation` | {"proposalMode": "excluded", "reason": "Bound to an ancient psionic item and activated by interaction."} |

## One-Sentence Summary
All that remains of a halfling from the Green Age — a psyche sealed in a psionic device beneath Giustenal, still running a transport system for a city that has been rubble for centuries, and carrying the true history of Athas in a form that drives listeners insane.

## Classification
- Subtype: named-npc — **disembodied psyche**
- Control: autonomous
- Status: **`inactive`, per the sandbox record — and that is the right call.** He is *dormant*, not gone: `simulation.proposalMode` is `excluded` because he is *"bound to an ancient psionic item and activated by interaction."* An earlier draft of this nominee proposed `active`; that was a prose reading of "still running the transport system", not a schema status. **No change proposed.**
- Faction or allegiance: none. His city and his age are both gone.
- Current location: `location-under-region-tunnels` — within a psionic item, deep below
- Current route, when traveling: he does not move; **he moves other things**
- Role: Controller of the psionic transport system beneath Giustenal

## Player-Safe Description

### Appearance
None. **Kataal is a psyche placed within a psionic item.** What a visitor encounters is contact, not a body.

### Manner and Voice
He **intones**. The one line of his the source records is delivered as narration over images:

> *"So began the Age of the Sorcerer-Kings — an age that still exists but is rapidly coming to a close."*

He does not converse so much as **place things in your mind.**

### Public Reputation
None. Nobody on the surface knows he exists — **except [[Jessareen]], who cannot explain him.**

## Confirmed Facts
- **The being known as Kataal the Mover is all that remains of a halfling from the Green Age of Athas.**
- **Kataal's psyche was placed within a psionic item deep in the tunnels below Giustenal.**
- **There, he controlled an intricate transportation system with the Way.**
- **His psyche can still be encountered in the tunnels, and that is where [[Jessareen]] met him.**
- **The images Kataal placed in the elf bard's mind are real. They are the memories of his own experiences, the scenes he witnessed as time passed by.**
- **The disembodied psyche doesn't know everything, however. He only knows what he was able to read from the minds of Giustenal's many occupants and the travellers that stopped by on their way across the region.**
- **If adventurers meet Kataal and he decides to grant them the knowledge of the ages of Athas, the chances are good that they will go mad.**
- **That's what happened to Jessareen, and now she has only brief moments of lucidity before the scenes boiling in her mind again overcome her.**
- The history he carries — the **Blue Age**, the halfling nature-masters, the failed experiment and the brown tide, the **Rebirth**, the **Green Age**, Rajaat, the Cleansing Wars, and the Age of the Sorcerer-Kings — **is the framing narration of the entire campaign book's first chapter.** It is presented as *"the story of the ages of Athas as Kataal the Mover placed them in my mind. It is a confusing story, full of incredible events, but I believe it to be true."*

## Goals
1. Description: Keep the transport system running.
   - Priority: 5
   - Progress: **still running, for a city that no longer exists**
   - Target: —
   - Deadline day: —
   - Secret: no
   - Status: active
2. Description: *(Proposed.)* Give the history to someone who can carry it.
   - Priority: 4
   - Progress: **one attempt so far; she is now a tragic figure**
   - Target: —
   - Deadline day: none set
   - Secret: no
   - Status: active

## Traits and Pressures
*(Almost entirely unrecorded. What the source supports:)*
- Ambition: None available to him.
- Caution: **None.** He gave a bard the ages of Athas and destroyed her.
- Secrecy: 0 — **the opposite. He wants to be heard, and being heard is the danger.**
- Loyalty: To a city and an age that ended before the Cleansing Wars.
- Cruelty: **Not intended.** Nothing suggests he meant to break Jessareen.
- Risk tolerance: Not applicable.
- Safety: He is a psyche in a device. Whether he can be destroyed is unaddressed.
- Status: The oldest surviving mind in the campaign.

## Resources and Capabilities
- **Control of an intricate psionic transportation system** beneath Giustenal — **an intact Green Age technology, still functioning.**
- **Eyewitness memory of the Blue Age's end, the Rebirth, the Green Age, the Time of Magic, and the Cleansing Wars.**
- **The accumulated readings of every mind that passed through Giustenal** across that entire span — occupants and travellers alike.
- The ability to place those memories directly into another mind. **This is not a spell; it is what he is for.**

## Relationships
- Existing actor or faction ID: `actor-jessareen`
  - Attitude: **Recipient, and casualty**
  - Reason: **She went looking for [[Jessix the Wanderer]] and met Kataal instead.** Her songs are now strange and confused. **She has only brief moments of lucidity.**
- Existing actor or faction ID: `actor-taraskir`
  - Attitude: *(Proposed.)* Remembered
  - Reason: Kataal was under Giustenal through the Time of Magic. **Taraskir ruled it then.** Kataal is the only surviving mind that watched the Ravager of Giants take the city.
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **Watched**
  - Reason: *"Giustenal's armies, led by Dregoth, ravaged the land. As more and more sorcery was used, more and more of the lush countryside withered and died… The races I couldn't identify were systematically wiped out as I watched the years roll by."*
- Existing actor or faction ID: `actor-caller-in-darkness`
  - Attitude: **Unresolved — see GM-Only Secrets**
  - Reason: Two psychic entities in the ruins of the same city, one an aggregate of absorbed minds and one a preserved single mind. **The module never puts them in the same sentence.**

## Knowledge
- Subject: **The true history of Athas**
  - Claim: The Blue Age, the halflings' fatal experiment, the Rebirth, the Green Age, Rajaat's rise, the thirteen Champions, the Cleansing Wars, the imprisonment of Rajaat, the making of the Dragon, and the fall of Giustenal.
  - Source: **He was there for most of it, and read the rest from the minds of people passing through.**
  - Learned day: continuously, from the Green Age onward
  - Confidence: high
  - Truth status: **true — the module presents his account as the campaign's actual history**
  - Secret: **no. He will give it to anyone. That is the problem.**
- Subject: The limits of what he knows
  - Claim: **He only knows what he could read from the minds of Giustenal's occupants and passing travellers.**
  - Source: —
  - Learned day: —
  - Confidence: —
  - Truth status: **true, and important — he is a witness, not an oracle. He does not know what nobody in Giustenal knew.**
  - Secret: no

## Current Activity
Running a transport system under a dead city, waiting for the next mind to arrive.

## GM-Only Secrets
- **He is the answer to the [[Jessareen]] question.** Her nominee flags *"what Kataal showed her"* as the biggest open slot in Chapter Two. **It is not open — it is the entire first chapter of the campaign book.** He gave her the ages of Athas, unfiltered, and **the images are real.** She is not deluded; she is overloaded.
- **Meeting him is a save-or-lose-your-mind proposition and the module says so plainly:** *if adventurers meet Kataal and he decides to grant them the knowledge of the ages of Athas, the chances are good that they will go mad.* **This should be an explicit, telegraphed choice**, not a trap. The players should be able to see what happened to Jessareen first.
- **He is the single greatest information source on Athas that the campaign can offer** — and the price is a PC. **A party that wants the truth about Rajaat, the Champions, the Blue Age or the Dragon can have all of it.** That is an extraordinary thing to put in front of players and should be run as a genuine temptation.
- **His limitation is the interesting constraint.** He knows what Giustenal knew. **He does not know what happened after the city fell** — which means he does not know about Dregoth's undeath, New Giustenal, the dray, or the Caller. **He is a perfect historian and a useless scout.**
- **The transport system still works.** An intact Green Age psionic transit network under the ruins, with a functioning controller, is a mobility asset for anyone who can talk to him — **and the module places it in Chapter Five, where the party will badly need to move between the Sunken City, the Groaning City, Kragmorta and New Giustenal.**
- *(Proposed.)* He does not know he is dead, or he does and has decided it is irrelevant. Either reading works and they play very differently.

## Proposed Developments
- **Recommended:** show them Jessareen first. Her broken songs, then the tunnels, then the offer. The choice only lands if they have seen the cost walking around.
- Partial transfers are the obvious mercy: let him give a **single age** rather than all of them, at proportionate risk. The module does not offer this and a GM should.
- Use the transport network as the practical reward. A party that treats him decently gets to move through the under-regions.
- The Kataal / Caller in Darkness relationship is completely unwritten and is the best unclaimed idea in the set. **Two minds under one dead city, one preserving and one consuming.**

## Stat Block or Rules Notes
- Class: — (disembodied psyche in a psionic item)
- Level: —
- Armor Class: — **he has no body**
- Hit Points: — **see below**
- Movement: none
- Alignment: Neutral
- Morale: —
- Attacks: **none.** Kataal does not attack and has never harmed anyone deliberately.
- **Ages of Athas:** if Kataal chooses to grant the full history, the recipient must save. **On a failure, the character is rendered functionally insane** — treat as [[Jessareen]]: **brief moments of lucidity before the scenes overwhelm them again.** This is not a temporary condition and there is no printed cure.
- **Partial Transfer (proposed, not printed):** a single age at a time, at reduced risk. **Recommended house ruling** — the printed all-or-nothing version costs a player their character with no middle ground.
- **The Mover:** controls an intricate psionic transportation network beneath Giustenal. **He can move those he chooses to move.**
- **Witness, not oracle:** he knows only what he witnessed or read from minds in Giustenal. **He knows nothing of events after the city fell.**
- **Destroying him:** unaddressed by the source. He is a psyche in an item; the item presumably exists and presumably can be broken. **A GM should decide what that would mean before a player asks.**
- **Running him at the table:** he intones. He does not chat. Give him one line and then describe what arrives in the character's head.
- **Conversion note:** the module gives Kataal **no statistics of any kind** — he is a narrative entity in Chapter One and an encounter in Chapter Five. Everything above is constructed from his printed function and the printed consequence of meeting him.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body token of Kataal the Mover — **the psionic item, not a person** — standing upright in a neutral token pose. An intricate Green Age psionic device roughly the height of a halfling, carved from pale porous stone shot through with veins of crystal, its surface covered in worn geometric channels and inlaid nodes that still hold a faint inner light. Vaguely suggestive of a seated figure without depicting one. Ancient, worn smooth in places by centuries, dust-caked in the recesses, unmistakably still working. Serene, alien, deeply old presence; cool blue-green internal glow. Dark Sun inspired, pre-Cleansing-Wars halfling aesthetic, gritty realism. Full object visible from base to top, clear silhouette, centered subject, neutral transparent or plain background, suitable for a VTT token, no environment, no scene.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter One: Giustenal's History — Stories of Ages Past; **Kataal the Mover**; Giustenal Through the Ages; The Coming of the War-Bringer
  - Printed page: 5–8
  - Source type: official
  - Adaptation note: **No statistics of any kind.** His nature, his function, the reality of the images, the limits of his knowledge, and the madness consequence are all printed. **Chapter Five carries the encounter itself — consult it before running him.**
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two: Giustenal Environs — Jessareen
  - Printed page: 13
  - Source type: official
  - Adaptation note: Source of Jessareen's post-Kataal condition.
- Title: mk-sandbox `actors/kataal-the-mover.json`
  - Section: —
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: This nominee proposes an update.
  - Id note: `actor-kataal-the-mover`, `actor-jessareen`, `actor-jessix-wanderer`, `actor-taraskir`, `actor-dregoth`, `actor-caller-in-darkness`, `location-under-region-tunnels` all resolve to real sandbox/vault records.

## Unresolved Questions
- **Adopt the partial-transfer house ruling?** The printed version costs a PC outright.
- What his relationship is, if any, to the Caller in Darkness.
- Whether the item can be moved, taken, or destroyed.
- Whether Jessareen can be cured — and whether Kataal could do it.
