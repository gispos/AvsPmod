#-------------------------------------------------------------------------------
# Name:        PreviewEncode.py
# Purpose:     AvsPmod timeline (selections) preview encoding with ffmpeg.exe
#              Encodes the selection(s) and insert the clips and trims into the script.
#              The purpose is a quick preview for the selected areas, but if also useful for other purpose.
#              Several encodings running at the same time possible.
#
#              Preview filters cannot be adopted.
#              And it is also assumed that an audio is included in the video
#
#              Use the Trim Editor to create selections. Select 'Copy to clipboard' and hit OK
#              Save this file (text) as PreviewEncode.py in the AvsPmod macro or a macro subfolder
#
# Author:      GPo
#
# Created:     24.05.2021, update 01.06.2021
# Copyright:   (c) GPo 2021
# Licence:     <free>
#-------------------------------------------------------------------------------
import os
import sys
import subprocess
import threading
import time

self = avsp.GetWindow()
script = self.currentScript
script_idx = self.scriptNotebook.GetSelection()
saveScriptTxt = script.GetText().strip()
global encoding_errors

################################################################################
## templates and user settings
################################################################################

# convert the encoded clips to the script colorspace  ( vSourceFilterEx must be used )
# otherwise the script will be converted, try what is better
convertToScriptColorSpace = True

# you can change the source filter ("%s" stands for the file name), but it should be frame accurate 
vSourceFilter = 'LWLibavVideoSource("%s", cache=False)'
aSourceFilter = 'LWLibavAudioSource("%s", cache=False)'
vSourceFilterEx = 'LWLibavVideoSource("%s", cache=False, format=pt)'

##### Encoder profile
# In the event of audio problems, the audio must be changed from 'copy' to a conversion format
# and the templates must be adapted (see dnxhd profile) For my videos it works with 'copy'
dnxhr_hq = '-c:v dnxhd -profile:v dnxhr_hq -vf format=yuv422p -c:a pcm_s16le .mov'
dnxhr_hqx = '-c:v dnxhd -profile:v dnxhr_hqx -vf format=yuv422p10le -c:a pcm_s16le .mov'
dnxhr_444 = '-c:v dnxhd -profile:v dnxhr_444 -vf format=yuv444p10le -c:a pcm_s16le .mov'
x264_lossless_8 = '-c:v libx264 -preset ultrafast -qp 0 -vf format=yuv422p -c:a copy .mkv'
x264_lossless_422 = '-c:v libx264 -preset ultrafast -qp 0 -vf format=yuv422p10le -c:a copy .mkv'
x264_lossless_444 = '-c:v libx264 -preset ultrafast -qp 0 -vf format=yuv444p10le -c:a copy .mkv'
x264_nvenc_vbr_8 = '-c:v h264_nvenc -preset p7 -profile:v main -rc vbr -b:v 8000k -c:a aac -b:a 256k .mkv'
x264_nvenc_vbr_422 = '-c:v h264_nvenc -preset P7 -profile:v main -rc vbr -b:v 18000k -c:a aac -b:a 256k .mkv'
x264_nvenc_lossless = '-c:v hevc_nvenc -preset lossless -c:a copy .mkv'
huffyuv_8 = '-c:v huffyuv -vf format=yuv422p -c:a copy .mkv'
ffvhuff = '-c:v ffvhuff -c:a copy .mkv'
FFV1 = '-c:v ffv1 -level 3 -threads 4 -g 1 -coder 1 -context 1 -slices 24 -slicecrc 1 -c:a copy .mkv'
# extra
x264_8_crf16_aac = '-c:v libx264 -preset fast -tune film -crf 16 -vf format=yuv420p -c:a aac -b:a 256k .mkv'
x264_422_crf16_aac = '-c:v libx264 -preset fast -tune film -crf 16 -vf format=yuv422p10le -c:a aac -b:a 256k .mkv'

##### Convert templates 
# converts the script clip to encoder profile, some audio conversions still missing e.g. channels
# if convertToScriptColorSpace = True, only the ConvertAudio section is used
conv_dnxhr_hq = 'ConvertBits(bits=8).ConvertToYUV422(matrix="Rec709").ConvertAudioTo16bit().AssumeSampleRate(48000)\n'
conv_dnxhr_hqx = 'ConvertBits(bits=10).ConvertToYUV422(matrix="Rec709").ConvertAudioTo16bit().AssumeSampleRate(48000)\n'
conv_dnxhr_444 = 'ConvertBits(bits=10).ConvertToYUV444(matrix="Rec709").ConvertAudioTo16bit().AssumeSampleRate(48000)\n'
conv_x264_lossless_8 = 'ConvertBits(bits=8).ConvertToYUV422(matrix="Rec709")\n'
conv_x264_lossless_422 = 'ConvertBits(bits=10).ConvertToYUV422(matrix="Rec709")\n'
conv_x264_lossless_444 = 'ConvertBits(bits=10).ConvertToYUV444(matrix="Rec709")\n'
conv_x264_nvenc_vbr = conv_x264_lossless_8
conv_x264_nvenc_vbr_422 = conv_x264_lossless_422
conv_x264_nvenc_lossless = '\n'
conv_huffyuv_8 = 'ConvertBits(bits=8).ConvertToYUV422(matrix="Rec709")\n'
conv_ffvhuff = '\n'
conv_FFV1 = '\n'
# extra
conv_x264_8_crf16_aac = conv_x264_lossless_8
conv_x264_422_crf16_aac = conv_x264_lossless_422

##### Settings
# set the encoding profile and convert template, default ffvhuff
encoding_args = ffvhuff
convert_txt = conv_ffvhuff

# use ffvhuff if bit count <= 8 else dnxhr_444 (you can change the templates, search for 'if codecAutoSelect')
codecAutoSelect = False

# change the save path for the encoded files or use the script dir if it exists (script saved)
savePath = 'K:\\Temp\\'
useScriptDir = False

# If True, a path selection dialog is displayed
promptForDir = False

# change the ffmpeg.exe path e.g. 'D:\\tools\\ffmpeg\\ffmpeg.exe', default ..AvsPmod\\encoders\\ffmpeg.exe
ffmpeg = os.path.join(self.programdir, 'encoders\\ffmpeg.exe')

# limit the encodings count to max_files, -1 disabled
max_files = -1

# if disabled, no text will insert in the script, only avs files created and encoding runs
insertTrims = True

# if insertTrims, insert also the selections as trim text for script playback with another app
insertSelectionsAsTrims = True

# not recommended, run all encodings at once, AvsPmod is not waiting, useThreads is disabled
# and the CPU usage can be 100% and hard drive and memory can be on the limit
allEncodingsAtOnce = False

# encode in threads, if I messed up or your system can't handle it, you must deactivate it!
useThreads = True

# if useThreads, you must set the maximum number of simultaneous encode processes
# good value should between 2-4, if it's not working set it to 1 or disable useThreads
max_encoding_threads = 2

################################################################################

if self.UpdateScriptAVI() is None or not self.previewOK(script):
    avsp.MsgBox('Script not initialized.')
    return

if not os.path.isfile(ffmpeg):
    avsp.MsgBox('ffmpeg not found:\n' + ffmpeg)
    return

if useScriptDir:
    if script.filename:
        savePath = os.path.split(script.filename)[0]

if promptForDir:       
    savePath = avsp.GetDirectory(title='Select a directory')
    if not savePath:
        return

if not os.path.isdir(savePath):
    if not avsp.MsgBox('Path not exists:\n%s\n\nTrying to create the path?' % savePath, cancel=True):
        return
    try:
        os.mkdir(savePath)
    except OSError as error:
        raise
 
if codecAutoSelect:
    if script.AVI.vi.bits_per_component() <= 8:
        encoding_args = ffvhuff #~huffyuv_8
        convert_txt = conv_ffvhuff #~conv_huffyuv_8
    else:
        encoding_args = dnxhr_444 #~ffvhuff 
        convert_txt = conv_dnxhr_444 #~conv_ffvhuff

# convert to list if needed
if isinstance(encoding_args, basestring):
    encoding_args = encoding_args.split(' ')

# command line encoding
def utf8ify(list):
  return [item.encode(sys.getfilesystemencoding()) for item in list]

def GetScriptFileName(default):
    if script.filename:
        return os.path.split(script.filename)[1]
    return default

def encodeAvs(infile, outfile, single=True):
    global encoding_errors
    args = [ffmpeg, '-i', infile]
    temp = list(encoding_args)
    temp.pop()
    args += temp + ['-y', outfile]
    args = utf8ify(args)
    if single:
        # single encoding AvsPmod is blocked if not in macro thread running
        re = subprocess.call(args)
        if re != 0:
            encoding_errors += 'Code: %s\n%s\n' % (str(re), os.path.split(outfile)[1])
    else:
       # multi encoding AvsPmod is not blocked (encoding CPU usage can be 100%)
       # Only initialize the script again when all encodings are finished!
       subprocess.Popen(args)

def RunnThread(avsFile, videoFile):
    thread = threading.Thread(target=encodeAvs, args=(avsFile, videoFile, True,), name='MacroThread')
    thread.daemon = True
    thread.start()
    return thread

selections = self.GetSliderSelections()
if not selections:
    avsp.MsgBox(_('You must first create selections'))
    return

# We must release the encoded video files or ffmpeg cannot create the new files
frameCount = script.AVI.Framecount
self.HidePreviewWindow()
self.OnMenuScriptReleaseMemory(None)
self.Refresh()
self.Update()

# read the selections
i = 0
encodings = []
start, stop = selections[0]
if start > 0:
    start = -1 if start == 1 else start-1
    encodings.append((0, 'Trim(%d, %d)' % (0, start)))

for start, stop in selections:
    encodings.append((1,'Trim(%d, %d)' % (start, stop)))
    if i < len(selections)-1:
        nextStart, nextStop = selections[i+1]
        encodings.append((0,'Trim(%d, %d)' % (stop+1, nextStart-1)))
    i += 1
    if (max_files > 0) and (i > max_files):
        break

if stop < frameCount-1: #self.videoSlider.maxValue-1:
    encodings.append((0, 'Trim(%d, %d)' % (stop+1, 0)))

# start the encoding loop
i = 0
trimList = []
threadList = []
selTrims = r'#encodes: '
scriptTxt = self.getCleanText(saveScriptTxt)
scriptTxt = self.stripComment_2(scriptTxt)  + '\n'

if allEncodingsAtOnce:
    useThreads = False
if convertToScriptColorSpace:
    vSourceFilter = vSourceFilterEx
encoding_errors = ''
start_time = time.time()

for typ, line in encodings:
    if typ == 0:
        trimList.append((line, '', ''))
        continue
    txt = scriptTxt + line
    txt = self.GetEncodedText(txt, bom=True)
    clip = 'enc%d' % (i)
    selTrims += line + '++'
    avsFile = os.path.join(savePath, clip + '_%s' % GetScriptFileName(str(script_idx) + '.avs'))
    try:
        with open(avsFile, 'wb') as f:
            f.write(txt)
            f.close()
    except IOError as err:
        raise
    time.sleep(0.1) # let the drive finished
    videoFile = avsFile + encoding_args[-1]
    trimList.append(('', clip, 'video = %s\naudio = %s\n%s = audioDub(video, audio)\n' % (vSourceFilter % videoFile, aSourceFilter % videoFile, clip)))
    if useThreads:
        # check every two seconds if a thread finished and force the next loop,
        # so max_encoding_threads always should be running
        while len(threadList) >= max_encoding_threads and not encoding_errors:
            for x in xrange(len(threadList)):
                threadList[x].join(2)
                if not threadList[x].isAlive() or encoding_errors:
                    del threadList[x]
                    break
        if not encoding_errors:
            threadList.append(RunnThread(avsFile, videoFile))
    elif not encoding_errors:
        encodeAvs(avsFile, videoFile, not allEncodingsAtOnce)
    if encoding_errors:
        break
    i += 1

if encoding_errors:
    avsp.MsgBox(_('Last encoding returns error. Process is canceled\n') + encoding_errors)
    return

# wait for the last threads
if threadList:
    for thread in threadList:
        thread.join()

# there may also be errors in the last run       
if encoding_errors:
    avsp.MsgBox(_('Last encoding returns error. Process is canceled\n') + encoding_errors)
    return

# insert the trims
if insertTrims and trimList:
    sourceTxt = '\n# preview encodings\n'
    if insertSelectionsAsTrims and len(selTrims) > 2:
        sourceTxt += selTrims[:-2] + '\n'
    if convertToScriptColorSpace:
        sourceTxt += 'pt=BuildPixelType(sample_clip=last)\n'
        # then copy only the audio conversion from the template if it exists
        i = convert_txt.find('ConvertAudio')
        trimTxt = convert_txt[i:] if i > -1 else ''
    else:
        trimTxt = convert_txt

    for trim, clip, source in trimList:
        if source:
           sourceTxt += source
        if clip:
            trimTxt += clip + '++'
        elif trim:
            trimTxt += trim + '++'

    sourceTxt += trimTxt
    #~ok = False
    try:
        """ # was for macro thread, but macro thread causes problems if a dialog pops up
        for i in xrange(self.scriptNotebook.GetPageCount()):
            if script == self.scriptNotebook.GetPage(i):
                script.InsertText(script.GetLength(), sourceTxt[:-2])
                ok = True
                break
        if not ok: raise
        """
        script.InsertText(script.GetLength(), sourceTxt[:-2])
    except:
        avsp.MsgBox(_('Error, cannot insert the encode preview text\nTrying to create new tab')) # Should never be
        try:
            self.NewTab(text=saveScriptTxt + '\n' + sourceTxt[:-2])
        except:
            pass

if not allEncodingsAtOnce:
    self.Raise()
    t = time.strftime("%Hh : %Mm : %Ss", time.gmtime(time.time() - start_time))
    avsp.MsgBox(_('Encoding finished\nElapsed time: %s') % (t))