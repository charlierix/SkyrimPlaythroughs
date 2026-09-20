[← back to the output-entries manual](../_manual.md)

# profiles — the fold bios

> ⚠ **runtime fill needed** — the five bodies are chosen at play time: [mind.md](./mind.md) takes `{name}` (the body being merged) and [body-template.md](./body-template.md) has the `{BODY NAME}` slots. Fill per recruited follower before merging; nothing here hardcodes a body's name.

A SkyrimNet profile is one file of named Inja blocks (verified against the base bios): `summary`, `interject_summary`, `background`, `personality`, `appearance`, `aspirations`, `relationships`, `occupation`, `skills`, `speech_style`.

Design sources: [the-five](../../writeups/the-five.md) (mind) · [speech-quality](../../writeups/speech-quality.md) (voice) · [topics](../../writeups/topics.md) (aspirations register) · [attribution](../../writeups/attribution.md) (the body's life = borrowed coat) · [cover-story](../../writeups/cover-story.md) (the boring line in background).

## shape per fold

- `summary`, `personality` — mind-level: Ohne, not the body
- `speech_style` — the shared voice registers
- `background` — the body's plain local history, kept boring; nothing fold-side
- `aspirations`, `interject_summary` — the topics register; when this fold speaks up
- `appearance`, `occupation`, `relationships` — the body's own; keep what the existing profile has

## recruit-time flow

1. recruit → look at the follower → pause
2. dashboard: find the body's profile (vanilla bodies ship pre-built; mod bodies get auto-generated)
3. merge in the fold content — mind text over body base
4. sanity-check `speech_style` and `interject_summary` survived

## example agent prompt

> Update the profile of {npc}. Replace `summary` and `personality` with: {mind text}. Set `speech_style` to: {registers}. Set `aspirations` to: {register}. In `background`, keep the body's history as one plain line. Leave `appearance`, `occupation`, `relationships` unchanged.

⚠ DynamicBio periodically rewrites profile sections (config: Advanced Configuration → DynamicBio) — check its section list so the fold voice isn't washed out.

## files (next pass)

- `mind.md` — the shared fold-mind text
- `body-template.md` — the per-body fill-in skeleton