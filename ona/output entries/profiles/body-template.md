[← profiles manual](_manual_profiles.md)

# body-template — the per-body fill-in skeleton

Copy per recruited body and fill the {slots} from the body's own base profile (vanilla bodies ship pre-built bios; mod bodies get auto-generated), then merge with [mind](./mind.md): mind text over body base.

## slots

| slot | rule |
| --- | --- |
| {BODY NAME} | the body's name as SkyrimNet knows it |
| summary | mind.md summary, with {name} → {BODY NAME} |
| personality | mind.md personality, unchanged |
| speech_style | mind.md speech_style, unchanged |
| aspirations | mind.md core + the experiment line below |
| interject_summary | mind.md interject_summary, with {name} → {BODY NAME} |
| background | one plain line of the body's local history — shape below |
| appearance, occupation, relationships, skills | keep the body's base text unchanged |

## the experiment line

Each fold runs its body's own experiment; append to the aspirations core:

- This body's experiment: {what this body is for — e.g. what hunger is like, what a sword arm learns, what startle does to thinking, what carrying weight teaches}

## the background line

One boring line, body-side only, nothing fold-side. Shape: "{BODY NAME} came from {place}, worked as {trade} before taking to the road."

## merge checklist (recruit time)

- speech_style and interject_summary survived the merge
- background is one boring line with nothing fold-side in it
- appearance, occupation, relationships untouched
- DynamicBio checked — Advanced Configuration → DynamicBio: make sure its rewrite set does not cover the fold-owned sections (summary, personality, speech_style, interject_summary), or the fold voice gets washed out
