# Written by GPo
# Shift all bookmarks div 2. 
# Useful if bookmarks were set and you forgot to reduce the framerate from 50 to 25 with SelectEven().

try:
    try:
        bookmarks=[(b+-int(b//2), t) for b,t in avsp.GetBookmarkList( title=True )]
    except TypeError:
        bookmarks=[(b+-int(b//2)) for b in avsp.GetBookmarkList()]
    avsp.GetWindow().DeleteAllFrameBookmarks(bmtype=0)
    avsp.SetBookmark( bookmarks )
except:
    pass