Direct 3D Window
-----------------
The D3D Window is mainly intended for UHD playback, when the normal drawing is too slow for that.
At the moment all color formats (except RGB32) are displayed in YUV420P8.
YUY2 is slower than YUV420P8 in my test when rendering directly, so it is also converted to YUV420P8.
The matrix is taken over from the current matrix when opening the window.

AvsPmod filters (Display Filter, Preview Filter) cannot be used, only 'Split Clip' is supported or the clip itself must be RGB32.
Unfortunately, there are some problems with the keyboard shortcuts.
Not all events of the keyboard are recognized, so I had to fix the shortcuts.

Existing functions and shortcuts: 
double click = fullscreen or not or toggle fullsize/fullscreen
mouse forward-backward = bookmark next-previous
mouse wheel = frame step 
numpad 4,5 = frame step
numpad 2,8 = jump custom units
numpad 0 or numpad . or middle mouse = Close
minus key = toggle 'Split Clip'
key b = add or remove bookmark 

Video Window Double Click Layout (not D3D Window)
-------------------------------------------------
On the left side (width 50 pixels):
___
d3d fullscreen (top start, 0)
___
normal fullscreen (top start, 51 pixel), is fullsize then switch between fullsize/fullscreen.
___
normal fullsize (top start, half height)
___
d3d fullsize (top start, height - 50 pixel)
___


Doubel click layout right, width -50 pixel:
___
Resample Filter current script (top start, 0)
___
normal fullscreen (top start, 51 pixel)
___
normal fullsize (top start, half height)
___
Resample Filter all scripts (top start heigth -50 pixel)
(Read the resample filter readme under help)
