---
entryType: actor
entrySubtype: named-npc
authorGM: ""
visibility: mixed
---

# Actor: The Caller in Darkness (update to existing actor-caller-in-darkness, revision 4)

*(Revision of existing actor `actor-caller-in-darkness`. **Not a monster — a weather system made of murdered souls. Read the "Running It" note before ever putting it on a battlemap.**)*

## Current record in mk-sandbox

*Read-only snapshot of `mk-repos/mk-sandbox/actors/caller-in-darkness.json` (revision 4, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-caller-in-darkness |
| `name` | The Caller in Darkness |
| `actorType` | named-npc |
| `status` | active |
| `role` | Psionic undead horror haunting Giustenal |
| `locationId` | location-giustenal-ruins |
| `description` | A unique undead consciousness created by the mass death surrounding Dregoth's fall. It reaches for minds with even slight psionic talent, speaking in an unknown language and driving victims toward madness, murder, and the ruins. |
| `traits` | {"psionicPower": 5, "secrecy": 5, "hunger": 5} |
| `resources` | {"psychicReach": 5} |
| `goals[]` | **Draw vulnerable psionic minds toward Giustenal.** — priority 5, progress 0, status active |
| `goals[]` | **Add more minds and psychic force to its collective existence.** — priority 5, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — The Caller in Darkness; The Caller in Giustenal (pp. 30-33, 43-45) |
| `simulation` | {"proposalMode": "eligible", "reason": "Regional supernatural threat."} |

## One-Sentence Summary
The merged group consciousness of everyone the sorcerer-kings slaughtered at Giustenal, trapped for two thousand years in an ethereal storm that is finally starting to dissolve — and which now murders psionic travellers to feed itself, because it mistakes being freed for dying.

## Classification
- Subtype: named-npc — **unique undead phenomenon**
- Control: autonomous
- Status: active, and **slowly failing**
- Faction or allegiance: none. It is not capable of allegiance.
- Current location: `location-giustenal-ruins` — the ruins, plus a **five-mile psionic search radius**
- Current route, when traveling: it does not travel. **It calls.**
- Role: The reason nobody goes to Giustenal

## Player-Safe Description

### Appearance
**None.** There is nothing to see. What people experience is a dead spouse standing on the city wall, or a glint of treasure past the gate, or a friend's voice saying something he did not say.

### Manner and Voice
It **speaks in an unknown language** — the tongue of the ancient city — and victims answer in it without knowing how. To everyone else the victim is just making strange noises at an empty wall.

Its signature trick is not illusion but **substitution**: it garbles what other people are actually saying. The module's own example:

> Mav grabs Cranch and hurls him to the floor of the skimmer. *"Come on, Cranch! Fight it! The Caller's got a hold of you!"* he shouts. Unfortunately, the Caller uses its ability to control sound to garble the words, and Cranch hears only, **"Now I'll have that treasure for myself!"**

### Public Reputation
**To most of the Tyr region, it has no name.** It is simply a danger, like tar pits and slavers, and the best way to deal with a danger is to avoid it. **Only the Sky Singers and others living in the ruins' shadow call it the Caller in Darkness.**

## Confirmed Facts
- **No one on Athas knows its true identity or nature — not even the Dragon or the sorcerer-kings.**
- **It is a very unique form of undead, created by the mass carnage inflicted on Giustenal by the sorcerer-kings at the time of [[Dregoth]]'s death.**
- The mechanism is printed in full: the **ethereal vortices** through which sorcerer-kings channel power to their templars behave like sandstorms — they gather loose energies that pass by. **When the sorcerer-kings battled in Giustenal, their collective vortices gathered in the ethereal space nearby. Never had the ethereal plane seen such a storm, and it was the souls of the city's slain that were caught up in the swirling funnels.**
- **Over the centuries, the powerful psionic energies of the spirits trapped within merged to form a kind of group consciousness.**
- **Only in the last few centuries have the supernatural winds begun to abate and slowly release souls to the Gray.** **The group consciousness believes that it is dying rather than being freed**, so it works to slay those nearby and draw in their souls.
- **Only those who die within the walls of the city are sucked into the Caller's maw.** This is why it does not kill at range — **it herds.**
- It searches constantly with psionic probes across a **five-mile area** around the ruins.
- **It only seeks full psionicists or those with wild talents** — and only minds that **remind it of who lived in Giustenal when Dregoth died: humans, elves, half-elves, dwarves, and halflings.** It **ignores thri-kreen, muls, half-giants, gith, and even the dray** beneath the ruins, and has **no use for unintelligent beasts**.
- **This is why so many predators live in the ruins unmolested** — and the module says the quiet part out loud: **the danger those beasts present helps heighten the fear of the Caller's desired victims.**
- **Fear is the point.** The original citizens and slaves died in stark terror, and that terror is what powered the storm. **A psionicist who dies with his heart full of fear adds more energy to the maelstrom than others.** So the Caller **terrifies a victim first, then forces the victim to take his own life.**
- It **prefers a slow, nerve-wracking, suspenseful orchestration of fear** — *"The Caller never simply creates illusions of giant monsters."* Only when a mind is about to snap, or the victim tries to flee the city, does it launch a savage mental attack.
- [[Abdaleem]] **has no psionic abilities, so the Caller has never bothered him.** He knows a little about it, **but nothing that will help characters defeat it.**
- Sky Singer guides from the Twilightcatchers clan will take money to guide people into the ruins, but **at the first hint of the Caller, the guide will disappear into the wastes.**
- **[[Nallan]] of Tenpug's Band is a confirmed kill.** He is found in the ancient temple with a bone dagger in his heart and an empty sheath on his belt.

## Goals
1. Description: Replace the souls the storm is losing.
   - Priority: 5
   - Progress: **losing ground — the winds are abating**
   - Target: any psionic mind of a suitable ancestry, inside the walls
   - Deadline day: none, and that is the horror of it
   - Secret: **it does not conceive of secrecy**
   - Status: active
2. Description: *(Proposed.)* Not die.
   - Priority: 5
   - Progress: it is not dying; it is being released, and it cannot tell the difference
   - Secret: no
   - Status: active

## Traits and Pressures
*(A group mind has no personality in the usual sense. What can be said:)*
- Ambition: **Survival, misunderstood.**
- Caution: It is patient to a degree no living creature could manage. It works in hours and days, not rounds.
- Secrecy: 0 — it does not hide; it is simply unrecognisable.
- Loyalty: None. It consumed everyone it ever was.
- Cruelty: **Total in effect, absent in intent.** It is a drowning thing grabbing whoever is nearest.
- Risk tolerance: Not applicable.
- Safety: **Effectively unkillable by conventional means.** See Rules Notes.
- Status: The most feared thing in the region, and nobody knows what it is.

## Resources and Capabilities
- **A constant five-mile psionic search net** around Giustenal, running always, forever.
- **Contact-class psionic assault**, once per day per victim outside the ruins, **twice per day inside**.
- **Control of sound** — it rewrites what victims hear other people say, in real time.
- **Bespoke illusion drawn from the victim's own mind**: *"The victim's mind is an open book to the spirit storm."* Dead loved ones, treasure, whatever the target wants most.
- **Contagion between victims.** Two contacted characters standing together each hear the name of *their own* beloved and each believes the other is seeing the same person.
- **Two thousand years of accumulated dead** as raw material.

## Relationships
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **Unaware neighbours**
  - Reason: **Dregoth's death created it, and Dregoth lives directly beneath it.** The module never states that they are aware of one another. See GM-Only Secrets — this is the biggest unwritten thing in the campaign.
- Proposed actor ID: `actor-nallan`
  - Attitude: **Kill**
  - Reason: Drove him to stab himself in the heart in the ancient temple.
- Proposed actor ID: `actor-abdaleem`
  - Attitude: **Invisible to it**
  - Reason: **He has no psionic ability.** The one man near Giustenal it cannot touch.
- Existing actor or faction ID: `actor-guvaano-twilightcatcher`
  - Attitude: Deterrent
  - Reason: His clan guides people into the ruins and abandons them at the first sign of it.
- Existing actor or faction ID: `actor-kataal-the-mover`
  - Attitude: **Unresolved**
  - Reason: Two psychic entities under and over one dead city — one preserving a single mind, one consuming thousands. **The module never puts them in the same sentence.** See [[Kataal the Mover]].

## Knowledge
- Subject: **Everything its victims knew**
  - Claim: Two millennia of absorbed minds, plus every psionicist it has taken since.
  - Source: consumption
  - Learned day: continuously since Dregoth's death
  - Confidence: —
  - Truth status: **inaccessible.** Nothing in the source suggests it can be interrogated, and it does not converse.
  - Secret: —
- Subject: Its own nature
  - Claim: That it is dying.
  - Source: —
  - Truth status: **false.** It is being freed.
  - Secret: **This is the lever. See Proposed Developments.**

## Current Activity
Sweeping five miles of desert for a mind that answers, every hour of every day.

## GM-Only Secrets
- **It is not a boss fight and the module says so directly:** *"The Dungeon Master must take care not to make the Caller simply another monster for player characters to confront with swords and spells."* Treat it as terrain, weather, and a countdown — not an encounter.
- **The real mechanic is social, not tactical.** Once a PC is contacted, the party's problem is *each other*: the affected character must be physically restrained, and **every word the restrainers say gets rewritten into threats and taunts.** The module notes this *"will usually cause resentment."* Run that at the table and it will do more damage than any attack routine.
- **It is a tragedy with a solution nobody has proposed.** The Caller kills because it thinks release is death. **It is factually wrong.** A party that can communicate the truth — that the storm is ending and the souls are going free — has a route to ending it that no amount of violence provides. **The module does not offer this. It should.**
- **The ancestry filter is a puzzle piece players can solve.** It takes humans, elves, half-elves, dwarves, halflings — the peoples of Giustenal at the time of the massacre — and ignores thri-kreen, muls, half-giants, gith and dray. **A party that works this out learns the date and nature of the atrocity from the shape of the predation itself.** It also means a half-giant or thri-kreen PC can walk in and out freely, which is an enormous and earnable tactical advantage.
- **Dregoth and the Caller are the campaign's great unwritten relationship.** Dregoth's murder created it. It sits directly above New Giustenal. It eats psionicists — and Dregoth is a psionic undead dragon king running a city of psionic templars. **Either he is immune, or he is hiding, or he is feeding it.** All three readings are supportable and all three are interesting. **Decide before Chapter Six.**
- **It is also Dregoth's perfect moat.** Nothing psionic gets near the ruins. Whether that is luck or design is unstated.
- *(Proposed.)* The souls are still individuals in there. A PC who loses a companion to it could, later, be spoken to *by that companion*. This is the single cruelest hook available and should be used at most once.

## Proposed Developments
- **Recommended: run it as a five-mile hazard band, not a monster.** Saves start when the party enters the radius; the ruins get worse; nothing is ever fought.
- **Adopt the "tell it the truth" resolution.** Give the party a way to learn that the storm is releasing souls, not losing them, and a way to communicate it. Ending the Caller by *explaining* is a far better climax than killing it, which the printed material barely supports anyway.
- Let a non-psionic or non-eligible PC be the party's only clear head. That is a great spotlight for whoever it lands on.
- Settle the Dregoth question. See GM-Only Secrets.
- The Kataal connection is the best unclaimed idea in either module. See [[Kataal the Mover]].

## Stat Block or Rules Notes
**The campaign book explicitly defers the statistics** to the MONSTROUS COMPENDIUM appendix packaged with the boxed set: *"Please refer to the Caller's entry before running an encounter with this unique being."* **That appendix is not present in the vault's book collection** — the block below is constructed, and should be replaced if the real entry is located.

- Class: — (unique undead group consciousness)
- Level: 10 (treat as beyond-tier; **it should not be defeated in combat**)
- Armor Class: — **it has no body and cannot be struck**
- Hit Points: — **see Ending It, below**
- Movement: none (its *reach* is five miles)
- Alignment: Chaotic
- Morale: —
- Attacks: **none physical, ever.**
- **The Call (contact):** once per day against any psionicist or wild talent within five miles of Giustenal; **twice per day** against a target inside the walls. Target makes a saving throw. On a failure, contact is established.
- **Summoning:** a contacted victim sees what they most want — a dead loved one on the walls, treasure past the gate — and begins speaking to it in the ancient tongue. **Once per hour thereafter**, save again: on a failure the victim can no longer resist and must find a way into the ruins. Success only means they hold out one more hour.
- **Garbled Sound:** words spoken to a contacted victim by unaffected characters **arrive as threats and taunts.** Two contacted victims each hear their own beloved's name in the other's mouth.
- **Terror, then the knife.** The Caller does not attack while it is still winning. **Only when the mind is about to break, or the victim tries to leave the city, does it make a savage mental attack** — and its preferred outcome is that the victim **kills himself**, in terror, inside the walls.
- **Selective:** affects **humans, elves, half-elves, dwarves and halflings** only. **Thri-kreen, muls, half-giants, gith and dray are wholly immune**, as are animals.
- **Feeding:** only those who **die within the walls** are taken.
- **Ending it:** no printed method exists. **Recommended house ruling:** it cannot be destroyed, only *undeceived* — convince the group mind that the abating winds are release rather than death and it lets go. Anything else is temporary.
- **Running it at the table:** slow, quiet, personal. Describe smells and half-heard voices for a session before anything mechanical happens. **Never give it a form.**
- **Conversion note:** the campaign book carries the full behaviour, mechanics of contact, victim selection, and the fear doctrine; **only the numeric block is missing.**

## Token art prompt (Banana Pro / image-gen reference):
> Full-body token of the Caller in Darkness — **not a creature, an apparition**. A towering vortex of pale ethereal dust and wind, roughly humanoid in overall silhouette but constantly dissolving, with dozens of faint screaming human, elf, dwarf and halfling faces surfacing and sinking within the swirling column. No solid body, no limbs, no eyes of its own. Colours are washed-out bone-grey and cold blue-white against darkness, with the faces lit faintly from within. Suggests a sandstorm and a mass grave at the same time. Terrifying but sorrowful, not monstrous. Dark Sun inspired, gritty realism, painterly. Full shape visible from base to top, clear silhouette, centered subject, neutral transparent or plain background, suitable for a VTT token, no environment, no scene.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Three: Outside Giustenal — The Caller in Darkness; Fear; Running the Caller in Darkness
  - Printed page: 30–31
  - Source type: official
  - Adaptation note: Origin, mechanism, victim selection, the fear doctrine, the contact/summoning sequence and the sound-garbling are all printed in full. **The numeric stat block is deferred to the boxed set's MONSTROUS COMPENDIUM appendix, which is not in the vault.**
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Two — Tenpug's Band (Nallan); Sky Singers (Twilightcatcher guides)
  - Printed page: 10, 12
  - Source type: official
- Title: City by the Silt Sea — Adventure Book
  - Section: Giustenal ruins — the ancient temple (Nallan's body)
  - Printed page: —
  - Source type: official
  - Id note: `actor-dregoth`, `actor-kataal-the-mover`, `actor-guvaano-twilightcatcher`, `location-giustenal-ruins` resolve to real sandbox/vault records. `actor-caller-in-darkness`, `actor-nallan`, `actor-abdaleem` are proposed ids from this batch.

## Unresolved Questions
- **Do Dregoth and the Caller know about each other?** The single biggest open question in the set.
- Whether the "undeceive it" resolution is adopted.
- What its relationship is, if any, to [[Kataal the Mover]].
- Whether individual absorbed souls can still be reached.
