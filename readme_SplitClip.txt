GPo 2022, AvsPmod 'Split Clip'

The 'Split Clip' splits the main clip, this allows you to switch between a fast preview (without filters) and a normal preview.
That's exactly what it's designed for, even though other things are possible, e.g. a quick comparison at different frame positions 
with another filter without having to create a new tab.

The memory requirement is not much higher than for a single main clip since the second clip is derived from the first.
If filters are also used for the 'Split Clip', this will of course increase the memory requirement.

The 'Split Clip' is fully integrated (preview filter, pixel values, video information, frame properties, etc.),
but the matrix can only be read if the 'Split Clip' enabled on refreshing the script, or use the frame properties to get the Matrix.
So, after a script refresh, the Matrix is always read from the active clip.

!! Do not set a 'Preview filter' area in a 'Split Clip' area and vice versa, this will cause an error.
!! It is recommended not to comment out lines with /* in a 'Split Clip' or 'Preview filter' area, use only #
!! The flag must not be in an 'if else' statement! And if __end__ or return is found before the flag, no Split Clip can be created.

The split position must be written into the script. Everything after this flag will not be played with the 'Split Clip'.
To create the 'Split Clip' the script must be reinitialized after setting the split position. /**avsp_split**/
 
To remove the 'Split Clip' the first flag (/**avsp_split) must be changed and the script must be reinitialized.
This is not about switching, because that is fast, no it is the complete removal of the 'Split Clip' meant.

Prefered way insert a space: /** avsp_split  (this can be done with mouse button left down and right click)
or insert character: /**#avsp_split or remove the 'Split Clip' area completely.

Only if the start and end flag in a single line: /**avsp_split**/ one comment out is enough: #/**avsp_split**/
otherwise if the 'Split Clip' has filters and you do not comment out all lines there will be a syntax error
and the filters are not disabled.

Under Video > Additional > 'Restore split clip if enabled' you can select should 'Split Clip' restored after a script refresh.
The timeline color indicates that 'Split Clip' is switched on or off. You can change the color in the context menu of the frame text field.

You can insert a 'Split Clip' under Edit > Insert > 'Split Clip'.
For me I have entered /**avsp_split**/ after the sourcfilter for all my source templates.

Note: 
If 'Split Clip' is switched on or off for the first time after a frame change, the required time is the time the filters needs for the new frame.


### An example of a split without 'Split Clip' filters:

video=LWLibavVideoSource(SourceFile)
audio=LWLibavAudioSource(SourceFile)
audioDub(video, audio)

/**avsp_split**/     

## The next part is skipped by the 'Split Clip'
QTGMC()
MCTemporalDenoise()
prefetch(4)


### Filters can be included in the 'Split Clip', then the syntax must look like this:

video=LWLibavVideoSource(SourceFile)
audio=LWLibavAudioSource(SourceFile)
audioDub(video, audio)

/**avsp_split             
Spline36Resize(1920, 1080)
prefetch(2)
**/         

## The next part is skipped by the 'Split Clip'
QTGMC()
MCTemporalDenoise()
Spline36Resize(1920, 1080)
prefetch(4)

### You can compare filters without having to create an extra tab:
LWLibavVideoSource(SourceFile)
/**avsp_split
MCTemporalDenoise()
prefetch(4)
**/
MCDegrainSharp()
prefetch(4)

### It also goes something like this (but only quick testet):
# switches between SourceFile_1 and SourceFile_2

LWLibavVideoSource(SourceFile_1)
/**avsp_split
LWLibavVideoSource(SourceFile_2)
**/ 


