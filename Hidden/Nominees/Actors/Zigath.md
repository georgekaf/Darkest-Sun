---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Zigath (update to existing actor-zigath, revision 4)

*(Update to existing actor `actor-zigath`. **Appearance conflict — see the notice below.**)*

## ⚠ Appearance conflict

The printed module: *"Zigath is a rare sight: a pudgy gith. She prefers gaudy clothes and armor."*

The campaign record (`actors/zigath.json`): *"A tall, scarred gith elder wrapped in ash-stained hides, with obsidian prayer shards and a dark-metal spear held like a ritual standard."*

These are incompatible. The sandbox record's own `sourceScope` resolves it: **`official` covers only her name, gith identity, psionic and fire-priest role, and Zigath's Nest** — `projectDescription` explicitly covers *"expanded appearance."* The campaign appearance therefore **wins**, and this file uses it. The printed description is recorded here only so it is not reintroduced by accident.

*(Worth noting what is lost: "a rare sight — a pudgy gith" tells you she has been eating well off the mine's profits while her warriors have not. If the campaign wants that characterisation without the appearance, it survives fine as behaviour.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/zigath.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-zigath |
| `name` | Zigath |
| `actorType` | named-npc |
| `status` | active |
| `role` | Ancient female gith psionicist and fire cleric |
| `factionId` | faction-black-spine-gith |
| `locationId` | location-zigaths-nest |
| `description` | An ancient female gith whose command of the Way and devotion to elemental fire have made her the spiritual center of the force holding the iron mine. Zigath views the captured metal as the foundation of a stronger gith dominion. |
| `traits` | {"intelligence": 5, "will": 5, "zeal": 5, "patience": 4, "cruelty": 4} |
| `resources` | {"githWarband": 4, "psionicAuthority": 5, "fireCultInfluence": 4} |
| `relationships` | `actor-vakskra` -5, `actor-orruk-vesh` -4, `actor-queen-trinth` +1 |
| `goals[]` | **Hold the iron mine against Nibenay's counterattack.** — priority 5, progress 0, status active |
| `goals[]` | **Move iron and captured weapons to strengthen Yathazor.** — priority 5, progress 0, status active |
| `goals[]` | **Interpret the fire omens that drew her to the mine.** — priority 4, progress 0, status active |
| `sourceRefs[]` | Darkest Sun project planning — Black Spine gith force, Yathazor, and the captured iron mine (pp. ?) |
| `sourceRefs[]` | DSE2 Black Spine — Into the Mines: Zigath's Nest (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
The fire-priest psionicist who owns this nest, has profited handsomely from it, and deeply resents the celebrated warrior who arrived and took her troops' admiration without taking any of the work.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-black-spine-gith`
- Current location: `location-zigaths-nest` — her roost, the balcony overlooking the Great Hall
- Current route, when traveling: can pass the stone seal by dimensional door and travel through Yathazor to the main nest
- Role: Master of Zigath's Nest; psionicist and fire cleric

## Player-Safe Description

### Appearance
A tall, scarred gith elder wrapped in ash-stained hides, hung with obsidian prayer shards, carrying a dark-metal spear held like a ritual standard.

Her weapons are **obsidian rather than steel** — she is a fire cleric, and the module is explicit that this is why. In a nest whose entire strategic value is metal, the commander carries stone on principle.

Her roost is a natural balcony over the Great Hall, with a long wooden table of pottery jars, skins and bottles: her experiments.

### Manner and Voice
Devotional and proprietary in equal measure. Zigath speaks about the fire omens that drew her here with genuine reverence, and about the mine's output with the tone of an owner. She does not distinguish between the two.

She mistrusts her own people. The stairs to her balcony are trapped with a glyph only she and her most trusted servants can pass, and gith warriors will not climb them.

### Public Reputation
She runs the nest. That is the whole of her standing, and it is enough — until Haza arrived.

## Confirmed Facts
- **Female gith, 10th-level psionicist / 10th-level fire cleric**, chaotic evil.
- **She runs this nest and has profited well from its mining operations.**
- **She resents the presence of Haza, who has upstaged her in the eyes of the troops.**
- Her weapons are obsidian instead of steel *because she is a fire cleric*: an obsidian dagger +3, an obsidian-tipped javelin +2, plate mail, and a ring of protection +1.
- 132 PSPs. Telepathy, psychokinesis, psychoportation and clairsentience — including **detonate, disintegrate, teleport, dimensional door**, molecular agitation and time shift. All defence modes.
- Cleric spells to 5th level, including **flame strike**, **wall of fire**, **produce fire** ×3, **glyph of warding** and dispel magic ×2.
- With Haza, she is one of the two brains behind the gith forces; the two of them plus Toogo rotate shifts so one is always on duty and only one asleep.
- **She developed the fire pebbles** — a magical weapon made using knowledge given to her by githyanki who contacted the gith deeper in the mountain. The unprepared ingredients for sixteen pounds of them are on her table.
- On the fourth round after an alarm, she drags three bound Nibenay slaves to the edge of her balcony **to deter intruders from using area-affecting attacks**, and casts from behind them.
- Several glyphs of warding protect the Great Hall and her stairs; the stair glyph fires flame strike on anyone who crosses without the password, **which few gith know — so her own warriors will not come up to help her**.
- **If the battle seems lost she does not die for it.** She uses dimensional door to move past the stone seal, then travels through Yathazor back to the main gith nest.
- If captured, she might reveal that gith deeper in the mountain have made contact with **a race of powerful magicians** who are going to help the gith reclaim what is "rightfully theirs" — all of Athas.
- **She has never been to Yathazor**, but she has heard about the Square of Gurdek.

## Goals
1. Description: Hold the iron mine against Nibenay's counterattack.
   - Priority: 5
   - Progress: **already failed above ground and she may not know it**
   - Target: 6
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: Move iron and captured weapons to strengthen Yathazor.
   - Priority: 5
   - Progress: ongoing
   - Target: 5
   - Deadline day: none set
   - Secret: yes
   - Status: active
3. Description: Interpret the fire omens that drew her to the mine.
   - Priority: 4
   - Progress: ongoing
   - Target: 4
   - Deadline day: none set
   - Secret: yes
   - Status: active
4. Description: Keep what she has built — the nest, the profits, and the standing Haza is eroding.
   - Priority: 4
   - Progress: losing ground
   - Target: —
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Intelligence: 5 · Will: 5 · Zeal: 5 · Patience: 4 · Cruelty: 4 *(existing sandbox trait values, retained)*
- Ambition: High, and territorial rather than expansionist.
- Caution: Very high (5) — glyphs, hostages, an escape route, and a balcony nobody can climb.
- Secrecy: 5. Even her own warriors do not know her password.
- Loyalty: To the gith cause, and beneath that to her own position.
- Risk tolerance: Low personally. She fights from height, behind hostages, with an exit prepared.
- Safety: Excellent, and entirely by design.
- Wealth: Considerable — the mine's profits, plus a stone chest of gems and ceramic pieces.
- Status: Owner of the nest; being quietly displaced in her own hall.

## Resources and Capabilities
- The most versatile individual capability in the first three adventures: two full casting suites plus teleportation.
- **Fire pebbles**, and the knowledge to make more — a githyanki-derived magical explosive that also detects invisible intruders by sound underfoot.
- Command, jointly with Haza, of 62 warriors and two sergeants.
- Three Nibenay slaves as human shields, deployed on a timer.
- **Dimensional door** — a guaranteed personal escape past her own stone seal.
- A stone chest, glyph-trapped, holding two red spinels, an amethyst, three bloodstones, a hematite and 81 ceramic pieces; plus raw experimental materials worth 100 cp.

## Relationships
- Existing actor or faction ID: `actor-vakskra`
  - Attitude: Hostile (−5)
  - Reason: The templar-wife sent to take her mine.
- Existing actor or faction ID: `actor-orruk-vesh`
  - Attitude: Hostile (−4)
  - Reason: Existing sandbox relationship — a surviving witness to the mine's fall.
- Existing actor or faction ID: `actor-queen-trinth`
  - Attitude: Faintly positive (1)
  - Reason: Existing sandbox relationship. Zigath knows only that powerful magicians have contacted the gith; she does not know who Trinth is.
- Proposed actor ID: `actor-haza`
  - Attitude: **Resentment**
  - Reason: Printed. He has upstaged her with her own troops. The single most exploitable relationship in Adventure Three.
- Proposed actor ID: `actor-toogo`
  - Attitude: Dismissive
  - Reason: Haza's companion, and not a tactician. She rotates shifts with him and thinks little of him.
- Proposed actor ID: `actor-slate`
  - Attitude: Knows of, never met
  - Reason: She has heard about the Square of Gurdek and has never been to Yathazor.

## Knowledge
- Subject: The powerful magicians
  - Claim: Gith deeper in the mountain have made contact with a race of powerful magicians who will help the gith reclaim all of Athas.
  - Source: Report from the main nest.
  - Learned day: current campaign
  - Confidence: high
  - Truth status: **true — they are githyanki, and she does not have that word**
  - Secret: yes — but she *might* reveal it if captured, which makes her the campaign's best available informant at this stage
- Subject: Fire pebble manufacture
  - Claim: She can make them; she was taught by the githyanki contact.
  - Source: Direct instruction.
  - Learned day: recent
  - Confidence: certain
  - Truth status: true
  - Secret: yes
- Subject: The cave-in and the new tunnel
  - Claim: A collapse about 50 days ago cut her nest off from the main gith nest; miners dug a new tunnel and found Yathazor, and Slate helped them excavate a path through.
  - Source: Her own operation.
  - Learned day: ~50 days ago
  - Confidence: certain
  - Truth status: true
  - Secret: yes

## Current Activity
Running a mining colony, interpreting fire omens, preparing a batch of fire pebbles, and watching the troops she recruited look at somebody else.

## GM-Only Secrets
- **She is the best interrogation prize in the first three adventures, and the module says so quietly.** Haza resists interrogation firmly; Toogo invents nonsense; Zigath *might reveal* the githyanki contact. She is the single door to the campaign's actual premise, and she is also the one most likely to escape.
- **Her escape is printed and should be honoured.** If the fight turns, she dimension-doors past the stone seal and walks to the main nest through Yathazor. That is not a GM cheat — it is her written behaviour, and it makes her a recurring antagonist rather than a boss fight.
- **Her paranoia is the party's opening.** The stair glyph means her own warriors cannot reinforce her. A party that isolates the balcony is fighting a level-10 caster alone, and a party that ignores the balcony is fighting everything at once.
- **The hostages are on a four-round timer.** Any good-aligned character who kills one gains **no experience for the battle at all**; saving them is worth 100 XP each. That is a printed moral mechanic and it is unusually pointed for a 1994 module — it should be used as written.
- **She has never seen Yathazor and is about to have to walk through it.** If she escapes, her route takes her through a city she considers sacred and has never entered. That is a good scene the module never stages.

## Proposed Developments
- **Recommended:** let her escape the first time. She is more valuable moving through the campaign than dead in a hall, and Adventures Four through Six all have room for her.
- The fire pebble ingredients on her table are a party-usable resource with a real risk of exploding — an Intelligence check with modifiers by class, and a result of 20+ detonating for 5d6. Let a PC try it.
- Her resentment of Haza is worth a scene *before* combat if the party scouts: two commanders on the same shift, not speaking.
- If she is captured rather than killed, she is the cleanest possible way to hand the players the word "githyanki" — or, better, to hand them the concept without the word.

## Stat Block or Rules Notes
- Class: Psionicist [UC] / Priest (fire)
- Level: 8 / 8
- Armor Class: 16 (plate mail and ring of protection +1)
- Hit Points: 42
- Movement: near
- Strength −1, Dexterity +1, Constitution +1, Intelligence +2, Wisdom +4, Charisma +3
- Alignment: Chaotic (evil)
- Morale: 13 — **but see the escape clause; morale is not what makes her leave**
- Attacks: 2 attacks per round.
  - *Obsidian dagger +3* +7, 1d4+3
  - *Claws* +5, 1d4 (×2)
  - *Obsidian-tipped javelin +2* +6, 1d6+2 (thrown)
- **Fire cleric spells:** flame strike (6d8), wall of fire, produce fire (×3), glyph of warding, dispel magic (×2), hold person, silence, flame blade, command, cure wounds.
- **Psionics:** detonate, disintegrate, project force, telekinesis, teleport, **dimensional door**, molecular agitation, inertial barrier, time shift, mind thrust, id insinuation. All defence modes.
- **Fights From Height:** she casts from the balcony, behind hostages, with cover. Attacks against her from the hall floor have disadvantage until the stairs are taken.
- **Glyph-Warded Stairs:** flame strike (6d8, save for half) on anyone crossing without her password. Her own troops will not risk it.
- **Dimensional Door (escape):** when reduced below half hit points or when the hall is lost, she leaves. She does not fight to the death and should not be played as though she might.
- **Running her at the table:** she is the fight's artillery and its most dangerous single element, and she is also the one who runs. Both are correct. Do not let players feel cheated — foreshadow the balcony, the stairs and the seal so the escape reads as a plan rather than a rescue.
- **Conversion note:** printed 2e stats are Female Gith Psionicist 10 / Fire Cleric 10, hp 40, AC 2, THAC0 14, obsidian dagger +3, PSPs 132. Scaled to Shadowdark 8/8. Damage on flame strike retained at 6d8 to match the printed glyphs.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Zigath, an ancient Athasian gith fire-priest and psionicist, standing upright in a neutral token pose. Tall gaunt gith elder, taller than a typical hunched gith, heavily scarred mottled grey hide, sunken burning eyes, jagged teeth. Wrapped in layered ash-stained hides and dark robes over segmented armor, hung with obsidian prayer shards and burnt bone fetishes that catch the light dully. Holds a dark-metal spear upright like a ritual standard rather than a weapon; an obsidian dagger at the belt. Faint heat-shimmer and drifting ash around her. Imperious, devotional, proprietary bearing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One — Into the Mines
  - Section: "Zigath's Nest" — The Gith Forces; Zigath; Key areas 7, 8, 9; fire pebbles
  - Printed page: 80 (forces and shifts), 83 (stat block, resentment of Haza, the githyanki magicians, never been to Yathazor), 88–89 (fire pebbles), 90 (glyphs and the stone seal), 92 (her roost, the hostages, the XP rule), 93 (her chambers and chest)
  - Source type: official
  - Adaptation note: Stats converted to Shadowdark and scaled from 10/10 to 8/8. **The printed appearance is superseded — see the notice at the head of this file.**
- Title: mk-sandbox `actors/zigath.json` revision 4
  - Section: appearance, traits, goals, relationships, `sourceScope`
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: Authoritative for appearance and traits by its own declared `sourceScope`. All three existing goals are preserved above as Goals 1–3; Goal 4 is new and derives from the printed Haza resentment.
  - Id note: `actor-vakskra`, `actor-orruk-vesh`, `actor-queen-trinth`, `faction-black-spine-gith`, `location-zigaths-nest` resolve to real sandbox records. `actor-haza`, `actor-toogo`, `actor-slate` are proposed ids from this batch.
