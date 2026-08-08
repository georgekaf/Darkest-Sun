---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: gm
---

# Actor: The Moonbeast (bound entity beneath Kharanok)

*(New actor. **No record of this entity exists anywhere** — not in `mk-sandbox/actors/` (179 records), not in `Nominees/Actors/`, and not under any of the names the campaign has used for it. Verified 2026-08-09. Proposed id `actor-moonbeast`. It has been an active force in the campaign since ad4 with no record at all.)*

**Proposed sandbox field shape:**

- `actorType`: named-npc · `controlType`: autonomous · `factionId`: null
- `status`: active · `canonStatus`: campaign-original · `locationId`: `location-kharanok` — **confined to the caves beneath it**
- `simulation`: proposalMode **triggered** — it acts only when someone with a reachable mind enters the tunnels
- `campaignContinuity`: firstConfirmedDay **111** (ad4, through the gith captive), lastConfirmedDay **117**

## One-Sentence Summary
Something ancient and bound beneath Kharanok that was brought into this world to help and no longer wants to, that cannot leave the caves because old magic holds it there, and that reaches into the minds of everyone who comes down — hunting for one old miner in particular.

## Classification
- Subtype: named-npc — a singular entity, not a creature type
- Control: autonomous
- Status: **active and confined**
- Faction or allegiance: none
- Current location: the caves and tunnels beneath Kharanok (`location-kharanok`)
- Role: bound power, patron-or-predator depending on who is asked

## Player-Safe Description

### Appearance
It has no fixed form the party has seen. It builds a place to meet in out of the visitor's own memories — for Relo, a version of Kharanok that is never quite right, missing a whole staircase — and it wears a face taken from those memories. On day 117 it spoke with **Kalia's face**, the woman who had annoyed Relo that morning.

### Manner and Voice
Direct, transactional, and out of patience. It negotiates, it does not plead. It becomes physical the moment it is crossed.

### Public Reputation
None. The village does not know it exists. What is known is folklore: people who linger near the mine at night **hear voices, see the holes change size, and have visions** — that is Dorak's warning from ad2, and this is what it is describing.

## Confirmed Facts
- **ad4, day 111:** the captured gith describes an entity that entered his mind in the tunnels — a voice that called him **blessed** and urged him to follow it, telling him it was **"the moon"** that was calling him. He describes it as something that was always there, always good to the worthy among them, and wonders whether there is a deeper reason the party made Kharanok their own. **This is the campaign's first contact with it, and the source of the name.**
- **Earlier contact:** it visited the party in a shared dream — the "Shared Dream" of the day-110 campaign record — which is where Relo's memories of it come from.
- **ad7, day 117:** Relo reaches out with The Way for any activity akin to his own and touches it. He finds himself inside a Kharanok built from his own memories, which it is still getting wrong. It has considered his earlier proposal and **refuses it**.
- **ad7:** it tells him **the one it is looking for was there that day**, among the people in the mine, because that person **holds what keeps it bound**.
- **ad7:** it felt something else — that what was opened in the caves let an energy pass **through the gate**: something that constantly hunts people to replace its dead, that sounded like **the voices of thousands of dead**. It heard that once before, thousands of years ago and very far from here, and says **even it could not face that.** *(That is the [[The Caller in Darkness|Caller in Darkness]], described from the other side.)*
- **ad7:** it explains its own origin — it was **brought into this world to help**, when the creatures Relo calls Sorcerer Kings and Queens caused a great catastrophe that split the earth open and made black liquid well up. **It does not want to help. It wants to go back.**
- **ad7:** when Relo mentions a great walled city with undercities where a Sorcerer King lives who must die, it realises his mind is giving away more than he intended and he tries to shut it. **It lifts him into the air and pins him against the wall of the shade houses**, warning him that he came alone and opened his own mind of his own accord.
- **ad7:** its offer — *it will show him the road he must take, if he brings it what keeps it bound* — and the road runs **through where the energy came from**.

## Goals
1. Description: **Get free.** Someone bound it; it wants that undone.
   - Priority: 5 · Progress: it has found the holder's presence but not the holder · Secret: no — it says so plainly · Status: active
2. Description: **Go home.** It was brought here to help with a catastrophe it did not cause and has no interest in.
   - Priority: 5 · Progress: none · Secret: no · Status: active
3. Description: **Find [[Dorak]].** *(GM-only — it does not know the name.)*
   - Priority: 5 · Progress: it has felt him in the tunnels · Secret: **yes** · Status: active

## Traits and Pressures
- Ambition: Singular. One objective, held for thousands of years.
- Caution: None needed. It cannot be reached where it is.
- Loyalty: None. It was conscripted.
- Cruelty: **Instrumental.** It hurt Relo to make a point about consent, not to harm him.
- Risk tolerance: Total, within its cage.
- Safety: **Bound.** Old magic keeps it inside the caves under Kharanok.
- Status: The most powerful thing in Kharanok, and the least able to act on it.

## Resources and Capabilities
- **Psionic reach that the binding does not stop.** It cannot leave the caves; it can still enter the mind of anyone who comes down, and has done so to a gith captive and to Relo.
- **Constructed mindscapes** — it builds a meeting place from the visitor's memories, improving it as it gets more.
- **Faces taken from memory** — it appeared as Kalia.
- **Physical force inside its own construct** — it lifted and pinned Relo.
- **Age.** It recognised the Caller in Darkness from an encounter thousands of years ago and knew immediately it could not face it.

## Relationships
- Proposed actor ID: `actor-dorak`
  - Attitude: **Hunting him, and does not know his name**
  - Reason: **GM-only.** Dorak carries the lion's-head medallion that binds it. See [[Dorak]].
- Player character: **Relo** (Mpelos)
  - Attitude: **Bargaining partner, and warned once**
  - Reason: Two contacts. It offered him a road for its freedom, refused his earlier proposal, and pinned him to a wall when he tried to close his mind mid-conversation.
- Proposed actor ID: `actor-caller-in-darkness`
  - Attitude: **Recognises it and will not face it**
  - Reason: It heard the Caller thousands of years ago, far from here, and felt its energy come through the Kharanok gate on day 117. **Two ancient psionic entities are now aware of each other across a working gate.** See [[The Caller in Darkness]].
- **The captured gith** (ad4, released)
  - Attitude: **Recruited, or tried to**
  - Reason: Called him blessed and told him to follow. He believed it was benevolent.
- Proposed actor ID: `actor-breck`
  - Attitude: **Cannot detect him at all**
  - Reason: **GM-only.** Breck wears a [[Mind Seal]] — thoughts sealed, no telepathy in or out. The party suspects Breck of holding the binding; the creature that would know is the one being that cannot see him. Note the rule text allows a psionic creature to sense *that* a seal is present without seeing behind it, so what the moonbeast may perceive is a blank walking around its cage. **Open GM decision.** See [[Breck]].

## Knowledge
- Subject: Its own origin and binding
  - Claim: Brought here to help after the Sorcerer Kings' catastrophe split the earth and black liquid welled up; now held by old magic in these caves.
  - Source: itself · Learned day: told on 117 · Confidence: certain · Truth status: **its own account, uncorroborated** · Secret: no
- Subject: The Caller in Darkness
  - Claim: A thing that hunts people to replace its dead and sounds like thousands of dead voices; heard once thousands of years ago, far away; unfaceable.
  - Source: direct experience · Learned day: told on 117 · Confidence: certain · Truth status: **true — it matches the printed source exactly** · Secret: no
- Subject: Who holds its binding
  - Claim: That person was in the mine on day 117.
  - Source: its own sense · Learned day: 117 · Confidence: certain · Truth status: **true, and it is Dorak** · Secret: **the identity is GM-only; the claim itself was told to Relo**

## Current Activity
Confined beneath Kharanok, reaching into every usable mind that comes down, waiting for the one carrying its medallion to come close enough — which Dorak does almost daily.

## GM-Only Secrets
- **The binding is the lion's-head medallion Dorak carries** — an almost fire-red gemstone that also casts fireball. See [[Dorak]] GM-Only Secrets.
- **It is searching for Dorak specifically.** Not for a psionicist, not for the party — for the holder.
- **The old magic is the only reason this is not already a catastrophe.** Take the medallion to it and the cage question becomes live. The party has been offered exactly that trade and does not know what it would be handing over.
- Its account of itself — conscripted helper, wants only to go home — is **its own testimony and nothing else**. Whoever bound it presumably had a reason, and that reason is unwritten.
- The gith captive was told he was *blessed*. Relo was pinned to a wall. It calibrates to the listener.

## Proposed Developments
All unapproved.
- The party's plan runs straight through the misunderstanding: they are watching Breck while the holder loads their gate.
- **Two ancient entities, one gate.** The Caller reached Ranni at the far end on the same day this one felt the Caller at the near end. Nothing has been decided about whether they can reach each other.
- If it is ever freed, "it wants to go back" is a goal with no stated method — and the only known transport in the region is the plate Dorak operates.

## Stat Block or Rules Notes
- **None. Deliberately.** It has never been fought and should not be statted before that is a real prospect. What is established mechanically: it acts on minds, at will, within the caves; it can hold and move a person physically inside its own mindscape; and it cannot leave.
- Name: **"Moonbeast" is the campaign's working name**, derived from the gith captive's account of "the moon" calling him. It has never named itself.

## Sources
- Title: Darkest Sun Campaign Record — Day 110, "The Shared Dream"
  - Section: the dream visit
  - Printed page: —
  - Source type: campaign-history
  - Adaptation note: The source of Relo's memories that it later builds its mindscape from.
- Title: Darkest Sun — Altar of Dust, ad4 "It's Raining Bats and Bugs"
  - Section: the gith captive's interrogation — the voice that called him blessed, "the moon"
  - Printed page: —
  - Source type: campaign-original (actual play, in-world day **111**)
- Title: Darkest Sun — Altar of Dust, ad7 "City by the Silt Sea"
  - Section: Relo's second contact — the refusal, the origin account, the energy through the gate, the pinning, the offer
  - Printed page: —
  - Source type: campaign-original (actual play, 7 August 2026, in-world day **117**)
- Title: `obsidian/Hidden/Session prep/0007 - Session Prep 7-8-2026.md`
  - Section: Done; Left open — "The cave creature: is freeing it wise at all? Someone once decided it had to be bound."
  - Source type: GM record
- Title: GM disclosure, 2026-08-09
  - Section: the binding, the search for Dorak, the confinement
  - Source type: GM decision
  - Adaptation note: Establishes that the medallion is the binding, that Dorak holds it, that old magic confines the entity to the caves, and that its psionic reach is unaffected.

## Unresolved Questions
- **Who bound it, and why?** Prep 0007 asks the same thing: someone once decided it had to be bound.
- What it actually is. "Brought into this world to help" is its own word for itself.
- What "go back" means, and where back is.
- Whether it and the Caller in Darkness can reach one another through the gate now that both have noticed.
- Whether it can tell the difference between the holder of its binding and the binding itself — that is, whether Dorak is safe while he carries it, or only while he stays out of reach.
- **Has it noticed the blank?** [[Breck]]'s Mind Seal makes him undetectable, but the rule says a seal can be sensed as a seal. A hole that moves through a village every day is a thing an ancient mind might well have opinions about.
- What the campaign should call it in canon. **"Moonbeast" is a working name from a gith captive's mouth, not a fact.**
