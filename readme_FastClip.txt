GPo 2023, AvsPmod 'Fast Clip', https://vimeo.com/user183482922

Options > 'Use Ultra Fast Clip'

If you don't know the 'Split Clip', please read the SplitClip readme beforehand.

The flag is the same as for 'Split Clip', but Split Clip does not need to be switched on, only the flag /**avsp_split**/ is required.
If /**avsp_split**/ is found in the script, a 'Fast Clip' can be created. 

In the normal case /**avsp_split**/ should be set after the SourceFilters and after audioDub(video, audio). 
You can also include heavy filters (set the heavy filters before the flag), but then the filters cannot be changed without reinitializing the 'Fast Clip'.

Test it yourself (with and without 'Fast Clip'):
After /**avsp_split**/ comment out a filter or switch it on again or change the parameters and reinitialise the script in between.

This means, for example:
That with a large video file that requires a long index process, a simple filter change such as sharpen(0.4) only takes milliseconds to set the new filter.
If there are several filters after /**avsp_split**/, the effort for each filter is of course required. 

Hint:
If a change is made before /**avsp_split**/ or a change is made in the 'Split Clip' filter, so:
/**avsp_split
sharpen(0.4) # > this is the Split Clip filter, it is used only when 'Split Clip' is enabled.
**/

then the Fast Clip is switched off until no changes are made there. 
This includes blanks, it is a native comparison function designed for speed. 
Only lines that begins with # are ignored. But remove or add a line disables the Fast Clip.

To update the part before /**avsp_split**/ there are the following possibilities:
With F5
Tab context menu 'Reload script'
Make a change in the script before /**avsp_split**/ or in the 'Split Clip' filter part, see above.
Release the script
Disable 'Use Ultra Fast Clip'
Comment out /**avsp_split**/ ( #/**avsp_split**/ )

And another big Hint: 
If you set variables after the flag, e.g var1 = True, then this variable is removed only when the complete script is reinitialized (see above). 
If the variable is only commented out, it remains valid. 

##################################################
var1 = 1
var2 = var1 + 1
result is 2

var1 = 2
var2 = var1 + 1
result is 3

#var1 = 2     commented out, but still in memory
var2 = var1 + 1
result is 3
###################################################

So remember: 
Everything before the flag is always reinitialized when it is changed. Everything after the flag can be used to create a Fast Clip.
However, the flag must not be in an 'if else' statement! And if __end__ or return is found before the flag, no Fast Clip can be created.