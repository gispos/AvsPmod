#-------------------------------------------------------------------------------
# Name:        PreviewEncodeThread.py forked from PreviewEncode.py
# Purpose:     AvsPmod timeline (selections) preview encoding with ffmpeg.exe
#              Encodes the selection(s) and insert the clips and trims into the script.
#              The purpose is a quick preview for the selected areas, but if also useful for other purpose.
#              Several encodings running at the same time possible.
#
#              Preview filters cannot be adopted.
#              And it is also assumed that an audio is included in the video
#
#              Use the Trim Editor to create selections. Select 'Copy to clipboard' and hit OK
#              Or select a line with trims and run the macro.
#              Coded files are always overwritten without any sorting order! (if the script name the same)
#
#              Save this file (text) as PreviewEncodeThread.py in the AvsPmod macro or a macro subfolder
#
# Author:      GPo
#
# Created:     24.05.2021,
#              update 09.06.2021
#                   showDialog, save and read options, encode selected trims (see encodeSelectedTrims)
#                       and notice video slider context menu 'Create trim' (the trims are sorted before encoding)
#                   encoding file names changed (for better sort handling with win explorer)
#                   removed last char '\n' from the convert templates
#                   add text line with the encoded clips, for playback with another app
#              update 12.06.2021
#                   message shows total file size and free disk space
#              update 14.06.2021
#                   search for "return" in the script
#              update 03.09.2022
#                   Added wx.GetApp().ProcessIdle() after updating the script so that the progress dialog can be closed.
#                   New variante PreviewEncodeThread.py:
#                        The whole script runs in one thread, AvsPmod is not blocked, only the processed script is blocked
#                   if I messed up run PreviewEncode.py
#
# Copyright:   (c) GPo 2021
# Licence:     <free>
#-------------------------------------------------------------------------------

import os
import sys
import subprocess
import threading
import time
import ctypes
import wx
import avsp as _avsp

self = avsp.GetWindow()
locals_ignor = [k for k, v in locals().items()]
locals_ignor += ['v', 'k', 'locals_ignor']

################################################################################
## templates and user settings
################################################################################

##### Encoder profile
# In the event of audio problems, the audio must be changed from 'copy' to a conversion format
# and the templates must be adapted (see dnxhd profile) For my videos it works with 'copy'
# If you don't want all templates to be displayed in the dialog, put a # at the beginning
# You can add or rename the templates (names without spaces)
dnxhr_hq = '-c:v dnxhd -profile:v dnxhr_hq -vf format=yuv422p -c:a pcm_s16le .mov'
dnxhr_hqx = '-c:v dnxhd -profile:v dnxhr_hqx -vf format=yuv422p10le -c:a pcm_s16le .mov'
dnxhr_444 = '-c:v dnxhd -profile:v dnxhr_444 -vf format=yuv444p10le -c:a pcm_s16le .mov'
x264_lossless_8 = '-c:v libx264 -preset ultrafast -qp 0 -vf format=yuv420p -c:a copy .mkv'
x264_lossless_422 = '-c:v libx264 -preset ultrafast -qp 0 -vf format=yuv422p10le -c:a copy .mkv'
x264_lossless_422_sar43 = '-c:v libx264 -preset ultrafast -qp 0 -vf format=yuv422p10le -vf setsar=sar=1.0667/1 -c:a copy .mkv'
x264_lossless_444 = '-c:v libx264 -preset ultrafast -qp 0 -vf format=yuv444p10le -c:a copy .mkv'
x264_nvenc_vbr_8 = '-c:v h264_nvenc -preset p7 -profile:v main -rc vbr -b:v 8000k -c:a aac -b:a 256k .mkv'
x264_nvenc_vbr_422 = '-c:v h264_nvenc -preset P7 -profile:v main -rc vbr -b:v 18000k -c:a aac -b:a 256k .mkv'
x264_nvenc_lossless = '-c:v hevc_nvenc -preset lossless -c:a copy .mkv'
huffyuv_8 = '-c:v huffyuv -vf format=yuv422p -c:a copy .mkv'
ffvhuff = '-c:v ffvhuff -c:a copy .mkv'
FFV1 = '-c:v ffv1 -level 3 -threads 4 -g 1 -coder 1 -context 1 -slices 24 -slicecrc 1 -c:a copy .mkv'
# encoder profile for low file size
x264_8_crf16_aac = '-c:v libx264 -preset fast -tune film -crf 16 -vf format=yuv420p -c:a aac -b:a 256k .mkv'
x264_422_crf16_aac = '-c:v libx264 -preset fast -tune film -crf 16 -vf format=yuv422p10le -c:a aac -b:a 256k .mkv'

##### Convert templates
# converts the script clip to encoder profile, some audio conversions still missing e.g. channels
# if convertToScriptColorSpace = True, only the ConvertAudio section is used
conv_dnxhr_hq = 'ConvertBits(bits=8).ConvertToYUV422(matrix="Rec709").ConvertAudioTo16bit().AssumeSampleRate(48000)'
conv_dnxhr_hqx = 'ConvertBits(bits=10).ConvertToYUV422(matrix="Rec709").ConvertAudioTo16bit().AssumeSampleRate(48000)'
conv_dnxhr_444 = 'ConvertBits(bits=10).ConvertToYUV444(matrix="Rec709").ConvertAudioTo16bit().AssumeSampleRate(48000)'
conv_x264_lossless_8 = 'ConvertBits(bits=8).ConvertToYUV420(matrix="Rec709")'
conv_x264_lossless_422 = 'ConvertBits(bits=10).ConvertToYUV422(matrix="Rec709")'
conv_x264_lossless_444 = 'ConvertBits(bits=10).ConvertToYUV444(matrix="Rec709")'
conv_x264_nvenc_vbr_8 = conv_x264_lossless_8
conv_x264_nvenc_vbr_422 = conv_x264_lossless_422
conv_x264_nvenc_lossless = ''
conv_huffyuv_8 = 'ConvertBits(bits=8).ConvertToYUV422(matrix="Rec709")'
conv_ffvhuff = ''
conv_FFV1 = ''
# profile for low file size
conv_x264_8_crf16_aac = conv_x264_lossless_8
conv_x264_422_crf16_aac = conv_x264_lossless_422

# Do not change! Convert the templates var names to string. Best place is after the tamplates
local_names = [k for k, v in locals().items()]
enc_templates_names = [v for v in local_names if not v.startswith('conv_') and not v in locals_ignor]
conv_templates_names = [v for v in local_names if v.startswith('conv_')]

##### User Settings
# convert the encoded clips to the script colorspace  ( vSourceFilterEx must be used )
# otherwise the script will be converted, try what is better
convertToScriptColorSpace = True

# you can change the source filter ("%s" stands for the file name), but it should be frame accurate
vSourceFilter = 'LWLibavVideoSource("%s", cache=False)'
aSourceFilter = 'LWLibavAudioSource("%s", cache=False)'
vSourceFilterEx = 'LWLibavVideoSource("%s", cache=False, format=pt)'

# set the encoding profile and convert template, default ffvhuff, is ignored if showDialog = True
encoding_args = ffvhuff
convert_txt = conv_ffvhuff

# use ffvhuff if bit count <= 8 else dnxhr_444 (you can change the templates, search for 'if codecAutoSelect')
# is ignored if showDialog = True
codecAutoSelect = True

# change the save path for the encoded files or use the script dir if it exists (script saved)
# if useScriptDir, savePath is ignored
savePath = 'C:\\Temp'
useScriptDir = False

# if True and showDialog = False, a path selection dialog is displayed
promptForDir = False

# if true, a options dialog is shown and promptForDir and codecAutoSelect is ignored
showDialog = True

# change the ffmpeg.exe path e.g. 'D:\\tools\\ffmpeg\\ffmpeg.exe', default ..AvsPmod\\encoders\\ffmpeg.exe
ffmpeg = os.path.join(self.programdir, 'encoders\\ffmpeg.exe')

# limit the encodings count to max_files, -1 disabled
max_files = -1

# if True and a line with trims e.g. trim(0, 50)++trim(100, 200) is selected in the script, only this trims will be encode
encodeSelectedTrims = True

# if disabled, no text will insert in the script, only avs files created and encoding runs
insertTrims = True

# if insertTrims, insert also the selections as trim text and the clips text
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
## end user settings
################################################################################

selectedText = avsp.GetSelectedText()

if not os.path.isfile(ffmpeg):
    avsp.MsgBox('ffmpeg not found.\nYou must change the "ffmpeg" variable in the macro.\n\n' + ffmpeg)
    return

# dialog
if showDialog:
    last_enc = 'ffvhuff' # on the first run of the dialog (options are empty)
    # read the macro options
    last_enc = avsp.Options.get('enc_template', last_enc)
    max_encoding_threads = avsp.Options.get('max_enc_threads', max_encoding_threads)
    insertTrims = avsp.Options.get('inserttrims', insertTrims)
    useScriptDir = avsp.Options.get('usescriptdir', useScriptDir)
    convertToScriptColorSpace = avsp.Options.get('convertscriptcolorspace', convertToScriptColorSpace)
    savePath = avsp.Options.get('savepath', savePath)

    enc_templates_names.sort()
    conv_templates_names.sort()
    enc_templates_names.append((last_enc)) # default or last used

    # create the dialog
    labels = [[_('Template:'), _('Encode threads:')] ,[_('Convert to script color space'), _('Insert trims into script')], [_('Use script dir')], [_('Select save path:')]]
    defaults = [[enc_templates_names, (max_encoding_threads, 1,10)], [convertToScriptColorSpace, insertTrims], [useScriptDir], [savePath]]
    types = [['list_read_only', 'spin'], ['check', 'check'], ['check'], ['dir']]
    entries = avsp.GetTextEntry(labels, defaults, _('Encode options'), types)
    if not entries:
        return
    enc_template_name, max_encoding_threads, convertToScriptColorSpace, insertTrims, useScriptDir, savePath = entries

    # search for the convert template
    conv_temp = ''
    conv_name = 'conv_' + enc_template_name
    for name in conv_templates_names:
        if name == conv_name:
            conv_temp = name
            break
    if not conv_temp: # no convert template found
        if not avsp.MsgBox('Conversion template not found: %s\nContinue?' % conv_name, cancel=True):
            return
        convert_txt = ''
    else:
        convert_txt = locals()[conv_temp]
    # get the enc variable content from the variable name
    encoding_args = locals()[enc_template_name]
    # save the options in the macro options (macro.dat)
    avsp.Options['enc_template'] = enc_template_name
    avsp.Options['max_enc_threads'] = max_encoding_threads
    avsp.Options['inserttrims'] = insertTrims
    avsp.Options['usescriptdir'] = useScriptDir
    avsp.Options['convertscriptcolorspace'] = convertToScriptColorSpace
    avsp.Options['savepath'] = savePath
    prompForDir = False
    codecAutoSelect = False

script = self.currentScript
script_idx = self.scriptNotebook.GetSelection()
saveScriptTxt = script.GetText().strip()
global encoding_errors
global encoding_file_size

# if "return" is found in the script (that happens to me every now and then)
pos = saveScriptTxt.lower().find('return ')
if pos > 1 and saveScriptTxt[pos-2:pos].find('#') == -1:
    if not avsp.MsgBox('Found "return" in the script.\nThis can make the selected areas invalid. Keep going?', cancel=True):
        return

if self.UpdateScriptAVI() is None or not self.previewOK(script):
    avsp.MsgBox('Script not initialized.')
    return

if self.UseAviThread:
    wx.GetApp().ProcessIdle()

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

# input in Byte
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

def getFreeSpace(path):
    if os.name != 'nt':
        return -1
    free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(path), None, None, ctypes.pointer(free_bytes))
    return free_bytes.value

def GetScriptFileName(default):
    if script.filename:
        base = os.path.split(script.filename)[1]
        return os.path.splitext(base)[0]
    return default

def SelectionsFromTrims(txt):
    txt = txt.lower()
    L = len('trim(')
    x2 = 0
    error = False
    selList = []
    while 1 and not error:
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
                        selList.append((int(start), int(stop)))
                    else: error = True
                else: error = True
            else: error = True
        else: break
    if error:
        avsp.MsgBox('Trim read error\nCheck the selected trims')
        return None
    if len(selList) > 1:
        selList.sort(key=lambda x: x[0]) # sort the trims
    return selList

def encodeAvs(infile, outfile, single=True):
    global encoding_errors
    global encoding_file_size
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
        elif os.path.isfile(outfile):
            encoding_file_size += os.path.getsize(outfile)
    else:
       # multi encoding AvsPmod is not blocked (encoding CPU usage can be 100%)
       # Only initialize the script again when all encodings are finished!
       subprocess.Popen(args)

# thread for eache encoding
def RunnThread(avsFile, videoFile):
    thread = threading.Thread(target=encodeAvs, args=(avsFile, videoFile, True,), name='MacroThread')
    thread.daemon = True
    thread.start()
    return thread

# get the selections
selections = None
if encodeSelectedTrims and selectedText:
    selections = SelectionsFromTrims(selectedText)
    if selections is None: # then error while reading the trims
        return
if not selections:
    selections = self.GetSliderSelections()
    if not selections:
        avsp.MsgBox(_('You must first create selections'))
        return

# we must release the encoded video files or ffmpeg cannot create the new files
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

if stop < frameCount-1:
    encodings.append((0, 'Trim(%d, %d)' % (stop+1, 0)))

# the main encoding thread
def StartEncodings(scriptTxt, encodings, vSourceFilter, aSourceFilter, allEncodingsAtOnce, max_encoding_threads, useThreads):
    global encoding_errors
    global encoding_file_size
    thread_error = False
    trimList = []
    selTrims = ''
    selClips = ''
    i = 0
    threadList = []
    try:
        try:
            for typ, line in encodings:
                if typ == 0:
                    trimList.append((line, '', ''))
                    continue
                txt = scriptTxt + line
                txt = _avsp.AsyncCall(self.GetEncodedText, txt, bom=True).Wait()
                clip = 'enc%d' % (i)
                selTrims += line + '++'
                selClips += clip + '++'
                videoFile = os.path.join(savePath, '%s_%s%s' % (GetScriptFileName('tab_%i' % script_idx), clip, encoding_args[-1]))
                avsFile = videoFile + '.avs'
                try:
                    with open(avsFile, 'wb') as f:
                        f.write(txt)
                        f.close()
                except IOError as err:
                    raise
                time.sleep(0.1) # let the drive finished
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
        except:
            thread_error = True
    finally:
        # wait for the last threads
        if threadList:
            for thread in threadList:
                thread.join()
        _avsp.AsyncCall(Finish, trimList, selTrims, selClips, thread_error)
        #wx.CallAfter(Finish, trimList, selTrims, selClips)


encoding_errors = ''
encoding_file_size = 0
scriptTxt = self.getCleanText(saveScriptTxt)
scriptTxt = self.stripComment_2(scriptTxt)  + '\n'
if allEncodingsAtOnce:
    useThreads = False
if convertToScriptColorSpace:
    vSourceFilter = vSourceFilterEx

start_time = time.time()

# start the main encoding thread
thread = threading.Thread(target=StartEncodings, args=(scriptTxt, encodings, vSourceFilter, aSourceFilter,
                          allEncodingsAtOnce, max_encoding_threads, useThreads, ), name='MacroThread')
thread.daemon = True
thread.start()
script.AviThread = thread

# encoding thread finished, call this
def Finish(trimList, selTrims, selClips, thread_error):
    global encoding_errors
    global encoding_file_size

    self.StopPlayback()

    try:
        script.AviThread = None
    except:
        pass

    if thread_error:
        avsp.MsgBox(_('Unknown thread error. Process is canceled\n'))
        return

    if encoding_errors:
        avsp.MsgBox(_('Last encoding returns error. Process is canceled\n') + encoding_errors)
        return

    # insert the trims
    if insertTrims and trimList:
        sourceTxt = '\n\n# preview encodings\n'
        if insertSelectionsAsTrims:
            if selTrims:
                sourceTxt += '#encode: %s\n' % selTrims[:-2]
            if selClips:
                selClips = '#%s\n' % selClips[:-2]
        else:
            selClips = ''
        if convertToScriptColorSpace:
            sourceTxt += 'pt=BuildPixelType(sample_clip=last)\n'
            # then copy only the audio conversion from the template if it exists
            i = convert_txt.find('ConvertAudio')
            trimTxt = convert_txt[i:] + '\n' if i > -1 else ''
        else:
            trimTxt = convert_txt + '\n' if convert_txt else ''

        for trim, clip, source in trimList:
            if source:
               sourceTxt += source
            if clip:
                trimTxt += clip + '++'
            elif trim:
                trimTxt += trim + '++'

        sourceTxt += selClips + trimTxt
        ok = False
        try:
            for i in xrange(self.scriptNotebook.GetPageCount()):
                if script is self.scriptNotebook.GetPage(i):
                    self.HidePreviewWindow()
                    x = script.GetLineCount() - 1
                    while x > 1 and not script.GetLine(x).strip():
                        x -= 1
                    script.InsertText(script.GetLineEndPosition(x), sourceTxt[:-2])
                    self.scriptNotebook.SetSelection(i)
                    ok = True
                    break
            if not ok: raise
        except:
            avsp.MsgBox(_('Error, cannot insert the encode preview text\nTrying to create new tab'))
            try:
                self.NewTab(text=saveScriptTxt + '\n' + sourceTxt[:-2])
            except:
                wx.Bell()
                avsp.MsgBox(_('Error, cannot create new tab'))

    if not allEncodingsAtOnce:
        t = time.strftime("%Hh : %Mm : %Ss", time.gmtime(time.time() - start_time))
        fSize = 'Total file size: %s' % fileSizeToString(encoding_file_size)
        freeSpace = getFreeSpace(savePath[0:2]+'\\')
        diskFree = '\nDisk free space: %s' % fileSizeToString(freeSpace) if freeSpace > 0 else ''
        self.Raise()
        avsp.MsgBox(_('Encoding finished\n\nElapsed time: %s\n%s%s') % (t, fSize, diskFree))