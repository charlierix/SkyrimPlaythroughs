# prompt set package — a portable prompt-set mod for SkyrimNet

Proposal: turn the hand-run [output-entries manual](<../output entries/_manual.md>) work into a **package an importer agent consumes** — a prep job once per playthrough, then a per-follower job that re-runs for every new follower. In modding terms: a **prompt set mod for SkyrimNet**.

**Built.** The package exists at [`output package/`](<../output package/README.md>), assembled from the frozen `output entries/` tree; `output - with names/` stays as the frozen name-filled snapshot. One as-built deviation from [package-layout](./prompt-set/package-layout.md): the knowledge entries live in `runtime/knowledge/` rather than a shipped pack — the party-roster entry updates at every joiner, and a `.sknpack` would freeze it; shipping the stable entries (cover story, silence rules) as a pack remains an open ⚠ option.

[← surface research — docs](./_overview.md)

## the scoping facts (why this proposal exists)

Verified against the beta25 migration doc:

| fact | consequence |
| --- | --- |
| prompt templates resolve through global layers: `saves/` (per-playthrough) > `overlay/` (player edits) > plugins in player order > shipped defaults | there is **no per-playthrough prompt layer** — an overlay edit or plugin file applies to every playthrough where its layer is active |
| `saves/` holds only per-playthrough **bios** (`prompts/_saves/**` — "not allowed in a plugin") | prompt sets cannot ride the saves layer |
| memories, profile rows, identity bonds, NPC-group membership are per-save database state | the play-time work is natively per-playthrough; only prompt templates need packaging for isolation |
| an external plugin lives in one small mod folder; removing the mod removes the layer | the built-in isolation mechanism: **one prompt set = one small external plugin, toggled per MO2 profile** |

So a new character does **not** need a cloned MO2 instance. It needs a copied package (a dozen files) shipped as its own external plugin, enabled by that character's MO2 profile. Two sets enabled at once resolve by plugin priority (the dashboard shows the winner per file) — cleaner to keep one set enabled per profile.

## the two halves

| half | what | delivery |
| --- | --- | --- |
| `plugin/` — shippable | prompt overrides + knowledge pack (group names ship with the pack; membership stays per playthrough) | beta25 external plugin: `Data/SKSE/Plugins/SkyrimNet/external/{author}.{slug}/` with `manifest.json` |
| `runtime/` — play-time | token registry, task graph (`tasks/prep.json`, `tasks/joiner.json`), memory texts, joiner bio template, bond + prewarm specs | read and executed by the importer agent at play time |

The split is forced by SkyrimNet's rules: prompts and knowledge packs may ship in a plugin; per-save state never does. Layout: [package-layout](./prompt-set/package-layout.md).

## the phases (mirroring the manual)

**prep — once per playthrough**

1. verify the plugin layer is active (Installed Plugins, External badge, no skipped files)
2. fill `{player}` + character tokens from `pack.json`
3. verify the group + knowledge entries landed with the pack ⚠
4. register the mind's virtual entity — private — and read it back (`get_virtual_npc_list`)
5. smoke-test the bond surface: throwaway bond → `get_linked_identities` → remove
6. seed the shared memories into the player-fold

**joiner — every time a follower is added** (repeatable, unbounded party)

1. pause; resolve the joiner's UUID (dashboard or `GetEntityUUID(Actor)`)
2. merge the ten-block profile (mind blocks + body template; dashboard paste; DynamicBio guard)
3. inject memories: the shared pool + this joiner's own memory (template, live party list)
4. create bonds: to the player-fold and every existing member — both directions
5. add the joiner to the NPC group
6. prewarm relationship floors: fold→player calls + blurb; pair blocks both directions
7. read-back verify + log

Nothing is numbered by recruit order — steps fan out from live party state. The writeup's `recruit-1…4` ladder becomes one template plus a loop. Step schema and rules: [task-graph](./prompt-set/task-graph.md).

## the importer agent

The importer agent is the **out-of-game AI agent** driving the dashboard, console and read-backs. The in-game chat assistant is a **verifier**, not a builder — its tools are read-only, live-confirmed in [AGENT FEEDBACK](<../output - with names/identity-links/AGENT FEEDBACK.md>). Steps carry their helper-agent instructions (prompt-helper prompts, knowledge-builder prompts) so the agent executes instead of improvising. Full brief: [importer-agent](./prompt-set/importer-agent.md).

## new character = copy + character block

| change | where |
| --- | --- |
| mind name, lore names, party group, party cap | `pack.json` → `character` |
| shared memory texts, joiner memory voice | `runtime/memories/` |
| prompt texts carrying character voice | `plugin/prompts/…` (character tokens filled at packaging time) |
| machinery — task graph, schemas, agent brief | unchanged |

Ship the copy under its own id (`{author}.{character}-promptset`); bump semver on any content change.

## open items

1. knowledge-pack route — entries ship as a Beta25 `.sknpack` (dashboard re-export); group creation via pack needs one live check
2. UUID fetch — pick console `GetEntityUUID` vs dashboard lookup; encode it in the steps
3. MO2-profile enable/disable cycle — one live pass to confirm clean layer removal
4. stretch: a SkyrimNet trigger/action that fires on a new follower and surfaces the joiner checklist in-game (⚠ read [WORKFLOW_TRIGGERS](../../sources/SkyrimNet-GamePlugin/docs/modding/WORKFLOW_TRIGGERS.md) first)
