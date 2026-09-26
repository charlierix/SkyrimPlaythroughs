I pasted a good part of `_manual_identity-links-setup.md` into the ai helper's prompt, its reply is at bottom of the doc

so it looks like those instructions should change to manually creating using virtual entities config

also, there is a public/private setting.  here is what the agent said:
```
On private vs public: I'd keep it private. Here's the reasoning.

First, what the flag actually controls: conversation mode governs whether the virtual is surfaced as a speakable entity in get_virtual_npc_list — private virtuals are only included for authorized requesters (effectively the player), while public ones are broadly available. It's about dialogue participation, not about the identity links themselves. The bonds render through get_linked_identities, which is a separate system.

Why private fits Ohne:

The mind is a secret. Your entire cover-story apparatus (the outsider entry) exists to hide the folds. A public virtual would be an addressable entity the world could interact with — that breaks the fiction. Ohne isn't a character the world meets; it's the substrate the five bodies share.
The bodies are the interface. Per your "how the mind talks" entry, the mind speaks through the bodies — fold talk is the register of the bodies. Ohne rarely (if ever) needs to speak as itself in a public scene.
Private keeps it clean. A public virtual would clutter public conversation surfaces with an entity that isn't meant to be there.
When you'd flip it to public: only if you want Ohne to speak as a distinct voice where others are present — the mind addressing the whole party, or being addressable by NPCs. Given the secretive narrative, I doubt that's what you want. And if you ever want a "voice in the player's head" that only the player-fold hears, private is exactly right.

One honest caveat: I can't yet confirm how private/public interacts with the identity-link rendering, because no bonds exist yet. As far as I can tell the conversation mode and the link data are independent — so I expect private won't affect the link rendering — but the only way to settle it is the smoke test your doc already prescribes: create one throwaway bond, then read it back. Once a test bond exists, I can call get_linked_identities on both actors and confirm the "One Soul, Two Bodies" framing renders regardless of Ohne's private flag. That's the live proof.

Bottom line: keep it private — it matches the narrative and shouldn't compromise the links. Revisit only if you decide Ohne needs to speak publicly as itself.
```

then ask ai helper to verify when that is done

-----

First, the framing mismatch
This section isn't a memories section — it's the identity-links / virtual-entity phase. Nothing in it creates memory rows. What it creates is the shared memory pool: per the get_linked_identities docs, "both selves then share memories and recent-event context according to the link's direction mode." So the 20 bonds are the plumbing that lets the five bodies share one memory pool. The actual implanted memory rows come in a later phase. Worth keeping straight so we don't build the wrong thing.

The doc's step-2 question, answered
The doc literally says "ask the chat assistant which identity tools it carries." I checked. Here's the honest inventory:

Read-only tools I do carry:

get_linked_identities(actorUUID) — a decorator that returns the identity links for an actor. This is the rendering side — it's what feeds 7050_identity_links.prompt. It returns the full link shape: {name, uuid, is_virtual, mode, dominance, host_unaware, is_present, sees_their_memories, they_see_yours, note, shared_virtual}.
get_virtual_npc_list(sourceUUID) — lists enabled virtual NPCs.
Creation tools I do not carry:

There is no create_identity_link / bond tool, and no register_virtual_npc tool in my toolset. I searched for identity, bond, link, soul, virtual, register — the only hits are the two read-only ones above.
So from this assistant's perspective, there is no link-creation surface. The doc's "possibly also MCP, port 8889" branch doesn't show up in my tools.
Conclusion for step 2: the creation surface is dashboard-only — Settings → NPCs → Identity Links (backed by IdentityLinks.yaml, with identityA/identityB, mode, dominance, awareness, note). That matches the doc's primary guess. My role is the read/verify side, not creation.

Step-1 status: Ohne is NOT registered
I rendered the live virtual-NPC list and it came back Count: 0 — there are currently zero enabled virtual NPCs. So RegisterVirtualNPC("Ohne", …) has not been run yet. Step 1 is unstarted.

And here's the catch: I can't do step 1 for you through my tools either. RegisterVirtualNPC / EnableVirtualNPC / GetVirtualNPCUUID live in SkyrimNetApi.psc, which is not among the quest scripts I can reach. The SkyrimNet controller quest (skynet_MainController) exposes skynet_MainController, skynet_MinAIBridge, and skynet_Library — none of which list those functions. So that surface is outside my reach too.

Where that leaves us
Step	Surface	Can I do it?
1 — register + enable Ohne	Dashboard VirtualEntities config, or console (RegisterVirtualNPC/EnableVirtualNPC)	❌ No tool for it
2 — create the 20 bonds	Dashboard Settings → NPCs → Identity Links (IdentityLinks.yaml)	❌ No creation tool; I can read/verify via get_linked_identities
2 — smoke-test "One Soul, Two Bodies" framing	Live test bond, then read it back	✅ I can verify the read side once a bond exists
Fallback — hard-code bonds into 7050_identity_links.prompt	Prompt override	✅ I can help author/validate that prompt
So both of the doc's actionable steps are dashboard jobs, not assistant jobs. My value-add here is:

Verification — once you register Ohne and create a test bond, I can call get_linked_identities on the two actors and confirm the link object comes back correctly (mode, dominance, shared_virtual, etc.), which is the live proof the doc wants.
The fallback — if you decide the prompt-override route instead, I can help draft and validate_prompt the 7050_identity_links.prompt override.
One decision the doc explicitly asks you to make now: "if no creation surface exists (or the framing misrenders): the fallback is overriding 7050_identity_links.prompt with the bonds hard-coded — decide now and fold it into the first-setup prompts pass." Since I've confirmed there's no assistant-side creation surface, the question is whether your dashboard has the Identity Links UI. If it does, use it. If it doesn't, we go the prompt-override route.

Want me to (a) help you check the dashboard path, or (b) start drafting the 7050_identity_links.prompt override as the fallback? And if you'd like, I can register Ohne via console command if you tell me the exact signature you want — though I'd want to confirm the plugin form ID for the API script first, since I couldn't locate SkyrimNetApi on a quest.
