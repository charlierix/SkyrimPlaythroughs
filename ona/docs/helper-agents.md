# helper agents — the dashboard buttons

SkyrimNet runs two families of agents. The **model agents** do the in-game work — dialogue, game master, memory, mood, speaking turns. The **helper agents** are the assistants behind the config-UI buttons: a chat console, a prompt-template editor, and a world-knowledge author. This doc maps the buttons to their prompts; the in-game roles are covered in [model-agents](../okf/skyrimnet/docs/model-agents.md).

## the three helper agents

All three are `.prompt` files in the base plugin, and all three extend `components/agent_tools_base.prompt`:

| agent | prompt file | what it does |
| --- | --- | --- |
| chat assistant | `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/agent_chat.prompt` | friendly in-world Q&A console; explores game data (spells, items, factions) and the player's situation on request |
| prompt helper | `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/agent_prompt_helper.prompt` | writes, edits and improves prompt templates; receives the open file (`currentPrompt`, `promptContent`), validation status, and the full decorator catalog as context |
| knowledge builder | `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/agent_knowledge_builder.prompt` | authors world-knowledge entries in batches: content, conditions, importance, tags, dedup keys; reviews and refines proposals into packs |

- okf concepts: [agent tool prompts](../okf/skyrimnet/prompts/templates/agent-tools.md) · [dialogue templates](../okf/skyrimnet/prompts/templates/dialogue.md) (agent_chat lives there)
- the button wiring itself is dashboard-side and not in this source snapshot — the `.prompt` files are the editable surface. Override any of them via `overlay/prompts/` at the same path: [what goes where](./what-goes-where.md).

## the shared scaffold

`components/agent_tools_base.prompt` gives all three the same machinery:

- **tools** — `availableTools` injected at render time: game-data queries like `get_spells`, `get_items`, `get_magic_effects`, plus `get_decorators` for the function catalog
- **protocol** — XML-style `<function_calls>` blocks, one JSON call per line; stop after the block, results arrive next turn
- **ephemeral results** — tool output exists only for the immediate next turn; the agent must fold findings into its reply text
- **hygiene** — plugin filters (`"plugin": "Skyrim.esm"`), fuzzy `name_contains`, pagination via `next_offset`

## knowledge builder schema

The schema the builder authors is the same one `SkyrimNetApi.AddWorldKnowledge(...)` writes — the agent is a friendly UI for it (placement rules: [what goes where](./what-goes-where.md)).

| field | meaning |
| --- | --- |
| `content` | in-world fact text; full Inja support (`{{ playerName }}`, decorators, conditionals) |
| `condition_expr` | who sees it — `is_in_faction`, `is_in_npc_group`, `get_quest_stage`, `is_quest_active`, `decnpc(...)`, `and`/`or`/`not` |
| `always_inject` | true = deterministic injection every turn; false (default) = semantic retrieval when the topic is relevant |
| `importance` | 0.0–1.0 retrieval priority (0.9+ major events, 0.7–0.8 notable, 0.4–0.6 minor) |
| `type` | KNOWLEDGE (default), EXPERIENCE, LOCATION, RELATIONSHIP, SKILL, TRAUMA, JOY |
| `tags` | natural-language labels for semantic retrieval |
| `knowledge_key` | dedup key — same key = only the highest-importance entry shows |

## model agents (in-game roles, for contrast)

Configured under Advanced Configuration → OpenRouter. Role → template map, per the okf groupings:

| role | job | base-plugin templates |
| --- | --- | --- |
| text generation | NPC dialogue | `dialogue_response`, `player_dialogue`, `warmup` |
| game master | initiates NPC interactions | `gamemaster_scene_planner`, `gamemaster_action_selector` |
| memory generation | write + rank memories | `memory/generate_memory`, `memory/memory_ranker`, `memory/evaluate_memory_relevance`, `memory/memory_builder` |
| profile generation | auto-profile unknown NPCs | `character_profile_update`, `helpers/generate_profile` |
| dynamic bio | periodic profile updates | `dynamic_bio_update` (sections under Advanced Configuration → DynamicBio) |
| action evaluation | pick the action | native action selector + drilldown |
| mood | emotional state for voice/face | `memory/mood_evaluator`, `helpers/evaluate_mood` |
| speaking turn | who speaks next | `dialogue_speaker_selector`, `player_dialogue_target_selector` |
| memory search | build retrieval query | `helpers/generate_search_query` |
| thoughts | inner monologue | `npc_thoughts`, `player_thoughts` |

okf indexes: [templates](../okf/skyrimnet/prompts/templates/index.md) · [components](../okf/skyrimnet/prompts/components/index.md)
