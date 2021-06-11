# GPo 2021, PreviewResize.py
# for Playback, AvsPmod zoom 'Antialiasing' is on playback disabled (to slow)
# if you want to scale down the video on playback and do not like the PointResizer then use this macro
# use it only for scale down (for scale up to slow) and set then AvsPmod zoom to 100%
# it's only for playback with scaling down the preview area useful! (fit or fill window)
# if zoom 0, the size of the current preview area is taken 
# resizer is into the script as preview filter insertet, so you can it switch on or off


self = avsp.GetWindow()
script = self.currentScript
if self.UpdateScriptAVI() is None or not self.previewOK(script):
    avsp.MsgBox('Script not initialized.')
    return  
 
# if False, default settings used
showDialog = True    
# fit the display or make the size larger if you want e.g. border = 20    
border = 0 
# fit only the height   
fitHeight = True 
# if zoom not '0', zoom is used 
zoom = '0'   
# default Resizer
rFilter = 'Spline36Resize'

# read the options
if showDialog:
    rFilter = avsp.Options.get('resizeFilter', rFilter)
    border =  avsp.Options.get('border', border)
    fitHeight = avsp.Options.get('fitHeight', fitHeight)

# list of resizers, change or at resizer but the resizer should be fast (I see no differences ;))
rFilters = (_('Spline16Resize'), _('Spline36Resize'), _('Spline64Resize'), _('BicubicResize'), rFilter)
rZooms =  (_('0.5'), _('0.75'), _('0'), _('1.5'), _('2.0'), '0') 

# dialog
if showDialog:
    labels = [[_('Resize Filter:'), _('Border:')], [_('Fit only height'), _('Use zoom')]]
    defaults = [[rFilters, border], [fitHeight, rZooms]]
    types = [['list_read_only','spin'], ['check', 'list_read_only']]
    entries = avsp.GetTextEntry(labels, defaults, _('Resise options'), types)
    if not entries:
        return
    # save the options
    rFilter, border, fitHeight, zoom = entries
    avsp.Options['resizeFilter'] = rFilter
    avsp.Options['border'] = border
    avsp.Options['fitHeight'] = fitHeight
    
cSize = self.videoWindow.GetClientSize()
cSize[1] += border -10 
cSize[0] += border -10
vW, vH = script.AVI.DisplayWidth, script.AVI.DisplayHeight
ratio = float(vW)/vH

if zoom == '0':
    factorWidth = float(cSize[0]) / vW
    factorHeight = float(cSize[1]) / vH
    if fitHeight or factorWidth >= factorHeight:
        H = int(float(cSize[1])/2)*2
        W = int(float(H)*ratio/2)*2
    else:
        W = int(float(cSize[0])/2)*2
        H = int(float(W)/ratio/2)*2
else:       
    W = int(vW* float(zoom))/2*2
    H = int(vH* float(zoom))/2*2

txt = '\n\n/**avsp_filter previewResize\n%s(%i, %i)\n**/\n' % (rFilter, W, H)  
pos = len(script.GetText().rstrip())
avsp.InsertText(txt, pos=pos)
self.zoomfactor = 1
self.zoomwindow = False
self.zoomwindowfit = False
self.zoomwindowfill = False
if self.previewOK() and self.previewWindowVisible:
    avsp.ShowVideoFrame()
# now you must set the preview filter in AvsPmod