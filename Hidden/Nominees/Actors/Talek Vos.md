---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: Talek Vos (update to existing actor-talek-vos, revision 2)

*(Revision of existing actor `actor-talek-vos`, currently at revision 1. Everything below is a change **against those values**. Revision 1 recorded a man riding toward Zharvek with three of its four facts unresolved; two of the three are now answered.)*

## Current record in mk-sandbox

*Read-only snapshot of `actors/talek-vos.json` (revision 1, updated 2026-08-04, event-traced to `event-day-0113-day-006`).*

| Field | Current value |
|---|---|
| `id` / `name` | actor-talek-vos / Talek Vos |
| `actorType` / `canonStatus` | named-npc / campaign-canon |
| `status` | **traveling** |
| `role` | Masked merchant-house envoy traveling toward Zharvek |
| `factionId` / `locationId` / `routeId` | null / null / null |
| `currentArea` | "Road toward Zharvek; later arrival not established" |
| `resources` | guards 6, ladenKanks 3 |
| `goals[]` | observe the gith unrest and report to his patron — priority 4, status **active** |
| `knowledge[]` | House Markon claims to have taken the Red Oasis — unverified, learned day 113 Day |
| `simulation.reason` | "Talek's arrival at Zharvek, patron, and report require later confirmed events." |
| `unresolvedDetails[]` | **identity of his house or patron** · meaning of the dragonfly banners · **whether he reached Zharvek** |

## Proposed changes

1. **His patron is House Shom.** `unresolvedDetails[0]` resolves. Propose `factionId: faction-house-shom` — he rides for the house, and revision 1 already records that he recognised House Markon from Doren's Nibenay entourage.
2. **He reached Zharvek.** `unresolvedDetails[2]` resolves. He arrived and was there when the settlement fell.
3. **He was taken alive on the night of day 114** by Silt Stalker raiders under **Luubarra Fire Dagger**, and is **imprisoned at Cromlin** for delivery to **Dregoth**.
4. **`status: traveling` → `captive`**, `locationId: null` → **`location-cromlin`**, `currentArea` rewritten.
5. **His goal fails.** He never observed the gith unrest and never reported. Propose `status: failed` with a completion note rather than deletion — the goal is why he was on that road.
6. **`simulation.reason` is now wrong.** Two of the three things it waits on have happened.

## One-Sentence Summary
A masked House Shom envoy who rode to Zharvek to look at gith trouble, found it, and was carried off by the pirates who were using it as cover — now a prisoner at Cromlin waiting to be handed to Dregoth.

## Classification
- Subtype: named-npc *(retained)*
- Status: **captive**
- Faction: **`faction-house-shom`**
- Current location: **`location-cromlin`**
- Role: House Shom envoy; now a held prisoner

## Player-Safe Description

### Appearance
*(Retained from revision 1.)* Slender and masked, seated on an elaborately decorated kank at the centre of a small guarded caravan, beneath **terracotta and beige dragonfly banners**.

### Public Reputation
An envoy of a merchant house, travelling with six guards and three laden kanks. He recognised House Markon on the road on day 113 and offered nothing about his own business.

## Confirmed Facts
- **Day 113** — sets out for Zharvek with **six guards** and three laden kanks to observe the gith unrest and report to his patron. *(ep.19.)*
- **His patron is House Shom.**
- **He reached Zharvek.**
- **Night of day 114** — taken alive when **Zarron's pirates**, the Silt Stalkers under Luubarra, empty the settlement under cover of the gith raiding.
- **Held at Cromlin**, for delivery to Dregoth. The rest of the Zharvek consignment has **already been delivered**; he and **Damak of Zharvek** are the two still held.
- **Nobody is looking for him yet.** **Vasara is dead** and cannot raise it. **Doren Shom will eventually wonder.** No day is set.

## Goals
1. Description: Observe the gith unrest around Zharvek and report its significance to his patron.
   - Priority: 4 · Progress: 0 · Target: 3 · Deadline day: none
   - Status: **failed** — completion note: *he reached Zharvek and was taken in the day 114 raid; no report was made.*
2. Description: Survive long enough to be ransomed, rescued, or found worth keeping.
   - Priority: 5 · Progress: 0 · Target: — · Secret: no · Status: active *(proposed)*

## Resources and Capabilities
- **guards 6** — *(status unrecorded. Nothing states whether they were killed, taken with him, or scattered. Not proposed either way.)*
- **ladenKanks 3** — *(likewise unrecorded, and worth something to whoever holds Cromlin's market.)*

## Relationships
- Faction: `faction-house-shom` — **his patron**
- Actor: `actor-doren-shom` — House Shom, Nibenay. **Will eventually wonder** why the envoy never reported
- Actor: `actor-vasara` — House Shom, **dead**; the person who might have raised it first, and cannot
- Actor: `actor-damak-of-zharvek` — **fellow prisoner**, held back from the same consignment
- Actor: `actor-luubarra-fire-dagger` · Faction: `faction-silt-stalkers` — **captors**

## Knowledge
- *(Retained.)* Subject `location-red-oasis` — House Markon claims to have taken the Red Oasis and offers it as a safe stop. Learned day 113, Day. Confidence 0.7, unverified.
  - **Note:** he is a captive and cannot report it. The claim is also false — the Red Oasis remains under covert Black Wake control.
- Subject: `location-zharvek`
  - Claim: what actually destroyed the settlement, and who did it.
  - Source: he was there. Learned day **114**. Confidence certain. Truth status **true**. Secret: no.

## Current Activity
Held at Cromlin.

## GM-Only Secrets
- **He is House Shom's problem before he is anyone's rescue.** An envoy of a great merchant house is a hostage with a price, not just a body for the pit — which may be exactly why he was held back while the villagers went forward.
- **The person best placed to notice is dead.** Vasara ran House Shom's ledgers and access in Nibenay and died in the undercity on day 118. Whatever she knew about a Zharvek-bound envoy died with her, unless it is in the **notebook of House Shom transactions House Markon now holds**.
- **Doren Shom is the one who eventually wonders**, and he is a bastard son trying to prove worth against legitimate siblings. A missing envoy is either a problem he solves visibly or a failure that lands on him.
- **His information completes the record.** The campaign's account has gith, and gith were genuinely raiding — but he was taken by **Zarron's pirates**, who moved under cover of that chaos. He is a literate envoy, not a frightened villager, and he can tell the two apart.

## Proposed Developments
All unapproved.
- Doren Shom notices. No day proposed.
- The dragonfly banners get explained by whoever holds his effects at Cromlin.
- Anyone following the Zharvek slaves finds him alive, or finds he has just been shipped.

## Sources
- Title: `actors/talek-vos.json`
  - Section: full entry, revision 1 · Source type: campaign record (read-only)
  - Adaptation note: The record this nominee revises.
- Title: Darkest Sun, s3 ep.19 "Bloody Red Oasis"
  - Section: roadside meeting with Talek Vos; he rides for Zharvek with six guards
  - Source type: campaign-original (actual play, in-world day **113**)
- Title: `locations/zharvek.json`
  - Section: `features[]` and `unresolvedDetails[]`, revision 8 · Source type: campaign record (read-only)
- Title: campaign owner ruling, 2026-08-13
  - Section: Talek Vos's fate, his House Shom patron, the day 114 Night timestamp, and who eventually looks for him
  - Source type: GM input
  - Adaptation note: Entered through MK-Sandbox #189. No confirmed event record is claimed here.
