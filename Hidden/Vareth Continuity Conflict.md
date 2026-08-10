---
entryType: history
entrySubtype: continuity-record
authorGM: "Ghost"
visibility: gm
---

# Historical Record: Vareth — the same character in two campaigns on the same day

## Subject and Period

- Subject: **Vareth** (player Giamicool, Human Preserver, student of Ragnis and Sandira) placed simultaneously in Zharvek and in Nibenay
- Exact day or approximate period: **day 116** (Macro 26th · al-Dun-Ak · eighth Or'Dom · Nar'Ai); the wider window runs 113–117
- Historical status: confirmed

*Identified during the continuity pass on the `s3 ep.20 - Rivers of Blood` summary (Markon). Resolved 2026-08-05.*

## Account

Vareth is played in both campaigns, and the two summaries placed him in incompatible locations on the same in-world days.

- **Altar of Dust — ad6:** days 113–114 resting at **Kharanok**; day 115 travelling south to **Zharvek**; **day 116** all day in the ruins with a night return — Vareth is explicitly in the marching order and in the fight with the earth spirit; day 117 at dawn, arrival back at Kharanok.
- **House Markon — s3 ep.20:** **day 116**, morning, Vareth presents himself at **Sandira's house inside Nibenay** and descends into the undercity the same day.

Two problems: the simultaneous presence on day 116, and — supposedly — the multi-day distance from Kharanok to Nibenay, which fitted nowhere in the chronology.

## Affected Elements

- Actors: Vareth; Agis (who moved him); Sandira (who summoned him); Ragnis
- Locations: `location-kharanok`, Zharvek, Nibenay (the undercity)
- Timelines: Altar of Dust (days 113–117) and House Markon (day 116) intersect
- Records: the ad6 summary and the s3 ep.20 summary

## Consequences Still Present

The ruling explains a sentence that was already in ad6 before anyone noticed the problem: *"exhausted — Vareth especially, completely spent from the day"*. He had worked a full day in the undercity of Nibenay before the night march even began.

The practical consequence that stays live: there is now a **same-day corridor between Kharanok and Nibenay** for anyone with access to Agis.

## Conflicting Accounts

- **ad6 (Altar of Dust):** Vareth present at Zharvek all of day 116, in the marching order and in the fight.
- **s3 ep.20 (House Markon):** Vareth in Nibenay on the morning of day 116, in the undercity the same day.
- Neither was wrong at the table. What was missing was the mechanism connecting them.

## Campaign Continuity Ruling

**RESOLVED (2026-08-05) — ruling by the campaign leader (Mikrokouneli): "Agis teleported him."**

Agis moved Vareth by teleport. That disposes of both problems:

1. **The distance stops mattering.** No travel window is needed, so no day has to shift in either campaign.
2. **Day 116 reconciles hour by hour.** Sandira sends word, Agis brings him to Nibenay in the morning, Vareth spends the day in the undercity with House Markon, and returns the same way before sundown — in time for the night march out of Zharvek.

**No date changed.**

What changed in the files:

- **The ad6 summary** — dates unchanged (115th/116th/117th). Date lines were added for days 116 and 117, which were missing (the rule requires a full line at every day change). One sentence was added to day 116 recording the absence and the teleport.
- **The s3 ep.20 summary** — one sentence added to the Sandira scene attributing his arrival to Agis's teleport.

## Player-Safe Version

Vareth was gone for a few hours during day 116 and returned before dusk, exhausted. Those with him at Zharvek did not see how he left or how he came back.

## GM-Only Notes

**Party membership, ruled 2026-08-11: after his appearance in Nibenay, Vareth is part of House Markon.** This is a transition rather than dual membership, so a single-valued `partyName` is sufficient and no schema change is needed. He still travels with the Altar of Dust party across days 115–117; that is an arrangement, not an allegiance.

**The teleport itself has not been fully explained by the Master GM.** The ruling establishes *that* Agis moved him and settles the placements. It does not establish how Agis does it, at what cost, how often he is willing to, or whether anyone else can ask. Record the placement as settled and the mechanism as unexplained — do not infer a spell, a range or a frequency from a single occurrence.

Date verification: the 15-day Or'Dom cycle was calculated from `athasian-draxian.json` (15 day names Nar-Ak … Dun-Keth, counted continuously, with no restart per Ai) and checked at three independent points: **day 113 → al-Qor-Traa** (ep.19), **day 115 → al-Qor-Keth** (ad6, as already written), **day 125 → al-Nar-Keth / ninth Or'Dom** (the table in the Draxian calendar terms). That file's `currentDate` shows day index 112 at 22:30 — the night of day 113, exactly where ep.19 closes.

Lines filled in on ad6:

| Day | Merchant | Draxian |
|---|---|---|
| 116th | Macro 26th | al-Dun-Ak, eighth Or'Dom, Nar'Ai |
| 117th | Macro 27th | al-Dun-Du, eighth Or'Dom, Nar'Ai |

Merchant month from `athasian.json`: Macro is the 4th month, days 91–120.

Things that were **not** conflicts:

- **Shaka / Cannibal King:** consistent across ad6 and ep.20 — master of Kharanok, sending messages to the gith.
- **Zharvek:** consistent across ep.19 (Talek Vos rides there over the gith unrest) and ad6 (sacked by gith, survivors remembering House Markon people passing through earlier). See [[Zharvek Continuity Conflict]].

## Sources

- Title: Darkest Sun, s3 ep.20 "Rivers of Blood"
  - Section: the Sandira scene; descent into the Nibenay undercity
  - Printed page: —
  - Source type: campaign-original (actual play, 5 August 2026)
  - Adaptation note: the House Markon side of the conflict.
- Title: Altar of Dust, ad6 "The Sand Also Rises"
  - Section: day 116 at Zharvek; the night march
  - Printed page: —
  - Source type: campaign-original (actual play, 31 July 2026)
  - Adaptation note: the Altar of Dust side of the conflict.
- Title: Campaign leader's ruling (Mikrokouneli)
  - Section: Campaign Continuity Ruling
  - Printed page: —
  - Source type: GM decision (2026-08-05)
  - Adaptation note: "Agis teleported him." No date changed.
- Title: GM ruling on party membership
  - Section: GM-Only Notes
  - Printed page: —
  - Source type: GM decision (2026-08-11)
  - Adaptation note: House Markon from day 116; a transition, not dual membership.
- Title: `athasian-draxian.json`, `athasian.json`, and the Draxian calendar terms
  - Section: calendar verification
  - Printed page: —
  - Source type: campaign reference data
  - Adaptation note: —

## Unresolved Questions

- **How does Agis's teleport actually work?** The Master GM has not explained it — no spell, cost, range or frequency is on record. Until that is answered, nothing should treat a same-day Kharanok↔Nibenay corridor as available.
- How often, and on what terms, is Agis willing to do this? If it is repeatable rather than a one-off favour, the geographic isolation of the two campaigns stops holding.
- Who else will ask for the same route once it becomes known?
- Does anyone at Zharvek know Vareth was gone, or did it pass unnoticed?
