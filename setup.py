# AvsP - an AviSynth editor
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

# setup - AvsP py2exe setup script
#
# Dependencies:
#     Python (v2.7) (v3.7 support experimental, not finished)
#     wxPython (tested on v2.8 Unicode and v2.9, v3.0.2 as the latest "classic)
#               or 4.0.2: experimental not finished
#     py2exe (tested on v0.6.9)
# Additional dependencies for x86-64:
#     cffi (tested on v0.9.2)
#     pycparser (tested on v2.10)
#     Visual C++
#     avisynth_c.h (interface 5, or at least 3 + colorspaces from 5,
#                   tested with the header used by x264)
#
# Note:
# py2exe v0.6.10a1 (to be exact p2exe r687+) always includes w9xpopen.exe
# (even if excluded with 'dll_excludes')

import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import py2exe # unfortunately not after 3.4
except ImportError:
    raise ImportError

# use Nuitka or PyInstaller https://stackoverflow.com/questions/49831163/compile-python-3-6-script-to-standalone-exe-with-nuitka-on-windows-10

use_classic_wx = True # fix True at the moment: use pre v4.0.0 wxPython

if use_classic_wx:
  import wxversion
  wxversion.select('2.9.4') # GPo: 2.9.3.0 is very fine, 2.9.3.1 also ok
  # wxversion.select('3.0.2') #PF 20181221 #GPo not working, mouse wheel problems and other bugs
  import wx
else:
  # for wxPython v4.x (Phoenix): import specific version: 4.0.3,
  # raise error if does not exists
  import pkg_resources
  pkg_resources.require("wxPython==4.0.3")
  import wx

# for wxPython v4.x (Phoenix): import current
# import wx

import global_vars

def isVersion(rv):
    currentVersion = sys.version_info
    if currentVersion[0] == rv[0] and currentVersion[1] == rv[1]:
        pass
    else:
        return False
    return True

# Calling the 'checkInstallation' function checks if Python is >= 2.7 and < 3
requiredVersion27 = (2,7)
requiredVersion37 = (3,7)
is27 = isVersion(requiredVersion27)
is37 = isVersion(requiredVersion37)
if not is27 and not is37:
  sys.stderr.write( "[%s] - Error: Python interpreter must be 2.7 or 3.7\n" % (sys.argv[0]) )
  sys.exit(-1)


x86_64 = sys.maxsize > 2**32
if x86_64:
    import avisynth_cffi
    ext_modules = [avisynth_cffi.ffi.verifier.get_extension()]
    arch = 'AMD64'
    crt_version = 'amd64_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_750b37ff97f4f68b'
else:
    ext_modules = []
    arch = 'x86'
    crt_version = 'x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_bcb86ed6ac711f91'


manifest = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="{arch}"
    name="{prog}"
    type="win32"
  />
  <description>{prog}</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="asInvoker"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>%(extra)s
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="{arch}"
            publicKeyToken="1fc8b3b9a1e18e3b">
      </assemblyIdentity>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="{arch}"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
""".format(prog=global_vars.name, arch=arch)

# When gdiplus.dll is not found, find it in WinSxS folder.
# Files in the WinSxS folders are created and populated when you install various C++ Runtime
# Redistributables and contain runtime files and DLLs that some third party programs you installed
# may need, so you could have more, less or no WinSxS folders.
# WinSxS is the technology that lets you have multiple copies of different versions of files
# with the same name on your system at the same time.
# E.g. c:\Windows\WinSxS\wow64_microsoft.windows.gdiplus.systemcopy_31bf3856ad364e35_10.0.17134.1_none_d6afcd2e9398abe3\GdiPlus.dll
lib_extra = []
# classic wx has its own gdiplus.dll
# e.g. in c:\Python27\lib\site-packages\wx-3.0-msw\wx\gdiplus.dll
if use_classic_wx:
  if not x86_64:
    lib_extra.append(os.path.join(os.path.dirname(wx.__file__), 'gdiplus.dll'))

lib = []

data_files = [
        ('', 
            [
            'filterdb.dat',
            'readme.md',
            'changelog.txt',
            'copying.txt',
            'previewFilterExample.txt',
            'previewFilterExample.avs',
            'readme_Threads.txt',
            'readme_ResampleFilter.txt',
            'readme_ApplyFilters.txt',
            'readme_SplitClip.txt',
            'readme_NumberWheel.txt',
            'readme_d2v_based_template.txt',
            'readme_FastClip.txt',
            'readme_LocateFrame.txt',
            'readme_FullscreenZoom.txt',
            'readme_Audio.txt',
            'license_cpuid'
            ]
        ),
        ('lib', lib_extra),
        ('src',
            [
            'run.py',
            'avsp.py',
            'wxp.py',
            'dpi.py',
            'utils.py',
            'func.py',
            'cfunc.pyd',
            'avisynth.py',
            'avisynth_cffi.py',
            'pyavs.py',
            'pyavs_avifile.py',
            'build.py',
            'setup.py',
            'i18n.py',
            'AvsP.ico',
            'icons.py',
            'global_vars.py',
            'cpuid.py',
            'build_instructions_windows.txt',
            'avisynth_c.h' # or perhaps include it only for x64?
            ]
         ),
         ('src\\avs', 
            [ # or perhaps include them only for x64?
            'avs\\types.h',
            'avs\\config.h',
            'avs\\capi.h'
            ]
         )
 ]

# todo:
# Python 3.7 uses VS2015 (2017) redistributables
# msvcr140.dll, msvcp140.dll

# Include the Microsoft Visual C runtime DLLs for Python 2.6+
# v9.0.21022.8, available in the Microsoft Visual C++ 2008 Redistributable Package
# 32-bit: <https://www.microsoft.com/en-us/download/details.aspx?id=29>
# 64-bit: <https://www.microsoft.com/en-us/download/details.aspx?id=15336>
if is27:
  crt_dst_dir = 'Microsoft.VC90.CRT'
  crt_files = ('msvcm90.dll', 'msvcp90.dll', 'msvcr90.dll')
elif is37:
  crt_dst_dir = 'Microsoft.VC140.CRT'
  crt_files = ('msvcp140.dll', 'msvcr140.dll')

crt_dirs = (os.path.expandvars(os.path.join('%windir%', 'winsxs', crt_version)),
            sys.prefix, os.path.join(sys.prefix, 'DLLs'))
crt_paths = []
for file in crt_files:
    for dir in crt_dirs:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            crt_paths.append(path)
            break
    else:
        crt_paths.append(file)
#data_files.append((crt_dst_dir, crt_paths)) # it doesn't seem to work
data_files.append(('', crt_paths))

# If a resource file doesn't exist in the current directory, take it from its parent
for i, (dsr, files) in enumerate(data_files):
    for j, file in enumerate(files):
        if not os.path.isfile(file):
            basename = os.path.basename(file)
            if basename != file and os.path.isfile(basename):
                data_files[i][1][j] = basename
                continue
            file_up = os.path.join('..', basename)
            if os.path.isfile(file_up):
                data_files[i][1][j] = file_up
            else:
                exit("Couldn't find '%s'" % basename)

# Add whole directories, optionally filtering by extension and including explicitly some files
# If a directory doesn't exist within the current one, search in its parent
dirs = (
    ('help', None, None),
    ('translations', None, None),
    ('macros', ('.py', '.txt'), None),
    ('tools', ('.py', '.presets'), ('session_info.pyo', 'avs2avi.exe', 'avs2avi_src.zip'))
       )
for dir, ext_filter, include in dirs:
    if not os.path.isdir(dir):
        dir_up = os.path.join('..', dir)
        if os.path.isdir(dir_up):
            dir = dir_up
        else:
            exit("Couldn't find '%s' directory" % dir)
    data_files.extend(
        [(root.split(os.sep, 1)[1] if root.startswith('..') else root,
          [os.path.join(root, file) for file in files
                if (not ext_filter or os.path.splitext(file)[1] in ext_filter or
                    include and file in include)]
         ) for root, dirs, files in os.walk(dir)])

# Add also the C extension that will be generated on the same setup()
if x86_64:
    data_files.append(('', # XXX: this path shouldn't be hard-coded
        [os.path.join('build', 'lib.win-amd64-{0}.{1}'.format(*sys.version_info[:2]),
         'avisynth_cffi_ext.pyd')]))
    data_files.append('DecodeYUVtoRGB.dll')

# Generate the dist files
packages = []
includes = ['glob', 'shutil']
excludes = ["translation", "Tkconstants", "Tkinter", "tcl", 'pyreadline',
            'win32api', 'win32con', 'win32pipe', 'pywintypes', 'pyexpat']
dll_excludes = ['MSVCP90.dll', 'w9xpopen.exe', 'mswsock.dll', 'powrprof.dll',
                'KERNELBASE.dll', 'MSASN1.dll', 'MPR.dll', 'CRYPT32.dll']
if x86_64: # otherwise lextab and yacctab are generated on the working
    packages.extend(('pycparser',))  # directory on every start
else:
    excludes.extend(('avisynth_cffi',))
setup(
    name = global_vars.name,
    description = global_vars.description,
    version = global_vars.version,
    url = global_vars.url,
    license = global_vars.license,
    options = {"py2exe":{
        "compressed": True,
        "optimize": 1,
        "packages": packages,
        "includes": includes,
        "excludes": excludes,
        "dll_excludes": dll_excludes,
    }},
    zipfile = 'lib/library.zip',
    data_files = data_files,
    ext_modules= ext_modules,
    windows = [
        {
            'copyright' : global_vars.license,
            "script": "run.py",
            "icon_resources": [(1, "AvsP.ico")],
            "other_resources" : [(24, 1, manifest)],
        }
    ],
)

if is27:
    # Write the manifest file for the CRT DLLs
    manifest = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <!-- Copyright (c) Microsoft Corporation.  All rights reserved. -->
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
        <noInheritable/>
        <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="{arch}"
            publicKeyToken="1fc8b3b9a1e18e3b"
        />
        <file name="msvcr90.dll" /> <file name="msvcp90.dll" /> <file name="msvcm90.dll" />
    </assembly>'''.format(arch=arch)
    for i, arg in enumerate(sys.argv):
        if arg.lower() == '-d':
            dist_dir = sys.argv[i+1].strip('"')
            break
        else:
            dir = arg.lower().partition('--dist-dir=')[2]
            if dir:
                dist_dir = dir.strip('"')
                break
    else:
        dist_dir = 'dist'
    #f = open(os.path.join(dist_dir, crt_dst_dir, crt_dst_dir + '.manifest'), 'w') # it doesn't seem to work
    f = open(os.path.join(dist_dir, '', crt_dst_dir + '.manifest'), 'w')
    f.write(manifest)
    f.close()
elif is37:
    # Comment for Python 3.7
    # App-local deployment of the Universal CRT is supported.
    # To obtain the binaries for app-local deployment, install the Windows Software Development Kit
    #  (SDK) for Windows 10. The binaries will be installed to
    #  C:\Program Files (x86)\Windows Kits\10\Redist\ucrt.
    #  You will need to copy all of the DLLs with your app
    #  (note that the set of DLLs are necessary is different on different versions of Windows,
    #  so you must include all of the DLLs in order for your program to run on
    #  all supported versions of Windows)
    # c:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\
    pass

