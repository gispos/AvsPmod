Accessing in threads to clip create/release and get frame.
on/off: Options menu > 'Accessing AviSynth in threads'

This option takes precedence for Playback in threads. So if this option is set, the playback is also performed with threads.

A user has reported that the threads lead to an immediate crash (CPU without AVX extended command). 
If the threads are causing problems on your system then you have to turn it off. 

On my system (Win10) initializing a clip with threads is about 15% faster and provides more security.
Under Program Options > Misc 2 > 'Hide thread progress dialog' you can hide the progress dialog and showing when pressing Ctrl.
Under Program Options > Misc 2 > 'Delay befor thread progress dialog appears' you can set the delay time. 

If a clip thread is canceled by the user while loading, it remains until the clip is returned by avisynth.
Only when the thread has internally finished (avisynth has returned) can an attempt be made to reinitialize the clip.
The same with frames, a new frame can only be requested when the frame thread has finished.

For clip threads:
 If the thread is canceled by the user and the thread terminates later, an attempt is made to release the now abandoned clip (new option see below).
 If the clip is released, a message appears in the status bar and it buzzes 2 times. Then the clip can be reinitialized (memory has been released).
 Otherwise, it is better to restart the program.

The whole should only be used for more script security. So that you can save your scripts even after a hanging avisynth. 

* New option Options > 'On cancel assign the clip later'
 AvsPmod should normally be closed after a thread has been canceled by the user. 
 this option tries to assign the clip to the script after the user has canceled the thread and the thread has been terminated internally.
 nice for indexing, you can cancel the thread and working with another tab and a message appears if the clip process finished.
 but test it, it's a bit alpha or beta or whatever. It's going smoothly for me, but you never know what the user is doing.

* New option Options > 'Use advanced frame thread'
Normally a new thread is created for each frame that is loaded. 
If this option is activated (default), only one thread is created for each script that waits in the background for a frame to be loaded. 
In terms of speed, this option is a little faster on my system. But test it yourself.

Another note about accessing Avisnth in threads:
 Even with threads it is easy to crash AvsPmod, the avisynth.dll is coupled with the main thread, 
 if an error is triggered by a plugin and the plugin or avisynth crashes, AvsPmod is also torn into the abyss. 
 The threads only help if avisynth does not return.
 Use program options > Save/Load > 'Backup session when previewing' and the accesses in threads to minimize the risk of losing the script.