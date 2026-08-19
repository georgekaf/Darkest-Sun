---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Raxxon (update to existing actor-raxxon, revision 7)

*(Update to existing actor `actor-raxxon`. Canonical spelling fixed by `gm-ruling-canonical-names-2026-07-21` — "Raxxon" supersedes the printed "Rakskon".)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/raxxon.json` (revision 7, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-raxxon |
| `name` | Raxxon |
| `actorType` | named-npc |
| `status` | active |
| `role` | Elf carpenter-thief and recruiter for Tenpug's Band |
| `factionId` | faction-tenpugs-band |
| `locationId` | location-nibenay |
| `description` | A young Athasian elf who poses as a wandering carpenter in Nibenay's outer market. Raxxon approaches useful strangers with the coded question, “Need any carpentry work done?”, testing whether they might aid Tenpug's hidden community of escaped slave craftsmen. |
| `traits` | {"caution": 4, "loyalty": 5, "craft": 4, "stealth": 4, "charisma": 3} |
| `resources` | {"carpentryTools": 1, "wrappedMetalSpearhead": 1} |
| `relationships` | `actor-tenpug` +4, `actor-lady-vardan` -2, `actor-veshara-seventh-seal` -1, `actor-danya` +2, `actor-arcus` +3, `actor-sala` +2, `actor-roi` +2, `actor-lynth` +3 |
| `goals[]` | **Recruit trustworthy outsiders with useful skills for Tenpug's Band.** — priority 5, progress 0, status active |
| `goals[]` | **Prevent Nibenay's templars, slavers, and gith from discovering the hidden community.** — priority 5, progress 0, status active |
| `goals[]` | **Learn how the organized gith acquired thin dark-metal weapons.** — priority 4, progress 0, status active |
| `sourceRefs[]` | Darkest Sun project planning — Raxxon and Tenpug's Band recruitment scene (pp. ?) |
| `sourceRefs[]` | DSE2 Black Spine — Clash by Night: source character Rakskon's approach (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
The band's recruiter: a genuinely bad carpenter and a superb reader of people, who walks into markets full of templars and asks armed strangers whether they need any carpentry work done.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-tenpugs-band` — outside agent
- Current location: `location-nibenay` (outer market)
- Current route, when traveling: Nibenay → the dune screen, travelling by night and navigating by stars
- Role: Recruiter, negotiator, nominal carpenter

## Player-Safe Description

### Appearance
A lean Athasian elf, tall even by elven standards, with a face wrinkled and burnished dark by deep-desert travel — he looks older than he is and uses it. Resin-stained fingers, permanently. Travelling clothes chosen to be forgettable, a coil of cord at the hip, a carpenter's satchel of bone tools that have seen real use and produced very little worth keeping.

Two short blades ride at his side, worn openly enough to read as sensible rather than threatening. Among the scrap timber in his pack is a wrapped dark-metal spearhead he has never explained to anyone.

### Manner and Voice
Fast, warm, and constantly working. Raxxon talks the way a trader talks — a question inside a joke inside a compliment — and every third thing he says is a test. He is physically comfortable getting close to strangers and steering them somewhere quieter.

He will appeal to your heroism first, your decency second, your appetite third, and your purse last and reluctantly. He is not stingy by nature; the money is not his.

### Public Reputation
In Nibenay's outer market he is a familiar minor nuisance — the elf carpenter who never seems to finish a job and always seems to be around. Nobody has ever connected him to anything. That is the entire point.

## Confirmed Facts
- Elf thief who trained as a carpenter after joining the band; still bad at the actual carpentry.
- Sold into slavery over "a little misunderstanding" with the templars of Gulg. Escaped within a week.
- Joined Tenpug's Band shortly after his escape.
- Kept on by Tenpug primarily because he obtains excellent prices for other people's work.
- Opens contact with the coded question: *"Need any carpentry work done?"* — asked of visibly armed strangers, in earshot of nobody.
- Will not discuss the band within hearing of templars; steers contacts to an alley or a tavern first.
- Authorised to offer food, lodging, friendship, and — grudgingly, last — money. The band can raise 1,000 sp in a genuine pinch.

## Goals
1. Description: Bring back fighters capable of saving the band, who can also be trusted with the temple's location.
   - Priority: 5
   - Progress: active recruitment underway
   - Target: one competent party
   - Deadline day: the gith are expected to be battle-ready in roughly seven days
   - Secret: no
   - Status: active
2. Description: Spend as little of the band's money as the recruitment can possibly be done for.
   - Priority: 3
   - Progress: ongoing
   - Target: —
   - Deadline day: none set
   - Secret: no
   - Status: active
3. Description: Never be taken alive by Gulg's templars a second time.
   - Priority: 4
   - Progress: eleven years clear
   - Target: indefinite
   - Deadline day: none set
   - Secret: yes
   - Status: active

## Traits and Pressures
- Ambition: Moderate — he likes being the one who is trusted outside the walls.
- Caution: High (4) in the city, careless (2) in the desert, which is backwards and will eventually cost him.
- Secrecy: 4 — competent operational discipline learned the hard way.
- Loyalty: Real, and slightly performative. He enjoys being seen to be loyal.
- Cruelty: None.
- Risk tolerance: High. He walks into templar-thick markets by choice.
- Safety: Exposed. He is the single most likely point of failure for the band's concealment.
- Wealth: Handles far more than he owns. Owns almost nothing.
- Status: Popular, not senior. Nobody consults him on policy; everybody relies on him for outcomes.

## Resources and Capabilities
- Market access and standing cover identity in Nibenay.
- Genuine talent for pricing and negotiation — the band's craft income runs substantially through him.
- Night navigation by stars across the sandy wastes to the temple.
- Thief's skillset: stealth, locks, pockets, and knowing when a conversation has been noticed.
- The trust of Tenpug, which he can spend on the band's behalf without checking first.

## Relationships
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: Devoted (4)
  - Reason: Tenpug kept him despite his uselessness at the trade he was assigned. Raxxon has never stopped repaying that.
- Existing actor or faction ID: `actor-lynth`
  - Attitude: Professional rapport (3)
  - Reason: The band's two operators. They compare notes on strangers and neither has yet turned that instinct on the other.
- Existing actor or faction ID: `actor-arcus`
  - Attitude: Fond (3)
  - Reason: Raxxon is one of the few who talks to Arcus rather than around him.
- Existing actor or faction ID: `actor-lady-vardan`
  - Attitude: Hostile (-2)
  - Reason: Existing sandbox relationship. Nibenese templar interest that Raxxon actively evades.
- Existing actor or faction ID: `actor-veshara-seventh-seal`
  - Attitude: Wary (-1)
  - Reason: Existing sandbox relationship.
- Existing actor or faction ID: `actor-danya`
  - Attitude: Cordial (2)
  - Reason: Carried over from the existing record. See the divergence flag on Danya.

## Knowledge
- Subject: The temple's location and approach
  - Claim: He can find it by night from Nibenay without landmarks.
  - Source: Repeated travel.
  - Learned day: years ago
  - Confidence: certain
  - Truth status: true
  - Secret: yes — this is the single most dangerous thing he carries
- Subject: Gith scouting activity around the dune screen
  - Claim: The approach is no longer safe; scouts are actively probing for weaknesses and counting defenders.
  - Source: Direct encounter en route.
  - Learned day: current campaign
  - Confidence: certain
  - Truth status: true
  - Secret: no
- Subject: The band's actual reserves
  - Claim: 1,000 sp, maximum, and that would hurt.
  - Source: Jolon.
  - Learned day: ongoing
  - Confidence: certain
  - Truth status: true
  - Secret: yes — he will not volunteer the figure while negotiating

## Current Activity
Working the Nibenay market at dusk, approaching armed strangers with the carpentry question, and preparing to lead whoever bites out into the sandy wastes at the next sunset.

## GM-Only Secrets
- **He has already been noticed.** Not caught — noticed. The gith scouts on the approach are not random; the band's location has been found, and Raxxon's repeated route is one plausible reason why. He has not considered this and would take it badly.
- **The wrapped dark-metal spearhead** in his pack is a captured gith weapon he is carrying to Tenpug for examination. He has not told anyone he has it, because carrying forged metal through a Nibenese market is a death sentence and he did it anyway.
- **He is not brave.** He is compulsively useful, which looks identical from outside and fails under completely different conditions.
- If the PCs mistreat him early, he does not retaliate — he downgrades them from "heroes" to "mercenaries" and quietly reopens the money conversation on worse terms.

## Proposed Developments
- The obvious reveal: Raxxon's route *is* the leak, and he has to live with having walked the gith home.
- He is the natural casualty if the campaign needs the band's danger made personal — he is likeable, exposed, and structurally expendable in a way Tenpug is not.
- If he survives the campaign, he is the band's natural ambassador to Nibenay in whatever settlement follows the mine's recapture.

## Stat Block or Rules Notes
- Class: Thief
- Level: 4
- Armor Class: 12 (leather and Dexterity)
- Hit Points: 18
- Movement: near (double near — Athasian elf)
- Strength +1, Dexterity +3, Constitution +1, Intelligence +2, Wisdom +0, Charisma +2
- Alignment: Neutral (good-leaning)
- Morale: 7 — he runs, and he is right to
- Attacks: 1 attack per round.
  - *Bone dagger* +4, 1d4 (carries two, wears them openly)
  - *Backstab* — triple damage against an unaware target
- **Elf Sprint:** double near movement; advantage on checks to outdistance pursuit across open sand.
- **Read the Room:** advantage on checks to notice surveillance, identify a templar in a crowd, or judge whether a stranger is worth approaching.
- **Haggle:** advantage on any check to set or argue a price. This is his actual class feature as far as the band is concerned.
- Not a spellcaster. No psionic talent.
- **Running him at the table:** he is the adventure's delivery mechanism and should never be the adventure's obstacle. Give him the coded line, let the players decide how suspicious to be, and let him be exactly as harmless as he appears — until the gith ambush on the approach, where he fights badly and honestly.
- **Conversion note:** printed 2e stats are Elven Thief 5, hp 22, AC 7, THAC0 18, bone daggers 1d4−1. Scaled to Shadowdark level 4.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Raxxon, an Athasian elf carpenter and recruiter, standing upright in a neutral token pose. Tall lean elf, six and a half feet, long-limbed, weather-toughened dark face deeply etched by desert wind and sun, sharp watchful eyes, close-cropped or wrapped hair. Practical forgettable desert travelling clothes in dust colors, wrapped forearms, a carpenter's satchel of bone tools, a coil of cord at the hip, scrap timber strapped to his pack. Two short bone blades worn openly at the sides, carried as sensible travel gear rather than menace. Resin-stained fingers. Friendly, quick, slightly conspiratorial expression — a man mid-negotiation. No armor plate, no metal shine, no heroic posing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One
  - Section: Clash by Night — "Plea From the Desert"; "Characters of the Slave Tribe"
  - Printed page: 5 (recruitment scene and stat block), 10 (background)
  - Source type: official
  - Adaptation note: Stats converted to Shadowdark. Printed name "Rakskon" superseded per the canonical-names ruling.
- Title: mk-sandbox `events/rulings/canonical-names-2026-07-21.json`
  - Section: rulings → canonical "Raxxon"
  - Printed page: —
  - Source type: GM ruling (read-only reference)
  - Adaptation note: Supersedes "Rakskon" and "Raxon". This also removes the printed material's accidental near-collision with the githyanki general Raskon (Adventure Six), who keeps his own spelling.
- Title: mk-sandbox `actors/raxxon.json`
  - Section: description, appearance, relationships
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: Existing record already places him at `location-nibenay` with the coded carpentry line. This nominee expands rather than replaces.
  - Id note: `actor-tenpug`, `actor-lynth`, `actor-arcus`, `actor-danya`, `actor-lady-vardan`, `actor-veshara-seventh-seal` all resolve to real sandbox records.
