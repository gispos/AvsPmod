GPo 2021, AvsPmod resample filter

Resample (resize) filter:
The resample filter is intended to reduce the video dimensions or, in exceptional cases, to enlarge it in order to be able 
to assess the quality better (antialiasing is deactivated when the resize filter is activated). 
It can also be used for better visible quality playback if the preview dimension needs to be adjusted.

It behaves in the same way as if a resizer is used in the script, with the difference that the resize factor is changed dynamically.
mod 2 is used, with the exception of the yv411 color format, then mod 4 is used. 
 
!! You must first enable the resample menu under Program options > Misc 2 > 'Show resample zoom menu'

The Avisynth resizer can be entered under Options > 'Resample filter...' (only the name, no parameters, default 'Spline36Resize').
The resize factor can be selected in the zoom menu (fit,fill,50%,75%, 200% !) for all scripts (tabs) or 
only for the current tab if control is pressed when selecting the menu.
or:
Double click on the top right or bottom right of the video window (50x50 pixels * DPI scaling).
Then the last globally changed value (fit or fill) is used, 'fit' is default at startup. 
If you double click above, the change only affects the current script.
If you double click below it affects all scripts (tabs).
or:
In the upper area, press the left mouse button and zoom with the mouse wheel. 
or:
Hold down the Shift key and use the mouse wheel. The zoom changes in 10% steps from 10 to 200% 

If fit or fill is selected, a new calculation of the dimension can be brought about by clicking on the script / video window separator.
Normally this is never needed, at the moment only when the size of the program window is changed. 

The normal zoom can still be used with the mouse (left down and right click or mouse wheel). But then 'Antialiasing' is active is it enabled.
 
There are two options for deactivating the resize filter:
1.) double click again on the upper or lower area (if a fixed zoom was set, a double click must follow).
2.) select a normal zoom factor with the keyboard (shortcut) or the video window context menu

If not 'Save view pos on tab change' or 'Save pos & zoom on tab change' enabled then all tabs disables the resize filter.

Certain functions are not possible with the resample filter: 
Crop dialog, read pixel values from avisynth.

If a resize is active this is indicated in the status bar with an 'r' in front of zoom and dimensions. And with a green triangle at the top left.  

* Big Note: 
- If Avisynth is trimmed too much with SetMemoryMax, all AvsPmod filters will take longer. 
- The Resample filter normally takes less than 1 second, but if the Avisynth memory is reduced too much, it can take 10 seconds. 

