#-------------------------------------------------------------------------------
# Name:        func.py
# Purpose:
#
# Author:      GPo
#
# Created:     23.10.2021
# Copyright:   (c) GPo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def GetMatrixName(idx):
    namedict = {
    0: 'RGB',
    1: 'BT.709',
    2: 'undef',
    #3: 'reserved',
    4: 'FCC T47',
    5: 'BT.470 B/G',
    6: 'BT.601',
    7: 'SMPTE ST 240',
    8: 'YCgCo',
    9: 'BT.2020ncl',
    10: 'BT.2020cl',
    11: 'SMPTE ST 2085',
    12: 'Chroma ncl',
    13: 'Chroma cl',
    14: 'BT.2100'
    }
    if idx in namedict.keys():
        return namedict[idx]
    return '..'

def GetColorPrimariesName(idx):
    namedict = {
    1: 'BT.709',
    2: 'undef',
    #3: 'undef',
    4: 'BT.470 M',
    5: 'BT.470 BG',
    6: 'SMPTE 170 M',
    7: 'SMPTE 240 M',
    8: 'Film',
    9: 'BT.2020',
    10: 'ST 428',
    11: 'ST 431-2',
    12: 'ST 432-1',
    22: 'jedec-p22'
    }
    if idx in namedict.keys():
        return namedict[idx]
    return '?'

def GetChromaLocationName(idx):
    namedict = {
    0: 'left',
    1: 'center',
    2: 'top-left',
    3: 'top',
    4: 'bottom-left',
    5: 'bottom'
    }
    if idx in namedict.keys():
        return namedict[idx]
    return '?'

def GetFieldBasedName(idx):
    namedict = {
    0:'progressive',
    1:'bottom-field',
    2:'top-field'
    }
    if idx in namedict.keys():
        return namedict[idx]
    return '?'

def GetTransferName(idx):
    namedict = {
    1:'709',
    2:'undef',
    4:'470m',
    5:'470bg',
    6:'601',
    7:'240m',
    8:'linear',
    9:'log100',
    10:'log316',
    11:'xvycc',
    13:'srgb',
    14:'2020_10',
    15:'2020_12',
    16:'st2084',
    18:'std-b67'
    }
    if idx in namedict.keys():
        return namedict[idx]
    return '?'

def GetColorRangeName(idx):
    namedict = {
    0:'full',
    1:'limited'
    }
    if idx in namedict.keys():
        return namedict[idx]
    return '?'

def GetGOPClosedName(idx):
    namedict = {
    0:'false',
    1:'true'
    }
    if idx in namedict.keys():
        return namedict[idx]
    return '?'

"""
def GetPropNameValue(key, value):
    propCharDict = {
        '_Matrix': func.GetMatrixName,
        '_Primaries': func.GetColorPrimariesName,
        '_ChromaLocation': func.GetChromaLocationName,
        '_FieldBased': func.GetFieldBasedName,
        '_Transfer': func.GetTransferName,
        '_ColorRange': func.GetColorRangeName,
        '_GOPClosed': func.GetGOPClosedName,
    }
    if key in propCharDict:
        return '[' + propCharDict[key](value) + ']'
    return ''
"""