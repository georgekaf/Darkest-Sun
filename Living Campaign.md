---
title: "Living Campaign"
icon: "file-lines"
---
# Guest GM Entry Guidelines

Guest GMs should submit **structured Markdown proposals**, not edit the canonical JSON directly. The repository treats its JSON actor, faction, location, route, artifact, plot, action, market, history, and event files as authoritative world state, while Markdown is primarily used for human review and reporting.

## Core submission rules

1. **Every guest submission begins as a proposal.**  
    Only the campaign owner can approve it as canon.
    
2. **One primary entry per Markdown file.**  
    One actor, location, faction, route, artifact, plot, and so on. The canonical repository follows the same one-element-per-file principle.
    
3. **Separate three kinds of information:**
    
    - table-confirmed facts;
        
    - previously established campaign facts;
        
    - new proposals, secrets, or possible consequences.
        
4. **Do not invent chronology.**  
    Use only confirmed campaign days and watches. Leave the watch unknown when the session only established the day.
    
5. **Mark secrets clearly.**  
    Every file uses `visibility: gm`, `player-safe`, or `mixed`.
    
6. **Provide sources.**  
    Published material should be paraphrased and cite the title, section, and printed pages. Campaign-original material should name the contributing GM and relevant session.
    
7. **Preserve Darkest Sun continuity.**  
    Campaign rulings override published adventure assumptions.
    

## Supported entry types

The pack includes guidelines, blank templates, and filled samples for:

- **Actor**
    
    - named NPC
        
    - autonomous group
        
    - creature group
        
    - agent
        
    - player character
        
- **Faction**
    
- **Location**
    
- **Route**
    
- **Artifact**
    
- **History**
    
- **Plot**
    
- **Campaign Resources**
    

The current actor model supports `named-npc`, `group`, `creature-group`, and `agent`, with statuses such as active, traveling, captured, hidden, inactive, and dead. Player characters are represented as non-autonomous actors controlled through table play.

Locations may represent city-states, villages, outposts, oases, ruins, mines, forts, tribal camps, regional nodes, or underground complexes. Resources should only be recorded when they can create decisions or consequences.

## Embedded records

These normally belong inside another entry rather than having separate files:

- goals;
    
- clocks;
    
- knowledge;
    
- rumors;
    
- relationships;
    
- resources;
    
- current actions;
    
- route conditions;
    
- source references.


```markdown
---
entryType: actor
entrySubtype: named-npc
authorGM: "Ghost"
visibility: mixed
---

# Actor: [Name]

## One-Sentence Summary

## Classification

- Subtype: named-npc | group | creature-group | agent | player-character
- Control: autonomous | faction-directed | player-character
- Status: active | traveling | recovering | captured | missing | hidden | inactive | dead
- Faction or allegiance:
- Current location:
- Current route, when traveling:
- Role:

## Player-Safe Description

### Appearance

### Manner and Voice

### Public Reputation

## Confirmed Facts

State only table-confirmed or already established campaign facts.

## Goals

List one to three goals for an active autonomous actor.

1. Description:
   - Priority: 1-5
   - Progress:
   - Target:
   - Deadline day:
   - Secret: yes/no
   - Status: active

## Traits and Pressures

- Ambition:
- Caution:
- Loyalty:
- Cruelty:
- Risk tolerance:
- Safety:
- Wealth:
- Status:

## Resources and Capabilities

## Relationships

- Existing actor or faction ID:
  - Attitude:
  - Reason:

## Knowledge

- Subject:
  - Claim:
  - Source:
  - Learned day:
  - Confidence:
  - Truth status:
  - Secret: yes/no

## Current Activity

## GM-Only Secrets

## Proposed Developments

Clearly label all unapproved material.

## Stat Block or Rules Notes

Optional. State the rules system and version.

## Sources

- Title:
  - Section:
  - Printed page:
  - Source type:
  - Adaptation note:

## Unresolved Questions
```



```markdown
---
entryType: faction
entrySubtype: organization
authorGM: "Ghost"
visibility: mixed
---

# Faction: [Name]

## Summary

## Classification

- Faction type:
- Status:
- Headquarters:
- Operational region:
- Leadership:

## Player-Safe Description

## Doctrine

## Confirmed Assets

Describe only assets that create strategic choices.

- Territory:
- Influence:
- Wealth:
- Agents:
- Military:
- Intelligence:
- Trade access:
- Water access:

## Limitations and Internal Problems

## Goals

1. Description:
   - Priority: 1-5
   - Progress:
   - Target:
   - Deadline:
   - Secret: yes/no
   - Status:

## Agents and Member Groups

## Relationships

## Faction Clocks

## GM-Only Secrets

## Proposed Reactions

## Sources

## Unresolved Questions
```


```markdown
---
entryType: location
entrySubtype: settlement
authorGM: "Ghost"
visibility: mixed
---

# Location: [Name]

## Summary

## Classification

- Location subtype:
- Region:
- Terrain:
- Parent location:
- Coordinates or map reference:
- Status:
- Controller:
- Contested by:

## Player-Safe Arrival Description

## Physical Features

## Population and Occupants

## Resources

Track only resources that create decisions.

- Water:
- Food:
- Trade:
- Verdance:
- Guards:
- Other:

## Important Areas

## Important Actors and Factions

## Dangers

## Opportunities

## Connections

- Destination:
  - Existing location ID:
  - Existing route ID:
  - Travel notes:

## Local Clocks and Pressures

## GM-Only Secrets

## Proposed Developments

## Sources

## Unresolved Questions
```

```markdown
---
entryType: artifact
entrySubtype: relic
authorGM: "Ghost"
visibility: mixed
---

# Artifact: [Name]

## Summary

## Status and Custody

- Status:
- Current location:
- Owner or bearer:
- Keyed to:
- Last confirmed day:

## Player-Safe Description

## Materials and Construction

## Known Powers

## Activation

## Costs, Risks, and Limitations

## Interested Actors and Factions

## Knowledge Partitions

State separately what each actor or faction knows.

## GM-Only Truth

## Proposed Developments

## Sources

## Unresolved Questions
```

```markdown
---
entryType: history
entrySubtype: continuity-record
authorGM: "Ghost"
visibility: mixed
---

# Historical Record: [Name]

## Subject and Period

- Subject:
- Exact day or approximate period:
- Historical status: confirmed | disputed | adapted | unknown

## Account

## Affected Elements

## Consequences Still Present

## Conflicting Accounts

## Campaign Continuity Ruling

Leave blank when the campaign owner has not ruled.

## Player-Safe Version

## GM-Only Notes

## Sources

## Unresolved Questions
```

```markdown
---
entryType: plot
entrySubtype: campaign-thread
authorGM: "Ghost"
visibility: gm
---

# Plot: [Name]

## Premise

## Status

- Dormant | active | stalled | resolved | failed | abandoned
- First possible activation day:
- Current confirmed phase:

## Confirmed Current State

## Involved Elements

- Actors:
- Factions:
- Locations:
- Routes:
- Artifacts:
- Markets:

## Activation Hooks

## Phases

1. Phase:
   - Pressure:
   - What may happen without intervention:
   - Player-facing decision:
   - Status:

## Secret Truths

## Clocks

## Possible Outcomes

Keep all future outcomes conditional and unresolved.

## GM Attention Required

## Sources

## Unresolved Questions
```