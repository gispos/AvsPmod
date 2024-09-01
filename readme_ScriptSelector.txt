AvsPmod Script selector, GPo 20.08.2023

Preliminary:
Some functions in the script selector can only be used meaningfully if the scripts located on the hard disk also have unique names. 
This means not only file 1, file 2 etc.
In my case almost all scripts (2500) have the name of the video file with .avs appended. 
So 'The Midnight Crime Story.mpg' = 'The Midnight Crime Story.mpg.avs'
I have created a tab for each partition where avs files are located with the corresponding partition or folder name (E DVB, E, F, ...).
Still tabs for favorites and a temp tab (Favor, Favor2, Temp) 
Of course you can also use it just as a kind of session file and insert the currently opened AvsPmod tabs.

Find, Search and Update Functions:
'Add or Update all scripts' Insert or updates all opened AvsPmod scripts (tabs).
'Clear and Add all scripts' Clears the tab and insert all opened AvsPmod scripts (tabs).
'Add or update script' Insert or updated the current AvsPmod script (tab).
'Find current script' finds the current AvsPmod script (tab).
'Find script...' searches for scripts in all tabs and displays found scripts in a separate tab. These tabs should be deleted when they are no longer needed.
'Search in scripts' searches inside all scripts for the given text. These tabs should also be deleted when they are no longer needed.
'Search in Notes...' searches in all Nodes for the given text. These tabs should also be deleted when they are no longer needed.

Probably the most important functions at the beginning:
'Find or Update from avs...' Searches with sub folders, the last opened dir is saved for the current tab for next use.
'Update selection from avs' The selected scripts are updated from avs files on the hard disk (no new files are added).
'Check existing 'Ctrl removes' All scripts in the current tab are checked for being present on the hard disk, if not exists and Ctrl was pressed the script is removed from the tab. 

Find duplicate functions:
'Find dup' find all duplicate names.
'Find dub (same tab)' find all duplicte names in the same tab.
'Find dup (dif)' find all duplicate names with different script text.

Mouse events global:
middle down finds the current AvsPmod script (tab)
double click > 20 pixel selects or opens the script in AvsPmod
Selections can be copied to/into another tab using drag and drop or use Edit > Copy and Paste

Mouse events on the script list items:
Name: 
left down < 22 pixels shows the saved Note as tip window (an asterisk indicates an existing note).
left down (rigth - 22 pixel) shows the name as tip window if auto tooltip disabled
double click < 22 pixels shows MediaInfo if the dll found in the systems or AvsPmod directory.
double click (right - 22 pixels) shows the script in an separate window

Bookmarks:
double click = open AvsPThumb with bk6/bk3 file or with this script is no bk* file exists

Path:
left < 22 pixel displays the path as a tooltip if Auto-Tooltip is deactivated
double click shows the script in an separate window

Keyboard events:
ESC = close
del and numpad del = Removes selected scripts from current tab
a to z and 0 to 9 = search for scripts in the current tab
Hot key AvsPmod for open/close Script selector = close

Note for Notes:
Note can be saved Edit > 'Change note'
Or the Note is read from the script if #note: is found in the script in the first 10 lines (the line must start with #note:) 
If a 'Note' is found in the script, the existing 'Note' is overwritten.

Color Markers and Flag: 
Who wants to use it... it is available .)

Disaster!:
Tab Context Menu 'Disaster! reopen last data'
If you accidentally delete all tabs or make another mistake, DO NOT CLOSE THE WINDOW! but use this menu, 
then the data will be loaded as it was before you started the Script Selector.


