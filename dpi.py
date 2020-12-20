#-------------------------------------------------------------------------------
# Name:        dpi
# Purpose:
#
# Author:      GPo
#
# Created:     17.12.2020
# Copyright:   (c) GPo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys
import ctypes
import wx
import global_vars

ppi_factor = 1.0

def intPPI(i):
    return int(ppi_factor * i)

def floatPPI(f):
    return float(ppi_factor * f)

def tuplePPI(n1,n2):
    return ((int(ppi_factor * n1), int(ppi_factor * n2)))

def SetFontPPI(obj):
    if ppi_factor > 1:
        font = obj.GetFont()
        font.SetPointSize(intPPI(font.GetPointSize()))
        obj.SetFont(font)

class DPI():
    def __init__(self):
        self.ppi = 96.0
        self.ppi_factor = 1.0
        self.DpiAwareness = False

    def GetPPIFactor(self, setPPI=False):
        if os.name != 'nt':
            return 1.0
        if self.DpiAwareness:
            return self.ppi_factor
        pw, ph = wx.ScreenDC().GetPPI()
        if ph < 110:
            ph = 96.0
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2) # Win 10 (mode 2)
            self.DpiAwareness = True
        except:
            try:
                ctypes.windll.user32.SetProcessDPIAware() # Win 8,7 (mode 1)
                self.DpiAwareness = True
            except:
                pass
        if self.DpiAwareness:
            try:
                self.ppi_factor = float(ph / 96.0)
            except:
                pass

        self.ppi = ph
        if setPPI:
            global ppi_factor
            ppi_factor = self.ppi_factor
            global_vars.ppi_factor = self.ppi_factor
        return self.ppi_factor



