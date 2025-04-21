# cfunc

import pyavs
import sys
import numpy

x86_64 = sys.maxsize > 2**32
if x86_64:
    import avisynth_cffi as avisynth
else:
    import avisynth

def CreateFastClip(self, scripttxt, useSplitClip, previewFilter, matrix, readmatrix, interlaced, swapuv, bit_depth):
    return None

def CheckSplitClip(self, script, filename):
    try:
        self.main_clip = self.env.invoke('Eval', [script, filename])
    except avisynth.AvisynthError as err:
        return err

def CreateFilterClip(self, f_args='', fast_display_clip=False, update_yv12clip=False):
    self.preview_filter = None
    return None, ''

def KillFilterClip(self, createDisplayClip=True):
    self.preview_filter = None
    if not self.initialized:
        return
    if createDisplayClip:
        self.CreateDisplayClip(self.matrix, self.interlaced, self.swapuv, self.bit_depth)

def MixAudioToStereo(audio_buffer, chn, dtype, cdb=0.7, db=1.0):
    # L R C Lfe Ls Rs. (SMPTE order)
    buf = numpy.frombuffer(audio_buffer, dtype=dtype)
    c = buf.reshape(chn, len(buf)/chn, order='FORTRAN')
    if chn == 2:
        left = (c[0]*db).astype(dtype)
        right = (c[1]*db).astype(dtype)
    elif chn >= 8:
        left = ((c[0]*0.7 + c[4]*0.2 + c[6]*0.1 + c[2]*0.7*cdb)*db).astype(dtype)
        right = ((c[1]*0.7 + c[5]*0.2 + c[7]*0.1 + c[2]*0.7*cdb)*db).astype(dtype)
    elif chn >= 6:
        left = ((c[0]*0.7 + c[4]*0.3 + c[2]*0.7*cdb)*db).astype(dtype)
        right = ((c[1]*0.7 + c[5]*0.3 + c[2]*0.7*cdb)*db).astype(dtype)
    elif chn >= 4:
        left = ((c[0]*0.7 + c[2]*0.3)*db).astype(dtype)
        right = ((c[1]*0.7 + c[3]*0.3)*db).astype(dtype)
    elif chn == 3:
        left = ((c[0]*0.7 + c[2]*cdb)*db).astype(dtype)
        right = ((c[1]*0.7 + c[2]*cdb)*db).astype(dtype)
    else:
        left = (c[0]*db).astype(dtype)
        right = (c[0]*db).astype(dtype)
    return numpy.dstack((left, right)).tobytes()

def MixAudio1(audio_buffer, chn, dtype, cdb=0.7, db=1.0):
    buf = numpy.frombuffer(audio_buffer, dtype=dtype)
    left = (buf*db).astype(dtype)
    right = (buf*db).astype(dtype)
    return numpy.dstack((left, right)).tobytes()

def MixAudio2(audio_buffer, chn, dtype, cdb=0.7, db=1.0):
    if db == 1: return audio_buffer
    buf = numpy.frombuffer(audio_buffer, dtype=dtype)
    c = buf.reshape(chn, len(buf)/chn, order='FORTRAN')
    left = (c[0]*db).astype(dtype)
    right = (c[1]*db).astype(dtype)
    return numpy.dstack((left, right)).tobytes()

def MixAudio3(audio_buffer, chn, dtype, cdb=0.7, db=1.0):
    buf = numpy.frombuffer(audio_buffer, dtype=dtype)
    c = buf.reshape(chn, len(buf)/chn, order='FORTRAN')
    left = ((c[0]*0.7 + c[2]*cdb)*db).astype(dtype)
    right = ((c[1]*0.7 + c[2]*cdb)*db).astype(dtype)
    return numpy.dstack((left, right)).tobytes()

def MixAudio4(audio_buffer, chn, dtype, cdb=0.7, db=1.0):
    buf = numpy.frombuffer(audio_buffer, dtype=dtype)
    c = buf.reshape(chn, len(buf)/chn, order='FORTRAN')
    left = ((c[0]*0.7 + c[2]*0.3)*db).astype(dtype)
    right = ((c[1]*0.7 + c[3]*0.3)*db).astype(dtype)
    return numpy.dstack((left, right)).tobytes()

def MixAudio6(audio_buffer, chn, dtype, cdb=0.7, db=1.0):
    buf = numpy.frombuffer(audio_buffer, dtype=dtype)
    c = buf.reshape(chn, len(buf)/chn, order='FORTRAN')
    left = ((c[0]*0.7 + c[4]*0.3 + c[2]*0.7*cdb)*db).astype(dtype)
    right = ((c[1]*0.7 + c[5]*0.3 + c[2]*0.7*cdb)*db).astype(dtype)
    return numpy.dstack((left, right)).tobytes()

def MixAudio8(audio_buffer, chn, dtype, cdb=0.7, db=1.0):
    buf = numpy.frombuffer(audio_buffer, dtype=dtype)
    c = buf.reshape(chn, len(buf)/chn, order='FORTRAN')
    left = ((c[0]*0.7 + c[4]*0.2 + c[6]*0.1 + c[2]*0.7*cdb)*db).astype(dtype)
    right = ((c[1]*0.7 + c[5]*0.2 + c[7]*0.1 + c[2]*0.7*cdb)*db).astype(dtype)
    return numpy.dstack((left, right)).tobytes()

# Experimental
def LocateFrame(self, start=-500, stop=500, framenr=None, thresh=None, target_src='', target_clip=None):
    re = [-1, '', '']
    return re

