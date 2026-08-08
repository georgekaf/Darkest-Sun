---
entryType: faction
entrySubtype: organization
authorGM: "Ghost"
visibility: mixed
---

# Faction: The Loyal (update to existing faction-the-loyal, revision 2)

## Summary
A small band of young elf preservers and thieves who follow Jessix the Wanderer, protecting travelers near Giustenal while trying to clear his name.

## Classification
- Faction type: Small elf protector band
- Status: active
- Headquarters: None — roams the wastes with Jessix
- Operational region: Giustenal ruins and the surrounding wastes
- Leadership: Jessix the Wanderer (leader); five named followers, all campaign-original

## Player-Safe Description
A handful of young elves, preservers and thieves, who travel with Jessix the Wanderer and help him watch the roads near Giustenal for danger. They say little about why they follow him, only that they trust him.

## Doctrine
- Remain loyal to Jessix.
- Protect travelers around Giustenal.
- Vindicate Jessix's name.

## Confirmed Assets
- Territory: None.
- Influence: Minor, local to the roads/ruins around Giustenal.
- Wealth: None notable.
- Agents: Jessix the Wanderer (leader) plus the five followers, now individually named and statted: Varesh (Thief 6), Kethen (Thief 6), Nyrra (Preserver 5), Saelis (Preserver 5), Tharek (Fighter 5). Names are campaign-original; the source leaves all five unnamed.
- Military: Small-band skirmish capability only; not a fighting force. Tharek is the sole dedicated fighter and the band's front line; everyone else fights as a thief or preserver.
- Intelligence: Direct witnesses to Slinnasia's death — firsthand knowledge of what actually happened.
- Trade access: None notable.
- Water access: None notable.

## Limitations and Internal Problems
No territory or institutional resources, and no standing anywhere: the band lives off what it carries. Until now no member but Jessix was named — that gap is what this revision closes. Their credibility is tied entirely to Jessix's — if his name isn't cleared, they remain outsiders with no formal standing.

## Goals
1. Description: Protect travelers near Giustenal from the Caller in Darkness.
   - Priority: 4
   - Progress: ongoing
   - Target: no confirmed target, standing patrol activity
   - Deadline: none set
   - Secret: no
   - Status: active
2. Description: Vindicate Jessix's name over Slinnasia's death.
   - Priority: 5
   - Progress: unresolved
   - Target: public exoneration
   - Deadline: none set
   - Secret: no
   - Status: active

## Agents and Member Groups
- `actor-jessix-wanderer` — leader. Not filed under the band's name; he leads it, he is not one of the five.
- Proposed `actor-varesh` — [[The Loyal - Varesh]]. Thief 6. Scout and forward eyes; walks ahead of the band and argues for withdrawal.
- Proposed `actor-kethen` — [[The Loyal - Kethen]]. Thief 6. Locks, seals and ancient doors; got the first expedition as far as Dregoth's templar chambers.
- Proposed `actor-nyrra` — [[The Loyal - Nyrra]]. Preserver 5. Enforces Jessix's rule against defiling more strictly than Jessix does.
- Proposed `actor-saelis` — [[The Loyal - Saelis]]. Preserver 5. Youngest; the one who approaches strangers first.
- Proposed `actor-tharek` — [[The Loyal - Tharek]]. Fighter 5. Stands between the band and whatever leaves the ruins.

All five ids are **proposed** — no `actor-varesh`, `actor-kethen`, `actor-nyrra`, `actor-saelis` or `actor-tharek` record exists in `actors/` yet. Levels are set from what the band survived (two Giustenal expeditions, permanent work in a Danger 5 region), and all sit below Jessix.

## Relationships
- Opposed to: the Caller in Darkness.
- Connected to: Slinnasia — the band witnessed her death and saw Jessix try to save her, which is the basis of their loyalty and their case for his innocence.
- Hostile to: Jessareen, who blames Jessix for Slinnasia's death. Tharek takes this personally in a way the others do not.
- Internal fault line: Varesh withdraws, Tharek advances — the band's standing argument, and the fastest way to characterise it at the table.
- Internal dependency: Nyrra trains Saelis and never praises him; Saelis keeps trying to earn it.
- Working pair: Varesh and Kethen run ahead together — the scout decides whether, the thief decides how.

## Faction Clocks
None established.

## GM-Only Secrets
None beyond what's in Confirmed Assets — the band's core secret (what really happened to Slinnasia) is already player-facing lore, not hidden.

## Proposed Reactions
- Field update to existing `faction-the-loyal`: add "Vindicate Jessix's name" to `doctrine`/`goals` (currently empty `goals: []`, and doctrine only covers loyalty + protection, not the exoneration motive) and record the Slinnasia-witness backstory in `sourceRefs`/notes, since it's the band's actual reason for existing, not just incidental flavor.
- Field update to existing `faction-the-loyal`: `agents` currently lists only `actor-jessix-wanderer`. If the five nominee actors are accepted, add `actor-varesh`, `actor-kethen`, `actor-nyrra`, `actor-saelis` and `actor-tharek` to `agents`, and change `membership.namedLeader: 1, followers: 5` to reflect five *named* followers rather than anonymous ones.
- Membership count (`followers: 5`) already matches `NPCs/The Loyal.md` and *City by the Silt Sea* p.12-13 — no change needed there.

## Sources
- Title: City by the Silt Sea Campaign Book
  - Section: Jessix the Wanderer
  - Printed page: 11-13
  - Source type: official
  - Adaptation note: —
- Title: `obsidian/NPCs/The Loyal.md`
  - Section: full entry
  - Printed page: —
  - Source type: campaign reference doc
  - Adaptation note: —
- Title: existing `faction-the-loyal.json` (revision 2)
  - Section: full entry
  - Printed page: —
  - Source type: campaign-original, prior MK-Sandbox submission
  - Adaptation note: —

## Unresolved Questions
- ~~Whether the 5 followers are meant to stay permanently unnamed~~ — answered: they are named as campaign-original characters, with individual sheets. Open instead: whether the GM wants those names treated as canon for the setting or as table-local only.
- Which of the five spotted Ranni in the Giustenal ruins on day 117 (ad7) before she teleported out. Varesh is the natural candidate as scout; unassigned so far.
