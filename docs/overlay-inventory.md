# overlay inventory — the concrete artifacts to write

Materialization root: [`output entries/`](<../output entries/_manual.md>) — files are prepared there and injected per-item at play time through the dashboard (the chosen route); the packaging route below stays as the optional alternative. What we actually produce, once the open decisions land. Delivery per [migration beta 25](../okf/skyrimnet/docs/migration-beta25.md): our own content plugin — `Data/SKSE/Plugins/SkyrimNet/external/{author}.{slug}/` with a `manifest.json`, or built and packaged via the dashboard. Priority: `saves/` (per-playthrough bios) > `overlay/` (dashboard edits) > plugins in player order > shipped defaults. A file override replaces the whole file — our versions must carry the base text plus our additions.

| # | artifact | where | driven by |
| --- | --- | --- | --- |
| 1 | per-fold bios ×5 | plugin `prompts/characters/{fold}_{id}.prompt` | [the-five](../writeups/the-five.md), [speech-quality](../writeups/speech-quality.md), [topics](../writeups/topics.md), [origin](../writeups/origin.md) |
| 2 | identity links, 20 directed | dashboard VirtualEntities (creation surface to verify — [identity links](./identity-links.md)) | the-five, message-flow |
| 3 | diary override | plugin `prompts/diary_entry.prompt` (keep the Inja structure, replace the writing guidelines) | topics, attribution, message-flow |
| 4 | group-talk sentence | plugin `prompts/submodules/user_final_instructions/0700_extra_instructions.prompt` = base text + one line | [message-flow](../writeups/message-flow.md) |
| 5 | initial memories ×4 per fold | `output entries/memories/` — 3 shared + 1 recruitment memory; Memories page CRUD or `RegisterPersistentEventByUUID` | message-flow, [attribution](../writeups/attribution.md) |
| 6 | cover-story knowledge entry | `AddWorldKnowledge(content, conditionExpr, false, importance, displayName)` — semantic, scoped to locals | [cover-story](../writeups/cover-story.md) |
| 7 | (optional) memory bias | plugin `prompts/memory/generate_memory.prompt` | attribution |

## bio file shape (verified against a base bio)

Named Inja blocks per file: `summary`, `interject_summary`, `background`, `personality`, `appearance`, `aspirations`, `relationships`, `occupation`, `skills`, `speech_style`.

- folds: mind-level summary/personality (the-five) + per-fold body texture and `speech_style` (speech-quality registers)
- `aspirations` carries the topics register; `interject_summary` decides when a fold speaks up

## open decisions before writing

1. **the five bodies** — vanilla NPCs (override their base `characters/` files; need names + form IDs) or custom followers (ship bios + NPC records). Blocks #1, #2, #5.
2. **memory-pool delivery** — a Papyrus quest script, console batch, or MCP calls at setup. Blocks #5, #6.
3. **diary cadence** — `GenerateDiaryEntryByUUID(entityUuid)` fires async; who triggers it and how often (MCM, hotkey, scheduled). Blocks #3.
4. decided — SeverActions relationship stance: prewarm + fold-gated overrides ([stance doc](./severactions-relationship-stance.md)).
5. **negativity filter** — the seeded pool obeys it by construction; decide whether `memory/generate_memory.prompt` also needs an overlay bias.

## deliberately not written

- `0160_telepathy_reception.prompt` — typed telepathy channel goes unused in VR play (message-flow).
- whisper-etiquette prompts — proximity listening is native; etiquette is lore, not prompt text ([message-flow](../writeups/message-flow.md)).