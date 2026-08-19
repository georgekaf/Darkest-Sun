---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Vasara (update to existing actor-vasara, revision 4)

*(Revision of existing actor `actor-vasara`, currently at revision 3. **She is dead.** The record carries her as `status: active` with two live goals and a deadline of day 111. This revision is independent of the Zharvek ruling — she died in play, in episode 22, and the record simply has not caught up.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/vasara.json` (revision 3, updated 2026-08-09, event-traced through `event-day-0117-dusk-008`).*

| Field | Current value |
|---|---|
| `id` / `name` | actor-vasara / Vasara |
| `status` | **active** |
| `role` | House Shom agent and keeper of the sealed undercity agreement |
| `factionId` / `locationId` | faction-house-shom / location-nibenay |
| `currentArea` | "House Shom access route in Nibenay" |
| `goals[]` | recover the sealed agreement rod (deadline day 111) · receive House Shom's fifty-percent share — **both active** |
| `relationships` | `actor-doren-shom` +1, `actor-utopi` 0, `actor-thymios` 0 |
| `campaignContinuity` | firstConfirmedDay 110, lastConfirmedDay 111 |
| `unresolvedDetails[]` | her reaction to Utopi's touch · whether she accepts Thymios's invitation · her response to the rod · accounting of the tombs' gold |
| `psionicStatus` | non-psionic |

## Proposed changes

1. **`status: active` → `dead`.** Killed on **day 118** in the undercity beneath Nibenay's Sages' District.
2. **She turned on House Markon first.** This is not a death to record quietly — she attempted to have a party member killed and died in the fight she started.
3. **Both goals close as failed**, and the day-111 deadline on the first is long past.
4. **Two `unresolvedDetails` become permanently unanswerable** and should be marked so rather than deleted: her reaction to Utopi's touch, and whether she accepts Thymios's invitation. Nobody can now answer either.
5. **Her effects passed to House Markon** — including a notebook of House Shom's transactions with separate notes she kept on Doren Shom. That is a live consequence for `actor-doren-shom` and `faction-house-shom`, not loot trivia.
6. **`campaignContinuity.lastConfirmedDay` 111 → 118.**

## One-Sentence Summary
The House Shom agent who sold House Markon access to the undercity, decided they were frauds she had been exploiting, ambushed them on the stairs with seven guards to buy the death of Hukaa, and was killed there.

## Classification
- Subtype: named-npc *(retained)*
- Status: **dead**, day 118
- Faction: `faction-house-shom` *(retained)*
- Last location: the undercity stair beneath the guarded abandoned house, Sages' District, Nibenay
- Role: House Shom agent and keeper of the sealed undercity agreement — **ended**

## Confirmed Facts

**Before the break** *(retained from revision 3)* — she recorded the undercity agreement on a sealed agafari-wood rod granting House Shom fifty percent of gold found; she opened the House Shom route into old Nibenay on days 111 and 117 and warned that the entrance locks in the evening.

**Day 118** *(ep.22, "Some truths are better left buried")*:

- Morning, at the Shom residence, she reports a rumour that **preservers have appeared in Nibenay**, detectable by the effects of their magic rather than the casting, and that the templars have tightened their checks.
- She offers to come down into the undercity herself; the exchange turns into an open quarrel. **She never once calls Hukaa by name — only "the elf"** — and dismisses her as a dowry bride from House Stel. Ougk threatens her; Doren arrives and, when Hukaa says she would rather deal with someone else, tells Vasara to go.
- Banga-Ranga follows her to the storeroom she uses as an office and negotiates. Vasara names her price for gladiators: **a week to assemble them, ten to fifteen gold each**. Then she says the real thing: **she knows they are warriors and not merchants, they have never registered a single caravan, and she has been exploiting them for exactly that reason.**
- **She hands over the metal key** to the lower city and withdraws her supervision, on the terms that they keep playing the role and keep bringing her the take.
- **On the stair she is waiting for them, armed, with seven guards in formation.** She had intended to end the arrangement on her own terms once she was rich enough. **She offers Ougk his life, fame and glory for the head of "the blonde elf".**
- **Ougk kills her** with the Scourge — the runes on the blade lighting as her last breath goes. **Two guards run and are hunted down before the exit; all seven die.** The bodies are stacked in a corner of the undercity.
- **Taken from her body:** a **potion of giant strength**, and a **notebook recording every House Shom transaction, with separate notes she had been keeping on Doren Shom**.
- **She appears to have brought nobody else.** The party surfaced at midday carrying three unconscious companions through the Sages' District and waited until dusk to move.

## Goals
1. Recover or secure the sealed agreement rod — **failed** (deadline day 111, dead day 118).
2. Receive House Shom's fifty-percent share of gold recovered from the undercity — **failed**.
3. *(Recorded for the history, not as a live goal.)* End the House Markon arrangement on her own terms once she had taken enough from it, buying Hukaa's death on the way out — **failed, and fatal.**

## Relationships
- `actor-doren-shom` +1 → **ended.** He had defended her as a partner rather than a subordinate hours before she died. **He does not know**, and her private notes on him are now in House Markon's hands.
- `actor-utopi` 0 *(retained; the reaction to his touch is now unanswerable)*
- `actor-thymios` 0 *(retained; the invitation is now moot)*
- `actor-hukaa` — **hostile.** She contracted for her head
- `actor-ougk` — **killed by**
- `actor-banga-ranga` — the last person she negotiated with, and the one she gave the key to

## Knowledge
*(Retained.)* `location-nibenay` — House Shom has a concealed undercity entrance beneath an abandoned Sages' District building. Confidence 1, true, secret. **The secret did not die with her: the key and the access are now House Markon's.**

## GM-Only Secrets
- **House Shom is missing an agent and does not know why.** She died underground with seven guards, and the bodies were hidden rather than found. Whoever eventually asks starts from a disappearance, not a murder.
- **The notebook is the real inheritance.** Every House Shom transaction, plus what she was privately compiling on Doren Shom. It is leverage over Doren, evidence against him, or both, depending on who reads it.
- **She was right about them.** They are not merchants and have never registered a caravan. The observation is now in a notebook that other people can also read.
- **Talek Vos is a House Shom envoy who never came home**, and she was among the people best placed to notice. She cannot. See #189.

## Proposed Developments
All unapproved.
- Someone at House Shom counts heads. The undercity is the last place she was seen going.
- Doren Shom learns what she was keeping on him — from the notebook, or from whoever else has read it by then.
- The party holds the key, the access and the arrangement, with nobody left to enforce the fifty percent.

## Sources
- Title: `actors/vasara.json`
  - Section: full entry, revision 3 · Source type: campaign record (read-only)
  - Adaptation note: The record this nominee revises.
- Title: Darkest Sun, s3 ep.22 "Some truths are better left buried"
  - Section: the morning quarrel, the storeroom negotiation, the ambush on the stair, and the aftermath
  - Source type: campaign-original (actual play, in-world day **118**)
  - Adaptation note: The source of everything in *Confirmed Facts* under day 118.
- Title: Darkest Sun, s3 ep.23 "Broken Promises"
  - Section: Hukaa on the undercity fight
  - Source type: campaign-original
  - Adaptation note: Corroborates the death in passing — *"she would have rotted down in the undercity along with Vasara."*
