#-------------------------------------------------------------------------------
# Name:        macro preload.py # must run with self.ExecuteMacro(Filename to preload.py) or as normal macro
# Purpose:     prelod the script if AVI None and display a progress dialog
#
# Author:      GPo
#
# Created:     09.10.2024
# Copyright:   (c) GPo 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import pyavs, wx, wxp, threading
import avsp as _avsp
AsyncCall = _avsp.AsyncCall

self = avsp.GetWindow() # as macro
script = self.currentScript
if script.AVI is not None:
    return
if self.AviThread_Running(script):
    return

# this runs in the main thread
def updateAbandonedScript(AVI, script, scripttxt, scr_filename):
    def _showDialog(idx):
        if (self.IsEnabled() and not self.ClipRefreshPainter) and self.fullScreenWnd.IsEnabled():
            wx.GetApp().ProcessIdle()
            ID = wxp.MessageDlgTop(self, _('Pre loaded clip assigned. Select the tab?'), _('Information'), wx.YES_NO|wx.ICON_INFORMATION)
            if ID == wx.ID_YES:
                self.HidePreviewWindow()
                self.scriptNotebook.SetSelection(idx)
    try:
        # check the clip and script again in the main thread, ignor AVI.isErrorClip
        if isinstance(AVI, pyavs.AvsClipBase):
            idx = -1
            if isinstance(script, _avsp.AvsStyledTextCtrl):
                for i in xrange(self.scriptNotebook.GetPageCount()):
                    if self.scriptNotebook.GetPage(i) is script:
                        idx = i
                        break
            if idx < 0: # create a new script if the original closed
                if self.cropDialog.IsShown():
                    self.cropDialog.Show(False)
                idx = self.NewTab(False)
                if idx:
                    script = self.currentScript
                    script.SetText(scripttxt)
                    script.filename = scr_filename

            if idx > -1:
                if script.GetText() != scripttxt:
                    script.SetText(scripttxt) # set the text with which the clip was loaded
                script.Colourise(0, script.GetTextLength())
                script.previewtxt = self.ScriptChanged(script, return_styledtext=True)[1]
                script.AVI = AVI
                script.AviThread = None
                script.display_clip_refresh_needed = True
                self.StopPlayback()
                if self.sdlWindow.running:
                    self.sdlWindow.ResetWindowToNormalSize()
                    #self.sdlWindow.Close()
                self.UpdateScriptTagProperties(script, scripttxt)
                self.GetAutoSliderInfo(script, scripttxt)
                self.UpdateScriptTabname(script)
                self.StatusbarTimer_Start(3000, _(u'Abandoned clip assigned: "{0}"').format(scr_filename), bellcount=1)
                if self.scriptNotebook.GetSelection() != idx:
                    wx.CallAfter(_showDialog, idx)
                return True
    except:
        pass
    return False

# this runs in a separate thread
def createclip(self, script, progress, workdir):
    readmatrix = True
    displayFilter = None
    resizeFilter = None
    previewFilter = None
    useSplitClip = False
    oldFramecount = 240
    scripttext = script.GetText()
    scr_filename = script.filename

    AVI = pyavs.AvsClip(self, self.getCleanText(scripttext), script.filename, workdir=workdir, env=None,
        fitHeight=None, fitWidth=None, oldFramecount=oldFramecount,
        matrix=script.matrix, interlaced=self.interlaced, swapuv=self.swapuv,
        bit_depth=self.bit_depth,callBack=self.AVICallBack,
        readmatrix=readmatrix, displayFilter=displayFilter, readFrameProps=self.readFrameProps,
        resizeFilter=resizeFilter, previewFilter=previewFilter, useSplitClip=useSplitClip, audioVolume=script.audioVolume)

    try:
        if not progress.Cancel:
            try:
                if isinstance(AVI, pyavs.AvsClipBase) and isinstance(script, _avsp.AvsStyledTextCtrl):
                    avsp.SafeCall(progress.SetLabel, _('Waiting for main thread'), '')
                    found = False
                    for i in xrange(self.scriptNotebook.GetPageCount()):
                        if self.scriptNotebook.GetPage(i) is script:
                            found = True
                            break
                    if found:
                        while wx.IsBusy() or self.ClipRefreshPainter or not self.IsEnabled() or not self.fullScreenWnd.IsEnabled():
                            wx.MilliSleep(1000)
                        if AsyncCall(updateAbandonedScript, AVI, script, scripttext, scr_filename).Wait():
                            return
            except:
                pass
        AVI = None
    finally:
        if isinstance(script, _avsp.AvsStyledTextCtrl):
            script.AviThread = None
        avsp.SafeCall(progress.Close)

# thread start
def run():
    try:
        mem = max(int(wx.GetFreeMemory()/1024/1024), 0)
    except:
        mem = 0
    if mem < 1001:
        ID = wxp.MessageDlgTop(self, _('Free memory is low %i MB, Continue?') % mem, 'Preload', wx.YES_NO|wx.ICON_WARNING)
        if ID != wx.ID_YES:
            return
    workdir_exp = self.ExpandVars(self.options['workdir'])
    if (self.options['useworkdir'] and self.options['alwaysworkdir']
        and os.path.isdir(workdir_exp)):
            workdir = workdir_exp
    else:
        workdir = script.workdir
    x, y = wx.GetDisplaySize() # progress dialog calcs the position from parent
    if self.options['reloadscriptprogresspos'] == 0:
        x = _avsp.intPPI(15)
    progress = wxp.ProgressDlg(self, 'Preload', 'Process in progress', 'Waiting for clip initialization', pos=(x,y), show=True)
    progress.Start()
    th = threading.Thread(target=createclip, args=(self, script, progress, workdir))
    th.daemon = True
    th.name = 'clip'
    script.AviThread = th
    th.start()

# return and start the thread from main thread
wx.CallAfter(run) # run as macro
