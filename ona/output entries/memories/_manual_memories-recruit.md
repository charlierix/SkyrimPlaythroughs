[← back to the output-entries manual](../_manual.md)

# memories — the pools at recruitment

> ⚠ **runtime fill needed** — the shared three ship ready; every `recruitment/recruit-N.md` carries `{player}` plus the earlier folds' names as `{fold1}`…`{fold3}` tokens. Fill at recruit time — each file's **tokens** section lists exactly what it needs. A token left unfilled enters the fold's memory verbatim.

Initial setup put the shared pool into the player-fold (see [memories — setup](./_manual_memories-setup.md)). Memories are per-NPC — a memory injected into one fold is invisible to the others, and the gaps close through conversation and gist retelling ([message-flow](../../writeups/message-flow.md)) — so the work here repeats for every recruited fold: its own copy of the shared three, plus the one recruitment memory that is its own.

## per recruitment — fill the new fold

The new fold, recruit *k*, gets:

- **the 3 shared memories** — the same files the player-fold got: [shared-1.md](./shared/shared-1.md) · [shared-2.md](./shared/shared-2.md) · [shared-3.md](./shared/shared-3.md)
- **its recruitment memory** — one per fold, matching its recruit number: [recruit-1.md](./recruitment/recruit-1.md) · [recruit-2.md](./recruitment/recruit-2.md) · [recruit-3.md](./recruitment/recruit-3.md) · [recruit-4.md](./recruitment/recruit-4.md)

| recruit | gets |
| --- | --- |
| every fold | the 3 shared memories |
| 1st | + recruit-1 — meeting the player fold |
| 2nd | + recruit-2 — meeting the player fold and one earlier fold |
| 3rd | + recruit-3 — meeting the player fold and the earlier folds |
| 4th | + recruit-4 — meeting the player fold and the full party |

The shared three make them unmistakably one mind; the fourth makes each fold's way in slightly its own.

## injection

The Memories page has full CRUD (verified in the README) — paste each memory onto the new fold. Or hand it to the chat assistant, with `{npc}` = the fold being recruited:

> Add a memory to {npc}: "{text}" — importance 0.8.

Fallback if the agent lacks memory tools: Papyrus `RegisterPersistentEventByUUID(content, originatorUuid, targetUuid)` — console or a tiny script, same content, target = the new fold.

Injections happen at recruit time even though real conversation waits for the wilderness — by the first stop, every fold already carries its four.
