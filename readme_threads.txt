Access in threads to clip create/release and get frame.
on/off: Options menu > 'Access Avisynth in threads'

This option takes precedence for Playback in threads. So if this option is set, the playback is also performed with threads.

A user has reported that the threads lead to an immediate chrash (CPU without AVX extended command). 
If the threads are causing problems on your system then you have to turn it off. 

Under Help > 'Active video thread count' you can find running threads.
Mostly only the clip threads that were canceled. So normally 0 should be printed. The output is printed in the Scrap window.
If a larger number is outputted here than threads that you canceled yourself, please report this.

For example, if a clip thread is canceled while loading, it remains until the clip is returned by avisynth.
Only when the thread has ended can an attempt be made to reinitialize the clip.
The same with frames, a new frame can only be requested when the frame thread has finished.

For clip threads:
If the thread is canceled by the user and the thread terminates later, an attempt is made to release the now abandoned clip.
If the clip is released, a message appears in the status bar and it buzzes 3 times. Then the clip can be reinitialized (memory has been released).
Otherwise, it is better to restart the program.

The whole should only be used for more script security. So that you can save your scripts even after a hanging avisynth. 