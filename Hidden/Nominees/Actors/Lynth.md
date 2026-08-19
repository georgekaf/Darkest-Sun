---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Lynth (update to existing actor-lynth, revision 4)

*(Update to existing actor `actor-lynth`.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/lynth.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-lynth |
| `name` | Lynth |
| `actorType` | named-npc |
| `status` | active |
| `role` | Human rogue and scout of Tenpug's Band |
| `factionId` | faction-tenpugs-band |
| `locationId` | location-tenpugs-temple |
| `description` | Lynth watches strangers, listens for inconsistencies, and handles tasks that cannot be explained to honest traders. She trusts Tenpug, but assumes every new ally could lead slavers or templars back to the band. |
| `traits` | {"stealth": 5, "suspicion": 5, "observation": 5, "loyalty": 4} |
| `resources` | {"scoutingNetwork": 3, "hiddenTools": 1} |
| `relationships` | `actor-tenpug` +4, `actor-raxxon` +2, `actor-danya` +1, `actor-arcus` +2, `actor-sala` +1, `actor-roi` +1 |
| `goals[]` | **Find and close any trail the gith or other enemies can follow to the temple.** — priority 5, progress 0, status active |
| `goals[]` | **Determine whether Raxxon's recruited outsiders can be trusted.** — priority 4, progress 0, status active |
| `sourceRefs[]` | DSE2 Black Spine — Cry Vengeance: Funeral Pyres (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
The band's scout and vetter of strangers, who is very good at spotting infiltrators because she is one — a Nibenese templar's informer who has been embedded so long she is no longer certain which way she would jump.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-tenpugs-band` (public) — a Nibenese templar's private informer network, **secret**
- Current location: `location-tenpugs-temple`
- Current route, when traveling: —
- Role: Scout and internal security (cover identity that has become substantially real)

## Player-Safe Description

### Appearance
A controlled human woman in practical desert clothes cut to conceal — thief's tools, a short bone sword, and more besides. Nothing about her dress draws the eye, which itself takes work in a camp of artists.

She rarely looks directly at whoever she is studying, preferring to place herself at an angle and watch hands. When she does make eye contact it is deliberate and slightly too long.

### Manner and Voice
Warm on the surface, measured underneath. Lynth asks good questions and remembers the answers, and she is genuinely charming when she decides to spend the effort. She never volunteers information about herself and deflects with a joke rather than a refusal, so people rarely notice she has told them nothing.

In debate she is calm, practical, and consistently argues against the war on grounds of cost.

### Public Reputation
Trusted. She is the person the band sends to look at a stranger and say whether they smell wrong, and she has never once been wrong in a way anyone could point to.

## Confirmed Facts
- Human rogue attached to Tenpug's Band as scout and screener of outsiders.
- Watches strangers, listens for inconsistencies, and handles work that cannot be explained to honest traders.
- Trusts Tenpug personally; treats every new ally as a potential vector for slavers or templars.
- Opposes the war with the gith. Her stated reason is that dead artisans are a loss the band cannot absorb.
- Will not leave the camp under current conditions — the gith are between her and anywhere else.

## Goals
1. Description: Establish whether any new arrivals are a threat to the band's concealment.
   - Priority: 4
   - Progress: ongoing
   - Target: indefinite
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: Keep the band's craftsmen alive and their skills intact.
   - Priority: 5
   - Progress: contested — the camp is drifting toward war
   - Target: —
   - Deadline day: none set
   - Secret: no — but her reason for it is
   - Status: active
3. Description: Deliver the band's location, defences, and skill inventory to her handler in Nibenay.
   - Priority: 4 — and falling
   - Progress: complete in her head; never sent
   - Target: 1
   - Deadline day: none set
   - Secret: yes
   - Status: active
4. Description: Survive long enough to choose, rather than have the choice made for her.
   - Priority: 5
   - Progress: —
   - Target: —
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Ambition: Low now. It was the whole reason once.
- Caution: Very high (5).
- Secrecy: 5 — eight years without exposure, in a camp of two hundred people who eat together.
- Loyalty: Genuinely divided, which is worse for her than treachery would be.
- Cruelty: None. Her objection to the war is partly mercenary and partly that she has come to like these people.
- Risk tolerance: Low. She is boxed in and knows it.
- Safety: Trapped — gith outside, Tenpug inside.
- Wealth: Modest, unspent, and useless to her where she is.
- Status: Trusted implicitly. She finds this increasingly unbearable.

## Resources and Capabilities
- Skilled rogue: stealth, locks, pockets, and the reading of people.
- Complete working knowledge of the temple's layout, the band's numbers, its defences, and every skill it can field.
- The band's total confidence, which functions as an operational asset she has never actually spent.
- A dormant contact route back to Nibenay that she has not used and is not certain still exists.

## Relationships
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: Trusted by him (4); guilt on her side
  - Reason: He believes her judgement absolutely. That trust is the mechanism of her betrayal and the reason she has not committed it.
- Existing actor or faction ID: `actor-raxxon`
  - Attitude: Professional rapport (3)
  - Reason: The band's two operators. He is the only one whose tradecraft is good enough to catch her, and he has never thought to look.
- Existing actor or faction ID: `actor-arcus`
  - Attitude: Cautious (2)
  - Reason: He cannot read her and is visibly bothered by it. He is the band's only unwitting alarm.
- Existing actor or faction ID: `actor-sala`, `actor-roi`
  - Attitude: Low positive (1)
  - Reason: Existing values. She keeps a deliberate distance from the ones who would take it hardest.
- Unknown Nibenese templar — **no id; she does not know the name**
  - Attitude: Handler
  - Reason: She receives instructions and has never met the principal. **Secret.**

## Knowledge
- Subject: Her own tasking
  - Claim: Observe the band; if their skills are valuable, carry their location and defences back to Nibenay.
  - Source: Her handler, at recruitment.
  - Learned day: years ago
  - Confidence: certain
  - Truth status: true
  - Secret: yes
- Subject: The templar rumour about the band
  - Claim: Nibenese templars have long heard of a valuable group of escaped artisan slaves who would be worth a great deal if recaptured.
  - Source: Handler briefing.
  - Learned day: at recruitment
  - Confidence: high
  - Truth status: true
  - Secret: yes
- Subject: The band's full defensive picture
  - Claim: Numbers, layout, water source, sealed chambers, weapon stocks, who can actually fight.
  - Source: Eight years of trusted access.
  - Learned day: ongoing
  - Confidence: certain
  - Truth status: true
  - Secret: yes

## Current Activity
Arguing against the war in open council while privately calculating whether the gith or her own handler represents the greater threat to her survival, and finding no comfortable answer.

## GM-Only Secrets
- **Lynth is an informer for a templar of Nibenay** — probably in the sorcerer-king's service, though she has never been told which templar or which office. She has instructions and a dead-drop, and nothing else.
- **She has not filed a report in a long time.** Not from conversion — from cowardice, then habit, then something she has not named. The intelligence is complete and undelivered.
- **She is not evil.** The printed source is explicit: treated with respect, and genuinely befriended by a PC, she may find betraying the band difficult or outright impossible. Play the friendship honestly and let it actually work.
- **Her stated anti-war argument is her real one**, arrived at for the wrong reason. She started opposing the war because dead craftsmen are worth less recaptured. She continued opposing it because she has watched Roi bake bread for eight years.
- **Exposure cost:** if the party burns her publicly, Tenpug does not execute her. He does something worse for the campaign — he stops trusting his own judgement at the exact moment the band needs him to make a decision.
- If she is left alone and the war goes badly, she will try to run, and the gith will take her. What she tells them under interrogation is a live question.

## Proposed Developments
- The cleanest use: a PC befriends her, and she is the one who warns them about the gith blockade rather than reporting it. Her arc resolves without anyone ever learning she had an arc.
- The sharpest use: she is exposed at the worst possible moment, mid-siege, and the party has to decide whether the band can afford to lose its best scout over a report she never sent.
- Her unknown handler is a free hook into Nibenay's templarate. Whoever that templar is, they have an eight-year-old asset who has gone dark, and someone eventually notices.
- If the campaign wants a Nibenese claim on the iron mine later, her intelligence is how that claim gets made.

## Stat Block or Rules Notes
- Class: Thief
- Level: 6
- Armor Class: 13 (concealed leather and Dexterity)
- Hit Points: 26
- Movement: near
- Strength +0, Dexterity +3, Constitution +1, Intelligence +2, Wisdom +0, Charisma +2
- Alignment: Neutral
- Morale: 8 — she does not fight losing battles for other people's causes, and is re-evaluating whose cause this is
- Attacks: 1 attack per round.
  - *Bone short sword* +5, 1d6
  - *Backstab* — triple damage against an unaware target
- **Weapon Mastery (short sword):** +1 attack and damage, included above.
- **Read the Mark:** advantage on checks to detect a lie, spot a disguise, or judge whether someone is concealing an allegiance. She is excellent at this because she is doing it herself.
- **Ghost:** advantage on stealth in occupied areas she knows well — which is the entire temple.
- Not a spellcaster. No psionic talent.
- **Running her at the table:** never play her as sinister. She is helpful, competent, and likeable, and the tell is structural rather than behavioural — she is always slightly better informed than her stated role allows. If a player befriends her sincerely, let that land; the character is written to be winnable.
- **Conversion note:** printed 2e stats are Human Rogue 8, Dex 18, Cha 17, hp 31, AC 7, THAC0 17, bone short sword 1d6−1. Scaled to Shadowdark level 6.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Lynth, an Athasian human scout and rogue, standing upright in a neutral token pose. Human woman in her thirties, lean and controlled, sun-weathered but unscarred face, dark hair tied back simply, watchful sidelong gaze rather than direct stare. Practical layered desert clothes in muted dust and clay colors cut loose enough to conceal gear, wrapped forearms, soft boots, a short bone sword at the hip, small tool roll and pouches partly hidden under a wrap. Nothing decorative, nothing that draws the eye. Calm, pleasant, faintly guarded expression. No armor plate, no metal shine, no heroic posing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One
  - Section: Clash by Night — "Characters of the Slave Tribe"
  - Printed page: 10
  - Source type: official
  - Adaptation note: Stats converted to Shadowdark. The printed text is on a badly interleaved OCR column; the spy tasking, the "not actually evil" clause, and the befriendable-by-PCs clause are all recoverable and are preserved above.
- Title: mk-sandbox `actors/lynth.json`
  - Section: description, appearance, relationships
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: The existing record carries only the public framing — scout, screener, suspicious of newcomers. The informer tasking is **not** in the sandbox description and is held here in GM-Only Secrets, consistent with that.
  - Id note: `actor-tenpug`, `actor-raxxon`, `actor-arcus`, `actor-sala`, `actor-roi` all resolve to real sandbox records. Her handler has no id and deliberately none is proposed.
