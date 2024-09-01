GPo 2023, AvsPmod function 'Locate frame' https://vimeo.com/797835669
Last update 30.08.2024, the old example video is not up to date, no variables or selections more needed.

The wonderful 'LocateFrames' function from Doom9 member StainlessS is needed.
https://www.mediafire.com/folder/hb26mthbjz7z6/StainlessS or http://www.sendspace.com/folder/2mwrco

Locate frames searches for the current frame in another clip, but I do not know if anyone will find it useful, it was more for fun and interest.
I use it to get the same frame from two clips (one shortened or recoded), for Split View synchronization.
If the Split View function is activated, the found frame is displayed and the offset and group are set.

For explanation: The partner script is the right tab next to the current tab.

Both clips must be initialized and match in terms of dimensions and color space.
The frame in the current script (tab) is searched for in the script to the right of it (the partner script).

Out of date, possible but there is now an dialog.
    You can set optional parameters in the current script:
      find_start = -500 # optional default -500, can aslo be positive
      find_stop = 600   # optional default +600
      find_thresh= 3.0  # optional default 3.0 (the higher frames are found that match less (0 = 100% match))
      find_mode = 1     # optional (0 or 1) default 1, 0 should not be used, can cause stop less start errors.

If found frame threshold less then find_thresh, only the frame property window is displayed and the result is attached:
  LF_MODE=1         # the set mode is displayed only if mode 0 are set
  LF_FOUND=5453     # the found frame number in the partner tab (the right one)
  LF_DIFF=0,000000  # the difference to the current frame
  LF_OFFSET=453     # the offset to the current frame, can also be negative

If Split View is switched on:
  The found frame is displayed in the right window and the 'Split View' is synchronized.
  This means that a common group and the frame offset are set.
  'Freeze frame' should then be turned off or when scrolling to another frame, the frame of the non-active tab remains frozen. 

The optional Variables:
  find_start, find_stop: the names should be self-explanatory.

  find_tresh = 3.0
  the same as in LocateFrames thresh but is not set and is handled differently. 
  in the partner script the found frame number is only set if the difference is less than thresh.
  if only one frame with a higher value is found, this will be only displayed in the frame properties.

  find_mode = 0: (should not be used, can couse stop less start errors)
	the start and stop are calculated from the current script frame position.
  find_mode = 1 (default)
	the start and stop are calculated from the partner script current frame position.
  In both cases it will stop when a match is 100%.


! Do not use any other filters, that slows down the compare process.

