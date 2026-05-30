# Guide to Shadowdark Monster Statistics
*By Matt Dietrich*

---

## Quick Combat Statistics

| LV | AC | HP  | ATK                    | Stat Mod Median [Low, High] | Effect DC |
|----|----|-----|------------------------|-----------------------------|-----------|
| 0  | 11 | 1   | 1 attack +1 (1)        | -2 [-4, 1]                  | 9         |
| 1  | 12 | 4   | 1 attack +1 (1d4)      | +0 [-2, 1]                  | 12        |
| 2  | 12 | 10  | 1 attack +2 (1d6)      | +0 [-2, 2]                  | 12        |
| 3  | 13 | 14  | 2 attacks +3 (1d6)     | +1 [-2, 2]                  | 12        |
| 4  | 13 | 19  | 2 attacks +3 (1d6)     | +1 [-2, 3]                  | 12        |
| 5  | 13 | 24  | 2 attacks +4 (1d8)     | +1 [-2, 3]                  | 15        |
| 6  | 14 | 29  | 3 attacks +5 (1d10)    | +1 [-2, 4]                  | 15        |
| 7  | 14 | 34  | 3 attacks +6 (1d10)    | +1 [-1, 4]                  | 15        |
| 8  | 14 | 38  | 3 attacks +6 (1d10)    | +1 [-1, 4]                  | 15        |
| 9  | 15 | 43  | 3 attacks +7 (2d8)     | +2 [-1, 5]                  | 15        |
| 10 | 15 | 48  | 3 attacks +7 (2d8)     | +2 [-1, 5]                  | 15        |
| 11 | 15 | 52  | 3 attacks +8 (2d8)     | +3 [1, 5]                   | 15        |
| 12 | 16 | 58  | 3 attacks +8 (2d10)    | +3 [2, 5]                   | 15        |
| 13 | 16 | 61  | 4 attacks +8 (2d10)    | +3 [2, 5]                   | 15        |
| 14 | 16 | 68  | 4 attacks +9 (2d10)    | +3 [3, 5]                   | 15        |
| 15 | 17 | 70  | 4 attacks +9 (2d10)    | +3 [3, 5]                   | 18        |
| 16 | 17 | 76  | 4 attacks +10 (2d12)   | +4 [3, 6]                   | 18        |
| 17 | 17 | 80  | 4 attacks +10 (2d12)   | +4 [3, 6]                   | 18        |
| 18 | 18 | 85  | 4 attacks +10 (2d12)   | +4 [3, 6]                   | 18        |
| 19 | 18 | 89  | 4 attacks +10 (2d12)   | +4 [3, 6]                   | 18        |
| 30 | 22 | 140 | 5 attacks +13 (3d10)   | +4 [3, 7]                   | 18        |

---

## Measuring Stick Monster Stat Modifiers

| Category    | Variant       | Sample Monster    | Stats                                      |
|-------------|---------------|-------------------|--------------------------------------------|
| Beast       | —             | Giant Rat         | S-2 D+1 C+1 I-2 W+1 Ch-2                  |
|             | Agile         | Panther           | D+4                                        |
|             | Tough         | Tyrannosaurus     | S+5 C+4                                    |
| Celestial   | —             | Seraph            | S+3 D+1 C+1 I+2 W+3 Ch+3                  |
|             | Powerful      | Archangel         | S+5 D+2 C+4 I+4 W+5 Ch+5                  |
| Construct   | —             | Stone Golem       | S+4 D-1 C+4 I-2 W+0 Ch-2                  |
| Dragon      | —             | Forest Dragon     | S+4 D+3 C+4 I+3 W+3 Ch+4                  |
|             | Powerful      | Fire Dragon       | S+6 D+5 C+4 I+4 W+4 Ch+5                  |
|             | Unintelligent | Wyvern            | I-3 W+1 Ch-3                               |
| Elemental   | —             | Water Elemental   | S+4 D+2 C+2 I-2 W+1 Ch-2                  |
|             | Incorporeal   | Shadow            | S-2                                        |
|             | Intelligent   | Djinni            | I+4 W+3 Ch+3                               |
|             | Mobile        | Air Elemental     | D+5                                        |
|             | Tough         | Earth Elemental   | S+5 C+4                                    |
| Fey         | —             | Dryad             | S-1 D+2 C+1 I+1 W+3 Ch+4                  |
| Fiend       | —             | Barbed Devil      | S+2 D+3 C+1 I+1 W+1 Ch+1                  |
|             | Powerful      | Balor             | S+6 D+2 C+5 I+4 W+3 Ch+4                  |
|             | Tiny          | Imp               | S-2                                        |
| Giant       | —             | Hill Giant        | S+4 D+0 C+3 I-2 W-2 Ch-2                  |
|             | Powerful      | Storm Giant       | S+6 D+2 C+4 I+3 W+4 Ch+4                  |
| Humanoid    | —             | Bandit            | S+1 D+0 C+0 I-1 W+0 Ch-1                  |
|             | Agile         | Assassin          | D+4                                        |
|             | Intelligent   | Archmage          | I+4 W+2 Ch+1                               |
|             | Tough         | Knight            | S+3 C+1                                    |
| Monstrosity | —             | Ankheg            | S+2 D+2 C+1 I-2 W+1 Ch-2                  |
|             | Intelligent   | Sphinx            | I+4 W+4 Ch+3                               |
|             | Mobile        | Harpy             | D+3                                        |
|             | Powerful      | Kraken            | S+6 D+3 C+4 I+4 W+3 Ch+4                  |
|             | Tough         | Owlbear           | S+4 C+3                                    |
| Ooze        | —             | Gray Ooze         | S+1 D+1 C+0 I-4 W-3 Ch-4                  |
|             | Tough         | Black Pudding     | S+2 C+3                                    |
| Plant       | —             | Rot Flower        | S+1 D-3 C+1 I-4 W-3 Ch-4                  |
|             | Powerful      | Treant            | S+4 D-1 C+2 I+2 W+3 Ch+1                  |
| Undead      | —             | Ghoul             | S+2 D+1 C+2 I-3 W-1 Ch+0                  |
|             | Incorporeal   | Ghost             | S-2                                        |
|             | Mobile        | Wraith            | D+4                                        |
|             | Powerful      | Lich              | S+3 D+1 C+4 I+4 W+3 Ch+3                  |

---

## Using the Measuring Stick Monster Chart

1. Identify the general monster **Category**
2. Use baseline modifiers for that Category
3. *(Optional)* Apply one or more **Variants**

**Categories:** Beast · Celestial · Construct · Dragon · Elemental · Fey · Fiend · Giant · Humanoid · Monstrosity · Ooze · Plant · Undead

**Variants:**
- **Agile** = Higher DEX
- **Incorporeal** = Lower STR
- **Intelligent** = Higher INT/WIS/CHA
- **Mobile** = Higher DEX
- **Powerful** = Higher all
- **Tiny** = Lower STR
- **Tough** = Higher STR/CON
- **Unintelligent** = Lower INT/WIS/CHA

---

*Guide to Shadowdark Monster Statistics is an independent product published under the Shadowdark RPG Third-Party License and is not affiliated with The Arcane Library, LLC. Shadowdark RPG © 2023 The Arcane Library, LLC.*
