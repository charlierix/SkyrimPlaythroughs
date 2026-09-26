---
type: Actions
title: Basic Actions
description: Everyday item handling, following, book reading, spellcasting and teaching actions of the Basic module.
resource: 'sources/SeverActions/Actions/Basic'
tags: [actions, skyrimnet, items, magic, follow, reading]
timestamp: 2026-09-18T00:00:00Z
---

# Overview

The Basic module (FOMOD option "Basic Actions", recommended) carries the everyday verbs: picking up, giving, taking and consuming items, looting and searching containers and corpses, following the player, reading books and notes aloud, casting and teaching spells and shouts, and transferring property ownership. Each YAML declares `name`, `description`, `questEditorId: SeverActions`, a `scriptName`/`executionFunctionName` pair, `parameterMapping`, an `enabled` flag, and `eligibilityRules` built from SkyrimNet decorators (for example `is_in_combat` and `get_faction_rank`).

The module ships 20 YAMLs — 18 executable actions plus 2 category files that only group actions for the AI's action menu (category files set no execution script).

# Member Actions

| File | Action | Category | Script.Function | Purpose |
|---|---|---|---|---|
| bringitem.yaml | BringItem | items | SeverActions_Loot.BringItem_Execute | Fetch-and-deliver in one motion — pick up a nearby loose item and carry it to the target actor |
| castspell.yaml | CastSpell | magic | SeverActions_SpellCast.CastSpell_Execute | Cast a known spell at a target; restoration heals auto-repeat until the target is whole or the caster runs dry |
| cat_inventory.yaml | Items | items | — | Category file grouping item pickup, give/take, looting and reading actions |
| cat_magic.yaml | Magic | magic | — | Category file grouping casting, teaching and shout actions |
| giveitem.yaml | GiveItem | items | SeverActions_Loot.GiveItem_Execute | Move an item from the speaker's pack into the target's — a gift, payment or handed draught |
| learnspell.yaml | LearnSpell | magic | SeverActions_SpellTeach.learnspell | The speaker takes a spell from the player, who must actually know it |
| lootcontainer.yaml | LootContainer | items | SeverActions_Loot.LootContainer_Execute | Open a chest, sack, barrel, drawer or strongbox and help themselves; locked ones get a lockpicking attempt |
| lootcorpse.yaml | LootCorpse | items | SeverActions_Loot.LootCorpse_Execute | Pull what is worth taking from a body |
| pickupitem.yaml | PickUpItem | items | SeverActions_Loot.PickUpItem_Execute | Grab a loose item lying out in the world — dropped sword, apple, coin, flower |
| readbook.yaml | ReadBook | items | SeverActions_Loot.ReadBook_Execute | Read a book or note aloud from the speaker's or the player's pack; continues until StopReading |
| searchcontainer.yaml | SearchContainer | items | SeverActions_Loot.SearchContainer_Execute | Look through a container without taking anything, so the contents can be judged first |
| searchcorpse.yaml | SearchCorpse | items | SeverActions_Loot.SearchCorpse_Execute | Pat down a body without taking anything |
| startfollowing.yaml | StartFollowing | — | SeverActions_Follow.StartFollowing | Fall into step behind the player when asked to come along (casual follow, not companion sign-up) |
| stopfollowing.yaml | StopFollowing | — | SeverActions_Follow.StopFollowing | Part ways and return to their own business while currently following |
| stopreading.yaml | StopReading | items | SeverActions_Loot.StopReading_Execute | Close the book, stow it, and fall quiet |
| takeitem.yaml | TakeItem | items | SeverActions_Loot.TakeItem_Execute | Accept an item from someone — coin counted at the bar, a key surrendered |
| teachshout.yaml | TeachShout | magic | SeverActions_SpellTeach.TeachShout | Teach one Word of Power of a Shout the speaker themselves knows |
| teachspell.yaml | TeachSpell | magic | SeverActions_SpellTeach.TeachSpell | Walk the player through one of the speaker's own spells |
| transferownership.yaml | TransferOwnership | — | SeverActions_Property.TransferOwnership | Formally hand over a property to the player — deed, keys, home rights |
| useitem.yaml | UseItem | items | SeverActions_Loot.UseItem_Execute | Consume something the speaker carries — potion, food, or a tasted ingredient |

# Eligibility Notes

- ReadBook and StopReading are a pair; the book's real text only surfaces after ReadBook fires (per-actor StorageUtil state read by the prompts — see [/prompts/core.md](/prompts/core.md)).
- CastSpell routes through the animated-cast alias pipeline ([/scripts/magic-travel.md](/scripts/magic-travel.md)).
- TransferOwnership enforces the speaker-owns-property gate in SeverActions_Property, because eligibility decorators cannot see the dynamic propertyName parameter at filter time ([/scripts/core-system.md](/scripts/core-system.md)).
- LearnSpell and TeachSpell check the speaker's known-spell list injected by the prompts ([/prompts/core.md](/prompts/core.md)).
- The FOMOD description for this module also mentions wait/relax verbs; those live in the Follower module's YAMLs today ([/actions/follower.md](/actions/follower.md)).

# Citations

[1] `sources/SeverActions/Actions/Basic/SKSE/Plugins/SkyrimNet/config/actions/*.yaml`
[2] `fomod/ModuleConfig.xml` — Basic Actions plugin description
