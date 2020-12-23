import os
import cPickle
import re
import wx
import dpi

intPPI = dpi.intPPI
tuplePPI = dpi.tuplePPI

class ResizeCalculatorDialog(wx.Dialog):
    def __init__(self, parent, script, input_width, input_height):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, _('Resize calculator'))
        dpi.SetFontPPI(self)
        self.script = script
        self.input_width = input_width
        self.input_height = input_height
        self.LoadOptions()
        self.CreatePixelAspectRatioMenu()
        self.CreateInterface()
        self.SetDefaultValues()
        self.ctrlDict['slider'].SetFocus()

    def LoadOptions(self):
        self.options = {}
        self.optionsFilename = os.path.join(self.GetParent().toolsfolder,
                                            __name__ + '.dat')
        if os.path.isfile(self.optionsFilename):
            f = open(self.optionsFilename, mode='rb')
            self.options = cPickle.load(f)
            f.close()

    def SaveOptions(self):
        # Save the options file
        f = open(self.optionsFilename, mode='wb')
        cPickle.dump(self.options, f, protocol=0)
        f.close()

    def SetDefaultValues(self):
        wmod = self.options.setdefault('wmod', 16)
        hmod = self.options.setdefault('hmod', 16)
        paro_x = self.options.setdefault('paro_x', 1.0)
        paro_y = self.options.setdefault('paro_y', 1.0)
        minresize = self.options.setdefault('minresize', 25)
        maxresize = self.options.setdefault('maxresize', 200)
        searcherror = self.options.setdefault('searcherror', 0.3)
        self.options.setdefault('avisynthresize', 'LanczosResize(%width%, %height%)')
        self.ctrlDict['widthi'].SetValue('%i' % self.input_width)
        self.ctrlDict['heighti'].SetValue('%i' % self.input_height)
        self.ComputePARfromD2V('1', '1')
        defaultValue = int(round(self.input_width / wmod))
        minValue = int(round(self.input_width * (minresize / 100.0) / wmod))
        maxValue = int(round(self.input_width * (maxresize / 100.0) / wmod))
        self.ctrlDict['slider'].SetRange(minValue, maxValue)
        self.ctrlDict['slider'].SetValue(defaultValue)
        self.ctrlDict['paro_x'].SetLabel('%i' % paro_x)
        self.ctrlDict['paro_y'].SetLabel('%i' % paro_y)
        self.ctrlDict['wmod'].SetLabel('%i' % wmod)
        self.ctrlDict['hmod'].SetLabel('%i' % hmod)
        self.ctrlDict['minresize'].SetLabel('%i' % minresize+'%')
        self.ctrlDict['maxresize'].SetLabel('%i' % maxresize+'%')
        self.ctrlDict['searcherror'].SetLabel('%.1f' % searcherror + '%')
        self.final_width = -1
        self.final_height = -1
        self.CalculateResize()

    def CreateInterface(self):
        int5 = intPPI(5)
        self.ctrlDict = {}
        # Input
        sizerInput = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Input')), wx.VERTICAL)
        gridsizer = wx.FlexGridSizer(cols=2, hgap=int5, vgap=int5)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Video resolution:'))
        textCtrlx = wx.TextCtrl(self, wx.ID_ANY, size=(intPPI(50), -1))
        textCtrly = wx.TextCtrl(self, wx.ID_ANY, size=(intPPI(50), -1))
        textCtrlx.Bind(wx.EVT_TEXT, lambda event: self.CalculateRangeAndResize())
        textCtrly.Bind(wx.EVT_TEXT, lambda event: self.CalculateResize())
        self.ctrlDict['widthi'] = textCtrlx
        self.ctrlDict['heighti'] = textCtrly
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(textCtrlx, 0, wx.RIGHT, int5)
        sizer.Add(wx.StaticText(self, wx.ID_ANY, 'x'), 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrly, 0, wx.RIGHT, int5)
        gridsizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL)
        gridsizer.Add(sizer, 0, wx.EXPAND)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Pixel aspect ratio:'))
        textCtrlx = wx.TextCtrl(self, wx.ID_ANY, size=(intPPI(40), -1))
        textCtrly = wx.TextCtrl(self, wx.ID_ANY, size=(intPPI(40), -1))
        textCtrlx.Bind(wx.EVT_TEXT, lambda event: self.CalculateResize())
        textCtrly.Bind(wx.EVT_TEXT, lambda event: self.CalculateResize())
        button = wx.Button(self, wx.ID_ANY, '...', size=(intPPI(30),-1))
        self.Bind(wx.EVT_BUTTON, self.OnButtonPAR, button)
        self.ctrlDict['pari_x'] = textCtrlx
        self.ctrlDict['pari_y'] = textCtrly
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(textCtrlx, 0, wx.RIGHT, int5)
        sizer.Add(wx.StaticText(self, wx.ID_ANY, ':'), 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrly, 0, wx.RIGHT, int5)
        sizer.Add(button, 0, wx.RIGHT, 0)
        gridsizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL)
        gridsizer.Add(sizer, 0, wx.EXPAND)
        sizerInput.Add(gridsizer, 0, wx.EXPAND|wx.ALL, int5)
        # Results
        sizerResults = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Results')), wx.VERTICAL)
        textCtrl = wx.StaticText(self, wx.ID_ANY, '640 x 480')
        font = textCtrl.GetFont()
        font.SetPointSize(intPPI(font.GetPointSize()+2))
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        textCtrl.SetFont(font)
        self.ctrlDict['resize'] = textCtrl
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add((-1,-1), 1, wx.EXPAND)
        sizer.Add(textCtrl, 0, wx.ALIGN_CENTER|wx.RIGHT, 0)
        sizer.Add((-1,-1), 1, wx.EXPAND)
        #~ sizerResults.Add(sizer, 0, wx.ALL, 5)
        sizerResults.Add(sizer, 1, wx.EXPAND|wx.BOTTOM, int5)
        slider = wx.Slider(self, wx.ID_ANY, 100, 0, 200)
        slider.Bind(wx.EVT_SCROLL, lambda event: self.CalculateResize())
        buttonLeft = wx.Button(self, wx.ID_ANY, '<<', size=(intPPI(24), intPPI(20)))
        self.Bind(wx.EVT_BUTTON, lambda event: self.FindNextResize(forward=False), buttonLeft)
        buttonRight = wx.Button(self, wx.ID_ANY, '>>', size=(intPPI(24), intPPI(20)))
        self.Bind(wx.EVT_BUTTON, lambda event: self.FindNextResize(forward=True), buttonRight)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(buttonLeft, 0, wx.ALL, 0)
        sizer.Add(slider, 1, wx.EXPAND|wx.ALIGN_CENTER, 0)
        sizer.Add(buttonRight, 0, wx.ALL, 0)
        self.ctrlDict['slider'] = slider
        sizerResults.Add(sizer, 0, wx.EXPAND|wx.ALL, 0)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Aspect ratio error:'))
        textCtrl2= wx.StaticText(self, wx.ID_ANY, '0 %')
        self.ctrlDict['error'] = textCtrl2
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        #~ sizer.Add(textCtrl, 0, wx.RIGHT, 0)
        #~ sizer.Add((-1,-1), 1, wx.EXPAND)
        sizer.Add(staticText, 0, wx.RIGHT, int5)
        sizer.Add(textCtrl2, 0, wx.RIGHT, intPPI(2))
        #~ sizer.Add(wx.StaticText(self, wx.ID_ANY, '%'), 0, wx.RIGHT, 0)
        sizerResults.Add(sizer, 0, wx.EXPAND|wx.ALL, int5)
        # Settings
        sizerSettings = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _('Settings')), wx.VERTICAL)
        info = (
            ('paro_x', 'paro_y', _('Target pixel aspect ratio:'), '1', '1', ':'),
            ('wmod', 'hmod', _('Resize block constraints:'), '16', '16', 'x'),
            ('minresize', 'maxresize', _('Resize percent ranges:'), '25%', '200%', '-'),
        )
        for xkey, ykey, label, xvalue, yvalue, divider in info:
            staticText = wx.StaticText(self, wx.ID_ANY, label)
            textCtrlx = wx.StaticText(self, wx.ID_ANY, xvalue)
            textCtrly = wx.StaticText(self, wx.ID_ANY, yvalue)
            self.ctrlDict[xkey] = textCtrlx
            self.ctrlDict[ykey] = textCtrly
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
            sizer.Add(textCtrlx, 0, wx.EXPAND|wx.RIGHT, intPPI(2))
            sizer.Add(wx.StaticText(self, wx.ID_ANY, divider), 0, wx.EXPAND|wx.RIGHT, intPPI(2))
            sizer.Add(textCtrly, 0, wx.EXPAND|wx.RIGHT, 0)
            sizerSettings.Add(sizer, 0, wx.EXPAND|wx.LEFT|wx.BOTTOM, int5)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Max search aspect ratio error:'))
        textCtrl = wx.StaticText(self, wx.ID_ANY, '1.0%')
        self.ctrlDict['searcherror'] = textCtrl
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 0, wx.EXPAND|wx.RIGHT, 0)
        sizerSettings.Add(sizer, 0, wx.EXPAND|wx.LEFT|wx.BOTTOM, int5)
        button =wx.Button(self, wx.ID_ANY, _('Configure'))
        self.Bind(wx.EVT_BUTTON, lambda event: self.ConfigureOptions(), button)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add((-1,-1), 1, wx.EXPAND)
        sizer.Add(button, 0, wx.EXPAND|wx.ALL, 0)
        sizerSettings.Add(sizer, 0, wx.EXPAND|wx.ALL, 0)
        # Standard buttons
        okay  = wx.Button(self, wx.ID_OK, _('Apply'))
        cancel = wx.Button(self, wx.ID_CANCEL, _('Cancel'))
        stdbtns = wx.StdDialogButtonSizer()
        stdbtns.AddButton(okay)
        stdbtns.AddButton(cancel)
        stdbtns.Realize()
        # Total
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(sizerInput, 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(sizerResults, 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(sizerSettings, 0, wx.EXPAND|wx.ALL, int5)
        dlgSizer.Add(stdbtns, 0, wx.EXPAND|wx.ALL, int5)
        self.SetSizer(dlgSizer)
        dlgSizer.Fit(self)

    def CreatePixelAspectRatioMenu(self):
        menuInfo = (
            (_('compute from .d2v'), None, None),
            (''),
            ('PC', 1, 1),
            (''),
            ('PAL 4:3', 59, 54),
            ('PAL 16:9', 118, 81),
            ('PAL VCD', 59, 54),
            ('PAL SVCD 4:3', 59, 36),
            ('PAL SVCD 16:9', 59, 27),
            ('PAL SVCD 2.21:1', '2.7123', 1),
            (''),
            ('NTSC 4:3', 10, 11),
            ('NTSC 16:9', 40, 33),
            ('NTSC VCD', 10, 11),
            ('NTSC SVCD 4:3', 15, 11),
            ('NTSC SVCD 16:9', 20, 11),
            ('NTSC SVCD 2.21:1', '2.2602', 1),
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
                    label = '%s - %s:%s' % (label, par_x, par_y)
                    handler = self.OnMenuPixelAspectRatio
                menuItem = self.par_menu.Append(wx.ID_ANY, label, '')
                self.Bind(wx.EVT_MENU, handler, menuItem)

    def ComputePARfromD2V(self, par_x='', par_y=''):
        for s in re.findall('".+?.d2v"', self.script):
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
        self.ctrlDict['pari_x'].SetValue(str(par_x))
        self.ctrlDict['pari_y'].SetValue(str(par_y))

    def CalculateResize(self):
        try:
            widthi = float(self.ctrlDict['widthi'].GetValue())
            heighti = float(self.ctrlDict['heighti'].GetValue())
            pari_x = float(self.ctrlDict['pari_x'].GetValue())
            pari_y = float(self.ctrlDict['pari_y'].GetValue())
            wmod = self.options['wmod']
            hmod = self.options['hmod']
            paro_x = self.options['paro_x']
            paro_y = self.options['paro_y']
            target_width = float(self.ctrlDict['slider'].GetValue()) * wmod
            #~ aspectratio = (widthi / heighti) * (pari_x / pari_y)
            #~ width = round(target_width / wmod) * wmod
            #~ height = round(width * paro_x / paro_y / aspectratio / hmod) * hmod
            #~ newaspectratio = width * paro_x / paro_y / float(height)
            #~ error = 100 * abs(aspectratio - newaspectratio) / float(aspectratio)
            width, height, error = self.ComputeWidthHeightError(target_width, widthi, heighti, pari_x, pari_y, wmod, hmod, paro_x, paro_y)
            self.ctrlDict['resize'].SetLabel('%i x %i' % (width, height))
            self.ctrlDict['error'].SetLabel('%.2f' % error+' %')
        except:
            width = height = -1
            self.ctrlDict['resize'].SetLabel('')
            self.ctrlDict['error'].SetLabel('')
        self.final_width = width
        self.final_height = height

    def ComputeWidthHeightError(self, target_width, widthi, heighti, pari_x, pari_y, wmod, hmod, paro_x, paro_y):
        aspectratio = (widthi / heighti) * (pari_x / pari_y)
        width = round(target_width / wmod) * wmod
        height = round(width * paro_x / paro_y / aspectratio / hmod) * hmod
        newaspectratio = width * paro_x / paro_y / float(height)
        error = 100 * abs(aspectratio - newaspectratio) / float(aspectratio)
        return (width, height, error)

    def FindNextResize(self, forward=True):
        searcherror = self.options['searcherror']
        widthi = float(self.ctrlDict['widthi'].GetValue())
        heighti = float(self.ctrlDict['heighti'].GetValue())
        pari_x = float(self.ctrlDict['pari_x'].GetValue())
        pari_y = float(self.ctrlDict['pari_y'].GetValue())
        wmod = self.options['wmod']
        hmod = self.options['hmod']
        paro_x = self.options['paro_x']
        paro_y = self.options['paro_y']
        value = self.ctrlDict['slider'].GetValue()
        minValue = self.ctrlDict['slider'].GetMin()
        maxValue = self.ctrlDict['slider'].GetMax()
        if forward:
            if value == maxValue:
                self.ctrlDict['slider'].SetFocus()
                return
            target_widths = [float(wmod * i) for i in xrange(value+1, maxValue+1)]
        else:
            if value == minValue:
                self.ctrlDict['slider'].SetFocus()
                return
            target_widths = [float(wmod * i) for i in xrange(value-1, minValue-1, -1)]
        for target_width in target_widths:
            width, height, error = self.ComputeWidthHeightError(target_width, widthi, heighti, pari_x, pari_y, wmod, hmod, paro_x, paro_y)
            if error <= searcherror:
                newValue = int(target_width / wmod)
                self.ctrlDict['slider'].SetValue(newValue)
                self.CalculateResize()
                break
        self.ctrlDict['slider'].SetFocus()

    def CalculateRangeAndResize(self):
        try:
            # Get old slider values
            oldValue = self.ctrlDict['slider'].GetValue()
            oldMinValue = self.ctrlDict['slider'].GetMin()
            oldMaxValue = self.ctrlDict['slider'].GetMax()
            # Compute new slider values
            input_width = int(self.ctrlDict['widthi'].GetValue())
            minresize = self.options['minresize']
            maxresize = self.options['maxresize']
            wmod = self.options['wmod']
            defaultValue = int(round(input_width / wmod))
            minValue = int(round(input_width * (minresize / 100.0) / wmod))
            maxValue = int(round(input_width * (maxresize / 100.0) / wmod))
            # Modify the slider as necessary
            if minValue != oldMinValue or maxValue != oldMaxValue:
                self.ctrlDict['slider'].SetRange(minValue, maxValue)
                if oldValue >= minValue and oldValue <= maxValue:
                    defaultValue = oldValue
                self.ctrlDict['slider'].SetValue(defaultValue)
        except:
            pass
        self.CalculateResize()

    def GetAvisynthResize(self):
        try:
            strWidth = '%i' % self.final_width
            strHeight = '%i' % self.final_height
        except ValueError:
            strWidth = strHeight = '-1'
        return self.options['avisynthresize'].replace('%width%', strWidth).replace('%height%', strHeight)#+'\n'

    def ConfigureOptions(self):
        dlg = ResizeCalculatorOptionsDialog(self)
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            self.options = dlg.GetOptionsDict()
            self.SaveOptions()
            self.ctrlDict['paro_x'].SetLabel('%i' % self.options['paro_x'])
            self.ctrlDict['paro_y'].SetLabel('%i' % self.options['paro_y'])
            self.ctrlDict['wmod'].SetLabel('%i' % self.options['wmod'])
            self.ctrlDict['hmod'].SetLabel('%i' % self.options['hmod'])
            self.ctrlDict['minresize'].SetLabel('%i' % self.options['minresize']+'%')
            self.ctrlDict['maxresize'].SetLabel('%i' % self.options['maxresize']+'%')
            self.ctrlDict['searcherror'].SetLabel('%.1f' % self.options['searcherror'] + '%')
            self.CalculateRangeAndResize()
            self.GetSizer().Layout()
        dlg.Destroy()

    def OnButtonPAR(self, event):
        win = event.GetEventObject()
        posx, posy = win.GetPositionTuple()
        pos = (posx, posy+win.GetSize()[1])
        self.PopupMenu(self.par_menu, pos)

    def OnMenuPixelAspectRatio(self, event):
        label = self.par_menu.GetLabel(event.GetId())
        par_x, par_y = label.split('-')[1].split(':', 1)
        self.ctrlDict['pari_x'].SetValue(par_x.strip())
        self.ctrlDict['pari_y'].SetValue(par_y.strip())

class ResizeCalculatorOptionsDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, _('Configure options'))
        dpi.SetFontPPI(self)
        self.parent = parent
        self.options = parent.options.copy()
        self.ctrlDict = {}
        self.CreateInterface()
        self.CreatePixelAspectRatioMenu()
        self.SetDefaultValues()
        self.Center()

    def CreateInterface(self):
        int5 = intPPI(5)
        generalSizer = wx.BoxSizer(wx.VERTICAL)
        # Settings
        info = (
            ('paro_x', 'paro_y', _('Target pixel aspect ratio:'), intPPI(40), ':', None),
            ('wmod', 'hmod', _('Resize block constraints:'), intPPI(30), 'x', None),
            ('minresize', 'maxresize', _('Resize percent ranges:'), intPPI(30), '-', '%'),
        )
        for xkey, ykey, label, ctrlwidth, divider, extra in info:
            staticText = wx.StaticText(self, wx.ID_ANY, label)
            textCtrlx = wx.TextCtrl(self, wx.ID_ANY, size=(ctrlwidth, -1))
            textCtrly = wx.TextCtrl(self, wx.ID_ANY, size=(ctrlwidth, -1))
            self.ctrlDict[xkey] = textCtrlx
            self.ctrlDict[ykey] = textCtrly
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
            sizer.Add(textCtrlx, 0, wx.EXPAND|wx.RIGHT, 0)
            if extra is None:
                sizer.Add(wx.StaticText(self, wx.ID_ANY, divider), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, intPPI(4))
                sizer.Add(textCtrly, 0, wx.EXPAND|wx.RIGHT, 0)
            else:
                sizer.Add(wx.StaticText(self, wx.ID_ANY, extra), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, intPPI(2))
                sizer.Add(wx.StaticText(self, wx.ID_ANY, divider), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, intPPI(4))
                sizer.Add(textCtrly, 0, wx.EXPAND|wx.RIGHT, 0)
                sizer.Add(wx.StaticText(self, wx.ID_ANY, extra), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, intPPI(2))
            if xkey == 'paro_x':
                button = wx.Button(self, wx.ID_ANY, '...', size=(intPPI(30),-1))
                self.Bind(wx.EVT_BUTTON, self.OnButtonPAR, button)
                sizer.Add(button, 0, wx.LEFT, int5)
            generalSizer.Add(sizer, 0, wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT, int5)
        staticText = wx.StaticText(self, wx.ID_ANY, _('Max search aspect ratio error:'))
        textCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(intPPI(40), -1))
        self.ctrlDict['searcherror'] = textCtrl
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, int5)
        sizer.Add(textCtrl, 0, wx.EXPAND|wx.RIGHT, 0)
        sizer.Add(wx.StaticText(self, wx.ID_ANY, '%'), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, intPPI(2))
        generalSizer.Add(sizer, 0, wx.EXPAND|wx.LEFT|wx.TOP|wx.RIGHT, int5)
        generalSizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, int5)
        # Avisynth resize
        staticText = wx.StaticText(self, wx.ID_ANY, _('Avisynth resize:'))
        textCtrl = wx.TextCtrl(self, wx.ID_ANY)
        self.ctrlDict['avisynthresize'] = textCtrl
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)
        sizer.Add(textCtrl, 1, wx.EXPAND|wx.LEFT, int5)
        generalSizer.Add(sizer, 0, wx.EXPAND|wx.ALL, int5)
        # Standard buttons
        okay  = wx.Button(self, wx.ID_OK, _('OK'))
        cancel = wx.Button(self, wx.ID_CANCEL, _('Cancel'))
        stdbtns = wx.StdDialogButtonSizer()
        stdbtns.AddButton(okay)
        stdbtns.AddButton(cancel)
        stdbtns.Realize()
        generalSizer.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, int5)
        generalSizer.Add(stdbtns, 0, wx.EXPAND|wx.ALL, int5)
        # Total
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(generalSizer, 0, wx.EXPAND|wx.ALL, intPPI(10))
        self.SetSizer(dlgSizer)
        dlgSizer.Fit(self)

    def CreatePixelAspectRatioMenu(self):
        menuInfo = (
            ('PC', 1, 1),
            (''),
            ('PAL 4:3', 59, 54),
            ('PAL 16:9', 118, 81),
            ('PAL VCD', 59, 54),
            ('PAL SVCD 4:3', 59, 36),
            ('PAL SVCD 16:9', 59, 27),
            ('PAL SVCD 2.21:1', '2.7123', 1),
            (''),
            ('NTSC 4:3', 10, 11),
            ('NTSC 16:9', 40, 33),
            ('NTSC VCD', 10, 11),
            ('NTSC SVCD 4:3', 15, 11),
            ('NTSC SVCD 16:9', 20, 11),
            ('NTSC SVCD 2.21:1', '2.2602', 1),
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
                    label = '%s - %s:%s' % (label, par_x, par_y)
                    handler = self.OnMenuPixelAspectRatio
                menuItem = self.par_menu.Append(wx.ID_ANY, label, '')
                self.Bind(wx.EVT_MENU, handler, menuItem)

    def SetDefaultValues(self):
        self.ctrlDict['paro_x'].SetValue('%i' % self.options['paro_x'])
        self.ctrlDict['paro_y'].SetValue('%i' % self.options['paro_y'])
        self.ctrlDict['wmod'].SetValue('%i' % self.options['wmod'])
        self.ctrlDict['hmod'].SetValue('%i' % self.options['hmod'])
        self.ctrlDict['minresize'].SetValue('%i' % self.options['minresize'])
        self.ctrlDict['maxresize'].SetValue('%i' % self.options['maxresize'])
        self.ctrlDict['searcherror'].SetValue('%.1f' % self.options['searcherror'])
        self.ctrlDict['avisynthresize'].SetValue(self.options['avisynthresize'])

    def OnButtonPAR(self, event):
        win = event.GetEventObject()
        posx, posy = win.GetPositionTuple()
        pos = (posx, posy+win.GetSize()[1])
        self.PopupMenu(self.par_menu, pos)

    def OnMenuPixelAspectRatio(self, event):
        label = self.par_menu.GetLabel(event.GetId())
        par_x, par_y = label.split('-')[1].split(':', 1)
        self.ctrlDict['paro_x'].SetValue(par_x.strip())
        self.ctrlDict['paro_y'].SetValue(par_y.strip())

    def GetOptionsDict(self):
        info = (
            ('paro_x', int),
            ('paro_y', int),
            ('wmod', int),
            ('hmod', int),
            ('minresize', int),
            ('maxresize', int),
            ('searcherror', float),
            ('avisynthresize', str),
        )
        for key, handle in info:
            try:
                strValue = self.ctrlDict[key].GetValue()
                value = handle(strValue)
                self.options[key] = value
            except ValueError:
                pass
        return self.options

def avsp_run():
    text = avsp.GetText().strip()
    parent = avsp.GetWindow()
    if text:
        if not avsp.UpdateVideo():
            avsp.MsgBox(_('The current Avisynth script contains errors.'), _('Error'))
            return
        width = avsp.GetVideoWidth()
        height = avsp.GetVideoHeight()
    else:
        width = 1280
        height = 720
    dlg = ResizeCalculatorDialog(parent, text, width, height)
    ID = dlg.ShowModal()
    if text and ID == wx.ID_OK:
        avsp.InsertText(dlg.GetAvisynthResize(), -2)
        avsp.ShowVideoFrame(forceRefresh=True)
    dlg.Destroy()
