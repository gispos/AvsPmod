# GPo 2022, AvsPmod macro CopyPixelinfo.py v5
#####
# If simple=False:
#   If multi=True then the macro waits 'timeout' (5 to 60) seconds for a mouse click, if there is no further click the result is output. 
#   Hereby several values (clicks) can be output at once.
#
#   If multi=False then the macro waits 'timeout' (5 to 60) seconds for a mouse click and then outputs the result.
#   The timeout can be canceled by hidden the video window (useful if multi=True).
#     
# If simple=True:
#   Then it only works with shortcut (Pixelinfo depends on the mouse position)
#   No mouse click is waited for, the pixel value under the mouse pointer is copied immediately
#
# If includeXY=False then only the color values are copied (raw)
# Valid values: 'xy', 'hex', 'rgb', 'rgba', 'yuv', 'yuva'
#
# If you don't want to write in the scrap window, set writeToScrap to False
# This is just a template change it to your liking. For more read macros_readme.txt
#####

##### user settings
# set one of the value: 'xy, hex', 'rgb', 'rgba', 'yuv', 'yuva'
colorval = 'hex'
# prefix e.g. for hex '$'
prefix = ''
# wait for multible clicks
multi = False
# timeout for waiting for a mouse click, valide range 5 to 60 seconds
# Note: You can cancel the waiting time by hidden the video window (useful if multi=True)
timeout = 10
# if simple then it only works with shortcut
simple = False
# write to scrap window
writeToScrap = True
# includes also the position
includeXY = True 
# draws a line to each clicked point, only if multi True and not simple
drawLines = False
# give an acoustic signal when done
signal = True
##### end user settings

s = ''
self = avsp.GetWindow()
colors = ('xy', 'hex', 'rgb', 'rgba', 'yuv', 'yuva')
try:
    idx = colors.index(colorval) 
except ValueError:
    avsp.MsgBox('Invalid input value', 'CopyPixelinfo')
    return

def GetValues(info):
    if idx == 0:
        return 'pos%s\n' % str(info)
    try:
        if includeXY:
            return 'pos%s, %s: %s\n' % (str(info[0]), colorval, prefix + str(info[1]))
        return prefix + str(info[1]).replace('(', '').replace(')', '') + '\n'
    except:
        return 'Error\n'

if simple:
    info = self.GetPixelInfo(None)
    s = GetValues((info[0], info[idx])) if idx > 0 else GetValues(info[0])
else:
    if multi:
        lines = avsp.GetPixelInfo(color=colorval, wait=True, lines=drawLines, waitTimeout=timeout)
        if lines:
            for info in lines:
                s += GetValues(info)    
    else:
        s = GetValues(avsp.GetPixelInfo(color=colorval, wait=False, lines=False, waitTimeout=timeout))
        
if s.strip():       
    if writeToScrap:
        avsp.WriteToScrap(s, pos=-1)
    self.SetClipboardText(s.strip())
if signal:
    from wx import _misc
    _misc.Bell()