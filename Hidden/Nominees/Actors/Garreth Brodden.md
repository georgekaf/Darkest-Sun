---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: Garreth Brodden (update to existing actor-garreth-brodden, revision 3)

*(Update to existing actor `actor-garreth-brodden`.)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/garreth-brodden.json` (revision 3, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-garreth-brodden |
| `name` | Garreth Brodden |
| `actorType` | named-npc |
| `status` | active |
| `role` | House M'ke representative and Master Trader in Cromlin |
| `factionId` | faction-house-mke |
| `locationId` | location-cromlin |
| `description` | Garreth Brodden manages House M'ke's Cromlin pier and its lucrative silt-skimmer construction and maintenance business. He respects Hurdll Crost and avoids openly angering House Shom, while treating any discreet advantage he can secure as good business. |
| `traits` | {"caution": 4, "commercialCunning": 4, "diplomacy": 4, "loyalty": 3} |
| `needs` | {"profit": 4, "security": 4, "status": 3} |
| `resources` | {"skimmerContracts": 3, "slaveCrafters": 3, "tradeCredit": 3} |
| `relationships` | `actor-hurdll-crost` +2 |
| `goals[]` | **Keep House M'ke's Cromlin operation profitable without provoking Hurdll Crost or House Shom.** — priority 5, progress 0, status active |
| `goals[]` | **Win additional silt-skimmer construction and maintenance commissions.** — priority 4, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Cromlin Location 4: Pier of House M'ke (pp. 18) |
| `sourceRefs[]` | Darkest Sun sandbox adaptation — Goals, traits, and simulation values (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
House M'ke's man in Cromlin — publicly deferential to House Shom, privately doing whatever he can get away with, and running the only silt skimmer construction yard in the region on the backs of an extremely talented group of slaves.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-house-mke` — **representative and Master Trader in Cromlin**
- Current location: `location-pier-of-house-mke`, Cromlin (area 4)
- Current route, when traveling: —
- Role: House M'ke Master Trader; shipwright

## Player-Safe Description

### Appearance
A human trader in **leather**, with an **iron long sword** — metal, though a step below [[Hurdll Crost]]'s enchanted blade, and the difference says everything about the pecking order in Cromlin.

### Manner and Voice
*(Manner proposed; behaviour printed.)* Correct, careful, and never the first to speak. **Garreth respects Crost and the employees of House Shom, and he engages in no activity that would anger the village's controlling merchant house. At least not openly. What he gets away with in secret is simply seen as good business.**

### Public Reputation
The House M'ke representative — the second house in a one-house town, and visibly content to be.

## Confirmed Facts
- **Male human trader 5**, neutral. AC 8 (leather), hp 21, Int 16.
- Weapon: **iron long sword**, 1d8.
- **38 PSPs; wild talent Displacement** (PS 10, cost 6 + 3/round).
- **House M'ke representative and Master Trader in Cromlin.**
- **He respects Crost and the employees of House Shom, and engages in no activity that would anger the village's controlling merchant house. At least not openly. What he gets away with in secret is simply seen as good business.**
- **Though trade with House Shom is the most profitable side of the operation, the construction and maintenance of silt skimmers is a close second.**
- **Few of these vehicles are made each year, but the high price commanded for the commission of a single vessel earns lucrative profits for House M'ke.**
- **The skimmers are built by an extremely talented group of slave-crafters.** **Prices demanded for the work of these slaves depend on the size and options desired by the client.**
- Context: the **Silt Shoals** route between Cromlin and **Break Shore**, the House M'ke village on the far side, is known to **only a brave few navigators**, who **never make a map** of it.

## Goals
1. Description: Keep House M'ke profitable in a House Shom town.
   - Priority: 5
   - Progress: succeeding, quietly
   - Target: —
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: **Never openly anger House Shom.**
   - Priority: 5
   - Progress: unbroken
   - Target: indefinite
   - Deadline day: none set
   - Secret: no — **the "openly" is the secret**
   - Status: active
3. Description: Keep the skimmer yard's commissions coming.
   - Priority: 4
   - Progress: few vessels a year, very high margins
   - Target: —
   - Deadline day: none set
   - Secret: no
   - Status: active

## Traits and Pressures
- Ambition: Real, and expressed entirely through deniability.
- Caution: **High (4).** Everything he does is calibrated against Crost's tolerance.
- Secrecy: **4** — *what he gets away with in secret is simply seen as good business.*
- Loyalty: To House M'ke.
- Cruelty: **Institutional.** He owns the slave-crafters who build the skimmers.
- Risk tolerance: Low in public, moderate in private.
- Safety: Modest — 21 hit points, and **Displacement**, which is a good talent for a man who expects to be attacked once.
- Wealth: Considerable. Skimmer commissions are the most lucrative single line of business in Cromlin.
- Status: Second man in the village, and comfortable with it.

## Resources and Capabilities
- **The only silt skimmer construction and maintenance yard in the region**, staffed by **extremely talented slave-crafters.**
- House M'ke's trade network, including the **Break Shore** connection across the shoals.
- **Wild talent Displacement** — 38 PSPs.
- An iron long sword, in a village where most people carry bone.

## Relationships
- Existing actor or faction ID: `actor-hurdll-crost`
  - Attitude: **Deference, publicly**
  - Reason: Printed. He will do nothing to anger House Shom openly. **What he does otherwise is unstated and explicitly acknowledged to exist.**
- Existing actor or faction ID: `faction-house-mke`
  - Attitude: Representative
  - Reason: His house.
- Proposed actor ID: `actor-captain-gaff`
  - Attitude: Professional counterpart
  - Reason: House M'ke builds and maintains the skimmers; House Shom sails them.
- Proposed actor or faction ID: `location-break-shore` *(not yet in mk-sandbox)*
  - Attitude: The other end of the route
  - Reason: The House M'ke village across the Silt Shoals.

## Knowledge
- Subject: Silt skimmer construction
  - Claim: Complete — hulls, wheels, sails, options, and costs by size.
  - Source: He runs the yard.
  - Learned day: ongoing
  - Confidence: certain
  - Truth status: true
  - Secret: no — **and directly relevant, because [[Passk]] has a beached skimmer that needs repairing**
- Subject: **What he gets away with**
  - Claim: —
  - Source: —
  - Learned day: —
  - Confidence: —
  - Truth status: **the module states it exists and never says what it is. See GM-Only Secrets.**
  - Secret: yes
- Subject: House M'ke's affairs at Break Shore
  - Claim: Trade volumes, the shoals crossing, and who navigates it.
  - Source: His house.
  - Learned day: ongoing
  - Confidence: high
  - Truth status: true
  - Secret: partially

## Current Activity
Running a shipyard and a trading post, deferring correctly to House Shom in public.

## GM-Only Secrets
- **The module hands the GM a blank cheque and it is the best thing about him.** *What he gets away with in secret is simply seen as good business.* **There is no stated content.** Options, all consistent with what is printed: skimming House Shom's cargo manifests; running goods to Break Shore off the books; buying the Sky Singers' Giustenal salvage that Crost would confiscate; **or quietly financing the silt pirates who are bleeding his competitor's economy.**
- **That last one is the sharpest.** Crost has **committed himself to destroying the pirates** because they are *a serious drain on the village's economy* — a village where House Shom takes a tenth of everything and House M'ke takes nothing. **The pirates hurt Shom far more than M'ke.** Nothing in the source says Brodden is behind them. Nothing says he isn't.
- **He is the answer to Passk's skimmer.** [[Passk]] has a beached silt skimmer that **can be repaired**, and Brodden runs the only yard. **The party will need him, and he will want something.**
- **The slave-crafters are the region's most valuable skilled labour** and they are property. **An extremely talented group of slave-crafters** who can build a vessel worth a fortune is a liberation target, an extortion target, and a reason Brodden is careful.
- **Displacement on a 5th-level trader is a tell.** He has one talent and it is *don't be where the blade is.* He expects, at some point, to be attacked.
- *(Proposed.)* He has already been approached by the pirates, and turned them down, and kept the conversation.

## Proposed Developments
- **Recommended:** decide what he is getting away with before the party meets him, and let them find the edge of it.
- Route Passk's skimmer repair through him. It gives the party a reason to negotiate with a man who has a price for everything.
- If the campaign wants Cromlin's two-house tension to become a plot, the pirate-financing reading turns Chapter Two into a merchant war.
- The slave-crafters are a moral hook with real economic weight — freeing them destroys the only shipyard in the region.

## Stat Block or Rules Notes
- Class: Fighter (trader)
- Level: 4 *(Shadowdark scaling of 2e 5)*
- Armor Class: 12 (leather)
- Hit Points: 21
- Movement: near
- Strength +1, Dexterity +0, Constitution +1, Intelligence +3, Wisdom +2, Charisma +1
- Alignment: Neutral
- Morale: 9
- Attacks: 1 attack per round.
  - *Iron long sword* +5, 1d8+1
- **Wild talent — Displacement:** PS 10, cost 6 + 3/round, from 38 PSPs. **Attacks against him suffer disadvantage while maintained.**
- **Trader:** advantage on checks to appraise, negotiate, or price a commission.
- **Shipwright's Yard:** can build or repair a silt skimmer given time, materials and payment. **Prices scale with size and options.**
- **Running him at the table:** scrupulously polite, entirely correct, and never quite answering the question. He should be the most obviously guilty man in Cromlin, of something the players cannot name.
- **Conversion note:** printed 2e stats are Male Human Trader 5, N, AC 8 (leather), MV 12, hp 21, THAC0 16, iron long sword 1d8, PSPs 38, wild talent Displacement. Scaled to Shadowdark level 4.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Garreth Brodden, a House M'ke trader in a silt-coast village, standing upright in a neutral token pose. Human man in his forties, neat and composed, dark hair combed back, careful watchful face with a practised pleasant expression. Wears well-kept leather armor under a merchant's overrobe in House M'ke colors, more restrained than a rival house's finery, a silt-scarf loose at the throat, a belt of small pouches and a wax-sealed document tube. An iron long sword sheathed at the hip — plain, functional, and notably metal. Polite, guarded, faintly calculating bearing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two: Giustenal Environs — Cromlin; Cromlin Locations area 4 "Pier of House M'ke"; Garreth Brodden; Silt Skimmer Construction
  - Printed page: 15, 18–19, 21
  - Source type: official
  - Adaptation note: Stats scaled to Shadowdark. The deference to House Shom, the "at least not openly" clause, the skimmer yard and the slave-crafters are all printed.
- Title: mk-sandbox `actors/garreth-brodden.json`
  - Section: —
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: This nominee proposes an update.
`actor-garreth-brodden`, `actor-hurdll-crost`, `faction-house-mke` resolve to real sandbox/vault records. **Correction:** `location-pier-of-house-mke`, `location-break-shore` do **not** exist in mk-sandbox and are proposed ids, not existing records. `actor-captain-gaff` and `actor-passk` are proposed ids from this batch.

## Unresolved Questions
- **What is he getting away with?** The file exists to force this decision.
- Whether he has any connection to the silt pirates.
- What it would cost the party to get Passk's skimmer repaired.
