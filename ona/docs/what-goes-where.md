# what goes where — content to surface

One rule: **base ships defaults at the bottom of the priority order; every other layer resolves above it.** Never edit base — override with a same-path file in `overlay/prompts/`, or add a new numbered file where folder order matters. ([base-plugin](../okf/skyrimnet/base-plugin.md) · [prompts-and-decorators](../sources/SkyrimNet-GamePlugin/docs/modding/prompts-and-decorators.md))

## layers

| layer | where | role |
| --- | --- | --- |
| base | `skyrimnet.base` bundle (`plugins/skyrimnet/base/` in repo, `library/skyrimnet.base/` installed) | shipped templates, components, 1,509 vanilla bios — always enabled |
| hub packs | `skyrimnet.bios-{mod}` packs | per-mod bios for third-party NPCs |
| external | `Data/SKSE/Plugins/SkyrimNet/external/{author}.{slug}/` | our content plugin, shipped with the mod ([migration beta 25](../okf/skyrimnet/docs/migration-beta25.md)) |
| overlay | `overlay/` | dashboard player-edit layer — same path = override, new numbered file = insertion |

## the prompt tree and its slots

Paths under `sources/SkyrimNet-GamePlugin/plugins/skyrimnet/base/prompts/` (okf: [prompts index](../okf/skyrimnet/prompts/index.md)):

| slot | what it is | use it for |
| --- | --- | --- |
| top-level `*.prompt` | big templates: `dialogue_response`, `player_dialogue`, `warmup`, `diary_entry`, `character_profile_update`, `dynamic_bio_update`, `agent_chat`, `agent_prompt_helper`, `agent_knowledge_builder` | full-rewrite overrides in overlay |
| `submodules/character_bio/` (18 files) | every NPC bio, assembled in filename order; render modes (`full`, `thoughts`, `transform`, `dialogue_target`, `short_inline`, `bio_summary`) pick sections; `npc` variable in scope | per-character texture — background, personality, aspirations, speech style; the prefix number is the insertion point |
| `submodules/system_head/` (8 + `guidelines/`) | top of the system prompt: instructions, setting, format rules, actor bios, telepathy awareness, scene context, omnisight, speech style + roleplay guidelines | global frame changes |
| `submodules/user_final_instructions/` (10 files) | appended just before each response: environment, telepathy reception, combat, response format, audio tags, **extra instructions (0700)**, quest dialogue, embedded actions, narration, recent state changes | `0700_extra_instructions.prompt` = the slot for standing rules like the group-talk sentence |
| `characters/` (1,509 files) | pre-written vanilla bios | override a specific NPC by same filename |
| `memory/` (5 templates) | generate_memory, memory_ranker, evaluate_memory_relevance, memory_builder, mood_evaluator | bias how memories form (first-person, importance) |
| `helpers/` | evaluate_mood, generate_profile, generate_search_query | support roles |
| `target_selectors/`, `transformers/`, `omnisight/` | who speaks, translation, perception | targeted rewrites |
| `dev/`, `documentation/`, `translation/`, `web/` | MCM test, doc gen, lexicons, dashboard pages | leave alone |

Custom decorators (Papyrus `SkyrimNetApi.RegisterDecorator`) put mod data into any prompt as `{{ my_decorator(npc.UUID).field }}` — caveat: only callable on speaker/target, not on looped bystanders.

## memories: generated vs seeded

**Generated at play** — the pipeline writes first-person memories from recent events and dialogue, ranks by importance, retrieves by meaning; explorable in the UI Memories section. Diaries ride the same flow: `diary_entry.prompt` writes first-person, keeps continuity via `lastDiaryEntry`, fed recent memories plus verbose event history.

**Seeded by us** — verified signatures in `Source/Scripts/SkyrimNetApi.psc`:

| call | signature | reads as |
| --- | --- | --- |
| `AddWorldKnowledge` | `(content, conditionExpr, alwaysInject, importance, displayName)` | a fact an NPC knows, condition-scoped |
| `RegisterPersistentEvent` | `(content, originatorActor?, targetActor?)` | "stored in actor memory without triggering conversation" |
| `RegisterDialogueToListener` | `(speaker, listener, dialogue)` | what the listener "was told" |

All three have `...ByUUID` variants. These are the primitives [message-flow](../writeups/message-flow.md) plans around: 3 shared + 1 recruitment memory per fold, injected at recruit time.

**Which surface for which intent** — the builder's own rule of thumb: omitting it in an unrelated conversation would make the NPC sound broken → `always_inject: true`; it should surface only when the topic comes up → semantic knowledge (default); it should fossilize into opinion → seeded memory ([attribution](../writeups/attribution.md)).

## mapping the playthrough content

| content (writeups) | surface |
| --- | --- |
| lore spine — origin, the-five, names, motivation ([the-five](../writeups/the-five.md), [names](../writeups/names.md)) | per-fold bios in our plugin ([inventory](./overlay-inventory.md)); folds bonded by identity links — `submodules/character_bio/7050_identity_links.prompt` renders the shared_virtual "one soul, N bodies" framing ([identity links](./identity-links.md)) |
| cover story ([cover-story](../writeups/cover-story.md)) | one boring background line in each body bio + a semantic knowledge entry for locals |
| implanted memories ([message-flow](../writeups/message-flow.md)) | the seeding API above — 3 shared + 1 recruitment memory per fold, injected at recruit time |
| diary-keeping instructions | override `diary_entry.prompt` in overlay — the writing guidelines live in the template, not in the bios |
| topics for folds to discuss ([topics](../writeups/topics.md)) | semantic knowledge entries for the ideas/events register + bio aspirations and interject-summary sections |
| group talk / follower dynamics ([message-flow](../writeups/message-flow.md)) | one sentence in `submodules/user_final_instructions/0700_extra_instructions.prompt`; proximity audience is native (chat audience strip, SeverActions Traveling Party) |
| voice quality ([speech-quality](../writeups/speech-quality.md)) | `submodules/character_bio/9990_speech_style.prompt` + `submodules/system_head/0400_speech_style_bio.prompt` |
| negativity filter ([attribution](../writeups/attribution.md)) | obeyed by the pre-seeded pool; optionally bias `memory/generate_memory.prompt` in overlay |
| SeverActions familiarity & reputation | its own prompt library (separate hub) — disable, pre-warm, or override ([okf severactions](../okf/severactions/prompts/familiarity.md)) |

## open gaps

- **identity-link creation surface** — narrowed to the dashboard VirtualEntities config / possibly MCP; the prompt-side model is traced in [identity links](./identity-links.md).
- **dashboard endpoints** behind the helper buttons — not in this source snapshot; the prompt files are the contract we can act on.
