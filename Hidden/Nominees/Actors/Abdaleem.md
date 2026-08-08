---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: Abdaleem (update to existing actor-abdaleem, revision 4)

*(Revision of existing actor `actor-abdaleem`. **The only friendly, competent, reachable spellcaster in the Giustenal environs — and the only person near the ruins the [[The Caller in Darkness|Caller]] cannot touch.**)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/abdaleem.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-abdaleem |
| `name` | Abdaleem |
| `actorType` | named-npc |
| `status` | active |
| `role` | Silt priest operating near Giustenal |
| `locationId` | location-abdaleems-island |
| `presenceStatus` | variable |
| `description` | An aloof silt cleric who travels beneath the silt, creates scroll-rocks, and opposes the krag of the Blasted Spire. |
| `resources` | {"scrollRocks": 10, "draxiaKnowledge": true} |
| `relationships` | `actor-krag-of-the-blasted-spire` -5 |
| `goals[]` | **Find capable allies to destroy the krag in the Blasted Spire.** — priority 5, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Abdaleem, Silt Priest (pp. 36-38) |
| `sourceStatBlock` | {"system": "AD&D 2e", "class": "Silt Priest", "level": 12, "armorClass": 7, "movement": 12, "hitPoints": 68, "thaco": 14, "strength": 15, "dexterity": 14, "constitution": 16, "intelligence": 15, "wisdom": 18, "charisma": 14} |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
A silt priest from Tyr who was driven out by Kalak's templars, was taken in by a cleric of the dusty sea, and now lives alone on an island north of the ruins serving the silt that killed everything he ever knew — while hoping one day it swallows Tyr whole.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: **the para-element of silt.** No house, no tribe, no city.
- Current location: `location-abdaleems-island` — an island **north of Giustenal's uncovered ruins**, reached by following the **eastern side of the Silt Road**
- Current route, when traveling: **beneath the silt**, for days at a time
- Role: Para-elemental priest of silt; supplier of the only gear that makes the Silt Sea survivable

## Player-Safe Description

### Appearance
**Male human**, described in the stat block as a silt priest in **studded leather**, carrying a **rod of flailing**. *(No physical description is printed.)*

### Manner and Voice
**Aloof and unconcerned** — and deliberately misleading about it. *"He may seem to take no interest in someone's pleas while he is actually figuring out how best to help them, and what he can get out of the deal for his patron element."*

Underneath: **bitter toward sorcerer-kings and most people in general.**

### Public Reputation
Little. He is a fixture of the region rather than a figure in it — **he never interferes with explorers of Giustenal**, so most people have no reason to think about him at all.

## Confirmed Facts
- **A para-elemental priest of silt named Abdaleem dwells on an island north of Giustenal's uncovered ruins.**
- **He claims that it is his task in life to serve the dusty sea that surrounds him.**
- **He never interferes with explorers of Giustenal** — **though he will challenge priests of rain or water if they make their allegiance known.**
- **He knows that this area of the Silt Sea could be destroyed by a powerful rain or water cleric, for the rocky basin beneath would hold water well.**
- **He spends much of his time travelling beneath the silt.** The rest goes on **creating his scroll-rocks** and on **avoiding the stalking presence of his prime nemesis, the krag from the Blasted Spire.**
- His island **can be reached by following the eastern side of the Silt Road.** **There is a 75% chance he is present**; otherwise he is below the surface and **won't return for 1d8 hours.**
- **Alignment: Chaotic Neutral.**
- **Origin:** *"Abdaleem was raised in Tyr and left shortly after being persecuted by Kalak's templars. He wandered the wastes for years before finally being taken in by a silt-cleric operating in the Giustenal area."*
- **His mentor disappeared some time ago**, but Abdaleem **was charged with helping the sea push its way forward.** **One day he hopes it will swallow Tyr and the entire Tablelands whole.**
- **He has no psionic abilities, so the [[The Caller in Darkness|Caller in Darkness]] has never bothered him.** **He knows a little about it, but nothing that will help characters defeat it.**

### What he can give a friendly party
- **draxia**, a local weed **hated by silt horrors**. Rubbed on the skin it acts as a repellent for **two hours**. It is **impossible to gather enough to repel a full-grown silt horror**, but **the spawn so common to Giustenal won't come within 10 feet of it.** **No effect on the silt spawn kraglings around the Blasted Spire.**
- **Scroll tablets** — *"like paper scrolls but using clay slabs instead."* Each contains **one modified spell of *free action* that allows the user to swim, breathe, and see in silt for three hours at a time.**
- **The price is fixed and non-negotiable: the head of the krag from the Blasted Spire.** *"Every foray into the submerged ruins is a cat-and-mouse chase through the eerily silent dust, and Abdaleem is afraid that one day his ability to turn the undead creature will fail."* **If someone brings him the head, he will give them as many scroll-rocks as they desire.** He **makes one every two days and keeps a standing supply of 10.**

## Goals
1. Description: Help the silt sea push its way forward.
   - Priority: 5
   - Progress: ongoing; it is the charge his vanished mentor left him
   - Target: **Tyr and the entire Tablelands, eventually**
   - Deadline day: none — he thinks in geological time
   - Secret: partially
   - Status: active
2. Description: Be rid of the krag from the Blasted Spire.
   - Priority: 5
   - Progress: **losing.** He is afraid his ability to turn it will fail one day.
   - Target: the krag's head
   - Deadline day: none set
   - Secret: no — **he will tell anyone who asks, because he needs it done**
   - Status: active
3. Description: *(Proposed.)* Find out what happened to his mentor.
   - Priority: 3
   - Progress: unstated
   - Secret: partially
   - Status: active

## Traits and Pressures
- Ambition: **Eschatological.** He wants a continent drowned in dust.
- Caution: High. He avoids the krag rather than fighting it, and he never picks fights with Giustenal's explorers.
- Secrecy: 2 — he is not hiding, he is just not interested.
- Loyalty: To the element, and to a mentor who is gone.
- Cruelty: Not demonstrated. **He is the least violent significant NPC in the region.**
- Risk tolerance: Moderate — he goes under the silt alone for days with a thing hunting him.
- Wealth: Irrelevant to him. **The scroll-rocks are worth far more than gold to the right party and he will not sell them for gold.**
- Status: A hermit with a monopoly.
- **Hard line:** **priests of rain or water.** He will challenge them on sight if they declare themselves. The reason is concrete, not doctrinal — **water would destroy this stretch of the Silt Sea, and the basin beneath would hold it.**

## Resources and Capabilities
- **Free movement beneath the Silt Sea** for days at a time — the single rarest capability in the region.
- **A standing stock of 10 scroll tablets**, replenished one every two days.
- **draxia**, and the knowledge of where it grows.
- **Turn undead** that currently, barely, holds off the krag.
- **Twelfth-level priest spellcasting** and a **rod of flailing**.
- **Immunity to the Caller** by simple absence of psionic talent — and therefore the ability to stand where nobody else can.

## Relationships
- Proposed actor ID: `actor-the-krag`
  - Attitude: **Hunted by**
  - Reason: *"His prime nemesis, the krag from the Blasted Spire."* Constant cat-and-mouse beneath the silt.
- Proposed actor ID: `actor-caller-in-darkness`
  - Attitude: **Beneath its notice**
  - Reason: **No psionic ability.** He lives five miles from it and has never been touched.
- Existing actor or faction ID: `actor-kalak`
  - Attitude: **Fled from; hated**
  - Reason: **Kalak's templars persecuted him out of Tyr.** He wants the sea to swallow the city.
- Proposed actor ID: `actor-abdaleems-mentor`
  - Attitude: **Missing**
  - Reason: The silt-cleric who took him in and **disappeared some time ago**, leaving him the charge.
- Existing actor or faction ID: `actor-eevuu-silt-stalker`
  - Attitude: *(Proposed.)* Neighbours
  - Reason: Both operate on the silt north of the ruins. The module does not connect them.

## Knowledge
- Subject: **Travelling and surviving beneath the silt**
  - Claim: Routes, depths, timings, and how to make clay tablets that grant free action in dust.
  - Source: A silt-cleric mentor plus years of practice.
  - Learned day: ongoing
  - Confidence: certain
  - Truth status: true
  - Secret: no — **but the tablets have a price**
- Subject: **The vulnerability of the Silt Sea itself**
  - Claim: *"This area of the Silt Sea could be destroyed by a powerful rain or water cleric, for the rocky basin beneath would hold water well."*
  - Source: his own study
  - Learned day: —
  - Confidence: high
  - Truth status: true
  - Secret: **yes, and it is the most dangerous thing he knows.** See GM-Only Secrets.
- Subject: The Caller in Darkness
  - Claim: A little.
  - Truth status: accurate as far as it goes
  - Secret: no — **and explicitly useless.** *"Nothing that will help characters defeat it."*
- Subject: **draxia**
  - Claim: Repels silt horror spawn within 10 feet for two hours; useless against adults and against kraglings.
  - Confidence: certain
  - Truth status: true
  - Secret: no

## Current Activity
Somewhere under the dust, making tablets and staying ahead of the krag. **75% chance he is home.**

## GM-Only Secrets
- **He is the region's quartermaster and the module hands the party a clean, priced quest to unlock him:** kill the krag, get unlimited *free action in silt*. **That is the key to the entire submerged half of Giustenal.** Nothing else in Chapter Three opens up as much.
- **The line about the basin is a campaign-ending weapon lying in the open.** He knows that **a powerful water or rain cleric could destroy this stretch of the Silt Sea**, and that **the rock beneath would hold the water.** He tells this to nobody, and he attacks water priests on sight. **A party with a water cleric turns the friendliest NPC in the region into an enemy by introducing themselves honestly** — and a party that grasps the implication is holding the means to flood Giustenal, drown New Giustenal, and end Dregoth without ever fighting him.
- **He is the anti-Caller control group.** A non-psionic man has lived beside the ruins for years, unharmed, and **knows something is there but nothing useful about it.** That is exactly the shape of evidence a clever party can reason from — the Caller's victim selection can be deduced from Abdaleem's continued existence.
- **The aloofness is a negotiating posture and the module says so.** *"He may seem to take no interest in someone's pleas while he is actually figuring out how best to help them, and what he can get out of the deal for his patron element."* **Play him as bored. He is not bored.**
- **His mentor vanished.** Given where they operated — silt north of Giustenal, in the era of the krag and the Caller — that is an unresolved death with three plausible causes and no printed answer.
- *(Proposed.)* He does not actually want Tyr drowned tomorrow. He wants it drowned eventually. **The difference matters if a PC offers to help.**

## Proposed Developments
- **Recommended: run the krag hunt as the gateway quest to the submerged ruins.** It is printed, priced, motivated and finite.
- Introduce him **before** the party has any water-priest exposure, so the later collision lands.
- Give the mentor's disappearance an answer and let the party find it. It is free goodwill and it is the only lever on him that isn't transactional.
- Decide whether the flood-the-basin idea is a real option in this campaign. **If it is, Abdaleem is the man who knows, and he must never be allowed to realise the party is thinking about it.**

## Stat Block or Rules Notes
*(Printed AD&D 2e block converted. Original: Male Human Silt Priest, CN; AC 7 studded leather; MV 12; Level 12; hp 68; THAC0 14; 1 attack, 1d6+1 rod of flailing; Spells 6/5/5/3/2/2; Str 15 Dex 14 Con 16 Int 15 Wis 18 Cha 14.)*

- Ancestry: Human
- Class: Priest (para-elemental — **silt**)
- Level: 9
- Armor Class: 13 (studded leather)
- Hit Points: 52
- Movement: near
- Strength +1, Dexterity +1, Constitution +2, Intelligence +1, **Wisdom +3**, Charisma +1
- Alignment: **Neutral** (printed Chaotic Neutral)
- Morale: 10
- Attacks: 1 attack per round.
  - *Rod of flailing* +7, 1d6+1
- **Silt-Walker:** he can swim, breathe and see in silt at will, and travels beneath it for days at a time. **This is his defining capability and it is unique in the region.**
- **Scroll Tablets:** clay slabs, each holding a modified *free action* — **swim, breathe and see in silt for three hours.** He carries **10**, makes **one every two days**, and **will not trade them for money.** The price is **the krag's head**.
- **draxia:** rubbed on skin, silt horror **spawn** will not approach within 10 feet, for **two hours**. **No effect on adult silt horrors or on the kraglings at the Blasted Spire.**
- **Turn Undead:** currently holds the krag at bay. **He is afraid it will fail.** A GM running the krag should make that fear load-bearing.
- **No psionics whatsoever** — and therefore **wholly immune to [[The Caller in Darkness]]**.
- **Hostile to water and rain priests** who declare themselves. Not negotiable, and he has a real reason.
- **Running him at the table:** distant, dry, faintly rude, and already calculating. He answers questions a beat late and always asks what's in it for the sea.
- **Conversion note:** full AD&D block printed and converted above. Level compressed 12 → 9 for Shadowdark's cap. Spell slots dropped in favour of Shadowdark's casting; treat him as a caster capable of high-tier priest magic, with silt-domain effects favoured.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Abdaleem, an Athasian human para-elemental priest of silt, standing upright in a neutral token pose. Lean, weathered human man in his forties, sun-darkened and dust-greyed skin, close-cropped hair and short beard both powdered pale with fine silt that never fully washes out, calm heavy-lidded eyes. Wears worn studded leather over dust-coloured robes in greys, bone-white and pale ochre, a long silt-scarf wound loosely at the throat, and a satchel of flat clay tablets at his hip. Holds a dark metal rod of flailing loosely at his side. Aloof, unhurried, faintly dismissive bearing. Fine dust clings to every fold of cloth. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Three: Outside Giustenal — **Abdaleem, Silt Priest**; Abdaleem (stat block)
  - Printed page: 36–37
  - Source type: official
  - Adaptation note: Location, the 75% presence chance and 1d8-hour absence, draxia and its exact limits, the scroll tablets and their terms, the krag rivalry, the Tyr backstory, the vanished mentor, the hostility to water/rain priests, the basin vulnerability, the absence of psionics and the resulting Caller immunity, and the full stat block are **all printed**. Everything marked *(Proposed)* is nominee-authored.
  - Id note: `actor-kalak`, `actor-eevuu-silt-stalker` resolve to real sandbox/vault records. `actor-abdaleem`, `actor-caller-in-darkness`, `actor-the-krag`, `actor-abdaleems-mentor`, `location-abdaleems-island` are proposed ids from this batch.

## Unresolved Questions
- What happened to his mentor.
- **Whether the "flood the basin" idea is live in this campaign** — and whether the party ever gets to realise he knows.
- Whether the krag can actually be killed by a party at this tier, or whether the hunt is meant to be a long arc.
- Whether he and the Silt Stalkers have any dealings.
