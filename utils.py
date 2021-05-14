#-------------------------------------------------------------------------------
# Name:        utils
# Purpose:
#
# Author:      GPo
#
# Created:     04.04.2021
# Copyright:   (c) GPo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import os

resource_str_threadwait = _('Waiting for Avisynth, thread still running.\n' +
                           'This dialog is automatically closed when avisynth returns.\n' +
                           'If you abort this process, you should restart the program!')

resource_str_threadwait2 = _('Waiting for Avisynth, thread still running.\n' +
                           'This dialog is automatically closed when avisynth returns.\n' +
                           'If you abort this process, the clip will assign later.')


"""
WIN_10 = (10, 0, 0)
WIN_8 = (6, 2, 0)
WIN_7_SP1 = (6, 1, 1)
WIN_7 = (6, 1, 0)
WIN_SERVER_2008 = (6, 0, 1)
WIN_VISTA_SP1 = (6, 0, 1)
WIN_VISTA = (6, 0, 0)
WIN_SERVER_2003_SP2 = (5, 2, 2)
WIN_SERVER_2003_SP1 = (5, 2, 1)
WIN_SERVER_2003 = (5, 2, 0)
WIN_XP_SP3 = (5, 1, 3)
WIN_XP_SP2 = (5, 1, 2)
WIN_XP_SP1 = (5, 1, 1)
WIN_XP = (5, 1, 0)
"""

def get_winversion():
    if os.name != 'nt':
        return 0
    wv = sys.getwindowsversion()
    if hasattr(wv, 'service_pack_major'):  # python >= 2.7
        sp = wv.service_pack_major or 0
    else:
        import re
        r = re.search("\s\d$", wv.service_pack)
        sp = int(r.group(0)) if r else 0
    #### get ver
    if wv.major < 6 or wv.minor < 1:
        return 6
    elif wv.major == 10:
        return 10
    elif wv.major == 6 and wv.minor > 1:
        return 8
    else:
        return 7
    #return (wv.major, wv.minor, sp)



##### Test ####

"""
def wxProcessEvents(self):
    # this version uses the new Phoenix API
    # Get app

    app = wx.App.Get()

    # Keep reference of old eventloop instance
    old = wx.EventLoopBase.GetActive()
    # Create new eventloop and process
    eventLoop = app.GetTraits().CreateEventLoop()
    wx.EventLoopActivator(eventLoop)
    while eventLoop.Pending():
        eventLoop.Dispatch()
    # Process idle
    eventLoop.ProcessIdle() # otherwise frames do not close
    # Set back the original
    wx.EventLoopActivator(old)
"""
"""
def getWidgets(self, parent):
    '''
    Return a list of all the child widgets
    '''
    items = [parent]
    for item in parent.GetChildren():
        items.append(item)
        if hasattr(item, "GetChildren"):
            for child in item.GetChildren():
                items.append(child)
    return items
"""
###############
