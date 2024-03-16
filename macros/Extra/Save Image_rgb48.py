# GPo 2024, Save Image_rgb48.py
# save current frame as 48bit tiff or png file with ffmpeg

import subprocess
import os
import sys
self = avsp.GetWindow()

##### user settings
# path to ffmpeg.exe 
ffmpeg = os.path.join(self.programdir, 'encoders\\ffmpeg.exe')

# added the output to a new tab ( ImageReader or FFImageSource )
addNewTab = True

# change the ImageReader for the new tab. FFImageSource("%s") or ImageReader("%s", pixel_type="RGB48")
ImageReader = 'ImageReader("%s", pixel_type="RGB48")'

# append frame number
addFrameNr = True
#####

script = self.currentScript
if self.UpdateScriptAVI() is None or not self.previewOK(script):
    avsp.MsgBox('Script not initialized.')
    return
frame = avsp.GetFrameNumber()
trim = 'trim(%i, -1)' % frame
txt = self.getCleanText(script.GetText())
txt = self.stripComment_2(txt)
txt, encoding = self.GetEncodedText(script, txt, forceUtf8=False)
scriptTxt = txt.strip() + '\n' + trim

if not os.path.isfile(ffmpeg):
    avsp.MsgBox('ffmpeg not found.\nYou must change the "ffmpeg" variable in the macro.\n\n' + ffmpeg, 'Error')
    return
    
default = self.options['imagesavedir']
tabTitle = self.scriptNotebook.GetPageText(self.scriptNotebook.GetSelection())
filterIdx = avsp.Options.get('filteridx', 0)

if not os.path.isdir(default):
    default = ''
if script.filename:
    base, ext = os.path.splitext(script.filename)
    if addFrameNr:
        default = '%s_%i' % (base, frame)
    else:
        default = base
elif addFrameNr:
    if default:
        path = os.path.join(default, tabTitle)
        default = '%s_%i' % (path, frame)
    else:
        default = '%s_%i' % (tabTitle, frame)
elif default:
   default = os.path.join(default, tabTitle)
else:
   default = tabTitle
 
filter = 'Tagged Image File (*.tif)|*.tif|Portable Network Graphics (*.png)|*.png' 
idx, outfile = avsp.GetSaveFilename(title='Save as', filefilter=filter, default=default, getfilteridx=True, setfilteridx=filterIdx)
if not outfile:
    return
imageType = 'tiff' if idx == 0 else 'png'

self.options['imagesavedir'] = os.path.dirname(outfile)
avsp.Options['filteridx'] = idx

infile = os.path.join(self.toolsfolder, 'encode.avs')
encoding_args = [
    ffmpeg,
    '-ss', '00:00:00',
    '-i', infile,
    #'-pix_fmt', 'rgb48',
    '-vcodec', imageType,
    '-frames:v','1',
    '-update', '1',
    '-y', outfile,
    ]
    
try:
    with open(infile, 'wb') as f:
        f.write(scriptTxt)
        f.close()
except IOError as err:
    raise

def utf8ify(list):
  return [item.encode(sys.getfilesystemencoding()) for item in list]
  
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
    
encoding_errors = ''
encoding_file_size = 0
args = utf8ify(encoding_args)
re = subprocess.call(args)
if re != 0:
    encoding_errors = 'Code: %s\n%s\n' % (str(re), os.path.split(outfile)[1])
elif os.path.isfile(outfile):
    encoding_file_size += os.path.getsize(outfile)
else:
    encoding_errors = 'Unknown error'
    
if encoding_errors:
    avsp.MsgBox('Last encoding returns error\n' + encoding_errors, 'Error')
elif addNewTab:
    ImageReader = ImageReader % outfile
    self.NewTab(text='#Filesize: %s\n%s' % (fileSizeToString(encoding_file_size), ImageReader))
    
