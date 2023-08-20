AvsPmod Script selector, GPo 20.08.2023

Preliminary:
Some functions in the script selector can only be used meaningfully if the scripts located on the hard disk also have unique names. 
This means not only file 1, file 2 etc.
In my case almost all scripts (2500) have the name of the video file with .avs appended. 
So 'The Midnight Crime Story.mpg' = 'The Midnight Crime Story.mpg.avs'
I have created a tab for each partition where avs files are located with the corresponding partition or folder name (E DVB, E, F, ...).
Still tabs for favorites and a temp tab (Favor, Favor2, Temp) 
Of course you can also use it just as a kind of session file and insert the currently opened AvsPmod tabs.

Functions:
'Add or Update all scripts' Insert or updates all opened AvsPmod scripts (tabs)
'Clear and Add all scripts' Clears the tab and insert all opened AvsPmod scripts (tabs)
'Add or update script' Insert or updated the current AvsPmod script (tab)

'Find or Update from avs...' Searches with sub folders, the last opened dir is saved for the current tab for next use
'Update selection from avs' The selected scripts are updated from avs files on the hard disk (no new files are added)
'Check existing 'Ctrl removes' All scripts in the current tab are checked for being present on the hard disk, if not exists and Ctrl was pressed the script is removed from the tab 

Mouse events:
middle down = find the current AvsPmod script (tab)

List lines mouse events
Name: 
left (22 pixel) if Note then show Note as tooltip
rigth - (22 pixel) show name if auto tooltip disabled
double Click = open script with AvsPmod

Bookmarks:
double Click = open AvsPThumb with bk6/bk3 file or with this script is no bk* file exists

Path:
left (22 pixel) show Path as tooltip if auto tooltip disabled
double Click = open script with AvsPmod

Keyboard events:
ESC = close
del and numpad del = Removes selected scripts from current tab
a to z and 0 to 9 = search for scripts in the current tab
Hot key AvsPmod for open/close Script selector = close

Note for Notes:
Note can be saved Edit > 'Change note'
Or the note is read from the script if #note: is found in the script in the first 10 lines (the line must start with #note:) 

