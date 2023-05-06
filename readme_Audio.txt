The first AvsPmod version with audio playback. Don't expect too much from the 4K playback, but there is a useful function 'Audio scrubbing'. See below. 

At the moment (I don't know if this will change) the avisynth audio mixer is used for downmix to stereo (I didn't spend any time on own audio downmix code).
The need for an audio mixer is:
The video output channels can only be directly routed to the device output channels (loudspeakers). But if there are only 2 speakers, no audio can be created.
Or if the device output is fixed to 2 speakers, only 2 of maybe 6 channels will be played back.

The audio mixer can be turned on or off under Video > Play video > 'Downmix audio'.

----------
For faster playback:
There is a new option for the 'Resample Filter', you can enter a function after the avisynth resizer separated by a semicolon. 
As default if the options.dat not existing, a Prefetch(1) is used, so Spline36Resize;Prefetch(1)
This gives me 30% more speed when using the 'Resample Filter'. 
Spline36Resize;sharpen(0.2).Prefetch(1) is also posible but makes it through the additional filter slower.

I can playback 4K on a QHD monitor with 'Resample Filter,Prefetch(1)' without audio dropouts (max. ~26 fps). Without resample filter it is not possible.
I think with a 4K monitor audio playback with 4K video will not be possible.

Use 'Split Clip' (avsp_split) to temporarily turn off all subsequent filters for non-stuttering audio playback.
----------

Audio scrubbing:
The number of frames to be played can be selected in the context menu of the play button.
There is also the function 'Play scrub', which plays the audio of 36 video frames. Even if 'Audio scrubbing' is switched off. 
This function should work well in conjunction with 'Split View' for an audio synchronous check (original vs. encoded).
If 'Split View' is activated, the audio of both clips will be played one after the other. With visual display of the currently used clip.

Preview Filter:
Audio scrubbing and audio mixer are turned off. So only video with 2 channel audio can be played back in the playback. 
Or there must be enough device outputs to play all channels. Or you can insert an audio downmix function in the script. 

It is the first version with audio, time will tell if and what can or must be changed.

This audio mixers are used.
You can also use your own mixer and add the function to the script, then no downmix will be used in AvsPmod, and the audio will also work with the 'Preview Filter'. Except scrubbing.
But I can already hear the screaming when someone forgets to remove their own audio downmix before encoding. :-)
channels >= 8:
    'a = ConvertAudioToFloat()'
    'flr = Getchannel(a, 1, 2, 3, 4)'
    'blr = Getchannel(a, 5, 6)'
    'slr = Getchannel(a, 7, 8)'
    'sur = MixAudio(blr, slr, 1.0, 1.0)'
    'mc = mergechannels(flr, sur)'
    'flr = GetChannel(mc, 1, 2)'
    'fcc = GetChannel(mc, 3, 3)'
    'lrc = MixAudio(flr, fcc, 0.3694, 0.2612)'
    'blr = GetChannel(mc, 5, 6)'
    'MixAudio(lrc, blr, 1.0, 0.3694)'
       
channels >= 6:
    'flr = GetChannel(1, 2)'
    'fcc = GetChannel(3, 3)'
    'lrc = MixAudio(flr, fcc, 0.3694, 0.2612)'
    'blr = GetChannel(5, 6)'
    'MixAudio(lrc, blr, 1.0, 0.3694)'
            
channels >= 4:
    'flr = GetChannel(1, 2)'
    'blr = GetChannel(3, 4)'
    'MixAudio(flr, blr, 0.5, 0.5)'
            
channels > 3:
    'flr = GetChannel(1, 2)'
    'fcc = GetChannel(3, 3)'
    'MixAudio(flr, fcc, 0.5858, 0.4142)'
           

And finally, I have a request:
For me, the 4 channel output does not work with Win10, so I have only stereo available, I can not check whether really all channels are read and directly forwarded to the output. 
So if someone has a 6 channel system and hears all 6 channels with the audio mixer turned off, he should let me know so that I no longer have to worry about it.