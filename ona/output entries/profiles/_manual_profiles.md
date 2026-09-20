[← back to the output-entries manual](../_manual.md)

# profiles — the fold bios

> ⚠ **runtime fill needed** — the five bodies are chosen at play time: [mind.md](./mind.md) takes `{name}` (the body being merged) and [body-template.md](./body-template.md) has the `{BODY NAME}` slots. Fill per recruited follower before merging; nothing here hardcodes a body's name.

A SkyrimNet profile is one file of named Inja blocks (verified against the base bios): `summary`, `interject_summary`, `background`, `personality`, `appearance`, `aspirations`, `relationships`, `occupation`, `skills`, `speech_style`. The recruit-time job is one complete ten-block bio in that order — [mind.md](./mind.md) supplies the fold-owned blocks, [body-template.md](./body-template.md) holds the body-side fill-ins and the paste-ready skeleton.

Design sources: [the-five](../../writeups/the-five.md) (mind) · [speech-quality](../../writeups/speech-quality.md) (voice) · [topics](../../writeups/topics.md) (aspirations register) · [attribution](../../writeups/attribution.md) (the body's life = borrowed coat) · [cover-story](../../writeups/cover-story.md) (the boring line in background).

## recruit-time flow

1. recruit → look at the follower → pause
2. **find the profile** — dashboard → Profiles page; search the body's **in-game name** (⚠ if the follower was renamed for the playthrough, the entry is keyed to the base NPC — check the original name too)
3. **create it if missing** — step 1 below; the chat assistant cannot do this for you
4. **fill section by section** — step 2, the per-block table
5. **verify** — step 3, then the DynamicBio guard

## step 1 — create the entry (only if missing)

Vanilla bodies ship pre-built bios, so the entry usually already exists. A fresh recruit can have none: the auto-profiler feeds on recent events and dialogue, and a body that just joined has nothing on record yet — that is the missing-entry case.

> ⚠ **the chat assistant cannot create profiles.** Its tools are read-only game-data queries (verified in `components/agent_tools_base.prompt`, and confirmed live when an assistant-created entry never reached the UI) — creation is a dashboard job.

Dashboard → Profiles page: paste the complete ten-block skeleton from [body-template](./body-template.md) as the new entry — fold blocks from [mind](./mind.md), body-side slots from the body's base text where it exists, plain boring body-side text where it does not ([attribution](../../writeups/attribution.md): the body's life is a coat — invented base text is fine as long as it stays boring). ⚠ Confirm the page's create/paste control live at first use; if the dashboard only offers a generate button, it runs the same event-hungry auto-profiler — the deterministic paste beats it.

## step 2 — fill, section by section

Work top to bottom in bio-file order (the order base bios ship their blocks — `abelone_750.prompt` as the reference). Fold-owned blocks are replaced wholesale; body-owned blocks stay untouched.

| # | block | action | source |
| --- | --- | --- | --- |
| 1 | `summary` | replace | [mind](./mind.md) → summary, `{name}` → body name |
| 2 | `interject_summary` | replace | [mind](./mind.md) → interject_summary, `{name}` → body name |
| 3 | `background` | replace | one boring body-side line — shape in [body-template](./body-template.md) |
| 4 | `personality` | replace | [mind](./mind.md) → personality, unchanged |
| 5 | `appearance` | keep | the body's base text |
| 6 | `aspirations` | replace | [mind](./mind.md) core + this body's experiment line ([body-template](./body-template.md)) |
| 7 | `relationships` | keep | the body's base text |
| 8 | `occupation` | keep | the body's base text |
| 9 | `skills` | keep | the body's base text |
| 10 | `speech_style` | replace | [mind](./mind.md) → speech_style, unchanged |

## step 3 — verify

- all ten blocks present in template format (`{% block name %}…{% endblock %}`)
- `speech_style` and `interject_summary` are the fold's, not the body's old ones
- `background` is one boring line, nothing fold-side in it
- `appearance`, `occupation`, `relationships`, `skills` unchanged from the body's base
- DynamicBio guard — Advanced Configuration → DynamicBio: its rewrite set must not cover the fold-owned sections (`summary`, `personality`, `speech_style`, `interject_summary`), or the fold voice gets washed out over time

## fallback — one AI pass, whole bio at a time

If pasting is unavailable, do not prompt section-by-section prose and let the model compose — the profile-update agent returns **all ten blocks every time** (its template demands the complete bio), so hand it the fully assembled bio and ask for it back verbatim:

> Update the profile of {npc} to exactly this content, section for section, no rewording: [the complete ten-block bio]

Anything less invites paraphrase drift in the blocks that were meant to stay untouched.
