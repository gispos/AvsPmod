# Version 2.7.7.8 GPo   
- With pinterf (pfmod) modifications   
- Avisynth header version 6 + needed part's from H8,H9   
- For more see changelog   
##### AvsPmod needs write permissions in its own directory. So please do not unzip into a system program directory!   
-----   
### Mouse button combinations (for the new users)   
##### On video window.   
- Press left and right click: changes zoom 100%, 200%   
- Press left and use mouse wheel: changes the zoom   
- Press Ctrl and double click on the video window increases the height a few pixels
- If tab change for mouse browse buttons selected, press Ctrl or move the mouse on the slider area and bookmark jump is used.   
- When the mouse pointer is in the video slider area. Press Ctrl and use mouse browse buttons only trim editor marks would be selected  
- When the mouse pointer is in the video slider area. Press Alt and use mouse browse buttons only bookmarks with title would be selected 

##### On script window:   
- Press left and right click: The # character is removed or added at the beginning of the selected lines 
- If a boolean selected (True, False) the value does change  

##### On slider window:
- If direct slider update enabled (only with preview filters), can then be deactivated by pressing Ctrl on slider move

##### On the status bar:
- A right click open a context menu for the video slider range
   
##### Furthermore   
- On the video slider right click to add or remove a bookmark
- Right click on a marked area in the video slider opens an area menu
- Right click on the play or frame step button opens a selection menu   
- Standard functions for mouse middle button, browse buttons and the wheel can be set under Options.

##### Preview Filter:
- Are an essential part of AvsPmod. They allow near real-time display of filter parameter changes.
- Help > Preview filter example (readme)
   
   
##### Releases GPo:      
<https://github.com/gispos/AvsPmod/releases>
### 
-----  

What is AviSynth?
-----------------

AviSynth is a powerful tool for video post-production.  It provides ways 
of editing and processing videos.  AviSynth works as a frameserver, 
providing instant editing without the need for temporary files.

AviSynth itself does not provide a graphical user interface (GUI), but 
instead relies on a script system that allows advanced non-linear 
editing.  While this may at first seem tedious and unintuitive, it is 
remarkably powerful and is a very good way to manage projects in a 
precise, consistent, and reproducible manner.  Because text-based scripts 
are human readable, projects are inherently self-documenting.  The 
scripting language is simple yet powerful, and complex filters can be 
created from basic operations to develop a sophisticated palette of 
useful and unique effects.


What is AvsP?
-------------

AvsP is at its core a tabbed text editor with features specific for 
creating AviSynth scripts.  It has text editing features such as 
AviSynth-specific syntax highlighting and autocompletion to simplify the 
task of writing scripts.  However, its primary advantage over other 
editors is its integrated video preview, which remains attached to the 
main window at all times.  Comparing the visual results of several 
different scripts is as easy as writing the scripts into several 
different tabs and activating the video preview, switching between tabs 
gives instantaneous feedback on visual differences (anyone remember 
lining up multiple instances of VirtualDub and alt-tabbing?). 
Furthermore, the program offers a unique way for the user to define 
sliders for any number in the script, giving AviSynth a unique graphical 
interface never known before.  The following are an outline of the 
program's main features:

- Tabbed text editor
- Avisynth-specific syntax highlighting and autocompletion
- Integrated video preview for easy script comparison
- Unique user-defined sliders for rapid filter setting comparison
- Built-in crop editor in video preview
- Bookmark any number of frames for quick access
- Complete macro language using the Python programming language
- Graphical front-end for command-line compression tool avs2avi


What is AvsPmod?
----------------

The AvsP project was abandoned by its original author by late 2007.  
AvsPmod is an ongoing community effort to maintain and provide some 
enhancements to AvsP:

- Improved syntax highlighting
- Code folding
- Improved function autocomplete
- Importing of function definitions, including from online wiki
- Snippets of text
- Better Unicode support
- HTML export and printing
- Move, rename, group and undo close tabs
- Video preview usability improvements
- YUV -> RGB options for previewing
- Support for AviSynth 2.6.0 new colorspaces
- Autocrop
- Bookmark titles
- Improved macro API with several scripts included
- Native *nix support through AvxSynth
- Codebase updated to Python 2.7 and wxPython 2.8
- Many bug fixes


Running AvsPmod
---------------

AviSynth, AviSynth+ (Windows) or AvxSynth (*nix) is required.  When 
not using the AvsPmod builds, currently only supplied for Windows, 
the following is also needed:

- Python 2.6-2.7
- wxPython 2.8-2.9
- Additionally for AviSynth+ x86-64 (Windows):
    - cffi module
    - pycparser module
    - Visual Studio 2008
    - avisynth_c.h

In that case start AvsPmod by running avsp.py, i.e. `python -O avsp.py`, 
pythonw recommended on Windows.


Updating to a new version
-------------------------

To update AvsPmod just overwrite the previous files.  Personal preferences 
and customizations are preserved.  However note that edited macro scripts, 
preset files and translations must be backed up first.

In case you want to backup the preferences or clean-up old files not longer 
used, these are the relevant files:

- options.dat: main preferences
- tools/*.dat: tool preferences
- macros/macros.dat: macro preferences
- _last_session_.ses: auto-saved session info

Links GPo forked version
-----
Discussion:
<https://forum.doom9.org/showthread.php?t=175823>

Development:
https://github.com/gispos/AvsPmod

Releases:
https://github.com/gispos/AvsPmod/releases

Links original version
-----

Development:
<https://github.com/AvsPmod/AvsPmod>

Releases:
<https://github.com/AvsPmod/AvsPmod/releases>

Filter database wiki:
<https://github.com/AvsPmod/AvsPmod/wiki/Filter-database>

Discussion: 
<http://forum.doom9.org/showthread.php?t=153248>

AvsP homepage: 
<http://avisynth.nl/users/qwerpoi/>

AviSynth wiki: 
<http://avisynth.nl/index.php/Main_Page>

AvxSynth wiki: 
<https://github.com/avxsynth/avxsynth/wiki>


---------------
<sub>AviSynth description extracted from the AviSynth wiki 
([CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/))</sub>