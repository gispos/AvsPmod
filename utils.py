#-------------------------------------------------------------------------------
# Name:        utils
# Purpose:
#
# Author:      GPo
#
# Created:     04.04.2021
# Copyright:   (c) GPo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import os
import wx
import ctypes
import threading
import re

# The frequency of the performance counter is fixed at system boot and is consistent across all processors.
_queryPerformanceFrequency = ctypes.c_int64()
ctypes.windll.Kernel32.QueryPerformanceFrequency(ctypes.byref(_queryPerformanceFrequency))


resource_str_threadwait = _("Waiting for Avisynth, thread still running.\n" \
                            "This dialog is automatically closed when avisynth returns.\n" \
                            "If you abort this process, you should restart the program!")

resource_str_threadwait2 = _("Waiting for Avisynth, thread still running.\n" \
                             "This dialog is automatically closed when avisynth returns.\n" \
                             "If you abort this process, the clip will assign later.")

resource_str_displayfilter = ("## you can run short macro with line start: #>\n"
                              "## or run a macro file by adding #>macro>MacroFilename.py\n"
                              "## Below resample example with fixed height\n\n"
                              "#>avsp.GetWindow().OnMenuVideoZoom(zoomfactor=1)\n"
                              "w=float(last.Width())\n"
                              "h=float(last.Height())\n"
                              "# set fixed height\n"
                              "ch = 920\n"
                              "ch = ch/4*4\n"
                              "Spline36Resize((round(ch*(w/h))/4)*4, ch)")

#resource_str_displayfilter_warn = _("You cannot change the display filter when the preview filter is switched on")

emptySnapShot = [-1, None, "", 0] # FrameNr, Bitmap, script, previewFilterIdx

"""
WIN_10 = (10, 0, 0)
WIN_8 = (6, 2, 0)
WIN_7_SP1 = (6, 1, 1)
WIN_7 = (6, 1, 0)
WIN_SERVER_2008 = (6, 0, 1)
WIN_VISTA_SP1 = (6, 0, 1)
WIN_VISTA = (6, 0, 0)
WIN_SERVER_2003_SP2 = (5, 2, 2)
WIN_SERVER_2003_SP1 = (5, 2, 1)
WIN_SERVER_2003 = (5, 2, 0)
WIN_XP_SP3 = (5, 1, 3)
WIN_XP_SP2 = (5, 1, 2)
WIN_XP_SP1 = (5, 1, 1)
WIN_XP = (5, 1, 0)
"""

def get_winversion():
    if os.name != 'nt':
        return 0
    wv = sys.getwindowsversion()
    if hasattr(wv, 'service_pack_major'):  # python >= 2.7
        sp = wv.service_pack_major or 0
    else:
        import re
        r = re.search("\s\d$", wv.service_pack)
        sp = int(r.group(0)) if r else 0
    #### get ver
    if wv.major < 6 or wv.minor < 1:
        return 6
    elif wv.major == 10:
        return 10
    elif wv.major == 6 and wv.minor > 1:
        return 8
    else:
        return 7
    #return (wv.major, wv.minor, sp)

def GetAvisynthVersion(env, VersionString):
    try:
        if env:
            if not env.check_version(8):
                raise
            re = VersionString.lower().find('avisynth+ ')
            if re < 0:
                raise
        sp = VersionString.split(' ')
        if len(sp) < 2:
            raise
        s = sp[1].replace('.', '')
        if not s.isdigit():
            raise
        if int(s) < 371:
            raise
    except:
        return 0
    return int(s)

def GetAvisynthRelease(VersionString):
    try:
        sp = VersionString.split('(r')
        if len(sp) > 1:
            sp = sp[1].split(',')
            if len(sp) > 1:
                if sp[0].strip().isdigit():
                    return int(sp[0].strip())
    except:
        return 0
    return 0

"""
def writeLog(s):
    nfile = os.path.join('E:\\Temp', 'AvsPmod.log')
    with open(nfile, 'w') as f:
        f.write(s)
"""

def GetScrollbarMetric_X():
    return wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X)

def GetScrollbarMetric_Y():
    return wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_Y)

# found no other way do get client size with the scrollbars (if scrollbar visible), or must check if scrollbar visible
def GetSizeWithoutBorder(wnd):
    return wx.Size(wnd.GetSize()[0]-wx.SystemSettings.GetMetric(wx.SYS_BORDER_X)*2, wnd.GetSize()[1]-wx.SystemSettings.GetMetric(wx.SYS_BORDER_Y)*2)

avsRGB = '"RGB24"/ "RGB32"/ "RGB48"/ "RGB64"'

avsRGBP = '"RGBP8"/ "RGBP10"/ "RGBP12"/ "RGBP14"/ "RGBP16"'
avsRGBAP = '"RGBPA8"/ "RGBAP10"/ "RGBAP12"/ "RGBAP14"/ "RGBAP16"'

avsYUV = '"YV12"/ "YUV420P10"/ "YUV420P12"/ "YUV420P14"/ "YUV420P16"/\
 "YV16"/ "YUV422P10"/ "YUV422P12"/ "YUV422P14"/ "YUV422P16"/\
 "YV24"/ "YUV444P10"/ "YUV444P12"/ "YUV444P14"/ "YUV444P16"'

avsYUVA = '"YUVA420P8"/ "YUVA420P10"/ "YUVA420P12"/ "YUVA420P14"/ "YUVA420P16"/\
 "YUVA422P8"/ "YUVA422P10"/ "YUVA422P12"/ "YUVA422P14"/ "YUVA422P16"/\
 "YUVA444P8"/ "YUVA444P10"/ "YUVA444P12"/ "YUVA444P14"/ "YUVA444P16"'

avsY = '"Y8"/ "Y10"/ "Y12"/ "Y14"/ "Y16"'

avs_RGB_RGBP_YUV = avsRGB + '/ ' + avsRGBP + '/ ' + avsYUV
avs_RGB_RGBP_YUV_Y = avs_RGB_RGBP_YUV + '/ ' + avsY
avs_RGB_RGBP_Y_YUV = avsRGB + '/ ' + avsY + '/ ' + avsYUV

avsRGBP_s = ('"RGBP*" 8/10/12/14/16')
avsY_s = '"Y*" 8/10/12/14/16'
avsYUV_s = '"YUV420P*" "YUV422P*" "YUV444P*" 8/10/12/14/16'
avsY_YUV_s = '"Y*" 8/10/12/14/16 - "YUV420P*" "YUV422P*" "YUV444P*" 8/10/12/14/16'


# wildcards: ? and *
def FindPattern(find, text):
    if len(find) == 0 and len(text) == 0:
        return True
    if len(find) > 1 and find[0] == '*':
        i = 0
        while i+1 < len(find) and find[i+1] == '*':
            i = i+1
        find = find[i:]
    if len(find) > 1 and find[0] == '*' and len(text) == 0:
        return False
    if (len(find) > 1 and find[0] == '?') or (len(find) != 0
            and len(text) != 0 and find[0] == text[0]):
        return FindPattern(find[1:], text[1:])
    if len(find) != 0 and find[0] == '*':
        return FindPattern(find[1:], text) or FindPattern(find, text[1:])
    return False

# wildcard only *
def FindPattern_Fast(find, text):
    sl = find.split('*')
    found = 0
    for i in range(len(sl)):
        if text.find(sl[i]) < 0:
            break
        found += 1
    return found == len(sl)

def GetKeyShortCut(label, shortcuts):
    for itemName, shortcut, id in shortcuts:
        if itemName.endswith(label):
            accel = wx.GetAccelFromString('\t'+ shortcut)
            if accel and accel.IsOk():
                return accel.GetKeyCode()

def IsAVX2():
    def is_set(leaf, subleaf, reg_idx, bit):
        import cpuid
        cpu = cpuid.CPUID()
        if not cpu.initialized:
            cpu = None
            return None
        regs = cpu(leaf, subleaf)
        cpu = None
        if (1 << bit) & regs[reg_idx]:
            return True
    return is_set(7, 0, 1, 5)

class RepeatTimer(threading.Thread):
    def __init__(self, interval, function, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()
    def cancel(self):
        self.finished.set()
    def setInterval(self, interval):
        self.interval = interval
    def run(self):
        while not self.finished.is_set():
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
        self.finished.set()

class WaitTimer(threading.Thread):
    def __init__(self, wait, function, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = True
        self.wait = wait
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()
    def cancel(self):
        self.finished.set()
    def run(self):
        while not self.finished.is_set():
            self.finished.wait(self.wait)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                return

# high-resolution counter 1ms
def milli_seconds():
    tics = ctypes.c_int64()
    ctypes.windll.Kernel32.QueryPerformanceCounter(ctypes.byref(tics))
    return tics.value*1e3/_queryPerformanceFrequency.value

# more accurate than wx.Millisleep()
def milli_delay(delay):
    fin = (milli_seconds() + delay)%(1<<32)
    while milli_seconds() < fin:
        pass
# high-resolution counter < 1 micro
def micro_seconds():
    tics = ctypes.c_int64()
    ctypes.windll.Kernel32.QueryPerformanceCounter(ctypes.byref(tics))
    return tics.value*1e6/_queryPerformanceFrequency.value

def micro_delay(delay):
    fin = (micro_seconds() + delay)%(1<<32)
    while micro_seconds() < fin:
        pass

def GetById(ID):
    return ctypes.cast(id(ID), ctypes.py_object).value

# idx = tuple index (xlist.sort(key=sort_alphanumeric(0))
def sort_alphanumeric(idx=-1):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    if idx >= 0:
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key[idx])]
    else: alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return alphanum_key

def FileSizeToString(filename, precision=0, maxsuffix='TB'):
    fsize = os.path.getsize(filename)
    if fsize < 1:
        return '0 B'
    suffixes = ['B','KB','MB','GB','TB']
    suffixIndex = 0
    while (fsize > 1024) and (suffixIndex < 4) and (maxsuffix != suffixes[suffixIndex]):
        suffixIndex += 1
        fsize = fsize/1024.0
    if suffixIndex > 2 and precision == 0:
        precision = 2
    return '%.*f %s' % (precision, fsize, suffixes[suffixIndex])

# Id generation for menus or...
import itertools
NewIdGen = itertools.count()
def NewId():
    return NewIdGen.next()
"""
# Python program for A modified Naive Pattern Searching
# algorithm that is optimized for the cases when all
# characters of pattern are different
def search(pat, txt):
    M = len(pat)
    N = len(txt)
    i = 0

    while i <= N-M:
        # For current index i, check for pattern match
        for j in range(M):
            if txt[i + j] != pat[j]:
                break
            j += 1

        if j == M:    # if pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            print ("Pattern found at index " + str(i))
            i = i + M
        elif j == 0:
            i = i + 1
        else:
            i = i + j    # slide the pattern by j

# Driver program to test the above function
txt = "ABCEABCDABCEABCD"
pat = "ABCD"
search(pat, txt)

class MyProgressDialog(wx.Dialog):
    def __init__(self, parent, id, title, text=''):
        wx.Dialog.__init__(self, parent, id, title, size=(200,150), style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)

        self.text = wx.StaticText(self, -1, text)
        self.gauge = wx.Gauge(self, -1)
        self.closebutton = wx.Button(self, wx.ID_CLOSE)
        self.closebutton.Bind(wx.EVT_BUTTON, self.OnClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text, 0 , wx.EXPAND)
        sizer.Add(self.gauge, 0, wx.ALIGN_CENTER)
        sizer.Add(self.closebutton, 0, wx.ALIGN_CENTER)

        self.SetSizer(sizer)
        self.Show()

    def OnClose(self, event):
        self.Destroy()
        #can add stuff here to do in parent.


def wxProcessEvents(self):
    # this version uses the new Phoenix API
    # Get app

    app = wx.App.Get()

    # Keep reference of old eventloop instance
    old = wx.EventLoopBase.GetActive()
    # Create new eventloop and process
    eventLoop = app.GetTraits().CreateEventLoop()
    wx.EventLoopActivator(eventLoop)
    while eventLoop.Pending():
        eventLoop.Dispatch()
    # Process idle
    eventLoop.ProcessIdle() # otherwise frames do not close
    # Set back the original
    wx.EventLoopActivator(old)
"""
"""
def getWidgets(self, parent):
    '''
    Return a list of all the child widgets
    '''
    items = [parent]
    for item in parent.GetChildren():
        items.append(item)
        if hasattr(item, "GetChildren"):
            for child in item.GetChildren():
                items.append(child)
    return items
"""
###############
