#-------------------------------------------------------------------------------
# Name:        DeleteEncodings.py
#              Purpose: Deletes the files selected in the script from disk (PreviewEncode)
#                       Deletes also the avs files e.g. star.mkv and star.mkv.avs
#                       Several lines can be selected, but if there are more files in one line,
#                           no file will be recognized in this line.
#                       The files are first displayed in a list before they are deleted.
#
# Author:      GPo
#
# Created:     11.06.2021, last change 25.05.2024
#              update 12.0.6.2021
#                  dpi, addFile, fileSize, fix return wrong result, freeing the files before deleting
#              bugfix: 25.05.2024
# Copyright:   (c) GPo 2021
# Licence:     <free>
#-------------------------------------------------------------------------------
import wx
import os
import dpi

##################################################
##### You use this script to your own risk ! #####
##################################################

# if True, another message is shown before deleting the files
showWarn = True

def deleteFiles(files):
    error = ok = notFound = 0
    for f in files:
        if os.path.isfile(f):
            try:
                os.remove(f)
            except:
                error += 1
            if not os.path.isfile(f):
                ok += 1
        else: notFound += 1
    return ok, notFound, error

def addFile(fList, f):
    fSize = 0
    if not f in fList:
        fList.append(f)
        fSize = os.path.getsize(f)
        if os.path.isfile(f + '.avs'):
            fList.append(f + '.avs')
            fSize += os.path.getsize(f + '.avs')
    return fSize

# input in Byte
def fileSizeToString(fsize, precision=0):
    if fsize < 1:
        return '0 B'
    suffixes = ['B','KB','MB','GB','TB']
    suffixIndex = 0
    while fsize > 1024 and suffixIndex < 4:
        suffixIndex += 1
        fsize = fsize/1024.0
    if suffixIndex > 2 and precision == 0:
        precision = 2
    return '%.*f%s' % (precision, fsize, suffixes[suffixIndex])

def showDlg(files, fSize, showWarn):
    dlg = wx.Dialog(None, wx.ID_ANY, _('Delete') + fSize, style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
    try:
        # PPI settings, but don't know if it needed for wx.Dialog
        #~dpi.SetFontPPI(dlg)
        okay  = wx.Button(dlg, wx.ID_OK, _('OK'))
        cancel  = wx.Button(dlg, wx.ID_CANCEL, _('Cancel'))
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        textCtrl = wx.TextCtrl(dlg, wx.ID_ANY, size=dpi.tuplePPI(600,200), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP)
        textCtrl.AppendText('\n'.join(files))
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(textCtrl, 1, wx.EXPAND)
        dlgSizer.Add(btns , 0, wx.EXPAND|wx.ALL, dpi.intPPI(10))
        dlg.SetSizer(dlgSizer)
        dlgSizer.Layout()
        dlg.Fit()
        if dlg.ShowModal() != wx.ID_OK:
            return
    finally:
        dlg.Destroy()
    if showWarn and not avsp.MsgBox('Delete files from disk?', cancel=True):
        return
    # freeing the files if in use
    self = avsp.GetWindow()
    if self.currentScript.AVI is not None:
        self.HidePreviewWindow()
        self.OnMenuScriptReleaseMemory(None)
    # delete the files
    msg = ''
    ok, notFound, error = deleteFiles(files)
    if ok > 0:
        msg = '%i File(s) deleted\n' % ok
    if notFound > 0:
        msg += '%i File(s) not found\n' % notFound
    if error > 0:
        msg += '%i Error(s)' % error
    avsp.MsgBox(msg)

txt = avsp.GetSelectedText()
if not txt:
    avsp.MsgBox('You must first select the files')
    return
fileSize = 0
txtLines = txt.split('\n')
files = []
for line in txtLines:
    sa = line.split('"')
    if len(sa) == 3:   # bla("star.mkv", blabla
        if os.path.isfile(sa[1]):
            fileSize += addFile(files, sa[1])
    elif len(sa) == 2: # C:\star.mkv", blabla
        f = ''
        if os.path.isfile(sa[0]):
            f = sa[0]
        elif os.path.isfile(sa[1]):
            f = sa[1]
        if f:
            fileSize += addFile(files, f)
    else:
        line = line.replace('"', '')
        if os.path.isfile(line):
            fileSize += addFile(files, line)

if files:
    fSize = ' ' + fileSizeToString(fileSize)
    showDlg(files, fSize, showWarn)
else:
    avsp.MsgBox('No file recognized or the file is not on the disk')
