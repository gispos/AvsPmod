# AvsP - an AviSynth editor
#
# Copyright 2007 Peter Jang <http://avisynth.nl/users/qwerpoi>
#           2010-2013 the AvsPmod authors <https://github.com/avspmod/avspmod>
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

# build - build script for AvsP
#
# Dependencies:
#     Python (tested on v2.6 and v2.7)
#     wxPython (tested on v2.8 Unicode and v2.9)
#     py2exe (tested on v0.6.9)
# Additional dependencies for x86-64:
#     cffi (tested on v0.9.2)
#     pycparser (tested on v2.10)
#     Visual C++
#     avisynth_c.h (interface 5, or at least 3 + colorspaces from 5,
#                   tested with the header used by x264)
# Optional:
#    editbin (only for x86-32)
#    UPX (only for x86-32)
#    7-zip
#
# Note:
# py2exe v0.6.10a1 (to be exact p2exe r687+) always includes w9xpopen.exe
# (even if excluded with 'dll_excludes')

import os
import sys
import platform
import atexit
import shutil
import tempfile
import zipfile
import subprocess
import re

import avsp
import i18n
import global_vars

# GPo, need do change the path for LargeAdressAware, editbin path hard coded
find_editbin = False  #when True search for editbin (original code)
editbinPath = r'C:\Users\GPo\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\VC\bin'

def isinpath(path):
    '''Check if a file is in PATH or in the working directory'''
    basename = os.path.basename(path)
    path = os.path.join(os.getcwdu(), basename)
    if os.path.isfile(path):
        return path
    for dir in os.environ['PATH'].split(os.pathsep):
        path = os.path.join(dir, basename)
        if os.path.isfile(path):
            return path

def main():
    # Define names and paths
    pythonexe = sys.executable
    x86_64 = sys.maxsize > 2**32
    zipname = '{0}_v{1}_({2}_{3}).zip'.format(global_vars.name,
        global_vars.version, platform.system(), 'x86-64' if x86_64 else 'x86-32')
    upx = os.path.join(os.environ['PROGRAMFILES'], 'upx', 'upx.exe')
    exe7z = os.path.join(os.environ['PROGRAMFILES'], '7-Zip', '7z.exe')

    tempdir = tempfile.mkdtemp()
    atexit.register(shutil.rmtree, tempdir)
    programdirname = os.path.join(tempdir, global_vars.name + '_64' if x86_64 else global_vars.name + '_32')

    # Create/update the master translation file
    print('\nCreating translation file...')
    if not i18n.main():
        return

    # Create the program executable using py2exe
    # todo: py2exe is not available for Python v3.7
    if os.system('""%s" -O setup.py py2exe -d %s"' % (pythonexe, programdirname)):
        return

    # Update the translation files in the temporal subdirectory
    i18n.UpdateTranslationFile(os.path.join(programdirname, 'translations'), version=global_vars.version)

    # Create/update 'macros_readme.txt' in the macros subdirectory
    avsp.GenerateMacroReadme(os.path.join(programdirname, 'macros', 'macros_readme.txt'))

    # Set the large address aware flag in the executable
    err = 0
    if find_editbin and not x86_64:
        re_vs = re.compile('VS\d+COMNTOOLS', re.I)
        for key, value in os.environ.iteritems():
            match = re_vs.match(key)
            if match:
                vs_path = value.rsplit(os.sep, 3)[0]
                editbin = os.path.join(vs_path, 'VC', 'bin', 'editbin.exe')
                if os.path.isfile(editbin):
                    dir = os.path.join(vs_path, 'Common7', 'IDE')
                    if os.path.isdir(dir):
                        os.environ['PATH'] += os.pathsep + dir
                        print('\nSetting large address aware flag...')
                        if os.system('""%s" /LARGEADDRESSAWARE "%s""' %
                                (editbin, os.path.join(programdirname, 'run.exe'))):
                            print('Failed')
                        else: break
        else:
            print("\neditbin not found.  Large address aware flag not set")
            err = 1

    elif not x86_64:
        # GPo, need do change the path for LargeAdressAware
        editbin = os.path.join(editbinPath, 'editbin.exe')
        print ('\nSetting large address aware flag...')
        if os.system('""%s" /LARGEADDRESSAWARE "%s""' % (editbin, os.path.join(programdirname, 'run.exe'))):
            print("\neditbin not found.  Large address aware flag not set")
            err = 1 #Breaks the upx, is error for LargAdressAware save time

    # Compress the files with UPX, if available
    # DISABLED ! getting errors on the exe
    """
    if x86_64:
        print("\nSkipping UPX'ing on x86-64 builds")
    elif  __debug__ or err == 1:
        print("\nDebug mode, skipping UPX'ing")
    else:
        if not os.path.isfile(upx):
            upx = isinpath('upx.exe')
        if upx:
            args = [upx, '--best', '--no-progress']
            for root, dirs, files in os.walk(programdirname):
                for file in files:
                    if os.path.splitext(file)[1] in ('.exe','.dll','.pyd'):
                        args.append(os.path.join(root, file))
            subprocess.call(args)
        else:
            print("\nUPX not found")
    """

    # Manage the files
    os.rename(os.path.join(programdirname, 'run.exe'),
              os.path.join(programdirname, '{0}.exe'.format(global_vars.name)))
    os.rename(os.path.join(programdirname, 'README.md'),
              os.path.join(programdirname, 'readme.txt'))
    atexit.register(shutil.rmtree, 'build')

    # Create the zip file for distribution.  Use 7-Zip if available
    if not os.path.isfile(exe7z):
        exe7z = isinpath('7z.exe')
    if exe7z:
        print('\nCreating 7z archive...')
        zipname = zipname.replace('.zip', '.7z')
        if os.path.isfile(zipname):
            os.remove(zipname)
        subprocess.call([exe7z, 'a', '-bd', '-r', zipname, programdirname])
    else:
        print('\nCreating ZIP archive...')
        if os.path.isfile(zipname):
            os.remove(zipname)
        zip = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(programdirname):
            for name in files:
                real_path = os.path.join(root, name)
                archive_path = os.path.relpath(real_path, tempdir)
                zip.write(real_path, archive_path)
        zip.close()

if __name__ == '__main__':
    main()
    raw_input('\nPress enter to continue')
