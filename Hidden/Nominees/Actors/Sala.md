---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Sala (update to existing actor-sala, revision 3)

*(Update to existing actor `actor-sala`.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/sala.json` (revision 3, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-sala |
| `name` | Sala |
| `actorType` | named-npc |
| `status` | active |
| `role` | Halfling water priest among Tenpug's Band |
| `factionId` | faction-tenpugs-band |
| `locationId` | location-tenpugs-temple |
| `description` | Sala tends the wounded, blesses the community's water, and performs rites for those killed by the gith. His gentleness conceals a hard refusal to waste life or water. |
| `traits` | {"compassion": 5, "faith": 4, "calm": 4, "resolve": 4} |
| `resources` | {"waterRites": 4, "healingKnowledge": 4} |
| `relationships` | `actor-tenpug` +4, `actor-danya` +2, `actor-arcus` +3, `actor-roi` +2, `actor-lynth` +1 |
| `goals[]` | **Keep the wounded alive and protect the band's remaining clean water.** — priority 5, progress 0, status active |
| `goals[]` | **Complete the rites for those killed during the gith attack.** — priority 4, progress 0, status active |
| `sourceRefs[]` | DSE2 Black Spine — Cry Vengeance: Funeral Pyres (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
A halfling water-priest who heals everyone who comes to him without asking who they are — which on Athas is not kindness but an anomaly, and the band has never stopped being slightly unnerved by it.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-tenpugs-band` — founding member
- Current location: `location-tenpugs-temple` (the infirmary)
- Current route, when traveling: does not travel
- Role: Physician, water priest, keeper of the spring

## Player-Safe Description

### Appearance
A compact halfling in layered hide wraps, with permanently wet hands and a small water vessel worn at the belt. He wears simple ritual cords rather than ornament. Everything in the infirmary is scaled to him — a little bench, a small table, a slim shelf — which makes the room feel like a child's until you look at what is laid out on the linen.

Vials of strange fluids and salves. Rolls of white bandage. Needles and very thin thread. Small, extremely sharp cutting tools, arranged with care.

### Manner and Voice
Soft, unhurried, and genuinely funny. Sala disarms frightened people by talking about something else entirely until they realise he has already finished stitching them. He does not moralise and does not lecture, and he does not ask how the injury happened unless the answer changes the treatment.

On one subject only he becomes adamant and openly aggressive: the war. He will argue it hard, repeatedly, and without any of his usual gentleness.

### Public Reputation
Trusted absolutely and seen rarely — he keeps to the infirmary and is not often in the main hall. The band's stock phrase for him is that he heals minds as well as bodies, and they mean it fairly literally.

Outsiders who know what Athasian halflings usually are find him difficult to process.

## Confirmed Facts
- Halfling priest of water, 3rd level in the printed source.
- Treated Tenpug for the loss of his arm, and never stopped being amazed by the mul's drive to live and his constitution.
- Escaped with Tenpug when the band originally formed. A founding member.
- Skilled in herbs and potions; brews his own preparations for the band's use.
- Worked several years on his master's gladiators at the arena, and so has real combat medicine: stopping bleeding, stitching wounds, dressing, and preventing infection.
- Blesses the band's water and performs the rites for those the gith kill.
- Pregnant women, the wounded, and orphans stay in his infirmary during the day and sleep there at night.
- Opposes the war outright, and is one of the two principal debaters in the second meeting tent. Favours Jolon's plan — bribery, or flight.

## Goals
1. Description: Keep everyone in the band alive and whole.
   - Priority: 5
   - Progress: ongoing
   - Target: indefinite
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: Stop the war before it starts, by any argument that works.
   - Priority: 5
   - Progress: winning his tent, losing the camp
   - Target: 1
   - Deadline day: before the gith are battle-ready
   - Secret: no
   - Status: active
3. Description: Keep the spring clean and the water rites kept, because the band's entire existence rests on one basin.
   - Priority: 4
   - Progress: unbroken
   - Target: indefinite
   - Deadline day: none set
   - Secret: no
   - Status: active
4. Description: Never again watch people die in numbers he cannot treat.
   - Priority: 5
   - Progress: about to fail catastrophically
   - Target: —
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Ambition: None.
- Caution: Moderate (3).
- Secrecy: 2 — he keeps patients' confidences and nothing else.
- Loyalty: To people, individually, including people who have not earned it.
- Cruelty: None, in a setting that makes that genuinely strange.
- Risk tolerance: Low for others, unexamined for himself — he will walk into a battlefield to reach a wounded man and has not thought about what that means.
- Safety: Very poor. Strength 6, and he stands still while things happen around him.
- Wealth: None. The preparations are the band's.
- Status: Deeply respected, physically slight, and easy to overlook until you need him.

## Resources and Capabilities
- The only real medicine within a very long march: herbalism, surgery, combat medicine, and water-priest healing.
- Water rites — the blessing and keeping of the spring the entire community depends on.
- Funerary authority. He performs the rites for the dead, which after the first battle becomes the busiest office in the camp.
- Considerable moral leverage in council, spent almost entirely on opposing the war.

## Relationships
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: Old bond (4)
  - Reason: He kept Tenpug alive when Tenpug was a one-armed slave worth nothing to anyone. Neither of them mentions it.
- Existing actor or faction ID: `actor-arcus`
  - Attitude: Warm (3)
  - Reason: The largest and smallest members of the band. Arcus is exaggeratedly careful around him.
- Existing actor or faction ID: `actor-roi`
  - Attitude: Fond exasperation (2)
  - Reason: Roi will not accept treatment on the grounds that he is not worth the herbs. Sala treats him anyway.
- Existing actor or faction ID: `actor-danya`
  - Attitude: Cordial (2)
  - Reason: Legacy value from the older record.
- Existing actor or faction ID: `actor-lynth`
  - Attitude: Mild (1)
  - Reason: She keeps her distance. He has noticed, and has drawn no conclusion from it.
- Proposed actor ID: `actor-jolon`
  - Attitude: Allied
  - Reason: The two leading anti-war voices, arguing from completely different premises — Jolon from arithmetic, Sala from having seen what wounds look like.

## Knowledge
- Subject: Combat medicine
  - Claim: He can stop arterial bleeding, close a wound, and prevent infection under field conditions.
  - Source: Years working on his master's gladiators at the arena.
  - Learned day: before the band
  - Confidence: certain
  - Truth status: true
  - Secret: no
- Subject: The spring
  - Claim: It wells up from deep underground through what looks like a constructed pipe, and has never run dry even in the longest summers.
  - Source: Years of tending it.
  - Learned day: on arrival
  - Confidence: certain
  - Truth status: true — and see GM-Only Secrets
- Subject: What war does to a body
  - Claim: Specific, detailed, and the actual basis of his position in council.
  - Source: The arena.
  - Learned day: before the band
  - Confidence: certain
  - Truth status: true
  - Secret: no

## Current Activity
Working alone in the infirmary among his preparations, with three patients — one sun-blind, two wounded by gith on the road home from a job — and going out to the meeting tent each evening to lose the same argument again.

## GM-Only Secrets
- **He is going to lose, and then he is going to work.** After the first battle, ninety to a hundred survivors reach the temple and most are too wounded to fight again without prompt care. Sala is that care, alone, for two hundred people, in a smoke-filled hall with the doors being battered. This is his actual role in the module and it is worth playing at length rather than narrating past.
- **The spring is not natural.** He knows the water arrives through a worked pipe from somewhere deep below, and he has never once asked what it is connected to. The temple sits above catacombs; the catacombs connect downward; the Black Spine is hollow. He is the only person in the band positioned to notice, and his complete lack of curiosity about it is characterful and load-bearing.
- **He is an Athasian halfling who does not eat people.** The printed source calls him "truly an enigma on Athas" and leaves it there. Whether he is an exile, a foundling, or the last decent member of a tribe that was not, is unwritten and is a genuinely good hook.
- If the party is cruel to prisoners in front of him, he does not threaten them. He simply starts treating the prisoners, and lets that be the argument.

## Proposed Developments
- The siege infirmary is the strongest quiet scene in Adventure One. Give the players the choice of who he treats first.
- The spring-and-pipe thread connects the temple directly to the catacombs and thence to the whole underground arc. Sala is the natural person to mention it in passing three sessions before it matters.
- If Roi charges into the battle as written, Sala is the one who has to deal with the result, and their long silent friendship is the cost.
- Halfling origin question: worth a single scene, at most, and worth not answering.

## Stat Block or Rules Notes
- Class: Priest (water)
- Level: 4
- Armor Class: 12 (hide wraps and Dexterity)
- Hit Points: 20
- Movement: near (short — halfling)
- Strength −2, Dexterity +2, Constitution +1, Intelligence +2, Wisdom +3, Charisma +1
- Alignment: Lawful (good)
- Morale: 9 — he does not flee a place that has wounded in it
- Attacks: 1 attack per round.
  - *Small steel dagger* +1, 1d4 (Strength penalty applied; he is genuinely bad at this)
- **Water Rites:** can bless a water source, rendering it safe to drink and — in this setting — meaningfully valuable. Central to the band's survival.
- **Field Surgeon:** advantage on any check to stabilise the dying, close a wound, or prevent infection. Can restore a downed ally to consciousness without magic, once per patient per day.
- **Herbalist:** brews restorative preparations from desert flora over downtime. The band's entire medical stock is his work.
- **Priest spellcasting** (water sphere): cure wounds, purify, create water, sanctuary-type protections. Keep the list small — he is level 4 and the module's tension depends on him being insufficient.
- **Running him at the table:** he is the moral floor of the adventure. He argues against violence honestly and loses honestly, and then he does the work anyway without a word of reproach. Do not let him say *I told you so*. The character is far stronger if he never does.
- **Conversion note:** printed 2e stats are Halfling Priest of Water 3, Str 6, Wis 14, hp 13, AC 8, THAC0 20, small steel dagger 1d4 (−1 to hit). Scaled to Shadowdark level 4 so the siege infirmary is survivable to run.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Sala, an Athasian halfling water priest and physician, standing upright in a neutral token pose. Small compact halfling, three feet tall, weathered brown skin, close-cropped hair, calm gentle face with tired kind eyes. Layered hide wraps in muted earth colors, simple ritual cords at the shoulder instead of jewelry, a small stoppered water vessel at the belt, rolled bandages and a slim tool roll at the hip, hands damp. A very small plain steel dagger sheathed and clearly unused. Warm, unhurried, faintly amused expression. No armor, no ornament, no menace, no heroic posing — nothing of the feral Athasian halfling about him. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One
  - Section: Clash by Night — "Characters of the Slave Tribe"; "10. Infirmary"; "Area #9 Tent" debate
  - Printed page: 11 (stat block and background), 12 (war position), 19 (infirmary), 23 (debate)
  - Source type: official
  - Adaptation note: Stats converted to Shadowdark and raised from 3 to 4 for playability during the siege. The "enigma on Athas" line is printed and is preserved as an open question rather than resolved.
- Title: mk-sandbox `actors/sala.json`
  - Section: description, appearance, relationships
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: Existing record already has "tends the wounded, blesses the community's water, and performs rites for those killed by the gith… gentleness conceals a hard refusal to waste life or water." This nominee is written directly onto that.
  - Id note: `actor-tenpug`, `actor-arcus`, `actor-roi`, `actor-danya`, `actor-lynth` all resolve to real sandbox records. `actor-jolon` is a proposed id from this nominee batch.
