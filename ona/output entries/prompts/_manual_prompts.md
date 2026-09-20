[← back to the output-entries manual](../_manual.md)

# prompts — the overlay overrides

Dashboard prompt edits land in the player's overlay layer — above every installed plugin. An override replaces the whole file, so each file here carries the base text plus our addition.

| file | entry | change |
| --- | --- | --- |
| `diary_entry.prompt` | [diary-entry](diary-entry.md) | keep the Inja structure (`npc`, `lastDiaryEntry`, `recentMemories`, event history); replace the writing guidelines ([topics](../../writeups/topics.md), [attribution](../../writeups/attribution.md)) |
| `submodules/user_final_instructions/0700_extra_instructions.prompt` | [extra-instructions](extra-instructions.md) | base text + the group-talk sentence ([message-flow](../../writeups/message-flow.md)) |
| `memory/generate_memory.prompt` (optional) | [memory-bias](memory-bias.md) | bias toward the negativity filter ([attribution](../../writeups/attribution.md)) |
| `submodules/character_bio/0175_severactions_follower.prompt` | [follower-0175](follower-0175.md) | SeverActions companion frame — fold-gated rewrite: mind frame for folds, stock text for non-folds ([stance](../../docs/severactions-relationship-stance.md)) |
| `sever_relationship_assess.prompt` | [relationship-assess](relationship-assess.md) | SeverActions companion→player assessment — fold rules: causal reads, single-misstep floors, sticky highs, mind-voiced blurb |
| `sever_relationship_interfollower.prompt` | [interfollower-assess](interfollower-assess.md) | SeverActions inter-follower assessment — identity-linked folds omitted from pairs; bonds authored, never eroded |

## example prompt-helper prompt

> Open `diary_entry.prompt` and replace the writing guidelines with: {our guidelines}. Keep every template variable, conditional and the `render_subcomponent` call exactly as they are.

Watch the validation panel after saving — the helper reports errors, warnings and variables used.

## files (next pass)

- `diary-entry.md`, `extra-instructions.md`, `memory-bias.md` — full replacement texts, ready to paste
- `follower-0175.md`, `relationship-assess.md`, `interfollower-assess.md` — SeverActions Follower-module overrides ([stance doc](../../docs/severactions-relationship-stance.md)); per-recruit prewarm batch in [prewarm](../prewarm/_manual_prewarm.md)