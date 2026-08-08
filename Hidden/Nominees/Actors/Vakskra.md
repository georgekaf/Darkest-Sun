---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: Vakskra (update to existing actor-vakskra, revision 5)

*(Update to existing actor `actor-vakskra`.)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/vakskra.json` (revision 5, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-vakskra |
| `name` | Vakskra |
| `actorType` | named-npc |
| `status` | active |
| `role` | Templar-wife commanding Nibenese troops near the captured iron mine |
| `factionId` | faction-shadow-brides |
| `locationId` | location-nibenay-iron-mine-stockade |
| `description` | A field commander sent from Nibenay to contain the gith occupation of an iron mine near the Black Spine. Vakskra must recover the mine without wasting troops, losing the metal, or allowing news of the defeat to damage the Shadow Brides. |
| `traits` | {"authority": 4, "caution": 4, "discipline": 5, "pride": 4} |
| `resources` | {"fieldCommand": 4, "nibeneseTroops": 3} |
| `relationships` | `actor-lady-vardan` +1, `actor-brugg-stone-thumb` +1, `actor-orruk-vesh` +0, `actor-zigath` -5 |
| `goals[]` | **Retake the captured iron mine from the gith.** — priority 5, progress 0, status active |
| `goals[]` | **Recover the mine without destroying the surviving Nibenese force.** — priority 4, progress 0, status active |
| `goals[]` | **Prevent the defeat and the gith metal weapons from becoming public knowledge.** — priority 4, progress 0, status active |
| `sourceRefs[]` | Darkest Sun project planning — Captured Nibenay iron mine and Black Spine expedition (pp. ?) |
| `sourceRefs[]` | DSE2 Black Spine — Cry Vengeance: At the Gate (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
A templar-wife of Nibenay whose relief column has been reduced to a handful of survivors — she cannot advance, cannot retreat, and cannot report, which makes her the most negotiable enemy in the campaign.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-shadow-brides` — templar-wife of Nibenay
- Current location: `location-nibenay-iron-mine-stockade`
- Current route, when traveling: `location-nibenay` ↔ `location-black-spine-mountains` ↔ `location-nibenay-iron-mine`
- Role: Field commander of the Nibenese relief expedition

## Player-Safe Description

### Appearance
A hard-faced templar-wife in dust-darkened wraps, carrying a bone command baton and a map case sealed in black wax. Young — the module says so — and visibly running an operation several sizes larger than her experience.

Her surviving troops are a ragged bunch. At distance, a scout can easily mistake them for raiders or slavers, and the module expects exactly that mistake to be made.

### Manner and Voice
Disciplined, clipped, and careful. Vakskra negotiates the way someone negotiates who has already worked out that she has no alternative and does not intend to let that show. She asks a great many questions and answers fewer.

She is **very curious** about who the PCs are and where an army of ex-slaves came from, and she will keep asking, politely, for as long as the alliance lasts.

### Public Reputation
Within Nibenay: an officer of the Shadow Brides on a mission that has gone badly. Outside it: unknown, and easily mistaken for a slaver — which nearly gets her exterminated by her own prospective allies.

## Confirmed Facts
- A **templar-wife of Nibenay**, and leader of the Nibenese unit sent to liberate the captured iron mine.
- Her unit was part of a much larger force sent to retake the mine and reopen it, so that vital iron ore would continue to flow to Nibenay.
- The force suffered the same psionic assault from [[Askai]] that the PCs did, compounded by constant gith skirmishing on its flanks. It has been reduced to a pitiful state.
- **She cannot go back** and tell the sorcerer-king she failed utterly with only a handful of her men alive.
- **She cannot go forward** — her scouts report the gith garrison is too strong for her small unit alone.
- She is **definitely open to negotiation**.
- Her terms: she will help the PCs besiege the fortress, **as long as Nibenay is allowed to reopen and use the mine once the gith are killed**.
- She will take no action against the PCs in exchange for their help, and recognises good fortune when it smiles on her.
- Her surviving force includes freed slave warriors (3rd-level fighters, hide and shields, low morale that rises if freed) and Nibenay regulars (4th-level fighters, bone halberds, thick studded leather).
- **If the PCs attack instead**, her people are not ready for battle and will only have time to form up into a single unit — less, if the PCs plan well.
- Nibenay dug the mine and built the stockade that is currently protecting the gith.
- The mine was lost when miners dug too deep and struck a gith nest.

## Goals
1. Description: Retake the captured iron mine from the gith.
   - Priority: 5
   - Progress: stalled — insufficient force
   - Target: 6
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: Recover the mine without destroying what is left of the Nibenese force.
   - Priority: 4
   - Progress: —
   - Target: 1
   - Deadline day: none set
   - Secret: no
   - Status: active
3. Description: Prevent the defeat — and the existence of gith metal weapons — from becoming public knowledge.
   - Priority: 4
   - Progress: holding, for now
   - Target: 1
   - Deadline day: none set
   - Secret: yes
   - Status: active
4. Description: Find out who these people are and where an army of armed ex-slaves came from.
   - Priority: 3
   - Progress: asking
   - Target: —
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Authority: 4
- Caution: 4
- Discipline: 5
- Pride: 4
- Ambition: Moderate, and currently subordinate to survival.
- Secrecy: 4 — the news-control goal is the one she will not discuss.
- Loyalty: To Nibenay, and to the Shadow Brides' standing within it.
- Cruelty: Not demonstrated. She is an officer with a problem, not a villain.
- Risk tolerance: Low, enforced by circumstance rather than temperament.
- Safety: Poor and improving only if she allies.
- Wealth: A ruined expedition's remaining stores.
- Status: An officer whose career is currently one bad report away from ending.

## Resources and Capabilities
- A small but genuine professional military force — regulars with halberds and studded leather, which is better equipped than anything Tenpug's Band can field.
- Templar authority, and the ability to legitimise Nibenese possession of the mine afterwards.
- Scouts who have already assessed the gith garrison.
- Sealed map case and command apparatus — she has proper intelligence products, which the PCs do not.
- The standing to make and keep an agreement on Nibenay's behalf.

## Relationships
- Existing actor or faction ID: `faction-shadow-brides`
  - Attitude: Member
  - Reason: Templar-wife of Nibenay.
- Existing actor or faction ID: `actor-zigath`
  - Attitude: Hostile (−5)
  - Reason: The gith commander holding the mine she was sent to take.
- Existing actor or faction ID: `actor-lady-vardan`
  - Attitude: Cordial (1)
  - Reason: Existing sandbox relationship.
- Existing actor or faction ID: `actor-brugg-stone-thumb`
  - Attitude: Cordial (1)
  - Reason: Existing sandbox relationship.
- Existing actor or faction ID: `actor-orruk-vesh`
  - Attitude: Neutral (0)
  - Reason: Existing sandbox relationship. Orruk is a wounded dwarf miner and survivor of the mine's fall — a witness to the thing she was sent to fix.
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: **Unformed — this is the negotiation**
  - Reason: A templar-wife of Nibenay and a community of escaped Nibenese slaves have every reason to kill each other and one very good reason not to.

## Knowledge
- Subject: The gith garrison's strength
  - Claim: Too strong for her unit alone. About twenty gith in the fort, including four sergeants and a lieutenant.
  - Source: Her own scouts.
  - Learned day: current campaign
  - Confidence: high
  - Truth status: true
  - Secret: no — she will share it as part of the deal
- Subject: The mine's origin and layout
  - Claim: Nibenay dug it and built the stockade; she has the plans.
  - Source: Her commission.
  - Learned day: on assignment
  - Confidence: certain
  - Truth status: true
  - Secret: no
- Subject: How the mine fell
  - Claim: The miners dug too deep and broke into a gith nest, and the gith came pouring out with metal weapons and clever tactics.
  - Source: Nibenese reporting and survivors.
  - Learned day: on assignment
  - Confidence: high
  - Truth status: true
  - Secret: **partially — this is precisely the information she is trying to keep from spreading**
- Subject: Tenpug's Band
  - Claim: Nothing yet, and she is working on it.
  - Source: —
  - Learned day: —
  - Confidence: —
  - Truth status: —
  - Secret: yes

## Current Activity
Camped near the stockade with a broken command, unable to advance or withdraw, watching an army of unknown origin approach and deciding whether it is a threat or a gift.

## GM-Only Secrets
- **The rumour is the trap.** If the PCs do not keep a lid on the scouts' report, a rumour starts in Tenpug's Band that the nearby force is slavers hunting slaves for Nibenay, and a growing sentiment builds that they should be confronted and exterminated. This is printed. The party's failure mode here is not a bad negotiation — it is not getting to a negotiation at all, because their own army destroyed the possibility while they were deciding.
- **She is negotiating with a community of escaped Nibenese slaves and does not appear to know it.** Every member of Tenpug's Band is, legally, Nibenese property. The alliance holds only as long as nobody says that out loud. The module never raises it. It should be raised.
- **Her news-control goal is a knife pointed at the PCs.** She needs the defeat and the gith steel kept quiet. The PCs are witnesses to both, plus an unregistered armed force of escaped slaves. Once the mine is retaken, her interests and theirs diverge sharply and immediately, and the module ends the adventure right before that lands.
- *(Proposed.)* She has not yet reported the mine's fall accurately. The sealed map case is a report she has written and not sent.

## Proposed Developments
- **Recommended:** play the alliance straight and let the reckoning wait. She keeps every promise she makes about the siege. The problem arrives afterwards, when Nibenay owns a working mine next door to a hidden community of its own escaped slaves.
- Give Tenpug's people a vote on the alliance. The band's founding trauma is Nibenese slavery; asking them to fight beside a templar-wife is a genuinely hard sell and a better scene than a handshake.
- The sealed map case is a lootable object with real content — the mine's plans, and possibly an unsent report.
- Long term: she is the campaign's natural route to a Nibenese claim on the Black Spine, and to the question of what a city-state does when it learns what is actually under that mountain.

## Stat Block or Rules Notes
- Class: Priest (templar)
- Level: 6
- Armor Class: 14 (studded leather and Dexterity)
- Hit Points: 30
- Movement: near
- Strength +1, Dexterity +2, Constitution +2, Intelligence +3, Wisdom +3, Charisma +3
- Alignment: Lawful (evil — templar of a sorcerer-king)
- Morale: 11
- Attacks: 1 attack per round.
  - *Bone command baton / mace* +4, 1d6+1
- **Templar Authority:** granted spellcasting from the Shadow King. Modest offensive and support magic; the campaign should keep the list short and unsettling rather than broad.
- **Command:** allies within near range who can hear her gain +1 to attack rolls and to morale. Her value is the unit, not the person.
- **Field Intelligence:** she has scouts, plans, and a sealed map case. Any question the party has about the fort, she can probably answer.
- **Supporting forces:** *Slave warriors* — 3rd-level fighters, hide and shield, morale 7, rising by two if freed. *Nibenay regulars* — 4th-level fighters, bone halberds, thick studded leather, morale 11.
- **Running her at the table:** she is not a villain in this adventure and should not be played as one. She is an officer in a hole, offering a fair deal she intends to honour, while quietly gathering information that will hurt the party later.
- **Conversion note:** the module gives Vakskra no personal stat block — only BATTLESYSTEM lines for her troops (Slave Warriors AD 8 / AR 7 / Hits 3 / ML 7; Nibenay Regulars AD 10 / AR 8 / Hits 3 / ML 11). Her own block is constructed from the templar-wife role.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Vakskra, a young Athasian templar-wife of Nibenay commanding a broken expedition, standing upright in a neutral token pose. Human woman in her late twenties, hard-featured and drawn with exhaustion, dark hair bound tightly back, dust-caked skin. Dust-darkened layered wraps over studded leather armor, a dark sash of office partly obscured by grime, wrapped forearms, worn boots. Carries a pale bone command baton in one hand and a leather map case sealed with black wax at the hip. Disciplined, guarded, proud bearing under visible strain. Restrained insignia, no ostentation, no heroic posing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One — Cry Vengeance
  - Section: "At the Gate" — The Forces of Nibenay; Negotiation; Combat; The Captured Mine
  - Printed page: 58–59, 60
  - Source type: official
  - Adaptation note: Stats converted to Shadowdark; her personal block is constructed. The negotiation terms, the slaver rumour, and the "too strong to attack, too shameful to retreat" bind are printed.
- Title: mk-sandbox `actors/vakskra.json` revision 5
  - Section: traits, goals, relationships, appearance
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: This nominee proposes an update. All three existing goals (`goal-vakskra-retake-mine`, `goal-vakskra-preserve-force`, `goal-vakskra-control-news`) are preserved above as Goals 1–3.
  - Id note: `faction-shadow-brides`, `actor-zigath`, `actor-lady-vardan`, `actor-brugg-stone-thumb`, `actor-orruk-vesh`, `actor-tenpug`, `location-nibenay-iron-mine-stockade`, `location-nibenay`, `location-black-spine-mountains`, `location-nibenay-iron-mine` all resolve to real sandbox records. `actor-askai` is proposed.

## Unresolved Questions
- **Does she learn what Tenpug's Band is?** The module never asks. The campaign should.
- What is in the sealed map case.
- What happens the day after the mine is retaken.
- Whether the band will even accept the alliance — this should be their decision, not the PCs'.
