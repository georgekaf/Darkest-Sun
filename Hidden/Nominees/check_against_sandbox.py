"""Compare nominee markdown against mk-sandbox actor records (READ-ONLY).

Emits a review report: which nominees correspond to an existing record, whether
they mislabel themselves as NEW, whether the id they propose matches the real
one, and what the existing record already contains.
"""
import glob
import json
import os
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = "K:/Darkest Sun"
NOM = ROOT + "/obsidian/Hidden/Nominees/Actors"
SB = ROOT + "/mk-repos/mk-sandbox/actors"
OUT = ROOT + "/obsidian/Hidden/Nominees/_sandbox-comparison.md"

STOP = {"the", "of", "a", "an"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "", s)


def tokens(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return {t for t in re.split(r"[^a-z0-9]+", s) if t and t not in STOP}


records, by_key, by_tokens = {}, {}, []
for p in sorted(glob.glob(SB + "/*.json")):
    slug = os.path.splitext(os.path.basename(p))[0]
    d = json.load(open(p, encoding="utf-8"))
    records[slug] = d
    keys = {slug, d.get("id", ""), d.get("name", "")}
    keys |= {str(v) for v in (d.get("aliases") or [])}
    keys |= {str(v) for v in (d.get("titles") or [])}
    for k in keys:
        if k:
            by_key.setdefault(norm(k), slug)
            by_key.setdefault(norm(re.sub(r"^actor-", "", k)), slug)
    by_tokens.append((slug, tokens(d.get("name", slug)) | tokens(slug)))

rows = []
for p in sorted(glob.glob(NOM + "/*.md")):
    base = os.path.splitext(os.path.basename(p))[0]
    text = open(p, encoding="utf-8").read()
    declared = (re.findall(r"`(actor-[a-z0-9\-']+)`", text) or [None])[0]
    is_update = bool(re.search(
        r"Update to existing actor|Revision of existing actor|update to existing actor-",
        text, re.I))

    slug = None
    for cand in (base, declared or "", re.sub(r"^The\s+", "", base),
                 base.split(" the ")[0], base.split(",")[0]):
        k = norm(re.sub(r"^actor-", "", cand))
        if k in by_key:
            slug = by_key[k]
            break
    # No fuzzy fallback: partial token overlap produced false positives
    # (e.g. "Chieftain of the Eye" -> "Jorath Chain-Eye", a Nibenay slave
    # hunter; "Chieftain of the Hand" -> "Korrun Sap-Hand", an agafari cutter).
    # A match must come from an exact name/alias/title/slug/id key.
    rows.append((base, slug, is_update, declared))

matched = [r for r in rows if r[1]]
new = [r for r in rows if not r[1]]

L = []
L.append("# Nominees vs mk-sandbox — comparison report\n")
L.append("Generated for review. **mk-sandbox is read-only**; nothing here was written to it.\n")
L.append("- Nominee files: **%d**\n- With an existing sandbox record: **%d**"
         "\n- Genuinely new: **%d**\n" % (len(rows), len(matched), len(new)))

bad_label = [r for r in matched if not r[2]]
bad_id = [(b, s, d) for b, s, u, d in matched
          if d and d != records[s].get("id")]

L.append("\n## Corrections needed\n")
L.append("### Mislabelled as NEW — a record already exists (%d)\n" % len(bad_label))
L.append("| Nominee | Existing record | Existing id | rev |\n|---|---|---|---|")
for b, s, u, d in bad_label:
    r = records[s]
    L.append("| %s | `%s` | `%s` | %s |" % (b, s, r.get("id"), r.get("revision")))

L.append("\n### Proposed id does not match the real id (%d)\n" % len(bad_id))
L.append("| Nominee | Proposed | Actual |\n|---|---|---|")
for b, s, d in bad_id:
    L.append("| %s | `%s` | `%s` |" % (b, d, records[s].get("id")))

L.append("\n## All nominees with an existing record (%d)\n" % len(matched))
L.append("| Nominee | Record | id | rev | status | actorType | goals | rels | srcRefs |\n"
         "|---|---|---|---|---|---|---|---|---|")
for b, s, u, d in sorted(matched):
    r = records[s]
    L.append("| %s | `%s` | `%s` | %s | %s | %s | %d | %d | %d |" % (
        b, s, r.get("id"), r.get("revision"), r.get("status"), r.get("actorType"),
        len(r.get("goals") or []), len(r.get("relationships") or {}),
        len(r.get("sourceRefs") or [])))

L.append("\n## Genuinely new — no sandbox record (%d)\n" % len(new))
for b, s, u, d in sorted(new):
    warn = "  **<- claims UPDATE but no record found**" if u else ""
    L.append("- %s — proposes `%s`%s" % (b, d or "no id", warn))

open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote", OUT)
print("matched %d / new %d / mislabelled %d / id-mismatch %d"
      % (len(matched), len(new), len(bad_label), len(bad_id)))
