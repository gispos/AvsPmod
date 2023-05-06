# avisynth - Python AviSynth/AvxSynth wrapper
#
# Copyright 2007 Peter Jang <http://avisynth.nl/users/qwerpoi>
#           2010-2017 the AvsPmod authors <https://github.com/avspmod/avspmod>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA, or visit
#  http://www.gnu.org/copyleft/gpl.html .

# Dependencies:
#     Python (tested on v2.6 and v2.7)
# Optional:
#     global_vars.py (for specifying a custom shared library location)
#
# Notes:
#
# This bindings are NOT compatible with x86-64
# See <http://bugs.python.org/issue16575>


import ctypes
import sys
import os
import os.path
import traceback
import collections
import weakref
#import wx
import func

# Initialization routines.  Assume AvxSynth/Linux if os.name is not NT.
try:
    import global_vars
    directory = global_vars.avisynth_library_dir
except:
    directory = ''
if os.name == 'nt':
    if __debug__:
        if directory:
            print('Using a custom AviSynth directory:', directory)
        else:
            print('Using AviSynth from PATH')
    path = os.path.join(directory, 'avisynth.dll')
    if isinstance(path, unicode): # fix for https://bugs.python.org/issue29082
        path = path.encode('mbcs')
    avidll = ctypes.WinDLL(path)
    FUNCTYPE = ctypes.WINFUNCTYPE
else:
    if __debug__:
        if directory:
            print('Using a custom AvxSynth directory:', directory)
        else:
            print('Using AvxSynth from LD_LIBRARY_PATH')
    path = os.path.join(directory, 'libavxsynth.so')
    if not os.path.isfile(path):
        path = os.path.join(directory, 'libavisynth.so')
    avidll = ctypes.CDLL(path)
    FUNCTYPE = ctypes.CFUNCTYPE


encoding = sys.getfilesystemencoding()

weak_dict = weakref.WeakKeyDictionary()

propCharDict = {
    '_Matrix': func.GetMatrixName,
    '_Primaries': func.GetColorPrimariesName,
    '_ChromaLocation': func.GetChromaLocationName,
    '_FieldBased': func.GetFieldBasedName,
    '_Transfer': func.GetTransferName,
    '_ColorRange': func.GetColorRangeName,
    '_GOPClosed': func.GetGOPClosedName,
}

# Interface: 3 + 5's new colorspaces and some of its other additions
# Interface: 6 and Avisynth+ additions PF 2018dec


# can't access define, enums or inline functions from ctypes

# in avisynth.cffi_all enums and consts from avisynth_c.h are ...
# so in avs class we should define them in the same way as in avisynth_h.c
# these constants can be accessed from avisynth.py with avs. prefix.
# e.g. avisynth_c.h defined AVS_PLANAR_U as
#   AVS_PLANAR_U=1<<1
# in avisynth_cffi.py it should be declared as
#   AVS_PLANAR_U = ..., // 1<<1,
# Here in avisynth.py the constants are accessed as avs.XXXXX e.g. avs.AVS_PLANAR_U, example: if plane in (avs.AVS_PLANAR_U, avs.AVS_PLANAR_V):
# From pyavs.py constants can be accessed as avisynth.avs.XXXXX, e.g. avisynth.avs.AVS_PLANAR_U

class avs(): # lowercase for compatibility with the cffi bindings

    # Constants
    AVS_SAMPLE_INT8  = 1 << 0
    AVS_SAMPLE_INT16 = 1 << 1
    AVS_SAMPLE_INT24 = 1 << 2
    AVS_SAMPLE_INT32 = 1 << 3
    AVS_SAMPLE_FLOAT = 1 << 4

    AVS_PLANAR_Y = 1 << 0
    AVS_PLANAR_U = 1 << 1
    AVS_PLANAR_V = 1 << 2
    AVS_PLANAR_ALIGNED = 1 << 3
    AVS_PLANAR_Y_ALIGNED = AVS_PLANAR_Y | AVS_PLANAR_ALIGNED
    AVS_PLANAR_U_ALIGNED = AVS_PLANAR_U | AVS_PLANAR_ALIGNED
    AVS_PLANAR_V_ALIGNED = AVS_PLANAR_V | AVS_PLANAR_ALIGNED
    AVS_PLANAR_A = 1 << 4
    AVS_PLANAR_R = 1 << 5
    AVS_PLANAR_G = 1 << 6
    AVS_PLANAR_B = 1 << 7
    AVS_PLANAR_A_ALIGNED = AVS_PLANAR_A | AVS_PLANAR_ALIGNED
    AVS_PLANAR_R_ALIGNED = AVS_PLANAR_R | AVS_PLANAR_ALIGNED
    AVS_PLANAR_G_ALIGNED = AVS_PLANAR_G | AVS_PLANAR_ALIGNED
    AVS_PLANAR_B_ALIGNED = AVS_PLANAR_B | AVS_PLANAR_ALIGNED

    # Colorspace properties
    AVS_CS_YUVA = 1 << 27
    AVS_CS_BGR = 1 << 28
    AVS_CS_YUV = 1 << 29
    AVS_CS_INTERLEAVED = 1 << 30
    AVS_CS_PLANAR = 1 << 31

    AVS_CS_SHIFT_SUB_WIDTH = 0
    AVS_CS_SHIFT_SUB_HEIGHT = 8
    AVS_CS_SHIFT_SAMPLE_BITS = 16

    AVS_CS_SUB_WIDTH_MASK = 7 << AVS_CS_SHIFT_SUB_WIDTH
    AVS_CS_SUB_WIDTH_1 = 3 << AVS_CS_SHIFT_SUB_WIDTH # YV24
    AVS_CS_SUB_WIDTH_2 = 0 << AVS_CS_SHIFT_SUB_WIDTH # YV12, I420, YV16
    AVS_CS_SUB_WIDTH_4 = 1 << AVS_CS_SHIFT_SUB_WIDTH # YUV9, YV411

    AVS_CS_VPLANEFIRST = 1 << 3 # YV12, YV16, YV24, YV411, YUV9
    AVS_CS_UPLANEFIRST = 1 << 4 # I420

    AVS_CS_SUB_HEIGHT_MASK = 7 << AVS_CS_SHIFT_SUB_HEIGHT
    AVS_CS_SUB_HEIGHT_1 = 3 << AVS_CS_SHIFT_SUB_HEIGHT # YV16, YV24, YV411
    AVS_CS_SUB_HEIGHT_2 = 0 << AVS_CS_SHIFT_SUB_HEIGHT # YV12, I420
    AVS_CS_SUB_HEIGHT_4 = 1 << AVS_CS_SHIFT_SUB_HEIGHT # YUV9

    AVS_CS_SAMPLE_BITS_MASK = 7 << AVS_CS_SHIFT_SAMPLE_BITS
    AVS_CS_SAMPLE_BITS_8 = 0 << AVS_CS_SHIFT_SAMPLE_BITS
    AVS_CS_SAMPLE_BITS_10 = 5 << AVS_CS_SHIFT_SAMPLE_BITS
    AVS_CS_SAMPLE_BITS_12 = 6 << AVS_CS_SHIFT_SAMPLE_BITS
    AVS_CS_SAMPLE_BITS_14 = 7 << AVS_CS_SHIFT_SAMPLE_BITS
    AVS_CS_SAMPLE_BITS_16 = 1 << AVS_CS_SHIFT_SAMPLE_BITS
    AVS_CS_SAMPLE_BITS_32 = 2 << AVS_CS_SHIFT_SAMPLE_BITS

    AVS_CS_PLANAR_MASK = AVS_CS_PLANAR | AVS_CS_INTERLEAVED | AVS_CS_YUV | \
                         AVS_CS_BGR | AVS_CS_YUVA | AVS_CS_SAMPLE_BITS_MASK | \
                         AVS_CS_SUB_HEIGHT_MASK | AVS_CS_SUB_WIDTH_MASK
    AVS_CS_PLANAR_FILTER = ~(AVS_CS_VPLANEFIRST | AVS_CS_UPLANEFIRST)

    AVS_CS_RGB_TYPE  = 1 << 0
    AVS_CS_RGBA_TYPE = 1 << 1

    AVS_CS_GENERIC_YUV420  = AVS_CS_PLANAR | AVS_CS_YUV | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_2 | AVS_CS_SUB_WIDTH_2 # 4:2:0 planar
    AVS_CS_GENERIC_YUV422  = AVS_CS_PLANAR | AVS_CS_YUV | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_1 | AVS_CS_SUB_WIDTH_2 # 4:2:2 planar
    AVS_CS_GENERIC_YUV444  = AVS_CS_PLANAR | AVS_CS_YUV | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_1 | AVS_CS_SUB_WIDTH_1 #  4:4:4 planar
    AVS_CS_GENERIC_Y       = AVS_CS_PLANAR | AVS_CS_INTERLEAVED | AVS_CS_YUV                                             # Y only (4:0:0)
    AVS_CS_GENERIC_RGBP    = AVS_CS_PLANAR | AVS_CS_BGR | AVS_CS_RGB_TYPE                                                # planar RGB
    AVS_CS_GENERIC_RGBAP   = AVS_CS_PLANAR | AVS_CS_BGR | AVS_CS_RGBA_TYPE                                               # planar RGBA
    AVS_CS_GENERIC_YUVA420 = AVS_CS_PLANAR | AVS_CS_YUVA | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_2 | AVS_CS_SUB_WIDTH_2 # 4:2:0:A planar
    AVS_CS_GENERIC_YUVA422 = AVS_CS_PLANAR | AVS_CS_YUVA | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_1 | AVS_CS_SUB_WIDTH_2 # 4:2:2:A planar
    AVS_CS_GENERIC_YUVA444 = AVS_CS_PLANAR | AVS_CS_YUVA | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_1 | AVS_CS_SUB_WIDTH_1 # 4:4:4:A planar
    #--------------------------------

    # Specific colorformats
    AVS_CS_UNKNOWN = 0
    AVS_CS_BGR24 = AVS_CS_RGB_TYPE  | AVS_CS_BGR | AVS_CS_INTERLEAVED
    AVS_CS_BGR32 = AVS_CS_RGBA_TYPE | AVS_CS_BGR | AVS_CS_INTERLEAVED
    AVS_CS_YUY2 = 1<<2 | AVS_CS_YUV | AVS_CS_INTERLEAVED
    #  AVS_CS_YV12  = 1<<3  Reserved
    #  AVS_CS_I420  = 1<<4  Reserved
    AVS_CS_RAW32 = 1<<5 | AVS_CS_INTERLEAVED

    AVS_CS_YV24  = AVS_CS_GENERIC_YUV444 | AVS_CS_SAMPLE_BITS_8 # YVU 4:4:4 planar
    AVS_CS_YV16  = AVS_CS_GENERIC_YUV422 | AVS_CS_SAMPLE_BITS_8 # YVU 4:2:2 planar
    AVS_CS_YV12  = AVS_CS_GENERIC_YUV420 | AVS_CS_SAMPLE_BITS_8 # YVU 4:2:0 planar
    AVS_CS_I420  = AVS_CS_PLANAR | AVS_CS_YUV | AVS_CS_SAMPLE_BITS_8 | AVS_CS_UPLANEFIRST | AVS_CS_SUB_HEIGHT_2 | AVS_CS_SUB_WIDTH_2 # YUV 4:2:0 planar
    AVS_CS_IYUV  = AVS_CS_I420
    AVS_CS_YV411 = AVS_CS_PLANAR | AVS_CS_YUV | AVS_CS_SAMPLE_BITS_8 | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_1 | AVS_CS_SUB_WIDTH_4 # YVU 4:1:1 planar
    AVS_CS_YUV9  = AVS_CS_PLANAR | AVS_CS_YUV | AVS_CS_SAMPLE_BITS_8 | AVS_CS_VPLANEFIRST | AVS_CS_SUB_HEIGHT_4 | AVS_CS_SUB_WIDTH_4 # YVU 4:1:0 planar
    AVS_CS_Y8    = AVS_CS_GENERIC_Y | AVS_CS_SAMPLE_BITS_8 # Y 4:0:0 planar

    # 10-12-14-16 bit + planar RGB + BRG48/64
    AVS_CS_YUV444P10 = AVS_CS_GENERIC_YUV444 | AVS_CS_SAMPLE_BITS_10 # YUV 4:4:4 10bit samples
    AVS_CS_YUV422P10 = AVS_CS_GENERIC_YUV422 | AVS_CS_SAMPLE_BITS_10 # YUV 4:2:2 10bit samples
    AVS_CS_YUV420P10 = AVS_CS_GENERIC_YUV420 | AVS_CS_SAMPLE_BITS_10 # YUV 4:2:0 10bit samples
    AVS_CS_Y10       = AVS_CS_GENERIC_Y | AVS_CS_SAMPLE_BITS_10 # Y 4:0:0 10bit samples

    AVS_CS_YUV444P12 = AVS_CS_GENERIC_YUV444 | AVS_CS_SAMPLE_BITS_12 # YUV 4:4:4 12bit samples
    AVS_CS_YUV422P12 = AVS_CS_GENERIC_YUV422 | AVS_CS_SAMPLE_BITS_12 # YUV 4:2:2 12bit samples
    AVS_CS_YUV420P12 = AVS_CS_GENERIC_YUV420 | AVS_CS_SAMPLE_BITS_12 # YUV 4:2:0 12bit samples
    AVS_CS_Y12       = AVS_CS_GENERIC_Y | AVS_CS_SAMPLE_BITS_12 # Y 4:0:0 12bit samples

    AVS_CS_YUV444P14 = AVS_CS_GENERIC_YUV444 | AVS_CS_SAMPLE_BITS_14 # YUV 4:4:4 14bit samples
    AVS_CS_YUV422P14 = AVS_CS_GENERIC_YUV422 | AVS_CS_SAMPLE_BITS_14 # YUV 4:2:2 14bit samples
    AVS_CS_YUV420P14 = AVS_CS_GENERIC_YUV420 | AVS_CS_SAMPLE_BITS_14 # YUV 4:2:0 14bit samples
    AVS_CS_Y14       = AVS_CS_GENERIC_Y | AVS_CS_SAMPLE_BITS_14 # Y 4:0:0 14bit samples

    AVS_CS_YUV444P16 = AVS_CS_GENERIC_YUV444 | AVS_CS_SAMPLE_BITS_16 # YUV 4:4:4 16bit samples
    AVS_CS_YUV422P16 = AVS_CS_GENERIC_YUV422 | AVS_CS_SAMPLE_BITS_16 # YUV 4:2:2 16bit samples
    AVS_CS_YUV420P16 = AVS_CS_GENERIC_YUV420 | AVS_CS_SAMPLE_BITS_16 # YUV 4:2:0 16bit samples
    AVS_CS_Y16       = AVS_CS_GENERIC_Y | AVS_CS_SAMPLE_BITS_16 # Y 4:0:0 16bit samples

    # 32 bit samples (float)
    AVS_CS_YUV444PS = AVS_CS_GENERIC_YUV444 | AVS_CS_SAMPLE_BITS_32 # YUV 4:4:4 32bit samples
    AVS_CS_YUV422PS = AVS_CS_GENERIC_YUV422 | AVS_CS_SAMPLE_BITS_32 # YUV 4:2:2 32bit samples
    AVS_CS_YUV420PS = AVS_CS_GENERIC_YUV420 | AVS_CS_SAMPLE_BITS_32 # YUV 4:2:0 32bit samples
    AVS_CS_Y32      = AVS_CS_GENERIC_Y | AVS_CS_SAMPLE_BITS_32 # Y 4:0:0 32bit samples

    # RGB packed
    AVS_CS_BGR48 = AVS_CS_RGB_TYPE | AVS_CS_BGR | AVS_CS_INTERLEAVED | AVS_CS_SAMPLE_BITS_16 # BGR 3x16 bit
    AVS_CS_BGR64 = AVS_CS_RGBA_TYPE | AVS_CS_BGR | AVS_CS_INTERLEAVED | AVS_CS_SAMPLE_BITS_16 # BGR 4x16 bit
    # no packed 32 bit (float) support for these legacy types

    # RGB planar
    AVS_CS_RGBP   = AVS_CS_GENERIC_RGBP | AVS_CS_SAMPLE_BITS_8  # Planar RGB 8 bit samples
    AVS_CS_RGBP10 = AVS_CS_GENERIC_RGBP | AVS_CS_SAMPLE_BITS_10 # Planar RGB 10bit samples
    AVS_CS_RGBP12 = AVS_CS_GENERIC_RGBP | AVS_CS_SAMPLE_BITS_12 # Planar RGB 12bit samples
    AVS_CS_RGBP14 = AVS_CS_GENERIC_RGBP | AVS_CS_SAMPLE_BITS_14 # Planar RGB 14bit samples
    AVS_CS_RGBP16 = AVS_CS_GENERIC_RGBP | AVS_CS_SAMPLE_BITS_16 # Planar RGB 16bit samples
    AVS_CS_RGBPS  = AVS_CS_GENERIC_RGBP | AVS_CS_SAMPLE_BITS_32 # Planar RGB 32bit samples

    # RGBA planar
    AVS_CS_RGBAP   = AVS_CS_GENERIC_RGBAP | AVS_CS_SAMPLE_BITS_8  # Planar RGBA 8 bit samples
    AVS_CS_RGBAP10 = AVS_CS_GENERIC_RGBAP | AVS_CS_SAMPLE_BITS_10 # Planar RGBA 10bit samples
    AVS_CS_RGBAP12 = AVS_CS_GENERIC_RGBAP | AVS_CS_SAMPLE_BITS_12 # Planar RGBA 12bit samples
    AVS_CS_RGBAP14 = AVS_CS_GENERIC_RGBAP | AVS_CS_SAMPLE_BITS_14 # Planar RGBA 14bit samples
    AVS_CS_RGBAP16 = AVS_CS_GENERIC_RGBAP | AVS_CS_SAMPLE_BITS_16 # Planar RGBA 16bit samples
    AVS_CS_RGBAPS  = AVS_CS_GENERIC_RGBAP | AVS_CS_SAMPLE_BITS_32 # Planar RGBA 32bit samples

    # Planar YUVA
    AVS_CS_YUVA444    = AVS_CS_GENERIC_YUVA444 | AVS_CS_SAMPLE_BITS_8 # YUVA 4:4:4 8bit samples
    AVS_CS_YUVA422    = AVS_CS_GENERIC_YUVA422 | AVS_CS_SAMPLE_BITS_8 # YUVA 4:2:2 8bit samples
    AVS_CS_YUVA420    = AVS_CS_GENERIC_YUVA420 | AVS_CS_SAMPLE_BITS_8 # YUVA 4:2:0 8bit samples

    AVS_CS_YUVA444P10 = AVS_CS_GENERIC_YUVA444 | AVS_CS_SAMPLE_BITS_10 # YUVA 4:4:4 10bit samples
    AVS_CS_YUVA422P10 = AVS_CS_GENERIC_YUVA422 | AVS_CS_SAMPLE_BITS_10 # YUVA 4:2:2 10bit samples
    AVS_CS_YUVA420P10 = AVS_CS_GENERIC_YUVA420 | AVS_CS_SAMPLE_BITS_10 # YUVA 4:2:0 10bit samples

    AVS_CS_YUVA444P12 = AVS_CS_GENERIC_YUVA444 | AVS_CS_SAMPLE_BITS_12 # YUVA 4:4:4 12bit samples
    AVS_CS_YUVA422P12 = AVS_CS_GENERIC_YUVA422 | AVS_CS_SAMPLE_BITS_12 # YUVA 4:2:2 12bit samples
    AVS_CS_YUVA420P12 = AVS_CS_GENERIC_YUVA420 | AVS_CS_SAMPLE_BITS_12 # YUVA 4:2:0 12bit samples

    AVS_CS_YUVA444P14 = AVS_CS_GENERIC_YUVA444 | AVS_CS_SAMPLE_BITS_14 # YUVA 4:4:4 14bit samples
    AVS_CS_YUVA422P14 = AVS_CS_GENERIC_YUVA422 | AVS_CS_SAMPLE_BITS_14 # YUVA 4:2:2 14bit samples
    AVS_CS_YUVA420P14 = AVS_CS_GENERIC_YUVA420 | AVS_CS_SAMPLE_BITS_14 # YUVA 4:2:0 14bit samples

    AVS_CS_YUVA444P16 = AVS_CS_GENERIC_YUVA444 | AVS_CS_SAMPLE_BITS_16 # YUVA 4:4:4 16bit samples
    AVS_CS_YUVA422P16 = AVS_CS_GENERIC_YUVA422 | AVS_CS_SAMPLE_BITS_16 # YUVA 4:2:2 16bit samples
    AVS_CS_YUVA420P16 = AVS_CS_GENERIC_YUVA420 | AVS_CS_SAMPLE_BITS_16 # YUVA 4:2:0 16bit samples

    AVS_CS_YUVA444PS  = AVS_CS_GENERIC_YUVA444 | AVS_CS_SAMPLE_BITS_32 # YUVA 4:4:4 32bit samples
    AVS_CS_YUVA422PS  = AVS_CS_GENERIC_YUVA422 | AVS_CS_SAMPLE_BITS_32 # YUVA 4:2:2 32bit samples
    AVS_CS_YUVA420PS  = AVS_CS_GENERIC_YUVA420 | AVS_CS_SAMPLE_BITS_32 # YUVA 4:2:0 32bit samples
#end of colorspaces

    AVS_IT_BFF = 1 << 0
    AVS_IT_TFF = 1 << 1
    AVS_IT_FIELDBASED = 1 << 2

    AVS_FILTER_TYPE = 1
    AVS_FILTER_INPUT_COLORSPACE = 2
    AVS_FILTER_OUTPUT_TYPE = 9
    AVS_FILTER_NAME = 4
    AVS_FILTER_AUTHOR = 5
    AVS_FILTER_VERSION = 6
    AVS_FILTER_ARGS = 7
    AVS_FILTER_ARGS_INFO = 8
    AVS_FILTER_ARGS_DESCRIPTION = 10
    AVS_FILTER_DESCRIPTION = 11

    AVS_FILTER_TYPE_AUDIO = 1
    AVS_FILTER_TYPE_VIDEO = 2
    AVS_FILTER_OUTPUT_TYPE_SAME = 3
    AVS_FILTER_OUTPUT_TYPE_DIFFERENT = 4

    # New 2.6 explicitly defined cache hints.
    AVS_CACHE_NOTHING=10 # Do not cache video.
    AVS_CACHE_WINDOW=11 # Hard protect upto X frames within a range of X from the current frame N.
    AVS_CACHE_GENERIC=12 # LRU cache upto X frames.
    AVS_CACHE_FORCE_GENERIC=13 # LRU cache upto X frames, override any previous CACHE_WINDOW.

    AVS_CACHE_GET_POLICY=30 # Get the current policy.
    AVS_CACHE_GET_WINDOW=31 # Get the current window h_span.
    AVS_CACHE_GET_RANGE=32 # Get the current generic frame range.

    AVS_CACHE_AUDIO=50 # Explicitly do cache audio, X byte cache.
    AVS_CACHE_AUDIO_NOTHING=51 # Explicitly do not cache audio.
    AVS_CACHE_AUDIO_NONE=52 # Audio cache off (auto mode), X byte intial cache.
    AVS_CACHE_AUDIO_AUTO=53 # Audio cache on (auto mode), X byte intial cache.

    AVS_CACHE_GET_AUDIO_POLICY=70 # Get the current audio policy.
    AVS_CACHE_GET_AUDIO_SIZE=71 # Get the current audio cache size.

    AVS_CACHE_PREFETCH_FRAME=100 # Queue request to prefetch frame N.
    AVS_CACHE_PREFETCH_GO=101 # Action video prefetches.

    AVS_CACHE_PREFETCH_AUDIO_BEGIN=120 # Begin queue request transaction to prefetch audio (take critical section).
    AVS_CACHE_PREFETCH_AUDIO_STARTLO=121 # Set low 32 bits of start.
    AVS_CACHE_PREFETCH_AUDIO_STARTHI=122 # Set high 32 bits of start.
    AVS_CACHE_PREFETCH_AUDIO_COUNT=123 # Set low 32 bits of length.
    AVS_CACHE_PREFETCH_AUDIO_COMMIT=124 # Enqueue request transaction to prefetch audio (release critical section).
    AVS_CACHE_PREFETCH_AUDIO_GO=125 # Action audio prefetches.

    AVS_CACHE_GETCHILD_CACHE_MODE=200 # Cache ask Child for desired video cache mode.
    AVS_CACHE_GETCHILD_CACHE_SIZE=201 # Cache ask Child for desired video cache size.
    AVS_CACHE_GETCHILD_AUDIO_MODE=202 # Cache ask Child for desired audio cache mode.
    AVS_CACHE_GETCHILD_AUDIO_SIZE=203 # Cache ask Child for desired audio cache size.

    AVS_CACHE_GETCHILD_COST=220 # Cache ask Child for estimated processing cost.
    AVS_CACHE_COST_ZERO=221 # Child response of zero cost (ptr arithmetic only).
    AVS_CACHE_COST_UNIT=222 # Child response of unit cost (less than or equal 1 full frame blit).
    AVS_CACHE_COST_LOW=223 # Child response of light cost. (Fast)
    AVS_CACHE_COST_MED=224 # Child response of medium cost. (Real time)
    AVS_CACHE_COST_HI=225 # Child response of heavy cost. (Slow)

    AVS_CACHE_GETCHILD_THREAD_MODE=240 # Cache ask Child for thread safetyness.
    AVS_CACHE_THREAD_UNSAFE=241 # Only 1 thread allowed for all instances. 2.5 filters default!
    AVS_CACHE_THREAD_CLASS=242 # Only 1 thread allowed for each instance. 2.6 filters default!
    AVS_CACHE_THREAD_SAFE=243 # Allow all threads in any instance.
    AVS_CACHE_THREAD_OWN=244 # Safe but limit to 1 thread, internally threaded.

    AVS_CACHE_GETCHILD_ACCESS_COST=260 # Cache ask Child for preferred access pattern.
    AVS_CACHE_ACCESS_RAND=261 # Filter is access order agnostic.
    AVS_CACHE_ACCESS_SEQ0=262 # Filter prefers sequential access (low cost)
    AVS_CACHE_ACCESS_SEQ1=263 # Filter needs sequential access (high cost)

    AVS_FRAME_ALIGN = 64

    #CPU flags: no need

class AvisynthError(Exception):
    pass


class AVS_ScriptEnvironment(object):

    def __init__(self, version=6):
        self.cdata = avs_create_script_environment(version)
        weak_dict[self] = []

    def from_param(obj):
        if not isinstance(obj, AVS_ScriptEnvironment):
            raise TypeError("Wrong argument: AVS_ScriptEnvironment expected")
        return obj.cdata

    def __del__(self):
        avs_delete_script_environment(self)

    def invoke(self, name, args=[], arg_names=None):
        if not isinstance(args, AVS_Value):
            args = AVS_Value(args, env=self)
        if not arg_names:
            arg_names = None
        elif isinstance(arg_names, list):
            arg_names2 = (ctypes.c_char_p * len(arg_names))(*arg_names)
            arg_names = ctypes.cast(ctypes.byref(arg_names2), ctypes.POINTER(ctypes.c_char_p))
        ret = AVS_Value(avs_invoke(self, name, args, arg_names), env=self)
        if ret.is_error():
            raise AvisynthError(ret.as_error())
        return ret.get_value()

    try: # 5
        avidll.avs_get_error
        def get_error(self): return avs_get_error(self)
    except: pass

    def get_cpu_flags(self):
        return avs_get_cpu_flags(self)

    def check_version(self,version):
        # 0 -> True, -1 -> False
        return not bool(avs_check_version(self, version))

    def save_string(self,string): # useless with ctypes
        return avs_save_string(self, string, len(string))

    def add_function(self, name, params, py_function, userdata=None):
        # it won't work, see http://bugs.python.org/issue5710
        if userdata is None:
            userdata = ctypes.c_void_p()
        return avs_add_function(self, name, params, APPLYFUNC(py_function),
                                ctypes.byref(userdata))

    def function_exists(self, name):
        return avs_function_exists(self, name)

    def get_var(self, name, type=False):
        if isinstance(name, unicode):
            # mbcs will replace invalid characters anyway
            name = name.encode(encoding, 'backslashreplace')
        value = AVS_Value(avs_get_var(self, name), env=self)
        if value.get_type() is None:
            raise AvisynthError("NotFound")
        if type:
            return value.get_value(self), value.get_type()
        return value.get_value(self)

    def set_var(self, name, value):
        if not isinstance(value, AVS_Value):
            value = AVS_Value(value, self)
        return avs_set_var(self, name, value)

    def set_global_var(self, name, value):
        if not isinstance(value, AVS_Value):
            value = AVS_Value(value, self)
        return avs_set_global_var(self, name, value)

    def new_video_frame_a(self, vi, align=avs.AVS_FRAME_ALIGN):
        return avs_new_video_frame_a(self, vi, align)

    def make_writable(self, AVS_VideoFrame):
        return avs_make_writable(self, ctypes.byref(AVS_VideoFrame.cdata))

    def bit_blt(self, dstp, dst_pitch, srcp, src_pitch, row_size, height):
        avs_bit_blt(self, dstp, dst_pitch, srcp, src_pitch, row_size, height)

    def at_exit(self, py_function, userdata):
        return avs_at_exit(self, SHUTDOWNFUNC(py_function), ctypes.POINTER(userdata))

    def set_memory_max(self, mem):
        return avs_set_memory_max(self, mem)

    def set_working_dir(self, new_dir):
        if isinstance(new_dir, unicode):
            new_dir = new_dir.encode(encoding, 'backslashreplace')
        return avs_set_working_dir(self, new_dir)

    def subframe(self, src, rel_offset, new_pitch, new_row_size, new_height):
        return avs_subframe(self, src, rel_offset, new_pitch, new_row_size, new_height)

    def subframe_planar(self, src, rel_offset, new_pitch, new_row_size,
                        new_height, rel_offsetU, rel_offsetV, new_pitchUV):
        return avs_subframe(self, src, rel_offset, new_pitch, new_row_size,
                            new_height, rel_offsetU, rel_offsetV, new_pitchUV)

    def propToChar(self, key, value):
        """ v1
        s = func.GetPropNameValue(key, value)
        return '[' + s + ']' if s else ''
        """
        """ v2
        f = propCharDict.get(key, None)
        if f is not None:
            return '[' + f(value) + ']'
        return ''
        """
        if key in propCharDict:
            return '[' + propCharDict[key](value) + ']'
        return ''

    def props_get_picture_type(self, frame):
        r = 0
        avsmap = avs_get_frame_props_ro(self, frame.cdata)
        if avsmap:
            c = avs_prop_num_keys(self, avsmap)
            if c > 0:
                for i in range(c):
                    key_name = avs_prop_get_key(self, avsmap, i)
                    if key_name == '_PictType':
                        return str(avs_prop_get_data(self, avsmap, key_name, 0, r))
        return ''

    def props_get_matrix(self, frame):
        r = 0
        avsmap = avs_get_frame_props_ro(self, frame.cdata)
        if avsmap:
            c = avs_prop_num_keys(self, avsmap)
            if c > 0:
                for i in range(c):
                    key_name = avs_prop_get_key(self, avsmap, i)
                    if key_name == '_Matrix':
                        typ = avs_prop_get_type(self, avsmap, key_name)
                        if typ == 'i':
                            return int(avs_prop_get_int(self, avsmap, key_name,  0, r))
        return -1

    def props_get_all(self, frame):
        s = ''
        r = 0
        avsmap = avs_get_frame_props_ro(self, frame.cdata)
        if avsmap:
            c = avs_prop_num_keys(self, avsmap)
            if c > 0:
                s = 'Keys: ' + str(c) + '\n'
                for i in range(c):
                    key_name = avs_prop_get_key(self, avsmap, i)
                    num_elements = avs_prop_num_elements(self, avsmap, key_name)
                    typ = avs_prop_get_type(self, avsmap, key_name)
                    s +=  key_name + ' ('
                    for j in range(num_elements):
                        if typ == 'i':
                            re = avs_prop_get_int(self, avsmap, key_name,  j, r)
                            s += str(re) + self.propToChar(key_name, re) + ', '
                        elif typ == 's':
                            s += str(avs_prop_get_data(self, avsmap, key_name, j, r)) + ', '
                        elif typ == 'f':
                            s += str(avs_prop_get_float(self, avsmap, key_name,  j, r)) + ', '
                        elif typ == 'c':
                            s += 'clip, '
                        elif typ == 'v':
                            s += 'frame, '
                        elif typ == 'u':
                            s += 'unset, '
                        else:
                            s += '?, '
                    s = s[:-2] + ')\n'
        return s #.rstrip() # bug in styledTextctrl
    """
    def props_clear_all(self, frame):
        avsmap = avs_get_frame_props_ro(self, frame.cdata)
        if avsmap:
            avs_clear_map(avsmap)
    """

class AVS_VideoInfo_C(ctypes.Structure):
    _fields_ = [("width",ctypes.c_int), # 0 means no video
                ("height",ctypes.c_int),
                ("fps_numerator",ctypes.c_uint),
                ("fps_denominator",ctypes.c_uint),
                ("num_frames",ctypes.c_int),
                ("pixel_type",ctypes.c_uint),
                ("audio_samples_per_second",ctypes.c_int), # 0 means no audio
                ("sample_type",ctypes.c_int),
                ("num_audio_samples",ctypes.c_int64),
                ("nchannels",ctypes.c_int),
                ("image_type",ctypes.c_int)]


class AVS_VideoInfo(object):

    def __init__(self, vi=None):
        self.cdata = vi or ctypes.pointer(VideoInfo())
        for field, type in self.cdata.contents._fields_:
            setattr(self, field, getattr(self.cdata.contents, field))

    def __str__(self):
        string = str(self.__class__)
        for field, type in self.cdata.contents._fields_:
            string += ', {0}: {1}'.format(field, getattr(self.cdata.contents, field))
        return string

    def from_param(obj):
        if not isinstance(obj, AVS_VideoInfo):
            raise TypeError("Wrong argument: AVS_VideoInfo expected")
        return obj.cdata

    def has_video(self):
        return self.cdata.contents.width != 0

    def has_audio(self):
        return self.cdata.contents.audio_samples_per_second != 0

    def is_rgb(self):
        return self.cdata.contents.pixel_type & avs.AVS_CS_BGR != 0

    def is_rgb24(self):
        return ((self.cdata.contents.pixel_type & avs.AVS_CS_BGR24) == avs.AVS_CS_BGR24) and \
            ((self.cdata.contents.pixel_type & avs.AVS_CS_SAMPLE_BITS_MASK) == avs.AVS_CS_SAMPLE_BITS_8)

    def is_rgb32(self):
        return ((self.cdata.contents.pixel_type & avs.AVS_CS_BGR32) == avs.AVS_CS_BGR32) and \
            ((self.cdata.contents.pixel_type & avs.AVS_CS_SAMPLE_BITS_MASK) == avs.AVS_CS_SAMPLE_BITS_8)

    def is_yuv(self):
        return self.cdata.contents.pixel_type & avs.AVS_CS_YUV != 0

    def is_yuy2(self):
        return (self.cdata.contents.pixel_type & avs.AVS_CS_YUY2) == avs.AVS_CS_YUY2

    def is_yv24(self):
        return bool(avs_is_yv24(self.cdata)) #V6
        #return (self.cdata.contents.pixel_type & avs.AVS_CS_PLANAR_MASK) == (avs.AVS_CS_YV24 & avs.AVS_CS_PLANAR_FILTER)

    def is_yv16(self):
        return bool(avs_is_yv16(self.cdata)) #V6
        #return (self.cdata.contents.pixel_type & avs.AVS_CS_PLANAR_MASK) == (avs.AVS_CS_YV16 & avs.AVS_CS_PLANAR_FILTER)

    def is_yv12(self):
        return bool(avs_is_yv12(self.cdata)) #V6
        #return (self.cdata.contents.pixel_type & avs.AVS_CS_PLANAR_MASK) == (avs.AVS_CS_YV12 & avs.AVS_CS_PLANAR_FILTER)

    def is_yv411(self):
        return bool(avs_is_yv411(self.cdata)) #V6
        #return (self.cdata.contents.pixel_type & avs.AVS_CS_PLANAR_MASK) == (avs.AVS_CS_YV411 & avs.AVS_CS_PLANAR_FILTER)

    def is_y8(self):
        return bool(avs_is_y8(self.cdata)) #V6
        #return (self.cdata.contents.pixel_type & avs.AVS_CS_PLANAR_MASK) == (avs.AVS_CS_Y8 & avs.AVS_CS_PLANAR_FILTER)

    def is_property(self, property):
        return (self.cdata.contents.pixel_type & property) == property

    def is_planar(self):
        return self.cdata.contents.pixel_type & avs.AVS_CS_PLANAR != 0

    def is_interleaved(self):
        return self.cdata.contents.pixel_type & avs.AVS_CS_INTERLEAVED != 0

    def is_color_space(self, c_space):
        return bool(avs_is_color_space(self.cdata, c_space)); #V6
        #if self.cdata.is_planar():
        #    return (self.cdata.contents.pixel_type & avs.AVS_CS_PLANAR_MASK) == (c_space & avs.AVS_CS_PLANAR_FILTER)
        #else:
        #    return (self.cdata.contents.pixel_type & c_space) == c_space

    def is_field_based(self):
        return self.cdata.contents.image_type & avs.AVS_IT_FIELDBASED != 0

    def is_parity_known(self):
        return (self.cdata.contents.image_type & avs.AVS_IT_FIELDBASED != 0) and \
            (self.cdata.contents.image_type & (avs.AVS_IT_BFF | avs.AVS_IT_TFF) != 0)

    def is_bff(self):
        return self.cdata.contents.image_type & avs.AVS_IT_BFF != 0

    def is_tff(self):
        return self.cdata.contents.image_type & avs.AVS_IT_TFF != 0

    def is_v_plane_first(self):
        # todo: move to avs_is_y when it's safe for classic avisynth
        return not self.is_y() and self.is_planar() and (self.cdata.contents.pixel_type &
            (avs.AVS_CS_VPLANEFIRST | avs.AVS_CS_UPLANEFIRST)) == avs.AVS_CS_VPLANEFIRST # Shouldn't use this

    def get_plane_width_subsampling(self, plane): # Subsampling in bitshifts!
        return avs_get_plane_width_subsampling(self.cdata, plane); #V6

    def get_plane_height_subsampling(self, plane): # Subsampling in bitshifts!
        return avs_get_plane_height_subsampling(self.cdata, plane) #V6

    def bits_per_pixel(self): # Lookup Interleaved, calculate PLANAR's
        return avs_bits_per_pixel(self.cdata); #V6

    def bytes_from_pixels(self, pixels):
        return avs_bytes_from_pixels(self.cdata) #V6

    def row_size(self, plane):
        return avs_row_size(self.cdata, plane) #V6

    def bmp_size(self):
        return avs_bmp_size(self.cdata); #V6

    def is_sample_type(self, testtype):
        return (self.cdata.contents.sample_type & testtype) != 0

    def samples_per_second(self):
        return self.cdata.contents.audio_samples_per_second

    def bytes_per_channel_sample(self):
        if self.cdata.contents.sample_type == avs.AVS_SAMPLE_INT8 :
            return ctypes.sizeof(ctypes.c_char)
        elif self.cdata.contents.sample_type == avs.AVS_SAMPLE_INT16:
            return ctypes.sizeof(ctypes.c_short)
        if self.cdata.contents.sample_type == avs.AVS_SAMPLE_INT24:
            return 3
        if self.cdata.contents.sample_type == avs.AVS_SAMPLE_INT32:
            return ctypes.sizeof(ctypes.c_int)
        if self.cdata.contents.sample_type == avs.AVS_SAMPLE_FLOAT:
            return ctypes.sizeof(ctypes.c_float)
        return 0

    def bytes_per_audio_sample(self):
        return self.bytes_per_channel_sample() * self.cdata.contents.nchannels

    def audio_samples_from_frames(self, frames):
        if self.has_audio() and self.cdata.contents.fps_denominator:
            return frames * self.cdata.contents.audio_samples_per_second \
                * self.cdata.contents.fps_denominator / self.cdata.contents.fps_numerator
        else: return 0

    def frames_from_audio_samples(self, samples):
        if self.has_audio() and self.cdata.contents.fps_denominator:
            return samples * self.cdata.contents.fps_numerator / self.cdata.contents.fps_denominator \
                / self.contents.cdata.audio_samples_per_second
        else: return 0

    def audio_samples_from_bytes(self,bytes):
        return bytes / self.bytes_per_audio_sample() if self.has_audio() else 0

    def bytes_from_audio_samples(self, samples):
        return samples * self.bytes_per_audio_sample()

    def audio_channels(self):
        return self.cdata.contents.nchannels if self.has_audio() else 0

    def sample_type(self):
        return self.cdata.contents.sample_type

    def set_property(self, property):
        self.cdata.contents.image_type |= property

    def clear_property(self, property):
        self.cdata.contents.image_type &= ~property

    def set_field_based(self, is_field_based):
        if is_field_based:
            self.cdata.contents.image_type |= avs.AVS_IT_FIELDBASED
        else:
            self.cdata.contents.image_type &= ~avs.AVS_IT_FIELDBASED

    def set_fps(self, numerator, denominator): # useful mutator
        if numerator == 0 or denominator == 0:
            self.cdata.contents.fps_numerator = 0
            self.cdata.contents.fps_denominator = 1
        else:
            x = numerator
            y = denominator
            while y: # find gcd
                x, y = y, x % y
            self.cdata.contents.fps_numerator = numerator / x
            self.cdata.contents.fps_denominator = denominator / x

    def is_same_colorspace(self, vi):
        return (self.cdata.contents.pixel_type == vi.pixeltype) or (self.is_yv12() and vi.is_yv12())

    # Avisynth+ extensions, they are callable even for Classic Avisynth where there functions originally missing
    def is_rgb48(self):
        return bool(avs_is_rgb48(self.cdata))
    def is_rgb64(self):
        return bool(avs_is_rgb64(self.cdata))
    def is_444(self):
        return bool(avs_is_444(self.cdata))
    def is_422(self):
        return bool(avs_is_422(self.cdata))
    def is_420(self):
        return bool(avs_is_420(self.cdata))
    def is_y(self):
        return bool(avs_is_y(self.cdata))
    def is_yuva(self):
        return bool(avs_is_yuva(self.cdata))
    def is_planar_rgb(self):
        return bool(avs_is_planar_rgb(self.cdata))
    def is_planar_rgba(self):
        return bool(avs_is_planar_rgba(self.cdata))
    def num_components(self):
        return avs_num_components(self.cdata)
    def component_size(self):
        return avs_component_size(self.cdata)
    def bits_per_component(self):
        return avs_bits_per_component(self.cdata)

class AVS_Clip:
    def __init__(self, clip):
        self.cdata = clip
        self._error = None # additional error info

    def from_param(obj):
        if not isinstance(obj, AVS_Clip):
            raise TypeError("Wrong argument: AVS_Clip expected")
        return obj.cdata

    def copy_clip(self):
        return avs_copy_clip(self)

    def __del__(self):
        avs_release_clip(self)

    def get_frame(self,n):
        self._error = None
        try:
            return AVS_VideoFrame(avs_get_frame(self, n))
        except Exception as err:
            # Clear the exception traceback in order to avoid keeping an
            # additional reference to the clip, which would cause its
            # destruction to be postponed until the process finishes (if
            # that's the last exception). It would then cause a new exception
            # as the env doesn't exist anymore at that point (maybe even
            # avisynth was already unloaded).
            self._error = ''.join(traceback.format_exception_only(type(err), err))
            sys.exc_clear()

    def get_parity(self, n):
        """ return field parity if field_based, else parity of first field in frame"""
        return avs_get_parity(self, n)

    def get_audio(self, buf, start, count):
    # start and count are in samples
        return avs_get_audio(self, buf, start, count)

    def get_frame_audio(self, n):
        src = self.get_frame(n)
        vi = self.get_video_info()
        if vi.has_audio():
            start = vi.audio_samples_from_frames(n)
            count = vi.audio_samples_from_frames(1)
            buffer_size = count * vi.sample_type() * vi.audio_channels()
            buffer = ctypes.create_string_buffer(buffer_size)
            return avs_get_audio(self, ctypes.addressof(buffer), max(0, start),
                                 count) # start and count are in samples

    def set_cache_hints(self, cachehints, frame_range):
        return avs_set_cache_hints(self, cachehints, frame_range)

    def get_error(self):
        error = avs_clip_get_error(self) or self._error
        self._error = None # avs_clip_get_error is used for more than get_frame
        return error

    def get_video_info(self):
        return AVS_VideoInfo(avs_get_video_info(self))

    def get_version(self):
        return avs_get_version(self)


GETFRAMEPROPS = FUNCTYPE(ctypes.c_void_p)
class AVS_Map_C(ctypes.Structure):
    _fields_ = [("getproperties", GETFRAMEPROPS)]

class AVS_VideoFrameBuffer_C(ctypes.Structure):
    _fields_ = [("data",ctypes.POINTER(ctypes.c_ubyte)),
                ("data_size",ctypes.c_int),
                ("sequence_number",ctypes.c_int),
                ("refcount",ctypes.c_int)]

class AVS_VideoFrame_C(ctypes.Structure):
    _fields_ = [("refcount",ctypes.c_int),
                ("vfb",ctypes.POINTER(AVS_VideoFrameBuffer_C)),
                ("offset",ctypes.c_int),
                ("pitch",ctypes.c_int),
                ("row_size",ctypes.c_int),
                ("height",ctypes.c_int),
                ("offsetU",ctypes.c_int),
                ("offsetV",ctypes.c_int),
                ("pitchUV",ctypes.c_int),
                ("row_sizeUV",ctypes.c_int),
                ("heightUV",ctypes.c_int),
                ("offsetA",ctypes.c_int), # 4th alpha plane support, pitch and row_size is 0 is none
                ("pitchA",ctypes.c_int),
                ("row_sizeA",ctypes.c_int),
                ("properties",ctypes.POINTER(AVS_Map_C))
               ]

class AVS_VideoFrame(object):

    def __init__(self, video_frame):
        self.cdata = video_frame

    def from_param(obj):
        if not isinstance(obj, AVS_VideoFrame):
            raise TypeError("Wrong argument: AVS_VideoFrame expected")
        return obj.cdata

    def __del__(self):
        avs_release_video_frame(self)

    def copy(self):
        return avs_copy_video_frame(self)

    def __str__(self):
        string = str(self.__class__)
        for field, type in self.cdata.contents._fields_:
            string += ', {0}: {1}'.format(field, getattr(self.cdata.contents, field))
        return string

    def get_pitch(self, plane=avs.AVS_PLANAR_Y):
        return avs_get_pitch_p(self.cdata, plane); #V6

    def get_row_size(self, plane=avs.AVS_PLANAR_Y):
        # wonder if there will be problems. let's see
        return avs_get_row_size_p(self.cdata, plane); #V6

    def get_height(self, plane=avs.AVS_PLANAR_Y):
        return avs_get_height_p(self.cdata, plane); #V6

    def get_frame_buffer(self): return self.cdata.contents.vfb

    def get_read_ptr(self, plane=avs.AVS_PLANAR_Y):
        return avs_get_read_ptr_p(self.cdata, plane) #V6

    def is_writable(self):
        return bool(avs_is_writable(self.cdata)) #V6

    def get_write_ptr(self, plane=avs.AVS_PLANAR_Y):
        return avs_get_write_ptr_p(self.cdata, plane) #V6


class AVS_Value(object):

    def __init__(self, value=None, env=None, release_on_del=True):
        self.cdata = AVS_Value_C()
        self.set_void()
        self.env = env # for using with clips, we assume all belong to the same env
        self._release_on_del = release_on_del
        if value is not None:
            self.set_value(value, env)

    def from_param(obj):
        if not isinstance(obj, AVS_Value):
            raise TypeError("Wrong argument: AVS_ScriptEnvironment expected")
        return obj.cdata

    def __str__(self):
        return str(self.get_value())

    def __repr__(self):
        return repr(self.get_value())

    # set methods

    def set_value(self, value, env=None):
        if   isinstance(value, bool):       self.set_bool(value)
        elif isinstance(value, int):        self.set_int(value)
        elif isinstance(value, float):      self.set_float(value)
        elif isinstance(value, basestring): self.set_string(value, env)
        elif isinstance(value, AVS_Clip):   self.set_clip(value)
        elif isinstance(value, AVS_Value):  self.copy_from(value)
        elif isinstance(value, (ctypes._SimpleCData, ctypes.Structure,
                                ctypes.Union)):  self.set_cdata(value)
        elif isinstance(value, collections.Iterable): self.set_array(value)
        else:
            raise AvisynthError('invalid type: {type}'.format(type=type(value)))

    def __call__(self, val, env=None):
        self.set_value(val, env)

    def copy_from(self, value):
        avs_copy_value(ctypes.byref(self.cdata), value)
        self.env = value.env
        self._release_on_del = value._release_on_del

    def set_void(self):
        self.cdata.type = ord('v')
        self.cdata.array_size = 0

    def set_cdata(self, value):
        if self.is_defined():
            self.release()
        self.cdata = value

    def set_bool(self, value):
        if self.is_defined():
            self.release()
        self.cdata.type = ord('b')
        self.cdata.d.b = value

    def set_int(self, value):
        if self.is_defined():
            self.release()
        self.cdata.type = ord('i')
        self.cdata.d.i = value

    def set_float(self, value):
        if self.is_defined():
            self.release()
        self.cdata.type = ord('f')
        self.cdata.d.f = value

    def set_string(self, value, env=None):
        if self.is_defined():
            self.release()
        if isinstance(value, unicode):
            value = value.encode(encoding, 'backslashreplace')
        env = env or self.env
        if isinstance(env, AVS_ScriptEnvironment):
            weak_dict[env].append(value)
        self.cdata.type = ord('s')
        self.cdata.d.s = value

    def set_error(self, value, env=None):
        if self.is_defined():
            self.release()
        if isinstance(value, unicode):
            value = value.encode(encoding, 'backslashreplace')
        env = env or self.env
        if isinstance(env, AVS_ScriptEnvironment):
            weak_dict[env].append(value)
        self.cdata.type = ord('s')
        self.cdata.d.s = value

    def set_clip(self, value):
        if self.is_defined():
            self.release()
        avs_set_to_clip(ctypes.byref(self.cdata), value)

    def set_array(self, values, env=None):
        if self.is_defined():
            self.release()
        env = env or self.env
        length = len(values)
        avs_values = (AVS_Value_C * length)()
        for i, value in enumerate(values):
            if not isinstance(value, AVS_Value):
                value = AVS_Value(value, env)
            avs_copy_value(ctypes.byref(avs_values[i]), value)
        self.cdata.type = ord('a')
        self.cdata.array_size = length
        self.cdata.d.a = ctypes.cast(ctypes.pointer(avs_values), ctypes.POINTER(AVS_Value_C))

    # check type methods

    def is_defined(self):
        return self.cdata.type not in (0, ord('v'))

    def get_type(self):
        if self.is_bool():
            type = 'bool'
        elif self.is_int():
            type = 'int'
        elif self.is_float():
            type = 'float'
        elif self.is_string():
            type = 'string'
        elif self.is_error():
            type = 'error'
        elif self.is_clip():
            type = 'clip'
        elif self.is_array():
            type = 'array'
        else:
            type = None
        return type

    def is_bool(self):
        return self.cdata.type == ord('b')

    def is_int(self):
        return self.cdata.type == ord('i')

    def is_float(self):
        return self.cdata.type in (ord('f'), ord('i'))

    def is_string(self):
        return self.cdata.type == ord('s')

    def is_error(self):
        return self.cdata.type == ord('e')

    def is_clip(self):
        return self.cdata.type == ord('c')

    def is_array(self):
        return self.cdata.type == ord('a')

    # get methods

    def get_value(self, env=None):
        if   self.is_bool():   return self.as_bool()
        elif self.is_int():    return self.as_int()
        elif self.is_float():  return self.as_float()
        elif self.is_string(): return self.as_string()
        elif self.is_error():  return self.as_error()
        elif self.is_clip():   return self.as_clip(env)
        elif self.is_array():  return self.as_array(env)

    def as_bool(self):
        if self.is_bool():
            return self.cdata.d.b
        else:
            raise AvisynthError("Not a bool")

    def as_int(self):
        if self.is_int():
            return self.cdata.d.i
        else:
            raise AvisynthError("Not an int")

    def as_float(self):
        if self.is_float():
            return self.cdata.d.f
        else:
            raise AvisynthError("Not a float")

    def as_string(self):
        if self.is_string():
            return self.cdata.d.s
        else:
            raise AvisynthError("Not a string")

    def as_error(self):
        if self.is_error():
            return self.cdata.d.s
        else:
            raise AvisynthError("Not an error")

    def as_clip(self, env=None):
        if self.is_clip():
            env = env or self.env
            if not isinstance(env, AVS_ScriptEnvironment):
                raise AvisynthError('AVS_Value.as_clip needs an environment')
            return AVS_Clip(avs_take_clip(self, env))
        else:
            raise AvisynthError("Not a clip")

    def as_array(self, env=None):
        if self.is_array():
            return [self.array_elt(i, env) for i in range(self.array_size())]
        else:
            raise AvisynthError("Not an array")

    def array_size(self):
        return self.cdata.array_size if self.is_array() else 1

    def array_elt(self, index, env=None):
        if not 0 <= index < self.array_size():
            raise IndexError
        return AVS_Value(self.cdata.d.a[index] if self.is_array() else self.cdata,
                         env=env or self.env, release_on_del=False).get_value()

    def __len__(self):
        return self.array_size()

    def __getitem__(self, index):
        if isinstance(index, slice):
            pass # TODO
        else:
            return self.array_elt(index)

    # free memory

    def release(self):
        if self.is_array():
            for index in range(self.array_size()):
                AVS_Value(self.cdata.d.a[index], self.env)
        avs_release_value(self)
        if self.is_defined():
            self.set_void()

    def __del__(self):
        if self._release_on_del:
            self.release()


class AVS_Value_C(ctypes.Structure):
    pass

class U(ctypes.Union):
       _fields_ = [("c",ctypes.c_void_p),
                   ("b",ctypes.c_bool),
                   ("i",ctypes.c_int),
                   ("f",ctypes.c_float),
                   ("s",ctypes.c_char_p),
                   ("a",ctypes.POINTER(AVS_Value_C))]
       # AvxSynth extends AVS_Value with a 64-bit integer type.
       if os.name != 'nt':
           _fields_.append(('l',ctypes.c_longlong))


AVS_Value_C._fields_ = [("type",ctypes.c_short),
                        ("array_size",ctypes.c_short),
                        ("d", U)]


class FilterInfo(ctypes.Structure):
    pass


GETFRAME = FUNCTYPE(ctypes.POINTER(AVS_VideoFrame_C), ctypes.POINTER(FilterInfo),
                    ctypes.c_int)
GETPARITY = FUNCTYPE(ctypes.c_int, ctypes.POINTER(FilterInfo), ctypes.c_int)
GETAUDIO = FUNCTYPE(ctypes.c_int, ctypes.POINTER(FilterInfo), ctypes.c_void_p,
                    ctypes.c_int64, ctypes.c_int64)
SETCACHEHINTS = FUNCTYPE(ctypes.c_int, ctypes.POINTER(FilterInfo), ctypes.c_int,
                         ctypes.c_int)
FREEFILTER = FUNCTYPE(None, ctypes.POINTER(FilterInfo))

FilterInfo._fields_=[("child",ctypes.c_void_p),
                     ("vi",AVS_VideoInfo_C),
                     ("env",ctypes.c_void_p),
                     ("get_frame",GETFRAME),
                     ("get_parity",GETPARITY),
                     ("get_audio",GETAUDIO),
                     ("set_cache_hints",SETCACHEHINTS),
                     ("free_filter",FREEFILTER),
                     ("error",ctypes.c_char_p),
                     ("user_data",ctypes.c_void_p)]

#def CreateAVS_VideoFrameCT(result, func, arguments):return AVS_VideoFrame(result)
#def CreateAVS_VideoInfoCT(result,func,arguments):return AVS_VideoInfo(result)
#def CreateAVS_ScriptEnvironmentCT(result,func,arguments):return AVS_ScriptEnvironment(result)


#setup avisynth_c functions

# AVS_ScriptEnvironment functions
avs_create_script_environment=avidll.avs_create_script_environment
avs_create_script_environment.restype = ctypes.c_void_p
avs_create_script_environment.argtypes= [ctypes.c_int]
#avs_create_script_environment.errcheck=CreateAVS_ScriptEnvironmentCT

avs_delete_script_environment=avidll.avs_delete_script_environment
avs_delete_script_environment.restype = None
avs_delete_script_environment.argtypes=[AVS_ScriptEnvironment]

try: # 5
    avs_get_error = avidll.avs_get_error
    avs_get_error.restype = ctypes.c_char_p
    avs_get_error.argtypes = [AVS_ScriptEnvironment]
except: pass

avs_get_cpu_flags=avidll.avs_get_cpu_flags
avs_get_cpu_flags.restype = ctypes.c_int
avs_get_cpu_flags.argtypes=[AVS_ScriptEnvironment]

avs_check_version=avidll.avs_check_version
avs_check_version.restype = ctypes.c_int
avs_check_version.argtypes=[AVS_ScriptEnvironment,ctypes.c_int]

avs_save_string=avidll.avs_save_string
avs_save_string.restype = ctypes.c_char_p
avs_save_string.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p,ctypes.c_int]

avs_vsprintf=avidll.avs_sprintf
avs_vsprintf.restype = ctypes.c_char_p
avs_vsprintf.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p,ctypes.c_void_p]


APPLYFUNC = FUNCTYPE(AVS_Value, AVS_ScriptEnvironment, AVS_Value,
                     ctypes.c_void_p)

avs_add_function=avidll.avs_add_function
avs_add_function.restype = ctypes.c_int
avs_add_function.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p,ctypes.c_char_p,
                           APPLYFUNC,ctypes.c_void_p]

avs_function_exists=avidll.avs_function_exists
avs_function_exists.restype = ctypes.c_int
avs_function_exists.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p]

avs_get_var=avidll.avs_get_var
avs_get_var.restype=AVS_Value_C
avs_get_var.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p]

avs_set_var=avidll.avs_set_var
avs_set_var.restype=ctypes.c_int
avs_set_var.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p,AVS_Value]

avs_set_global_var=avidll.avs_set_global_var
avs_set_global_var.restype=ctypes.c_int
avs_set_global_var.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p,AVS_Value]

avs_new_video_frame_a=avidll.avs_new_video_frame_a
avs_new_video_frame_a.restype=ctypes.POINTER(AVS_VideoFrame_C)
avs_new_video_frame_a.argtypes=[AVS_ScriptEnvironment,AVS_VideoInfo,ctypes.c_int]
#avs_new_video_frame_a.errcheck=CreateAVS_VideoFrameCT

# AVS_VideoInfo
#avs_is_rgb32=avidll.avs_is_rgb32
#avs_is_rgb32.restype=ctypes.c_int
#avs_is_rgb32.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_is_yv24=avidll.avs_is_yv24 #V6
avs_is_yv24.restype=ctypes.c_int
avs_is_yv24.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_is_yv16=avidll.avs_is_yv16 #V6
avs_is_yv16.restype=ctypes.c_int
avs_is_yv16.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_is_yv12=avidll.avs_is_yv12 #V6
avs_is_yv12.restype=ctypes.c_int
avs_is_yv12.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_is_yv411=avidll.avs_is_yv411 #V6
avs_is_yv411.restype=ctypes.c_int
avs_is_yv411.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_is_y8=avidll.avs_is_y8 #V6
avs_is_y8.restype=ctypes.c_int
avs_is_y8.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_is_color_space=avidll.avs_is_color_space #V6
avs_is_color_space.restype=ctypes.c_int
avs_is_color_space.argtypes=[ctypes.POINTER(AVS_VideoInfo_C), ctypes.c_int]

avs_get_plane_width_subsampling=avidll.avs_get_plane_width_subsampling #V6
avs_get_plane_width_subsampling.restype=ctypes.c_int
avs_get_plane_width_subsampling.argtypes=[ctypes.POINTER(AVS_VideoInfo_C), ctypes.c_int]

avs_get_plane_height_subsampling=avidll.avs_get_plane_height_subsampling #V6
avs_get_plane_height_subsampling.restype=ctypes.c_int
avs_get_plane_height_subsampling.argtypes=[ctypes.POINTER(AVS_VideoInfo_C), ctypes.c_int]

avs_bits_per_pixel=avidll.avs_bits_per_pixel #V6
avs_bits_per_pixel.restype=ctypes.c_int
avs_bits_per_pixel.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_bytes_from_pixels=avidll.avs_bytes_from_pixels #V6
avs_bytes_from_pixels.restype=ctypes.c_int
avs_bytes_from_pixels.argtypes=[ctypes.POINTER(AVS_VideoInfo_C), ctypes.c_int]

avs_bmp_size=avidll.avs_bmp_size #V6
avs_bmp_size.restype=ctypes.c_int
avs_bmp_size.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

avs_row_size=avidll.avs_row_size #V6
avs_row_size.restype=ctypes.c_int
avs_row_size.argtypes=[ctypes.POINTER(AVS_VideoInfo_C), ctypes.c_int]

# Avisynth+ extensions
# fallback: simulations of missing avs+ functions
# returns False (0) if e.g. avs_is_rgb48 does not exists
is_XY_color_space_like_FUNC_TYPE = FUNCTYPE(ctypes.c_int, ctypes.POINTER(AVS_VideoInfo_C))
num_components_like_FUNC_TYPE = FUNCTYPE(ctypes.c_int, ctypes.POINTER(AVS_VideoInfo_C))
component_size_like_FUNC_TYPE = FUNCTYPE(ctypes.c_int, ctypes.POINTER(AVS_VideoInfo_C))
bits_per_component_like_FUNC_TYPE = FUNCTYPE(ctypes.c_int, ctypes.POINTER(AVS_VideoInfo_C))

def internal_fake_is_XY_returns_False(arg):
    return 0

def internal_fake_component_size(arg):
    return 1 # always 1 bytes for classic Avisynth

def internal_fake_num_components(arg):
    if avs_is_y8(arg) != 0: return 1 # Y only
    #if avs_is_rgb32(arg) != 0: return 4 # R,G,B,A
    if AVS_VideoInfo(arg).is_rgb32: return 4 # GPo 2021
    return 3 # all other is 3 (planes, components)

def internal_fake_bits_per_component(arg):
    return 8 # always 8 bits/component for classic Avisynth

def internal_fake_get_frame_props_2(arg1, arg2):
    return None

def internal_fake_get_frame_props_3(arg1, arg2, arg3):
    return None

def internal_fake_get_frame_props_5(arg1, arg2, arg3, arg4, arg5):
    return None

# AVS+ function in "safe mode" to accept classic Avisynth which have such no new functions
try: # AVS+ ?
    avs_is_rgb48=avidll.avs_is_rgb48 #AVS+
    avs_is_rgb48.restype=ctypes.c_int
    avs_is_rgb48.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_is_rgb48=is_XY_color_space_like_FUNC_TYPE(internal_fake_is_XY_returns_False) # fallback to always False

try:
    avs_is_rgb64=avidll.avs_is_rgb64 #AVS+
    avs_is_rgb64.restype=ctypes.c_int
    avs_is_rgb64.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_is_rgb64=is_XY_color_space_like_FUNC_TYPE(internal_fake_is_XY_returns_False) # fallback to always False

try:
    avs_is_444=avidll.avs_is_444 #AVS+
except:
    avs_is_444=avidll.avs_is_yv24 # fallback

avs_is_444.restype=ctypes.c_int
avs_is_444.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

try:
    avs_is_422=avidll.avs_is_422 #AVS+
except:
    avs_is_422=avidll.avs_is_yv16 # fallback
avs_is_422.restype=ctypes.c_int
avs_is_422.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

try:
    avs_is_420=avidll.avs_is_420 #AVS+
except:
    avs_is_420=avidll.avs_is_yv12 # fallback
avs_is_420.restype=ctypes.c_int
avs_is_420.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

try:
    avs_is_y=avidll.avs_is_y #AVS+
except:
    avs_is_y=avidll.avs_is_y8 # fallback
avs_is_y.restype=ctypes.c_int
avs_is_y.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]

try:
    avs_is_yuva=avidll.avs_is_yuva #AVS+
    avs_is_yuva.restype=ctypes.c_int
    avs_is_yuva.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_is_yuva=is_XY_color_space_like_FUNC_TYPE(internal_fake_is_XY_returns_False) # fallback to always False

try:
    avs_is_planar_rgb=avidll.avs_is_planar_rgb #AVS+
    avs_is_planar_rgb.restype=ctypes.c_int
    avs_is_planar_rgb.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_is_planar_rgb=is_XY_color_space_like_FUNC_TYPE(internal_fake_is_XY_returns_False) # fallback to always False

try:
    avs_is_planar_rgba=avidll.avs_is_planar_rgba #AVS+
    avs_is_planar_rgba.restype=ctypes.c_int
    avs_is_planar_rgba.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_is_planar_rgba=is_XY_color_space_like_FUNC_TYPE(internal_fake_is_XY_returns_False) # fallback to always False

try:
    avs_num_components=avidll.avs_num_components #AVS+
    avs_num_components.restype=ctypes.c_int
    avs_num_components.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_num_components=num_components_like_FUNC_TYPE(internal_fake_num_components)

try:
    avs_component_size=avidll.avs_component_size #AVS+
    avs_component_size.restype=ctypes.c_int
    avs_component_size.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_component_size=component_size_like_FUNC_TYPE(internal_fake_component_size) # always return 1

try:
    avs_bits_per_component=avidll.avs_bits_per_component #AVS+
    avs_bits_per_component.restype=ctypes.c_int
    avs_bits_per_component.argtypes=[ctypes.POINTER(AVS_VideoInfo_C)]
except:
    avs_bits_per_component=bits_per_component_like_FUNC_TYPE(internal_fake_bits_per_component) # always returns 8

# end of Avisynth+ extensions
# todo: move them to wrapper functions

avs_make_writable=avidll.avs_make_writable
avs_make_writable.restype=ctypes.c_int
avs_make_writable.argtypes=[AVS_ScriptEnvironment,
                            ctypes.POINTER(ctypes.POINTER(AVS_VideoFrame_C))]

avs_bit_blt=avidll.avs_bit_blt
avs_bit_blt.restype=None
avs_bit_blt.argtypes=[AVS_ScriptEnvironment,ctypes.POINTER(ctypes.c_ubyte),
                      ctypes.c_int,ctypes.POINTER(ctypes.c_ubyte),
                      ctypes.c_int,ctypes.c_int,ctypes.c_int]

SHUTDOWNFUNC = FUNCTYPE(ctypes.c_void_p, AVS_ScriptEnvironment)

avs_at_exit=avidll.avs_at_exit
avs_at_exit.restype=None
avs_at_exit.argtypes=[AVS_ScriptEnvironment,SHUTDOWNFUNC,ctypes.c_void_p]

avs_set_memory_max=avidll.avs_set_memory_max
avs_set_memory_max.restype=ctypes.c_int
avs_set_memory_max.argtypes=[AVS_ScriptEnvironment,ctypes.c_int]

avs_set_working_dir=avidll.avs_set_working_dir
avs_set_working_dir.restype=ctypes.c_int
avs_set_working_dir.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p]

avs_subframe_planar=avidll.avs_subframe_planar
avs_subframe_planar.restype=ctypes.POINTER(AVS_VideoFrame_C)
avs_subframe_planar.argtypes=[AVS_ScriptEnvironment,AVS_VideoFrame,ctypes.c_int,
                              ctypes.c_int,ctypes.c_int,ctypes.c_int,
                              ctypes.c_int,ctypes.c_int,ctypes.c_int]
#avs_subframe_planar.errcheck=CreateAVS_VideoFrameCT

avs_subframe=avidll.avs_subframe
avs_subframe.restype=ctypes.POINTER(AVS_VideoFrame_C)
avs_subframe.argtypes=[AVS_ScriptEnvironment,AVS_VideoFrame,ctypes.c_int,
                       ctypes.c_int,ctypes.c_int,ctypes.c_int]
#avs_subframe.errcheck=CreateAVS_VideoFrameCT

avs_invoke=avidll.avs_invoke
avs_invoke.restype=AVS_Value_C
avs_invoke.argtypes=[AVS_ScriptEnvironment,ctypes.c_char_p,
                     AVS_Value,ctypes.POINTER(ctypes.c_char_p)]

#IClip functions
avs_take_clip=avidll.avs_take_clip
avs_take_clip.restype=ctypes.c_void_p
avs_take_clip.argtypes=[AVS_Value, AVS_ScriptEnvironment]

avs_set_to_clip=avidll.avs_set_to_clip
avs_set_to_clip.restype=None
avs_set_to_clip.argtypes=[ctypes.POINTER(AVS_Value_C), AVS_Clip]

avs_clip_get_error=avidll.avs_clip_get_error
avs_clip_get_error.restype=ctypes.c_char_p
avs_clip_get_error.argtypes=[AVS_Clip]

avs_get_video_info=avidll.avs_get_video_info
avs_get_video_info.restype=ctypes.POINTER(AVS_VideoInfo_C)
avs_get_video_info.argtypes=[AVS_Clip]
#avs_get_video_info.errcheck=CreateAVS_VideoInfoCT

avs_get_frame=avidll.avs_get_frame
avs_get_frame.restype=ctypes.POINTER(AVS_VideoFrame_C)
avs_get_frame.argtypes=[AVS_Clip, ctypes.c_int]
#avs_get_frame.errcheck=CreateAVS_VideoFrameCT

avs_get_version=avidll.avs_get_version
avs_get_version.restype=ctypes.c_int
avs_get_version.argtypes=[AVS_Clip]

avs_get_parity=avidll.avs_get_parity
avs_get_parity.restype=ctypes.c_int
avs_get_parity.argtypes=[AVS_Clip, ctypes.c_int]

avs_get_audio=avidll.avs_get_audio
avs_get_audio.restype=ctypes.c_int
avs_get_audio.argtypes=[AVS_Clip,ctypes.c_void_p,ctypes.c_int64,ctypes.c_int64]

avs_set_cache_hints=avidll.avs_set_cache_hints
avs_set_cache_hints.restype=ctypes.c_int
avs_set_cache_hints.argtypes=[AVS_Clip,ctypes.c_int,ctypes.c_int]

avs_copy_clip=avidll.avs_copy_clip
avs_copy_clip.restype=ctypes.c_void_p
avs_copy_clip.argtypes=[AVS_Clip]

avs_release_clip=avidll.avs_release_clip
avs_release_clip.restype=None
avs_release_clip.argtypes=[AVS_Clip]

avs_new_c_filter=avidll.avs_new_c_filter
avs_new_c_filter.restype=ctypes.c_void_p
avs_new_c_filter.argtypes=[AVS_ScriptEnvironment,
                           ctypes.POINTER(ctypes.POINTER(FilterInfo)),
                           AVS_Value,
                           ctypes.c_int]


#VideoFrame functions
avs_copy_video_frame=avidll.avs_copy_video_frame
avs_copy_video_frame.restype=ctypes.POINTER(AVS_VideoFrame_C)
avs_copy_video_frame.argtypes=[AVS_VideoFrame]
#avs_copy_video_frame.errcheck=CreateAVS_VideoFrameCT

avs_get_pitch_p=avidll.avs_get_pitch_p #V6
avs_get_pitch_p.restype=ctypes.c_int
avs_get_pitch_p.argtypes=[ctypes.POINTER(AVS_VideoFrame_C), ctypes.c_int]

avs_get_row_size_p=avidll.avs_get_row_size_p #V6
avs_get_row_size_p.restype=ctypes.c_int
avs_get_row_size_p.argtypes=[ctypes.POINTER(AVS_VideoFrame_C), ctypes.c_int]

avs_get_height_p=avidll.avs_get_height_p #V6
avs_get_height_p.restype=ctypes.c_int
avs_get_height_p.argtypes=[ctypes.POINTER(AVS_VideoFrame_C), ctypes.c_int]

avs_get_read_ptr_p=avidll.avs_get_read_ptr_p #V6
avs_get_read_ptr_p.restype=ctypes.POINTER(ctypes.c_ubyte)
avs_get_read_ptr_p.argtypes=[ctypes.POINTER(AVS_VideoFrame_C), ctypes.c_int]

avs_is_writable=avidll.avs_is_writable #V6
avs_is_writable.restype=ctypes.c_int
avs_is_writable.argtypes=[ctypes.POINTER(AVS_VideoFrame_C)]

avs_get_write_ptr_p=avidll.avs_get_write_ptr_p #V6
avs_get_write_ptr_p.restype=ctypes.POINTER(ctypes.c_ubyte) # for BYTE * (restype must be ubyte)
avs_get_write_ptr_p.argtypes=[ctypes.POINTER(AVS_VideoFrame_C), ctypes.c_int]

avs_release_video_frame=avidll.avs_release_video_frame
avs_release_video_frame.restype=None
avs_release_video_frame.argtypes=[AVS_VideoFrame]

#AVS_Value functions
avs_copy_value=avidll.avs_copy_value
avs_copy_value.restype=None
avs_copy_value.argtypes=[ctypes.POINTER(AVS_Value_C), AVS_Value]

avs_release_value=avidll.avs_release_value
avs_release_value.restype=None
avs_release_value.argtypes=[AVS_Value]
AVS_Value.avs_release_value=avs_release_value

#### frame props ####

try:
    avs_get_frame_props_ro=avidll.avs_get_frame_props_ro
    avs_get_frame_props_ro.restype=ctypes.POINTER(AVS_Map_C)
    avs_get_frame_props_ro.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_VideoFrame_C)]
except:
    avs_get_frame_props_ro=internal_fake_get_frame_props_2

try:
    avs_get_frame_props_rw=avidll.avs_get_frame_props_rw
    avs_get_frame_props_rw.restype=ctypes.POINTER(AVS_Map_C)
    avs_get_frame_props_rw.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_VideoFrame_C)]
except:
    avs_get_frame_props_rw=internal_fake_get_frame_props_2

try:
    avs_prop_num_keys=avidll.avs_prop_num_keys
    avs_prop_num_keys.restype=ctypes.c_int
    avs_prop_num_keys.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C)]
except:
   avs_prop_num_keys=internal_fake_get_frame_props_2

try:
    avs_prop_num_elements=avidll.avs_prop_num_elements
    avs_prop_num_elements.restype=ctypes.c_int
    avs_prop_num_elements.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C), ctypes.c_char_p]
except:
    avs_prop_num_elements=internal_fake_get_frame_props_3

try:
    avs_prop_get_key=avidll.avs_prop_get_key
    avs_prop_get_key.restype=ctypes.c_char_p
    avs_prop_get_key.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C), ctypes.c_int]
except:
    avs_prop_get_key=internal_fake_get_frame_props_3

try:
    avs_prop_get_type=avidll.avs_prop_get_type
    avs_prop_get_type.restype=ctypes.c_char
    avs_prop_get_type.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C), ctypes.c_char_p]
except:
    avs_prop_get_type=internal_fake_get_frame_props_3

try:
    avs_prop_get_int=avidll.avs_prop_get_int
    avs_prop_get_int.restype=ctypes.c_int                                        # keyname, element_index, return error
    avs_prop_get_int.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
except:
    avs_prop_get_int=internal_fake_get_frame_props_5

try:
    avs_prop_get_float=avidll.avs_prop_get_float
    avs_prop_get_float.restype=ctypes.c_double                                     # keyname, element_index, return error
    avs_prop_get_float.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
except:
    avs_prop_get_int=internal_fake_get_frame_props_5

try:
    avs_prop_get_data=avidll.avs_prop_get_data
    avs_prop_get_data.restype=ctypes.c_char_p                                       # keyname, element_index, return error
    avs_prop_get_data.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
except:
    avs_prop_get_data=internal_fake_get_frame_props_5

try:
    avs_prop_get_data_size=avidll.avs_prop_get_data_size
    avs_prop_get_data_size.restype=ctypes.c_int                                        # keyname, element_index, return error
    avs_prop_get_data_size.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
except:
    avs_prop_get_data=internal_fake_get_frame_props_5

try:
    avs_clear_map=avidll.avs_clear_map
    avs_clear_map.resypes=None
    avs_clear_map.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C)]
except:
    avs_clear_map=internal_fake_get_frame_props_2

"""
try:
    avs_free_map=avidll.avs_prop_free_map
    avs_free_map.resypes=None
    avs_free_map.argtypes=[AVS_ScriptEnvironment, ctypes.POINTER(AVS_Map_C)]
except:
    avs_free_map=internal_fake_get_frame_props_1
"""

def test():
    env = AVS_ScriptEnvironment(6)
    print('environment created:', env)
    err = env.get_error()
    if err is not None:
        print('error:', err)
        return
    print('checking for interface 3:', env.check_version(3))
    print('checking for interface 33:', env.check_version(33))
    print(env.invoke('VersionString'))

    print('\nsome internal functions...')
    for function_name in env.get_var('$InternalFunctions$').split()[:10]:
        try:
            params = env.get_var('$Plugin!' + function_name + '!Param$')
        except AvisynthError as err:
            if str(err) != 'NotFound': raise
        else:
            print(' ', function_name, params)
    var_name, value = 'test var', 'some text'
    print('\nsetting a string variable with value {0}'.format(repr(value)))
    env.set_var(var_name, value)
    print('value retrieved:', repr(env.get_var(var_name))) # check save_string
    print('\ninvoking...')
    try:
#        ret = env.invoke('Version')
        ret = env.invoke('BlankClip', [100, 200, 300])
#        ret = env.invoke('Eval',
#                         ['assert(false, "assert message")', 'script title'])
    except AvisynthError as err:
        print('error:', env.get_error())
    else:
        if isinstance(ret, AVS_Clip):
            clip = ret
            AVS_Value(AVS_Value(clip, env), env).get_value() # test passing clip
            print(clip.get_video_info())
            frame = clip.get_frame(5)
            err = clip.get_error()
            if err:
                print('error:', err)
            else:
                print(frame)
                frame.get_read_ptr()[0:20]
        else:
            print('value:', ret)

if __name__ == '__main__':
    test()
