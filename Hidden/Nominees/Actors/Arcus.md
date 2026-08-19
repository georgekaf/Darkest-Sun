---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Arcus (update to existing actor-arcus, revision 3)

*(Update to existing actor `actor-arcus`.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/arcus.json` (revision 3, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-arcus |
| `name` | Arcus |
| `actorType` | named-npc |
| `status` | active |
| `role` | Half-giant protector of Tenpug's Band |
| `factionId` | faction-tenpugs-band |
| `locationId` | location-tenpugs-temple |
| `description` | Arcus is the great physical shield of Tenpug's community. He is loyal, straightforward, and slow to understand intrigue, but he reacts immediately when the band is threatened. |
| `traits` | {"strength": 5, "loyalty": 5, "protectiveness": 5, "subtlety": 1} |
| `resources` | {"protectivePresence": 5} |
| `relationships` | `actor-tenpug` +5, `actor-danya` +2, `actor-sala` +2, `actor-roi` +2, `actor-lynth` +2 |
| `goals[]` | **Keep Tenpug and the surviving artisans safe from another gith attack.** — priority 5, progress 0, status active |
| `goals[]` | **Find the attackers who killed members of the band.** — priority 4, progress 0, status active |
| `sourceRefs[]` | DSE2 Black Spine — Cry Vengeance: Funeral Pyres (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
The band's half-giant shield — enormously strong, genuinely kind, badly frightened of complexity, and the loudest voice in the camp arguing that the gith can simply be killed one at a time.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-tenpugs-band` — protector
- Current location: `location-tenpugs-temple`
- Current route, when traveling: supply runs to markets and outlying settlements, always escorting someone else
- Role: Muscle, escort, hauler

## Player-Safe Description

### Appearance
Twelve feet of scarred half-giant, thick through the chest and shoulders in a way that makes the temple's doorways a daily negotiation. Skin sun-cracked across the back and forearms. He wears whatever the band's tanners can assemble at his size, which is never quite enough of it, and carries a wooden club the length of a grown man — trimmed from one of the Crescent Forest logs and worn smooth at the grip.

His face is habitually wary, and slides into open confusion the moment a conversation acquires a second layer. When that happens he looks for someone he trusts and waits to be told what he thinks.

### Manner and Voice
Slow, loud, warm, and literal. Arcus asks people to repeat things without embarrassment. He laughs easily and at the wrong moments. He states his opinions as flat facts — *"we can kill them"* — and is genuinely baffled when this fails to settle a debate.

He does not understand sarcasm and is hurt by it more than he lets on.

### Public Reputation
Beloved and slightly patronised. The band treats him as a very large child who can lift the water jars, and they are wrong about the first part in ways they have not had to learn yet.

## Confirmed Facts
- Half-giant, found wandering lost in the deep desert after escaping a slave caravan.
- Came from a primitive tribe far from the temple; on arrival he did not know how to find a city or locate water, which in an Athasian adult is close to unheard of.
- Was nursed back to health by the band's then Keeper of Supplies and has stayed with the band ever since. **See the divergence note under Sources — the printed text names Danya here, and the campaign record no longer supports that.**
- Chaotic by temperament; has been known to become violent, though almost always only when seriously threatened.
- Spends much of his time abroad with the band's supply runs, gathering and purchasing what the community needs.
- Principal pro-war debater in the second meeting tent. Argues the band can win; doubts the gith can organise well enough to be a real threat; correctly points out that nobody has actually counted them.
- Weak on defensive planning. His military thinking begins and ends with hand-to-hand combat.

## Goals
1. Description: Keep the band physically safe — by standing in front of it.
   - Priority: 5
   - Progress: ongoing
   - Target: indefinite
   - Deadline day: none set
   - Secret: no
   - Status: active
2. Description: Win the argument for fighting, because running means the desert, and he remembers the desert.
   - Priority: 4
   - Progress: contested — the tent is leaning the other way
   - Target: 1
   - Deadline day: before the gith are battle-ready
   - Secret: no
   - Status: active
3. Description: Be useful enough that nobody ever decides he is not worth the food he eats.
   - Priority: 5
   - Progress: unexamined
   - Target: —
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Ambition: None whatsoever.
- Caution: Low (2) — he does not model consequences well.
- Secrecy: 0. He cannot keep a secret and everyone knows not to give him one.
- Loyalty: Total, and attached to individuals rather than to the band as an idea.
- Cruelty: None. He is frightened of his own strength and has been since he first understood it.
- Risk tolerance: Very high for himself. He has never once considered that he might be the one who dies.
- Safety: The safest person in the camp, and the first one the gith will concentrate on.
- Wealth: None. Does not understand money and is routinely short-changed when sent to buy things alone.
- Status: Adored, not consulted — except in the war debate, where his voice carries because everyone can see him.

## Resources and Capabilities
- Raw strength sufficient to move temple stonework, haul timber, and end most fights in one exchange.
- Escort capability that makes the band's supply runs viable at all.
- Emotional weight in the debate — when the largest person in the room says *fight*, it lands.
- Complete willingness to be put anywhere in a battle line and left there.

## Relationships
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: Worshipful (5)
  - Reason: Tenpug is the one who decided Arcus was worth feeding. Arcus has never needed a second reason.
- Existing actor or faction ID: `actor-danya`
  - Attitude: Attached and slightly afraid (2)
  - Reason: **Divergence flag.** The printed source makes Danya his rescuer and employer, and has him cringing under her sarcasm while loving her. The campaign record has moved Danya elsewhere entirely. The emotional dynamic is worth keeping; the name attached to it needs a GM ruling. See Danya.
- Existing actor or faction ID: `actor-sala`
  - Attitude: Trusting (3)
  - Reason: Sala is small, gentle, and fixes things. Arcus is careful around him in a way that is quietly touching.
- Existing actor or faction ID: `actor-roi`
  - Attitude: Comfortable (2)
  - Reason: They sit near the oven and say almost nothing to each other for hours.
- Existing actor or faction ID: `actor-lynth`
  - Attitude: Uneasy (2)
  - Reason: He cannot read her and it bothers him. This is the closest thing the band has to an early warning about her.
- Existing actor or faction ID: `actor-raxxon`
  - Attitude: Fond (3)
  - Reason: Raxxon talks to him directly instead of over him.

## Knowledge
- Subject: His own origins
  - Claim: He came from a tribe somewhere far off, and cannot say where or name it reliably.
  - Source: Self-report, fragmentary.
  - Learned day: before the band
  - Confidence: low — his own account is inconsistent
  - Truth status: unconfirmed
  - Secret: no
- Subject: Gith numbers
  - Claim: Nobody has actually counted them, so nobody knows they are dangerous.
  - Source: His own observation, made in open debate.
  - Learned day: current campaign
  - Confidence: certain
  - Truth status: true and dangerously misused — he is right about the ignorance and wrong about the conclusion
  - Secret: no

## Current Activity
Arguing in the second meeting tent that the gith can be killed, and being steadily out-argued by Sala on grounds he does not have the vocabulary to contest.

## GM-Only Secrets
- **He is a level 6 fighter.** In a camp of craftsmen with ten combat veterans, Arcus is a genuine military asset that nobody has thought to use as one, because they cannot stop seeing the man who gets confused by jokes.
- **He does not know how he got to the desert.** The gap in his account is real, not simple-mindedness. Something happened between the slave caravan and being found, and he has no memory of it. The GM should decide whether that is trauma or something worse; the campaign has never touched it.
- **He is terrified of being sent away.** Goal 3 drives him more than the other two combined. A PC who tells him he is useless will do more damage than the gith manage.
- If the band is ever genuinely overrun, Arcus does not retreat. He will hold the temple doorway alone, which is both magnificent and exactly how he dies if the GM wants that.

## Proposed Developments
- The natural arc: a PC actually trains him and uses him as a unit anchor, and the band discovers what he is. Cheap, satisfying, and directly supports the "forge an army from craftsmen" premise.
- His rescuer's identity is now an open slot. Reassigning it — to Teva, to Sala, to Alshal, or to an unnamed predecessor — is a small, clean fix that also gives whoever gets it a permanent claim on him.
- The memory gap is a free hook of any size the campaign wants it to be, up to and including the gith having had him before.

## Stat Block or Rules Notes
- Class: Fighter
- Level: 6
- Armor Class: 12 (assembled hide; nothing fits properly)
- Hit Points: 48
- Movement: near
- Strength +4, Dexterity +0, Constitution +3, Intelligence −1, Wisdom +0, Charisma +0
- Alignment: Chaotic (good-natured)
- Morale: 12 — he does not retreat, largely because retreating does not occur to him
- Attacks: 2 attacks per round.
  - *Giant wooden club* +7, 1d8+4 (a trimmed Crescent Forest log; two-handed for anyone else, one-handed for him)
  - *Slam/shove* +7, 1d6+4 — and a Strength check to knock a target prone
- **Half-Giant Reach:** can strike targets at near range without closing.
- **Weapon Mastery (club):** +1 attack and damage, included above.
- **Immovable:** advantage on checks to resist being moved, grappled, or forced back. Contributes directly to holding a doorway.
- **Doesn't Follow:** disadvantage on any check involving deception, negotiation, or reading intent. Cannot be talked into a plan he does not understand — which occasionally saves him.
- Not a spellcaster. No psionic talent.
- **Running him at the table:** play the warmth first and the strength second. His combat value should be a surprise the players discover, not something the stat line advertises. He takes instructions literally and holds positions until told otherwise, including well past when he should have been told otherwise.
- **Conversion note:** printed 2e stats are Half-Giant Fighter 7, Str 21, hp 77, AC 8, THAC0 14 (10 with Str), giant wooden club 1d6+7. Scaled to Shadowdark level 6.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Arcus, an Athasian half-giant protector, standing upright in a neutral token pose. Enormous twelve-foot humanoid, massively built through chest and shoulders, sun-cracked weathered skin, heavy blunt features, old scars across forearms and back. Ill-fitting assembled hide and leather armor pieced together from mismatched sections, simple wraps, no helm. Carries a huge smooth-worn wooden club the length of a grown man, held loosely at rest. Expression wary and slightly confused rather than menacing — a gentle, uncertain giant. No metal, no ornament, no heroic posing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One
  - Section: Clash by Night — "Characters of the Slave Tribe"; "Area #9 Tent" debate
  - Printed page: 8 (stat block and background), 23 (debate position)
  - Source type: official
  - Adaptation note: Stats converted to Shadowdark. The printed background reads "Danya nursed him back to health, and has been with her and the tribe ever since" — retained here as *the then Keeper of Supplies* pending a GM ruling, because the campaign has moved Danya.
- Title: mk-sandbox `actors/arcus.json`
  - Section: description, appearance, relationships
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: Existing record already frames him as "the great physical shield… loyal, straightforward, and slow to understand intrigue." This nominee is consistent with that and adds the stat block, goals, and secrets.
  - Id note: `actor-tenpug`, `actor-danya`, `actor-sala`, `actor-roi`, `actor-lynth`, `actor-raxxon` all resolve to real sandbox records.
