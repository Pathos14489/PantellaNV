# PantellaNV
> Bring Fallout New Vegas NPCs to life with AI

<img src="./img/pantella_logo_github.png" align="left" alt="Pantella logo" width="150" height="auto">

This repository is for the PantellaNV mod, which handles the FalloutNV-side logic of Pantella. For the main Pantella repository, see [here](https://github.com/Pathos14489/Pantella).

The source code for the subtitles plugin can be found [here](https://github.com/swwu/Mantella-Subtitles-Plugin-NG).

Doesn't currently support behaviors, multiNPC conversations or radiant conversations. Just single NPC to player conversations.

# Required Mods

- [xNVSE 6.4.4](https://github.com/xNVSE/NVSE/releases) or greater (might work with older versions, no idea really)
- [JIP LN NVSE Plugin](https://www.nexusmods.com/newvegas/mods/58277)
- [ShowOff xNVSE Plugin](https://www.nexusmods.com/newvegas/mods/72541)
- [JohnnyGuitar NVSE](https://www.nexusmods.com/newvegas/mods/66927)

# Supported Mods
- [Tale of Two Wastelands 3.4](https://thebestoftimes.moddinglinked.com/index.html) - Includes character cards and a seperate plugin for TTW support. If you are using TTW, make sure to enable the TTW version of the plugin, not the FNV version and set ttw_enabled to true in the backend when it asks you to during first time setup, or by changing the setting in the falloutnv_config.json file in the configs directory.

# How to Install - Launcher (Recommended fr Windows)

1. This guide presumes that you're following the launcher installation guide and you were directed here from the launcher guide. If you were not, I recommend following the launcher installation guide instead of the manual installation guide, which can be found [here](https://github.com/Pathos14489/Pantella).
2. Install the required mods listed above in your mod manager of choice and enable them. If you're installing TTW, this is where you would install it as well.
3. Make sure the following INI settings are set in your falloutcustom.ini file:
```
iAudioCacheSize=0
iMaxSizeForCachedSound=0
```
If you do not change these settings, the game will cache the voicelines when it first loads them, and it won't get the latest voicelines that get generated because it'll be using the cached version.
4. Follow the rest of the launcher installation guide to install the PantellaNV plugin and set up the backend.
5. When first starting a save you intend to use Pantella in, please create your character, save and then load your save to finish the initialization for that save. You will need to do this for every save you want to use Pantella in, but only once per save unless you use the console to change your character race or name. In which case, please redo this process after you have finished changing your character. After that, you can just load the save and start playing.

# How to Install - Manual (Recommended for Linux)

1. All the scripts on this repo are precompiled. Download by clicking the Code button, then Download ZIP. The zip downloaded will contain the mod plugin. Install it using your mod manager of choice.
2. Install the required mods listed above in your mod manager of choice.
3. Make sure the following INI settings are set in your falloutcustom.ini file:
```
iAudioCacheSize=0
iMaxSizeForCachedSound=0
```
If you do not change these settings, the game will cache the voicelines when it first loads them, and it won't get the latest voicelines that get generated because it'll be using the cached version.
4. Enable the plugin in your mod manager. If you are using TTW, make sure to enable the TTW version of the plugin, not the FNV version.
5. When first starting a save you intend to use Pantella in, please create your character, save and then load your save to finish the initialization for that save. You will need to do this for every save you want to use Pantella in, but only once per save unless you use the console to change your character race or name. In which case, please redo this process after you have finished changing your character. After that, you can just load the save and start playing.
# Controls
H - Adds an NPC to the conversation. Currently only single NPC to player conversations are supported.
B - Opens the text input menu
Backspace - Ends all ongoing conversations. Use this if you want to end a conversation early or if an NPC gets stuck in a conversation loop or if the Pantella backend crashes and you want to end the conversation without reloading your save.