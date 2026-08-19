---
entryType: artifact
entrySubtype: relic
authorGM: "Ghost"
visibility: mixed
---

# Artifact: The Dark Lens (update to existing artifact-dark-lens, revision 2)

*(Revision of existing artifact `artifact-dark-lens`, now at revision 1. **A record exists** — verified 16 August 2026 against `artifacts/` on the default branch, along with `plots/dark-lens.json` at revision 4. This is not a new filing. Everything below is a change **against those values**, drawn only from House Markon table play. Issue #251 asks for construction requirements, where the knowledge lives, where the historical Lens is, and the campaign-specific limitations; three of the four are partly answerable from the record of play, and this revision supplies them.)*

## Current record in mk-sandbox

*Read-only snapshot of `artifacts/dark-lens.json`, revision 1, created 29 July 2026.*

| Field | Current value |
| --- | --- |
| `status` / `canonStatus` | historical-whereabouts-unconfirmed-in-campaign / official-dark-sun-lore-adopted |
| `description` | Rajaat-created flawless polished obsidian egg-shaped orb, about the size of a small kank, ~170 lbs, radiating intense heat. Amplifies magic and psionics. **Explicitly not Kalak's perfect obsidian orb.** |
| `operatingRequirements[]` | physical contact · successful psionic contact at severe penalty · heat harms until contact is established · draws on its own psionic reserve first |
| `history[]` | Rajaat made it near the end of the Time of Magic · used to create other artifacts and empower the Champions · Jor'orsh and Sa'ram stole it from the Pristine Tower, hid it on Mytilene, guarded it as banshees |
| `relationshipToKalaksOrb` | Separate artifact. Kalak's orb may serve as the same *kind* of perfect-obsidian focus for a new device, but is not a piece or core of the historical Lens |
| `unresolvedDetails[]` | current location and custody in this continuity · **whether House Markon will attempt to locate the historical artifact or create a new Lens-like device** |
| `sourceRefs[]` | *Psionic Artifacts of Athas*, "The Dark Lens", pp. 7-8 |

**Revision 1 is sound as lore and this revision does not touch it.** What it lacks is the campaign layer: three sessions of House Markon play have established a construction project, a bargain that authorises it, and a target, and none of that is in the record.

## Proposed changes

### 1. The second `unresolvedDetail` is answered — resolve it

*"Whether House Markon will attempt to locate the historical artifact or create a new Lens-like device."*

**They are building one, and they have paid for the right to do it.** On **Day 113** (episode 19, «Bloody Red Oasis») the party struck a bargain directly with **Siemhouk**: they descend into the depths of Nibenay to fight **Zwuun** on the Sorcerer-King's behalf, and in exchange they receive **free access to build the Dark Lens**. She added that she would follow them to Tyr herself when the time came to kill Kalak, and that House Shom stays untouched for now. The only reason she did not kill them on the spot for the Scourge, she said, was a vision in which she saw them fight Zwuun and win.

This should move out of `unresolvedDetails[]` and into the record as a confirmed campaign commitment.

### 2. Add the construction project, as campaign material distinct from the historical artifact

**Origin of the plan: Tithian's notes.** On episode 13 Agis and Sadira revealed what they had taken from the dead **Tithian**'s notes — that he had planned to build the weapon, described there as a **dark mirror able to amplify and direct magical energy at long range, powerful enough to strike a Sorcerer King**. Agis proposed following Tithian's plan directly.

**Construction method, as proposed in play.** Collect the **scattered construction components from several cities, beginning with Nibenay**, specifically so that no single city's authorities can infer the real purpose. That is the method the party adopted; no component list beyond the core has been established.

**The core component.** Episode 14: Agis and Sadira describe the Lens as Rajaat's work, able to channel magic into a destructive beam, **with a flawless obsidian sphere at its centre**.

**Internal dissent, which is campaign-significant.** Hukaa raised strong moral objections to building a weapon of that scale. Karkus proposed an alternative course entirely — recovering the **Heartwood Spear**, the Sorcerer-King-killing weapon, either from dead Kalak's treasury in Tyr or by asking the Halflings. Neither objection was resolved; the project proceeded.

### 3. Record the target — this is new and it is the sharpest thing play has produced

**Siemhouk stated the Lens is aimed specifically at Borys, not at Sorcerer-Kings in general.** Her reasoning, given on Day 113: if **Borys** dies, **Rajaat is freed**, the remaining Sorcerer-Kings **lose their power**, the peoples rise, and the whole structure of authority collapses.

The existing `plots/dark-lens.json` already carries this as `testimony[]`. **It belongs on the artifact record too**, flagged the same way — it is Siemhouk's claim, not established fact, and the plot record's `unresolvedDetails[]` already lists its objective truth as open.

### 4. Flag the conflict rather than resolve it — Melketh contradicts the sourcebook

This is the one item that must not be silently merged.

`artifacts/dark-lens.json` states, from *Psionic Artifacts of Athas*, that the historical Dark Lens **is not** Kalak's perfect obsidian orb and that Kalak's orb is not a piece or core of it.

**In episode 14 the blind Melketh says the opposite**: that Rajaat made the Lens, that his Champions turned it against him and exiled him, and that **the piece at its centre — a flawless obsidian sphere — is the same sphere the party had already taken from Kalak.**

Both cannot be recorded as fact. Three readings, none of them proposed here:

1. **Melketh is wrong or speaking loosely**, and means Kalak's orb is the same *kind* of focus — which is exactly what `relationshipToKalaksOrb` already allows.
2. **Melketh is right and the campaign diverges** from the printed lore on this point, which is a ruling the owner would have to make explicitly.
3. **Melketh is describing the new device, not the historical one** — in which case the party's orb is the core of the thing they are building, and the two artifacts stay separate.

Reading 3 is the most economical and matches the `proposalConstraint` already on the plot record. **It is still a ruling, not a deduction, and the record should carry the conflict until it is made.**

Note also that the plot record states Kalak's orb **remains buried and guarded at Quor'Anok**, while Melketh speaks of it as something the party already has. Whichever reading is taken, that custody question needs settling before any construction step can be recorded.

### 5. Corroborate the theft legend

Melketh also told a legend — **explicitly not offered as certain history** — of **two dwarf warriors who once stole the Dark Lens from the dragon Borys**. That matches `history[]`'s **Jor'orsh and Sa'ram**, already on the record from the sourcebook. Worth recording as in-campaign corroboration of the printed account, and as the reason the party has any reason to believe the historical Lens is findable at all.

## What issue #251 asks, and what this leaves open

| #251 asks | State after this revision |
| --- | --- |
| Lens **construction requirements** | **Partly answered.** Method (scattered components, several cities, starting with Nibenay) and core (flawless obsidian sphere) are established. **No component list, no procedure, no craft requirement has ever been stated at the table.** GM input still needed. |
| Where the **knowledge** is located | **Partly answered.** Tithian's notes, held via Agis and Sadira. Melketh, a former Veiled Alliance member and once a scholar of the great library **inside the Nibenay palace** (episode 23). Whether the library holds the rest is unestablished. |
| **Historical Lens** location | **Not answered in play.** The sourcebook places it on Mytilene under Jor'orsh and Sa'ram, and the record already says its whereabouts in this continuity are unconfirmed. Nothing at the table has moved it. |
| **Campaign-specific limitations** | **Partly answered.** Siemhouk's bargain is the operative permission — access granted in exchange for fighting Zwuun. The `simulation.activationPolicy` of `gm-confirmed-only` still governs. Hukaa's objection and Karkus's counter-proposal remain unresolved in-fiction. |

## Sources
- Title: `artifacts/dark-lens.json`
  - Section: whole record, revision 1 · Source type: campaign record (read-only)
- Title: `plots/dark-lens.json`
  - Section: `unresolvedDetails[]`, `proposalConstraint`, `testimony[]`, revision 4 · Source type: campaign record (read-only)
- Title: Darkest Sun, s3 ep.13 "Marauders of Nibenay"
  - Section: Tithian's notes, Agis's proposal, Hukaa's objection, Karkus's counter-proposal
  - Source type: campaign-original (actual play, House Markon)
- Title: Darkest Sun, s3 ep.14 "Traders and Killers"
  - Section: the Agis/Sadira briefing, Melketh's account of the Lens, its obsidian core and the two-dwarves legend
  - Source type: campaign-original (actual play, House Markon)
- Title: Darkest Sun, s3 ep.19 "Bloody Red Oasis"
  - Section: the Siemhouk bargain and her Borys testimony, in-world day **113**
  - Source type: campaign-original (actual play, House Markon)
- Title: *Psionic Artifacts of Athas*
  - Section: "The Dark Lens", printed pages 7-8 · Source type: official-setting-source, already cited by the record
