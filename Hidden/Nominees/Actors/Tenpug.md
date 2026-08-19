---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Tenpug (update to existing actor-tenpug, revision 5)

*(Update to existing actor `actor-tenpug`, revision 5.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/tenpug.json` (revision 5, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-tenpug |
| `name` | Tenpug |
| `actorType` | named-npc |
| `status` | active |
| `role` | One-armed mul artisan and leader of Tenpug's Band |
| `factionId` | faction-tenpugs-band |
| `locationId` | location-tenpugs-temple |
| `description` | A quiet, gentle one-armed mul who was once a gladiator in Nibenay and later became a weapon-crafter and leader of escaped-slave artisans. He detests combat, but the organized gith attacks force him to protect the band and support a campaign of vengeance. |
| `relationships` | `actor-danya` +4, `actor-arcus` +5, `actor-sala` +4, `actor-roi` +4, `actor-lynth` +4, `actor-raxxon` +4 |
| `goals[]` | **Protect the band and discourage reckless expeditions into Giustenal.** — priority 4, progress 0, status active |
| `goals[]` | **Protect the survivors and learn why organized gith attacked the band with rare metal weapons.** — priority 5, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Tenpug's Band (pp. 10) |
| `sourceRefs[]` | DSE2 Black Spine — Clash by Night and Cry Vengeance (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
The one-armed mul who freed a column of artisan slaves and has spent every year since trying not to lead them — a gentle craftsman with a gladiator's body and a gladiator's memory, now forced to decide whether his people fight or run.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-tenpugs-band` — founder and named head
- Current location: `location-tenpugs-temple`
- Current route, when traveling: —
- Role: Leader of Tenpug's Band; master weaponsmith

## Player-Safe Description

### Appearance
A mul in his middle years, built like the arena built him — heavy through the shoulders and neck, scarred in the flat wide way that comes from edged weapons rather than accidents. His left arm ends above the elbow in a clean, long-healed stump; the right is disproportionately overdeveloped from thirty years of doing two arms' work. Hairless, sun-darkened, with the broad flat features and slight jaw underbite common to muls.

He wears carru leather cut loose, and he is almost always dusted with something — bone meal, forge ash, clay slip. The iron war hammer at his belt is the finest object in the camp and he made it himself. He does not carry it as a weapon. He carries it the way a smith carries a tool he happens to trust.

His voice is quiet and unhurried, and he stands closer to people than most Athasians find comfortable, because he does not expect to be attacked.

### Manner and Voice
Slow, mild, and disarmingly direct. Tenpug asks questions and then actually waits through the silence for an answer, which unsettles people used to being interrupted. He does not raise his voice; when he wants a room to stop, he stops, and the room notices.

He deflects authority reflexively — "ask the tents," "that is not mine to say" — and only takes it back when he judges the situation past debate. Everyone in the band can tell the difference immediately.

### Public Reputation
Revered without being obeyed, which is exactly the arrangement he engineered. Among the band he is "the one who opened the collars." Outside it, he is a name attached to unusually good weapons that surface in Nibenay's markets through intermediaries, with no one able to say who forged them.

## Confirmed Facts
- One-armed mul, former gladiator of Nibenay; lost the arm in the arena and survived, which got him reclassified as an artisan slave rather than killed.
- Learned weaponsmithing as a slave and continued to earn for his master one-handed.
- When a column of artisan slaves was ambushed in the Crescent Forest and its guards killed, he became leader of the survivors and led them into the desert, where he found the temple the band now occupies.
- Has spent years devolving decisions to the community; reserves his own judgement for genuine crises.
- Forbids searching the temple's sealed chambers. This is not negotiable and the band will back him against outsiders by force.
- Sandbox record already carries both source strands: the *City by the Silt Sea* framing and the *Black Spine* gith attack.

## Goals
1. Description: Keep the band alive through the gith war without becoming the kind of leader who spends people.
   - Priority: 5
   - Progress: undecided — the council is split by design
   - Target: survival of the band as a community, not just as bodies
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: Learn where organized gith obtained forged metal weapons in quantity.
   - Priority: 5
   - Progress: none — he knows only that it is impossible and therefore important
   - Target: identify the source
   - Deadline day: none set
   - Secret: no
   - Status: active
3. Description: Avoid dishonouring the temple's builders, whatever they were.
   - Priority: 4
   - Progress: offering bowl maintained; sealed rooms untouched
   - Target: indefinite
   - Deadline day: none set
   - Secret: no
   - Status: active
4. Description: Never again be the person who decides who dies.
   - Priority: 5
   - Progress: failing
   - Target: —
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Ambition: Very low. He has refused every opportunity to formalise his authority.
- Caution: High (4) — specifically about irreversible decisions.
- Secrecy: 2 — he keeps almost nothing back except his own fear.
- Loyalty: Absolute to the band. He considers the debt unpayable and is correct.
- Cruelty: None. He has killed a great many people and takes no comfort from any of it.
- Risk tolerance: High for himself, near-zero for others.
- Safety: Physically formidable, strategically exposed — the band's location is known to the gith.
- Wealth: Communal. Personally owns a hammer, a bedroll, and the tools of his trade.
- Status: Founder. Deferred to absolutely and consulted as little as he can arrange.

## Resources and Capabilities
- Master weaponsmith — the band's only source of quality arms, and its only hope of repairing what it captures.
- The temple itself: stone doors eight inches thick, defensible approach, concealed by dune screen.
- Roughly 150 adults capable of fighting, of whom about ten have any combat experience at all.
- Moral authority sufficient to overturn any council decision, spendable perhaps twice before it stops working.
- Personal combat capability far beyond anyone else in the band.

## Relationships
- Existing actor or faction ID: `faction-tenpugs-band`
  - Attitude: Founder
  - Reason: He opened the collars. Every member's freedom traces through him.
- Existing actor or faction ID: `actor-raxxon`
  - Attitude: Trusted (4)
  - Reason: Raxxon is his recruiter and outside voice — bad at carpentry, superb at getting good prices and reading strangers.
- Existing actor or faction ID: `actor-arcus`
  - Attitude: Protective (5)
  - Reason: Arcus is the band's shield and does not fully understand the politics he is being shielded from.
- Existing actor or faction ID: `actor-sala`
  - Attitude: Old debt (4)
  - Reason: Sala treated the arm. Tenpug has never forgotten who kept him alive when he was worth nothing to anyone.
- Existing actor or faction ID: `actor-roi`
  - Attitude: Kinship (4)
  - Reason: Two very old survivors of very long slaveries. They rarely speak and understand each other completely.
- Existing actor or faction ID: `actor-lynth`
  - Attitude: Trusted (4) — misplaced
  - Reason: He values her caution about strangers. See GM-Only Secrets.
- Existing actor or faction ID: `actor-danya`
  - Attitude: Wary respect
  - Reason: **Divergence flag.** Sandbox now places Danya as an Order psionicist watching Kharanok and the Black Spine, not as the band's Keeper of Supplies. The relationship value survives from the older record; the role behind it does not. See Unresolved Questions.
- Proposed actor ID: `actor-jolon`
  - Attitude: Exasperated reliance
  - Reason: Jolon holds the band's money and argues for bribery or flight. Tenpug seats him at council precisely because he disagrees.
- Proposed actor ID: `actor-teva`
  - Attitude: Consults her first
  - Reason: The band's wisest voice and the origin of the offering-bowl rite.

## Knowledge
- Subject: The sealed chambers beneath the temple
  - Claim: There are two concealed treasure rooms behind the friezes, and he knows how to open them.
  - Source: DSE2 Black Spine, Clash by Night — "Eye of the Storm".
  - Learned day: years before the gith war
  - Confidence: certain
  - Truth status: true
  - Secret: yes
- Subject: What the temple's builders were
  - Claim: Lion-headed giants whose spirits still watch the place and will punish desecration.
  - Source: Band tradition, formalised by Teva.
  - Learned day: on arrival
  - Confidence: certain (his), unfounded (actual)
  - Truth status: partially true — the builders are real, the curse-belief is not what he thinks it is
  - Secret: no
- Subject: Gith metallurgy
  - Claim: The gith raiders carry forged steel spears of uniform manufacture. Gith cannot forge.
  - Source: Direct examination of captured weapons.
  - Learned day: current campaign
  - Confidence: certain
  - Truth status: true
  - Secret: no

## Current Activity
Repairing and forging weapons at the bread oven while the two meeting tents argue themselves hoarse, listening from the edge of the crowd, waiting for a solution to present itself so he does not have to impose one.

## GM-Only Secrets
- **He has already decided to fight.** The council, the balanced advisors, the long deferral — it is all an attempt to make the band choose what he has privately concluded, so the deaths are theirs and not his. If the PCs argue for war, they are doing his work for him and he knows it.
- **Lynth is a Nibenese informer.** Tenpug does not know. If he learns it from the PCs rather than from her, his response is not violence — it is the quiet, total withdrawal of a man confirming his worst belief about himself as a judge of people.
- **The stump still hurts**, constantly, and has for thirty years. He has never mentioned this to Sala, who could help, because complaining is a slave's habit he refuses to resume.
- **He will lose the first battle.** The book requires it. What he does afterwards — barricaded in the smoke-filled hall with the doors buckling — is the actual character: he opens the sealed rooms himself, on his own authority, and never once suggests it was anyone else's idea.

## Proposed Developments
- The rubyheart is the trap laid for him specifically: an artifact that solves the casualty problem by making one person responsible for all the killing. He will not take it. He will let a PC take it, and he will hate himself for the relief.
- If the band survives and the gith are driven back, the natural next pressure is the iron itself — Nibenay will want the mine, and a hidden community of skilled artisans sitting near a metal source is a prize, not a secret.
- Long arc: the man who refuses to command is being steadily converted into a warlord by circumstance. The interesting failure state is that he is good at it.

## Stat Block or Rules Notes
- Class: Gladiator
- Level: 5
- Armor Class: 13 (carru leather; no shield — one arm)
- Hit Points: 34
- Movement: near
- Strength +3, Dexterity +2, Constitution +2, Intelligence +1, Wisdom +1, Charisma +0
- Alignment: Neutral
- Morale: 11 — he does not break, but he will accept terms if the band can be spared
- Attacks: 1 attack per round.
  - *Iron war hammer* +5, 1d8+3 (his own work; the best-made weapon within a hundred miles)
  - *Grapple/throw* +5 — arena technique, still reflexive
- **One-Armed:** cannot use shields or two-handed weapons; disadvantage on any check requiring two hands. He has had thirty years to route around this and does so without comment.
- **Arena Veteran:** advantage on morale-adjacent checks made to steady allies who can see him fighting.
- **Weapon Mastery (hammer):** +1 attack and damage, included above.
- Not a spellcaster. No psionic talent — unusual for a mul of his history, and something he has been quietly grateful for.
- **Running him at the table:** he answers questions honestly and deflects decisions. Do not let him solve the adventure. His function is to make the PCs' choices carry weight by visibly refusing to make those choices himself.
- **Conversion note:** printed 2e stats are Gladiator 7, Str 20, AC 5, hp 56, THAC0 14. Scaled to Shadowdark level 5 to sit correctly against the current House Markon roster (levels 2–7).

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Tenpug, a one-armed Athasian mul weaponsmith and former gladiator, standing upright in a neutral token pose. Hairless heavy-shouldered mul in middle age, sun-darkened skin, broad flat features with a slight underbite, deep flat scars across chest and forearm. Left arm ends in a long-healed stump above the elbow; right arm heavily overdeveloped. Loose carru leather armor dusted with bone meal and forge ash, simple work wraps, leather apron, plain belt. A finely made iron war hammer held at rest in the single hand, carried like a tool rather than a weapon. Calm, tired, gentle expression — not menacing. No ornament, no metal shine beyond the hammer, no heroic posing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One
  - Section: Clash by Night — "Characters of the Slave Tribe"; "Eye of the Storm"
  - Printed page: 12 (stat block), 36 (sealed chambers)
  - Source type: official
  - Adaptation note: Stats converted to Shadowdark. OCR of the source interleaves columns on p.12; stat line reconstructed from the readable fragments.
- Title: City by the Silt Sea Campaign Book
  - Section: Tenpug's Band
  - Printed page: 10
  - Source type: official
  - Adaptation note: Retained in the existing sandbox record. Places the band near Giustenal; Black Spine places it ~50 miles from Nibenay. Unreconciled — see Unresolved Questions.
- Title: mk-sandbox `actors/tenpug.json` revision 5
  - Section: goals, relationships, description
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: This nominee proposes an update, not a replacement. Existing goals `goal-tenpug-protect-band` and `goal-tenpug-answer-gith-attack` are preserved above as Goals 1–2.
  - Id note: `actor-raxxon`, `actor-arcus`, `actor-sala`, `actor-roi`, `actor-lynth`, `actor-danya`, `faction-tenpugs-band`, `location-tenpugs-temple` all resolve to real sandbox records. `actor-jolon` and `actor-teva` are proposed ids introduced by this nominee batch.
