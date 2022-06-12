GPo 2022, AvsPmod 'SplitClip'

The 'Split Clip' splits the main clip into 2 clips, this allows you to switch between a fast preview (without filters) and a normal preview.
That's exactly what it's designed for, even though other things are possible, e.g. a quick comparison at different frame positions 
with another filter.

The memory requirement is not much higher than for a single main clip since the second clip is derived from the first.
If filters are also used for the 'SplitClip', this will of course increase the memory requirement.

The split position must be written into the script. Everything after this flag will not be played with the 'SplitClip'.
To create the 'SplitClip' the script must be reinitialized after setting the split position. /**avsp_split**/
 
To remove the 'SplitClip' the first flag (/**avsp_split) must be changed and the script must be reinitialized.
This is not about switching, because that is fast, no it is the complete removal of the 'SplitClip' meant.

Prefered way insert a space: /** avsp_split  (this can be done with mouse button left down and right click)
or insert character: /**#avsp_split or remove an asterisk: /*avsp_split

Only if the start and end flag in a single line: /**avsp_split**/ one comment out is enough: #/**avsp_split**/
otherwise If the 'SplitClip' has filters and you do not comment out all lines there will be a syntax error
and the filters are not disabled.

The 'Resample filter' is supported by the 'SplitClip', 
if a 'Preview filter' is switched on or the script is reinitialized the 'SplitClip' is switched off.
The timeline color indicates that 'SplitClip' is switched on or off.


An example of a split without SplitClip filters:

video=LWLibavVideoSource(SourceFile)
audio=LWLibavAudioSource(SourceFile)
audioDub(video, audio)

/**avsp_split**/     

## The next part is skipped by the SplitClip

QTGMC()
MCTemporalDenoise()
prefetch(4)


### Filters can be included in the SplitClip, then the syntax must look like this:

video=LWLibavVideoSource(SourceFile)
audio=LWLibavAudioSource(SourceFile)
audioDub(video, audio)

/**avsp_split             
Spline36Resize(1920, 1080)
prefetch(2)
**/         

## The next part is skipped by the SplitClip

QTGMC()
MCTemporalDenoise()
Spline36Resize(1920, 1080)
prefetch(4)


### It also goes something like this (only quickly tested (it was not made for that!)):
LWLibavVideoSource(SourceFile_1)

/**avsp_split
LWLibavVideoSource(SourceFile_2)
**/ 

# switches between SourceFile_1 and SourceFile_2

