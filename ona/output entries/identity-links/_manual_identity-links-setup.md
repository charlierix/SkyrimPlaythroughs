[← back to the output-entries manual](../_manual.md)

# identity links — initial setup (before recruiting)

> ⚠ **runtime fill needed** — [bonds.md](./bonds.md) takes `{fold1}`…`{fold4}` / `{player}` for the name columns **and one real `{uuid}` per row**, fetched live at recruit time (dashboard or `GetEntityUUID(Actor)`). Nothing in this folder can be pre-filled before the bodies exist.

This phase is plumbing, not content: it registers the virtual entity **Ohne** — the mind every bond's `shared_virtual` points at, which must exist before the first bond does — and proves the bond-creation surface with one throwaway bond. No bonds and no memory rows yet: the 20 bonds are created per recruitment from [bonds.md](./bonds.md), and the memory rows that fill the shared pool come in the [memories phase](../memories/_manual_memories-setup.md). Bonds render through `submodules/character_bio/7050_identity_links.prompt` ([full trace](../../docs/identity-links.md)); every bond row needs the other body's real `{uuid}`, fetched live.

## who can do what

| surface | role |
| --- | --- |
| dashboard (`localhost:8080`) | creation — VirtualEntities config for Ohne, Identity Links UI for bonds |
| chat assistant | verify only — `get_virtual_npc_list` (did step 1 land?) and `get_linked_identities` (does a bond render?); no creation tool, no MCP branch — confirmed against its toolset |
| console | `RegisterVirtualNPC` / `EnableVirtualNPC` exist in `SkyrimNetApi.psc` — console reachability unverified |

No Papyrus function creates a link — everything below is a dashboard job, with the chat assistant as the read-back verifier.

## step 1 — register Ohne

Dashboard → VirtualEntities config: register the entity as **Ohne**, conversation mode **private**, then enable it. The UUID derives from the registration name — `GetVirtualNPCUUID("Ohne")` if anything asks, stable across sessions.

> **why private** — Ohne is the secret, not a character the world meets. The cover story exists to hide the folds, the five bodies are the only interface, and a public virtual would put an addressable stranger into public conversation surfaces. The mode only governs whether Ohne surfaces as a speakable entity in `get_virtual_npc_list` — it does not touch how bonds render. And there is no public case to flip to: the mind never speaks as a separate voice — the five bodies are its only mouths ([the-five](../../writeups/the-five.md)). The standing silence rules — a folds-side fence plus the entity's own self-rule — live in the [knowledge phase](../knowledge/_manual_knowledge.md), which also holds the cleanup ladder if the entity ever roleplays a follower.

Console signature if the dashboard fights back: `RegisterVirtualNPC("Ohne", "Ohne", <voiceId>, "private", <language>)` then `EnableVirtualNPC("Ohne")` — verified in `SkyrimNetApi.psc`; returns 0 on success or if it already exists.

Check: ask the chat assistant to render `get_virtual_npc_list` — Ohne must appear, with `conversationMode` reading `private` (last check returned `Count: 0`).

## step 2 — smoke-test the Identity Links UI

Bond creation lives in the dashboard's Identity Links UI — Settings → NPCs → Identity Links, backed by `IdentityLinks.yaml` (form fields reported by the chat assistant's live check: `identityA`/`identityB`, `mode`, `dominance`, `awareness`, `note` — ⚠ confirm on the form). Before committing all 20 bonds to it:

1. create one throwaway bond between two bodied actors — the player-fold and any NPC — with `shared_virtual` = Ohne
2. ask the chat assistant to verify: `get_linked_identities` on both actors must return the full link shape and render the "One Soul, Two Bodies" framing — live proof that bodied-to-bodied bonds work and that Ohne's private flag doesn't interfere
3. remove the test bond

The prompt branch never checks `is_virtual`, so bodied-to-bodied reads as supported — this test settles it. If the UI can't express `shared_virtual` or the framing misrenders, the fallback is overriding `7050_identity_links.prompt` with the bonds hard-coded — a prompt-override job, so decide now and fold it into the first-setup [prompts](../prompts/_manual_prompts.md) pass.

## done

Ohne registered (private), the creation surface proven, the read-back verified. At each recruitment, continue with [identity links — recruit](./_manual_identity-links-recruit.md).
