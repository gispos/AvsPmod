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
# Created:     11.06.2021
# Copyright:   (c) GPo 2021
# Licence:     <free>
#-------------------------------------------------------------------------------
import wx
import os
global showWarn

##################################################
##### You use this script to your own risk ! #####
##################################################

# if True, another message is shown before deleting the files
showWarn = True

def deleteFiles(files):
    error = ok = notFound = 0
    for file in files:
        if os.path.isfile(file):
            try:
                os.remove(file)
                ok += 1
            except:
                error += 1
        else: notFound += 1
    return ok, notFound, error

def showDlg(files):
    dlg = wx.Dialog(None, wx.ID_ANY, _('Delete'), style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
    okay  = wx.Button(dlg, wx.ID_OK, _('OK'))
    cancel  = wx.Button(dlg, wx.ID_CANCEL, _('Cancel'))
    btns = wx.StdDialogButtonSizer()
    btns.AddButton(okay)
    btns.AddButton(cancel)
    btns.Realize()
    textCtrl = wx.TextCtrl(dlg, wx.ID_ANY, size=(600,200), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP)
    textCtrl.AppendText('\n'.join(files))
    dlgSizer = wx.BoxSizer(wx.VERTICAL)
    dlgSizer.Add(textCtrl, 1, wx.EXPAND)
    dlgSizer.Add(btns , 0, wx.EXPAND|wx.ALL, 10)
    dlg.SetSizer(dlgSizer)
    dlgSizer.Layout()
    dlg.Fit()
    if dlg.ShowModal() != wx.ID_OK:
        return
    if showWarn and not avsp.MsgBox('Delete files from disk?', cancel=True):
        return
    msg = ''
    ok, notFound, error = deleteFiles(files)
    if ok > 0:
        msg = '%i: Files deleted\n' % ok
    if notFound > 0:
        msg += '%i: Files not found\n' % notFound
    if error > 0:
        msg += '%i: Errors' % error
    avsp.MsgBox(msg)


txt = avsp.GetSelectedText()
if not txt:
    avsp.MsgBox('You must first select the files')
    return
txtLines = txt.split('\n')
files = []
for line in txtLines:
    sa = line.split('"')
    if len(sa) == 3:
        if os.path.isfile(sa[1]):
            if sa[1] in files:
                continue
            files.append(sa[1])
            if os.path.isfile(sa[1] + '.avs'):
                files.append(sa[1] + '.avs')
    else:
        line = line.replace('"', '')
        if os.path.isfile(line):
            if line in files:
                continue
            files.append(line)
            if os.path.isfile(line + '.avs'):
                files.append(line + '.avs')

if files:
    showDlg(files)
else:
    avsp.MsgBox('No file recognized or the file is not on the disk')