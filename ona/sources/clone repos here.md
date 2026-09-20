okf folder is a nested cluster of concepts in the form of markdowns and subfolders.  it is built referencing the two repos in this source folder, holding links to files

it's designed so that you point your agent framework at the root folder (I use agent zero).  then all you have to say is:

```
see `okf`

(then ask question)
```

there are skills in the okf folder, and the agent will efficiently find references into the repos to help answer your question


-----


since there are file links, the folders under sources need to be named:
- SkyrimNet-GamePlugin
- SeverActions

if you have git installed, type cmd in the windows explorer address to pull up a command window into this sources folder (or cd\ "folder path")

```bash
git clone https://github.com/MinLL/SkyrimNet-GamePlugin.git
git clone https://github.com/Severause/SeverActions.git
```

if you need to download zips instead, unzip into this folder, remove the '-main' from the end of the folder name