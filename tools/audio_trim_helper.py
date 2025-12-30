#-------------------------------------------------------------------------------
# Name:        AudioTrimHelper
# Purpose:     plays the audio in a loop from or to the current frame for better trimming the start or end frame (audio)
#              while the audio is playing you can change the current frame with mouse wheel or the keyboard (the video window must be focused)
#
# Author:      GPo
#
# Created:     10.11.2025
# Copyright:   (c) GPo 2025
# Licence:     <none>
#-------------------------------------------------------------------------------

import wx, wxp, time, threading, dpi
from avsp import AsyncCall

class AudioTrimHelper(wx.Dialog):
    def __init__(self, parent):
        style = wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP | wx.FRAME_FLOAT_ON_PARENT
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title='Audio trim helper', style=style, name='wxAudioTrimHelper')
        self.parent = parent
        dpi.SetFontPPI(self)
        int5 = dpi.intPPI(5)
        self.th = None
        self.playing = False
        self.cloop = 0
        def OnClose(event):
            if self.th and self.th.isAlive():
                self.playing = False
                if self.cloop < 5:
                    self.cloop += 1
                    wx.CallLater(1000, OnClose, None)
                    return
                else:
                    wxp.MessageBox(_('Cannot cancel the audio play thread\nPlease restart AvsPmod'), 'Error', parent=self)
            self.Destroy()
        self.Bind(wx.EVT_CLOSE, OnClose)
        ## with gauge
        bSizer = wx.BoxSizer(wx.VERTICAL)
        self.gauge = wx.Gauge(self, wx.ID_ANY, 100, style=wx.GA_HORIZONTAL)
        self.gauge.SetValue(0)
        bSizer.Add(self.gauge, 0, wx.ALL|wx.EXPAND, int5)
        ## end
        gSizer = wx.GridSizer(0, 2, 0, 0)
        self.radio1 = wx.RadioButton(self, wx.ID_ANY, _('From current'))
        gSizer.Add(self.radio1, 0, wx.ALL, int5)
        self.radio2 = wx.RadioButton(self, wx.ID_ANY, _('To current'))
        gSizer.Add(self.radio2, 0, wx.ALL, int5)
        self.cbFrames = wx.ComboBox(self, wx.ID_ANY, '15', choices=['15', '25', '33'], style=wx.CB_READONLY|wx.CB_DROPDOWN)
        self.cbFrames.SetSelection(0)
        gSizer.Add(self.cbFrames, 0, wx.ALL, int5)
        self.togglePlay = wx.Button(self, wx.ID_ANY, _('Play'))
        self.togglePlay.Bind(wx.EVT_BUTTON, self.OnBtnPlay)
        gSizer.Add(self.togglePlay, 0, wx.ALL, int5)
        ## with gauge
        bSizer.Add(gSizer, 1, wx.EXPAND, int5)
        self.SetSizerAndFit(bSizer)
        ## end
        #self.SetSizerAndFit(gSizer)  #without gauge
        self.Layout()
        self.Centre(wx.BOTH)
        self.Show()
    def ResetBtn(self):
        self.cbFrames.Enable(True)
        self.togglePlay.SetLabel(_('Play'))
        self.gauge.SetValue(0)
    def th_play(self, app):
        try:
            try:
                AVI = app.currentScript.AVI
                frame_count = int(self.cbFrames.GetValue()) # must be mod 3 or only one frame
                max_loop = 60 # stop automatically after 60 loops
                audio = AVI.IsAudioActive()
                if not audio:
                    if not AVI.SetAudio(True, frame_count):
                        wxp.MessageBox(_('Cannot activate the audio playback'), 'Error', parent=self)
                        return
                wait = float(frame_count) / AVI.Framerate
                #self.gauge.SetRange(frame_count) # no problems but...
                AsyncCall(self.gauge.SetRange, frame_count).Wait()
                while self.playing and not app.playing_video and (AVI is app.currentScript.AVI) and (max_loop > -1):
                    if self.radio1.GetValue(): # from current
                        frame = min(AVI.current_frame, AVI.Framecount-frame_count-1)
                        if frame < 0: # clip to short break
                            wx.Bell()
                            break
                    else: # to current
                        frame = max(AVI.current_frame - frame_count, 0)
                    AVI.PlayAudioBuffer(frame, frame_count)
                    #self.gauge.SetValue(frame_count) # no problems but...
                    AsyncCall(self.gauge.SetValue, frame_count).Wait()
                    time.sleep(wait) # wait for playback finished
                    if self.playing:
                        #self.gauge.SetValue(0) # no problems but...
                        AsyncCall(self.gauge.SetValue, 0).Wait()
                        time.sleep(0.6) # pause for better visibility
                        max_loop -= 1
                AVI.SetAudio(audio, app.options['audioscrubcount']) # reset to default count and state
            except:
                pass
        finally:
            wx.CallAfter(self.ResetBtn)
    def OnBtnPlay(self, event):
        if self.th and self.th.isAlive():
            self.playing = False
        elif self.parent.previewOK():
            self.parent.StopPlayback()
            self.cbFrames.Enable(False)
            self.togglePlay.SetLabel(_('Stop'))
            self.playing = True
            self.th = threading.Thread(target=self.th_play, args=(self.parent,))
            self.th.deamon = True
            self.th.name = 'clip'
            self.th.start()
        else:
            wx.Bell()

##### run as tool or remove 'def avsp_run()' and run as macro
def avsp_run():
    if wx.FindWindowByName('wxAudioTrimHelper'):
    	wx.Bell()
    	return
    AudioTrimHelper(avsp.GetWindow())
