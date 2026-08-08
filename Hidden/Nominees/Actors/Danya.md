---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: Danya (update to existing actor-danya, revision 5)

*(Update to existing actor `actor-danya`. **Campaign-divergent — read the supersession notice before using anything from the printed module.**)*

## ⚠ Supersession notice

The printed *Black Spine* Danya is an elf thief of 3rd level, Keeper of Supplies for Tenpug's Band, aggressive and sarcastic, employer of Arcus, and a pro-war voice in the first meeting tent.

The campaign record (`actors/danya.json`, `canonStatus: campaign-original-with-source-name`, carrying a **GM-confirmed Day 104 history correction**) makes her something else entirely: an **agent of the Order and a very strong psionicist**, stationed at `location-kharanok`, watching the Black Spine Mountains.

Per `GUIDELINES.md` → *NPC background corrections*, the confirmed version wins outright. This file is written to the campaign version. The printed version is recorded below only as superseded material, so nobody re-imports it by accident.

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/danya.json` (revision 5, updated 2026-07-29). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-danya |
| `name` | Danya |
| `actorType` | named-npc |
| `status` | active |
| `role` | Agent of the Order watching over Kharanok and the Black Spine Mountains |
| `locationId` | location-kharanok |
| `description` | Danya is an agent of the Order and a very strong psionicist. She watches over Kharanok and the surrounding Black Spine Mountains. Her claims about Rajaat, the Gray, and the sorcerer-kings remain possible but unconfirmed. |
| `traits` | {"psionicStrength": "very strong"} |
| `goals[]` | **Watch over Kharanok and the surrounding Black Spine Mountains.** — priority 5, progress 0, status active |
| `sourceRefs[]` | DSE2 Black Spine — Cry Vengeance: Funeral Pyres (pp. ?) |
| `sourceRefs[]` | GM-confirmed Day 104 history correction — Danya's identity and operating area (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
An Order psionicist keeping watch on the Black Spine under a quartermaster's cover — sharp, severe, and telling anyone who will listen a story about Rajaat and the Gray that nobody has been able to confirm or dismiss.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: the Order (no faction record yet — see Unresolved Questions)
- Current location: `location-kharanok`
- Current route, when traveling: the Kharanok–Black Spine watch circuit
- Role: Observer for the Order; supply-factor as cover

## Player-Safe Description

### Appearance
A sharp-eyed elf woman with a severe, upright posture that reads as disapproval before she has said anything. She carries a supply satchel, a bone dagger, compact ledgers, and bundles tied off with knotted cord — the kit of a working quartermaster, maintained with more precision than a quartermaster needs.

She is watchful in a specific, trained way: she looks at doorways, hands, and the space behind people.

### Manner and Voice
Direct to the point of abrasion. Danya challenges anyone who makes a demand of her, and her wit is quick and edged. She does not perform warmth and does not apologise for its absence.

When the conversation turns to the sorcerer-kings, Rajaat, or the Gray, her register changes — she becomes precise, patient, and slightly evangelical, and she will keep talking well past the point where her audience has stopped believing her.

### Public Reputation
Known as a hard-nosed supply factor with an unusually long memory and unusually strange opinions. Respected for competence; not sought out for company.

## Confirmed Facts
- Elf. Agent of the Order. A very strong psionicist.
- Watches over Kharanok and the surrounding Black Spine Mountains.
- Makes claims about Rajaat, the Gray, and the sorcerer-kings. Those claims **remain possible but unconfirmed** — this is explicitly the campaign's position, not a hedge.
- Carries quartermaster's kit: satchel, ledgers, knotted-cord bundles, bone dagger.
- Subject of a GM-confirmed history correction on Day 104.

## Goals
1. Description: Watch the Black Spine and report what comes out of it.
   - Priority: 5
   - Progress: ongoing
   - Target: indefinite
   - Deadline day: none set
   - Secret: partially — the watching is visible, the reporting is not
   - Status: active
2. Description: Get someone with standing to take the Rajaat and the Gray material seriously.
   - Priority: 4
   - Progress: none — she is treated as a crank
   - Target: 1 credible listener
   - Deadline day: none set
   - Secret: no
   - Status: active
3. Description: Maintain the supply-factor cover well enough that nobody asks why an elf of her capability is counting sacks.
   - Priority: 4
   - Progress: holding
   - Target: indefinite
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Ambition: Moderate, and pointed entirely at being believed rather than at rank.
- Caution: High (4) operationally, low (2) conversationally — she says the dangerous thing out loud.
- Secrecy: 4 about her affiliation, 0 about her theories, which is an unstable combination.
- Loyalty: To the Order, and beneath that to the specific thing she thinks is coming.
- Cruelty: None, but she is careless with people's feelings and does not track the damage.
- Risk tolerance: High. She has stationed herself next to the Black Spine deliberately.
- Safety: Moderate. Her cover is good; her mouth is not.
- Wealth: Modest, and mostly other people's, held in trust.
- Status: Useful, tolerated, quietly dismissed.

## Resources and Capabilities
- Strong psionic capability — the strongest the party is likely to meet outside the gith command structure.
- Order contacts and whatever reporting channel that implies.
- Genuine logistical competence: she can source, price, and move goods, and her ledgers are real.
- Standing watch position with a long baseline of observation on the Black Spine.

## Relationships
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: Mutual wary respect
  - Reason: Legacy relationship value from the older record. Under the corrected history their connection needs re-grounding — see Unresolved Questions.
- Existing actor or faction ID: `actor-arcus`
  - Attitude: Attached (2)
  - Reason: The printed source made her his rescuer and employer. That chain is broken by the correction; the affection in the sandbox values survives it. See [[Arcus]].
- Existing actor or faction ID: `actor-raxxon`
  - Attitude: Cordial (2)
  - Reason: Legacy value from the existing record.
- Existing actor or faction ID: `actor-sala`, `actor-roi`, `actor-lynth`
  - Attitude: Low positive values carried in the older band-member records
  - Reason: These were written when she was a member of the band. They should be re-examined rather than deleted.

## Knowledge
- Subject: Rajaat, the Gray, and the sorcerer-kings
  - Claim: Substantial and specific. The campaign has deliberately left the content of the claim open.
  - Source: The Order, or her own work, or both.
  - Learned day: unknown
  - Confidence: hers, total
  - Truth status: **possible but unconfirmed** — campaign position, do not resolve without a GM ruling
  - Secret: no, and that is the problem
- Subject: Black Spine activity
  - Claim: She has a long observational baseline on what moves in and out of the mountains.
  - Source: Standing watch.
  - Learned day: ongoing
  - Confidence: high
  - Truth status: true
  - Secret: partially

## Current Activity
Working the Kharanok supply routes and keeping the Black Spine under observation, while trying to find anyone who will treat her conclusions as intelligence rather than eccentricity.

## GM-Only Secrets
- **The quartermaster cover is not a coincidence** — it is the proposed reconciliation between the printed Keeper of Supplies and the corrected Order agent. A supply factor has a legitimate reason to be everywhere, count everything, and remember it. If the GM wants the two versions to be one person, this is the seam, and it costs nothing to adopt.
- **She is the strongest psionicist the party can reach without going underground.** If the campaign needs the gith lord's dream assault answered by someone other than a PC, she is the answer already sitting on the board.
- Whether the Order knows what she reports, or whether she has been left in place and quietly ignored, is unwritten and is a good lever.
- Her theories being *correct* is more dangerous to her than her theories being wrong.

## Proposed Developments
- **Reconciliation ruling (recommended):** adopt the supply-factor cover, keep her Kharanok posting, and treat the printed "Keeper of Supplies for Tenpug's Band" as an earlier posting she has since left. This preserves every existing relationship value without contradicting the Day 104 correction.
- If instead the GM wants a clean break, the Keeper of Supplies post needs reassigning and Arcus needs a new rescuer — see [[Arcus]] and [[Tenpug]].
- The Rajaat/Gray material is a campaign-scale thread parked in a minor NPC. Promoting it is a decision, not an accident, and should be made deliberately.

## Stat Block or Rules Notes
- Class: Psionicist [UC]
- Level: 8
- Armor Class: 12 (travel leathers and Dexterity)
- Hit Points: 32
- Movement: near (double near — Athasian elf)
- Strength +0, Dexterity +2, Constitution +1, Intelligence +3, Wisdom +3, Charisma +1
- Alignment: Neutral
- Morale: 10
- Attacks: 1 attack per round.
  - *Bone dagger* +3, 1d4
  - *Mind thrust* +6, 2d6 psychic, near range, ignores armor
- **Contact / Probe:** can open a psionic contact on a target she can see. Wisdom check to resist.
- **Tower of Iron Will:** as a reaction, she or one ally within near range gains advantage against a psionic or mind-affecting effect.
- **Long Watch:** advantage on checks to recall detail from something she has observed, counted, or logged.
- **Sense the Way:** detects active psionic use within far range, and can usually name the discipline.
- **Running her at the table:** she is an information source who charges in patience. She will answer questions accurately and then keep talking about Rajaat until the players leave. Do not let her fight the party's battles; do let her be the reason a dream attack fails.
- **Conversion note:** the printed 2e Danya is a 3rd-level thief with hp 14. That stat block is **superseded** — it does not describe "a very strong psionicist." The block above is built to the campaign description instead.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Danya, an Athasian elf supply factor and hidden psionicist, standing upright in a neutral token pose. Tall lean elf woman, six and a half feet, long-limbed, weather-toughened face, severe upright posture, sharp watchful pale eyes, dark hair bound back tightly. Practical desert travelling clothes in muted dust colors under a worn leather coat, supply satchel across the body, compact bound ledgers at the belt, bundles tied with knotted cord, a plain bone dagger sheathed at the hip. Precise, disapproving, alert expression. No armor plate, no ornament, no visible magic or glow, no heroic posing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: mk-sandbox `actors/danya.json`
  - Section: description, appearance, role, location
  - Printed page: —
  - Source type: campaign record (read-only reference), `canonStatus: campaign-original-with-source-name`
  - Adaptation note: **Authoritative for this file.** Carries a GM-confirmed Day 104 history correction.
- Title: DSE2 Black Spine, Book One
  - Section: Clash by Night — "Characters of the Slave Tribe"; "Area #8 Tent" debate
  - Printed page: 8–9 (stat block and background), 22–23 (debate position)
  - Source type: official — **superseded**
  - Adaptation note: Printed material retained above only as a supersession record. Do not re-import the thief stat block, the Keeper of Supplies post, the Arcus employment, or the tent-8 debate role without an explicit GM ruling reversing the Day 104 correction.
  - Id note: `actor-tenpug`, `actor-arcus`, `actor-raxxon`, `actor-sala`, `actor-roi`, `actor-lynth`, `location-kharanok` all resolve to real sandbox records. The Order has **no faction record** in `factions/`.

## Unresolved Questions
- **Does the Order need a faction record?** She is described as its agent and there is no `faction-` id for it. This is a real gap.
- Whether to adopt the supply-factor reconciliation above, or to fully sever her from Tenpug's Band.
- What her Rajaat/Gray claim actually says. It has been referenced twice and never written down.
- Whether the legacy relationship values to the band members should be re-grounded or retired.
