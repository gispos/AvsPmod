import os
import os.path
import cPickle
import ctypes
import wx
import dpi

intPPI = dpi.intPPI
tuplePPI = dpi.tuplePPI

class Avs2aviDialog(wx.Dialog):
    def __init__(self, parent, inputname='', title='Save as AVI'):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, title)
        dpi.SetFontPPI(self)
        self.LoadOptions()
        default_avs2avipath = os.path.join(parent.toolsfolder, 'avs2avi.exe')
        self.avs2avipath = self.options.setdefault('avs2avipath', default_avs2avipath)
        if not os.path.isfile(self.avs2avipath):
            self.avs2avipath = self.options['avs2avipath'] = default_avs2avipath
        if not os.path.isfile(self.avs2avipath):
            wx.MessageBox(_('Please select the path to avs2avi.exe'), _('Message'))
            dlg = wx.FileDialog(self, title, '', '', '*.exe', wx.OPEN)
            ID = dlg.ShowModal()
            if ID == wx.ID_OK:
                self.avs2avipath = dlg.GetPath()
            else:
                self.avs2avipath = ''
            dlg.Destroy()
            if not os.path.isfile(self.avs2avipath):
                wx.MessageBox(_('Error: avs2avi is required to save an avi!'),
                              _('Error'), style=wx.OK|wx.ICON_ERROR)
                return
            else:
                self.options['avs2avipath'] = self.avs2avipath
        self.SaveOptions()
        self.boolCanceled = False
        self.jobInfo = {
            'pid': None,
            'pass': 0,
            'passes': None,
            'frames': -1,
            'frame': 0,
            'size': None,
            'fps': None,
            'eta': None,
            'sec': None,
            'min': None,
            'hr': None,
            'time': 0,
        }
        # Preprocess the progress output string
        line1 = _('Pass: %(pass)s / %(passes)s')
        line2 = _('Frame: %(frame)i / %(frames)i')
        line3 = _('Size: %(size).2f MB')
        line4 = _('FPS: %(fps).1f fps')
        line5 = _('Time left: %(hr)02i:%(min)02i:%(sec)02i')
        self.progressinfo = '%s\n%s\n%s\n%s\n%s' % (line1, line2, line3, line4, line5)
        if not inputname:
            index = parent.scriptNotebook.GetSelection()
            self.outputname = parent.scriptNotebook.GetPageText(index)
            inputname = parent.MakePreviewScriptFile(parent.currentScript)
        self.CreateInterface(inputname)

    def CreateInterface(self, inputname):
        # Entry fields for source input/output
        int5 = intPPI(5)
        int10 = intPPI(10)
        inoutSizer = wx.FlexGridSizer(cols=3, hgap=int5, vgap=int5)
        inoutSizer.AddGrowableCol(1)
        self.ctrlDict = {}
        for eachKey, eachLabel in self.fieldInfo():
            staticText = wx.StaticText(self, wx.ID_ANY, eachLabel)
            textCtrl = wx.TextCtrl(self, size=(intPPI(280),-1))
            self.ctrlDict[eachKey] = textCtrl
            button = wx.Button(self, wx.ID_ANY, '...', size=(intPPI(30),-1), name=eachKey)
            self.Bind(wx.EVT_BUTTON, self.OnButtonSelectFile, button)
            inoutSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            inoutSizer.Add(textCtrl, 0, wx.EXPAND, int5)
            inoutSizer.Add(button, 0, wx.EXPAND)
        self.ctrlDict['input'].Replace(0, -1, inputname)
        self.SetOutputNameText(inputname)
        # Buttons for misc avs2avi configuration
        spinSizer = wx.BoxSizer(wx.HORIZONTAL)
        for eachKey, eachLabel, eachMin, eachMax, eachVal in self.spinInfo():
            staticText = wx.StaticText(self, wx.ID_ANY, eachLabel)
            spinCtrl = wx.SpinCtrl(self, wx.ID_ANY, '', size=(intPPI(50),-1))
            spinCtrl.SetRange(eachMin, eachMax)
            spinCtrl.SetValue(eachVal)
            self.ctrlDict[eachKey] = spinCtrl
            spinSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
            spinSizer.Add(spinCtrl, 0, wx.EXPAND|wx.RIGHT, intPPI(20))
        # Buttons and controls associated with running the process
        self.buttonRunStop = wx.Button(self, wx.ID_ANY, _('Run'))
        self.Bind(wx.EVT_BUTTON, self.OnButtonRunStop, self.buttonRunStop)
        self.textProgress = wx.StaticText(self, wx.ID_ANY, ' \n \n \n \n')
        self.gauge = wx.Gauge(self, wx.ID_ANY, 240, size=(-1,intPPI(20)), style=wx.GA_SMOOTH)
        # Set the sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(inoutSizer, 0, wx.EXPAND|wx.ALL, int5)
        sizer.Add(spinSizer, 0, wx.ALL|wx.ALIGN_CENTER, int10)
        sizer.Add(self.buttonRunStop, 0, wx.ALIGN_CENTER|wx.ALL, int10)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND)
        sizer.Add(self.textProgress, 0, wx.ALL, int5)
        sizer.Add(self.gauge, 0, wx.EXPAND|wx.ALL, int10)
        self.SetSizer(sizer)
        sizer.Fit(self)
        # Events
        self.process=None
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_END_PROCESS, self.OnProcessEnded)
        # Misc
        if self.ctrlDict['input'].GetLineText(0):
            self.ctrlDict['output'].SetFocus()

    def fieldInfo(self):
        return (
            ('input', _('Input file (.avs):')),
            ('output', _('Output file (.avi):')),
        )

    def spinInfo(self):
        return (
            ('passes', _('# of passes:'), 1, 3, 1),
            ('priority', _('Priority:'), 0, 2, 0),
        )

    def LoadOptions(self):
        self.options = {}
        self.optionsFilename = os.path.join(self.GetParent().toolsfolder,
                                            __name__ + '.dat')
        if os.path.isfile(self.optionsFilename):
            f = open(self.optionsFilename, mode='rb')
            self.options = cPickle.load(f)
            f.close()

    def SaveOptions(self):
        f = open(self.optionsFilename, mode='wb')
        cPickle.dump(self.options, f, protocol=0)
        f.close()

    def OnButtonSelectFile(self, event):
        key = event.GetEventObject().GetName()
        if key not in ('input', 'output'):
            print>>sys.stderr, _('Error: Unknown button')
            return
        textCtrl = self.ctrlDict[key]
        if key == 'input':
            title = _('Open an AviSynth script')
            filefilter = _('AviSynth script (*.avs)|*.avs')
            style = wx.OPEN
        elif key == 'output':
            title = _('Save the avi as')
            filefilter = _('Avi file (*.avi)|*.avi')
            style = wx.SAVE | wx.OVERWRITE_PROMPT
        recentdir = ''
        dirname, filename = os.path.split(textCtrl.GetValue())
        if os.path.isdir(dirname):
            recentdir = dirname
        dlg = wx.FileDialog(self, title, recentdir, filename, filefilter, style)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            filename = dlg.GetPath()
            textCtrl.Replace(0, -1, filename)
            if key == 'input':
                self.SetOutputNameText(filename)
        dlg.Destroy()
        textCtrl.SetFocus()

    def OnButtonRunStop(self, event):
        button = event.GetEventObject()
        if button.GetLabel() == _('Run'):
            self.boolCanceled = False
            # Retrieve and validate inputs
            infilename = self.ctrlDict['input'].GetLineText(0)
            if not os.path.exists(infilename):
                wx.MessageBox(_('Input file does not exist!'), _('Error'),
                              style=wx.OK|wx.ICON_ERROR)
                self.ctrlDict['input'].SetFocus()
                self.ctrlDict['input'].SetSelection(-1, -1)
                return
            if os.path.splitext(infilename)[1].lower() != '.avs':
                wx.MessageBox(_('Input file must be an avisynth script!'),
                              _('Error'), style=wx.OK|wx.ICON_ERROR)
                self.ctrlDict['input'].SetFocus()
                self.ctrlDict['input'].SetSelection(-1, -1)
                return
            outfilename = self.ctrlDict['output'].GetLineText(0)
            if not os.path.exists(os.path.dirname(outfilename)):
                wx.MessageBox(_('Output path does not exist!'), _('Error'),
                              style=wx.OK|wx.ICON_ERROR)
                self.ctrlDict['output'].SetFocus()
                self.ctrlDict['output'].SetSelection(-1, -1)
                return
            try:
                self.jobInfo['passes'] = int(self.ctrlDict['passes'].GetValue())
            except ValueError:
                wx.MessageBox(_('# of passes must be an integer!'), _('Error'),
                              style=wx.OK|wx.ICON_ERROR)
                self.ctrlDict['passes'].SetFocus()
                self.ctrlDict['passes'].SetSelection(-1, -1)
                return
            try:
                prioritylevel = int(self.ctrlDict['priority'].GetValue())
            except ValueError:
                wx.MessageBox(_('Priority must be an integer!'), _('Error'),
                              style=wx.OK|wx.ICON_ERROR)
                self.ctrlDict['priority'].SetFocus()
                self.ctrlDict['priority'].SetSelection(-1, -1)
                return
            # Run the process
            infilename = '"%s"' % infilename
            outfilename = '"%s"' % outfilename
            args = [
                self.avs2avipath, infilename, outfilename,
                '-w',
                '-P', str(self.jobInfo['passes']),
                '-p', str(prioritylevel),
                '-f',
            ]
            self.process = wx.Process(self)
            self.process.Redirect()
            self.pid = wx.Execute(' '.join(args), wx.EXEC_ASYNC, self.process)
            button.SetLabel(_('Stop'))
        elif button.GetLabel() == _('Stop'):
            self.boolCanceled = True
            # Close the hidden avs2avi window (eventually stopping the process)
            if self.jobInfo['pid'] is not None:
                WM_CLOSE = 16
                ctypes.windll.user32.SendMessageA(self.jobInfo['pid'], WM_CLOSE, 0, 0)
        elif button.GetLabel() == _('Done'):
            # Close the dialog box
            self.OnClose(None)

    def OnIdle(self, event):
        if self.process is not None:
            stream = self.process.GetInputStream()
            if stream.CanRead():
                txt = stream.read()
                self.textProgress.SetLabel(self.formatStreamText(txt))
                self.gauge.SetValue(self.jobInfo['frame'])

    def OnProcessEnded(self, evt):
        stream = self.process.GetInputStream()
        if self.boolCanceled:
            self.textProgress.SetLabel(_('Process stopped.'))
            self.gauge.SetValue(0)
            self.buttonRunStop.SetLabel(_('Run'))
        elif stream.CanRead():
            txt = stream.read()
            self.textProgress.SetLabel(self.formatStreamText(txt))
            self.buttonRunStop.SetLabel(_('Done'))
            self.gauge.SetValue(self.jobInfo['frames'])
        else:
            self.buttonRunStop.SetLabel(_('Done'))
            self.gauge.SetValue(self.jobInfo['frames'])
        self.process.Destroy()
        self.process = None
        self.jobInfo['pid'] = None
        self.jobInfo['frame'] = 0
        self.jobInfo['time'] = 0

    def OnClose(self, event):
        if self.process is not None:
            return
        self.SaveOptions()
        self.Destroy()

    def SetOutputNameText(self, inputname):
        if hasattr(self, 'outputname'):
            dirname = os.path.dirname(inputname)
            inputname = os.path.join(dirname, self.outputname)
            del self.outputname
        if inputname != '':
            root = os.path.splitext(inputname)[0]
            outputname = '%s.avi' % root
            i = 1
            while os.path.exists(outputname):
                outputname = '%s_%s.avi' % (root, i)
                i += 1
            self.ctrlDict['output'].Replace(0, -1, outputname)

    def formatStreamText(self, txt):
        newtxt = _('Processing...')
        for line in txt.split('\n'):
            if line.startswith('PROGRESS'):
                pieces = line.split()
                if len(pieces) >= 5:
                    self.jobInfo['frame'] = int(pieces[1])
                    self.jobInfo['size'] = float(pieces[2]) / 1024 / 1024
                    self.jobInfo['fps'] = float(pieces[3])
                    eta = float(pieces[4])
                    if eta == -1:
                        self.jobInfo['sec'] = self.jobInfo['min'] = self.jobInfo['hr'] = 99
                    else:
                        min, self.jobInfo['sec'] = divmod(eta / 1000, 60)
                        self.jobInfo['hr'], self.jobInfo['min'] = divmod(min, 60)
                    #~ newtxt = (
                        #~ 'Pass: %(pass)s / %(passes)s\n'
                        #~ 'Frame: %(frame)i / %(frames)i\n'
                        #~ 'Size: %(size).2f MB\n'
                        #~ 'FPS: %(fps).1f fps\n'
                        #~ 'Time left: %(hr)02i:%(min)02i:%(sec)02i' % self.jobInfo
                    #~ )
                    newtxt = self.progressinfo % self.jobInfo
                    #~ newtxt = 'Pass:\t%(pass)s / %(passes)s\nFrame:\t%(frame)i / %(frames)i\nSize:\t%(size).2f MB\nFPS:\t%(fps).1f fps\nETA:\t%(eta).1f seconds remaining' % self.jobInfo
                else:
                    pass
            elif line.startswith('PASS_END'):
                self.jobInfo['time'] += float(line.split(' ')[1]) / 1000
            elif line.startswith('ENC_END'):
                min, sec = divmod(self.jobInfo['time'], 60)
                self.jobInfo['hr'], self.jobInfo['min'] = divmod(min, 60)
                self.jobInfo['size'] = float(line.split()[1]) / 1024 / 1024
                if self.jobInfo['hr'] != 0:
                    line1 = _('Finished in %(hr)i hour(s) and %(min)i minute(s).') % self.jobInfo
                else:
                    if self.jobInfo['min'] != 0:
                        line1 = _('Finished in %(min)i minute(s) and %(sec)i second(s).') % self.jobInfo
                    else:
                        line1 = _('Finished in %(time).1f seconds.') % self.jobInfo
                line2 = _('Filesize: %(size).2f MB') % self.jobInfo
                newtxt = '%s\n%s' % (line1, line2)
                self.gauge.SetValue(self.jobInfo['frames'])
            elif line.startswith('INIT'):
                self.jobInfo['pid'] = long(line.split(' ')[1])
            elif line.startswith('ENC_START'):
                pieces = line.split()
                #~ self.jobInfo['passes'] = int(pieces[1])
                self.jobInfo['frames'] = int(pieces[2])
                self.gauge.SetRange(self.jobInfo['frames'])
            elif line.startswith('PASS_START'):
                self.jobInfo['pass'] += 1
            elif line.startswith('ERROR'):
                newtxt = line
            elif line.startswith('VERSION'):
                pass
            elif line.startswith('PASS_START'):
                pass
        return newtxt

def avsp_run():
    # Ensure the script is ready
    #~ if not avsp.IsScriptSaved():
        #~ avsp.MsgBox(_('The current script has unsaved changes, exiting.'), _('Error'))
        #~ return
    if not avsp.UpdateVideo():
        avsp.MsgBox(_('The current script contains errors, exiting.'), _('Error'))
        return
    inputname = avsp.GetScriptFilename()
    if inputname and not avsp.IsScriptSaved():
        avsp.SaveScript()
    # Show the dialog
    dlg = Avs2aviDialog(avsp.GetWindow(), inputname, title=_('Save as AVI'))
    dlg.Show()
