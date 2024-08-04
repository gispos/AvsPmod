Don't expect too much from the 4K playback, but there is a useful function 'Audio scrubbing'. See below. 

For faster playback:
There is a new option for the 'Resample Filter', you can enter a function after the avisynth resizer separated by a semicolon. 
As default if the options.dat not existing, a Prefetch(1) is used, so Spline36Resize;Prefetch(1)
This gives me 30% more speed when using the 'Resample Filter'. 
Spline36Resize;sharpen(0.2).Prefetch(1) is also posible but makes it through the additional filter slower.

I can playback 4K on a QHD monitor with 'Resample Filter,Prefetch(1)' without audio dropouts (max. ~29 fps).
Use Video > Display > 'Fast YUV420 display conversion' or 'Prefetch RGB display conversion' for faster playback.

Use 'Split Clip' (avsp_split) to temporarily turn off all subsequent filters for non-stuttering audio playback.
Or use the D3D Window for faster 4K playback.
----------

Audio scrubbing:
The number of frames to be played can be selected in the context menu of the play button.
There is also the function 'Play scrub', which plays the audio of 36 video frames. Even if 'Audio scrubbing' is switched off. 
This function should work well in conjunction with 'Split View' for an audio synchronous check (original vs. encoded).
If 'Split View' is activated, the audio of both clips will be played one after the other. With visual display of the currently used clip. 


           
