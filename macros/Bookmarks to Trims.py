# GPo 2020

import wx

bmlist = avsp.GetBookmarkList(title=False)
if not bmlist:
    wx.MessageBox(_('No bookmarks defined.'), _('Error'), style=wx.OK|wx.ICON_ERROR)
    return

bmlist.sort()
count = len(bmlist)
txt = ''

for i in xrange(count):
    if i %2 == 0:
        txt += 'Trim(' + str(bmlist[i])
    else:
        txt += ', ' + str(bmlist[i]) + ') ++ '
    
if count %2 == 0:
    txt = txt[:-4]
else:
    txt += ', 0)' 

avsp.InsertText(txt, pos=None)