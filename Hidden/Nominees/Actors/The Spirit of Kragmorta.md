---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: The Spirit of Kragmorta (update to existing actor-spirit-of-kragmorta, revision 4)

*(Revision of existing actor `actor-spirit-of-kragmorta`. **This entity does not exist. It is [[Dregoth]] wearing a dead god's face. Everything below the Player-Safe section is a spoiler for the best twist in Chapter Six.**)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/spirit-of-kragmorta.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-spirit-of-kragmorta |
| `name` | The Spirit of Kragmorta |
| `actorType` | named-npc |
| `status` | active |
| `role` | Supernatural enemy of the first-generation dray |
| `locationId` | location-kragmorta |
| `description` | A hostile supernatural presence bound to Kragmorta and feared by its first-generation dray inhabitants. Its attacks and influence have become the settlement's central external threat. |
| `traits` | {"will": 5, "secrecy": 4, "malice": 5} |
| `resources` | {"localInfluence": 5} |
| `relationships` | `actor-mosak-eggstealer` -5, `actor-high-priest-absalom` -2 |
| `goals[]` | **Break the security and cohesion of the Kragmorta dray.** — priority 5, progress 0, status active |
| `goals[]` | **Avoid or destroy those recruited by Mosak and Abdaleem to end its threat.** — priority 5, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — The Spirit of Kragmorta (pp. 75-80) |
| `simulation` | {"proposalMode": "eligible", "reason": "Local supernatural threat."} |

## One-Sentence Summary
A prophetic guardian spirit that appeared to the banished dray of Kragmorta a year ago wearing the shape of the lion-headed god of the Groaning City, told them their birthright had been stolen, and is in fact a psionic projection by the father who threw them away — recruiting them to die for him.

## Classification
- Subtype: named-npc — **fraudulent apparition**
- Control: **[[Dregoth]]**, directly, in real time
- Status: active — **first appeared about one year ago**
- Faction or allegiance: **Dregoth**, unknowingly to everyone who listens to it
- Current location: `location-kragmorta`
- Current route, when traveling: appears in the fiery cavern when Dregoth chooses
- Role: Guardian spirit, prophet, agitator — **none of which are real**

## Player-Safe Description

### Appearance
**A strange, ethereal figure that looks much like the lion-headed god once worshipped in the Groaning City.** *(That is to say: it looks like [[Taraskir the Lion]], though nobody in Kragmorta has the history to know it.)*

### Manner and Voice
Forgiving, patriarchal, aggrieved on their behalf. When [[Mosak Eggstealer]] challenged it outright, **it did not strike him down — it forgave his doubt**, which is precisely how it won the room.

It speaks in contrasts and images rather than commands:

> **"They are your brothers,"** the spirit exclaimed, showing them images of the second generation dray, **"but they have stolen your birthright. They live the good life because you have been cast out to suffer!"**

### Public Reputation
Among the first generation dray, **a genuine prophetic spirit** that grants signs and portents. It is the most credible voice in Kragmorta.

## Confirmed Facts
- **A prophetic spirit haunts the ruins of Kragmorta, granting signs and portents to the dray who live here.**
- **It first appeared about one year ago.** The occasion is precisely recorded: **a first generation dray warrior slew a huge beast that had entered the cavern in search of prey. She and her mate could not eat all of the meat, so she invited the rest of the clan to share in their feast. During the feast, a strange, ethereal figure appeared.**
- **It looked much like the lion-headed god once worshipped in the Groaning City.** **When it spoke, it claimed to be the guardian spirit of Kragmorta.**
- **[[Mosak Eggstealer]] was suspicious and challenged the spirit.** **Instead of striking him down like the crowd feared it would, the spirit forgave Mosak's doubt.**
- **It told the assembled dray that the Dread King of New Giustenal was to be blamed for the injustices done to the first born of the dray race.**
- **It showed them images of the luxuries of New Giustenal** — beautiful buildings, lively taverns, clean streets, **and clear water as abundant as the lava flow of Kragmorta** — in deliberate contrast to the fiery cavern they live in.
- **It urges them to attack New Giustenal.**
- **Mosak seeks help against the Spirit** — and **if adventurers confront it and expose it for what it is, thus saving more of Mosak's clan, they earn the respect and gratitude of the Clan Father.**

## Goals
*(These are Dregoth's goals. The spirit has none of its own.)*
1. Description: Provoke the first generation dray into attacking New Giustenal.
   - Priority: 5
   - Progress: ongoing for about a year; **an initial raiding party has already gone and been destroyed**
   - Target: Kragmorta's entire clan
   - Deadline day: none set
   - Secret: **absolutely**
   - Status: active
2. Description: Convert their deaths into worship.
   - Priority: 5
   - Progress: *"He has already done this to one of the Silt Stalkers' clans and to the first generation dray of the initial raiding party. Now he wants more."*
   - Secret: yes
   - Status: active

## Traits and Pressures
*(As performed. The performance is the character.)*
- Ambition: Presented as none — it claims only to guard.
- Caution: **High and skilful.** It waited for a feast, a full clan, and a moment of plenty.
- Secrecy: **5.** Its entire existence is the lie.
- Loyalty: Presented as absolute loyalty to Kragmorta. Actual loyalty: to the being projecting it.
- Cruelty: **It is grooming a whole people for slaughter and speaks to them tenderly while doing it.**
- Risk tolerance: Low — Dregoth risks nothing personally.
- Status: The most trusted voice in the city.

## Resources and Capabilities
- **Dregoth's psionic powers**, used to project a disguised image and to show the dray vivid images of New Giustenal.
- **The credibility of a forgiven challenge.** Mosak doubted it publicly and it responded with grace; that single moment is worth more than any miracle.
- **A genuine grievance to work with.** The dray really were cast out. The spirit is not inventing the injustice, only the remedy.
- **The stolen face of a real god** — the lion-headed deity of the Groaning City.

## Relationships
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **It *is* him**
  - Reason: *"The spirit is simply part of an elaborate plan set in motion by Dregoth himself... Dregoth uses his psionic powers to project his disguised image to Mosak and the clan."*
- Proposed actor ID: `actor-mosak-eggstealer`
  - Attitude: **Target, and the one who suspects**
  - Reason: Mosak challenged it, was publicly forgiven, and **still wants help against it.** He is being worked and half-knows it.
- Existing actor or faction ID: `actor-taraskir`
  - Attitude: **Identity theft**
  - Reason: The lion-headed god of the Groaning City is Taraskir — **whom Dregoth personally killed.** See GM-Only Secrets.
- Existing actor or faction ID: `actor-eevuu-silt-stalker`
  - Attitude: **Parallel operation**
  - Reason: *"As with the Silt Stalkers elf tribe, Dregoth seeks to increase his number of followers."* Same scheme, different marks.

## Knowledge
- Subject: New Giustenal
  - Claim: Its buildings, taverns, streets and water are exactly as shown.
  - Source: **Dregoth built it.**
  - Learned day: —
  - Confidence: certain
  - Truth status: **true, and that is why the lie works.** The images are real.
  - Secret: no
- Subject: Why the first generation dray were banished
  - Claim: That the Dread King wronged them.
  - Truth status: **true in fact, fraudulent in mouth.** Dregoth banished them himself and is now agitating them about it.
  - Secret: yes

## Current Activity
Appearing to a clan of exiles at intervals, sharpening a grievance it manufactured the conditions for.

## GM-Only Secrets
- **The whole thing is a recruitment drive for a god-in-progress.** *"He believes that he can only become a god if a huge amount of believers worship him. And if they will not follow him while they live, Dregoth is not above killing them and turning them into undead."*
- **It has already worked once, fatally.** An initial raiding party of first generation dray attacked New Giustenal, died, and **was raised as undead.** The spirit is now recruiting the rest of the clan into the same furnace.
- **The face is the tell, and it is a magnificent one.** Dregoth is wearing the likeness of **[[Taraskir the Lion]]**, the giant king he murdered to take Giustenal in the first place. **The banished dray are being urged to their deaths by an image of the last person Dregoth destroyed to build the city they're being told is their birthright.** Nothing in the module points this out. **A party that has seen the Lion Temple, or the lion-headed statues, or read the frescoes, can point it out.** That is the single best payoff available across both boxed sets.
- **Mosak already suspects.** The module hands the party their in: *he seeks help against the Spirit of Kragmorta.* The Clan Father wants this solved and cannot solve it himself.
- **Exposure is the printed win condition** — *"If adventurers confront the spirit and expose it for what it is (thus saving more of Mosak's clan), they will earn the respect and gratitude of the Clan Father."* That is an alliance with an entire dray city, obtained by argument.
- **Dregoth watches Kragmorta and always has** — *"Every few years, the Dread King scryed on the clan and watched their progress, always alert for useful mutations or adaptations that might develop."* His visits became less frequent because they were boring. He came back only when he needed bodies.
- **If the spirit appears while surface visitors are present, Dregoth will be furious to learn that his secret realm has been penetrated.** This is a printed trigger and it is the moment the campaign turns. **Decide in advance what he does about it.**
- *(Proposed.)* The spirit cannot be in two places at once, and Dregoth is a busy king. **Its appearances are schedulable.** A party that maps when it shows up is halfway to proving what it is.

## Proposed Developments
- **Recommended: let the party be present for an appearance and let them argue.** Do not make this a fight. Mosak's clan is the audience and the check is social.
- **Use the Taraskir recognition as the killing blow in that argument.** Any PC who has seen Taraskir's imagery elsewhere can identify the borrowed face. Reward the campaign's own accumulated knowledge.
- Have Mosak approach the party first, quietly, away from the clan. He cannot be seen doubting again.
- Decide what Dregoth does the instant he realises surface-dwellers are watching. **This is the campaign's hinge.**
- The parallel Silt Stalkers operation ([[Eevuu Silt Stalker]]) makes an excellent second data point — two tribes, one method.

## Stat Block or Rules Notes
**The Spirit has no statistics and must never have any.** It is an image. It cannot be attacked, damaged, dispelled, banished, turned, or interrogated as an independent being — **there is nothing there.**

- Class: — (psionic projection)
- Level: — (use [[Dregoth]]'s own capabilities for anything it does)
- Armor Class: — **nothing to hit**
- Hit Points: — **nothing to reduce**
- Movement: appears and vanishes at the projector's will
- Alignment: as Dregoth
- Morale: —
- Attacks: **none. It has never harmed anyone and never will — it gets others to do that.**
- **Projected Image:** Dregoth's psionics, disguised as the lion-headed god of the Groaning City. Anything that would reveal a psionic projection, trace a psionic link, or detect a mind at the far end of one **should work** — and is the intended route to exposure.
- **Vision-casting:** shows the assembled dray true images of New Giustenal. The images are **accurate**, which is why disproving them is useless. **Attack the messenger, not the message.**
- **Exposing it:** the printed outcome of exposure is social, not mechanical — the clan turns, and **Mosak's respect and gratitude** are the reward. Handle with checks against the *audience*, not against the spirit.
- **If exposed while Dregoth is projecting**, he learns immediately that his realm has been penetrated. **This is a printed consequence, not an optional one.**
- **Conversion note:** the module gives the Spirit **no statistics at all**, correctly. Everything above is procedure, not numbers.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body token of the Spirit of Kragmorta — **a ghostly apparition, semi-transparent throughout**. Tall, dignified humanoid figure with the head of a great lion, heavy mane, calm and paternal expression rather than fierce. Robed in the archaic ceremonial style of the Green Age, layered cloth falling to the ground with the lower edges fading into nothing rather than ending. Rendered entirely in cold luminous blue-white with faint edge glow; the whole figure is see-through and slightly indistinct, as though remembered rather than seen. Serene, benevolent, trustworthy in bearing — deliberately reassuring. Dark Sun inspired, painterly, gritty realism in the details of the robes and mane. Full figure visible from head to hem, clear silhouette, centered subject, neutral transparent or plain background, suitable for a VTT token, no environment, no scene.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Six: Beneath Giustenal — Kragmorta; **The Spirit of Kragmorta**
  - Printed page: 74–75
  - Source type: official
  - Adaptation note: The appearance, the feast, Mosak's challenge and its forgiveness, the quoted speech, the vision-casting, the truth of the deception, Dregoth's motive, the prior scrying and the raiding-party precedent are all printed. **No statistics exist and none should.** The identification of the lion-headed god as [[Taraskir the Lion]] is nominee-authored inference and is flagged as such.
  - Id note: `actor-dregoth`, `actor-taraskir`, `actor-eevuu-silt-stalker`, `location-kragmorta` resolve to real sandbox/vault records. `actor-spirit-of-kragmorta`, `actor-mosak-eggstealer` are proposed ids from this batch.

## Unresolved Questions
- **Confirm the lion-headed god is Taraskir?** The module implies it and never says it.
- What Dregoth does the moment he sees surface-dwellers in Kragmorta.
- Whether the spirit's appearances follow a schedule the party can map.
- Whether Mosak, once the truth is out, attacks New Giustenal anyway.
