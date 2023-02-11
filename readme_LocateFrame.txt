GPo 2023, AvsPmod function 'Locate frame' https://vimeo.com/797835669

The wonderful 'LocateFrames' function from Doom9 member StainlessS is needed.
https://www.mediafire.com/folder/hb26mthbjz7z6/StainlessS or http://www.sendspace.com/folder/2mwrco

Locate frames searches for the current frame in another clip, but I do not know if anyone will find it useful,
it was more for fun and interest.
I use it to get the same frame from two clips (one shortened or recoded), for Split View synchronization.
If the Split View function is activated, the found frame is displayed and the offset and group are set.

For this function the same video source must be entered in the Split View partner tab. 
The partner tab is the right tab next to the current tab.

Both clips must be initialized in the current script and a variable must be set on the clip to be searched for the frame.
The variable has a fixed name: find_clip

Example main script:
Import("...LocateFrames.avs")
LWLibavVideoSource("E:\Test.mpg")
 
find_clip = LWLibavVideoSource("E:\Test_2.mpg")
find_start = -500 # optional, default -500
find_stop = 500   # optional, default +500
find_mode = 0     # optional autoset, if Split View enabled = 1 else 0
find_thresh= 3.0  # optional, default 3.0
last

Example partner script for the Split View functionality:
LWLibavVideoSource("E:\Test_2.mpg") # the find_clip source

If Split View is not enabled, only the frame property window is displayed and the result is attached:
LF_MODE=0
LF_FOUND=5453     # the found frame number in find_clip
LF_DIFF=0,000000  # the difference to the current frame
LF_OFFSET=453     # the offset to the current frame, can also be negative

If Split View is switched on:
find_mode is then 1 if it is not set to 0 by setting the variable.
The found frame is displayed in the right window and the 'Split View' is synchronized.
This means that a common group and the frame offset are set.
Groups > 'Freeze Split View frame' should then be turned off or when scrolling to another frame, the frame of the non-active tab remains frozen. 

To the optional Variables:
find_start = -500  # can also be positive
if find_mode = 0:
	subtract 500 frames from the current frame position and start the search at this frame number in the find_clip.
if find_mode = 1
	subtract 500 frames from the find_clip frame position and start the search at this frame number in the find_clip.

find_stop = 500
if find_mode = 0:
	500 frames are added to the current frame position and the search is stopped at this frame number.
if find_mode = 1:
	500 frames are added to the find_clip frame position and the search is stopped at this frame number.

In both cases it will stop when a match is 100%.

find_tresh = 3.0
the same as in LocateFrames tresh1 but is not set and handled differently. 
Found frame is only displayed if the difference is less than thresh.
If only one frame with a higher value is found, this will be displayed in the frame properties.

! Do not use any other filters, that slows down the finding process.

