
Automatic zoom in fullscreen mode.
Program options > Misc2 > 'Fullscreen zoom', None, Normal, Resample, default Normal
Note: Resample only works when the resample function is enabled. (Program Options > Misc2 > 'Show Resample zoom menu')

None:
Nothing happens. If the 'Save pos & zoom on tab change' option is checked, the previous fullscreen zoom will be restored for that tab.

Normal zoom:
Resample filters of the tab are turned off and zoom 'fill' is set.
If you don't change tab in Fullscreen, all other tabs will keep the zoom if 'Save pos & zoom on tab change' is checked.
If you switch tabs and this tab has a resample zoom, the resample function is disabled and this tab is set to zoom 'fill' when you exit full screen mode.
All other tabs keep their zoom if 'Save pos & zoom on tab change' is on.

Resample zoom:
If Fullscreen is started and ended with the same tab, the zoom that existed before the fullscreen mode is restored.
If a tab is changed in Fullscreen mode, this tab will retain the resample filter even after Fullscreen mode is ended. 

Big Note: 
- If Avisynth is trimmed too much with SetMemoryMax, all AvsPmod filters will take longer. 
- The Resample filter normally takes less than 1 second, but if the Avisynth memory is reduced too much, it can take 10 seconds.

