---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: Mosak Eggstealer (update to existing actor-mosak-eggstealer, revision 4)

*(Revision of existing actor `actor-mosak-eggstealer`. **Clan Father of Kragmorta. He publicly doubted a god and was publicly forgiven, and he has not stopped doubting since — which is the party's way in.**)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/mosak-eggstealer.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-mosak-eggstealer |
| `name` | Mosak Eggstealer |
| `actorType` | named-npc |
| `status` | active |
| `role` | Clan Father of Kragmorta |
| `factionId` | faction-kragmorta-dray |
| `locationId` | location-kragmorta |
| `description` | A cautious planner who distrusts outsiders, wants news of the surface, and seeks help against the Spirit of Kragmorta. |
| `relationships` | `actor-spirit-of-kragmorta` -5 |
| `goals[]` | **End the threat posed by the Spirit of Kragmorta.** — priority 5, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Kragmorta (pp. 74-75) |
| `sourceStatBlock` | {"system": "AD&D 2e", "class": "Thief", "level": 11, "armorClass": 7, "movement": 15, "hitPoints": 46, "thaco": 15, "strength": 16, "dexterity": 16, "constitution": 14, "intelligence": 15, "wisdom": 13, "charisma": 13} |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
The Clan Father of the first generation dray, a planner rather than a talker, who leads three thousand exiles who still worship the god that threw them away — and who is the only one of them who looked at their miraculous guardian spirit and said *prove it*.

## Classification
- Subtype: named-npc — **first generation dray**
- Control: autonomous
- Status: active
- Faction or allegiance: **the first generation dray of Kragmorta**; **worships [[Dregoth]] and hates him**
- Current location: `location-kragmorta` — **area 5, the dray settlement**, among ancient buildings amid rivers of lava
- Current route, when traveling: —
- Role: **Clan Father** — *"Like the leaders before him, he carries the title of Clan Father (though there have been Clan Mothers in the past, too)."*

## Player-Safe Description

### Appearance
*(Not printed individually.)* A first generation dray: one of the **misshapen creatures with a variety of strange mutations** that resulted from Dregoth's first attempt to transform humans into dragonlike beings.

### Manner and Voice
**"Mosak is a planner. He is not known as a talker, but when he speaks his words are revered by the rest of his clan."**

Give him few words and total weight.

### Public Reputation
Absolute within Kragmorta. **He is the man who challenged the spirit in front of everyone and was forgiven** — which made him look brave and made the spirit look divine, in one stroke.

## Confirmed Facts
- **The current leader of Kragmorta's dray is Mosak Eggstealer.** **Like the leaders before him, he carries the title of Clan Father** — *"though there have been Clan Mothers in the past, too."*
- **Mosak is a planner. He is not known as a talker, but when he speaks his words are revered by the rest of his clan.**
- **He distrusts outsiders, fearing they may be from Dregoth.**
- **Neither he nor his dray know much about the surface world.**
- **If visitors can convince Mosak that they are friendly, he would love to hear tales of the world above.**
- **He also seeks help against the [[The Spirit of Kragmorta|Spirit of Kragmorta]].**
- **If adventurers confront the spirit and expose it for what it is (thus saving more of Mosak's clan), they will earn the respect and gratitude of the Clan Father.**
- **When the spirit first appeared, Mosak was suspicious and challenged it.** **Instead of striking him down like the crowd feared it would, the spirit forgave Mosak's doubt.**
- **He believes the wall-walkers come from the same place as the other terrors of Kragmorta** — *"the truth is the wall-walkers are native to Athas's subterranean regions."* **He is wrong about that one.**
- **If strangers get into a fight with one of Kragmorta's many creatures, the dray are not likely to get involved.** *"They are far more interested in seeing how strangers defend themselves than in providing help."* **Only if the group shows extreme bravery or skill early on and is then overcome will Mosak lead the clan to help them.**
- **To prove themselves, surface dwellers must pass the same coming of age tests that all the dray of Kragmorta undergo.** **Mosak calls for tough but fair tests suited to the talents of those participating in them.**
- **Failure to accept or complete a test is seen as a sign of weakness.** **To refuse or fail is to be marked as a child, and all first generation dray will treat such a character as a child forever after.** **Children are tolerated but ignored, not allowed to participate in adult discussions or trusted to handle matters of consequence.** **A character who fails is allowed one more try. After that, he can never be anything more than a child in Kragmorta.**
- **If the dray of Kragmorta are threatened, they cut the rope bridges** — woven from silk wall-walker webbing, which resists the heat of the lava — **to protect their homes from invaders.**
- **His people watch for signs of the second generation dray, for Dregoth's templars sometimes invade Kragmorta with hostile intentions.** **They do not hate their cousins, but they do not trust them either.**
- **The first generation dray still worship Dregoth as their god, but they also hate the Dread King for banishing them.** **They hope to one day prove their worthiness so they can return to live in the heaven that they believe New Giustenal to be.**
- **None of the first generation dray have ever seen a live human or demihuman.** **They haven't been subjected to the teachings of Dregoth's templars either, so they don't automatically feel hatred for surface dwellers.** **They respect all classes, but have an overwhelming distrust of templars — even the templars of other sorcerer-kings.**

## Goals
1. Description: Keep the clan alive in a cavern full of things Dregoth released to kill them.
   - Priority: 5
   - Progress: holding — *"an occasional hungry hell hound or wall-walker claims a dray for a meal now and then"*
   - Target: —
   - Deadline day: —
   - Secret: no
   - Status: active
2. Description: **Deal with the Spirit of Kragmorta.**
   - Priority: 5
   - Progress: **stalled — he doubted it once in public and cannot do so again**
   - Target: `actor-spirit-of-kragmorta`
   - Deadline day: none set
   - Secret: **partially — he is asking outsiders for help with it**
   - Status: active
3. Description: Prove the clan's worthiness and return to New Giustenal.
   - Priority: 4
   - Progress: **the goal of the entire exile community**
   - Secret: no
   - Status: active — **and it is exactly the lever the Spirit is pulling**

## Traits and Pressures
- Ambition: For the clan, not himself.
- Caution: **High and demonstrated.** He tested a miracle in front of a crowd.
- Secrecy: 3 — he wants help against the Spirit but cannot be seen wanting it.
- Loyalty: **To three thousand exiles**, and — painfully — **to the god who exiled them.**
- Cruelty: Not demonstrated. **He is the most reasonable leader in Chapter Six.**
- Risk tolerance: Moderate. **He watches strangers fight before deciding whether to save them.**
- Wealth: None to speak of. Kragmorta has lava and ruins.
- Status: Absolute.
- **The bind:** he worships Dregoth, hates Dregoth, wants to return to Dregoth, and distrusts anyone who might be from Dregoth. **Every direction he faces is the same person.**

## Resources and Capabilities
- **Command of the first generation dray of Kragmorta** — a whole city of exiles.
- **The rope bridges** over the lava flows, cuttable on his order, which is the city's entire defensive doctrine.
- **The coming of age tests**, which he sets personally and tailors to the participant.
- **Deep knowledge of Kragmorta's hazards** — the hell hounds, the fire snakes, the wall-walker hive, the dark naga, the escaped fire giant shaman **Bracorr**.
- **Hunting packs and tunnel guards**, who will find surface visitors before the visitors find anyone.

## Relationships
- Proposed actor ID: `actor-spirit-of-kragmorta`
  - Attitude: **Suspicious, publicly humbled, privately still unconvinced**
  - Reason: He challenged it and it forgave him. **He is right and he cannot say so.**
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **Worshipped and resented**
  - Reason: Dregoth created his people, called them a failure, and banished them. **They still pray to him.**
- Proposed actor ID: `actor-absalom`
  - Attitude: **Protected by, probably without knowing the full reason**
  - Reason: Absalom **secretly aids the first generation dray**, preaches to them, and is described as **defender of Kragmorta's dray.**
- Proposed actor ID: `actor-bracorr`
  - Attitude: **Stalemate**
  - Reason: A fire giant shaman from another world took over a building in Kragmorta and **has thus far refused to speak with Mosak and the first generation dray.**
- Existing actor or faction ID: `actor-mon-adderath`
  - Attitude: **Enemy at one remove**
  - Reason: *"Dregoth's templars sometimes invade Kragmorta with hostile intentions."* Those templars answer to the High Templar.

## Knowledge
- Subject: Kragmorta and everything in it
  - Claim: Every lava crossing, every lair, every predator.
  - Source: leadership
  - Confidence: high
  - Truth status: **mostly true — he is wrong about the wall-walkers**, believing they came from Dregoth's planar gate when they are native to Athas's underground.
  - Secret: no
- Subject: The surface world
  - Claim: **Almost nothing.** *"Neither he nor his dray know much about the surface world."* **None of them have ever seen a live human or demihuman**, and **none believe the surface can be reached without Dregoth's help.**
  - Truth status: —
  - Secret: no — **and he would love to be told.** This is the cheapest currency the party has.
- Subject: **That the Spirit is wrong**
  - Claim: Unproven instinct.
  - Source: he challenged it and something did not sit right
  - Confidence: **low, and correct**
  - Truth status: **true**
  - Secret: **yes — he is seeking outside help precisely because he cannot pursue it himself**

## Current Activity
Leading a city of exiles, humouring a spirit he does not trust, and watching the tunnels.

## GM-Only Secrets
- **He is the printed friendly contact in the most hostile place in the campaign, and the module hands the party three separate on-ramps:** he wants tales of the surface, he wants help with the Spirit, and he rewards anyone who exposes it. **Chapter Six is winnable through him.**
- **The forgiveness was the trap and he is the only one who half-felt it.** A spirit that struck him down would have been feared; a spirit that forgave him was *believed*. **Mosak has been living with that discomfort for a year.**
- **The tests are a superb roleplaying gate and they have teeth.** Fail twice and **a PC is permanently a child in Kragmorta** — tolerated, ignored, excluded from every adult discussion for the rest of the campaign. **That is a real, lasting social consequence with no combat attached, and it should be enforced.** They are *"tough but fair"* and **suited to the talents of the participant** — so build one per PC.
- **The clan will watch the party get mauled before helping.** Printed. *"They are far more interested in seeing how strangers defend themselves."* **Only extreme bravery or skill, followed by being overwhelmed, brings Mosak in.** The first fight in Kragmorta is an audition.
- **He is Absalom's protectorate and does not know why.** [[Absalom]] shields Kragmorta and preaches there, and is quietly working to reconcile the two dray generations. **Mosak has a patron in the enemy capital and no idea.**
- **The templar allergy is exploitable in both directions.** They distrust templars **of any sorcerer-king**. A party travelling with a templar — or a defector from Nibenay, Tyr or anywhere else — has a problem the module explicitly anticipates.
- *(Proposed.)* "Eggstealer" is a name with a story behind it that nobody has written. **First generation dray with strange mutations, in a cavern full of imported predators — something laid eggs, and he took them.**
- *(Proposed.)* If the Spirit is exposed and the clan turns, **Mosak still has three thousand people who worship Dregoth.** Proving the messenger false does not undo the religion. **He may need the party's help with the aftermath more than with the exposure.**

## Proposed Developments
- **Recommended: run the coming of age tests as the entry price to Chapter Six**, individually tailored, and honour the "permanent child" consequence for anyone who refuses.
- **Let him approach the party privately about the Spirit**, away from the clan. He cannot be seen doubting twice.
- Trade surface stories for goodwill. It costs the party nothing and it is the one thing he actually wants.
- Give "Eggstealer" an origin and let a dray tell it.
- **Plan the aftermath.** Exposing the Spirit saves the clan from a massacre and leaves three thousand people with no god and no plan.

## Stat Block or Rules Notes

**⚠ Correction against the sandbox.** An earlier draft of this nominee stated that no
stat block is printed and gave him a constructed **Fighter 7**. That was wrong:
`actor-mosak-eggstealer` revision 4 already carries a printed AD&D 2e block, and it makes
him a **Thief 11**. The converted block below now follows the record.

*(Printed AD&D 2e block, from the sandbox record: Thief; AC 7; MV 15; level 11; hp 46;
THAC0 15; Str 16, Dex 16, Con 14, Int 15, Wis 13, Cha 13.)*
- Ancestry: **Dray, first generation** — *misshapen, with a variety of strange mutations*
- Class: **Thief** *(printed — not Fighter)*
- Level: 8
- Armor Class: 13 (heat-cured hide)
- Hit Points: 46
- Movement: near *(printed MV 15 — fast for his bulk)*
- **Strength +2**, **Dexterity +2**, Constitution +1, Intelligence +1, Wisdom +0, Charisma +0
- Alignment: Neutral
- Morale: 12
- Attacks: 1 attack per round.
  - *Obsidian blade* +6, 1d8+2
- **Backstab:** as a thief of his tier. **A Clan Father who leads by ambush, not by charge** — which fits the printed temperament better than a warrior build did.
- **Clan Father:** the clan does what he says. **His word alone commits or withholds the dray of Kragmorta**, including cutting the rope bridges.
- **Heat-Adapted:** the first generation dray live beside rivers of magma. **Resistance to heat and fire damage**, and no penalty for operating near the lava flows that cost others 1d4 per round.
- **The Planner:** advantage on any check to prepare, ambush, fortify, or set terms in advance. **Disadvantage on anything requiring him to talk his way through something on the spot.**
- **Setting the Tests:** he tailors a coming of age test to each participant's talents. **Tough but fair. Two attempts, then permanent status as a child.**
- **Running him at the table:** three sentences maximum per scene, and the table should lean in for all three.
- **Conversion note:** a printed AD&D 2e block **does** exist and is recorded in the sandbox (`sourceStatBlock`, sourced to *City by the Silt Sea* Campaign Book, Kragmorta, pp. 74–75). Level compressed 11 → 8 for Shadowdark's cap; AC 7 → 13; hit points and the Thief class kept as printed. The narrative material above (Clan Father policies, the tests, the bridge-cutting) comes from the campaign book text and is unaffected by this correction.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Mosak Eggstealer, Clan Father of the first generation dray, standing upright in a neutral token pose. Powerfully built draconic humanoid, roughly seven feet tall, visibly asymmetrical and mutated — one shoulder heavier than the other, uneven horn growth along the brow, patches of thick dark-red scale alternating with rough grey hide. Blunt reptilian face with heavy jaw and small deep-set amber eyes, intelligent and steady. Wears layered heat-cured hide armour scorched and darkened by proximity to lava, reinforced with plates of black volcanic stone, and a heavy clasped cloak. Carries a large obsidian-bladed weapon resting point-down. Bearing is still, deliberate and unhurried — a leader who says little. Faint heat-glow lighting from below. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Six: Beneath Giustenal — Kragmorta; **The Spirit of Kragmorta**; Kragmorta Locations
  - Printed page: 74–77
  - Source type: official
  - Adaptation note: His title, temperament, distrust of outsiders, desire for surface tales, request for help against the Spirit, the challenge and forgiveness, the bridge-cutting doctrine, the wait-and-watch policy toward strangers in danger, and his mistaken belief about the wall-walkers are all printed.
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Six: Dregoth and the Dray — First Generation Dray
  - Printed page: 66–68
  - Source type: official
  - Adaptation note: Source of the coming of age tests and the permanent "child" consequence, the mixed worship-and-hatred of Dregoth, the distrust of all templars, and the fact that no first generation dray has ever seen a live human or demihuman.
  - Id note: `actor-dregoth`, `location-kragmorta` resolve to real sandbox/vault records. `actor-mosak-eggstealer`, `actor-spirit-of-kragmorta`, `actor-absalom`, `actor-mon-adderath`, `actor-bracorr` are proposed ids from this batch.

## Unresolved Questions
- **Where the name "Eggstealer" comes from.** Nothing is printed.
- What the clan does after the Spirit is exposed — they still worship Dregoth.
- Whether he ever learns Absalom has been protecting them.
- Whether he would accept help from a party travelling with a templar of any kind.
