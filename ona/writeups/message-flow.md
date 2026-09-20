# message flow — how words move

The old relay protocol answered an engine limitation that turns out not to exist. What the engine natively does covers the need; what remains is group conversation as the default scene, memory seeding for gaps, and a little retelling style.

## the standing rules

- **Together: say it once.** Nearby folds hear it — proximity audience, companion-tagged speaker selection, and SeverActions' Traveling Party block ("everyone above is nearby and can hear you") make multi-fold conversation the default scene. No relay mechanic; nothing to prompt for.
- **Apart: words wait.** There is no live channel across distance in play. Aimed thought stays a lore channel (the-five.md), but the engine carries no words between folds remotely — the typed telepathy channel is a keyboard habit, unused in VR play. A fold with something to say holds it, and retells in gist on reunion. What distance touches is the hum: it thins, never silences, and still carries nothing (the-five.md).
- **Gaps: memory seeding.** Knowledge one fold holds and others don't is handled by seeding, not conversation: `AddWorldKnowledge(content, conditionExpr, ...)` for condition-scoped shared facts (scope to the five folds as the baseline), `RegisterPersistentEvent(...)` — its own doc comment says "stored in actor memory without triggering conversation" — and `RegisterDialogueToListener(speaker, listener, dialogue)` for what a fold "was told" (SkyrimNetApi.psc).

## initial memories: shared three, personal one

At recruit time each fold gets four memories: three shared, injected identically into every fold, plus one of its own by order of recruiting — the first fold remembers meeting the player fold, the second remembers the player fold and one earlier fold, and so on. The difference between folds stays small and natural, and prompts never encourage it to grow. Recruitment is a rushed gathering — the party is being collected to rescue the others, no lingering in town — so the memories go in at recruit time and first real conversation waits for the wilderness. Place them with the seeding primitives above.

## style: retell in gist

When a fold retells what another said, it retells in gist — "you said the cave was worth it" — never a recording, no echo-chorus, one fold at a time. Style, not protocol: a thought becoming ours through words already implies it.

## prompt footprint: deliberately small

One small sentence in the final system prompt (roughly: what one fold says aloud, the folds nearby hear; what is known to one is soon said to all), plus optional seeded memories for anything that must be pre-known. This topic does not dominate prompts.

## whisper etiquette

Proximity listening is modeled, so Ohne-talk near locals is overhearable. In towns, sensitive fold-talk waits for a better moment or the group moves aside — one lore line doubles as cover-story protection. No whisper prefix needed; that was a typed-channel habit.
