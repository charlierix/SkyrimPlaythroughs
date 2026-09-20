# SkyrimPlaythroughs
SkyrimNet manages llm calls for npcs.  This has prompt replacements for custom playthroughs

I use agent zero as my agent framework, which has a concept of projects.  Subfolders under this repo are meant to be the contents of a project

Even if you don't like the plot of my writeup, this is a good model for making your own, the steps to follow:

1. clone repos into `sources` folder
2. ask agent to verify and repair `okf` and `docs`, since repos will probably be newer versions
3. touch up or completely rewrite the `writeups` section
4. have your agent framework build a new `output` folder based on your writeup
> prompt: "see `okf`, `docs`, `writeups`.  please generate `output` based on how `output entries` was built"
5. play the new game from a cloned mo2 folder, so you don't affect current playthroughs.  inject the prompts as specified in the `output` folder

# folders

| folder | description |
| --- | --- |
| ona | a single mind split into the player and 4 followers (kind of like the borg), prompts engourage group think and cooperation |