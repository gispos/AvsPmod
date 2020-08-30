"""
 GPo 2020, AvsPmod macro 'Open ImageSequence.py'
 Only useful for image names with consecutive frame numbers in a sequence.
 If the frame number is not consecutive, a new ImageSource is added.
 Uses all images in the selected directory that match the selected file name.
 Separate by file (frame) range numbers e.g.:
     Img_000000.png to Img_000020.png insert one ImageSource
     Img_000000.png to Img_000010.png and Img_000012.png to Img_000020.png insert two ImageSources
     000001.png to 000010.png and 000012.png to 000020.png insert also two ImageSources
"""
import os

filename = avsp.GetFilename(_('Select the Image'), filefilter=
                            _('Images (bmp, jpg, png, tiff)') + '|*.bmp;*.jpg;*.png;*.tiff|' +
                            _('All files (*.*)') + '|*.*')
if not filename:
    return
                            
base_dir, name = os.path.split(filename)
base_name, base_ext = os.path.splitext(name)
alpha = ''
files = []
clips = 0
s = ''
ss = ''
base_dir = os.path.join(base_dir, '')

# return the first non number chars
def GetFirstAlpha(f):
    a = ''
    for n in f:
        if not n.isdigit():
            a = ''.join([a,n])
        else:
            break
    return a
    
def GetFormat(f):
    return base_dir + alpha + '%0' + str(len(f)) + 'd' + base_ext
    
if not base_name.isdigit():
    alpha = GetFirstAlpha(base_name)
    if not base_name[len(alpha):].isdigit():
        avsp.MsgBox('No valid range numbers in file name found')
        return

# add all matched file names        
for f in os.listdir(base_dir):
    name, ext = os.path.splitext(f)
    if alpha:
        if alpha != name[:len(alpha)]:
            continue
        name = name[len(alpha):]
    if name.isdigit() and ext.lower() == base_ext.lower():
        files.append(name)
        
if len(files) < 1:
    avsp.MsgBox('No files to process')
    return
files.sort()       
 
start = int(files[0]) 
for i in xrange(len(files)):
    if i > 0:
        last = int(files[i-1])
        if int(files[i]) - last != 1: # if next frame number is not consecutive, create a new ImageSource
            clips += 1
            s += 'c%d=ImageSource("%s", start=%d, end=%d)\n' % (clips, GetFormat(files[i]), start, last)
            ss += 'c' + str(clips) + '+'
            start = int(files[i])
    end = int(files[i])
                
clips += 1 
ss += 'c' + str(clips)      
s += 'c%d=ImageSource("%s", start=%d, end=%d)\n%s' % (clips, GetFormat(files[len(files)-1]), start, end, ss)
avsp.InsertText(s)