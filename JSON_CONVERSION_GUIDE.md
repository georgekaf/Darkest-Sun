# Darkest Sun.json → Obsidian: Conversion Guide

Reference for re-running the JSON-to-Obsidian conversion when the source file is updated.

---

## 1. What Comes from the JSON vs What Doesn't

### Auto-generated (safe to overwrite on re-run)

These folders are fully sourced from `Darkest Sun.json`. Overwrite freely:

| Folder / File | Contents |
|---|---|
| `Classes/` | Bard, Bounty Hunter, Druid, Fighter, Gladiator, Necromancer, Priest, Psionicist, Ranger, Thief, Wizard |
| `Rules/` | Hex Crawling, Conditions, Ancestries, Alignment, Luck Tokens, Poisons, Downtime, Food & Water, Vision & Darkness, Βασικοί Όροι, Δημιουργία Χαρακτήρων, Μάχη, Shadowdark RPG, etc. |
| `The World/` | 21 Greek lore files: Ιστορία, Μαγεία, Psionics, Οι Πόλεις-Κράτη, Cosmology, Athasian Calendar, etc. |
| `Journal/` | 25+ session files (01. FREEDOM … 25. Black Wind Fire and Steel), written in Greek |
| `Map/` | Location stubs: City-States, Forts, Settlements, Battle of the Orb |
| `Kharanok- The Altar of Dust/` | Campaign location and sub-pages |
| `Languages/` | Language reference pages |
| `Campaign Map/` | Map resource pages |
| `Darkest Main.md` | Root campaign page |
| `Downtime Activities.md` | Standalone rule page |
| `Timeline.md` | Campaign timeline |
| `Character - Soldier.md` | NPC/character reference |
| `Misery.md` | Rule/mechanic page |
| `Mounts.md` | Rule/mechanic page |
| `Untitled.md` | Empty resource from JSON |

### Manually maintained — DO NOT overwrite

These folders were built by hand from the PDF boxed set. The JSON export does not contain them:

| Folder | Contents | Notes |
|---|---|---|
| `NPCs/` | 34 named characters from *City by the Silt Sea* | Role, Location, Page refs, Agenda, Relationships per file |
| `Monsters/` | Caller in Darkness, Dray, Fire Dagger Clan, Spirit of Kragmorta, Taraskir the Lion, Πλάσματα της Ερήμου | Separated from NPCs; Πλάσματα της Ερήμου is a Greek bestiary |
| `BookLocations/` | All named locations from the campaign book | Cromlin, Giustenal districts, Kragmorta, Blasted Spire, etc. |

---

## 2. The Conversion Script

Script lives at:
```
outputs/json_to_obsidian.py
```

Copy it to a working directory before running. Key constants at the top:

```python
SRC   = Path(".../Darkest Sun.json")   # source export
VAULT = Path(".../obsidian")           # target vault
```

### What it does

1. **Blanks all existing `.md` files** in the vault (can't delete on Windows-mounted fs from Linux — blanking is the workaround). This hits ALL folders including manually-maintained ones — see section 3.
2. Parses the JSON `resources` array and builds a `parentId` tree.
3. Converts each resource's ProseMirror document to Markdown via `n2md()`.
4. Writes `YAML frontmatter` + body + child wikilinks to each file.
5. Places files: resources with children → `folder/name.md`; leaves → `parent/name.md`.
6. Skips resources with `parentId == "templates"`.

### ProseMirror node types handled

`doc`, `paragraph`, `heading`, `bulletList`, `orderedList`, `listItem`, `blockquote`, `rule`, `hardBreak`, `panel` (→ Obsidian callout), `table` (with header separator), `taskList` (→ `- [ ]` / `- [x]`), `mediaSingle`/`media` (→ image embed), `mention` (→ inline code), `layoutSection`/`layoutColumn` (transparent wrappers), `extension`/`bodiedExtension`/`inlineExtension` (skipped).

Marks handled: `strong` → `**`, `em` → `*`, `underline` → `<u>`.

---

## 3. Safe Re-run Procedure

**Critical:** The script's blanking step will wipe manually-maintained folders. Follow this order exactly.

### Step 1 — Back up manually-maintained folders

Before running the script, copy these three folders out of the vault:

```
obsidian/NPCs/          → backup/NPCs/
obsidian/Monsters/      → backup/Monsters/
obsidian/BookLocations/ → backup/BookLocations/
```

Or on Windows, just copy the whole vault folder first.

### Step 2 — Update the script's SRC path

Point `SRC` at the new `Darkest Sun.json`.

### Step 3 — Modify the blanking loop to skip protected folders

Replace the blanking loop in the script with this version:

```python
PROTECTED = {"NPCs", "Monsters", "BookLocations", "greek"}

for p in VAULT.rglob("*.md"):
    rel = p.relative_to(VAULT)
    parts = rel.parts
    if any(part == '.obsidian' for part in parts):
        continue
    if parts[0] in PROTECTED:
        continue   # skip manually-maintained folders and all Greek translations
    p.write_text("", encoding="utf-8")
    blanked += 1
```

### Step 4 — Run the script

```bash
python3 json_to_obsidian.py
```

### Step 5 — Post-conversion checks

After the script runs, verify:

- `Journal/` has all sessions (count should match the new export)
- `The World/` has expected lore files
- `Classes/` has all class files
- `Rules/` looks complete
- `NPCs/`, `Monsters/`, `BookLocations/` are untouched

### Step 6 — Apply grammar fixes

Re-run `fix_grammar.py` (or an updated version) on the vault. The JSON content consistently has these issues that need patching:

- Greek accents: `ειναι` → `είναι`, `ηταν` → `ήταν`, `οτι` → `ότι`
- Greek article errors: `τη ` before vowels should be `την `
- AI-leaked text at end of `Μάχη.md` and `Βασικοί Όροι.md` — remove lines starting with "Αν θες, μπορώ να"
- Empty headings (lines with only `## ` or `### `)
- Bold marker artifacts (`** **`, `****`)

### Step 7 — Review Journal #7 (NIGHT RAID)

This session file was written in the source without Greek diacritics throughout. Needs manual accent restoration — programmatic fixing risks wrong placements.

---

## 4. Greek Translations of Protected Pages

There is a single top-level `greek/` folder at the vault root that mirrors the structure of the manually-maintained folders. English originals live in their normal locations; Greek translations live under `greek/` in matching subfolders.

### Folder structure

```
obsidian/
├── NPCs/
│   └── Dregoth.md                   ← English
├── Monsters/
│   └── Caller in Darkness.md        ← English
├── BookLocations/
│   └── Cromlin.md                   ← English
├── Kharanok- The Altar of Dust/
│   └── Kharanok- The Altar of Dust.md  ← English
└── greek/
    ├── NPCs/
    │   └── Dregoth.md               ← Greek translation
    ├── Monsters/
    │   └── Caller in Darkness.md    ← Greek translation
    ├── BookLocations/
    │   └── Cromlin.md               ← Greek translation
    └── Kharanok- The Altar of Dust.md  ← Greek (location files sit directly in greek/)
```

### Linking convention

Every English page must end with:

```markdown
---
*Ελληνική έκδοση: [[greek/PageName]]*
```

Every Greek page must end with:

```markdown
---
*English version: [[PageName]]*
```

Because Obsidian resolves wikilinks by filename, the bare `[[PageName]]` in a Greek file links to the English original without needing a folder prefix. Only use full relative paths if two files share the same filename across folders.

### When adding a new page to a protected folder

1. Create the English page in its content folder.
2. Create the Greek translation in the matching `greek/` subfolder with the same filename.
3. Add the cross-links at the bottom of both files.
4. Add entries to both the English index and the Greek index under `greek/`.

### On re-run

The `greek/` folder is not generated by the JSON script, so it is never blanked. However, add it explicitly to the `PROTECTED` set in the blanking loop just in case:

```python
PROTECTED = {"NPCs", "Monsters", "BookLocations", "greek"}
```

---

## 5. JSON Structure Reference

```
Darkest Sun.json
└── resources: [...]        # flat array of all pages
    ├── id                  # UUID
    ├── name                # page title
    ├── parentId            # UUID of parent, or "" for root, or "templates" (skip)
    ├── tags: [...]         # string array → YAML tags
    ├── iconGlyph           # emoji or icon → YAML icon field
    └── documents: [...]    # array; use documents[0].content (ProseMirror doc node)
```

Folder hierarchy is reconstructed by following `parentId` chains recursively. Resources that have children in the tree become `folder/name.md` so sibling files can nest alongside them.

---

## 6. Known Limitations

- **No file deletion from Linux bash on NTFS mount** — blanking (`write_text("")`) is used instead of `unlink()`. Old files from removed resources become empty. After a re-run, manually delete empty `.md` files in Windows Explorer or PowerShell:
  ```powershell
  Get-ChildItem -Path "obsidian" -Filter "*.md" -Recurse |
    Where-Object { $_.Length -eq 0 } | Remove-Item
  ```
- **Image embeds** — `mediaSingle`/`media` nodes emit `![](<url>)` with the original Confluence/Notion URL. Images are not downloaded. If the source app changes URLs, embeds break.
- **Extension nodes skipped** — any Confluence/Notion-specific extension blocks (macros, smart links, etc.) produce no output. Content in those blocks is lost.
- **Filenames with special characters** — `sanitize()` replaces `<>:"/\|?*` with `-`. Greek filenames are preserved as-is (UTF-8 supported by Obsidian).
