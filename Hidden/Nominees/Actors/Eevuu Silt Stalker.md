---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: Eevuu Silt Stalker (update to existing actor-eevuu-silt-stalker, revision 4)

*(Update to existing actor `actor-eevuu-silt-stalker`. **No printed stat block — see Sources.**)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/eevuu-silt-stalker.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-eevuu-silt-stalker |
| `name` | Eevuu Silt Stalker |
| `actorType` | named-npc |
| `status` | active |
| `role` | Ruler of the Silt Stalkers |
| `factionId` | faction-silt-stalkers |
| `presenceStatus` | unconfirmed |
| `description` | Rules through fear, intimidation, and death-fights; wary of Giustenal despite dreams of great raids. |
| `goals[]` | **Decide whether to send more of the tribe toward Giustenal.** — priority 4, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — The Silt Stalkers (pp. 14-15) |
| `simulation` | {"proposalMode": "triggered", "reason": "The source establishes Eevuu's strategic posture, but no campaign event confirms a current location or activates off-screen proposals for him."} |

## One-Sentence Summary
The chief of a raiding tribe that rules by fear and death-fights, who has lost a third of his people to a ruin he is afraid of, is being fed prophecies by the defiler who took them, and is one more refusal away from being murdered for it.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active — **and marked**
- Faction or allegiance: Silt Stalkers elf tribe — **chief**
- Current location: with the Silt Stalkers, eastern Tyr region
- Current route, when traveling: the tribe's raiding range across the eastern Tyr region
- Role: Tribal chief

## Player-Safe Description

### Appearance
*(Proposed — the source gives none.)* A raiding chief who has held his position through violence and expects to be looked at.

### Manner and Voice
*(Manner proposed; behaviour printed.)* **He rules the tribe through fear, intimidation, and the occasional death-fight.**

He is also, at present, **hesitating** — and everyone can see it.

### Public Reputation
Chief of a tribe that **delights in attacking travellers and small settlements**, for whom **the plunder the raids provide is simply an added bonus.**

## Confirmed Facts
- **Eevuu Silt Stalker rules the tribe through fear, intimidation, and the occasional death-fight.**
- The Silt Stalkers **terrorise the eastern portion of the Tyr region.** They **delight in attacking travellers and small settlements** — **the plunder the raids provide is simply an added bonus.**
- The tribe consists of three clans: **Fire Bow, Fire Dagger, and Fire Sword.**
- **The Fire Dagger clan has disappeared recently, after being sent to explore the ruins of Giustenal by [[Luubarra Fire Dagger]], the tribe's master defiler.**
- **This has caused Eevuu some concern, but Luubarra keeps him occupied with her prophecies of power, glory, and untold riches.**
- **Eevuu has been listening to Luubarra's urgings, but he has yet to send the rest of the tribe to search for the missing clan.**
- **He is wary of the haunted ruins, but his dreams are full of great raids to come — provided he follows the advice of his chief defiler.**
- **Luubarra is currently working to convince Eevuu that the rest of the Silt Stalkers should join the Fire Daggers. If he continues to refuse, Luubarra will take matters into her own hands.**
- The tribe is detailed further in **DSS3 *Elves of Athas***.

## Goals
1. Description: Keep the tribe raiding and keep himself on top of it.
   - Priority: 5
   - Progress: ongoing
   - Target: —
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: Find out what happened to the Fire Dagger clan — **without going into Giustenal.**
   - Priority: 4
   - Progress: stalled
   - Target: 1
   - Deadline day: none set
   - Secret: partially — **he is not advertising the concern**
   - Status: active
3. Description: **Not go into the ruins.**
   - Priority: 5
   - Progress: holding, and being worn down
   - Target: —
   - Deadline day: **until Luubarra runs out of patience**
   - Secret: **yes — he is wary, and a chief who rules by fear cannot say he is afraid**
   - Status: active

## Traits and Pressures
*(Ambition, cruelty and rule-by-fear are printed; the rest are proposed.)*
- Ambition: High, and conventional — raids, plunder, standing.
- Caution: **Higher than his reputation allows him to admit.** He is wary of Giustenal and has stalled for a long time.
- Secrecy: 3 — specifically about the fear.
- Loyalty: To the tribe as his possession.
- Cruelty: **High.** Rule by fear, intimidation, and death-fights.
- Risk tolerance: High in raids, **low about the ruins.**
- Safety: **Poor, and he does not know it.** His chief adviser is preparing to remove him.
- Wealth: Tribal plunder.
- Status: Chief — **and being managed by a subordinate.**

## Resources and Capabilities
- **Two remaining clans** of a feared raiding tribe — Fire Bow and Fire Sword.
- Command authority backed by the credible threat of a death-fight.
- Deep knowledge of the eastern Tyr region's travel routes and settlements, from raiding them.

## Relationships
- Existing actor or faction ID: `actor-luubarra-fire-dagger`
  - Attitude: **Reliant, manipulated, and unaware**
  - Reason: She is his chief defiler and prophet. **She has already sold a third of his tribe to Dregoth as undead**, and **she will kill him if he keeps refusing.**
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **Unknowing supplier**
  - Reason: Dregoth has a deal with Luubarra requiring **the whole Silt Stalker tribe** to come to Giustenal. Eevuu is the last obstacle to it.
- Proposed actor or faction ID: `faction-fire-dagger-clan` *(not yet in mk-sandbox)*
  - Attitude: **His missing clan**
  - Reason: Sent to Giustenal by Luubarra; now Dregoth's undead warriors.

## Knowledge
- Subject: The Fire Dagger clan
  - Claim: They went to Giustenal at Luubarra's direction and did not come back. **He is concerned.**
  - Source: Direct.
  - Learned day: recently
  - Confidence: certain
  - Truth status: true — **and he does not know they are undead in Dregoth's service**
  - Secret: partially
- Subject: The eastern Tyr region
  - Claim: Raiding routes, settlements, caravan patterns.
  - Source: His trade.
  - Learned day: ongoing
  - Confidence: high
  - Truth status: true
  - Secret: no

## Current Activity
Stalling, while the woman who took his missing clan explains to him nightly why he should send the rest.

## GM-Only Secrets
- **He is a doomed man who has made the correct decision.** Everything about Eevuu — the fear-rule, the raiding, the cruelty — is set dressing on one printed fact: **he is right not to go into Giustenal, and it is going to get him killed.**
- **He is the party's cheapest possible lever on the Silt Stalkers.** A tribe of feared raiders is currently one piece of evidence away from turning on its own defiler. **If the party can prove the Fire Daggers are undead in Dregoth's service, Eevuu will act** — and a chief who rules by death-fight has a very direct way of acting.
- **The assassination is on a trigger the party can pull either way.** *If he continues to refuse, Luubarra will take matters into her own hands.* **Stiffening his resolve accelerates it. So does doing nothing.** There is no version where the situation holds.
- **If Luubarra wins, the whole tribe walks into Giustenal**, and Dregoth's army gains two more clans of elves. **That is a live worsening of the campaign's endgame that runs entirely in the background if the party ignores Chapter Two.**
- *(Proposed.)* His dreams are Luubarra's work. The module says his dreams are full of great raids *provided he follows the advice of his chief defiler* — which reads much less like optimism and much more like a defiler with psionics working on a sleeping man.

## Proposed Developments
- **Recommended:** make the Fire Dagger clan's fate findable in Giustenal, and make the party carry it back. It is a rare case where information is a weapon.
- Run the death-fight. If Eevuu confronts Luubarra, a tribal chief challenging his own defiler in front of two clans is the best set-piece in the environs.
- If the party never engages, resolve it offscreen and let them find the Silt Stalkers gone.
- Give him a stat block before he is needed — see below.

## Stat Block or Rules Notes
*(No printed stat block in City by the Silt Sea. Proposed, built to role. **DSS3 *Elves of Athas* may carry a fuller entry — check before finalising.**)*
- Class: Fighter
- Level: 8
- Armor Class: 14
- Hit Points: 52
- Movement: near (double near — Athasian elf)
- Strength +3, Dexterity +3, Constitution +2, Intelligence +1, Wisdom +1, Charisma +2
- Alignment: Chaotic (evil)
- Morale: 13
- Attacks: 2 attacks per round.
  - *Elven long sword* +7, 1d8+3
  - *Bow* +6, 1d6+3 (far range)
- **Rule by Fear:** advantage on checks to intimidate or command Silt Stalkers. **A challenger must beat him in a death-fight to displace him** — this is the tribe's actual succession mechanism and Luubarra intends to bypass it.
- **Elf Sprint:** double near movement.
- **Raider's Ground:** advantage on checks to ambush, track or run down travellers in open desert.
- **Wary of the Ruins:** he will not enter Giustenal. This is not cowardice at the table; it is the correct call and should be played as judgement.
- **Running him at the table:** brutal, direct, and quietly stalling. The players should meet a terrifying raider chief and slowly realise he is frightened of something and being handled by his own adviser.
- **Conversion note:** **no stat block exists in this source** — the module describes him in two paragraphs and refers the reader to DSS3 *Elves of Athas*. Everything above is constructed.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Eevuu Silt Stalker, chief of an Athasian elf raiding tribe, standing upright in a neutral token pose. Tall powerfully built elf man, six and a half feet, long-limbed, hard weather-scoured face with old raid scars, cold assessing eyes, dark hair shaved at the sides and bound above. Wears raider's leathers hung with taken trophies — bone fetishes, scraps of enemy cloth, a scavenged metal buckle — over dust-colored wraps, wrapped forearms, worn sandals. Carries an elven long sword drawn and held low, a bow slung at the back. Brutal, commanding, faintly unsettled bearing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two: Giustenal Environs — The Silt Stalkers
  - Printed page: 14
  - Source type: official
  - Adaptation note: **No stat block.** The rule-by-fear, the three clans, the missing Fire Daggers, his wariness and Luubarra's ultimatum are all printed. Everything in the stat block is constructed.
- Title: DSS3 *Elves of Athas*
  - Section: Silt Stalkers
  - Printed page: —
  - Source type: official cross-reference
  - Adaptation note: **The module refers the reader here for the full tribe.** Available in the vault at `Hidden/Books/Elves of Athas.md`. Worth checking for a fuller Eevuu entry before this nominee is submitted.
- Title: mk-sandbox `actors/eevuu-silt-stalker.json`
  - Section: —
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: This nominee proposes an update.
  - Id note: `actor-eevuu-silt-stalker`, `actor-luubarra-fire-dagger`, `actor-dregoth` resolve to real sandbox records. `faction-fire-dagger-clan` — the vault has a [[Fire Dagger Clan]] page; confirm the sandbox id.

## Unresolved Questions
- **Does *Elves of Athas* give him a stat block?** Check before finalising.
- Whether he survives Luubarra.
- Whether the party ever tells him what happened to the Fire Daggers.
