# -*- coding: utf-8 -*-

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

# i18n - internationalization and localization
# 
# Dependencies:
#     Python (tested on v2.6 and v2.7)
# Scripts:
#     global_vars.py (application info and other shared variables)

try:
    import __builtin__ as builtins
except ImportError:
    #The __builtin__ module was renamed to builtins in Python3.
    import builtins
import sys
import os
import os.path
import glob
import re

import global_vars

def _(s): return s
builtins._ = _ # Python3
# Python2 only: __builtin__._ = _

pythonexe = sys.executable 
pygettextpath = os.path.join(sys.prefix, 'Tools', 'i18n', 'pygettext.py')
toolsdir = 'tools'
macrosdir = 'macros'

def main(version=global_vars.version):
    """Generate __translation_new.py"""
    
    argsList = ['avsp.py wxp.py pyavs.py pyavs_avifile.py global_vars.py']
    # Get additional files to translate from the tools directory
    sys.path.insert(0, toolsdir)
    try:
        items = __import__('ToolsMenu').menuInfo
    except ImportError:
        items = []
    for item in items:
        if len(item) == 3:
            argsList.append(item)
    
    newlines = ['messages = {\n']
    messageSet = set()
    for args in argsList:
        newlines.extend(GenerateMessages(messageSet, args))
    
    # Include the macros' filenames
    newlines.append('\n    #--- Macros ---#\n')
    macro_list = []
    label_list = []
    global macrosdir
    if not os.path.isdir(macrosdir):
        macrosdir = os.path.join('..', macrosdir)
        if not os.path.isdir(macrosdir):
            exit('Macros directory not found')
    re_macro = re.compile(r'(?:\[\s*\d+\s*\]\s+)?((?P<chr>\w)(?P=chr){2}\s+)?\s*([^\[].+?)\s*\.py')
    for dirpath, dirnames, filenames in os.walk(macrosdir):
        for filename in filenames:
            match = re_macro.match(filename)
            if match and match.group(3) != '---':
                newlines.append('    "%s" : u"",\n' % match.group(3))
                messageSet.add('"%s"' % match.group(3))
                if not match.group('chr'):
                    macro_list.append('"%s" ' % os.path.abspath(os.path.join(dirpath, filename)))
                    label_list.append(match.group(3))
        for dirname in dirnames:
            newlines.append('    "%s" : u"",\n' % dirname)
    
    # Include the macros
    for macro, label in zip(macro_list, label_list):
        lines = GenerateMessages(messageSet, macro)
        if lines:
            newlines.append('\n    #--- Macro: %s ---#\n' % label)
            newlines.extend(lines)
    newlines.append('\n    #--- Macros - Extra ---#\n')
    
    newlines.append('}')

    f = open('__translation_new.py', 'w')
    f.write("new_translation_string = r'''")
    f.write('version = "%s"\n\n' % version)
    f.writelines(newlines)
    f.write("'''")
    f.close()
    
    return True

def GenerateMessages(messageSet, args):
    
    oldline = ''
    newlines = []
    from six import string_types # for Python 2 and 3
    if isinstance(args, string_types): # no basestring
        # V3: The builtin basestring abstract type was removed. 
        # Use str instead. The str and bytes types don’t have functionality enough in common to warrant 
        # a shared base class. The 2to3 tool replaces every occurrence of basestring with str.
        os.system('""%s" "%s" %s"' % (pythonexe, pygettextpath, args))
    else:
        filename, menuLabel, statusString = args
        filename += '.py'
        fullname = os.path.join(toolsdir, filename)
        s = '\n    #--- Tool: %s ---#\n' % (filename)
        newlines.append(s)
        s = '    "%s" : u"",\n' % (menuLabel)
        newlines.append(s)
        s = '    "%s" : u"",\n' % (statusString)
        newlines.append(s)
        os.system('""%s" "%s" %s"' % (pythonexe, pygettextpath, fullname))
    f = open('messages.pot', 'r')
    lines = f.readlines()
    f.close()
    os.remove('messages.pot')
    multiline = False
    for i, line in enumerate(lines):
        line = line.strip()
        if not multiline:
            if line.startswith('msgid '):
                text = line.split('msgid ')[1]
                if text.strip('"'):
                    if oldline.startswith('#:') and text not in messageSet:
                        #~ comment = ' %s' % oldline
                        #~ s = '    %s : u"",%s\n' % (text, comment)
                        s = '    %s : u"",\n' % (text)
                        newlines.append(s)
                        messageSet.add(text)
                else:
                    multiline = i
                    text = '"'
            oldline = line
        else:
            if not line.startswith('msgstr '):
                text += line.strip('"')
            else:
                text += '"'
                if i - multiline > 1 and text not in messageSet:
                    s = '    %s : u"",\n' % (text)
                    newlines.append(s)
                    messageSet.add(text)
                multiline = False
    return newlines

def UpdateTranslationFile(dir, lang=None, version=global_vars.version):
    try:
        from __translation_new import new_translation_string
    except ImportError:
        if hasattr(sys,'frozen'):
            raise
        else:
            main(version)
            from __translation_new import new_translation_string
    newmark = ' # New in v%s' % version
    # Get the text from the translation file
    file_list = ([os.path.join(dir, 'translation_%s.py' % lang)] if lang
                 else glob.glob(os.path.join(dir, 'translation_*.py')))
    for filename in file_list:
        if os.path.isfile(filename):
            f = open(filename, 'r')
            txt = f.read()
            f.close()
        else:
            txt = ''
        # Setup the new text...
        oldMessageDict = {}
        oldMessageDict2 = {}
        allMessagesMatched = True
        if not txt.strip():
            newmark = ''
            newlines = (
            '# -*- coding: utf-8 -*-\n'
            '\n'
            '# This file is used to translate the messages used in the AvsPmod interface.\n'
            '# To use it, make sure it is named "translation_lng.py" where "lng" is the \n'
            '# three-letter code corresponding to the language that is translated to \n'
            '# (see <http://www.loc.gov/standards/iso639-2/php/code_list.php>), \n'
            '# and is placed in the "%s" subdirectory.\n' % os.path.basename(dir) +
            '# \n'
            '# Simply add translated messages next to each message (any untranslated \n'
            '# messages will be shown in English).  You can type unicode text directly \n'
            '# into this document - if you do, make sure to save it in the appropriate \n'
            '# format.  If required, you can change the coding on the first line of this \n'
            '# document to a coding appropriate for your translated language. DO NOT \n'
            '# touch line breaks (\\n) and any words inside formatted strings (ie, any \n'
            '# portions of the text which look like {...}, %(...)s, %(...)i, etc.)\n'
            ).split('\n')
            extra_txt = None
        else:
            newlines = []
            boolStartLines = True
            re_mark = re.compile(r'(.*(?<![\'"])[\'"],)\s*#')
            txt, extra_sep, extra_txt = txt.partition('\n    #--- Macros - Extra ---#\n')
            for line in txt.split('\n'):
                # Copy the start lines
                if line.strip() and not line.lstrip('\xef\xbb\xbf').strip().startswith('#'):
                    boolStartLines = False
                if boolStartLines:
                    newlines.append(line)
                # Get the key
                splitline = line.split(' : ', 1)
                if len(splitline) == 2:
                    key = splitline[0].strip()
                    match = re_mark.match(line)
                    oldMessageDict[key] = match.group(1) if match else line
                    # Heuristically add extra keys for similar enough messages
                    if splitline[1].strip().startswith('u"'):
                        rawkey = key.strip('"')
                        splitvalue = splitline[1].strip().split('"')
                        if rawkey.endswith(':'):
                            key2 = '"%s"' % rawkey.rstrip(':')
                            splitvalue[1] = splitvalue[1].rstrip(':')
                            line2 = '    ' + key2 + ' : ' + '"'.join(splitvalue)
                            oldMessageDict2[key2] = line2
                        elif rawkey.endswith(' *'):
                            key2 = '"%s"' % rawkey.rstrip(' *')
                            splitvalue[1] = splitvalue[1].rstrip(' *')
                            line2 = '    ' + key2 + ' : ' + '"'.join(splitvalue)
                            oldMessageDict2[key2] = line2
                        elif rawkey and (rawkey[0].isspace() or rawkey[-1].isspace()):
                            key2 = '"%s"' % rawkey.strip()
                            splitvalue[1] = splitvalue[1].strip()
                            line2 = '    ' + key2 + ' : ' + '"'.join(splitvalue)
                            oldMessageDict2[key2] = line2
        # Get the new translation strings and complete the new text
        curlines = new_translation_string.split('\n')
        for line in curlines:
            splitline = line.split(' : ')
            if line.startswith('    ') and len(splitline) > 1:
                key = splitline[0].strip()
                if key in oldMessageDict:
                    newlines.append(oldMessageDict[key])
                elif key in oldMessageDict2:
                    newlines.append(oldMessageDict2[key])
                else:
                    newlines.append(line+newmark)
                    allMessagesMatched = False
            else:
                newlines.append(line)
        if extra_txt:
            newlines[-1] = extra_txt
        
        # Overwrite the text file with the new data
        f = open(filename, 'w')
        f.write('\n'.join(newlines))
        f.close()
    else:
        allMessagesMatched = True
    return not allMessagesMatched

def display_name(code):
    """Return the native language name of an ISO 639-2 language code"""
    return language_names.get(code, code)

language_names = {
    "aar": u"Qafara",
    "abk": u"Аҧсуа",
    "ave": u"avesta",
    "afr": u"Afrikaans",
    "aka": u"akana",
    "amh": u"አማርኛ",
    "arg": u"aragonés",
    "ara": u"العربية",
    "asm": u"অসমীয়া",
    "ava": u"авар мацӀ",
    "aym": u"aymar aru",
    "aze": u"Azərbaycanca",
    "bak": u"башҡорт теле",
    "bel": u"Беларуская мова",
    "bul": u"български език",
    "bih": u"भोजपुरी",
    "bis": u"Bislama",
    "bam": u"bamanankan",
    "ben": u"বাংলা",
    "tib": u"བོད་ཡིག",
    "bre": u"brezhoneg",
    "bos": u"bosanski jezik",
    "cat": u"català",
    "che": u"нохчийн мотт",
    "cha": u"Chamoru",
    "cos": u"corsu",
    "cre": u"ᓀᐦᐃᔭᐍᐏᐣ",
    "cze": u"čeština",
    "chu": u"ѩзыкъ словѣньскъ",
    "chv": u"чӑваш чӗлхи",
    "wel": u"Cymraeg",
    "dan": u"dansk",
    "ger": u"Deutsch",
    "div": u"ދިވެހިބަސ",
    "dzo": u"རྫོང་ཁ",
    "ewe": u"Ɛʋɛgbɛ",
    "gre": u"Ελληνικά",
    "eng": u"English",
    "epo": u"Esperanto",
    "spa": u"español",
    "est": u"eesti keel",
    "baq": u"euskara",
    "per": u"فارسی",
    "ful": u"Fulfulde",
    "fin": u"suomi",
    "fij": u"vosa Vakaviti",
    "fao": u"føroyskt",
    "fra": u"français",
    "fre": u"français",
    "fry": u"frysk",
    "gle": u"Gaeilge",
    "gla": u"Gàidhlig",
    "glg": u"Galego",
    "grn": u"Avañe'ẽ",
    "guj": u"ગુજરાતી",
    "glv": u"Gaelg",
    "hau": u"Hausancī",
    "heb": u"עִבְרִית",
    "hin": u"हिन्दी",
    "hmo": u"Hiri Motu",
    "hrv": u"hrvatski jezik",
    "hat": u"Kreyòl ayisyen",
    "hun": u"magyar",
    "arm": u"Հայերեն լեզու",
    "her": u"Otjiherero",
    "ina": u"interlingua",
    "ind": u"Bahasa Indonesia",
    "ile": u"Interlingue",
    "ibo": u"Igbo",
    "iii": u"ꆇꉙ",
    "ipk": u"Iñupiaq",
    "ido": u"Ido",
    "ice": u"íslenska",
    "ita": u"italiano",
    "iku": u"ᐃᓄᒃᑎᑐᑦ",
    "jpn": u"日本語",
    "jav": u"basa Jawa (ꦧꦱꦗꦮ)",
    "geo": u"ქართული ენა (kartuli ena)",
    "kon": u"Kikongo",
    "kik": u"Gĩkũyũ",
    "kua": u"kuanyama",
    "kaz": u"Қазақ тілі",
    "kal": u"kalaallisut",
    "khm": u"ភាសាខ្មែរ",
    "kan": u"ಕನ್ನಡ",
    "kor": u"한국어 (韓國語)",
    "kau": u"kanuri",
    "kas": u"कॉशुर",
    "kur": u"Kurdî",
    "kom": u"коми кыв",
    "cor": u"Kernewek",
    "kir": u"кыргыз тили",
    "lat": u"latine",
    "ltz": u"Lëtzebuergesch",
    "lug": u"Luganda",
    "lim": u"Limburgs",
    "lin": u"lingala",
    "lao": u"ພາສາລາວ",
    "lit": u"lietuvių kalba",
    "lub": u"",
    "lav": u"latviešu valoda",
    "mlg": u"Malagasy fiteny",
    "mah": u"Kajin M̧ajeļ",
    "mao": u"te reo Māori",
    "mac": u"македонски јазик",
    "mal": u"മലയാളം",
    "mon": u"монгол хэл",
    "mar": u"मराठी",
    "may": u"bahasa Melayu",
    "mlt": u"Malti",
    "bur": u"မြန်မာစာ",
    "nau": u"Ekakairũ Naoero",
    "nob": u"bokmål",
    "nde": u"isiNdebele",
    "nep": u"नेपाली",
    "ndo": u"Owambo",
    "dut": u"Nederlands",
    "nno": u"nynorsk",
    "nor": u"norsk",
    "nbl": u"isiNdebele",
    "nav": u"Diné bizaad",
    "nya": u"chiCheŵa",
    "oci": u"Occitan",
    "oji": u"ᐊᓂᔑᓇᐯᒧᐏᐣ (Anishinaabemowin)",
    "orm": u"Afaan Oromoo",
    "ori": u"ଓଡ଼ିଆ",
    "oss": u"ирон ӕвзаг",
    "pan": u"ਪੰਜਾਬੀ",
    "pli": u"पालि",
    "pol": u"polski",
    "pus": u"پښتو",
    "por": u"português",
    "que": u"Runa Simi",
    "roh": u"rumantsch grischun",
    "run": u"Rundi",
    "rum": u"română",
    "rus": u"русский язык",
    "kin": u"Ikinyarwanda",
    "san": u"संस्कृतम्",
    "srd": u"sardu",
    "snd": u"سنڌي، سندھی",
    "sme": u"sámi",
    "sag": u"yângâ tî sängö",
    "sin": u"සිංහල",
    "slo": u"slovenčina",
    "slv": u"slovenščina",
    "smo": u"gagana fa'a Samoa",
    "sna": u"chiShona",
    "som": u"Soomaaliga",
    "alb": u"Shqip",
    "srp": u"српски језик",
    "ssw": u"siSwati",
    "sot": u"Sesotho",
    "sun": u"basa Sunda",
    "swe": u"svenska",
    "swa": u"Kiswahili",
    "tam": u"தமிழ்",
    "tel": u"తెలుగు",
    "tgk": u"тоҷикӣ",
    "tha": u"ภาษาไทย",
    "tir": u"ትግርኛ",
    "tuk": u"Түркмен",
    "tgl": u"Wikang Tagalog",
    "tsn": u"Setswana",
    "ton": u"faka-Tonga",
    "tur": u"Türkçe",
    "tso": u"Xitsonga",
    "tat": u"татарча",
    "twi": u"Twi",
    "tah": u"te reo Tahiti",
    "uig": u"Uyƣurqə",
    "ukr": u"українська мова",
    "urd": u"اردو",
    "uzb": u"O'zbek",
    "ven": u"Tshivenḓa",
    "vie": u"Tiếng Việt",
    "vol": u"Volapük",
    "wln": u"walon",
    "wol": u"Wolof",
    "xho": u"isiXhosa",
    "yid": u"ייִדיש",
    "yor": u"Yorùbá",
    "zha": u"Saɯ cueŋƅ",
    "chi": u"漢語",
    "zul": u"isiZulu",
    }

if __name__ == '__main__':
    main()
