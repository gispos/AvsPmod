# AvsP - an AviSynth editor
#
# Copyright 2012, 2013 the AvsPmod authors <https://github.com/avspmod/avspmod>
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

# global_vars - shared global variables
#
# Dependencies:
#     Python (tested on v2.6 and v2.7)

try: _
except NameError: _ = lambda s:s

# Application info
name = 'AvsPmod'
description = _('An AviSynth script editor')
url = 'http://avspmod.github.io/'
url2 = 'https://github.com/gispos/AvsPmod/'
license = 'GNU GPL v2'
version = '2.7.3.2'

# stores the dpi scalling factor on startup
ppi_factor = 1.0

# Used to pass the shared library location to avisynth.py, don't touch
avisynth_library_dir = ''

# This will be improved on the future refactoring for wxPython Phoenix
# and VapourSynth
options = {}

