---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Roi (update to existing actor-roi, revision 3)

*(Update to existing actor `actor-roi`.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/roi.json` (revision 3, updated 2026-07-22). Anything this nominee proposes is a change **against these values**.*

| Field | Current value |
|---|---|
| `id` | actor-roi |
| `name` | Roi |
| `actorType` | named-npc |
| `status` | active |
| `role` | Elder dwarf baker and artisan of Tenpug's Band |
| `factionId` | faction-tenpugs-band |
| `locationId` | location-tenpugs-temple |
| `description` | Roi is an elderly dwarf baker whose food and steady habits give the hidden community a sense of ordinary life. He has survived slavery and violence, but the latest deaths have left him quiet and bitter. |
| `traits` | {"craft": 4, "endurance": 4, "grief": 4, "steadiness": 5} |
| `resources` | {"foodStores": 2, "bakingCraft": 5} |
| `relationships` | `actor-tenpug` +4, `actor-danya` +3, `actor-arcus` +2, `actor-sala` +2, `actor-lynth` +1 |
| `goals[]` | **Ensure that grief and fear do not stop the community from eating and working.** — priority 4, progress 0, status active |
| `goals[]` | **Preserve the ordinary routines that keep the band from breaking apart.** — priority 3, progress 0, status active |
| `sourceRefs[]` | DSE2 Black Spine — Cry Vengeance: Funeral Pyres (pp. ?) |
| `simulation` | {"proposalMode": "eligible", "reason": "Standard NPC may be evaluated during GM-invoked simulation windows when relevant."} |

## One-Sentence Summary
A two-hundred-year-old dwarf baker who survived fifty years in Nibenay's brick-pits, walked away from his own execution, and has since refused to hold any focus at all — which makes him the band's warmest presence and, by dwarven reckoning, a walking catastrophe.

## Classification
- Subtype: named-npc
- Control: autonomous
- Status: active
- Faction or allegiance: `faction-tenpugs-band` — founding member
- Current location: `location-tenpugs-temple`
- Current route, when traveling: no longer travels; too old
- Role: Baker

## Player-Safe Description

### Appearance
A very old dwarf, stooped, with cracked hands and a flour-stained apron worn over everything. His back and face carry the marks of the whip — not scars from a beating, but the layered, overlapping record of decades of them, which is a different and much worse thing to look at.

Sad, patient eyes. A wooden club leans within reach of the oven, and has for years, and has never been used.

### Manner and Voice
Quiet. Roi speaks rarely and briefly, usually about bread. He is gentle with the camp's children, who cluster around the oven, and he does not appear to notice that he is the reason they do.

He becomes almost talkative on exactly one subject — the dwarven focus, which he does not have and will not take. *"Life was meant to be lived day by day, not from one conquest to the next."* Any dwarf who finds this strange, he will call a fool to their face, which is the only time anyone hears him raise his voice.

### Public Reputation
The heart of the camp, universally, and completely without anyone deciding it. The temple smells of his bread every morning. That smell is most of what makes the place feel like a home rather than a hiding hole.

## Confirmed Facts
- Dwarf, over two hundred years old.
- Captured in a raid when his people were destroyed.
- Worked fifty years in Nibenay's brick-pits, mashing straw into mud for the city's buildings.
- During a lull in construction he was taught to cook for other slaves and became a baker.
- His master was very cruel. When Roi was judged too old and sickly, he was sold off to die in the mines.
- Escaped on the road to the mines — his first act of defiance in five decades of slavery.
- Joined Tenpug before the band had even found the temple. A founding member.
- Bread is one of the band's staples; the temple's ovens are his, and pottery is fired in part of them.
- Holds **no focus**, deliberately, and defends the choice aggressively.
- Does not wish to fight — he is old and weak and says so plainly.

## Goals
1. Description: Feed the band. Every morning. Without exception.
   - Priority: 5
   - Progress: unbroken for years
   - Target: indefinite
   - Deadline day: daily
   - Secret: no
   - Status: active
2. Description: Live the remaining days as days, not as steps toward something.
   - Priority: 5
   - Progress: ongoing and contested by every dwarf who hears about it
   - Target: —
   - Deadline day: none set
   - Secret: no
   - Status: active
3. Description: Not be present when the killing starts.
   - Priority: 3
   - Progress: —
   - Target: —
   - Deadline day: —
   - Secret: no
   - Status: **will fail — see GM-Only Secrets**

## Traits and Pressures
- Ambition: Refused on principle. This is the defining fact about him.
- Caution: Moderate (3). He has no illusions about what people are capable of.
- Secrecy: 1. He simply does not talk much.
- Loyalty: Complete, quiet, and expressed entirely through labour.
- Cruelty: None — but there is fifty years of banked hatred in him for bullies and killers, and it has never once been discharged.
- Risk tolerance: Nominally very low. Actually unmeasured, because nothing has yet triggered him.
- Safety: Frail. He would not survive a serious blow.
- Wealth: None. Owns an apron, an oven he did not build, and a club he has never swung.
- Status: Beloved. Not consulted, not defended, not thought about — the way people do not think about the floor.

## Resources and Capabilities
- The ovens: bread for two hundred people daily, and the firing of the potters' work, which is the band's chief export.
- Fifty years of institutional knowledge about Nibenay's brick-pits, work gangs, and how the city moves slave labour.
- Extraordinary constitution — the thing that let him survive five decades that should have killed him in ten.
- Moral weight. When Roi is hurt, the band does not deliberate.

## Relationships
- Existing actor or faction ID: `actor-tenpug`
  - Attitude: Kinship (4)
  - Reason: Two very old survivors of two very long slaveries. They sit near each other and say almost nothing and understand it completely.
- Existing actor or faction ID: `actor-arcus`
  - Attitude: Comfortable (2)
  - Reason: Arcus sits by the oven for hours. Neither of them requires the other to talk.
- Existing actor or faction ID: `actor-sala`
  - Attitude: Grateful (2)
  - Reason: Sala keeps him upright. Roi is a difficult patient in the specific way of someone who does not think he is worth the herbs.
- Existing actor or faction ID: `actor-danya`
  - Attitude: Cordial (3)
  - Reason: Legacy value from the older record.
- Existing actor or faction ID: `actor-lynth`
  - Attitude: Mild (1)
  - Reason: She keeps her distance from him deliberately. He has not noticed and would not mind.

## Knowledge
- Subject: Nibenay's brick-pits and slave logistics
  - Claim: How work gangs are organised, moved, sold, and disposed of; which routes the condemned travel to the mines.
  - Source: Fifty years inside it.
  - Learned day: long past
  - Confidence: certain, though decades out of date
  - Truth status: true as of his time
  - Secret: no — nobody has ever thought to ask him
- Subject: The dwarven focus
  - Claim: That a life spent on a single fulfilment is a life wasted, and the fear of undeath is not a good enough reason.
  - Source: His own conclusion.
  - Learned day: after his escape
  - Confidence: absolute
  - Truth status: **theologically dangerous — see GM-Only Secrets**
  - Secret: no

## Current Activity
Baking, before dawn, while the camp argues about whether it is going to exist next week.

## GM-Only Secrets
- **He will not stay out of the battle.** The printed source is explicit: the moment any member of the band is killed, fifty years of banked animosity for bullies and killers comes up all at once and he charges in. He is a 0-level dwarf with 8 hit points and a wooden club. He will get himself into far more trouble than he can handle, and this should be allowed to be as bad as it sounds.
- **The focus problem is a live mechanical threat in this setting.** Per the vault's own `Rules/Ancestries.md`, dwarves pursue a personal focus they must fulfil before death *for fear of undeath otherwise*. Roi has refused to hold one for two centuries. If he dies angry, in a fight he chose, having completed nothing — the campaign has already established what that produces.
- **Black Spine supplies the answer to its own question.** Adventure Five puts two dwarven banshees, Pimns and Solaq, at the chasm below Yathazor — dead slaves who died mid-rebellion with everything unfinished. If the party later meets them and has already watched Roi die, the connection does the work without a word of exposition.
- **He has a focus and denies it.** The bread. Every morning, without exception, for years. He would reject this framing furiously, and it is nonetheless the reason he is still upright.

## Proposed Developments
- **Recommended:** if the GM wants one death in the first battle to matter, it is this one. He is beloved, frail, and structurally guaranteed to charge.
- The banshee thread is the strongest long-range hook in the band. Roi dying at the temple and the party meeting Pimns and Solaq underground several sessions later is a two-part structure the module hands over for free.
- Alternative and quieter: he survives, and a PC works out what the bread actually is, and tells him. He would not thank them.
- His brick-pit knowledge is an unused key to Nibenay. Nobody in two hundred years has debriefed the man who spent fifty years inside the city's labour system.

## Stat Block or Rules Notes
- Class: none — 0-level artisan
- Level: 0
- Armor Class: 10 (apron)
- Hit Points: 8
- Movement: near (slow — treat as reduced for chases and forced marches)
- Strength +1, Dexterity +0, Constitution **+4**, Intelligence +1, Wisdom +0, Charisma −3
- Alignment: Chaotic (good-natured)
- Morale: 5 normally — and **12 the moment a member of the band is killed in front of him**
- Attacks: 1 attack per round.
  - *Wooden club* +1, 1d6
- **Unkillable, Historically:** his Constitution modifier is the highest in the band and is the reason he is alive. Advantage on saves against exhaustion, heat, thirst, disease, and poison.
- **No Focus:** Roi holds no dwarven focus. If he dies with unfinished violent business, the GM should treat undeath as a live outcome rather than a flavour note — see GM-Only Secrets.
- **Fifty Years of Patience:** the first time he attacks a creature that has harmed a member of the band, he attacks with advantage. Once. He is not a fighter; he is two centuries of restraint failing at once.
- Not a spellcaster. No psionic talent.
- **Running him at the table:** do not give him dialogue about the war. Give him bread, children at the oven, and short answers. Everything the character is worth is in the contrast between how harmless he looks and what Athas spent two hundred years doing to him.
- **Conversion note:** printed 2e stats are Dwarf, 0 level, Con 20, hp 8, AC 10, THAC0 20, wooden club 1d6. Kept at level 0 deliberately — scaling him up would destroy the point.

## Token art prompt (Banana Pro / image-gen reference):
> Full-body character token of Roi, an extremely old Athasian dwarf baker, standing upright in a neutral token pose. Very aged dwarf, stooped, broad but shrunken, bald or thin white hair, deeply lined face, sad patient eyes, cracked and burn-marked hands. Overlapping old whip scars visible across the face and forearms. Flour-stained apron over simple worn work clothes in dust and clay colors, sleeves pushed up, cloth wrap at the waist. A plain wooden club held loosely and awkwardly, clearly not a weapon he knows how to use. Gentle, tired, quietly broken expression. No armor, no metal, no ornament, no heroic posing. Dark Sun inspired, gritty desert fantasy realism. Full body visible from head to feet, clear silhouette, centered character, neutral transparent or plain background, suitable for a VTT token, no environment, no scene, no action pose.

## Sources
- Title: DSE2 Black Spine, Book One
  - Section: Clash by Night — "Characters of the Slave Tribe"
  - Printed page: 11
  - Source type: official
  - Adaptation note: Stats kept at 0 level. The charge-into-battle trigger and the refusal of a focus are both printed and are load-bearing here.
- Title: mk-sandbox `actors/roi.json`
  - Section: description, appearance, relationships
  - Printed page: —
  - Source type: campaign record (read-only reference)
  - Adaptation note: Existing record already has "survived slavery and violence, but the latest deaths have left him quiet and bitter." This nominee is consistent and adds the focus/undeath reading.
- Title: `obsidian/Rules/Ancestries.md`
  - Section: Dwarf
  - Printed page: —
  - Source type: campaign rules
  - Adaptation note: Source of the focus-and-undeath mechanic that makes Roi's refusal dangerous rather than merely characterful.
  - Id note: `actor-tenpug`, `actor-arcus`, `actor-sala`, `actor-danya`, `actor-lynth` all resolve to real sandbox records. Pimns and Solaq are proposed ids from this nominee batch.
