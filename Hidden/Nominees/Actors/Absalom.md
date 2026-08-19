---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Absalom (update to existing actor-high-priest-absalom, revision 3)

*(Revision of existing actor `actor-high-priest-absalom`. **Dregoth's High Priest, the first stable dray ever made, and the only member of the Dread King's inner circle working — quietly — against his god's plan. He is also "Akrag", who runs a bathhouse.**)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/high-priest-absalom.json` (revision 3, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-high-priest-absalom |
| `name` | Absalom |
| `actorType` | named-npc |
| `status` | active |
| `role` | High Priest of Dregoth |
| `factionId` | faction-new-giustenal |
| `locationId` | location-new-giustenal |
| `description` | An undead high priest who secretly aids the banished first-generation dray and hopes to reconcile them with Dregoth. |
| `goals[]` | **Serve Dregoth and preserve his religion.** — priority 5, progress 0, status active |
| `goals[]` | **Reconcile the first-generation dray of Kragmorta with Dregoth.** — priority 4, progress 0, status active |
| `sourceRefs[]` | City by the Silt Sea Campaign Book — Dregoth's Templars; First Generation Dray; Dray Relations (pp. 86-87, 91-93) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
A templar whom Dregoth killed and raised into undeath so that he could be a priest worthy of his god, who became the first dray ever to survive its own creation — and who now runs a seedy public bath under a false name while secretly protecting the exiles his god threw away.

## Proposed field changes *(added 13 August 2026, on the owner's ruling that the Akrag disguise is live)*
- **`aliases[]`: add `"Akrag"`.** The record currently has no aliases at all, so nothing on it connects Absalom to the bathhouse. Anyone reading the actor record alone cannot make the link.
- **`associatedLocationIds[]`: add `location-akrags-pools`.** `locationId` stays `location-new-giustenal`; the baths are where he operates under the alias, and the new location record names him as controller, so the link is carried on both sides.
- Everything else below is unchanged from the existing proposal.

## Classification
- Subtype: named-npc — **undead dray; High Priest**
- **Aliases: "Akrag"** — a dray bathhouse owner. **The disguise is live** (owner's ruling, 13 August 2026); his cover has not lapsed.
- Control: autonomous
- Status: **undead, active, and leading a double life**
- Faction or allegiance: **Dregoth**, publicly and doctrinally. **The first generation dray, privately.**
- Current location: `location-new-giustenal` — **area 11, Akrag's Pools**, and the Temples of the Dragon; frequently in `location-kragmorta`
- Current route, when traveling: between New Giustenal and Kragmorta, unremarked
- Role: **High Priest of Dregoth; Templar of the Fifteenth Scale**; publicly, a bathhouse owner named **Akrag**

## Player-Safe Description

### Appearance
As **Akrag**: a dray who owns and operates a public bath. As himself: **an undead visage** — *"The PCs might mistake him for some sort of spirit due to his undead visage."*

### Manner and Voice
He **delivers sermons on Dregoth** beneath the steeple of the temples. In Kragmorta he **preaches Dregoth's doctrine to the banished children**, and in New Giustenal he runs a bathhouse **"darker and seedier than most."**

He appears to the party **using psionics, in his true form**, speaks, and **disappears**.

### Public Reputation
**Two of them.** As High Priest of Dregoth, he is one of only two beings in existence with the power to mark a templar's advancement. As Akrag, he owns a bath **with a nasty reputation for several assassinations that have taken place in its steaming pools** — *"According to some, a mid-level templar was recently murdered while in the baths. Evidently, the body was pushed through the water drains into the Blackjaw River, for the templar was never seen again."*

## Confirmed Facts
- **Absalom is Dregoth's High Priest.**
- **He was a templar.** **To be his priest, Absalom had to become like his god. So Dregoth killed the templar and turned him into an undead creature.**
- **In truth, Absalom was the first dray ever to live beyond its creation.** Up to that point **all of Dregoth's attempts had resulted in dray, but the process was not stable** — subjects **continued to mutate beyond the point Dregoth had hoped for, became strange monstrosities, and eventually died.** **The only way to stabilise the process at the time was to kill the subject at the stage Dregoth desired and then turn him into an undead of some sort.** **This was what was done to Absalom.**
- **He was granted immortality alongside Mon-Adderath** so that the two could assist Dregoth in the centuries to come.
- **He is a Templar of the Fifteenth Scale.** **Only Mon-Adderath and Absalom have the necessary power to mark a templar's advancement**, using **a spell granted to them by Dregoth**. Every advance past 2nd level raises **a thick, yellowish scale from the templar's spine.**
- **Beneath the steeple in each temple is a huge room where Mon-Adderath or Absalom often deliver sermons on Dregoth.**
- **In truth, Akrag is actually Absalom, Dregoth's trusted High Priest.** *(The module directs the DM to the boxed set's cardstock sheets for his statistics and role-playing tips while in the guise of Akrag.)*
- **Akrag's Pools is area 11** — a public bath, **darker and seedier than most**, with **a nasty reputation for several assassinations** in its pools, including **a mid-level templar recently murdered there** whose body **went out through the water drains into the Blackjaw River.**
- **Akrag is listed as one of the people who could become the PCs' friends**, alongside some of the fishermen and Freiha the tavern owner.
- **Absalom secretly aids the first generation dray, as he feels an affinity toward them.**
- **He also preaches Dregoth's doctrine to these banished children, keeping them a part of the flock even though Dregoth has all but forgotten about them.**
- **Someday Absalom hopes to reconcile the rift between the exiles and their god, for the Day of Light should be shared by all Dregoth's children.**
- **He is working to forge a peace between the two types of dray** — **while Dregoth, through The Spirit of Kragmorta, is working to lure the first generation dray to New Giustenal in order to slay them and raise them as undead troops.**
- **The PCs can meet him in Kragmorta** — *"Absalom, Dregoth's High Priest and defender of Kragmorta's dray."*
- **After the PCs drive away the planar war party, they receive a visit from Absalom.** **He uses psionics to appear before them in his true form**, speaks to them, and disappears.
- **His statistics are in the boxed set's MONSTROUS COMPENDIUM appendix.**

## Goals
1. Description: **Reconcile the first generation dray with Dregoth.**
   - Priority: 5
   - Progress: ongoing and secret; **he is preaching to them, protecting them, and building toward it**
   - Target: both dray generations, and his god
   - Deadline day: **the Day of Light** — *"the Day of Light should be shared by all Dregoth's children"*
   - Secret: **yes — and it runs directly against what Dregoth is actually doing**
   - Status: active
2. Description: Serve as High Priest and keep the church running.
   - Priority: 5
   - Progress: he marks the scales and preaches the sermons
   - Secret: no
   - Status: active
3. Description: *(Proposed.)* Keep the Akrag identity intact.
   - Priority: 4
   - Progress: holding — **though people are dying in his bathhouse**
   - Secret: absolutely
   - Status: active

## Traits and Pressures
- Ambition: **Not for himself.** Everything he does is for a reconciliation he will not personally benefit from.
- Caution: **Extreme.** He operates under a false identity inside his own god's capital.
- Secrecy: **5.** Two identities, a secret ministry, and a plan opposed to his king's.
- Loyalty: **Genuinely to Dregoth — which is what makes him tragic.** He is not a traitor. He believes the exiles belong in the flock and that his god has simply forgotten them.
- Cruelty: Unrecorded, but **his bathhouse is where templars get murdered.**
- Risk tolerance: High, and quiet.
- Wealth: A bathhouse and a priesthood.
- Status: **Second or third most powerful being under Giustenal, and a bath attendant.**
- **Affinity:** *"He feels an affinity toward them."* **He was the first one, and the first one was killed to be stabilised.** He knows exactly what it is to be a failed experiment that Dregoth fixed by force.

## Resources and Capabilities
- **High Priest's authority** over Dregoth's entire church.
- **The scale-marking spell**, shared with only one other being alive.
- **Psionics** sufficient to project his true form to a party in another cavern and vanish.
- **Immortality**, granted by Dregoth.
- **A perfect cover identity** with a room full of steam, water drains, and a river outlet.
- **Standing and trust in Kragmorta** as *"defender of Kragmorta's dray."*
- **Access to both cities** and, presumably, to the tunnels between.

## Relationships
- Existing actor or faction ID: `actor-dregoth`
  - Attitude: **Worshipped, served, and quietly obstructed**
  - Reason: Dregoth killed him to make him, and Absalom loves him for it. **He is nonetheless working to save the people Dregoth intends to slaughter.**
- Proposed actor ID: `actor-mon-adderath`
  - Attitude: **Counterpart**
  - Reason: The only other immortal in the inner circle, and the only other holder of the scale-marking spell. **Mon-Adderath is a Templar of the Highest Scale (18); Absalom is of the Fifteenth.**
- Proposed actor ID: `actor-mosak-eggstealer`
  - Attitude: **Protected, secretly**
  - Reason: Absalom preaches to and defends Kragmorta's dray while Mosak is being worked by the Spirit.
- Proposed actor ID: `actor-spirit-of-kragmorta`
  - Attitude: **Direct opposition, probably unknowing**
  - Reason: **The Spirit is Dregoth luring the exiles to their deaths. Absalom is trying to bring them home alive.** Whether Absalom knows the Spirit is his god is the file's central open question.
- Proposed actor ID: `actor-freiha`
  - Attitude: Fellow potential ally
  - Reason: Both are named as people the PCs could befriend in New Giustenal.
- Proposed actor ID: `actor-casskka`
  - Attitude: *(Proposed.)* Competitor's neighbour
  - Reason: The Beetle's Bite is area 14; Akrag's Pools is area 11. Small city.

## Knowledge
- Subject: **The dray creation process, from the inside**
  - Claim: He is the first stable result of it, and he was made by being killed.
  - Source: **He is the experiment.**
  - Learned day: at his death
  - Confidence: certain
  - Truth status: true
  - Secret: **partially — the dray's own origin story is not necessarily told this honestly**
- Subject: Dregoth's doctrine and the Coruscation
  - Claim: He preaches it in both cities.
  - Confidence: total
  - Truth status: **doctrinally accurate, factually impossible.** See Dregoth.
  - Secret: no
- Subject: **What Dregoth is doing to Kragmorta**
  - Claim: **Unstated.**
  - Truth status: unknown
  - Secret: **This is the question the whole file turns on. See GM-Only Secrets.**

## Current Activity
Running a bathhouse in New Giustenal, preaching in Kragmorta, and trying to end a two-hundred-year schism from underneath.

## GM-Only Secrets
- **He is the campaign's best possible ally and the party will meet him as a suspicious bathhouse owner.** The module lists **Akrag** among the NPCs who *"could all prove to become the PCs' friends, depending on the actions of the group."* **They will have no idea who they are befriending.**
- **The central question the module never answers: does Absalom know the Spirit of Kragmorta is Dregoth?**
  - **If he does not**, he is a good man working for peace while his god quietly engineers a massacre, and the party can tell him. **That conversation is the campaign's moral climax.**
  - **If he does**, he is a High Priest deliberately deceiving his own church to save three thousand exiles from his god, and he is the most interesting NPC in either boxed set.
  - **Decide before Chapter Six.** Both are excellent; they are completely different characters.
- **He is proof the process required murder.** *"The only way to stabilise the process at the time was to kill the subject at the stage Dregoth desired and then turn him into an undead."* **Every dray alive descends from a line that only worked because Dregoth killed the first one.** Telling the dray that is a weapon.
- **The bathhouse is a murder room and he owns it.** Assassinations in the pools, a dead mid-level templar, a body flushed into the Blackjaw River. **Either Akrag is running a killing floor for his own purposes, or someone else is and he is letting it happen.** The module raises it and drops it. **It is the best unexplained detail in New Giustenal.**
- **He and Mon-Adderath are the only two who can mark a templar's scale.** **The entire hierarchy of 338 templars depends on two individuals, one of whom has a secret agenda.** He can create templars. He can presumably refuse to.
- **He appears to the party of his own accord** after the planar war party is driven off — **he seeks them out.** That is not an ambush; it is an approach.
- *(Proposed.)* He is the only being who could plausibly tell the party what Dregoth actually is, what the Coruscation actually requires, and where the dragon-skull font sits — and the only one with a motive to.

## Proposed Developments
- **Recommended: introduce Akrag early and neutrally.** Let the party use the baths, notice the reputation, and form an opinion. The reveal lands much harder if they liked him first.
- **Answer the "does he know" question and stick to it.** Everything else about him follows.
- Run the Kragmorta appearance exactly as printed — psionic projection, true form, a short speech, gone.
- **Give the bathhouse murders an owner.** If it's him, say what for. If it isn't, he has a problem he might want help with — which is a perfect, low-stakes first favour.
- Let the party be the ones who tell him about the Spirit. Then let him decide.

## Stat Block or Rules Notes
**The campaign book defers his statistics to the boxed set's MONSTROUS COMPENDIUM appendix and his Akrag role-playing notes to the cardstock sheets. Neither is present in the vault.** The block below is constructed.

- Ancestry: **Dray** (**the first**), **undead**
- Class: Priest (templar)
- Level: 10
- Armor Class: 17
- Hit Points: 70
- Movement: near
- Strength +3, Dexterity +2, Constitution —, Intelligence +3, **Wisdom +4**, Charisma +2
- Alignment: Lawful
- Morale: 12
- Attacks: 2 attacks per round.
  - *Claw* +9, 1d8+3
- **Undead:** does not eat, sleep, breathe or age. **Immune to charm, sleep, poison and disease.** *(Whether he can be turned is unstated — given he is a High Priest of a kaisharga, recommend **no**.)*
- **Templar spellcasting** at high tier, granted through Dregoth.
- **Mark of the Scale:** he and **Mon-Adderath** alone hold the spell that raises the yellowish spinal scale marking a templar's advancement. **Without one of them, Dregoth's hierarchy cannot promote anyone.**
- **Psionics:** sufficient to **project his true form into another cavern**, hold a conversation, and vanish. Treat as reliable long-range psychic projection at will.
- **The Akrag Guise:** a maintained false identity as a dray bathhouse owner. **Anything that would pierce a disguise or detect undeath should work** — and should be a major scene when it does.
- **Running him at the table:** as Akrag, wry, unbothered, faintly disreputable. As Absalom, formal and grieving. **The same voice underneath both.**
- **Conversion note:** **no accessible stat block.** Everything numeric above is constructed from his printed rank (Templar of the Fifteenth Scale, against Mon-Adderath's Highest at 18), his undead nature, and his demonstrated psionic projection.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Absalom, undead High Priest of Dregoth, standing upright in a neutral token pose. Tall gaunt draconic humanoid — a dray — with fine grey-green scales stretched tight over a lean frame, an elongated skull-like face with a short blunt snout, and no visible flesh at the cheekbones. A ridge of thick yellowish spinal scales rises along his back and behind his neck. Skin has the dry ashen cast of the undead; eyes are steady points of pale gold light with no pupil. Wears heavy priestly vestments of deep crimson and blackened obsidian-scale mail, a mantle marked with a roaring dragon head inside a crimson circle, and a long stole. Hands are clawed and folded calmly before him. Dignified, sorrowful, patient bearing — a clergyman, not a monster. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Five: The Ruins Below — New Giustenal area 11 "Akrag's Pools"; Dregoth's Templars
  - Printed page: —
  - Source type: official
  - Adaptation note: The Akrag identity, the bathhouse and its assassinations, the scale-marking monopoly and his rank of Fifteenth Scale are all printed. **Statistics and Akrag role-playing notes are deferred to boxed-set components not in the vault.**
- Title: City by the Silt Sea — Campaign Book
  - Section: Chapter Six: Dregoth and the Dray — the granting of immortality; First Generation Dray
  - Printed page: 63–66
  - Source type: official
  - Adaptation note: **Source of the whole character** — that Dregoth killed him to make him a priest, that he was the first stable dray, that the process required death to stabilise, and that he secretly aids the exiles and hopes to reconcile them.
- Title: City by the Silt Sea — Adventure Book
  - Section: Part Six — Kragmorta; the planar war party; Absalom's appearance
  - Printed page: —
  - Source type: official
  - Adaptation note: The psionic appearance in true form, and his description as *"defender of Kragmorta's dray."*
  - Id note: `actor-dregoth`, `location-new-giustenal`, `location-kragmorta` resolve to real sandbox/vault records. `actor-absalom`, `actor-mon-adderath`, `actor-mosak-eggstealer`, `actor-spirit-of-kragmorta`, `actor-freiha`, `actor-casskka` are proposed ids from this batch.
