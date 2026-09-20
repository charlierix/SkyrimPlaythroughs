[← back to the output-entries manual](../_manual.md)

# memories — initial setup (the shared pool)

> ⚠ **runtime fill needed** — the shared three ship ready; every `recruitment/recruit-N.md` carries `{player}` plus the earlier folds' names as `{fold1}`…`{fold3}` tokens. Fill at recruit time — each file's **tokens** section lists exactly what it needs. A token left unfilled enters the fold's memory verbatim.

Every fold ends up carrying four memories: the three **shared** memories — the mind's common remembered history — plus one **recruitment** memory of its own, added at each recruitment ([message-flow](../../writeups/message-flow.md)). The shared three are what make the folds unmistakably one mind, so they ship ready to inject and are never edited per fold.

## now — inject the 3 shared memories into the player-fold

One memory per file: [shared-1.md](./shared/shared-1.md) · [shared-2.md](./shared/shared-2.md) · [shared-3.md](./shared/shared-3.md)

Inject all three into the player-fold, exactly as written — every fold must carry them identically. The Memories page has full CRUD (verified in the README): paste each memory onto the player-fold, or hand it to the chat assistant, with `{npc}` = the player-fold:

> Add a memory to {npc}: "{text}" — importance 0.8.

Fallback if the agent lacks memory tools: Papyrus `RegisterPersistentEventByUUID(content, originatorUuid, targetUuid)` — console or a tiny script, same content, target = the player-fold.

## writing rules (if you edit or add)

- first-person; obeys [attribution](../../writeups/attribution.md) — memories fossilize into opinions
- shared memories are written so any fold can carry them; recruitment memories are phrased as joining, not meeting a stranger — the folds are one mind ([the-five](../../writeups/the-five.md))
- keep them short and vivid: the recruitment window is a rushed mini pre-game (rescue the others, no lingering in town), real talk waits for the wilderness

## done

The shared pool is in. At each recruitment, the new fold gets its own copy of these three plus its recruitment memory — continue with [memories — recruit](./_manual_memories-recruit.md).
