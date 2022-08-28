# wxp - general framework classes for wxPython
#
# Copyright 2007 Peter Jang <http://avisynth.nl/users/qwerpoi>
#           2010-2013 the AvsPmod authors <https://github.com/avspmod/avspmod>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA, or visit
#  http://www.gnu.org/copyleft/gpl.html .

# Dependencies:
#     Python (tested on v2.6 and 2.7)
#     wxPython (tested on v2.8 Unicode and 2.9)
# Scripts:
#     icon.py (icons embedded in a Python script)

import wx
import wx.lib.buttons as wxButtons
import wx.lib.mixins.listctrl  as  listmix
import wx.lib.filebrowsebutton as filebrowse
import wx.lib.colourselect as  colourselect
#import colourselect_dpi as colourselect
from wx.lib.agw.floatspin import FloatSpin
from wx.lib.agw.hyperlink import HyperLinkCtrl
import wx.lib.agw.ultimatelistctrl as ULC
from wx import stc
import string
import keyword
import os
import os.path
import sys
import copy
import time
import dpi

import wx.lib.newevent
import socket
try:
    import thread
except:
    pass
    # or import threading??

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO # not 100% the same, ComvertError can occur
    # Python 3: The StringIO and cStringIO modules are gone.
    # Instead, import the io module and use io.StringIO or io.BytesIO for text and data respectively.

try:
    import cPickle # Python 2
except ImportError:
    import pickle as cPickle # Python 3

from icons import checked_icon, unchecked_icon

OPT_ELEM_CHECK = 0
OPT_ELEM_INT = 1
OPT_ELEM_FLOAT = 1
OPT_ELEM_SPIN = 1
OPT_ELEM_STRING = 2
OPT_ELEM_FILE = 3
OPT_ELEM_FILE_OPEN = 3
OPT_ELEM_FILE_SAVE = 4
OPT_ELEM_FILE_URL = 5
OPT_ELEM_DIR = 6
OPT_ELEM_DIR_URL = 7
OPT_ELEM_RADIO = 8
OPT_ELEM_LIST = 9
OPT_ELEM_SLIDER = 10
OPT_ELEM_COLOR = 11
OPT_ELEM_FONT = 12
OPT_ELEM_BUTTON = 13
OPT_ELEM_SEP = 14

keyStringList = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
    'Enter', 'Space', 'Escape', 'Tab', 'Insert', 'Backspace', 'Delete',
    'Home', 'End', 'PgUp', 'PgDn', 'Up', 'Down', 'Left', 'Right', 'NumLock',
    'Numpad 0', 'Numpad 1', 'Numpad 2', 'Numpad 3', 'Numpad 4', 'Numpad 5', 'Numpad 6', 'Numpad 7', 'Numpad 8', 'Numpad 9',
    'Numpad +', 'Numpad -', 'Numpad *', 'Numpad /', 'Numpad .', 'Numpad Enter',
    '`', '-', '=', '\\', '[', ']', ';', "'", ',', '.', '/',
    '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '|', '{', '}', ':', '"', '<', '>', '?',
]

numpadDict = {
    'NumLock' : wx.WXK_NUMLOCK,
    'Numpad 0': wx.WXK_NUMPAD0,
    'Numpad 1': wx.WXK_NUMPAD1,
    'Numpad 2': wx.WXK_NUMPAD2,
    'Numpad 3': wx.WXK_NUMPAD3,
    'Numpad 4': wx.WXK_NUMPAD4,
    'Numpad 5': wx.WXK_NUMPAD5,
    'Numpad 6': wx.WXK_NUMPAD6,
    'Numpad 7': wx.WXK_NUMPAD7,
    'Numpad 8': wx.WXK_NUMPAD8,
    'Numpad 9': wx.WXK_NUMPAD9,
    'Numpad +': wx.WXK_NUMPAD_ADD,
    'Numpad -': wx.WXK_NUMPAD_SUBTRACT,
    'Numpad *': wx.WXK_NUMPAD_MULTIPLY,
    'Numpad /': wx.WXK_NUMPAD_DIVIDE,
    'Numpad .': wx.WXK_NUMPAD_DECIMAL,
    'Numpad Enter': wx.WXK_NUMPAD_ENTER,
}

(PostArgsEvent, EVT_POST_ARGS) = wx.lib.newevent.NewEvent()

try: _
except NameError:
    def _(s): return s

def MakeWindowTransparent(window, amount, intangible=False):
    import ctypes
    user32 = ctypes.windll.user32
    hwnd = window.GetHandle()
    style = user32.GetWindowLongA(hwnd, 0xffffffec) # Python3: no L suffix after 0xffffffec
    style |= 0x00080000
    if intangible:
        style |= 0x00000020  # Python3: no L suffix
        window.SetWindowStyleFlag(window.GetWindowStyleFlag()|wx.STAY_ON_TOP)
    user32.SetWindowLongA(hwnd, 0xffffffec, style)  # Python3: no L suffix after 0xffffffec
    user32.SetLayeredWindowAttributes(hwnd, 0, amount, 2)

def GetTranslatedShortcut(shortcut):
        return shortcut.replace('Ctrl', _('Ctrl')).replace('Shift', _('Shift')).replace('Alt', _('Alt'))

class CharValidator(wx.PyValidator):
    def __init__(self, flag):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        return CharValidator(self.flag)

    def Validate(self, win):
        return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True

    def OnChar(self, event):
        key = event.GetKeyCode()
        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return
        if self.flag == 'alpha' and chr(key) in string.letters:
            event.Skip()
            return
        if self.flag == 'digit' and chr(key) in string.digits:
            event.Skip()
            return
        return

class ListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.parent = parent

    def SelectItem(self, item, setFocus=True):
        self.SetItemState(item, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED)
        self.EnsureVisible(item)
        if setFocus:
            self.SetFocus()

    def SelectLabel(self, label):
        item = self.FindItem(-1, label)
        self.SelectItem(item)

    def GetSelectedItem(self):
        return self.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)

class UListCtrl(ULC.UltimateListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID,  agwStyle=0):
        ULC.UltimateListCtrl.__init__(self, parent, ID, agwStyle=agwStyle)
        self.parent = parent

    def SelectItem(self, item):
        self.SetItemState(item, ULC.ULC_STATE_SELECTED|ULC.ULC_STATE_FOCUSED, ULC.ULC_STATE_SELECTED|ULC.ULC_STATE_FOCUSED)
        self.EnsureVisible(item)

    def GetSelectedItem(self):
        return self.GetNextItem(-1, ULC.ULC_NEXT_ALL, ULC.ULC_STATE_SELECTED)

class MenuItemInfo(object):
    def __init__(self, label=None, handler=None, status=None, submenu=None, id=wx.ID_ANY):
        self.label = label
        self.handler = handler
        self.submenu = submenu
        self.id = id

class StdoutStderrWindow:
    """
    A class that can be used for redirecting Python's stdout and
    stderr streams.  It will do nothing until something is written to
    the stream at which point it will create a Frame with a text area
    and write the text there.
    """
    def __init__(self, title=None):
        if title is None:
            title = _('Error Window')
        self.frame  = None
        self.title  = title
        self.pos    = wx.DefaultPosition
        self.size   = dpi.tuplePPI(550, 300)
        self.parent = None
        logname = 'error_log.txt'
        if hasattr(sys,'frozen'):
            self.logfilename = os.path.join(os.path.dirname(sys.executable), logname)
        else:
            self.logfilename = os.path.join(os.getcwdu(), logname)
        self.firstTime = True

    def SetParent(self, parent):
        """Set the window to be used as the popup Frame's parent."""
        self.parent = parent


    def CreateOutputWindow(self, st):
        self.frame = wx.Frame(self.parent, -1, self.title, self.pos, self.size,
                              style=wx.DEFAULT_FRAME_STYLE)
        dpi.SetFontPPI(self.frame)
        self.text  = TextCtrl(self.frame, -1, "",
                                 style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.text.AppendText(st)
        self.frame.Show(True)
        wx.EVT_CLOSE(self.frame, self.OnCloseWindow)


    def OnCloseWindow(self, event):
        if self.frame is not None:
            self.frame.Destroy()
        self.frame = None
        self.text  = None


    # These methods provide the file-like output behaviour.
    def write(self, text):
        """
        Create the output window if needed and write the string to it.
        If not called in the context of the gui thread then uses
        CallAfter to do the work there.
        """
        if self.frame is None:
            if not wx.Thread_IsMain():
                wx.CallAfter(self.CreateOutputWindow, text)
            else:
                self.CreateOutputWindow(text)
        else:
            if not wx.Thread_IsMain():
                wx.CallAfter(self.text.AppendText, text)
            else:
                self.text.AppendText(text)
        f = open(self.logfilename, 'a')
        if self.firstTime:
            f.write('\n[%s]\n' % time.asctime())
            self.firstTime = False
        f.write(text)
        f.close()


    def close(self):
        if self.frame is not None:
            wx.CallAfter(self.frame.Close)


    def flush(self):
        pass

class App(wx.App):
    outputWindowClass = StdoutStderrWindow

class SingleInstanceApp(wx.App):
    outputWindowClass = StdoutStderrWindow

    #~port = 50009
    # GPo 2020, make sure the port in AvsPmode is the same
    # make a difference between x64, x32
    xSys = 'x64' if sys.maxsize > 2**32 else 'x32'
    port = 50009 if xSys == 'x64' else 50008

    name = 'SingleInstanceApp'
    IsFirstInstance = True
    boolSingleInstance = True
    def __init__(self, *args, **kwargs):
        # Get extra keyword arguments

        if kwargs.has_key('name'):
            #~self.name = kwargs.pop('name')
            self.name = kwargs.pop('name') + xSys # GPo 2020, make sure the name in AvsPmode is the same
        if kwargs.has_key('port'):
            self.port = kwargs.pop('port')
        # Determine if program is already running or not
        self.instance = wx.SingleInstanceChecker(self.name+wx.GetUserId())
        if self.instance.IsAnotherRunning():
            self.IsFirstInstance = False
            if self.boolSingleInstance:
                # Send data to the main instance via socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(('localhost', self.port))
                pickledstring = StringIO()
                cPickle.dump(sys.argv[1:],pickledstring)
                sock.sendall(pickledstring.getvalue())
                response = sock.recv(8192)
            # Start the wx.App (typically check self.IsFirstInstance flag and return False)
            wx.App.__init__(self, *args, **kwargs)
        else:
            self.IsFirstInstance = True
            wx.App.__init__(self, *args, **kwargs)
            # Start socket server (in a separate thread) to receive arguments from other instances
            self.argsPosterThread = ArgsPosterThread(self)
            self.argsPosterThread.Start()

    def OnExit(self):
        if self.IsFirstInstance:
            wx.Yield()
            self.argsPosterThread.Stop()
            running = 1
            while running:
                running = 0
                running = running + self.argsPosterThread.IsRunning()
                time.sleep(0.1)

class ArgsPosterThread:
    def __init__(self, app):
        self.app = app

    def Start(self):
        self.keepGoing = self.running = True
        thread.start_new_thread(self.Run, ())

    def Stop(self):
        self.keepGoing = False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(('localhost', self.app.port))
            sock.close()
        except:
            pass

    def IsRunning(self):
        return self.running

    def Run(self):

        # Prevent open sockets from being inherited by child processes
        # see http://bugs.python.org/issue3006
        # code taken from CherryPy
        #
        # Copyright (c) 2004-2011, CherryPy Team (team@cherrypy.org)
        # All rights reserved.
        #
        # Redistribution and use in source and binary forms, with or without modification,
        # are permitted provided that the following conditions are met:
        #
        #     * Redistributions of source code must retain the above copyright notice,
        #       this list of conditions and the following disclaimer.
        #     * Redistributions in binary form must reproduce the above copyright notice,
        #       this list of conditions and the following disclaimer in the documentation
        #       and/or other materials provided with the distribution.
        #     * Neither the name of the CherryPy Team nor the names of its contributors
        #       may be used to endorse or promote products derived from this software
        #       without specific prior written permission.
        #
        # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
        # ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
        # WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        # DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
        # FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
        # DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
        # SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
        # CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
        # OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
        # OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
        try:
            import fcntl
        except ImportError:
            try:
                from ctypes import windll, WinError
            except ImportError:
                def prevent_socket_inheritance(sock):
                    """Dummy function, since neither fcntl nor ctypes are available."""
                    pass
            else:
                def prevent_socket_inheritance(sock):
                    """Mark the given socket fd as non-inheritable (Windows)."""
                    if not windll.kernel32.SetHandleInformation(sock.fileno(), 1, 0):
                        raise WinError()
        else:
            def prevent_socket_inheritance(sock):
                """Mark the given socket fd as non-inheritable (POSIX)."""
                fd = sock.fileno()
                old_flags = fcntl.fcntl(fd, fcntl.F_GETFD)
                fcntl.fcntl(fd, fcntl.F_SETFD, old_flags | fcntl.FD_CLOEXEC)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        prevent_socket_inheritance(sock)
        sock.bind(('localhost',self.app.port))
        sock.listen(5)
        try:
            while self.keepGoing:
                newSocket, address = sock.accept()
                prevent_socket_inheritance(newSocket)
                while True:
                    receivedData = newSocket.recv(8192)
                    if not receivedData: break
                    # Post a wxPython event with the unpickled data
                    pickledstring = StringIO(receivedData)
                    unpickled = cPickle.load(pickledstring)
                    evt = PostArgsEvent(data=unpickled)
                    wx.PostEvent(self.app, evt)
                    newSocket.sendall(receivedData)
                newSocket.close()
                if self.app.IsIconized():
                    self.app.Iconize(False)
                else:
                    self.app.Raise()
                if self.app.separatevideowindow and self.app.videoDialog.IsShown():
                    if self.app.videoDialog.IsIconized():
                        self.app.videoDialog.Iconize(False)
                    else:
                        self.app.videoDialog.Raise()
        finally:
            sock.close()
            self.running = False

class Frame(wx.Frame):

    def createMenuBar(self, menuBarInfo, shortcutList, oldShortcuts, menuBackups=[], backupShowShortcuts=False):
        '''
        General utility function to create a menu bar of menus
        Input is a list of label/menuInfo tuples
        The function utilizes the createMenu function (defined below)
        '''
        buckups = menuBackups[:]
        menuBackups[:] = []
        index = 0
        self._shortcutBindWindowDict = {}
        menuBar = wx.MenuBar()
        for eachMenuBarInfo in menuBarInfo:
            menuLabel = eachMenuBarInfo[0]
            menuInfo = eachMenuBarInfo[1:]
            menu = self.createMenu(menuInfo, menuLabel, shortcutList, oldShortcuts)
            menuBar.Append(menu, menuLabel)
            if index in buckups:
                menuBackups.append(self.createMenu(menuInfo, menuLabel, shortcutList, oldShortcuts, True, backupShowShortcuts))
            index += 1
        return menuBar

    def createMenu(self, menuInfo, name='', shortcutList = None, oldShortcuts=None, backup=False, backupShowShortcuts=False):
        menu = wx.Menu()
        if shortcutList is None:
            shortcutList = []
        if oldShortcuts is None:
            oldShortcutNames = []
            oldShortcuts = []
        else:
            try:
                oldShortcutNames, oldShortcutInfos = oldShortcuts
            except ValueError:
                oldShortcutNames = []
                oldShortcuts = []
        for eachMenuInfo in menuInfo:
            # Get the info, fill in missing info with defaults
            nItems = len(eachMenuInfo)
            # Special case: separator
            if eachMenuInfo == '' or nItems == 1:
                menu.AppendSeparator()
                menu.Remove(menu.Append(wx.ID_ANY, '0',).GetId()) # wxGTK fix
                continue
            if nItems > 7:
                raise
            defaults = ('', '', None, '', wx.ITEM_NORMAL, None, self)
            label, shortcut, handler, status, attr, state, bindwindow = eachMenuInfo + defaults[nItems:]
            if not bindwindow or bindwindow is None:
                bindwindow = self
            # Special case: submenu
            if handler is None: #not isinstance(handler, FunctionType):
                submenu = self.createMenu(shortcut, '%s -> %s'% (name, label), shortcutList, oldShortcuts, backup, backupShowShortcuts)
                menu.AppendMenu(wx.ID_ANY, label, submenu, status)
                continue
            elif handler == -1:
                submenu = shortcut #self.createMenu(shortcut, '%s -> %s'% (name, label), shortcutList, oldShortcuts, bindwindow)
                menu.AppendMenu(wx.ID_ANY, label, submenu, status)
                continue
            # Get the id and type (normal, checkbox, radio)
            if attr in (wx.ITEM_CHECK, wx.ITEM_RADIO):
                kind = attr
                id = wx.ID_ANY
            elif attr == wx.ITEM_NORMAL:
                kind = attr
                id = wx.ID_ANY
            elif type(attr) is tuple:
                kind, state, id = attr
            else:
                kind = wx.ITEM_NORMAL
                id = attr
            # Get the shortcut string
            itemName = '%s -> %s'% (name, label)
            itemName = itemName.replace('&', '')
            try:
                index = oldShortcutNames.index(itemName)
                shortcut = oldShortcutInfos[index][1]
            except ValueError:
                pass
            # GPo, show the shortcuts in the context menus (videoWindow, script)
            if backup:
                shortcutString = ''
                if backupShowShortcuts and shortcut != '':
                    for item in shortcutList:
                        if item[0] == itemName and item[1] == shortcut:
                            shortcutString = u'\t%s\u00a0' % GetTranslatedShortcut(shortcut)
                            break
            else:
                if shortcut != '' and shortcut not in [item[1] for item in shortcutList]:
                    shortcutString = u'\t%s\u00a0' % GetTranslatedShortcut(shortcut)
                else:
                    shortcutString = ''
            # Append the menu item
            if os.name != 'nt' and wx.version() >= '2.9': # XXX
                shortcutString = shortcutString[:-1]
            menuItem = menu.Append(id, '%s%s' % (label, shortcutString), status, kind)
            id = menuItem.GetId()
            self.Bind(wx.EVT_MENU, handler, menuItem)
            # Add the accelerator
            if shortcut is not None:
                if not backup and (shortcut == '' or not shortcut[-1].isspace()):
                    shortcutList.append([itemName, shortcut, id])
                try:
                    bindShortcutIdList = self._shortcutBindWindowDict.setdefault(bindwindow, [])
                    bindShortcutIdList.append(id)
                except AttributeError:
                    pass
            # Extra properties (enable/disable, check)
            if state is not None:
                if kind == wx.ITEM_NORMAL:
                    menuItem.Enable(state)
                else:
                    menuItem.Check(state)
        return menu

    def BindShortcutsToWindows(self, shortcutInfo, forcewindow=None):
        idDict = dict([(id, shortcut) for itemName, shortcut, id in shortcutInfo])
        forceAccelList = []
        for window, idList in self._shortcutBindWindowDict.items():
            accelList = []
            #~ for label, data in value.items():
                #~ accelString, id = data
                #~ accel = wx.GetAccelFromString('\t'+accelString)
                #~ accelList.append((accel.GetFlags(), accel.GetKeyCode(), id))
            for id in idList:
                try:
                    accelString = idDict[id]
                except KeyError:
                    continue
                #~ index = [z for x,y,z in shortcutInfo].index(id)
                accel = wx.GetAccelFromString('\t'+accelString)
                if accel is not None and accel.IsOk():
                    accelList.append((accel.GetFlags(), accel.GetKeyCode(), id))
                else:
                    for key in numpadDict:
                        if accelString.endswith(key):
                            break
                    accelString = accelString.replace(key, 'Space')
                    accel = wx.GetAccelFromString('\t'+accelString)
                    accelList.append((accel.GetFlags(), numpadDict[key], id))
            if forcewindow is None:
                accelTable = wx.AcceleratorTable(accelList)
                window.SetAcceleratorTable(accelTable)
            else:
                forceAccelList += accelList
        if forcewindow is not None:
            accelTable = wx.AcceleratorTable(forceAccelList)
            forcewindow.SetAcceleratorTable(accelTable)

    def accelListFromMenu(self, menu, accelList):
        for menuItem in menu.GetMenuItems():
            submenu = menuItem.GetSubMenu()
            if submenu is not None:
                self.accelListFromMenu(submenu, accelList)
            else:
                id = menuItem.GetId()
                text = menuItem.GetText()
                accel = wx.GetAccelFromString(text)
                if accel is not None and accel.IsOk():
                    accelList.append((accel.GetFlags(), accel.GetKeyCode(), id))

    def createButton(self, parent, label='', id=wx.ID_ANY, handler=None, pos=(0,0)):
        button = wx.Button(parent, id, label, pos)
        if handler:
            button.Bind(wx.EVT_BUTTON, handler)
        return button

    def createToolbarButton(self, parent, label, handler, pos=(0, 0), size=wx.DefaultSize, style=wx.NO_BORDER, toolTipTxt=None, statusTxt=None, showStatusTxt=True):
        # Return a static line if empty
        if type(label) == type('') and label == '':
            return wx.StaticLine(parent, style=wx.LI_VERTICAL)
        # Create the button
        try: # label is a bitmap
            w,h = label.GetSize()
            button = wxButtons.GenBitmapButton(parent, wx.ID_ANY, label, pos, size, style)
            button.SetBestSize((w+7, h+7))
        except AttributeError: # label is a string
            button = wxButtons.GenButton(parent, wx.ID_ANY, label, pos, size, style)
        # Bind the button to the given handler
        button.Bind(wx.EVT_BUTTON, handler)
        # Set the tool tip string if given
        if toolTipTxt:
            button.SetToolTipString(toolTipTxt)
        # Define mouse event functions (change status bar text and button bevel width)
        def OnMouseMove(event):
            if statusTxt and self.options['showbuttontooltip']:
                self.SetStatusText(statusTxt)
        def OnMouseOver(event):
            if statusTxt and self.options['showbuttontooltip']:
                self.SetStatusText(statusTxt)
            b = event.GetEventObject()
            b.SetBezelWidth(b.GetBezelWidth()+1)
            b.Refresh()
        def OnMouseLeave(event):
            if statusTxt and self.options['showbuttontooltip']:
                try:
                    self.ResetStatusText()
                except AttributeError:
                    self.SetStatusText('')
            b = event.GetEventObject()
            b.SetBezelWidth(b.GetBezelWidth()-1)
            b.Refresh()
        button.Bind(wx.EVT_ENTER_WINDOW, OnMouseOver)
        button.Bind(wx.EVT_MOTION, OnMouseMove)
        button.Bind(wx.EVT_LEAVE_WINDOW, OnMouseLeave)
        return button


class Notebook(wx.Notebook):
    """wx.Notebook, changing selected tab on mouse scroll"""

    def __init__(self, *args, **kwargs):
        self.invert_mouse_wheel_rotation = kwargs.pop('invert_scroll', False)
        wx.Notebook.__init__(self, *args, **kwargs)
        self.mouse_wheel_rotation = 0
        self.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheelNotebook)

    def OnMouseWheelNotebook(self, event):
        """Rotate between tabs"""
        rotation = event.GetWheelRotation()
        if self.mouse_wheel_rotation * rotation < 0:
            self.mouse_wheel_rotation = rotation
        else:
            self.mouse_wheel_rotation += rotation
        if abs(self.mouse_wheel_rotation) >= event.GetWheelDelta():
            inc = -1 if self.mouse_wheel_rotation > 0 else 1
            if self.invert_mouse_wheel_rotation: inc = -inc
            self.SelectTab(inc=inc)
            self.mouse_wheel_rotation = 0

    def SelectTab(self, index=None, inc=0):
        """Change to another tab

        index: go the specified tab
        inc: increment, with wrap-around"""
        nTabs = self.GetPageCount()
        if nTabs == 1:
            self.SetSelection(0)
            return True
        if index is None:
            index = inc + self.GetSelection()
            # Allow for wraparound with user-specified inc
            if index < 0:
                index = nTabs - abs(index) % nTabs
                if index == nTabs:
                    index = 0
            if index > nTabs - 1:
                index = index % nTabs
        # Limit index if specified directly by user
        if index < 0:
            return False
        if index > nTabs - 1:
            return False
        self.SetSelection(index)
        return True


class QuickFindDialog(wx.Dialog):
    ''' Simple find dialog for a wx.StyledTextCtrl, using FindReplaceDialog'''

    def __init__(self, parent, text=''):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, _('Quick find'), style=0)
        self.app = parent.app
        dpi.SetFontPPI(self)

        # Prepare a toolbar-like dialog
        find_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FIND))
        self.find_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1),
                                          style=wx.TE_PROCESS_ENTER, value=text)
        id = wx.ID_CLOSE if wx.version() >= '2.9' else wx.ID_OK
        self.close = wx.BitmapButton(self, id, bitmap=wx.ArtProvider.GetBitmap(wx.ART_CROSS_MARK))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(find_bitmap, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        sizer.Add(self.find_text_ctrl, 1, wx.EXPAND|wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, 5)
        sizer.Add(self.close, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        sizer.Fit(self)
        self.SetSizer(sizer)
        sizer.SetSizeHints(self)
        sizer.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnClose, self.close)
        self.Bind(wx.EVT_TEXT, self.OnInstantFindNext, self.find_text_ctrl)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnFindNext, self.find_text_ctrl)
        self.find_text_ctrl.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.find_text_ctrl.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

        # Auto-hide timer
        class QuickFindTimer(wx.Timer):
            def __init__(self, parent):
                wx.Timer.__init__(self)
                self.parent = parent
            def Notify(self):
                self.parent.Hide()
        self.timer = QuickFindTimer(self)

        # Bind open find/replace dialog and up and down arrows
        up_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnFindPrevious, id=up_id)
        down_id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.OnFindNext, id=down_id)
        accel_list = []
        accel_list.append(wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_UP, up_id))
        accel_list.append(wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_DOWN, down_id))
        find = replace = False
        find_menu = u'{0} -> {1}'.format(_('&Edit'), _('Find...')).replace('&', '')
        replace_menu = u'{0} -> {1}'.format(_('&Edit'), _('Replace...')).replace('&', '')
        for menu_item, shortcut, id in self.app.options['shortcuts']:
            if not find and menu_item.replace('&', '') == find_menu:
                accel = wx.GetAccelFromString('\t' + shortcut)
                if accel is not None and accel.IsOk():
                    accel_list.append(wx.AcceleratorEntry(accel.GetFlags(), accel.GetKeyCode(), id))
                    self.Bind(wx.EVT_MENU, lambda event:self.UpdateText(), id=id)
                find = True
            if not replace and menu_item.replace('&', '') == replace_menu:
                accel = wx.GetAccelFromString('\t' + shortcut)
                if accel is not None and accel.IsOk():
                    accel_list.append(wx.AcceleratorEntry(accel.GetFlags(), accel.GetKeyCode(), id))
                    self.Bind(wx.EVT_MENU, self.app.OnMenuEditReplace, id=id)
                replace = True
            if find and replace: break
        self.SetAcceleratorTable(wx.AcceleratorTable(accel_list))

    def SetFocus(self):
        self.find_text_ctrl.SetFocus()

    def OnSetFocus(self, event):
        self.timer.Stop()
        self.find_text_ctrl.SelectAll()

    def OnKillFocus(self, event):
        self.timer.Start(3000)

    def GetFindText(self):
        return self.find_text_ctrl.GetValue()

    def SetFindText(self, text):
        self.find_text_ctrl.ChangeValue(text)
        self.find_text_ctrl.SetInsertionPointEnd()

    def UpdateText(self, text=None):
        if text is None:
            text = self.app.currentScript.GetSelectedText()
        self.SetFindText(text)
        self.app.replaceDialog.SetFindText(text)

    def OnInstantFindNext(self, event):
        script = self.app.currentScript
        range = (script.GetSelectionStart(),
                 script.GetLineEndPosition(script.GetLineCount() - 1))
        self.app.replaceDialog.SetFindText(self.GetFindText())
        self.app.replaceDialog.OnFindNext(range=range, update_list=False)

    def OnFindNext(self, event):
        self.app.replaceDialog.SetFindText(self.GetFindText())
        self.app.replaceDialog.OnFindNext()

    def OnFindPrevious(self, event):
        self.app.replaceDialog.SetFindText(self.GetFindText())
        self.app.replaceDialog.OnFindPrevious()

    def OnClose(self, event):
        self.Hide()


class FindReplaceDialog(wx.Dialog):
    ''' Find/replace dialog for a wx.StyledTextCtrl'''

    def __init__(self, parent, text=''):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, _('Find/replace text'),
                           style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
        self.app = parent.app
        dpi.SetFontPPI(self)
        self.find_recent = self.app.options['find_recent']
        self.replace_recent = self.app.options['replace_recent']

        # Set controls
        panel = wx.Panel(self)
        find_text = wx.StaticText(self, wx.ID_ANY, _('Search &for'))
        self.find_text_ctrl = wx.ComboBox(self, wx.ID_ANY, style=wx.CB_DROPDOWN,
                            size=(dpi.intPPI(200),-1), value=text, choices=self.find_recent)
        replace_text = wx.StaticText(self, wx.ID_ANY, _('R&eplace with'))
        self.replace_text_ctrl = wx.ComboBox(self, wx.ID_ANY, size=(dpi.intPPI(200),-1),
                                    style=wx.CB_DROPDOWN|wx.TE_PROCESS_ENTER,
                                    value='', choices=self.replace_recent)
        self.find_next = wx.Button(self, wx.ID_ANY, label=_('Find &next'))
        self.find_previous = wx.Button(self, wx.ID_ANY, label=_('Find &previous'))
        self.replace_next = wx.Button(self, wx.ID_ANY, label=_('&Replace next'))
        self.replace_all = wx.Button(self, wx.ID_ANY, label=_('Replace &all'))
        id = wx.ID_CLOSE if wx.version() >= '2.9' else wx.ID_OK
        self.close = wx.Button(self, id, label=_('Close'))
        self.word_start = wx.CheckBox(self, wx.ID_ANY, label=_('Only on word s&tart'))
        self.whole_word = wx.CheckBox(self, wx.ID_ANY, label=_('Only &whole words'))
        self.only_selection = wx.CheckBox(self, wx.ID_ANY, label=_('Only in &selection'))
        self.dont_wrap = wx.CheckBox(self, wx.ID_ANY, label=_("&Don't wrap-around"))
        self.match_case = wx.CheckBox(self, wx.ID_ANY, label=_('&Case sensitive'))
        self.find_regexp = wx.CheckBox(self, wx.ID_ANY, label=_('Use regular e&xpressions'))
        re_url = HyperLinkCtrl(self, wx.ID_ANY, label='?',
                               URL=r'http://www.yellowbrain.com/stc/regexp.html')
        self.escape_sequences = wx.CheckBox(self, wx.ID_ANY, label=_('&Interpret escape sequences'))

        # Bind events
        def OnChar(event):
            key = event.GetKeyCode()
            if key == wx.WXK_TAB: # wx.TE_PROCESS_ENTER causes wx.EVT_CHAR to also process TAB
                panel.Navigate(flags = 0 if event.ShiftDown() else wx.NavigationKeyEvent.IsForward)
            else:
                event.Skip()
        self.replace_text_ctrl.Bind(wx.EVT_CHAR, OnChar)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnReplace, self.replace_text_ctrl)
        self.Bind(wx.EVT_BUTTON, self.OnFindNext, self.find_next)
        self.Bind(wx.EVT_BUTTON, self.OnFindPrevious, self.find_previous)
        self.Bind(wx.EVT_BUTTON, self.OnReplace, self.replace_next)
        self.Bind(wx.EVT_BUTTON, self.OnReplaceAll, self.replace_all)
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.close)

        # Organize controls
        check1_sizer = wx.BoxSizer(wx.VERTICAL)
        check1_sizer.Add(self.word_start, 0, wx.EXPAND|wx.RIGHT|wx.TOP|wx.BOTTOM, 4)
        check1_sizer.Add(self.whole_word, 0, wx.EXPAND|wx.RIGHT|wx.TOP|wx.BOTTOM, 4)
        check1_sizer.Add(self.only_selection, 0, wx.EXPAND|wx.RIGHT|wx.TOP|wx.BOTTOM, 4)
        check1_sizer.Add(self.dont_wrap, 0, wx.EXPAND|wx.RIGHT|wx.TOP|wx.BOTTOM, 4)
        check2_sizer = wx.BoxSizer(wx.VERTICAL)
        check2_sizer.Add(self.match_case, 0, wx.EXPAND|wx.ALL, 4)
        re_sizer = wx.BoxSizer(wx.HORIZONTAL)
        re_sizer.Add(self.find_regexp, 0)
        re_sizer.Add(re_url, wx.LEFT, 5)
        check2_sizer.Add(re_sizer, 0, wx.EXPAND|wx.ALL, 4)
        check2_sizer.Add(self.escape_sequences, 0, wx.EXPAND|wx.ALL, 4)
        check_sizer = wx.BoxSizer(wx.HORIZONTAL)
        check_sizer.Add(check1_sizer, 0)
        check_sizer.Add(check2_sizer, 0)
        ctrl_sizer = wx.BoxSizer(wx.VERTICAL)
        ctrl_sizer.Add(find_text, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 3)
        ctrl_sizer.Add(self.find_text_ctrl, 0, wx.EXPAND|wx.ALL, 3)
        ctrl_sizer.Add(replace_text, 0, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 3)
        ctrl_sizer.Add(self.replace_text_ctrl, 0, wx.EXPAND|wx.ALL, 3)
        ctrl_sizer.Add(check_sizer, 0, wx.EXPAND|wx.ALL, 3)
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer.Add(self.find_next, 0, wx.EXPAND|wx.ALL, 3)
        button_sizer.Add(self.find_previous, 0, wx.EXPAND|wx.ALL, 3)
        button_sizer.Add(self.replace_next, 0, wx.EXPAND|wx.ALL, 3)
        button_sizer.Add(self.replace_all, 0, wx.EXPAND|wx.ALL, 3)
        button_sizer.Add(self.close, 0, wx.EXPAND|wx.ALL, 3)
        col_sizer = wx.BoxSizer(wx.HORIZONTAL)
        col_sizer.Add(ctrl_sizer, 1, wx.EXPAND|wx.ALIGN_CENTER)
        col_sizer.Add(button_sizer, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.LEFT, 2)

        # Size the elements
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(col_sizer, 0, wx.EXPAND|wx.ALL, 5)
        dlgSizer.Fit(self)
        self.SetSizer(dlgSizer)
        dlgSizer.SetSizeHints(self)
        dlgSizer.Layout()
        self.find_next.SetDefault()
        self.find_text_ctrl.SetFocus()

    def GetFindText(self):
        return self.find_text_ctrl.GetValue()

    def GetReplaceText(self):
        return self.replace_text_ctrl.GetValue()

    def SetFindText(self, text):
        self.find_text_ctrl.SetValue(text)
        if self.IsShown():
            self.find_text_ctrl.SetFocus()
            self.find_text_ctrl.SetInsertionPointEnd()

    def SetReplaceText(self, text):
        self.replace_text_ctrl.SetValue(text)
        if self.IsShown():
            self.replace_text_ctrl.SetFocus()
            self.replace_text_ctrl.SetInsertionPointEnd()

    def UpdateText(self, text=None, ctrl='find'):
        if text is None:
            text = self.app.currentScript.GetSelectedText()
        if ctrl == 'find':
            self.SetFindText(text)
        else:
            self.SetReplaceText(text)

    def OnFindNext(self, event=None, range=None, update_list=True):
        text = self.GetFindText()
        if not text: return
        if update_list and text not in self.find_recent:
            self.find_recent[11:] = []
            self.find_recent.insert(0, text)
            self.find_text_ctrl.Insert(text, 0)
        if self.escape_sequences.IsChecked():
            text = self.Unescape(text)
        if self.Find(text, True, range):
            script = self.app.currentScript
            script.EnsureCaretVisible()

    def OnFindPrevious(self, event=None):
        text = self.GetFindText()
        if not text: return
        if text not in self.find_recent:
            self.find_recent[11:] = []
            self.find_recent.insert(0, text)
            self.find_text_ctrl.Insert(text, 0)
        if self.escape_sequences.IsChecked():
            text = self.Unescape(text)
        if self.Find(text, False):
            script = self.app.currentScript
            script.EnsureCaretVisible()

    def Find(self, text, top2bottom=True, range=None, wrap=None):
        script = self.app.currentScript
        stcflags = 0
        if self.match_case.IsChecked():
            stcflags = stcflags | stc.STC_FIND_MATCHCASE
        if self.word_start.IsChecked():
            stcflags = stcflags | stc.STC_FIND_WORDSTART
        if self.whole_word.IsChecked():
            stcflags = stcflags | stc.STC_FIND_WHOLEWORD
        if self.find_regexp.IsChecked():
            stcflags = stcflags | stc.STC_FIND_REGEXP
        if self.only_selection.IsChecked() and not range:
            range = script.GetSelection()
        if wrap is None:
            wrap = not self.dont_wrap.IsChecked()
        if not range:
            if top2bottom:
                minPos, maxPos = (script.GetSelectionEnd(),
                                  script.GetLineEndPosition(script.GetLineCount() - 1))
            else:
                minPos, maxPos = script.GetSelectionStart(), 0
        elif top2bottom:
            minPos, maxPos = range
        else:
            minPos, maxPos = reversed(range)
        findpos = script.FindText(minPos, maxPos, text, stcflags)
        if findpos == -1 and wrap:
            minPos = 0 if top2bottom else script.GetLineEndPosition(script.GetLineCount() - 1)
            findpos = script.FindText(minPos, maxPos, text, stcflags)
        if findpos == -1:
            script.app.GetStatusBar().SetStatusText(_('Cannot find "%(text)s"') % locals())
        else:
            script.app.GetStatusBar().SetStatusText('')
            script.SetAnchor(findpos)
            script.SetCurrentPos(findpos + len(text.encode('utf-8')))
        return findpos

    def OnReplace(self, event=None):
        find_text = self.GetFindText()
        replace_text = self.GetReplaceText()
        if not find_text or find_text == replace_text: return
        if find_text not in self.find_recent:
            self.find_recent[11:] = []
            self.find_recent.insert(0, find_text)
            self.find_text_ctrl.Insert(find_text, 0)
        if replace_text not in self.replace_recent:
            self.replace_recent[11:] = []
            self.replace_recent.insert(0, replace_text)
            self.replace_text_ctrl.Insert(replace_text, 0)
        if self.escape_sequences.IsChecked():
            find_text = self.Unescape(find_text)
            replace_text = self.Unescape(replace_text)
        script = self.app.currentScript
        script.GotoPos(script.GetSelectionStart())
        if self.Replace(find_text, replace_text):
            script.EnsureCaretVisible()

    def Replace(self, find_text, replace_text, range=None, wrap=True):
        script = self.app.currentScript
        if self.Find(find_text, True, range, wrap) != -1:
            script.ReplaceSelection(replace_text)
            return True

    def OnReplaceAll(self, event):
        find_text = self.GetFindText()
        replace_text = self.GetReplaceText()
        if not find_text or find_text == replace_text: return
        if find_text not in self.find_recent:
            self.find_recent[11:] = []
            self.find_recent.insert(0, find_text)
            self.find_text_ctrl.Insert(find_text, 0)
        if replace_text not in self.replace_recent:
            self.replace_recent[11:] = []
            self.replace_recent.insert(0, replace_text)
            self.replace_text_ctrl.Insert(replace_text, 0)
        if self.escape_sequences.IsChecked():
            find_text = self.Unescape(find_text)
            replace_text = self.Unescape(replace_text)
        offset = len(replace_text.encode('utf8')) - len(find_text.encode('utf8'))
        script = self.app.currentScript
        if self.only_selection.IsChecked():
            start, end = script.GetSelection()
        else:
            start, end = 0, script.GetLineEndPosition(script.GetLineCount() - 1)
        pos = script.GetCurrentPos()
        count = pos_count = 0
        script.BeginUndoAction()
        while True:
            if not self.Replace(find_text, replace_text, (start, end), False):
                break
            start = script.GetSelectionEnd()
            end += offset
            count += 1
            if script.GetSelectionEnd() < pos:
                pos_count += 1
        script.EndUndoAction()
        script.GotoPos(pos + offset * pos_count)
        self.app.GetStatusBar().SetStatusText(_('Replaced %(count)i times') % locals())

    def OnClose(self, event):
        self.Hide()

    @staticmethod
    def Unescape(text):
        """Unescape backslashes on a Unicode string"""
        return text.encode('utf8').decode('string-escape').decode('utf8')


class TextCtrl(wx.TextCtrl):
    """wx.TextCtrl with Ctrl-A also on multiline"""
    def __init__(self, *args, **kwargs):
        wx.TextCtrl.__init__(self, *args, **kwargs)
        if self.IsMultiLine():
            self.Bind(wx.EVT_CHAR, self.OnChar)

    def OnChar(self, event):
        key = event.GetKeyCode()
        if key == 1: # wx.WXK_CONTROL_A in wxPython 2.9
            self.SelectAll()
        else:
            event.Skip()


class FloatSpin2(FloatSpin):
    """FloatSpin without some annoyances

    - Select all on TAB or Ctrl+A
    - Process RETURN normally

    wx.TE_NOHIDESEL effect still present though
    """

    def __init__(self, *args, **kwargs):
        FloatSpin.__init__(self, *args, **kwargs)
        self._validkeycode.append(1) # available on wxPython 2.9 as wx.WXK_CONTROL_A

    def OnFocus(self, event):
        FloatSpin.OnFocus(self, event)
        if self._textctrl:
           self._textctrl.SelectAll()

    def OnTextEnter(self, event): # bypass wx.TE_PROCESS_ENTER
        self.SyncSpinToText() # wx.EVT_TEXT_ENTER action without event.Skip()
        top_level = self.GetTopLevelParent()
        default_item = top_level.GetDefaultItem()
        if default_item is not None:
            default_event = wx.PyCommandEvent(wx.EVT_BUTTON.typeId, default_item.GetId())
            wx.PostEvent(top_level, default_event)


class ColourSelect(colourselect.ColourSelect):
    """Subclass of ColourSelect accepting a ColourData instance

    This allows using and changing custom colours

    All in all is still better than wx.ColourPickerCtrl
    """

    def __init__(self, *args, **kwargs):
        self.colour_data = kwargs.pop('colour_data', None)
        colourselect.ColourSelect.__init__(self, *args, **kwargs)

    def OnClick(self, event):
        data = self.colour_data or wx.ColourData()
        data.SetChooseFull(True)
        data.SetColour(self.colour)
        dlg = wx.ColourDialog(wx.GetTopLevelParent(self), data)

        changed = dlg.ShowModal() == wx.ID_OK

        if changed:
            data = dlg.GetColourData()
            self.SetColour(data.GetColour())
            if self.colour_data is not None:
                for i in range(self.colour_data.NUM_CUSTOM):
                    self.colour_data.SetCustomColour(i, data.GetCustomColour(i))
        dlg.Destroy()

        # moved after dlg.Destroy, since who knows what the callback will do...
        if changed:
            self.OnChange()


if hasattr(wx.ColourData, 'FromString'):
    ColourData = wx.ColourData
else:
    class ColourData(wx.ColourData):
        """Backport of ToString and FromString methods"""
        NUM_CUSTOM = 16

        def ToString(self):
            colour_data_str = str(int(self.GetChooseFull()))
            for i in range(self.NUM_CUSTOM):
                colour_data_str += ','
                colour = self.GetCustomColour(i)
                if colour.IsOk():
                    colour_data_str += colour.GetAsString(wx.C2S_HTML_SYNTAX)
            return colour_data_str

        def FromString(self, colour_data_str):
            colour_data = colour_data_str.split(',')
            if colour_data[0] not in ('0', '1'):
                return False
            self.SetChooseFull(colour_data[0] == '1')
            for i, colour in enumerate(colour_data[1:self.NUM_CUSTOM + 1]):
                try:
                    self.SetCustomColour(i, colour or wx.Colour())
                except:
                    return False


class OptionsDialog(wx.Dialog):
    def __init__(self, parent, dlgInfo, options, title=None, startPageIndex=0,
                starText=True, invert_scroll=False, dlgsize=None, canResize=True):
        '''Init the OptionsDialog window

        Create a wx.Notebook from the tabs specified in 'dlgInfo' and the
        current/default values in 'options'. If there's only one tab, create
        a simple wx.Panel.

        'starText': show a message next to the window's standard buttons if
        some condition is satisfied. 'startext' == True imposes a min window
        width.

        '''
        if title is None:
            title = _('Program Settings')
        if canResize:
            wx.Dialog.__init__(self, parent, wx.ID_ANY, title, style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.NO_FULL_REPAINT_ON_RESIZE)
        else:
            wx.Dialog.__init__(self, parent, wx.ID_ANY, title, style=wx.DEFAULT_DIALOG_STYLE|wx.NO_FULL_REPAINT_ON_RESIZE)

        dpi.SetFontPPI(self)
        self.options = options.copy()
        self.optionsOriginal = options
        # Create the options tabs
        self.controls = {}
        self.starList = []
        notebook = len(dlgInfo) > 1
        if notebook:
            style = wx.NO_BORDER
            #style |= wx.NB_MULTILINE
            nb = self.nb = Notebook(self, wx.ID_ANY, style=style,
                                    invert_scroll=invert_scroll)
        else:
            self.nb = None
        for tabInfo in dlgInfo:
            if notebook:
                tabPanel = wx.Panel(nb, wx.ID_ANY)
                nb.AddPage(tabPanel, tabInfo[0], select=True)
            else:
                tabPanel = wx.Panel(self, wx.ID_ANY)
            #tabPanel.SetDoubleBuffered(True) #buggy
            tabSizer = wx.BoxSizer(wx.VERTICAL)
            tabSizer.Add((-1,dpi.intPPI(5)), 0)
            boolStar = False
            for line in tabInfo[1:]:
                colSizer = wx.BoxSizer(wx.HORIZONTAL)
                for label, flag, key, tip, misc in line:
                    try:
                        optionsValue = self.options[key]
                        if optionsValue is None:
                            optionsValue = ''
                    except KeyError:
                        optionsValue = ''

                    # Set the controls
                    # possible values for 'label_position' and 'orientation' parameters: wx.HORIZONTAL, wx.VERTICAL

                    if flag is None:
                        # horizontal blank space separator
                        # misc: {height}
                        height = misc['height'] if 'height' in misc else dpi.intPPI(10)
                        itemSizer = wx.BoxSizer(wx.VERTICAL)
                        itemSizer.Add((-1,height), 0)

                    elif flag == OPT_ELEM_SEP:
                        # horizontal separator formed by a text line and a horizontal line
                        # misc: {width, adjust_width, expand}
                        width = misc['width'] if 'width' in misc else -1
                        adjust_width = misc['adjust_width'] if 'adjust_width' in misc else False
                        if width != -1 or adjust_width:
                            expand = 0
                        else:
                            expand = (wx.EXPAND if misc['expand'] else 0) if 'expand' in misc else wx.EXPAND
                        itemSizer = wx.BoxSizer(wx.VERTICAL)
                        if label:
                            staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                            if tip:
                                staticText.SetToolTipString(tip)
                            if adjust_width:
                                width = staticText.GetTextExtent(label)[0] + dpi.intPPI(4)
                            itemSizer.Add(staticText, 0, wx.EXPAND|wx.ALL, dpi.intPPI(2))
                        else:
                            itemSizer.AddSpacer((-1, 3))
                        staticLine = wx.StaticLine(tabPanel, wx.ID_ANY, size=(width, -1))
                        margin = 0 if not width and not expand else dpi.intPPI(2)
                        itemSizer.Add(staticLine, 0, expand|wx.TOP|wx.BOTTOM, margin)

                    elif flag == OPT_ELEM_CHECK:
                        # simple check box, with the label on the right
                        # misc: {width, ident}
                        width = misc['width'] if 'width' in misc else -1
                        ctrl = wx.CheckBox(tabPanel, wx.ID_ANY, label, size=(width,-1))
                        ctrl.SetMinSize(ctrl.GetBestSize())
                        ctrl.SetValue(bool(optionsValue))
                        if 'handler' in misc:
                            handler = misc['handler']
                            self.Bind(wx.EVT_CHECKBOX, handler, ctrl)
                        if tip:
                            ctrl.SetToolTipString(tip)
                        itemSizer = wx.BoxSizer(wx.VERTICAL)
                        if 'ident' in misc:
                            identSizer = wx.BoxSizer(wx.HORIZONTAL)
                            identSizer.Add((misc['ident'], -1), 0)
                            identSizer.Add(ctrl, 1, wx.TOP|wx.BOTTOM, dpi.intPPI(1))
                            itemSizer.AddStretchSpacer()
                            itemSizer.Add(identSizer, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL)
                        else:
                            itemSizer.Add((-1,2), 1, wx.EXPAND)
                            itemSizer.Add(ctrl, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))

                    elif flag in (OPT_ELEM_SPIN, OPT_ELEM_INT, OPT_ELEM_FLOAT):
                        # numeric field, with arrows to increment and decrement the value
                        # misc: (width, expand, label_position, min_val, max_val, digits, increment)
                        width = misc['width'] if 'width' in misc else dpi.intPPI(50)
                        expand = misc['expand'] if 'expand' in misc else False
                        label_position = misc['label_position'] if 'label_position' in misc else wx.HORIZONTAL
                        min_val = misc['min_val'] if 'min_val' in misc else None
                        max_val = misc['max_val'] if 'max_val' in misc else None
                        digits = misc['digits'] if 'digits' in misc else 0
                        increment = misc['increment'] if 'increment' in misc else 1
                        ctrl = FloatSpin2(tabPanel, wx.ID_ANY, size=(width, -1),
                                    min_val=min_val, max_val=max_val,
                                    value=optionsValue, digits=digits, increment=increment)
                        itemSizer = wx.BoxSizer(label_position)
                        staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                        if tip:
                            staticText.SetToolTipString(tip)
                            ctrl._textctrl.SetToolTipString(tip)
                        if label_position == wx.HORIZONTAL:
                            itemSizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(6))
                            expand_flags = (1, 0) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                        else:
                            itemSizer.AddStretchSpacer()
                            itemSizer.Add(staticText, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            expand_flags = (0, wx.EXPAND) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            itemSizer.AddStretchSpacer()

                    elif flag == OPT_ELEM_SLIDER:
                        # select a number with a draggable handle
                        # misc: (width, expand, label_position, orientation, minValue, maxValue, TickFreq)
                        width = misc['width'] if 'width' in misc else dpi.intPPI(200)
                        expand = misc['expand'] if 'expand' in misc else False
                        label_position = misc['label_position'] if 'label_position' in misc else wx.HORIZONTAL
                        orientation = misc['orientation'] if 'orientation' in misc else wx.HORIZONTAL
                        minValue = misc['minValue'] if 'minValue' in misc else 0
                        maxValue = misc['maxValue'] if 'maxValue' in misc else 100
                        TickFreq = misc['TickFreq'] if 'TickFreq' in misc else 50
                        size = (width, -1) if orientation == wx.HORIZONTAL else (-1, width)
                        style = wx.SL_LABELS | orientation
                        if TickFreq: style |= wx.SL_AUTOTICKS
                        ctrl = wx.Slider(tabPanel, wx.ID_ANY, size=size,
                                    minValue=minValue, maxValue=maxValue,
                                    value=optionsValue, style=style)
                        ctrl.SetTickFreq(TickFreq)
                        staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                        if tip:
                            staticText.SetToolTipString(tip)
                            ctrl.SetToolTipString(tip)
                        itemSizer = wx.BoxSizer(label_position)
                        if label_position == wx.HORIZONTAL:
                            itemSizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(5))
                            expand_flags = (1, 0) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL)
                        else:
                            itemSizer.AddStretchSpacer()
                            itemSizer.Add(staticText, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            expand_flags = (0, wx.EXPAND) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL)
                            itemSizer.AddStretchSpacer()

                    elif flag in (OPT_ELEM_FILE, OPT_ELEM_FILE_OPEN, OPT_ELEM_FILE_SAVE, OPT_ELEM_FILE_URL):
                        # text field with additional browse for file button
                        # misc: {width, expand, label_position, fileMask, startDirectory, buttonText, buttonWidth}
                        width = misc['width'] if 'width' in misc else dpi.intPPI(400)
                        expand = misc['expand'] if 'expand' in misc else True
                        label_position = misc['label_position'] if 'label_position' in misc else wx.HORIZONTAL
                        fileMode = wx.SAVE|wx.OVERWRITE_PROMPT if flag == OPT_ELEM_FILE_SAVE else wx.OPEN|wx.FILE_MUST_EXIST
                        fileMask = misc['fileMask'] if 'fileMask' in misc else '*.*'
                        startDirectory = (self.GetParent().ExpandVars(misc['startDirectory']) if misc.get('startDirectory')
                                          else os.path.dirname(self.GetParent().ExpandVars(optionsValue)))
                        buttonText = misc['buttonText'] if 'buttonText' in misc else _('Browse')
                        buttonWidth = misc['buttonWidth'] if 'buttonWidth' in misc else -1
                        itemSizer = wx.BoxSizer(wx.VERTICAL)
                        itemSizer.AddStretchSpacer()
                        Label = label
                        if label and label_position == wx.VERTICAL:
                            staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                            staticText.SetToolTipString(tip)
                            itemSizer.Add(staticText, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            label = ''
                        ctrl = filebrowse.FileBrowseButton(tabPanel, wx.ID_ANY, size=(width,-1),
                            labelText=label,
                            toolTip=tip,
                            fileMode=fileMode,
                            fileMask=fileMask,
                            startDirectory=startDirectory,
                            buttonText=buttonText,
                            #dialogTitle = ''
                        )
                        ctrl.SetValue(optionsValue)
                        ctrl.Sizer.Children[0].SetBorder(0)
                        if not label:
                            ctrl.Sizer.Children[0].Sizer.Children[1].SetBorder(0)
                        elif tip:
                            ctrl.label.SetToolTipString(tip)
                        ctrl.Sizer.Children[0].Sizer.Children[2].SetInitSize(buttonWidth, -1)
                        ctrl.Label = Label
                        itemSizer.Add(ctrl, 0, (wx.EXPAND if expand else 0)|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                        itemSizer.AddStretchSpacer()

                    elif flag in (OPT_ELEM_DIR, OPT_ELEM_DIR_URL):
                        # text field with additional browse for directory button
                        # misc: (width, expand, label_position, startDirectory, buttonText, buttonWidth)
                        width = misc['width'] if 'width' in misc else dpi.intPPI(400)
                        expand = misc['expand'] if 'expand' in misc else True
                        label_position = misc['label_position'] if 'label_position' in misc else wx.HORIZONTAL
                        startDirectory = (self.GetParent().ExpandVars(misc['startDirectory']) if misc.get('startDirectory')
                                          else self.GetParent().ExpandVars(optionsValue))
                        buttonText = misc['buttonText'] if 'buttonText' in misc else _('Browse')
                        buttonWidth = misc['buttonWidth'] if 'buttonWidth' in misc else -1
                        itemSizer = wx.BoxSizer(wx.VERTICAL)
                        itemSizer.AddStretchSpacer()
                        Label = label
                        if label and label_position == wx.VERTICAL:
                                staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                                staticText.SetToolTipString(tip)
                                itemSizer.Add(staticText, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                                label = ''
                        ctrl = filebrowse.DirBrowseButton(tabPanel, wx.ID_ANY, size=(width,-1),
                            labelText=label,
                            toolTip=tip,
                            startDirectory=startDirectory,
                            newDirectory=True,
                            buttonText=buttonText,
                            #dialogTitle = ''
                        )
                        ctrl.SetValue(optionsValue)
                        ctrl.Sizer.Children[0].SetBorder(0)
                        if not label:
                            ctrl.Sizer.Children[0].Sizer.Children[1].SetBorder(0)
                        elif tip:
                            ctrl.label.SetToolTipString(tip)
                        ctrl.Sizer.Children[0].Sizer.Children[2].SetInitSize(buttonWidth, -1)
                        ctrl.Label = Label
                        itemSizer.Add(ctrl, 0, (wx.EXPAND if expand else 0)|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                        itemSizer.AddStretchSpacer()

                    elif flag == OPT_ELEM_RADIO:
                        # select an option from the displayed ones
                        # misc: {width, expand, orientation, dimensions, choices}
                        width = misc['width'] if 'width' in misc else -1
                        expand = 1 if 'expand' in misc and misc['expand'] else 0
                        orientation = (wx.RA_SPECIFY_COLS if 'orientation' in misc and
                                       misc['orientation'] == wx.VERTICAL else wx.RA_SPECIFY_ROWS)
                        dimensions = misc['dimensions'] if 'dimensions' in misc else 1
                        choices = [s for s,v in misc['choices']]
                        ctrl = wx.RadioBox(tabPanel, wx.ID_ANY, size=(width,-1), label=label,
                                           choices=choices, style=orientation, majorDimension=dimensions)
                        ctrl.items = misc['choices']
                        ctrl.SetSelection(0)
                        for s, v in misc['choices']:
                            if v == optionsValue:
                                ctrl.SetStringSelection(s)
                                break
                        if tip:
                            ctrl.SetToolTipString(tip)
                        itemSizer = wx.BoxSizer(wx.HORIZONTAL)
                        itemSizer.Add(ctrl, expand, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))

                    elif flag == OPT_ELEM_LIST:
                        # select an option from a drop-down list
                        # misc: {width, expand, label_position, choices, writable}
                        width = misc['width'] if 'width' in misc else -1
                        expand = misc['expand'] if 'expand' in misc else False
                        label_position = misc['label_position'] if 'label_position' in misc else wx.HORIZONTAL
                        list_type = wx.CB_DROPDOWN if 'writable' in misc and misc['writable'] else wx.CB_READONLY
                        if misc['choices'] and not isinstance(misc['choices'][0], basestring):
                            ctrl = wx.ComboBox(tabPanel, wx.ID_ANY, size=(width,-1), style=wx.CB_READONLY)
                            ctrl.client_data = True # not ctrl.HasClientData() in wxWidgets 2.8
                            for display_string, client_data in misc['choices']:
                                ctrl.Append(display_string, client_data)
                                if client_data == optionsValue:
                                    ctrl.SetValue(display_string)
                        else:
                            ctrl = wx.ComboBox(tabPanel, wx.ID_ANY, size=(width,-1), choices=misc['choices'],
                                               value=optionsValue, style=list_type)
                            ctrl.client_data = False
                        itemSizer = wx.BoxSizer(label_position)
                        staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                        if tip:
                            staticText.SetToolTipString(tip)
                            ctrl.SetToolTipString(tip)
                        if label_position == wx.HORIZONTAL:
                            itemSizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(5))
                            expand_flags = (1, 0) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                        else:
                            itemSizer.AddStretchSpacer()
                            itemSizer.Add(staticText, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            expand_flags = (0, wx.EXPAND) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            itemSizer.AddStretchSpacer()

                    elif flag == OPT_ELEM_BUTTON:
                        # button with an associated handler
                        # misc: {width, handler}
                        width = misc['width'] if 'width' in misc else -1
                        handler = misc['handler']
                        ctrl = wx.Button(tabPanel, wx.ID_ANY, size=(width,-1), label=label)
                        self.Bind(wx.EVT_BUTTON, handler, ctrl)
                        if tip:
                            ctrl.SetToolTipString(tip)
                        itemSizer = wx.BoxSizer(wx.VERTICAL)
                        #~ staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                        #~ ctrl = wxButtons.GenButton(tabPanel, wx.ID_ANY, label=label)
                        #~ ctrl.SetUseFocusIndicator(False)
                        #~ itemSizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5)
                        itemSizer.Add(ctrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))

                    elif flag == OPT_ELEM_COLOR:
                        # button for selecting a color
                        # misc: {width, colour_data}
                        width = misc['width'] if 'width' in misc else -1
                        colour_data = misc.get('colour_data')
                        colour = wx.Colour(*optionsValue)
                        staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                        ctrl = ColourSelect(tabPanel, wx.ID_ANY, colour=colour,
                                            size=(width, -1), colour_data=colour_data)
                        if tip:
                            staticText.SetToolTipString(tip)
                            ctrl.SetToolTipString(tip)
                        itemSizer = wx.BoxSizer(wx.HORIZONTAL)
                        itemSizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(6))
                        itemSizer.Add(ctrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))

                    elif flag == OPT_ELEM_FONT:
                        # button for choosing font
                        # misc: {width}
                        width = misc['width'] if 'width' in misc else -1
                        staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                        if optionsValue is not None:
                            (fontFace, fontSize, fontWeight, fontStyle,
                                fontColorTuple) = optionsValue
                            weight = wx.FONTWEIGHT_NORMAL
                            if fontWeight == 'bold':
                                weight = wx.FONTWEIGHT_BOLD
                            style = wx.FONTSTYLE_NORMAL
                            if fontStyle == 'italic':
                                style = wx.FONTSTYLE_ITALIC
                            font = wx.Font(fontSize, wx.FONTFAMILY_DEFAULT,
                                           style, weight, faceName=fontFace)
                        else:
                            font = wx.NullFont
                        ctrl = wx.FontPickerCtrl(tabPanel, wx.ID_ANY, font,
                                                 size=(width,-1), name=label,
                                                 style=wx.FNTP_FONTDESC_AS_LABEL)
                        if tip:
                            staticText.SetToolTipString(tip)
                            ctrl.SetToolTipString(tip)
                        itemSizer = wx.BoxSizer(wx.HORIZONTAL)
                        itemSizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(6))
                        itemSizer.Add(ctrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM, dpi.intPPI(2))

                    else: #elif flag == OPT_ELEM_STRING:
                        # regular text field
                        # misc: {width, expand, label_position}
                        width = misc['width'] if 'width' in misc else -1
                        expand = misc['expand'] if 'expand' in misc else True
                        label_position = misc['label_position'] if 'label_position' in misc else wx.HORIZONTAL
                        staticText = wx.StaticText(tabPanel, wx.ID_ANY, label)
                        ctrl = wx.TextCtrl(tabPanel, wx.ID_ANY, size=(width,-1), value=optionsValue)
                        if tip:
                            staticText.SetToolTipString(tip)
                            ctrl.SetToolTipString(tip)
                        itemSizer = wx.BoxSizer(label_position)
                        if label_position == wx.HORIZONTAL:
                            itemSizer.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(5))
                            expand_flags = (1, 0) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                        else:
                            itemSizer.AddStretchSpacer()
                            itemSizer.Add(staticText, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            expand_flags = (0, wx.EXPAND) if expand else (0, 0)
                            itemSizer.Add(ctrl, expand_flags[0], expand_flags[1]|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(2))
                            itemSizer.AddStretchSpacer()

                    if label.rstrip(' :').endswith('*'):
                        boolStar = True
                    if flag != OPT_ELEM_SEP: self.controls[key] = (ctrl, flag, nb.GetSelection() if notebook else -1)
                    colSizer.Add(itemSizer, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, dpi.intPPI(4))
                tabSizer.Add(colSizer, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, dpi.intPPI(4))
            if boolStar:
                self.starList.append(tabPanel if notebook else 1)
                #~ tabSizer.Add((0,0),1)
                #~ tabSizer.Add(wx.StaticText(tabPanel, wx.ID_ANY, '    '+_('* Requires program restart for full effect')), 0, wx.TOP, 20)
            tabSizerBorder = wx.BoxSizer(wx.VERTICAL)
            tabSizerBorder.Add(tabSizer, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, dpi.intPPI(4))
            tabSizerBorder.Add((-1,4), 0, wx.EXPAND)
            tabPanel.SetSizer(tabSizerBorder)
            tabSizerBorder.Layout()
        if notebook:
            if startPageIndex >=0 and startPageIndex < nb.GetPageCount():
                nb.SetSelection(startPageIndex)
            else:
                nb.SetSelection(0)
        # Standard buttons
        okay = wx.Button(self, wx.ID_OK, _('OK'))
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, okay)
        cancel = wx.Button(self, wx.ID_CANCEL, _('Cancel'))
        btns = wx.StdDialogButtonSizer()
        self.starText = None # GPo disable the static text
        if starText:
            #~self.starText = wx.StaticText(self, wx.ID_ANY, _('* Requires program restart for full effect'))
            #~btns.Add(self.starText, 0, wx.ALIGN_CENTER_VERTICAL)
            # GPo 2020
            ctrl = wx.CheckBox(self, wx.ID_ANY, _('* Requires program restart for full effect'), size=(-1,-1))
            self.Bind(wx.EVT_CHECKBOX, self.OnCheckBoxRestart, ctrl)
            ctrl.SetMinSize(ctrl.GetBestSize())
            btns.Add(ctrl, 0, wx.ALIGN_CENTER_VERTICAL)

        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Size the elements
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        if notebook:
            dlgSizer.Add(nb, 0, wx.EXPAND|wx.ALL, dpi.intPPI(5))
        else:
            dlgSizer.Add(tabPanel, 0, wx.EXPAND|wx.ALL, 0)
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, dpi.intPPI(10))
        dlgSizer.Fit(self)
        self.SetSizer(dlgSizer)
        dlgSizer.SetSizeHints(self)
        dlgSizer.Layout()
        if dlgsize:
            dlgsize = (dlgsize[0], self.GetSize()[1]) # set only the width
            self.SetSize(dlgsize)
        if canResize:
            self.Center()
        else:
            self.CenterOnParent()
        # Misc
        okay.SetDefault()
        if starText and self.starText is not None:
            if (notebook and self.nb.GetPage(0) not in self.starList) or (not notebook and not self.starList):
                self.starText.Hide()
            if notebook: self.nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNotebookPageChanged)

    def OnNotebookPageChanged(self, event):
        if self.starText is not None: # GPo 2020
            if self.nb.GetPage(event.GetSelection()) in self.starList:
                self.starText.Show()
            else:
                self.starText.Hide()
        event.Skip()

    def OnButtonOK(self, event):
        if self.UpdateDict():
            event.Skip()

    def OnCheckBoxRestart(self, event): # GPo 2020, 2=restart
        self.options['exitstatus'] = 2 if event.IsChecked() else 1

    def OnButtonFont(self, event):
        button = event.GetEventObject()
        font = button.GetFont()
        colour = button.GetForegroundColour()
        # Show the font dialog
        data = wx.FontData()
        data.EnableEffects(False)
        #~ data.SetColour(button.GetForegroundColour())
        data.SetInitialFont(font)
        dlg = wx.FontDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetFontData()
            font = data.GetChosenFont()
        # Show the color dialog
        data = wx.ColourData()
        data.SetColour(colour)
        dlg2 = wx.ColourDialog(self, data)
        dlg2.GetColourData().SetChooseFull(True)
        if dlg2.ShowModal() == wx.ID_OK:
            data = dlg2.GetColourData()
            colour = data.GetColour()
        button.SetFont(font)
        button.SetForegroundColour(colour)
        button.SetBestSize()
        button.Refresh()
        self.GetSizer().Fit(self)
        dlg2.Destroy()
        dlg.Destroy()

    def GetDict(self):
        return self.options

    def UpdateDict(self):
        for key, value in self.controls.items():
            if not key: # GPo, 2022 needed for show sub options dialog eg. DPI settings
                continue
            ctrl, flag, tabIndex = value
            if flag in (OPT_ELEM_DIR, OPT_ELEM_DIR_URL):
                entry = self.GetParent().ExpandVars(ctrl.GetValue())
                if entry == '' or os.path.isdir(entry):
                    newValue = entry
                elif flag == OPT_ELEM_DIR_URL and entry.lstrip().startswith('http://'):
                    newValue = entry
                else:
                    label = u'\n\n{0}{1}'.format(ctrl.Label.rstrip(':') + ': ' if ctrl.Label else '', entry)
                    self.ShowWarning(ctrl, _('Invalid directory!') + label, tabIndex)
                    return False
            elif flag in (OPT_ELEM_FILE, OPT_ELEM_FILE_OPEN, OPT_ELEM_FILE_SAVE, OPT_ELEM_FILE_URL):
                entry = self.GetParent().ExpandVars(ctrl.GetValue())
                if entry == '' or os.path.isfile(entry) or flag == OPT_ELEM_FILE_SAVE or (
                   flag == OPT_ELEM_FILE_URL and entry.lstrip().startswith('http://')):
                    newValue = entry
                else:
                    label = u'\n\n{0}{1}'.format(ctrl.Label.rstrip(':') + ': ' if ctrl.Label else '', entry)
                    self.ShowWarning(ctrl, _('Invalid filename!') + label, tabIndex)
                    return False
            elif flag == OPT_ELEM_COLOR:
                #~ newValue = ctrl.GetBackgroundColour().Get()
                newValue = ctrl.GetColour().Get()
            elif flag == OPT_ELEM_FONT:
                font = ctrl.GetSelectedFont() # ctrl.GetFont()
                bold = ''
                if font.GetWeight() == wx.FONTWEIGHT_BOLD:
                    bold = 'bold'
                italic = ''
                if font.GetStyle() == wx.FONTSTYLE_ITALIC:
                    italic = 'italic'
                color = ctrl.GetChildren()[0].GetForegroundColour() # ctrl.GetForegroundColour()
                newValue = (font.GetFaceName(), font.GetPointSize(), bold, italic, color.Get())
            elif flag == OPT_ELEM_CHECK:
                newValue = ctrl.GetValue()
            elif flag in (OPT_ELEM_INT, OPT_ELEM_FLOAT, OPT_ELEM_SPIN):
                newValue = ctrl.GetValue() if ctrl.GetDigits() else int(ctrl.GetValue())
            elif flag == OPT_ELEM_SLIDER:
                newValue = ctrl.GetValue()
            elif flag == OPT_ELEM_RADIO:
                index = ctrl.GetSelection()
                newValue = ctrl.items[index][1]
            elif flag == OPT_ELEM_LIST:
                try:  # GPo try if component changed to list and options name the same, select index 0
                    if ctrl.client_data: # ctrl.HasClientData() in wxWidgets 2.9+
                        newValue = ctrl.GetClientData(ctrl.GetSelection())
                    else:
                        newValue = ctrl.GetValue()
                except:
                    ctrl.SetSelection(0)
                    if ctrl.client_data: # ctrl.HasClientData() in wxWidgets 2.9+
                        newValue = ctrl.GetClientData(ctrl.GetSelection())
                    else:
                        newValue = ctrl.GetValue()
            elif flag == OPT_ELEM_BUTTON:
                newValue = self.optionsOriginal[key]
            else: # flag == OPT_ELEM_STRING:
                newValue = ctrl.GetValue()
            self.options[key] = newValue
        return True

    def ShowWarning(self, ctrl, message, tabIndex):
        if tabIndex != -1: self.nb.SetSelection(tabIndex)
        color = ctrl.textControl.GetBackgroundColour()
        ctrl.textControl.SetBackgroundColour('pink')
        ctrl.Refresh()
        wx.MessageBox(message, 'Error')
        ctrl.textControl.SetBackgroundColour(color)
        ctrl.Refresh()
        ctrl.SetFocus()

    def GetPageIndex(self):
        return self.nb.GetSelection() if self.nb else 0

class ShortcutsDialog(wx.Dialog):
    def __init__(self, parent, shortcutList, title=None, exceptionIds=None, submessage=None):
        if title is None:
            title = _('Edit shortcuts')
        wx.Dialog.__init__(self, parent, wx.ID_ANY, title, style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
        dpi.SetFontPPI(self)
        self.parent = parent
        self.shortcutList = copy.deepcopy(shortcutList)#shortcutList[:]
        if exceptionIds is None:
            exceptionIds = []
        if type(exceptionIds) is tuple:
            exceptionShortcuts = exceptionIds[0]
            self.advancedShortcuts = advancedShortcuts = exceptionIds[1]
            self.reservedShortcuts = reservedShortcuts = exceptionIds[2][:]
            self.advancedInfo = exceptionIds[3]
            advanced = wx.Button(self, wx.ID_ANY, _('Advanced'))
            advanced.Bind(wx.EVT_BUTTON, self.OnAdvancedButton)
        else:
            advanced = None
        # Define the shortcut editing modal dialog (used later)
        #~ self.dlgEdit = self.defineShortcutEditDialog()
        # Define the virtual list control
        class VListCtrl(ListCtrl):
            def OnGetItemText(self, item, column):
                label, shortcut, id = self.parent.shortcutList[item]
                if column == 0:
                    if advanced:
                        if shortcut in exceptionShortcuts:
                            label = '* %s' % label
                        elif shortcut in reservedShortcuts:
                            if (label, shortcut) in advancedShortcuts[-1]:
                                label = '~ %s' % label
                            else:
                                label = '* %s' % label
                    elif id in exceptionIds:
                        label = '* %s' % label
                    return label
                elif column == 1:
                    return GetTranslatedShortcut(shortcut)
                #~ return self.parent.shortcutList[item][column]
        listCtrl = VListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VIRTUAL|wx.LC_HRULES|wx.LC_VRULES)
        listCtrl.InsertColumn(0, _('Menu label'))
        listCtrl.InsertColumn(1, _('Keyboard shortcut'))
        nItems = len(self.shortcutList)
        listCtrl.SetItemCount(nItems)
        listCtrl.setResizeColumn(1)
        listCtrl.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        listCtrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnListCtrlActivated)
        self.listCtrl = listCtrl
        # Standard buttons
        okay  = wx.Button(self, wx.ID_OK, _('OK'))
        #~ self.Bind(wx.EVT_BUTTON, self.OnButtonClick, okay)
        cancel = wx.Button(self, wx.ID_CANCEL, _('Cancel'))
        #~ self.Bind(wx.EVT_BUTTON, self.OnButtonClick, cancel)
        btns = wx.StdDialogButtonSizer()
        if advanced:
            btns.Add(advanced)
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Size the elements
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(listCtrl, 1, wx.EXPAND|wx.ALL, dpi.intPPI(5))
        if submessage is not None:
            dlgSizer.Add(wx.StaticText(self, wx.ID_ANY, submessage), 0, wx.ALIGN_LEFT|wx.LEFT|wx.BOTTOM, dpi.intPPI(10))
        message = _('Double-click or hit enter on an item in the list to edit the shortcut.')
        dlgSizer.Add(wx.StaticText(self, wx.ID_ANY, message), 0, wx.ALIGN_CENTER|wx.ALL, dpi.intPPI(5))
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, dpi.intPPI(10))
        self.SetSizerAndFit(dlgSizer)
        width, height = self.GetSize()
        self.SetSize((width, height*2))
        self.sizer = dlgSizer
        # Misc
        #okay.SetDefault()

    def OnAdvancedButton(self, event):
        dlg = wx.Dialog(self, wx.ID_ANY, _('Advanced'), style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
        dpi.SetFontPPI(dlg)
        class CheckListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin):
            def __init__(self, parent):
                wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
                listmix.CheckListCtrlMixin.__init__(self, checked_icon.GetBitmap(), unchecked_icon.GetBitmap())
        checklist = CheckListCtrl(dlg)
        checklist.InsertColumn(0, _('Shortcut'))
        checklist.InsertColumn(1, _('Action'))
        for index in range(0, len(self.advancedShortcuts)-1):
            shortcut, action = self.advancedShortcuts[index]
            checklist.InsertStringItem(index, shortcut)
            checklist.SetStringItem(index, 1, action)
            if index % 2:
                checklist.SetItemBackgroundColour(index, '#E8E8FF')
            if shortcut in self.reservedShortcuts:
                checklist.CheckItem(index)
        checklist.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        checklist.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        # Standard buttons
        okay  = wx.Button(dlg, wx.ID_OK, _('OK'))
        cancel = wx.Button(dlg, wx.ID_CANCEL, _('Cancel'))
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Dialog layout
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(checklist, 1, wx.EXPAND|wx.ALL, dpi.intPPI(5))
        if self.advancedInfo:
            dlgSizer.Add(wx.StaticText(dlg, wx.ID_ANY, self.advancedInfo), 0, wx.LEFT|wx.BOTTOM, dpi.intPPI(10))
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, dpi.intPPI(10))
        dlg.SetSizerAndFit(dlgSizer)
        width = checklist.GetColumnWidth(0) + checklist.GetColumnWidth(1) + dpi.intPPI(40)
        dlg.SetSize((width, width*3/4))
        if wx.ID_OK == dlg.ShowModal():
            while self.reservedShortcuts:
                self.reservedShortcuts.pop()
            for index in range(0, len(self.advancedShortcuts)-1):
                if checklist.IsChecked(index):
                    self.reservedShortcuts.append(self.advancedShortcuts[index][0])
            self.listCtrl.RefreshItems(0, len(self.shortcutList)-1)
        dlg.Destroy()

    def GetShortcutList(self):
        return self.shortcutList, self.reservedShortcuts

    def defineShortcutEditDialog(self):
        dlg = wx.Dialog(self, wx.ID_ANY, _('Edit the keyboard shortcut'))
        dpi.SetFontPPI(dlg)
        # Menu string label
        dlg.menuLabel = wx.StaticText(dlg, wx.ID_ANY, '')
        # Main controls
        dlg.checkBoxCtrl = wx.CheckBox(dlg, wx.ID_ANY, _('Ctrl'))
        dlg.checkBoxAlt = wx.CheckBox(dlg, wx.ID_ANY, _('Alt'))
        dlg.checkBoxShift = wx.CheckBox(dlg, wx.ID_ANY, _('Shift'))
        dlg.listBoxKey = wx.Choice(dlg, wx.ID_ANY, choices=keyStringList)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(dlg.checkBoxCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(15))
        sizer.Add(dlg.checkBoxAlt, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(15))
        sizer.Add(dlg.checkBoxShift, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(15))
        sizer.Add(wx.StaticText(dlg, wx.ID_ANY, _('Key:')), 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(5))
        sizer.Add(dlg.listBoxKey, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, dpi.intPPI(15))
        # Standard buttons
        okay  = wx.Button(dlg, wx.ID_OK, _('OK'))
        #~ dlg.Bind(wx.EVT_BUTTON, self.OnEditButtonOK, okay)
        clear = wx.Button(dlg, wx.ID_NO, _('Clear'))
        dlg.Bind(wx.EVT_BUTTON, self.OnEditButtonClear, clear)
        cancel = wx.Button(dlg, wx.ID_CANCEL, _('Cancel'))
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.AddButton(clear)
        btns.Realize()
        # Size the elements
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(dlg.menuLabel, 0, wx.TOP|wx.LEFT, dpi.intPPI(10))
        dlgSizer.Add(sizer, 0, wx.EXPAND|wx.ALL, dpi.intPPI(15))
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, dpi.intPPI(10))
        dlg.SetSizer(dlgSizer)
        dlgSizer.Fit(dlg)
        # Misc
        okay.SetDefault()
        return dlg

    def OnListCtrlActivated(self, event):
        dlg = self.defineShortcutEditDialog()
        index = event.GetIndex()
        dlg.listIndex = index
        label, shortcut, id = self.shortcutList[index]
        dlg.menuLabel.SetLabel(label)
        if shortcut == '':
            dlg.checkBoxCtrl.SetValue(False)
            dlg.checkBoxAlt.SetValue(False)
            dlg.checkBoxShift.SetValue(False)
            dlg.listBoxKey.SetSelection(wx.NOT_FOUND)
        else:
            items = [s.upper() for s in shortcut.split('+')]
            if not items[-1]:
                del items[-1]
                items[-1] += '+'
            boolCtrl = False
            boolAlt = False
            boolShift = False
            if 'CTRL' in items:
                boolCtrl = True
            if 'ALT' in items:
                boolAlt = True
            if 'SHIFT' in items:
                boolShift = True
            if len(items) == 1:
                keyString = items[0]
            else:
                keyString = items[-1]
            dlg.checkBoxCtrl.SetValue(boolCtrl)
            dlg.checkBoxAlt.SetValue(boolAlt)
            dlg.checkBoxShift.SetValue(boolShift)
            if not dlg.listBoxKey.SetStringSelection(keyString):
                print>>sys.stderr, _('%(keyString)s not found in key string list') % locals()
        ID = dlg.ShowModal()
        # Set the data
        if ID == wx.ID_OK:
            self.OnEditButtonOK(dlg)
            #~ self.options = dlg.GetDict()
        dlg.Destroy()

    def OnEditButtonOK(self, dlg):
        # Get the values from the dialog
        boolCtrl = dlg.checkBoxCtrl.GetValue()
        boolAlt = dlg.checkBoxAlt.GetValue()
        boolShift = dlg.checkBoxShift.GetValue()
        keyString = dlg.listBoxKey.GetStringSelection()
        # Check basic invalid cases
        #~ if keyString == '':
            #~ wx.MessageBox(_('You must specify a key!'), _('Error'), style=wx.ICON_ERROR)
            #~ return
        #~ if (len(keyString) == 1 or keyString in ('Home', 'End', 'PgUp', 'PgDn', 'Up', 'Down', 'Left', 'Right')) and (not boolCtrl and not boolAlt and not boolShift):
        #~ if (len(keyString) == 1) and (not boolCtrl and not boolAlt and not boolShift):
            #~ wx.MessageBox(_('You must check at least one modifier!'), _('Error'), style=wx.ICON_ERROR)
            #~ return
        # Build the shortcut string
        shortcut = ''
        if boolCtrl:
            shortcut += 'Ctrl+'
        if boolAlt:
            shortcut += 'Alt+'
        if boolShift:
            shortcut += 'Shift+'
        if keyString:
            shortcut += keyString
            # Check if keyboard shortcut already exists
            oldShortcut = self.shortcutList[dlg.listIndex][1]
            shortcutUpper = shortcut.upper()
            if shortcutUpper != oldShortcut.upper():
                #~ if shortcutUpper in [info[1].upper() for info in self.shortcutList]:
                for info in self.shortcutList:
                    if shortcutUpper == info[1].upper():
                        line1 = _('This shortcut is being used by:')
                        line2 = info[0]
                        line3 = _('Do you wish to continue?')
                        ret = wx.MessageBox('%s\n\n%s\n\n%s' % (line1, line2 , line3), _('Warning'),
                                            wx.OK|wx.CANCEL|wx.ICON_EXCLAMATION, dlg)
                        if ret == wx.OK:
                            info[1] = ''
                            #~ self.updateMenuLabel(info[2], '')
                        else:
                            return
                        break
        self.shortcutList[dlg.listIndex][1] = shortcut
        #~ self.updateMenuLabel(self.shortcutList[dlg.listIndex][2], shortcut)
        self.listCtrl.Refresh()
        #~ event.Skip()

    def OnEditButtonClear(self, event):
        dlg = event.GetEventObject().GetParent()
        dlg.checkBoxCtrl.SetValue(False)
        dlg.checkBoxAlt.SetValue(False)
        dlg.checkBoxShift.SetValue(False)
        dlg.listBoxKey.SetSelection(wx.NOT_FOUND)
        #~ msgDlg = wx.MessageDialog(self, _('Are you sure you want to clear this shortcut?'), _('Warning'))
        #~ ID = msgDlg.ShowModal()
        #~ msgDlg.Destroy()
        #~ if ID == wx.ID_OK:
            #~ self.shortcutList[dlg.listIndex][1] = ''
            #~ dlg.EndModal(wx.ID_NO)
            #~ self.listCtrl.Refresh()
        #~ else:
            #~ dlg.EndModal(wx.ID_CANCEL)

    def _x_updateMenuLabel(self, id, shortcut):
        menuItem = self.parent.GetMenuBar().FindItemById(id)
        label = menuItem.GetLabel()
        newLabel = '%s\t%s' % (label, shortcut)
        menuItem.SetText(newLabel)

class EditStringDictDialog(wx.Dialog):
    def __init__(self, parent, infoDict, title='Edit', keyTitle='Key',
                 valueTitle='Value', editable=False, insertable=False, size=dpi.tuplePPI(640, 440),
                 about='', keyChecker=None, valueChecker=None, nag=False):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, title, size=size, style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
        dpi.SetFontPPI(self)
        int5 = dpi.intPPI(5)
        int10 = dpi.intPPI(10)
        int20 = dpi.intPPI(20)
        self.infoDict = infoDict.copy()
        self.keyTitle = keyTitle
        self.valueTitle = valueTitle
        self.keyChecker = keyChecker
        self.valueChecker = valueChecker
        self.nag = nag
        self.previousKey = None
        self.editName = ''
        self.textChanged = False
        # Create the key and value static text labels
        keyLabel = wx.StaticText(self, wx.ID_ANY, keyTitle)
        valueLabel = wx.StaticText(self, wx.ID_ANY, valueTitle)
        # Create the list control using the dictionary
        style = wx.LC_REPORT|wx.LC_NO_HEADER|wx.LC_SORT_ASCENDING|wx.LC_SINGLE_SEL
        if editable:
            style |= wx.LC_EDIT_LABELS
        self.listCtrl = ListCtrl(self, wx.ID_ANY, style=style)
        self.listCtrl.InsertColumn(0, 'Column 0')
        for row, key in enumerate(self.infoDict.keys()):
            self.listCtrl.InsertStringItem(row, key)
        self.listCtrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnListItemSelected)
        self.listCtrl.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnListItemEdit)
        self.listCtrl.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.OnListItemEdited)
        # Create the text control
        self.textCtrl = TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE|wx.HSCROLL)
        self.textCtrl.Bind(wx.EVT_TEXT, self.OnValueTextChanged)
        # Create the insert/delete buttons
        if insertable:
            insertButton = wx.Button(self, wx.ID_ANY, _('Insert'))
            self.Bind(wx.EVT_BUTTON, self.OnButtonInsert, insertButton)
            deleteButton = wx.Button(self, wx.ID_ANY, _('Delete'))
            self.Bind(wx.EVT_BUTTON, self.OnButtonDelete, deleteButton)
            insSizer = wx.BoxSizer(wx.HORIZONTAL)
            insSizer.Add(insertButton, 1, wx.ALIGN_CENTER|wx.ALL, int5)
            insSizer.Add(deleteButton, 1, wx.ALIGN_CENTER|wx.ALL, int5)
        # Standard buttons
        okay  = wx.Button(self, wx.ID_OK, _('OK'))
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, okay)
        cancel = wx.Button(self, wx.ID_CANCEL, _('Cancel'))
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Size the elements
        gridSizer = wx.FlexGridSizer(cols=2, hgap=int10, vgap=int5)
        gridSizer.AddGrowableCol(1, 1)
        gridSizer.AddGrowableRow(1)
        gridSizer.Add(keyLabel, 0)
        gridSizer.Add(valueLabel, 0, wx.ALIGN_CENTER)
        gridSizer.Add(self.listCtrl, 2, wx.EXPAND|wx.RIGHT, int10)
        gridSizer.Add(self.textCtrl, 3, wx.EXPAND)
        minWidth = max(self.listCtrl.GetColumnWidth(0), keyLabel.GetSize()[0])
        gridSizer.SetItemMinSize(self.listCtrl, min(minWidth+int20, 200), int20*2)
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(gridSizer, 1, wx.EXPAND|wx.ALL, int10)
        if insertable:
            dlgSizer.Add(insSizer, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.BOTTOM, dpi.intPPI(15))
        if about:
            dlgSizer.Add(wx.StaticText(self, wx.ID_ANY, about), 0, wx.ALIGN_CENTER|wx.BOTTOM, int10)
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, int5)
        self.SetSizer(dlgSizer)
        # Misc
        if self.listCtrl.GetItemCount():
            self.listCtrl.SelectItem(0)
        okay.SetDefault()

    def GetDict(self):
        return self.infoDict

    def UpdateDictEntry(self):
        if self.infoDict.has_key(self.previousKey) and self.textChanged:
            self.infoDict[self.previousKey] = self.textCtrl.GetValue().strip()

    def OnValueTextChanged(self, event):
        self.textChanged = True

    def OnListItemSelected(self, event):
        # Update the previously selected key
        self.UpdateDictEntry()
        # Display the value associated with the selected key
        key = event.GetText()
        value = self.infoDict.get(key)
        if value is not None:
            self.textCtrl.Replace(0, -1, value)
            self.textCtrl.SetInsertionPoint(0)
            self.textChanged = False
        else:
            print>>sys.stderr, _('Error: key %(key)s does not exist!') % locals()
        self.previousKey = key

    def OnListItemEdit(self, event):
        self.editName = event.GetText()

    def OnListItemEdited(self, event):
        if event.IsEditCancelled():
            return
        newName = event.GetLabel()
        if not newName:
            event.Veto()
            return
        if newName != self.editName:
            if newName in self.infoDict:
                wx.MessageBox(_('Item %(newKey)s already exists!') % {'newKey': newName},
                              _('Error'), style=wx.OK|wx.ICON_ERROR)
                event.Veto()
                return
            if self.keyChecker:
                msg = self.keyChecker(newName)
                if msg is not None:
                    wx.MessageBox(msg, _('Error'), style=wx.OK|wx.ICON_ERROR)
                    event.Veto()
                    return
            if self.nag:
                oldName = self.editName
                dlg = wx.MessageDialog(self, _('Are you sure you want to rename from %(oldName)s to %(newName)s?') % locals(), _('Question'))
                ID = dlg.ShowModal()
                dlg.Destroy()
                if ID != wx.ID_OK:
                    event.Veto()
                    return
            # "Rename" the key in the dictionary
            del self.infoDict[self.editName]
            self.infoDict[newName] = self.textCtrl.GetValue().strip()

    def OnButtonInsert(self, event):
        dlg = wx.Dialog(self, wx.ID_ANY, _('Insert a new item'))
        dpi.SetFontPPI(dlg)
        sizer = wx.BoxSizer(wx.VERTICAL)
        keyTextCtrl = wx.TextCtrl(dlg, wx.ID_ANY)
        valueTextCtrl = TextCtrl(dlg, wx.ID_ANY, style=wx.TE_MULTILINE|wx.HSCROLL)
        sizer.Add(wx.StaticText(dlg, wx.ID_ANY, self.keyTitle.strip()), 0, wx.EXPAND)
        sizer.Add(keyTextCtrl, 0, wx.EXPAND|wx.BOTTOM, 10)
        sizer.Add(wx.StaticText(dlg, wx.ID_ANY, self.valueTitle.strip()), 0, wx.EXPAND)
        sizer.Add(valueTextCtrl, 1, wx.EXPAND|wx.BOTTOM, 10)
        # Standard buttons
        okay  = wx.Button(dlg, wx.ID_OK, _('OK'))
        cancel = wx.Button(dlg, wx.ID_CANCEL, _('Cancel'))
        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okay)
        btns.AddButton(cancel)
        btns.Realize()
        # Size the elements
        dlgSizer = wx.BoxSizer(wx.VERTICAL)
        dlgSizer.Add(sizer, 1, wx.EXPAND|wx.ALL, 10)
        dlgSizer.Add(btns, 0, wx.EXPAND|wx.ALL, 5)
        dlg.SetSizer(dlgSizer)
        # Show the dialog
        ID = dlg.ShowModal()
        newKey = keyTextCtrl.GetValue().lstrip('.')
        newValue = valueTextCtrl.GetValue().strip()
        dlg.Destroy()
        # Add the new item to the dictionary as well as the listCtrl
        if ID == wx.ID_OK:
            if not newKey:
                wx.MessageBox(_('Must enter a name!'), _('Error'),
                              style=wx.OK|wx.ICON_ERROR)
                return
            if self.infoDict.has_key(newKey):
                wx.MessageBox(_('Item %(newKey)s already exists!') % locals(),
                              _('Error'), style=wx.OK|wx.ICON_ERROR)
                return
            if self.keyChecker:
                msg = self.keyChecker(newKey)
                if msg is not None:
                    wx.MessageBox(msg, _('Error'), style=wx.OK|wx.ICON_ERROR)
                    return
            if self.valueChecker:
                msg = self.valueChecker(newValue)
                if msg is not None:
                    wx.MessageBox(msg, _('Error'), style=wx.OK|wx.ICON_ERROR)
                    return
            self.infoDict[newKey] = newValue
            self.listCtrl.InsertStringItem(0, newKey)
            self.listCtrl.SelectLabel(newKey)
            if newValue == '' and self.nag:
                wx.MessageBox(_('Warning: no value entered for item %(newKey)s!') % locals(), _('Warning'))
                self.textCtrl.SetFocus()

    def OnButtonDelete(self, event):
        index = self.listCtrl.GetNextItem(-1, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
        if index == -1:
            wx.MessageBox(_('Select an item to delete first'), _('Message'))
            return
        key = self.listCtrl.GetItemText(index)
        dlg = wx.MessageDialog(self, _('Are you sure you want to delete item %(key)s?') % locals(), _('Question'))
        ID = dlg.ShowModal()
        if ID == wx.ID_OK:
            del self.infoDict[key]
            self.listCtrl.DeleteItem(index)
            if self.listCtrl.GetItemCount():
                if index - 1 < 0:
                    self.listCtrl.SelectItem(0)
                else:
                    self.listCtrl.SelectItem(index-1)
        dlg.Destroy()


    def OnButtonOK(self, event):
        # Update the previously selected key
        self.UpdateDictEntry()
        event.Skip()

class Slider(wx.Slider):
    def __init__(self, parent, id=wx.ID_ANY,
            value=0, minValue=0, maxValue=100,
            point=wx.DefaultPosition, size=wx.DefaultSize,
            style=wx.SL_HORIZONTAL, validator=wx.DefaultValidator,
            name="slider", nDecimal=0, mod=None, onscroll=None):
        # Class variables
        self.parent = parent
        self.onscroll = onscroll
        self.wxMaxValueLimit = 10000
        # User slider values
        self.uValue = value
        self.uMinValue = minValue
        self.uMaxValue = maxValue
        if mod is not None:
            if mod > maxValue - minValue:
                mod = None
            else:
                #~ minValue = minValue + minValue % mod
                if type(mod) is int:
                    maxValue = maxValue - (maxValue - minValue) % mod
                if mod > maxValue - minValue:
                    mod = None
                else:
                    nDecimal = 0
                    self.uMinValue = minValue
                    self.uMaxValue = maxValue
                    self.uValue = min(value + (value - minValue) % mod, maxValue)
        self.uSelStart = 0
        self.uSelEnd = 0
        self.nDecimal = nDecimal
        # Determine the internal slider range (0 to wxMaxValue)
        self.wxMaxValue = self._get_wxMaxValue(minValue, maxValue, nDecimal, mod)
        # Create the slider control
        aValue = self._upos2wxpos(value)
        aMaxValue = self._upos2wxpos(maxValue)
        wx.Slider.__init__(self, parent, id,
            aValue, 0, self.wxMaxValue,
            point=point, size=size, style=style,
            validator=validator, name=name
        )
        self.name = self.GetName()
        # Event binding
        #EVT_SCROLL_ENDSCROLL(self,self.OnSliderChanged)
        self.Bind(wx.EVT_SCROLL, self._OnSliderChanging)
        #~ super(Slider, self).Bind(wx.EVT_SCROLL, self._OnSliderChanged)

    def _get_wxMaxValue(self, uMinValue, uMaxValue, nDecimal, mod):
        if mod is None:
            step = 1/float(10**nDecimal)
        else:
            step = mod
        wxMaxValue = (uMaxValue - uMinValue) / step
        wxMaxValue = int(round(wxMaxValue))
        if wxMaxValue >= self.wxMaxValueLimit:
            wxMaxValue = self.wxMaxValueLimit
        return wxMaxValue

    def _upos2wxpos(self, upos):
        ''' Converts user pos to actual wxSlider pos '''
        wxpos = self.wxMaxValue * (upos - self.uMinValue) / float(self.uMaxValue - self.uMinValue)
        return int(round(wxpos))

    def _wxpos2upos(self, wxpos):
        ''' Converts actual wxSlider pos to user pos '''
        upos = self.uMinValue + (self.uMaxValue - self.uMinValue) * wxpos / float(self.wxMaxValue)
        if self.nDecimal == 0:
            upos = int(round(upos))
        #~ else:
            #~ upos = round(upos, 4)
        return upos

    def _OnSliderChanging(self, event):
        self.uValue = self._wxpos2upos(super(Slider, self).GetValue())
        if self.onscroll:
        #~ if False:
            self.onscroll(event)
        event.Skip()

    def GetValue(self):
        #~ self.uValue = self._wxpos2upos(super(Slider, self).GetValue())
        return self.uValue

    def GetValueAsString(self):
        strTemplate = '%.'+str(self.nDecimal)+'f'
        return strTemplate % self.uValue

    def GetMin(self):
        return self.uMinValue

    def GetMax(self):
        return self.uMaxValue

    def _GetSelStart(self):
        return self.uSelStart

    def _GetSelEnd(self):
        return self.uSelEnd

    def _GetLineSize(self):
        pass

    def _GetPageSize(self):
        pass

    def _GetThumbLength(self):
        pass

    def _GetTickFreq(self):
        pass

    def SetValue(self, value):
        if self.nDecimal == 0:
            value = int(round(value))
        self.uValue = value
        super(Slider, self).SetValue(self._upos2wxpos(value))
        #~ self.uValue = self._wxpos2upos(super(Slider, self).GetValue())

    def SetRange(self, minValue, maxValue, nDecimal=None, mod=None):
        if minValue >= maxValue:
            if minValue == 0 and (maxValue == -1 or maxValue ==0):
                maxValue = 1
            else:
                print>>sys.stderr, _('Error: minValue must be less than maxValue')
                return
        self.uMinValue = minValue
        self.uMaxValue = maxValue
        if nDecimal is not None:
            self.nDecimal = nDecimal
        self.wxMaxValue = self._get_wxMaxValue(minValue, maxValue, self.nDecimal, mod)
        super(Slider, self).SetRange(0, self.wxMaxValue)

    def SetSelection(self, startPos, endPos):
        self.uSelStart = startPos
        self.uSelEnd = endPos
        super(Slider, self).SetSelection(self._upos2wxpos(startPos), self._upos2wxpos(endFrame))

    def Increment(self):
        wxpos = super(Slider, self).GetValue()
        if wxpos < super(Slider, self).GetMax():
            wxpos += 1
            self.uValue = self._wxpos2upos(wxpos)
            super(Slider, self).SetValue(wxpos)
        return self.uValue

    def Decrement(self):
        wxpos = super(Slider, self).GetValue()
        if wxpos > super(Slider, self).GetMin():
            wxpos -= 1
            self.uValue = self._wxpos2upos(wxpos)
            super(Slider, self).SetValue(wxpos)
        return self.uValue

    def _SetLineSize(self):
        pass

    def _SetPageSize(self):
        pass

    def _SetThumbLength(self):
        pass

    def _SetTickFreq(self):
        pass

    def SetTick(self, upos):
        super(Slider, self).SetTick(self._upos2wxpos(upos))

class StaticText(wx.StaticText):
    ''' StaticText without flicker '''
    def __init__(self, parent, id=wx.ID_ANY, label=wx.EmptyString,
            pos=wx.DefaultPosition, size=wx.DefaultSize,
            style=0, name=wx.StaticTextNameStr):
        wx.StaticText.__init__(self, parent, id, label=label, pos=pos, size=size, style=style, name=name)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self._OnEraseBackground)

    def _OnEraseBackground(self, event): # Do nothing, eleminates the flicker
        pass

