import string
import re
import os
import os.path
import stat
import sys
import subprocess
import cPickle
import wx
import MP3Info
import dpi

intPPI = dpi.intPPI
tuplePPI = dpi.tuplePPI

# Open a file or directory with its associate program
def startfile(path, prefer_dir=True):
    '''Open a file or directory with its associate program

    'prefer_dir': If True, ensure to open a dir and not an executable with
    the same name on Windows (ignore PATHEXT)
    '''
    if os.name == 'nt':
        if prefer_dir and os.path.isdir(path):  path += os.sep
        os.startfile(path)
    else:
        os.system('xdg-open "{0}"'.format(path))

class CompressVideoDialog(wx.Dialog):
    def __init__(self, parent, inputname='', framecount=None, framerate=None, framewidth=None, frameheight=None):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, _('Encode video'))
        dpi.SetFontPPI(self)
        self.inputname = inputname
        if not inputname:
            index = parent.scriptNotebook.GetSelection()
            self.outputname = parent.scriptNotebook.GetPageText(index)
            self.inputname = parent.MakePreviewScriptFile(parent.currentScript)
        self.framecount = framecount
        self.framerate = framerate
        self.framewidth = framewidth
        self.frameheight = frameheight
        self.windowTextColor = wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT)
        self.LoadOptions()
        self.LoadPresets()
        self.CreateInterface()
        self.bitrateDialog = BitrateCalcDialog(self, defaultdir=os.path.dirname(inputname))
        self.SetDefaultValues()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def LoadOptions(self):
        self.options = {}
        self.optionsFilename = os.path.join(self.GetParent().toolsfolder,
                                            __name__ + '.dat')
        if os.path.isfile(self.optionsFilename):
            f = open(self.optionsFilename, mode='rb')
            self.options = cPickle.load(f)
            f.close()

    def SaveOptions(self):
        # Retrieve values to save
        outputname = self.ctrlDict['video_output'].GetValue()
        self.options['output_ext'] = os.path.splitext(outputname)[1]
        self.options['preset'] = self.ctrlDict['preset'].GetStringSelection()
        self.options['target_size'] = self.bitrateDialog.ctrlDict['target_size'].GetValue()
        self.options['container'] = self.bitrateDialog.ctrlDict['container'].GetStringSelection()
        self.options['audio_compress'] = self.bitrateDialog.ctrlDict['audio_compress'].GetValue()
        self.options['audio_bitrate'] = self.bitrateDialog.ctrlDict['audio_bitrate'].GetValue()
        self.options['audio_format'] = self.bitrateDialog.ctrlDict['audio_format'].GetStringSelection()
        # Delete unused exe options
        deleteList = []
        for exeName, exeDict in self.options['exe_options'].items():
            if not [value for value in exeDict.values() if value.strip()]:
                deleteList.append(exeName)
        for exeName in deleteList:
            del self.options['exe_options'][exeName]
        # Save the options file
        f = open(self.optionsFilename, mode='wb')
        cPickle.dump(self.options, f, protocol=0)
        f.close()

    def LoadPresets(self):
        self.presets = {}
        self.presetKeys = []  # keep separate list to preserve order
        filenames = os.listdir(self.GetParent().toolsfolder)
        filenames.sort()
        for filename in filenames:
            base, ext = os.path.splitext(filename)
            if ext.lower() == '.presets':
                f = open(os.path.join(self.GetParent().toolsfolder, filename), 'r')
                lines = f.readlines()
                f.close()
                encoderName = os.path.basename(base)
                for line in lines:
                    line = line.strip()
                    if line.startswith('[') and line.endswith(']'):
                        key = '%s - %s'  % (encoderName, line.strip('[]'))
                        self.presetKeys.append(key)
                        self.presets[key] = ''
                    else:
                        if self.presetKeys != [] and line != '':
                            self.presets[key] += line+'\n'

    def CreateInterface(self):
        int5 = intPPI(5)
        int10 = intPPI(10)
        self.ctrlDict = {}
        # Files
        sizer_System = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('System settings')), wx.VERTICAL)
        fieldInfo = (
            ('video_input', _('Input file:'), self.OnButtonSelectInput),
            ('video_output', _('Output file:'), self.OnButtonSelectOutput),
        )
        gridSizer = wx.FlexGridSizer(cols=3, hgap=int5, vgap=int5)
        gridSizer.AddGrowableCol(1)
        for key, label, handler in fieldInfo:
            staticText = wx.StaticText(self, wx.ID_ANY, label)
            textCtrl = wx.TextCtrl(self, size=(intPPI(300),-1))
            textCtrl.Bind(wx.EVT_TEXT, self.OnTextChangeCommandLine)
            button = wx.Button(self, wx.ID_ANY, '...', size=(intPPI(30),-1), name=key)
            self.Bind(wx.EVT_BUTTON, handler, button)
            self.ctrlDict[key] = textCtrl
            gridSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            gridSizer.Add(textCtrl, 0, wx.EXPAND)
            gridSizer.Add(button, 0, wx.EXPAND)
        sizer_System.Add(gridSizer, 1, wx.EXPAND|wx.ALL, int5)
        # Compression
        sizer_Compression = wx.BoxSizer(wx.HORIZONTAL)
        sizer_CompressionA = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Compression settings')), wx.VERTICAL)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Bitrate (kbits/sec):'))
        textCtrl = wx.TextCtrl(self, size=(intPPI(50),-1))
        textCtrl.Bind(wx.EVT_TEXT, self.OnTextChangeCommandLine)
        button = wx.Button(self, wx.ID_ANY, _('calculate'))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCalculate, button)
        self.ctrlDict['video_bitrate'] = textCtrl
        self.ctrlDict['x264'] = (_('Quality CRF (0-51):'), 21, 0, 51)
        self.ctrlDict['x265'] = (_('Quality CRF (0-51):'), 21, 0, 51)
        self.ctrlDict['xvid'] = (_('Quality CQ (1-31):'), 4, 1, 31)
        self.ctrlDict['ffmpeg'] = (_('Quality CRF (0-51):'), 21, 0, 51)
        staticTextQty = wx.StaticText(self, wx.ID_ANY, self.ctrlDict['x264'][0], style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        self.ctrlDict['quality_label'] = staticTextQty
        spinCtrlQty = wx.SpinCtrl(self, size=(intPPI(50),-1), style=wx.SP_ARROW_KEYS|wx.ALIGN_CENTRE)
        spinCtrlQty.Bind(wx.EVT_TEXT, self.OnTextChangeCommandLine)
        self.ctrlDict['video_quality'] = spinCtrlQty
        gridsizer = wx.GridBagSizer(hgap=int5, vgap=int10)
        gridsizer.Add(staticText, pos=(0,0), flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        gridsizer.Add(staticTextQty, pos=tuplePPI(1,0), flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        gridsizer.Add(textCtrl, pos=tuplePPI(0,1))
        gridsizer.Add(button, pos=tuplePPI(0,2))
        gridsizer.Add(spinCtrlQty, pos=tuplePPI(1,1))

        sizer_CompressionA.Add((int5,-1), 1, wx.EXPAND|wx.ALL, 0)
        sizer_CompressionA.Add(gridsizer, 0, wx.ALIGN_CENTER|wx.ALL, int5)
        sizer_CompressionA.Add((int5,-1), 1, wx.EXPAND|wx.ALL, 0)
        sizer_CompressionB = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Additional settings')), wx.VERTICAL)
        staticTextCredits = wx.StaticText(self, wx.ID_ANY, _('Credits start frame:'))
        textCtrl = wx.TextCtrl(self, size=(intPPI(75),-1))
        textCtrl.Bind(wx.EVT_TEXT, self.OnTextCreditsChange)
        self.ctrlDict['credits_frame'] = textCtrl
        staticTextPAR = wx.StaticText(self, wx.ID_ANY, _('Pixel aspect ratio:'))
        textCtrl1 = wx.TextCtrl(self, size=(intPPI(30), -1))
        textCtrl1.Bind(wx.EVT_TEXT, self.OnTextChangeCommandLine)
        self.ctrlDict['par_x'] = textCtrl1
        textCtrl2 = wx.TextCtrl(self, size=(intPPI(30), -1))
        textCtrl2.Bind(wx.EVT_TEXT, self.OnTextChangeCommandLine)
        self.ctrlDict['par_y'] = textCtrl2
        button = wx.Button(self, wx.ID_ANY, '...', size=(intPPI(30),-1))
        self.Bind(wx.EVT_BUTTON, self.OnCalculateSAR, button)
        self.CreatePixelAspectRatioMenu()
        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer3.Add(textCtrl1, 0, wx.ALL, 0)
        sizer3.Add(wx.StaticText(self, wx.ID_ANY, ':'), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, int5)
        sizer3.Add(textCtrl2, 0, wx.ALL, 0)
        sizer3.Add(button, 0, wx.LEFT, int5)
        gridsizer = wx.GridBagSizer(hgap=int5, vgap=int10)
        gridsizer.Add(staticTextCredits, pos=(0,0), flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        gridsizer.Add(staticTextPAR, pos=(intPPI(1),0), flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        gridsizer.Add(textCtrl, pos=(0,intPPI(1)))
        gridsizer.Add(sizer3, pos=tuplePPI(1,1))
        sizer_CompressionB.Add(gridsizer, 0, wx.ALL, int5)
        sizer_Compression.Add(sizer_CompressionA, 1, wx.ALIGN_CENTER|wx.EXPAND|wx.RIGHT, int5)
        sizer_Compression.Add(sizer_CompressionB, 0, wx.EXPAND|wx.ALL, 0)
        # Command line
        sizer_Command_line = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Command line settings')), wx.VERTICAL)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Preset:'))
        choiceBox = wx.Choice(self, wx.ID_ANY,choices=self.presetKeys)
        choiceBox.Bind(wx.EVT_CHOICE, self.OnSelectPreset)
        button = wx.Button(self, wx.ID_ANY, _('Configure'))
        self.Bind(wx.EVT_BUTTON, self.OnButtonConfigure, button)
        self.ctrlDict['preset'] = choiceBox
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(choiceBox, 0, wx.ALL, 0)
        sizer.Add((int10,-1), 1, wx.EXPAND)
        sizer.Add(button, 0, wx.ALIGN_RIGHT|wx.ALL, 0)
        sizer_Command_line.Add(sizer, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, int5)
        textCtrl = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_DONTWRAP, size=(-1,intPPI(80)))
        self.ctrlDict['commandline'] = textCtrl
        sizer_Command_line.Add(textCtrl, 1, wx.EXPAND|wx.ALL, int5)
        # Run
        button = wx.Button(self, wx.ID_ANY, _('Run'))
        self.Bind(wx.EVT_BUTTON, self.OnButtonRun, button)
        # Total
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(sizer_System, 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(sizer_Compression, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, int5)
        dlgSizer.Add(sizer_Command_line, 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, int10)
        self.SetSizer(dlgSizer)
        dlgSizer.Fit(self)

    def CreatePixelAspectRatioMenu(self):
        menuInfo = (
            (_('compute from .d2v'), None, None),
            (''),
            ('Square', 1, 1),
            (''),
            ('DAR 4:3', 4.0, 3000.0),
            ('DAR 16:9', 16.0, 9000.0),
            ('DAR 2.35', 2.35, 1000.0),
            ('DAR 14:9', 14.0, 9000.0),
            (''),
            ('PAL DV 4:3', 59, 54),
            ('PAL DV 16:9', 118, 81),
            ('PAL SVCD 4:3', 59, 36),
            ('PAL SVCD 16:9', 59, 27),
            ('PAL SVCD 2.21:1', '2.7123', 1),
            (''),
            ('NTSC DV 4:3', 10, 11),
            ('NTSC DV 16:9', 40, 33),
            ('NTSC SVCD 4:3', 15, 11),
            ('NTSC SVCD 16:9', 20, 11),
            ('NTSC SVCD 2.21:1', '2.2602', 1),
            (''),

        )
        self.par_menu = wx.Menu()
        for i, eachMenuInfo in enumerate(menuInfo):
            # Define optional arguments
            if not eachMenuInfo:
                self.par_menu.AppendSeparator()
            else:
                label, par_x, par_y = eachMenuInfo
                if par_x is None:
                    handler = lambda event: self.ComputePARfromD2V()
                else:
                    if par_y >= 1000:   # GPo, frame AR to DAR e.g. (PAL TV-SD 720x576 to DAR 16:9)
                        try:
                            x = (par_x/(par_y/1000.0)) / (self.framewidth/float(self.frameheight))
                            par_x = "%.4f" % x
                        except:
                            par_x = 1
                        par_y = 1
                    label = '%s - %s:%s' % (label, par_x, par_y)
                    handler = self.OnMenuPixelAspectRatio
                menuItem = self.par_menu.Append(wx.ID_ANY, label, '')
                self.Bind(wx.EVT_MENU, handler, menuItem)


    def ComputePARfromD2V(self):
        par_x = par_y = ''
        avsfilename = self.ctrlDict['video_input'].GetValue().strip()
        if os.path.isfile(avsfilename):
            text = self.GetParent().GetTextFromFile(avsfilename)[0]
            for s in re.findall('".+?.d2v"', text):
                d2vfilename = s.strip('"')
                if os.path.isfile(d2vfilename):
                    f = open(d2vfilename, 'r')
                    lines = f.readlines()
                    f.close()
                    ar_lines = [line for line in lines if line.startswith('Aspect_Ratio')]
                    pr_lines = [line for line in lines if line.startswith('Picture_Size')]
                    if len(ar_lines) > 0 and len(pr_lines) > 0:
                        try:
                            ar_x, ar_y = [int(s) for s in ar_lines[0].split('=')[1].split(':')]
                            pr_x, pr_y = [int(s) for s in pr_lines[0].split('=')[1].split('x')]
                            par_x = ar_x * pr_y
                            par_y = ar_y * pr_x
                            # Reduce this fraction
                            a, b = par_x, par_y
                            while a != 0:
                                a, b = b%a, a
                            par_x = par_x / b
                            par_y = par_y / b
                        except:
                            break
                    break
        self.ctrlDict['par_x'].SetValue(str(par_x))
        self.ctrlDict['par_y'].SetValue(str(par_y))

    def SetDefaultValues(self):
        self.ctrlDict['video_input'].Replace(0, -1, self.inputname)
        output_ext = self.options.setdefault('output_ext', '.mp4')
        self.SetOutputNameText(self.inputname, output_ext)
        default_preset = self.options.setdefault('preset', self.ctrlDict['preset'].GetString(0))
        self.ctrlDict['preset'].SetStringSelection(default_preset)
        encoderName = default_preset.split()[0]
        label, initial, _min, _max = self.ctrlDict[encoderName]
        self.ctrlDict['quality_label'].SetLabel(label)
        self.ctrlDict['video_quality'].SetValue(initial)
        self.ctrlDict['video_quality'].SetRange(_min, _max)
        self.ctrlDict['video_bitrate'].SetValue('5000')
        self.ctrlDict['credits_frame'].SetValue(str(self.framecount-1))
        self.ctrlDict['par_x'].SetValue('1')
        self.ctrlDict['par_y'].SetValue('1')
        self.SetDefaultValuesBitrateCalc()
        bitrate = self.bitrateDialog.ComputeBitrate()
        boolAudio = self.bitrateDialog.ctrlDict['audio_input'].GetValue().strip() != '' or self.bitrateDialog.ctrlDict['audio_compress'].GetValue()
        boolAutoBitrate = self.options.setdefault('auto_bitrate', True)
        if bitrate is not None and boolAudio and boolAutoBitrate:
            self.ctrlDict['video_bitrate'].Replace(0, -1, '%i' % bitrate)

        if self.options.setdefault('auto_par_d2v', False):
            self.ComputePARfromD2V()
        commandline = self.ComputeCommandLine()
        self.SetValidControls()
        self.GetUnknownPaths(commandline)
        self.options.setdefault('priority', 'belownormal')
        self.options.setdefault('credits_warning', 10)
        self.options.setdefault('cmd_codepage', '')
        self.options.setdefault('append_comments', False)
        self.options.setdefault('add_output_newtab', False)
        self.options.setdefault('exe_options', {})

    def SetDefaultValuesBitrateCalc(self):
        ctrls = self.bitrateDialog.ctrlDict
        default_target_size = self.options.setdefault('target_size', ctrls['target_size'].GetString(0))
        ctrls['target_size'].SetValue(default_target_size)
        default_container = self.options.setdefault('container', ctrls['container'].GetString(0))
        ctrls['container'].SetStringSelection(default_container)
        try:
            ctrls['framecount'].SetValue('%i' % self.framecount)
        except TypeError:
            ctrls['framecount'].SetValue('')
        try:
            ctrls['framerate'].SetValue('%.3f' % self.framerate)
        except TypeError:
            ctrls['framerate'].SetValue('')
        input_dirname = os.path.dirname(self.inputname)
        input_basename = os.path.splitext(os.path.basename(self.inputname))[0].lower()
        input_audio = input_subtitles = ''
        audioTypes = self.options.setdefault('audiotypes', ['.aac', '.mp3', '.ogg', '.ac3', '.dts', '.wav'])
        subtitlesTypes = self.options.setdefault('subtitletypes', ['.idx', '.srt', '.sub'])
        if os.path.isdir(input_dirname):
            for filename in os.listdir(input_dirname):
                if filename.lower().startswith(input_basename):
                    ext = os.path.splitext(filename)[1]
                    if ext in audioTypes:
                        try:
                            oldIndex = audioTypes.index(os.path.splitext(input_audio)[1])
                        except ValueError:
                            oldIndex = len(audioTypes)
                        if audioTypes.index(ext) < oldIndex:
                            input_audio = os.path.join(input_dirname, filename)
                    if ext in subtitlesTypes:
                        try:
                            oldIndex = subtitlesTypes.index(os.path.splitext(input_subtitles)[1])
                        except ValueError:
                            oldIndex = len(subtitlesTypes)
                        if subtitlesTypes.index(ext) < oldIndex:
                            input_subtitles = os.path.join(input_dirname, filename)
        ctrls['audio_input'].SetValue(input_audio)
        ctrls['subtitles_input'].SetValue(input_subtitles)
        ctrls['audio_compress'].SetValue(self.options.setdefault('audio_compress', False))
        self.bitrateDialog.OnCheckBoxAudioCompression(None)
        default_audio_bitrate = self.options.setdefault('audio_bitrate', ctrls['audio_bitrate'].GetString(3))
        ctrls['audio_bitrate'].SetValue(default_audio_bitrate)
        default_audio_format = self.options.setdefault('audio_format', ctrls['audio_format'].GetString(0))
        ctrls['audio_format'].SetStringSelection(default_audio_format)

    def SetOutputNameText(self, inputname, ext):
        if hasattr(self, 'outputname'):
            dirname = os.path.dirname(inputname)
            inputname = os.path.join(dirname, self.outputname)
            del self.outputname
        if inputname != '':
            root = os.path.splitext(inputname)[0]
            outputname = '%s%s' % (root, ext)
            i = 1
            while os.path.exists(outputname):
                outputname = '%s_%s%s' % (root, i, ext)
                i += 1
            self.ctrlDict['video_output'].Replace(0, -1, outputname)

    def ComputeCommandLine(self):
        # Get the appropriate preset from self.presets
        try:
            commandline = self.presets[self.ctrlDict['preset'].GetStringSelection()]
            tempcommandline = commandline
        except KeyError:
            self.ctrlDict['commandline'].SetValue('')
            return ''
        # Handle the $extra_options
        exeOptions = self.options.setdefault('exe_options', {})
        templist = []
        for line in commandline.strip().split('\n'):
            splitline = line.split(None, 1)
            if len(splitline) == 2:
                first, rest = splitline
            else:
                first, rest = splitline[0], ''
            try:
                extra = exeOptions[first.lower()]['extra']
                if extra.strip() == '':
                    extra = None
            except KeyError:
                extra = None
            if extra is None:
                templist.append('%s %s' % (first, rest.replace('$extra_options', '')))
            else:
                if rest.count('$extra_options') > 0:
                    templist.append('%s %s' % (first, rest.replace('$extra_options', extra)))
                else:
                    templist.append('%s %s %s' % (first, extra, rest))
        commandline = '\n'.join(templist) + '\n'
        # Retrieve values from gui
        keyInfo = (
            ('video_bitrate', self.ctrlDict),
            ('video_quality', self.ctrlDict),
            ('video_input', self.ctrlDict),
            ('video_output', self.ctrlDict),
            ('audio_input', self.bitrateDialog.ctrlDict),
            ('audio_bitrate', self.bitrateDialog.ctrlDict),
            ('subtitles_input', self.bitrateDialog.ctrlDict),
            ('container', self.bitrateDialog.ctrlDict),
            ('audio_format', self.bitrateDialog.ctrlDict),
            ('credits_frame', self.ctrlDict),
            ('par_x', self.ctrlDict),
            ('par_y', self.ctrlDict),
        )
        replaceDict = {}
        for key, keydict in keyInfo:
            value = keydict[key].GetValue()
            try:
                value = value.strip()
            except:
                pass
            if value != '':
                replaceDict[key] = value

        # Compute additional values
        replaceDict['last_frame'] = self.framecount - 1

        # GPo, fix for ffmpeg
        raw_commandline = self.presets[self.ctrlDict['preset'].GetStringSelection()]
        if raw_commandline.count('$video_bitrate_k') != 0:
            replaceDict['video_bitrate_k'] = str(self.ctrlDict['video_bitrate'].GetValue()) + 'k'
        """
        if raw_commandline.count('$dar_y') != 0:
            replaceDict['dar_y'] = self.ctrlDict['par_y'].GetValue()
        if raw_commandline.count('$dar_x') != 0:
            replaceDict['dar_x'] = self.ctrlDict['par_x'].GetValue()
        """

        audioname = self.bitrateDialog.ctrlDict['audio_input'].GetValue()
        try:
            replaceDict['audio_delay'] = audioname.lower().split('delay',1)[1].split('ms')[0].strip()
        except:
            replaceDict['audio_delay'] = 0
        try:
            replaceDict['par'] = '%.4f' % (float(replaceDict['par_x'])/float(replaceDict['par_y']))
        except:
            pass
        # Create the final command line
        template = string.Template(commandline)
        commandline = template.safe_substitute(replaceDict)
        self.ctrlDict['commandline'].SetValue(commandline)
        return commandline

    def SetValidControls(self):
        raw_commandline = self.presets[self.ctrlDict['preset'].GetStringSelection()]
        for key in ('video_bitrate', 'video_bitrate_k','video_quality', 'credits_frame', 'par_x', 'par_y', 'video_input', 'video_output'):
            if key == 'video_bitrate_k':  # GPo, fix for ffmpeg
                key = 'video_bitrate'
            if raw_commandline.count('$'+key) == 0:
                self.ctrlDict[key].Disable()
            else:
                self.ctrlDict[key].Enable()

    def GetUnknownPaths(self, commandline):
        # Parse the command line for exe arguments
        int5 = intPPI(5)
        exeOptions = self.options.setdefault('exe_options', {})
        unknownPathKeys = []
        for s in commandline.strip().split('\n'):
            try:
                key = s.split(None, 1)[0].lower()
            except IndexError:
                continue
            if os.name == 'nt' and not key.endswith('.exe'):
                continue
            value = exeOptions.setdefault(key, {'path': '', 'extra': ''})
            if not os.path.isfile(value['path']):
                default_path = os.path.join(self.GetParent().toolsfolder, key)
                if os.path.isfile(default_path):
                    value['path'] = default_path
                    continue
                elif os.name == 'nt':
                    try:
                        path = subprocess.check_output('for %i in ({0}) do @echo. %~$PATH:i'.format(key),
                                                       shell=True).strip().splitlines()[0]
                        if os.path.isfile(path) or os.path.isfile(path + '.exe'):
                            value['path'] = path
                            continue
                    except:
                        pass
                else:
                    key2, ext = os.path.splitext(key)
                    key2 = key2 if ext == '.exe' else key
                    try:
                        value['path'] = subprocess.check_output(['which', key2]).strip().splitlines()[0]
                        continue
                    except:
                        pass
                if not key in unknownPathKeys:
                    unknownPathKeys.append(key)
        if len(unknownPathKeys) == 0:
            return
        # Prompt for unknown exe paths
        s1 = _('First time using this compression preset!')
        s2 = _('Please enter the exe paths in the following dialog.')
        wx.MessageBox('%s\n%s' % (s1, s2), _('Message'))
        dlg = wx.Dialog(self, wx.ID_ANY, _('Exe pathnames'))
        dlg.ctrlDict = {}
        # Path pickers
        gridSizer = wx.FlexGridSizer(cols=3, hgap=int5, vgap=int5)
        for key in unknownPathKeys:
            staticText = wx.StaticText(dlg, wx.ID_ANY, key)
            textCtrl = wx.TextCtrl(dlg, wx.ID_ANY, size=(intPPI(200), -1))
            button = wx.Button(dlg, wx.ID_ANY, '...', size=(intPPI(30), -1))
            button.textCtrl = textCtrl
            dlg.Bind(wx.EVT_BUTTON, self.OnButtonSelectExe, button)
            dlg.ctrlDict[key] = textCtrl
            gridSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            gridSizer.Add(textCtrl, 0, wx.EXPAND)
            gridSizer.Add(button, 0, wx.EXPAND)
        # Standard buttons
        okay  = wx.Button(dlg, wx.ID_OK, _('OK'))
        dpi.SetFontPPI(okay)
        okay.SetDefault()
        cancel = wx.Button(dlg, wx.ID_CANCEL, _('Cancel'))
        dpi.SetFontPPI(cancel)
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Total
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add((-1,-1), 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(gridSizer, 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add((-1,intPPI(50)), 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, int5)
        dlg.SetSizer(dlgSizer)
        dlgSizer.Fit(dlg)
        dlg.Center()
        # Show the dialog
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            for key, ctrl in dlg.ctrlDict.items():
                exeOptions[key]['path'] = ctrl.GetValue()
        dlg.Destroy()

    def ConfigureOptions(self):
        dlg = CompressVideoOptionsDialog(self)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            self.options = dlg.GetOptionsDict()
            self.ComputeCommandLine()
        dlg.Destroy()

    def OnClose(self, event):
        self.SaveOptions()
        self.bitrateDialog.Destroy()
        self.Destroy()

    def OnButtonSelectInput(self, event):
        recentdir = ''
        inputname = self.ctrlDict['video_input'].GetValue()
        if os.path.exists(inputname):
            recentdir = os.path.dirname(inputname)
        title = _('Open an AviSynth script')
        filefilter = _('AviSynth script') + ' (*.avs, *.avsi)|*.avs;*.avsi'
        style = wx.OPEN
        dlg = wx.FileDialog(self, title, recentdir, '', filefilter, style)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            filename = dlg.GetPath()
            output_ext = self.options['output_ext']
            self.ctrlDict['video_input'].Replace(0, -1, filename)
            self.SetOutputNameText(filename, output_ext)
        dlg.Destroy()

    def OnButtonSelectOutput(self, event):
        recentdir = ''
        outputdir, filename = os.path.split(self.ctrlDict['video_output'].GetValue())
        if os.path.isdir(outputdir):
            recentdir = outputdir
        title = _('Save the video as')
        filefilter = ''
        style = wx.SAVE | wx.OVERWRITE_PROMPT
        dlg = wx.FileDialog(self, title, recentdir, filename, filefilter, style)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            filename = dlg.GetPath()
            self.ctrlDict['video_output'].Replace(0, -1, filename)
        dlg.Destroy()

    def OnButtonSelectExe(self, event):
        recentdir = ''
        title = _('Select a program')
        filefilter = _('Executable files') + ' (*.exe)|*.exe' if os.name == 'nt' else ''
        style = wx.OPEN
        dlg = wx.FileDialog(self, title, recentdir, '', filefilter, style)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            filename = dlg.GetPath()
            event.GetEventObject().textCtrl.Replace(0, -1, filename)
        dlg.Destroy()

    def OnCalculateSAR(self, event):
        win = event.GetEventObject()
        posx, posy = win.GetPositionTuple()
        pos = (posx, posy+win.GetSize()[1])
        self.PopupMenu(self.par_menu, pos)

    def OnMenuPixelAspectRatio(self, event):
        label = self.par_menu.GetLabel(event.GetId())
        par_x, par_y = label.split('-')[1].split(':', 1)
        self.ctrlDict['par_x'].SetValue(par_x.strip())
        self.ctrlDict['par_y'].SetValue(par_y.strip())

    def OnButtonConfigure(self, event):
        self.ConfigureOptions()

    def OnButtonRun(self, event):
        unknownPathKeys = []
        commandline = self.ctrlDict['commandline'].GetValue().strip()
        unreplacedList = re.findall(r'\$.+?\b', commandline.replace('$$', ''))
        if len(unreplacedList) > 0:
            s1 = _('Unreplaced items remain in the command line:')
            s2 = '\n'.join(unreplacedList)
            wx.MessageBox('%s\n\n%s' % (s1, s2), _('Error'), style=wx.OK|wx.ICON_ERROR)
            return
        if os.name == 'nt':
            lines = []
            if self.options['cmd_codepage'].strip():
                lines.append('chcp ' + self.options['cmd_codepage'].strip() + '\n')
            lines.append('@echo off\n')
            startline = 'start /%s /b /w' % self.options['priority']
            for s in commandline.split('\n'):
                s2 = s.split(None, 1)
                key = s2[0].lower()
                if key.endswith('.exe'):
                    try:
                        path = self.options['exe_options'][key]['path']
                        if not os.path.isfile(path):
                            unknownPathKeys.append(key)
                    except KeyError:
                        path = key
                        unknownPathKeys.append(key)
                    dirname, exename = os.path.split(path)
                    if len(s2) == 2:
                        lines.append('%s /d "%s" %s %s\n' % (startline, dirname, exename, s2[1]))
                    else:
                        lines.append('%s /d "%s" %s\n' % (startline, dirname, exename))
                else:
                    lines.append('%s %s\n' % (startline, s))
        else:
            lines = []
            ret = 'if [ "$?" -ne "0" ]\nthen\n  exit\nfi\n'
            for s in commandline.split('\n'):
                s2 = s.split(None, 1)
                key = s2[0].lower()
                if key.endswith('.exe'):
                    key = key[:-4]
                args = s2[1].replace('NUL ', '/dev/null ')
                lines.append('"%s" %s\n%s' % (key, args, ret))
        if unknownPathKeys != []:
            wx.MessageBox(_('Unknown exe paths!'), _('Error'), style=wx.OK|wx.ICON_ERROR)
            return
        else:
            batchname = os.path.join(self.GetParent().toolsfolder,
                                     'encode' + ('.bat' if os.name == 'nt' else '.sh'))

            batchname = batchname.encode(sys.getfilesystemencoding()) # GPo

            f = open(batchname, 'w')
            for line in lines:
                if type(line) == unicode:
                    line = line.encode(sys.getfilesystemencoding())
                f.write(line)
            f.close()

            # GPo 2020, make output dir if not exists
            path = self.ctrlDict['video_output'].GetValue()
            if commandline.find(path) > -1:
                dirname = os.path.split(path)[0]
                if dirname and not os.path.isdir(dirname):
                    try:
                        os.mkdir(dirname)
                        recentdir = dirname
                    except:
                        pass
            else:
                dlg = wx.MessageDialog(self,'Output filename in commandline and edit field different\n' +\
                                            'Cannot create the directory if it not exists', 'Information',\
                                             wx.OK|wx.CANCEL)
                ID = dlg.ShowModal()
                dlg.Destroy()
                if ID != wx.ID_OK:
                   return

            if self.options['append_comments']:
                avsname = self.ctrlDict['video_input'].GetValue()
                if os.path.isfile(avsname) and os.path.splitext(avsname)[1] == '.avs':
                    s = '\n\n'
                    for line in lines:
                        s += '#~ %s\n' % line
                    avsp.InsertText(s)
                    #~avsp.SaveScript(avsname)

            if self.options['add_output_newtab']:
                s = avsp.GetSourceStringFromFilename(self.ctrlDict['video_output'].GetValue())
                if s:
                   avsp.NewTab(copyselected=False)
                   avsp.InsertText(s)

            #~ os.startfile(batchname)
            if os.name == 'nt':
                #os.system('start "AvsP encoding" "%s"' % batchname.encode(sys.getfilesystemencoding()))
                os.system('start "AvsP encoding" "%s"' % batchname) # GPo
            else:
                os.chmod(batchname, os.stat(batchname).st_mode | stat.S_IXUSR)
                os.system('"%s"' % batchname.encode(sys.getfilesystemencoding()))
            self.Close()

    def OnButtonCalculate(self, event):
        #~ self.SetDefaultValuesBitrateCalc()
        self.bitrateDialog.ComputeBitrate()
        ID = self.bitrateDialog.ShowModal()
        if ID == wx.ID_OK:
            bitrate = self.bitrateDialog.ComputeBitrate()
            if bitrate is not None:
                self.ctrlDict['video_bitrate'].Replace(0, -1, '%i' % bitrate)
            container = self.bitrateDialog.ctrlDict['container'].GetStringSelection()
            if container in ('avi', 'mkv', 'mp4'):
                inputname = self.ctrlDict['video_input'].GetValue()
                output_ext = '.' + container
                self.SetOutputNameText(inputname, output_ext)

    def OnTextChangeCommandLine(self, event):
        self.ComputeCommandLine()
        event.Skip()

    def OnSelectPreset(self, event):
        encoderName = event.GetString().split()[0]
        label, initial, min, max = self.ctrlDict[encoderName]
        self.ctrlDict['quality_label'].SetLabel(label)
        self.ctrlDict['video_quality'].SetValue(initial)
        self.ctrlDict['video_quality'].SetRange(min, max)
        commandline = self.ComputeCommandLine()
        self.SetValidControls()
        self.GetUnknownPaths(commandline)
        event.Skip()

    def OnTextCreditsChange(self, event):
        warning_minutes = self.options.setdefault('credits_warning', 10)
        ctrl = event.GetEventObject()
        try:
            value = int(ctrl.GetValue())
            last_frame = self.framecount - 1
            credits_seconds = (last_frame - value) / self.framerate
            if value > last_frame or credits_seconds > warning_minutes * 60:
                ctrl.SetForegroundColour(wx.RED)
            else:
                ctrl.SetForegroundColour(self.windowTextColor)
        except ValueError:
            ctrl.SetForegroundColour(wx.RED)
        ctrl.Refresh()
        self.ComputeCommandLine()
        event.Skip()

class CompressVideoOptionsDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, _('Configure options'))
        dpi.SetFontPPI(self)
        self.parent = parent
        self.options = parent.options.copy()
        self.ctrlDict = {}
        self.CreateInterface()
        self.Center()

    def CreateInterface(self):
        int5 = intPPI(5)
        noteBook = wx.Notebook(self, wx.ID_ANY, style=wx.NO_BORDER)
        #if dpi.ppi_factor > 1: # not needed if on init font size set
            #dpi.SetFontPPI(noteBook)
            #noteBook.SetTabSize((-1, intPPI(23)))
        # General tab
        tabPanel = wx.Panel(noteBook, wx.ID_ANY)
        noteBook.AddPage(tabPanel, _('General'), select=True)
        #~ audioTypes = self.options.setdefault('audiotypes', ('.aac', '.mp3', '.ogg', '.ac3'))
        #~ subtitlesTypes = self.options.setdefault('subtitletypes', ('.idx', '.srt', '.sub'))
        #~ 'audio_bitrate'
        #~ 'audio_format'
        gridSizer = wx.FlexGridSizer(cols=2, hgap=int5, vgap=int5)
        staticText = wx.StaticText(tabPanel, wx.ID_ANY, _('Credits warning minutes:'))
        textCtrl = wx.TextCtrl(tabPanel, wx.ID_ANY, size=(intPPI(50), -1))
        textCtrl.SetValue(str(self.options['credits_warning']))
        self.ctrlDict['credits_warning'] = textCtrl
        gridSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        gridSizer.Add(textCtrl, 0)
        # GPo new, cmd codepage for batch file
        staticText = wx.StaticText(tabPanel, wx.ID_ANY, _('Cmd Codepage (enter 1252 for Latin 1):'))
        textCtrl = wx.TextCtrl(tabPanel, wx.ID_ANY, size=(intPPI(50), -1))
        textCtrl.SetValue(self.options['cmd_codepage'])
        self.ctrlDict['cmd_codepage'] = textCtrl
        gridSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        gridSizer.Add(textCtrl, 0)
        checkBox0 = wx.CheckBox(tabPanel, wx.ID_ANY, _('Automatically compute bitrate value on startup'))
        checkBox0.SetValue(self.options['auto_bitrate'])
        checkBox1 = wx.CheckBox(tabPanel, wx.ID_ANY, _('Automatically compute pixel aspect ratio from d2v on startup'))
        checkBox1.SetValue(self.options['auto_par_d2v'])
        checkBox2 = wx.CheckBox(tabPanel, wx.ID_ANY, _('Append batch commands to the avs script as comments'))
        checkBox2.SetValue(self.options['append_comments'])
        checkBox3 = wx.CheckBox(tabPanel, wx.ID_ANY, _('Add output file to new tab'))
        checkBox3.SetValue(self.options['add_output_newtab'])
        self.ctrlDict['auto_bitrate'] = checkBox0
        self.ctrlDict['auto_par_d2v'] = checkBox1
        self.ctrlDict['append_comments'] = checkBox2
        self.ctrlDict['add_output_newtab'] = checkBox3

        gridSizer2 = wx.FlexGridSizer(cols=2, hgap=int5, vgap=int5)
        staticText = wx.StaticText(tabPanel, wx.ID_ANY, _('Encoder priority:'))
        textCtrl = wx.Choice(tabPanel, wx.ID_ANY, choices=('low', 'normal', 'high', 'realtime', 'abovenormal', 'belownormal'))
        textCtrl.SetStringSelection(self.options['priority'])
        self.ctrlDict['priority'] = textCtrl
        gridSizer2.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        gridSizer2.Add(textCtrl, 0, wx.EXPAND)
        tabSizer = wx.BoxSizer(wx.VERTICAL)
        tabSizer.Add((-1,-1), 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add(checkBox0, 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add(checkBox1, 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add(checkBox2, 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add(checkBox3, 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add((-1,-1), 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add(gridSizer, 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add((-1,-1), 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add(gridSizer2, 0, wx.EXPAND|wx.ALL, int5)
        tabSizer.Add((-1,intPPI(100)), wx.EXPAND|wx.ALL, 0)
        tabPanel.SetSizer(tabSizer)
        # Encoder tabs
        exeNames = self.options['exe_options'].keys()
        exeNames.sort()
        for name in exeNames:
            tabPanel = wx.Panel(noteBook, wx.ID_ANY)
            noteBook.AddPage(tabPanel, os.path.splitext(name)[0])
            gridSizer = wx.FlexGridSizer(cols=3, hgap=int5, vgap=int5)
            gridSizer.AddGrowableCol(1)
            staticText = wx.StaticText(tabPanel, wx.ID_ANY, _('Path to %(name)s:') % locals())
            textCtrl = wx.TextCtrl(tabPanel, size=(intPPI(200),-1))
            textCtrl.SetValue(self.options['exe_options'][name]['path'])
            button = wx.Button(tabPanel, wx.ID_ANY, '...', size=(intPPI(30),-1))
            self.Bind(wx.EVT_BUTTON, self.OnButtonSelectExe, button)
            button.textCtrl = textCtrl
            gridSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            gridSizer.Add(textCtrl, 0, wx.EXPAND)
            gridSizer.Add(button, 0, wx.EXPAND)
            staticText = wx.StaticText(tabPanel, wx.ID_ANY, _('Extra arguments:'))
            textCtrl2 = wx.TextCtrl(tabPanel)
            textCtrl2.SetValue(self.options['exe_options'][name]['extra'])
            self.ctrlDict[name] = [textCtrl, textCtrl2]
            gridSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            gridSizer.Add(textCtrl2, 0, wx.EXPAND)
            tabSizer = wx.BoxSizer(wx.VERTICAL)
            tabSizer.Add(gridSizer, 0, wx.EXPAND|wx.ALL, int5)
            button = wx.Button(tabPanel, wx.ID_ANY, os.path.splitext(name)[0] + '.presets') # GPo
            self.Bind(wx.EVT_BUTTON, self.OnOpenPresets, button)
            tabSizer.Add(button, 0,  wx.ALIGN_LEFT|wx.ALIGN_BOTTOM)
            tabPanel.SetSizer(tabSizer)
        # Standard buttons
        okay  = wx.Button(self, wx.ID_OK, _('OK'))
        #dpi.SetFontPPI(okay)
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL, _('Cancel'))
        #dpi.SetFontPPI(cancel)
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Total
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(noteBook, 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, int5)
        self.SetSizer(dlgSizer)
        dlgSizer.Fit(self)

    def OnButtonSelectExe(self, event):
        recentdir = ''
        title = _('Select a program')
        filefilter = _('Executable files') + ' (*.exe)|*.exe' if os.name == 'nt' else ''
        style = wx.OPEN
        dlg = wx.FileDialog(self, title, recentdir, '', filefilter, style)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            filename = dlg.GetPath()
            event.GetEventObject().textCtrl.Replace(0, -1, filename)
        dlg.Destroy()

    def GetOptionsDict(self):
        try:
            self.options['credits_warning'] = int(self.ctrlDict['credits_warning'].GetValue())
        except ValueError:
            pass
        self.options['auto_bitrate'] = self.ctrlDict['auto_bitrate'].GetValue()
        self.options['auto_par_d2v'] = self.ctrlDict['auto_par_d2v'].GetValue()
        self.options['append_comments'] = self.ctrlDict['append_comments'].GetValue()
        self.options['add_output_newtab'] = self.ctrlDict['add_output_newtab'].GetValue()
        self.options['cmd_codepage'] = self.ctrlDict['cmd_codepage'].GetValue()
        for key in self.options['exe_options'].keys():
            self.options['exe_options'][key]['path'] = self.ctrlDict[key][0].GetValue()
            self.options['exe_options'][key]['extra'] = self.ctrlDict[key][1].GetValue()
        self.options['priority'] = self.ctrlDict['priority'].GetStringSelection()
        return self.options

    def OnOpenPresets(self, event):
        button = event.GetEventObject()
        presets = os.path.join(self.parent.GetParent().toolsfolder, button.GetLabel())
        if not os.path.isfile(presets):
            wx.MessageBox(_('Presets file not found:\n') + presets)
        if os.path.isdir(self.parent.GetParent().toolsfolder):
            startfile(self.parent.GetParent().toolsfolder, True)

class BitrateCalcDialog(wx.Dialog):
    def __init__(self, parent, defaultdir=''):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, _('Bitrate Calculator'))
        dpi.SetFontPPI(self)
        self.ctrlDict = {}
        self.defaultdir = defaultdir
        self.audiofilename = None
        self.audioformat = None
        self.CreateInterface()

    def CreateInterface(self):
        int5 = intPPI(5)
        # Output info
        sizer_Target = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Output info')), wx.VERTICAL)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Total size:'))
        textCtrl = wx.ComboBox(self, wx.ID_ANY, choices=('700 MB (1CD)', '1400 MB (2CD)'), style=wx.CB_DROPDOWN)
        textCtrl.Bind(wx.EVT_TEXT, self.OnTextChangeBitrate)
        textCtrl.Bind(wx.EVT_COMBOBOX, self.OnComboBoxBitrate)
        self.ctrlDict['target_size'] = textCtrl
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 0, wx.ALL, 0)
        #~ sizer_Target.Add(sizer, 0, wx.ALL, 5)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Container:'))
        textCtrl = wx.Choice(self, wx.ID_ANY, choices=(_('(None)'), 'avi', 'mkv', 'mp4'))
        textCtrl.Bind(wx.EVT_CHOICE, self.OnChoiceBitrate)
        textCtrl.SetSelection(0)
        textCtrl.GetValue = textCtrl.GetStringSelection
        self.ctrlDict['container'] = textCtrl
        #~ sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add((intPPI(10),-1), 0, wx.ALL, 0)
        sizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 0, wx.ALL, 0)
        sizer_Target.Add(sizer, 0, wx.ALL, int5)
        # Video info
        sizer_Video = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Video info')), wx.VERTICAL)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Framecount:'))
        textCtrl = wx.TextCtrl(self, size=(intPPI(75),-1))
        textCtrl.Bind(wx.EVT_TEXT, self.OnTextChangeBitrate)
        staticText2 = wx.StaticText(self, wx.ID_ANY, _('FPS:'))
        textCtrl2 = wx.ComboBox(self, wx.ID_ANY, '', choices=('23.976', '24.000', '25.000', '29.970', '30.000'), style=wx.CB_DROPDOWN)
        textCtrl2.Bind(wx.EVT_TEXT, self.OnTextChangeBitrate)
        textCtrl2.Bind(wx.EVT_COMBOBOX, self.OnComboBoxBitrate)
        #~ textCtrl2 = wx.TextCtrl(self, size=(50, -1))
        self.ctrlDict['framecount'] = textCtrl
        self.ctrlDict['framerate'] = textCtrl2
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 0, wx.RIGHT, intPPI(20))
        sizer.Add(staticText2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl2, 0, wx.ALL, 0)
        sizer_Video.Add(sizer, 0, wx.ALL, int5)
        # Audio info
        sizer_Audio = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Audio info')), wx.VERTICAL)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Audio file:'))
        textCtrl = wx.TextCtrl(self)
        textCtrl.Bind(wx.EVT_TEXT, self.OnTextChangeBitrate)
        button = wx.Button(self, wx.ID_ANY, '...', size=(intPPI(30),-1))
        self.Bind(wx.EVT_BUTTON, self.OnButtonSelectInputAudio, button)
        self.ctrlDict['audio_input'] = textCtrl
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 1, wx.EXPAND|wx.RIGHT, int5)
        sizer.Add(button, 0, wx.RIGHT, 0)
        sizer_Audio.Add(sizer, 1, wx.EXPAND|wx.ALL, int5)
        checkBox = wx.CheckBox(self, wx.ID_ANY, _('Compress audio'))
        checkBox.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxAudioCompression)
        self.ctrlDict['audio_compress'] = checkBox
        sizer_Audio.Add((-1,int5), 0, wx.ALL, 0)
        sizer_Audio.Add(checkBox, 0, wx.ALL, int5)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Audio bitrate:'))
        textCtrl = wx.ComboBox(self, wx.ID_ANY, choices=('320 kbps', '256 kbps', '192 kbps', '128 kpbs', '96 kpbs', '32 kbps'), style=wx.CB_DROPDOWN)
        textCtrl.Bind(wx.EVT_TEXT, self.OnTextChangeBitrate)
        textCtrl.Bind(wx.EVT_COMBOBOX, self.OnComboBoxBitrate)
        staticText2 = wx.StaticText(self, wx.ID_ANY, _('Format:'))
        textCtrl2 = wx.Choice(self, wx.ID_ANY, choices=('aac', 'ac3', 'mp3-cbr', 'mp3-vbr', 'ogg'))
        textCtrl2.Bind(wx.EVT_CHOICE, self.OnChoiceBitrate)
        textCtrl2.GetValue = textCtrl2.GetStringSelection
        #~ textCtrl2.SetSelection(0)
        self.audioCompressionControls = (staticText, textCtrl, staticText2, textCtrl2)
        for ctrl in self.audioCompressionControls:
            ctrl.Disable()
        self.ctrlDict['audio_bitrate'] = textCtrl
        self.ctrlDict['audio_format'] = textCtrl2
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 0, wx.RIGHT, int5)
        sizer.Add(staticText2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, int5)
        sizer.Add(textCtrl2, 0, wx.RIGHT, int5)
        sizer_Audio.Add(sizer, 0, wx.EXPAND|wx.ALL, int5)
        # Subtitles info
        sizer_Subtitle = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Subtitles info')), wx.VERTICAL)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Subtitles file:'))
        textCtrl = wx.TextCtrl(self)
        textCtrl.Bind(wx.EVT_TEXT, self.OnTextChangeBitrate)
        button = wx.Button(self, wx.ID_ANY, '...', size=(intPPI(30),-1))
        self.Bind(wx.EVT_BUTTON, self.OnButtonSelectInputSubtitles, button)
        self.ctrlDict['subtitles_input'] = textCtrl
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 1, wx.EXPAND|wx.RIGHT, int5)
        sizer.Add(button, 0, wx.RIGHT, 0)
        sizer_Subtitle.Add(sizer, 1, wx.EXPAND|wx.ALL, int5)
        # Results
        sizer_Results = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Results')), wx.VERTICAL)
        fieldInfo = (
            ('video_time', _('Total time:')),
            ('', ''),
            ('video_size', _('Video size:')),
            ('audio_size', _('Audio size:')),
            ('subtitles_size', _('Subtitles size:')),
            ('overhead_size', _('Overhead size:')),
            ('bitrate', _('Bitrate:')),
        )
        gridSizer = wx.FlexGridSizer(cols=2, hgap=int5, vgap=int5)
        for key, label in fieldInfo:
            if not key:
                gridSizer.Add((-1,int5), 0)
                gridSizer.Add((-1,-1), 0)
                continue
            staticText = wx.StaticText(self, wx.ID_ANY, label)
            if key == 'video_time':
                textCtrl = wx.StaticText(self, wx.ID_ANY, '')
                textCtrl.SetValue = textCtrl.SetLabel
            else:
                textCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(intPPI(100),-1), style=wx.TE_READONLY)
                #~ textCtrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DFACE))
            if key == 'bitrate':
                font = staticText.GetFont()
                #~ font.SetPointSize(10)
                font.SetWeight(wx.FONTWEIGHT_BOLD)
                font.SetUnderlined(True)
                staticText.SetFont(font)
            self.ctrlDict[key] = textCtrl
            gridSizer.Add(staticText, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            gridSizer.Add(textCtrl, 0, wx.ALL, 0)
        sizer_Results.Add(gridSizer, 0, wx.ALIGN_CENTER|wx.ALL, int5)
        # Standard buttons
        okay  = wx.Button(self, wx.ID_OK, _('OK'))
        #dpi.SetFontPPI(okay) set BitrateCalcDialog
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL, _('Cancel'))
        #dpi.SetFontPPI(cancel) set BitrateCalcDialog
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Total
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(sizer_Target, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, int5)
        dlgSizer.Add(sizer_Video, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, int5)
        dlgSizer.Add(sizer_Audio, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, int5)
        dlgSizer.Add(sizer_Subtitle, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, int5)
        dlgSizer.Add(sizer_Results, 0, wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, int5)
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, int5)
        self.SetSizer(dlgSizer)
        dlgSizer.Fit(self)
        self.Center()

    def OnButtonSelectInputAudio(self, event):
        recentdir = self.defaultdir
        inputname = self.ctrlDict['audio_input'].GetValue()
        if os.path.exists(inputname):
            recentdir = os.path.dirname(inputname)
        title = _('Open the audio file')
        filefilter = ''
        style = wx.OPEN
        dlg = wx.FileDialog(self, title, recentdir, '', filefilter, style)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            filename = dlg.GetPath()
            self.ctrlDict['audio_input'].Replace(0, -1, filename)
        dlg.Destroy()

    def OnButtonSelectInputSubtitles(self, event):
        recentdir = self.defaultdir
        inputname = self.ctrlDict['subtitles_input'].GetValue()
        if os.path.exists(inputname):
            recentdir = os.path.dirname(inputname)
        title = _('Open the subtitles file')
        filefilter = ''
        style = wx.OPEN
        dlg = wx.FileDialog(self, title, recentdir, '', filefilter, style)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            filename = dlg.GetPath()
            self.ctrlDict['subtitles_input'].Replace(0, -1, filename)
        dlg.Destroy()

    def OnTextChangeBitrate(self, event):
        self.ComputeBitrate()
        event.Skip()

    def OnComboBoxBitrate(self, event):
        event.GetEventObject().SetValue(event.GetString())
        self.ComputeBitrate()
        event.Skip()

    def OnChoiceBitrate(self, event):
        self.ComputeBitrate()
        event.Skip()

    def OnCheckBoxAudioCompression(self, event):
        checkBox = self.ctrlDict['audio_compress']
        if checkBox.GetValue():
            for ctrl in self.audioCompressionControls:
                ctrl.Enable()
        else:
            for ctrl in self.audioCompressionControls:
                ctrl.Disable()
        self.ComputeBitrate()

    def ComputeBitrate(self):
        ctrls = self.ctrlDict
        try:
            # Video
            framecount = int(ctrls['framecount'].GetValue())
            framerate = float(ctrls['framerate'].GetValue())
            seconds = framecount / framerate
            # Audio
            audio_size = 0
            audio_format = ''
            if ctrls['audio_compress'].GetValue():
                audio_format = ctrls['audio_format'].GetStringSelection()
                audio_bitrate = int(ctrls['audio_bitrate'].GetValue().split()[0])
                audio_size = int(round(audio_bitrate * seconds * 1000 / 8.0))
            else:
                audio_name = ctrls['audio_input'].GetValue()
                audio_format = os.path.splitext(audio_name)[1].strip('.')
                if os.path.isfile(audio_name):
                    audio_size = os.path.getsize(audio_name)
                    if audio_format == 'mp3':
                        # Determine cbr or vbr from header information
                        if audio_name == self.audiofilename:
                            audio_format = self.audioformat
                        else:
                            f = open(audio_name, 'rb')
                            info = MP3Info.MP3Info(f)
                            f.close()
                            if info.mpeg.is_vbr:
                                audio_format = 'mp3-vbr'
                            else:
                                audio_format = 'mp3-cbr'
                            self.audiofilename = audio_name
                            self.audioformat = audio_format
            # Subtitles
            subtitles_size = 0
            subtitles_format = ''
            subtitles_name = ctrls['subtitles_input'].GetValue()
            if os.path.isfile(subtitles_name):
                subtitles_size = os.path.getsize(subtitles_name)
                basename, ext = os.path.splitext(subtitles_name)
                subtitles_format = ext.strip('.')
                if ext == '.idx':
                    for extension in ('.sub', '.ifo'):
                        if os.path.isfile(basename+extension):
                            subtitles_size += os.path.getsize(basename+extension)
            # Target
            target_size = int(ctrls['target_size'].GetValue().split()[0]) * 1024 * 1024
            # Overhead
            overhead_size = 0
            container = ctrls['container'].GetStringSelection()
            if container == 'avi':
                overhead_size = self.CalculateAviOverhead(framecount, framerate, audio_format, subtitles_format)
            elif container == 'mkv':
                overhead_size = self.CalculateMkvOverhead(framecount, framerate, audio_format, subtitles_format)
            elif container == 'mp4':
                overhead_size = self.CalculateMp4Overhead(framecount, framerate, audio_format, subtitles_format)
            # Compute video size and bitrate
            video_size = target_size - (audio_size + subtitles_size + overhead_size)
            bitrate = int(round(video_size *8 /1000.0 / seconds))
            # Compute the total time
            m, s = divmod(framecount/framerate, 60)
            h, m = divmod(m, 60)
            totaltime = _('%(h)i hr and %(m)i min') % locals()
            # Set the gui values
            ctrls['video_time'].SetValue(totaltime)
            ctrls['video_size'].SetValue('%i KB' % (video_size / 1024))
            ctrls['audio_size'].SetValue('%i KB' % (audio_size / 1024))
            ctrls['subtitles_size'].SetValue('%i KB' % (subtitles_size / 1024))
            ctrls['overhead_size'].SetValue('%i KB' % (overhead_size / 1024))
            ctrls['bitrate'].SetValue('%i kbits/sec' % bitrate)
            return bitrate
        except:
            ctrls['video_size'].SetValue('')
            ctrls['audio_size'].SetValue('')
            ctrls['subtitles_size'].SetValue('')
            ctrls['overhead_size'].SetValue('')
            ctrls['bitrate'].SetValue('')
            return None

    def CalculateAviOverhead(self, framecount, framerate, audiotype, subtitlestype):
        milliseconds = framecount / framerate * 1000
        frames = framecount
        if audiotype == 'mp3-cbr':
            frames += milliseconds / (1000)
        elif audiotype == 'mp3-vbr':
            frames += milliseconds / (24 * 1)
        elif audiotype == 'aac':
            frames += milliseconds / (24 * 1) # ???
        elif audiotype == 'ac3':
            frames += milliseconds / (32 * 2)
        elif audiotype == 'dts':
            frames += milliseconds / (21)
        elif audiotype:
            frames = None  # Invalid audio format, throw exception
        overhead = 16 * frames  # Open-DML without legacy index
        return overhead

    def CalculateMkvOverhead(self, framecount, framerate, audiotype, subtitlestype):
        milliseconds = framecount / framerate * 1000
        frames = framecount
        overhead = 13 * frames  # <- estimation...
        return overhead

    def CalculateMp4Overhead(self, framecount, framerate, audiotype, subtitlestype):
        milliseconds = framecount / framerate * 1000
        frames = framecount
        if audiotype == 'aac':
            pass
        elif audiotype == 'mp3-cbr':
            pass
        elif audiotype == 'mp3-vbr':
            pass
        elif audiotype:
            frames = None  # Invalid audio format, throw exception
        overhead = 13 * frames  # <- estimation...
        return overhead

def avsp_run():
    # Ensure the script is ready
    if not avsp.UpdateVideo():
        avsp.MsgBox(_('The current Avisynth script contains errors.'), _('Error'))
        return
    # Show the dialog
    inputname = avsp.GetScriptFilename()
    if inputname and not avsp.IsScriptSaved():
        avsp.SaveScript()
    framecount = avsp.GetVideoFramecount()
    framerate = avsp.GetVideoFramerate()
    framewidth = avsp.GetVideoWidth()
    frameheight = avsp.GetVideoHeight()

    dlg = CompressVideoDialog(avsp.GetWindow(), inputname, framecount, framerate, framewidth, frameheight)
    dlg.Show()