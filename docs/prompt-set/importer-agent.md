# prompt set — the importer agent brief

[← proposal](../prompt-set-package.md) · [layout](./package-layout.md) · [task graph](./task-graph.md)

Who executes a prompt set at play time. The importer agent is the **out-of-game AI agent** driving the dashboard, console and read-backs. The in-game chat assistant is a **verifier**, not a builder.

## capability map (live-verified)

| surface | can do | cannot do |
| --- | --- | --- |
| dashboard pages (`localhost:8080`) | create + edit everything: Profiles, Memories, World Knowledge, VirtualEntities, Identity Links, prompt editor | — |
| chat assistant | read-backs: `get_linked_identities`, `get_virtual_npc_list`; game-data queries; memory/profile reads | no creation tools for profiles, links or virtuals — its own tool inventory confirms it |
| console / Papyrus | fallbacks: `RegisterVirtualNPC`/`EnableVirtualNPC`, `RegisterPersistentEventByUUID`, `SeverActionsNativeExt.*` floors | ⚠ console reachability unverified per call — prove with one round-trip before trusting |

Source of the assistant row: [AGENT FEEDBACK](<../../output - with names/identity-links/AGENT FEEDBACK.md>) — the assistant inventoried its own tools: read-only decorators plus game-data queries; no create/bond/register surface; no MCP branch.

## per-step protocol

1. **fill** — resolve the step's tokens from `pack.json` + live state; reject any game-facing text still carrying `{` tokens
2. **submit** — through the step's declared surface and helper; paste whole files, never paraphrase
3. **read back** — run the step's `verify`; a step without its read-back is not done
4. **log** — append `runtime/run-log.md`: step id, timestamp, read-back result
5. **stop on drift** — known failure modes have cleanup ladders in the source manuals (e.g. [virtual entity roleplay](<../../output entries/knowledge/_manual_knowledge.md>)); follow the ladder, do not improvise

## standing rules

- **whole-file fidelity** — prompt overrides replace entire files: submit the package's full text. Same rule for the profile fallback: one AI pass, complete ten-block bio, "no rewording" — partial prompts invite paraphrase drift
- **idempotency** — check-before-create; re-runs patch or skip
- **⚠ items** — anything marked ⚠ needs one live proof before the agent treats it as fact; record the proof in the run log
- **one joiner at a time** — the joiner phase is atomic per follower; the run log marks the resume point after an abort
- **assistants verify, dashboards create** — never ask the chat assistant to create; never hand-edit what a read-back can confirm

## fallback ladder

| step kind | primary | fallback |
| --- | --- | --- |
| virtual entity | dashboard VirtualEntities | console `RegisterVirtualNPC` + `EnableVirtualNPC` |
| profile merge | dashboard paste | one AI pass, whole bio, verbatim |
| memories | dashboard Memories CRUD / assistant with tools | `RegisterPersistentEventByUUID` |
| bonds | dashboard Identity Links UI | override `7050_identity_links.prompt`, bonds hard-coded |
| prewarm | console natives | dashboard/MCP tools if present ⚠ · custom Papyrus quest script |

The bond fallback changes the plugin half — that is why it is decided at packaging time (`on_fail` in the task steps), not at play time.
