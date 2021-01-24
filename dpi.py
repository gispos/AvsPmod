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
dpiAware = False
dpiAwareness = 0

def intPPI(n):
    return int(ppi_factor * n)

def roundPPI(n):
    return round(ppi_factor * n)

def floatPPI(n):
    return ppi_factor * float(n)

def tuplePPI(n1,n2):
    return ((int(ppi_factor * n1), int(ppi_factor * n2)))

def SetFontPPI(obj, size_adj=0):
    if ppi_factor > 1:
        font = obj.GetFont()
        font.SetPointSize(intPPI(font.GetPointSize())+size_adj)
        obj.SetFont(font)

class DPI():
    def __init__(self):
        self.ppi_factor = 1.0
        self.dpiAware = False
        self.dpiAwareness = 0

    def GetPPIFactor(self, setPPI=False):
        if os.name != 'nt':
            return 1.0
        if self.dpiAware:
            return self.ppi_factor

        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2) # Win 10 (mode 2) monitor v2 (win10 sizes the non client areas)
            self.dpiAware = True
            self.dpiAwareness = 2
        except:
            try:
                ctypes.windll.user32.SetProcessDPIAware() # Win 8,7 (mode 1) windows borders, title bar may be to small
                self.dpiAware = True
                self.dpiAwareness = 1
            except:
                pass
        if self.dpiAware:
            pw, ph = wx.ScreenDC().GetPPI()
            #pw, ph = wx.GetDisplayPPI()
            if ph < 110:
                ph = 96.0
            try:
                self.ppi_factor = float(ph / 96.0)
            except:
                pass

        global dpiAware
        global dpiAwareness
        dpiAware = self.dpiAware
        dpiAwareness = self.dpiAwareness

        if setPPI:
            global ppi_factor
            ppi_factor = self.ppi_factor
            global_vars.ppi_factor = self.ppi_factor
        return self.ppi_factor



