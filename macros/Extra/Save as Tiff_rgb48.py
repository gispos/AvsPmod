# GPo 2021, Save as Tiff_rgb48.py
# save current frame as 48bit tiff image file with ffmpeg

import subprocess
import os
import sys
self = avsp.GetWindow()

##### user settings
# path to ffmpeg.exe 
ffmpeg = os.path.join(self.programdir, 'encoders\\ffmpeg.exe')

# added the output to a new tab ( FFImageSource )
addNewTab = True
#####

script = self.currentScript
if self.UpdateScriptAVI() is None or not self.previewOK(script):
    avsp.MsgBox('Script not initialized.')
    return
frame = avsp.GetFrameNumber()
trim = 'trim(%i, -1)' % frame
scriptTxt = avsp.GetText(index=None, clean=True).strip() + '\n' + trim

if not os.path.isfile(ffmpeg):
    avsp.MsgBox('ffmpeg not found.\nYou must change the "ffmpeg" variable in the macro.\n\n' + ffmpeg, 'Error')
    return
    
default = self.options['imagesavedir']
#default = self.GetProposedPath(type_='image')
if not os.path.isdir(default):
    default = ''
if script.filename:
    base, ext = os.path.splitext(script.filename)
    default = base + '.tif'
    
outfile = avsp.GetSaveFilename(title='Save as', filefilter=_('Tagged Image File') + ' (*.tif)|*.tif', default=default)
if not outfile:
    return
self.options['imagesavedir'] = os.path.dirname(outfile)
        
infile = os.path.join(os.path.split(outfile)[0], 'encoding.avs')
encoding_args = [
    ffmpeg,
    '-i', infile,
    '-an',
    '-pix_fmt', 'rgb48',
    '-vcodec', 'tiff',
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
    self.NewTab(text='#Filesize: %s\nFFImageSource("%s")' % (fileSizeToString(encoding_file_size), outfile))
    
