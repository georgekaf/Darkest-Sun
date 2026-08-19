---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Luubarra Fire Dagger (update to existing actor-luubarra-fire-dagger, revision 5)

*(Update to existing actor `actor-luubarra-fire-dagger`, currently at revision 4. **The scheme this record has been holding as printed-source potential since July is now live in the campaign.** Everything below the printed material is a change against the current values.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/luubarra-fire-dagger.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-luubarra-fire-dagger |
| `name` | Luubarra Fire Dagger |
| `actorType` | named-npc |
| `status` | active |
| `role` | Master defiler of the Silt Stalkers |
| `factionId` | faction-silt-stalkers |
| `presenceStatus` | unconfirmed |
| `description` | A power-seeking defiler secretly committed to bringing the Silt Stalkers into Dregoth's service. |
| `relationships` | `actor-eevuu-silt-stalker` +1, `actor-dregoth` +2 |
| `goals[]` | **Bring the Silt Stalkers to Giustenal and into Dregoth's service.** — priority 5, progress 1, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — The Silt Stalkers (pp. 14-15) |
| `sourceStatBlock` | {"system": "AD&D 2e", "class": "Defiler", "level": 10, "armorClass": 2, "movement": 18, "hitPoints": 24, "thaco": 17, "strength": 13, "dexterity": 19, "constitution": 10, "intelligence": 18, "wisdom": 11, "charisma": 18} |
| `simulation` | {"proposalMode": "triggered", "reason": "Luubarra's sourcebook scheme is retained as a goal, but no campaign event confirms her current location or activates the scheme."} |

## Proposed changes

*(New in revision 5. Everything else in this nominee is printed material and stands unchanged.)*

1. **`presenceStatus: unconfirmed` → confirmed.** `simulation.reason` currently reads *"no campaign event confirms her current location or activates the scheme."* **The scheme is activated.** She raided **Zharvek** on the **night of day 114** and is delivering slaves to Dregoth.
2. **Her raiding is now campaign fact, not printed potential.** Silt Stalkers under her emptied a settlement on the Black Spine road and took its people.
3. **Cromlin is her staging point.** Captives are held there, twenty miles west of Giustenal, and delivered onward. **Most of the Zharvek consignment is already delivered.** Two prisoners are still held.
4. **Goal 1's progress needs restating.** The record has *"Bring the Silt Stalkers to Giustenal and into Dregoth's service"* at progress 1 of 3 — one clan of three. **What she is doing at Zharvek is not that goal.** She is delivering non-elf slaves to a bargain that was about her tribe. See the question below; a second goal is proposed rather than inflating the first.
5. **Two of her victims are named:** `actor-talek-vos` and `actor-damak-of-zharvek`, both held at Cromlin.

## Campaign-confirmed activity

*(GM input, 13 August 2026, entered through MK-Sandbox #189. Nothing here is printed.)*

**She works for Zarron.** *(Ruled 13 August 2026, reconciling the two accounts of Zharvek's destruction.)* The Silt Stalkers under Luubarra operate **for `actor-zarron`**, leader of the pirates, and the two statements — *"Zharvek was destroyed by Zarron's pirates"* and *"the Day 114 raid was Luubarra's Silt Stalkers"* — are the same event described at two levels of the same chain. **Neither supersedes the other.** Propose `faction-silt-stalkers` gains a subordinate relationship to `faction-black-wake` / `actor-zarron`, and that this record gains `actor-zarron` as a relationship.

**What this does not settle:** the printed source has Luubarra **secretly** committed to Dregoth, trading her own tribe for the powers of a sorcerer-king. Whether Zarron knows he is supplying Dregoth, or believes he is running slave raids for his own account, is **not established and is not proposed here**. It is the difference between a pirate lord with an undead patron and a pirate lord being used as a delivery service.

- **Night of day 114** — Silt Stalker raiders under Luubarra empty **Zharvek**, a roadside settlement and animal market on the Black Spine caravan road, and take its people.
- **The captives are held at Cromlin** and delivered onward to **Dregoth** at Giustenal. **Most have already been delivered.**
- **Two are still held:** **Talek Vos**, a House Shom envoy who rode into the raid, and **Damak of Zharvek**, the dwarf who oversaw the settlement.
- **Gith were raiding Zharvek, and she used it.** The survivors reported gith because gith were genuinely attacking the settlement; **her people took the population under cover of that chaos**. Her involvement is invisible in the campaign's own record of the event, and it was invisible from inside the village too.

## One-Sentence Summary
The Silt Stalkers' master defiler, who went to Giustenal, met Dregoth, cut a deal for the powers of a sorcerer-king, has already fed one of her own clans to him as undead, is working on the rest of the tribe — and is emptying settlements on the Black Spine road in the meantime.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: Silt Stalkers elf tribe — **master defiler**; secretly serving Dregoth
- Presence: **confirmed active in the campaign** as of day 114
- Current location: with the Silt Stalkers, eastern Tyr region; **operating between the Black Spine road, Cromlin and Giustenal**
- Current route, when traveling: the Silt Stalker raiding range
- Role: Chief defiler; Dregoth's agent inside the tribe

## Player-Safe Description

### Appearance
A female elf defiler with **bracers of defence AC 6** and a **quarterstaff +2**. Dexterity 19, Intelligence 18, **Charisma 18** — she is the most personally magnetic figure in the environs and uses it.

### Manner and Voice
*(Manner proposed; behaviour printed.)* Prophetic, seductive and relentless. **She keeps Eevuu Silt Stalker occupied with her prophecies of power, glory and untold riches**, and **to make these omens come true she insists that the tribe engage in even more bloodshed than usual.**

### Public Reputation
The tribe's chief defiler and prophet. **Eevuu has been listening to Luubarra's urgings**, and **his dreams are full of great raids to come — provided he follows the advice of his chief defiler.**

## Confirmed Facts
- **Female elf defiler 10**, chaotic evil. AC 2 (bracers AC 6, Dex), hp 24, Dex 19, Int 18, Cha 18.
- Weapon: **quarterstaff +2**. Spells: **4/4/3/2/2** — to 5th level.
- **55 PSPs. Wild talent: Aging** (PS 3, cost 15) — **"among her many secrets," a talent she employs with malice when the need and opportunity arise.**
- **She is the Silt Stalkers' master defiler.**
- The Silt Stalkers consist of three clans: **Fire Bow, Fire Dagger, and Fire Sword.**
- **The Fire Dagger clan has disappeared recently, after being sent to explore the ruins of Giustenal by Luubarra.** This **has caused Eevuu some concern**, but she keeps him distracted.
- **Luubarra started making her dark predictions after her own visit to Giustenal.**
- **She met Dregoth, and the two made a deal that requires the whole Silt Stalker tribe to travel to the city by the Silt Sea.**
- **Dregoth, quick to add more followers to his growing army, promised Luubarra the powers of a sorcerer-king.**
- **He has no intention of honouring that promise, but he will take all the elves she sends him.**
- **The Fire Dagger clan has already been assimilated into Dregoth's fold. They now serve him as undead warriors.**
- **She enjoys power**, always seeks to increase her personal power, and **desires to always be near those of power greater than her own.**
- **She has a thirst for blood and violence, and she likes to test her defiling arts on those her tribe captures.**
- **Since meeting Dregoth, her desire for murder and mayhem has increased dramatically.** *"The road to power," Dregoth told her, "is paved with the blood of innocents."*
- **She has dedicated her life and tribe to Dregoth's unholy plans.**
- **She is currently working to convince Eevuu that the rest of the Silt Stalkers should join the Fire Daggers. If he continues to refuse, Luubarra will take matters into her own hands.**

## Goals
1. Description: Deliver the whole Silt Stalker tribe to Dregoth.
   - Priority: 5
   - Progress: **one clan of three already delivered and raised as undead**
   - Target: 3 clans
   - Deadline day: none set
   - Secret: **yes — the tribe believes it is following prophecy**
   - Status: active
2. Description: Receive the powers of a sorcerer-king.
   - Priority: 5
   - Progress: promised
   - Target: —
   - Deadline day: none set
   - Secret: yes
   - Status: **active, and doomed — see GM-Only Secrets**
3. Description: Remove Eevuu if he keeps refusing.
   - Priority: 4
   - Progress: contingency
   - Target: 1
   - Deadline day: none set
   - Secret: **yes**
   - Status: active

## Traits and Pressures
- Ambition: **Total.** It is the whole character — *she always seeks to increase her personal power.*
- Caution: Moderate. She works through prophecy and persuasion rather than force, until she doesn't.
- Secrecy: 5 — **the tribe does not know she has sold them.**
- Loyalty: To power, and to whoever currently has more of it than she does.
- Cruelty: **High and recreational.** She tests her defiling arts on captives for practice.
- Risk tolerance: High.
- Safety: Good — AC 2 and a tribe around her.
- Wealth: Tribal.
- Status: Chief defiler; **effectively the tribe's true ruler through Eevuu.**

## Resources and Capabilities
- **Defiler spellcasting to 5th level.**
- **Wild talent: Aging** — a secret, and used with malice.
- **Prophetic authority over an entire raiding tribe**, and through it over Eevuu's decisions.
- **A direct line to Dregoth**, and his active backing.
- **The Fire Dagger clan, now undead**, which she delivered.

## Relationships
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **Patron, and the greater power she wants to stand near**
  - Reason: They made a deal. **He promised her the powers of a sorcerer-king and has no intention of honouring it.**
- Existing actor or faction ID: `actor-eevuu-silt-stalker`
  - Attitude: **Handler, and obstacle**
  - Reason: She keeps him occupied with prophecy. **If he continues to refuse, she will take matters into her own hands.**
- Proposed faction ID: `faction-fire-dagger-clan` *(not in mk-sandbox; the vault has a Fire Dagger Clan page — confirm the id before submission)*
  - Attitude: **Sold**
  - Reason: Her own clan by name. She sent them into Giustenal and they now serve Dregoth as undead warriors.

## Knowledge
- Subject: **Dregoth is alive, in Giustenal, and building an army**
  - Claim: She has met him personally and made a deal with him.
  - Source: Direct.
  - Learned day: her visit to Giustenal
  - Confidence: certain
  - Truth status: **true — and she is one of very few surface Athasians who knows it**
  - Secret: **absolutely**
- Subject: What happened to the Fire Dagger clan
  - Claim: They were assimilated. They serve Dregoth as undead.
  - Source: She arranged it.
  - Learned day: —
  - Confidence: certain
  - Truth status: true
  - Secret: **yes — Eevuu has "some concern" and no idea**
- Subject: A route into Giustenal
  - Claim: She went and came back.
  - Source: Direct.
  - Learned day: —
  - Confidence: certain
  - Truth status: true
  - Secret: yes

## Current Activity
Prophesying glory to a chief whose tribe she has already sold, and preparing to kill him if he keeps hesitating.

## GM-Only Secrets
- **She is the campaign's earliest hard evidence that Dregoth is alive**, and she is walking around the environs where a party can meet her. **Everyone else in Chapter Two deals in rumour about the Caller. Luubarra has shaken hands with the actual antagonist.**
- **Dregoth is going to betray her and the module says so flatly:** *he has no intention of honouring that promise, but he will take all the elves she sends him.* **She is not a villain with a plan; she is a supplier being harvested.** If the party ever tells her — or she works it out — **she has a tribe, 5th-level defiling, and nothing to lose.**
- **The Fire Dagger clan is a whole clan of elves now serving as undead warriors**, and the vault already has a Fire Dagger Clan record. **That is a specific, named, findable atrocity the party can uncover in Giustenal**, and it is the proof that would turn Eevuu against her instantly.
- **Her removal of Eevuu is pending and triggerable.** *If he continues to refuse, Luubarra will take matters into her own hands.* **A party that stiffens Eevuu's resolve causes an assassination.** A party that does nothing watches the tribe walk into the ruins.
- **The Aging wild talent is a hidden weapon.** PS 3, cost 15 — expensive, rarely used, and devastating. **The module calls it one of her many secrets.** Save it for one scene.
- *(Proposed.)* She knows the deal is bad. She took it anyway, because Dregoth is the greatest power she has ever stood near, and that is the actual thing she wants.

## Proposed Developments
- **Recommended:** let the party find the Fire Daggers first, as undead, in the ruins — and only then work out who sent them.
- The Eevuu confrontation is the payoff. Whether the party arms him with the truth, and whether he survives using it, is a genuine choice with a body count.
- If Luubarra learns Dregoth intends to discard her, she is the most useful possible ally against him and the most dangerous.
- She is the module's only pre-established route to a meeting with Dregoth that does not involve walking into Giustenal blind.

## Stat Block or Rules Notes
- Class: Wizard (defiler)
- Level: 8 *(Shadowdark scaling of 2e 10)*
- Armor Class: 17 (bracers of defence and Dexterity)
- Hit Points: 24
- Movement: near (double near — Athasian elf)
- Strength +1, Dexterity **+4**, Constitution +0, Intelligence **+4**, Wisdom +0, Charisma **+4**
- Alignment: Chaotic (evil)
- Morale: 12
- Attacks: 1 attack per round.
  - *Quarterstaff +2* +6, 1d6+2
- **Defiler spells to 5th level:** 4/4/3/2/2. Defiling drains the life from surrounding vegetation — **in the deep desert this is often no cost at all, and near an oasis or a settlement it is an atrocity in public.**
- **Wild talent — Aging (secret):** PS 3, cost 15 of 55 PSPs. Roughly twice per day. **She does not use this where witnesses survive.**
- **Prophet:** advantage on any check to persuade, mislead or steer the Silt Stalkers, and on convincing Eevuu specifically.
- **Elf Sprint:** double near movement.
- **Running her at the table:** charming, certain, and visibly enjoying herself. She should read as the most dangerous person in Chapter Two, because she is — and the players should not learn what she has already done until they find the Fire Daggers.
- **Conversion note:** printed 2e stats are Female Elf Defiler 10, CE, AC 2 (bracers AC 6, Dex), MV 18, hp 24, THAC0 17 (staff 15), quarterstaff +2 1d6+2, PSPs 55, wild talent Aging (PS 3, cost 15), spells 4/4/3/2/2. Scaled to Shadowdark level 8.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Luubarra Fire Dagger, an Athasian elf defiler, standing upright in a neutral token pose. Tall lean elf woman, six and a half feet, long-limbed and striking, sharp weather-etched features, intense confident eyes, dark hair worn long with bone and metal ornaments. Wears layered raider's finery in deep reds and blacks over travelling leathers — better dressed than her tribe, deliberately — with plain leather bracers on both forearms. Holds a carved quarterstaff upright in one hand. Faint traces of ash and withered plant matter clinging to the hem of her robes. Magnetic, imperious, openly hungry bearing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two: Giustenal Environs — The Silt Stalkers; Luubarra Fire Dagger
  - Printed page: 14
  - Source type: official
  - Adaptation note: Stats scaled to Shadowdark. The Dregoth deal, the broken promise, the Fire Dagger clan's fate, the plan for Eevuu and the secret Aging talent are all printed. The Silt Stalkers are detailed further in DSS3 *Elves of Athas*.
- Title: campaign owner ruling, 2026-08-13
  - Section: the Zharvek raid of day 114 Night, the Cromlin holding point, and the delivery of its people to Dregoth
  - Printed page: —
  - Source type: GM input
  - Adaptation note: Entered through MK-Sandbox #189. No confirmed event record is claimed here.
- Title: `actors/luubarra-fire-dagger.json`
  - Section: —
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: This nominee proposes an update. Existing record already frames her as "servant of Dregoth, corrupting the Silt Stalker tribe."
  - Id note: `actor-dregoth`, `actor-eevuu-silt-stalker`, `actor-luubarra-fire-dagger` resolve to real sandbox records. `faction-fire-dagger-clan` — the vault has a Fire Dagger Clan page; confirm the sandbox faction id before submission.
