[← back to the output-entries manual](../_manual.md)

# identity links — initial setup (before recruiting)

> ✓ **names filled in this copy** — [bonds.md](./bonds.md) name columns carry the locked roster (Ingrid, Miya, Neala, Ornella, Svetlana). The **`{uuid}` column remains live**: fetch each body's UUID at recruit time (dashboard or `GetEntityUUID(Actor)`).

Identity links are the 20 directed bonds between the five bodies, rendered by `submodules/character_bio/7050_identity_links.prompt` ([full trace](../../docs/identity-links.md)). Nothing in this phase creates a bond — the bodies don't exist yet, and every bond row needs a real `{uuid}` fetched live at recruit time.

## step 1 — register the virtual entity Ohne

Every bond's `shared_virtual` points at Ohne — the mind all bodies belong to — so the entity must exist before the first bond does.

Surface: the dashboard VirtualEntities config. From console or script, the call is `RegisterVirtualNPC(name, displayName, voiceId, conversationMode, language)` (verified in `SkyrimNetApi.psc`; returns 0 on success or if it already exists), then `EnableVirtualNPC`. The UUID derives from the registration name and is stable across sessions — `GetVirtualNPCUUID("Ohne")` if anything asks for it.

## step 2 — ⚠ verify the link-creation surface live

No Papyrus function creates a link, and nothing outside the prompt files references these fields in the source snapshot — the surface is the dashboard's VirtualEntities config (possibly also MCP, port 8889):

- open VirtualEntities in the dashboard, find link/bond creation
- or ask the chat assistant which identity tools it carries
- smoke-test the branch: one throwaway bond between two bodied actors (player-fold + any NPC) with `shared_virtual` = Ohne — confirm the "One Soul, Two Bodies" framing renders, then remove the test bond. The branch never checks `is_virtual`, so bodied-to-bodied reads as supported, but only a live test settles it
- if no creation surface exists (or the framing misrenders): the fallback is overriding `7050_identity_links.prompt` with the bonds hard-coded — a prompt-override job, so decide now and fold it into the first-setup [prompts](../prompts/_manual_prompts.md) pass

## done

Identity links are set up. At each recruitment, continue with [identity links — recruit](./_manual_identity-links-recruit.md).
