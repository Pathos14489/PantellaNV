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

# How to Install

I do not recommend manually installing this mod, instead please use the [launcher](https://github.com/Pathos14489/Pantella-Launcher). However if you must, all the scripts on this repo are precompiled, merely download by clcking the Code button, then Download ZIP. The zip downloaded will contain the mod plugin. Install it using your mod manager of choice.

## INI Settings

If you are setting this up following The Best of Times guide, part of the guide is the falloutcustom.ini changes they recommend. These settings are great, except they break Pantella support. To fix it, make sure that these settings are changed:
```
iAudioCacheSize=16384
iMaxSizeForCachedSound=2048
```
to
```
iAudioCacheSize=0
iMaxSizeForCachedSound=0
```
If you do not change these settings, the game will cache the voicelines when it first loads them, and it won't get the latest voicelines that get generated because it'll be using the cached version.