# skyrimnet integration docs

Working docs for wiring the playthrough into SkyrimNet. Design source of truth stays in `../writeups/` — these docs map that design onto SkyrimNet's surfaces.

| doc | question it answers |
| --- | --- |
| [helper-agents.md](./helper-agents.md) | what the dashboard helper agents are, and which prompts back them |
| [what-goes-where.md](./what-goes-where.md) | which content (backstory, memories, diary, topics) goes on which SkyrimNet surface |
| [identity-links.md](./identity-links.md) | how one-mind-many-bodies is modeled — the identity-link system traced to source |
| [overlay-inventory.md](./overlay-inventory.md) | the concrete artifacts to write, and the decisions blocking them |
| [severactions-relationship-stance.md](./severactions-relationship-stance.md) | what SeverActions' relationship machinery does to folds — the decided stance, prewarm floors, and the three overrides |
| [output entries manual](<../output entries/_manual.md>) | the play-time injection manual — what to hand SkyrimNet, folder by folder |

## next steps (candidates)

1. pick the five bodies (vanilla vs custom) — unblocks bios, links, and the memory pool
2. verify the identity-link creation surface live (dashboard VirtualEntities config)
3. fill the output-entries files: profiles, memory pools, knowledge, prompt overrides
4. decided — SeverActions relationship stance: prewarm + fold-gated overrides ([severactions-relationship-stance](./severactions-relationship-stance.md))
