# GPo 2020
# Insert selected avisynth trims as trim editor selections
# If the selection mark is present, the selection mark is deleted,
# you can also delete individual selections in this way

txt = avsp.GetSelectedText(index=None)
if not txt:
   return

self = avsp.GetWindow()
txt = txt.lower()
L = len('trim(')
x2 = 0
error = 0

while 1:
    x1 = txt.find('trim(', x2)
    if x1 > -1:
        x2 = txt.find(')',x1+L)
        if x2 > -1:
            trim = txt[x1+L:x2]
            a = trim.split(',')
            if len(a) > 1:
                start = a[0].strip()
                stop = a[1].strip()
                if start.isdigit() and stop.isdigit():
                    self.AddFrameBookmark(int(start), 1, refreshVideo=False)
                    self.AddFrameBookmark(int(stop), 2, refreshVideo=False)
                else:
                    error += 1 
            else:
                error += 1
        else:
            error += 1
            break
    else:
        break
        
if error > 0:
    avsp.MsgBox(str(error) + ' trim error(s)\nCheck the selected trims', title='Error')
    return
# if script focused, the script deletes the selected text when you press space key
# so deselect the selection and focus the video window for play video with space key
self.currentScript.ClearSelections()
if self.previewWindowVisible:
    self.videoWindow.SetFocus()