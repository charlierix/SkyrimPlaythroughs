# identity links — one mind, several bodies

SkyrimNet models shared identities natively: **identity links** attach to an NPC's bio and tell the model "this other self is still you". The whole system is rendered by `get_linked_identities(actorUUID)` in one file: `submodules/character_bio/7050_identity_links.prompt`.

## the link schema

Fields read by 7050 (verified against the template itself):

| field | meaning |
| --- | --- |
| `name`, `uuid` | the other side of the bond |
| `shared_virtual` | both sides are bodies of one named mind → the "One Soul, Two Bodies" branch |
| `host_unaware` | possession where the body never knew — separate branch |
| `dominance` | `entity_led` (other self at the reins) · `contested` (the mouth changes hands) · `host_led` (whisper beneath) — used by the non-shared_virtual branches |
| `is_virtual` | the other side is a bodiless entity |
| `sees_their_memories` | true: shared memories, rendered with `[experienced as X]` tags; false: "you feel this other self out there, but you cannot read its memories" |
| `is_present` | the other side is in the current scene → renders the two-places-at-once section |
| `note`, `custom_framing`, `custom_conduct` | per-bond text overrides (custom_framing/conduct are **not** offered in the shared_virtual branch — its framing text is fixed) |

## where links are consumed

| site | effect |
| --- | --- |
| `character_bio/7050_identity_links.prompt` | the framing + conduct block itself |
| `character_bio/0100…9990` (summary, background, personality, interject summary, aspirations, relationships, occupation, speech style) | `suppress_host_persona`: under entity_led the body's own sections stand down |
| `character_bio/7100_memories.prompt` | memory list mixes both lives; foreign entries render `[experienced as {originName}]` (retrieval supplies `memory.isOwn` / `originName`) |
| `system_head/0400_speech_style_bio.prompt` | entity_led virtual → the entity's speech style replaces the body's |
| `user_final_instructions/0500_response_format.prompt` | contested: lines tagged with whose voice won the mouth |
| `npc_thoughts.prompt`, `dynamic_bio_update.prompt` | thoughts and dynamic bio updates iterate linked identities |

## registration API (verified in `Source/Scripts/SkyrimNetApi.psc`)

| call | notes |
| --- | --- |
| `RegisterVirtualNPC(name, displayName, voiceId, conversationMode, language)` | registers a bodiless entity; 0 on success or already exists |
| `EnableVirtualNPC` / `DisableVirtualNPC` / `UpdateVirtualNPC` | lifecycle |
| `GetVirtualNPCUUID(name)` | UUID derived from the registration name — stable across sessions, safe to cache |
| `GetVirtualNPCList()` | JSON array; needs an external JSON lib to parse |
| `IsVirtualEntity`, `GetEntityUUID(Actor)`, `GetActorByUUID` | entity↔actor resolution |

## the creation gap

No Papyrus function creates a link, and no `shared_virtual` / `host_unaware` / `dominance` reference exists outside the prompt files in this repo snapshot. The plugin's config-category list includes **VirtualEntities** — so the creation surface is the dashboard (`localhost:8080`, VirtualEntities config), possibly also the MCP server (port 8889). To verify live at first setup.

## mapping to the five folds

- The `shared_virtual` branch is purpose-built for us: "one consciousness wearing two vessels", both bodies speaking as YOU, no dominance hierarchy needed. Five folds = 20 directed links (each fold's bio renders its own four).
- **`sees_their_memories: false`** is our design ([message-flow](../writeups/message-flow.md)): folds start with the shared memories plus a per-fold recruitment memory, and gaps close through conversation and gist retelling. Setting it true would natively merge all memories and flatten the texture.
- `is_present: true` gives the in-scene section: both mouths may speak, never surprised by each other — exactly the group-talk default scene.
- If the fixed shared_virtual framing text ever fights our voice set, the fallback is overriding `7050_identity_links.prompt` itself.

## open items for live verification

1. the exact link-creation UI/API on the dashboard (VirtualEntities page)
2. whether shared_virtual bonds work between two bodied actors or require one side virtual — the branch itself never checks `is_virtual`, which reads bodied-to-bodied, but only live testing settles it
3. how the `[experienced as]` marker interacts with seeded memories — does `RegisterPersistentEvent(content, originatorActor, ...)` stamp originName?