# -*- coding: utf-8 -*-

# This file is used to translate the messages used in the AvsPmod interface.
# To use it, make sure it is named "translation_lng.py" where "lng" is the 
# three-letter code corresponding to the language that is translated to 
# (see <http://www.loc.gov/standards/iso639-2/php/code_list.php>), 
# and is placed in the "translations" subdirectory.
# 
# Simply add translated messages next to each message (any untranslated 
# messages will be shown in English).  You can type unicode text directly 
# into this document - if you do, make sure to save it in the appropriate 
# format.  If required, you can change the coding on the first line of this 
# document to a coding appropriate for your translated language. DO NOT 
# touch line breaks (\n) and any words inside formatted strings (ie, any 
# portions of the text which look like {...}, %(...)s, %(...)i, etc.)
#
# Данный файл используется для перевода сообщений, используемых в интерфейсе AvsP.
# Чтобы использовать его, убедитесь, что он назван "translation.py" и лежит в той же папке,
# что и AvsP.exe.  Просто добавьте переведенные сообщения после каждого сообщения
# (любое непереведенное сообщение будет показано на английском).  Вы можете вводить
# текст в кодировке unicode прямо в этом документе - если так, будьте уверены сохранить его
# в соответствующем формате (кодировке). Если требуется, вы можете изменить кодировку 
# в первой сточке данного документа на кодировку подходящую для вашего языка перевода.
# (Фактически для русского языка можно использовать редакторы типа Блокнот в Win2000 и WinXP.) 
# НЕ ПЕРЕВОДИТЕ любые слова внутри форматированных строк (то есть, любые части
# текста, которые выглядят подобно {...}, %(...)s, %(...)i, и т.п.)

# Russian interface file for AvsP editor by qwerpoi, http://avisynth.nl/users/qwerpoi
# Translated by Fizick 19.09.2006-11.03.2007 for AvsP v1.3.7, http://avisynth.org.ru/avsp

version = "2.6.1.5"

messages = {
    "AviSynth script" : u"", # New in v2.3.0
    "AviSynth fonts and colors" : u"", 
    "Background" : u"Фон", 
    "Font" : u"Шрифт", 
    "Text color" : u"Цвет текста", 
    "Select a predefined theme" : u"", # New in v2.5.1
    "Only change colours" : u"", # New in v2.5.1
    "When selecting a theme, don't change current fonts" : u"", # New in v2.5.1
    "OK" : u"Да", 
    "Cancel" : u"Отменить ",
    "Page:" : u"", # New in v2.3.1
    "Page: %d" : u"", # New in v2.3.1
    "Scrap Window" : u"Окно заметок",
    "Undo" : u"Отмена",
    "Redo" : u"Повтор",
    "Cut" : u"Вырезать",
    "Copy" : u"Копировать",
    "Paste" : u"Вставить",
    "Select all" : u"Выделить все",
    "Refresh" : u"Обновить",
    "Insert frame #" : u"Вставить номер кадра",
    "Save to file..." : u"Сохранить в файл...",
    "Clear all" : u"Очистить все",
    "Toggle scrap window" : u"Переключить окно заметок",
    "Save script" : u"Сохранить скрипт",
    "Error: no contextMenu variable defined for window" : u"Ошибка: переменная contextMenu не определена для окна",
    "Text document" : u"", # New in v2.3.0
    "All files" : u"", # New in v2.3.0
    "Save scrap text" : u"Сохранить текст заметок",
    "This field must contain a value!" : u"Данное поле должно содержать величину!",
    "This slider label already exists!" : u"Данная метка ползунка уже существует!",
    "Invalid slider label modulo syntax!" : u"Неверный синтаксис метки модуля ползунка",
    "This field must contain a number!" : u"Данное поле дожно содержать число!",
    "The min value must be less than the max!" : u"Минимальная величина должна быть меньше максимальной!",
    "The initial value must be between the min and the max!" : u"Начальная величина должна быть между минимумом и максимумом!",
    "The min value must be a multiple of %(mod)s!" : u"Мин. значение должно быть кратно %(mod)s!",
    "The max value must be a multiple of %(mod)s!" : u"Макс. значение должно быть кратно %(mod)s!",
    "The initial value must be a multiple of %(mod)s!" : u"Начальное значение должно быть кратно %(mod)s!",
    "The difference between the min and max must be greater than %(mod)s!" : u"Разница между мин. и макс. должна быть больше чем %(mod)s!",
    "Error" : u"Ошибка",
    "Define user slider" : u"Определить пользовательский ползунок",
    "Slider label:" : u"Метка ползунка:",
    "Min value:" : u"Минимальное значение:",
    "Max value:" : u"Максимальное значение:",
    "Initial value:" : u"Начальное значение:",
    "Add or override AviSynth functions in the database" : u"", # New in v2.2.1
    "Core filters" : u"", # New in v2.2.1
    "Plugins" : u"", # New in v2.2.1
    "User functions" : u"", # New in v2.2.1
    "Script functions" : u"", # New in v2.2.1
    "Clip properties" : u"", # New in v2.2.1
    "New function" : u"", # New in v2.2.1
    "Edit selected" : u"", # New in v2.2.1
    "Delete selected" : u"", # New in v2.2.1
    "Select installed" : u"", # New in v2.2.1
    "Import" : u"", # New in v2.4.2
    "Import from files" : u"", # New in v2.2.1
    "Import from wiki" : u"", # New in v2.4.2
    "Export customizations" : u"", # New in v2.2.1
    "Clear customizations" : u"", # New in v2.2.1
    "Clear manual presets" : u"", # New in v2.2.1
    "When importing, don't show the choice dialog" : u"", # New in v2.2.1
    "Edit function information" : u"", # New in v2.2.1
    "Name:" : u"", # New in v2.2.1
    "Type:" : u"", # New in v2.2.1
    "clip property" : u"свойство клипа", 
    "core filter" : u"", # New in v2.2.1
    "plugin" : u"", # New in v2.2.1
    "script function" : u"", # New in v2.2.1
    "user function" : u"", # New in v2.2.1
    "Arguments:" : u"", # New in v2.2.1
    "define sliders" : u"", # New in v2.2.1
    "reset to default" : u"", # New in v2.2.1
    "Slider information" : u"", # New in v2.2.1
    "Preset:" : u"Предустановка",
    "Auto-generate" : u"", # New in v2.2.1
    "Filter name already exists!" : u"", # New in v2.2.1
    "Invalid filter name!" : u"", # New in v2.2.1
    "Renaming not allowed!" : u"", # New in v2.2.1
    "You must use dllname_function naming format for plugins!" : u"", # New in v2.2.1
    "Long name" : u"", # New in v2.5.0
    "Short name" : u"", # New in v2.5.0
    "Both" : u"", # New in v2.5.0
    "Only long names" : u"", # New in v2.5.0
    "Only short names" : u"", # New in v2.5.0
    "All names" : u"", # New in v2.5.0
    "Open Customization files, Avisynth scripts or Avsp options files" : u"", # New in v2.2.1
    "All supported" : u"", # New in v2.3.0
    "Customization file" : u"", # New in v2.3.0
    "AvsP data" : u"", # New in v2.3.0
    "Unrecognized files" : u"", # New in v2.2.1
    "Select the functions to import" : u"", # New in v2.4.2
    "Check selected" : u"", # New in v2.4.2
    "Check all" : u"", # New in v2.4.2
    "Check all in this file" : u"", # New in v2.4.2
    "Check all not customized" : u"", # New in v2.4.2
    "Uncheck selected" : u"", # New in v2.4.2
    "Uncheck all" : u"", # New in v2.4.2
    "Uncheck all in this file" : u"", # New in v2.4.2
    "Uncheck all customized" : u"", # New in v2.4.2
    "Red - a customized function already exists." : u"", # New in v2.2.1
    "Invalid plugin function name \"{name}\". Must be \"pluginname_functionname\"." : u"", # New in v2.5.1
    "No customizations to export!" : u"", # New in v2.2.1
    "Save filter customizations" : u"", # New in v2.2.1
    "This will delete all filter customizations. Continue?" : u"", # New in v2.2.1
    "Warning" : u"Предупреждение",
    "This will delete all manually defined presets. Continue?" : u"", # New in v2.2.1
    "Do you really want to delete this custom filter?" : u"", # New in v2.5.0
    "Do you really want to reset this filter?" : u"", # New in v2.5.0
    "Edit filter database" : u"", # New in v2.2.1
    "Default" : u"По умолчанию",
    "Min value" : u"Минимальное значение",
    "Max value" : u"Максимальное значение",
    "Step size" : u"", # New in v2.2.1
    "Value list (comma separated)" : u"", # New in v2.2.1
    "Value must be True or False!" : u"", # New in v2.2.1
    "Export filter customizations" : u"Экспорт настроенных фильтров",
    "Import filter customizations" : u"Импорт настроенных фильтров",
    "Select filters to export:" : u"Выбрать фильтры для экспорта:",
    "Select filters to import from the file:" : u"Выбрать фильтры для импорта из файла:",
    "Overwrite all data" : u"Переписать все данные",
    "You must select at least one filter!" : u"Вы должны быбрать по крайней мере один фильтр",
    "Error: minValue must be less than maxValue" : u"Ошибка: мин. величина должна быть меньше чем макс. величина",
    "New File" : u"Новый файл",
    "Windows Bitmap" : u"", # New in v2.3.0
    "Animation" : u"", # New in v2.3.0
    "JPEG" : u"", # New in v2.3.0
    "Zsoft Paintbrush" : u"", # New in v2.3.0
    "Portable Network Graphics" : u"", # New in v2.3.0
    "Netpbm" : u"", # New in v2.3.0
    "Tagged Image File" : u"", # New in v2.3.0
    "ASCII Text Array" : u"", # New in v2.3.0
    "Windows Icon" : u"", # New in v2.3.0
    "Windows Cursor" : u"", # New in v2.4.0
    "Frame" : u"Кадр",
    "fps" : u"кадр/с",
    "A crash detected at the last running!" : u"", # New in v2.2.1
    "&Zoom" : u"", # New in v2.2.1
    "Damaged {0}. Using default settings." : u"", # New in v2.4.0
    "%s translation file updated with new messages to translate" : u"", # New in v2.3.0
    "Translation updated" : u"", # New in v2.3.0
    "%s translation file updated.  No new messages to translate." : u"", # New in v2.3.0
    "%s language couldn't be loaded" : u"", # New in v2.3.0
    "Solarized light" : u"", # New in v2.5.1
    "Solarized dark" : u"", # New in v2.5.1
    "Zenburn" : u"", # New in v2.5.1
    "Cannot read the avisynth plugins directory from the registry\n" : u"", # New in v2.6.1.5
    "HKLM\\Software\\Avisynth'plugindir2_5' or 'plugindir+' is missing or wrong.\n\n" : u"", # New in v2.6.1.5
    "You should set the plugins path under options manually or register it." : u"", # New in v2.6.1.5
    "Alternatively, specify now its directory." : u"", # New in v2.4.0
    "Select the {0} directory" : u"", # New in v2.4.0
    "Make sure you have AviSynth installed and that there are no unstable plugins or avsi files in the AviSynth plugins directory." : u"", # New in v2.2.1
    "Error loading AviSynth!" : u"", # New in v2.2.1
    "Paths" : u"", # New in v2.2.1
    "Available variables: %programdir%, %avisynthdir%, %pluginsdir%" : u"", # New in v2.4.0
    "Choose a different version than the installed" : u"", # New in v2.4.0
    "Use a custom AviSynth directory" : u"", # New in v2.4.0
    "Alternative location of avisynth.dll/avxsynth.so" : u"", # New in v2.4.0
    "Custom AviSynth directory:" : u"", # New in v2.4.0
    "Leave blank for reset or choose a directory for manually set or for register" : u"", # New in v2.6.1.5
    "Disable autoload, set manually" : u"", # New in v2.6.1.5
    "If plugins autoload fails set the path manually. Read only. Only for proper program functions" : u"", # New in v2.6.1.5
    "Register the plugins directory" : u"", # New in v2.6.1.5
    "This changes the plugins directory for Avisynth itself. On Windows Registry values in HKLM are changed." : u"", # New in v2.6.1.5
    "Override the current working directory" : u"", # New in v2.4.0
    "Use a custom working directory" : u"", # New in v2.4.0
    "For all scripts" : u"", # New in v2.4.0
    "Use the custom directory also for scripts saved to file, instead of its parent" : u"", # New in v2.4.0
    "Specify an alternative working directory" : u"", # New in v2.4.0
    "Working directory:" : u"", # New in v2.4.0
    "External player:" : u"Внешний проигрыватель:",
    "Location of external program for script playback" : u"Расположение внешней программы для проигрывания скриптов",
    "Executable files" : u"", # New in v2.3.0
    "Additional arguments when running the external player" : u"Дополнительные аргументы при выполнении внешнего проигрывателя", 
    "External player extra args:" : u"Доп. аргументы внешнего проигрывателя", 
    "Avisynth help file/url:" : u"Файл/ссылка помощи Avisynth",
    "Location of the avisynth help file or url" : u"Расположение файла справки Avisynth или ссылки",
    "Documentation search paths:" : u"Пути поиска документации",
    "Specify which directories to search for docs when you click on a filter calltip" : u"Укажите в каких папках искать документы, когда Вы щелкните на подсказке для фильтра",
    "Documentation search url:" : u"", # New in v2.2.1
    "The web address to search if docs aren't found (the filter's name replaces %filtername%)" : u"", # New in v2.2.1
    "Text" : u"", # New in v2.2.1
    "Highlight the text as if it wasn't enclosed by triple quotes" : u"", # New in v2.5.1
    "Style inside triple-quoted strings" : u"", # New in v2.5.1
    "Prefer functions over variables" : u"", # New in v2.5.0
    "When a word could be either a function or a variable, highlight it as function" : u"", # New in v2.5.0
    "Don't allow lines wider than the window" : u"Не допускать строки шире чем окно", 
    "Wrap text" : u"Перенос текста",
    "Draw lines at fold points" : u"", # New in v2.2.1
    "For code folding, draw a line underneath if the fold point is not expanded" : u"", # New in v2.2.1
    "Check to insert actual tabs instead of spaces when using the Tab key" : u"Отметьте, чтобы вставлять табуляцию вместо пробелов при использовании клавиши Tab",
    "Use tabs instead of spaces" : u"Использовать табуляцию вместо пробелов",
    "Set the size of the tabs in spaces" : u"Установить размер табуляции в пробелах",
    "Tab width" : u"Ширина табуляции",
    "Initial space to reserve for the line margin in terms of number of digits. Set it to 0 to disable showing line numbers" : u"", # New in v2.3.1
    "Line margin width" : u"Ширина отступа строк",
    "Show filter calltips" : u"Показывать подсказки для фильтра",
    "Turn on/off automatic tips when typing filter names" : u"Включить/выключить автоматические подсказки при наборе имен фильтров",
    "Always show calltips any time the cursor is within the filter's arguments" : u"Всегда показывать подсказки во время нахождения курсора на аргументах фильтра", 
    "Frequent calltips" : u"Частые подсказки",
    "Show autocomplete on capital letters" : u"", # New in v2.2.1
    "Turn on/off automatic autocomplete list when typing words starting with capital letters" : u"Включить/выключить список автоматического автозавершения при наборе слов, начинающихся с заглавных букв",
    "Amount of letters typed" : u"", # New in v2.3.0
    "Show autocomplete list when typing a certain amount of letters" : u"", # New in v2.2.1
    "Autocomplete" : u"Автозавершение",
    "AviSynth user function database" : u"", # New in v2.4.2
    "Select what functions beside internal and user-defined will be included in the database" : u"", # New in v2.4.2
    "Autoloaded plugin functions" : u"", # New in v2.4.2
    "Include the functions on autoloaded plugins in the database" : u"", # New in v2.4.2
    "Autoloaded script functions" : u"", # New in v2.4.2
    "Include the functions on autoloaded avsi files in the database" : u"", # New in v2.4.2
    "Include plugin functions from the program's database" : u"", # New in v2.4.2
    "Plugin functions from database" : u"", # New in v2.4.2
    "Include user script functions from the program's database" : u"", # New in v2.4.2
    "Script functions from database" : u"", # New in v2.4.2
    "Add user defined variables into autocomplete list" : u"", # New in v2.2.1
    "Show autocomplete with variables" : u"", # New in v2.2.1
    "Show autocomplete on single matched lowercase variable" : u"", # New in v2.2.1
    "When typing a lowercase variable name, show autocomplete if there is only one item matched in keyword list" : u"", # New in v2.2.1
    "Add icons into autocomplete list. Using different type to indicate how well a filter's presets is defined" : u"", # New in v2.2.1
    "Show autocomplete with icons" : u"", # New in v2.2.1
    "Don't show autocomplete when calltip is active" : u"", # New in v2.2.1
    "When calltip is active, autocomplete will not be activate automatically. You can still show autocomplete manually" : u"", # New in v2.2.1
    "Autoparentheses level" : u"Уровень автоскобок",
    "Close \"()\"" : u"Закрытая \"()\"",
    "Determines parentheses to insert upon autocompletion" : u"Определяет скобки для вставки при автозавершении",
    "None \" \"" : u"Никакая \" \"",
    "Open \"(\"" : u"Открытая \"(\"",
    "Determines which key activates the filter preset when the autocomplete box is visible" : u"", # New in v2.2.1
    "Preset activation key" : u"", # New in v2.2.1
    "Return" : u"", # New in v2.2.1
    "Tab" : u"", # New in v2.2.1
    "None" : u"Не определена",
    "Video" : u"Видео",
    "Constantly update video while dragging" : u"Непрерывно обновлять видео при перетаскивании",
    "Update the video constantly when dragging the frame slider" : u"Обновлять видео непрерывно при перемещении ползунка кадров",
    "Enable line-by-line update" : u"Разрешить обновление построчно", 
    "Enable the line-by-line video update mode (update every time the cursor changes line position)" : u"Разрешить режим построчного обновления видео (обновлять каждый раз при смене позиции строки курсора)", 
    "Focus the video preview upon refresh" : u"Фокус на видеопросмотр при обновлении",
    "Switch focus to the video preview window when using the refresh command" : u"Переключить фокус на окне видео просмотра при использовании команды обновления",
    "Refresh preview automatically" : u"", # New in v2.2.1
    "Refresh preview when switch focus on video window or change a value in slider window" : u"", # New in v2.2.1
    "Seeking to a certain frame will seek to that frame on all tabs" : u"", # New in v2.2.1
    "Shared timeline" : u"", # New in v2.2.1
    "Only on tabs of the same characteristics" : u"", # New in v2.5.0
    "Only share timeline for clips with the same resolution and frame count" : u"", # New in v2.5.0
    "Determines which mouse wheel function is used, see below tabs" : u"", # New in v2.5.1.09
    "Frames step" : u"", # New in v2.6.1.5
    "Mouse Wheel Function" : u"", # New in v2.5.1.09
    "Tabs scrolling" : u"", # New in v2.5.1.09
    "Enable scroll wheel through similar tabs" : u"", # New in v2.2.1
    "Mouse scroll wheel cycles through tabs with similar videos" : u"", # New in v2.2.1
    "Enable scroll wheel through tabs on the same group" : u"", # New in v2.5.0
    "Mouse scroll wheel cycles through tabs assigned to the same tab group" : u"", # New in v2.5.0
    "Allow AvsPmod to resize and/or move the program window when updating the video preview" : u"", # New in v2.2.1
    "Allow AvsPmod to resize the window" : u"", # New in v2.2.1
    "Separate video preview window" : u"Отдельное окно просмотра видео",
    "Use a separate window for the video preview" : u"Использоваить отдельное окно для просмотра видео",
    "Keep it on top of the main window" : u"", # New in v2.3.1
    "Keep the video preview window always on top of the main one and link its visibility" : u"", # New in v2.3.1
    "Min text lines on video preview" : u"Мин. число строк при просмотре видео",
    "Minimum number of lines to show when displaying the video preview" : u"Минимальное число строк текста при просмотре видео",
    "Customize the video information shown in the program status bar" : u"Настроить видео информацию показываемую в полосе статуса",
    "Customize video status bar..." : u"Настроить полосу статуса",
    "Error message font..." : u"", # New in v2.6.1.5
    "Set the font used for displaying the error if evaluating the script fails" : u"", # New in v2.5.1
    "User Sliders" : u"", # New in v2.2.1
    "Hide slider window by default" : u"", # New in v2.2.1
    "Keep the slider window hidden by default when previewing a video" : u"", # New in v2.2.1
    "Create user sliders automatically" : u"", # New in v2.2.1
    "Create user sliders automatically using the filter database" : u"", # New in v2.2.1
    "Create user sliders for int and float arguments" : u"", # New in v2.2.1
    "type int/float (numerical slider)" : u"", # New in v2.2.1
    "Create listboxes for int list arguments" : u"", # New in v2.5.1
    "type int (list)" : u"", # New in v2.5.1
    "Create color pickers for hex color arguments" : u"", # New in v2.2.1
    "type int (hex color)" : u"", # New in v2.2.1
    "Create radio boxes for bool arguments" : u"", # New in v2.2.1
    "type bool" : u"", # New in v2.2.1
    "Create listboxes for string list arguments" : u"", # New in v2.2.1
    "type string (list)" : u"", # New in v2.2.1
    "Create filename pickers for string filename arguments" : u"", # New in v2.2.1
    "type string (filename)" : u"", # New in v2.2.1
    "Create placeholders for arguments which have no database information" : u"", # New in v2.2.1
    "undocumented" : u"", # New in v2.2.1
    "Determines which filters will initially have hidden arguments in the slider window" : u"", # New in v2.2.1
    "Fold all" : u"", # New in v2.2.1
    "Fold non-numbers" : u"", # New in v2.2.1
    "Fold none" : u"", # New in v2.2.1
    "Fold startup setting" : u"", # New in v2.2.1
    "Filter exclusion list:" : u"", # New in v2.2.1
    "Specify filters never to build automatic sliders for" : u"", # New in v2.2.1
    "Save/Load" : u"", # New in v2.2.1
    "Automatically save the session on shutdown and load on next startup" : u"Автоматически сохранять сеанс при закрытии и загружать при следующем запуске",
    "Save session for next launch" : u"Сохранять сеанс для следующего запуска",
    "Always load startup session" : u"Всегда загружать стартовый сеанс", 
    "Always load the auto-saved session before opening any other file on startup" : u"Всегда загружать авто-сохраненный сеанс до открытия другого файла при запуске", 
    "Always hide the video preview window when loading a session" : u"", # New in v2.2.1
    "Don't preview when loading a session" : u"", # New in v2.2.1
    "Backup session periodically (minutes)" : u"", # New in v2.3.0
    "Backup the session every X minutes, if X > 0" : u"", # New in v2.3.0
    "Backup session when previewing" : u"", # New in v2.2.1
    "If checked, the current session is backed up prior to previewing any new script" : u"Если включен, текущий сеанс сохраняется перед просмотром любого скрипта",
    "Prompt to save a script before previewing (inactive if previewing with unsaved changes)" : u"Предлагать сохранить скрипт перед просмотром (неактивно если просмотр с несохраненными изменениями)", 
    "Prompt to save when previewing" : u"Предлагать сохранить перед просмотром", 
    "Create a temporary preview script with unsaved changes when previewing the video" : u"Создавать временный скрипт просмотра с несохраненными изменениями при просмотре видео", 
    "Preview scripts with unsaved changes" : u"", # New in v2.2.1
    "When closing a tab, don't prompt to save the script if it doesn't already exist on the filesystem" : u"", # New in v2.3.0
    "When closing tab, don't prompt to save scripts without file" : u"", # New in v2.5.1.09
    "Prompt to save each script with unsaved changes when exiting the program" : u"Приглашение сохранять каждый скрипт с несохраненными изменениями при выходе из программы",
    "Prompt to save scripts on program exit" : u"Приглашение сохранять скрипты при выходе",
    "Only with existing script" : u"", # New in v2.5.1.09
    "When exiting the program, don't prompt to save the script if it doesn't already exist on the filesystem" : u"", # New in v2.5.1.09
    "Auto" : u"", # New in v2.5.1
    "Auto: CRLF on Windows and LF on *nix for new scripts, existing scripts keep their current line endings" : u"", # New in v2.5.1
    "Force CRLF" : u"", # New in v2.5.1
    "Force LF" : u"", # New in v2.5.1
    "Line endings" : u"", # New in v2.5.1
    "Save and read AvsPmod-specific markings (user sliders, toggle tags, etc) as a commented section in the *.avs file" : u"", # New in v2.6.1.5
    "Save or read .avs scripts with AvsPmod markings" : u"", # New in v2.6.1.5
    "Start dialogs on the last used directory" : u"", # New in v2.4.0
    "If unchecked, the script's directory is used" : u"", # New in v2.4.0
    "Start save image dialogs on the last used directory" : u"", # New in v2.4.0
    "Choose a default pattern for image filenames. %s -> script title, %06d -> frame number padded to six digits" : u"", # New in v2.5.0
    "Default image filename pattern" : u"", # New in v2.5.0
    "Ask for JPEG quality" : u"", # New in v2.5.0
    "When saving a JPEG image, prompt for the quality level. Use the value from the last time if not checked" : u"", # New in v2.5.0
    "Misc" : u"Разное", 
    "Choose the language used for the interface" : u"", # New in v2.3.0
    "Language" : u"", # New in v2.3.0
    "Double the size of the buttons on the video control bar" : u"", # New in v2.4.1
    "Use large size video controls" : u"", # New in v2.4.1
    "Show keyboard images in the script tabs when video has focus" : u"", # New in v2.2.1
    "Use keyboard images in tabs" : u"", # New in v2.2.1
    "Show tabs in multiline style" : u"", # New in v2.2.1
    "There can be several rows of tabs" : u"", # New in v2.2.1
    "All tabs will have same width" : u"", # New in v2.2.1
    "Show tabs in fixed width" : u"", # New in v2.2.1
    "Invert scroll wheel direction (Tabs, Zoom)" : u"", # New in v2.5.1.09
    "Scroll the mouse wheel up for changing tabs to the right" : u"", # New in v2.4.1
    "Invert scroll wheel direction (Frame)" : u"", # New in v2.5.1.09
    "Invert wheel direction for frames step" : u"", # New in v2.6.1.5
    "Automatically load bookmarks from script only if tab count 1" : u"", # New in v2.6.1.5
    "On first script load bookmarks from script" : u"", # New in v2.6.1.5
    "Automatically load bookmarks from script if tab changed" : u"", # New in v2.6.1.5
    "Tabs changing loads bookmarks from script" : u"", # New in v2.6.1.5
    "Only allow a single instance of AvsPmod" : u"", # New in v2.2.1
    "Show warning at startup if there are dlls with bad naming in default plugin folder" : u"", # New in v2.2.1
    "Show warning for bad plugin naming at startup" : u"", # New in v2.2.1
    "Middle mouse button behavior on the script" : u"", # New in v2.6.1.5
    "Middle mouse on script (0 open source, 1 show video frame)" : u"", # New in v2.6.1.5
    "Max number of recent filenames" : u"Макс. число имен последних файлов", 
    "This number determines how many filenames to store in the recent files menu" : u"Это число определяет, сколько имен файлов сохраняется в меню последних файлов", 
    "Custom jump size:" : u"Задаваемый размер шага",
    "Jump size used in video menu" : u"Размер шага используемый в меню видео",
    "Custom jump size units" : u"Единицы задаваемого размера шага",
    "Units of custom jump size" : u"Единицы задаваемого размера шага",
    "hours" : u"часы",
    "minutes" : u"минуты",
    "seconds" : u"секунды",
    "frames" : u"кадры",
    "Add tab to group" : u"", # New in v2.5.0
    "Extend selection to line down position" : u"", # New in v2.2.1
    "Scroll down" : u"", # New in v2.2.1
    "Extend rectangular selection to line down position" : u"", # New in v2.2.1
    "Extend selection to line up position" : u"", # New in v2.2.1
    "Scroll up" : u"", # New in v2.2.1
    "Extend rectangular selection to line up position" : u"", # New in v2.2.1
    "Go to previous paragraph" : u"", # New in v2.2.1
    "Extend selection to previous paragraph" : u"", # New in v2.2.1
    "Go to next paragraph" : u"", # New in v2.2.1
    "Extend selection to next paragraph" : u"", # New in v2.2.1
    "Extend selection to previous character" : u"", # New in v2.2.1
    "Go to previous word" : u"", # New in v2.2.1
    "Extend selection to previous word" : u"", # New in v2.2.1
    "Extend rectangular selection to previous character" : u"", # New in v2.2.1
    "Extend selection to next character" : u"", # New in v2.2.1
    "Go to next word" : u"", # New in v2.2.1
    "Extend selection to next word" : u"", # New in v2.2.1
    "Extend rectangular selection to next character" : u"", # New in v2.2.1
    "Go to previous word part" : u"", # New in v2.2.1
    "Extend selection to previous word part" : u"", # New in v2.2.1
    "Go to next word part" : u"", # New in v2.2.1
    "Extend selection to next word part" : u"", # New in v2.2.1
    "Extend selection to start of line" : u"", # New in v2.2.1
    "Go to start of document" : u"", # New in v2.2.1
    "Extend selection to start of document" : u"", # New in v2.2.1
    "Go to start of line" : u"", # New in v2.2.1
    "Extend selection to end of line" : u"", # New in v2.2.1
    "Go to end of document" : u"", # New in v2.2.1
    "Extend selection to end of document" : u"", # New in v2.2.1
    "Go to end of line" : u"", # New in v2.2.1
    "Extend selection to previous page" : u"", # New in v2.2.1
    "Extend rectangular selection to previous page" : u"", # New in v2.2.1
    "Extend selection to next page" : u"", # New in v2.2.1
    "Extend rectangular selection to next page" : u"", # New in v2.2.1
    "Delete to end of word" : u"", # New in v2.2.1
    "Delete to end of line" : u"", # New in v2.2.1
    "Delete back" : u"", # New in v2.2.1
    "Delete to start of word" : u"", # New in v2.2.1
    "Delete to start of line" : u"", # New in v2.2.1
    "Cancel autocomplete or calltip" : u"", # New in v2.2.1
    "Indent selection" : u"Отступ выбранного",
    "Unindent selection" : u"Убрать отступ выбранного",
    "Newline" : u"", # New in v2.2.1
    "Zoom in" : u"", # New in v2.2.1
    "Zoom out" : u"", # New in v2.2.1
    "Reset zoom level to normal" : u"", # New in v2.2.1
    "Line cut" : u"", # New in v2.2.1
    "Line delete" : u"", # New in v2.2.1
    "Line copy" : u"", # New in v2.2.1
    "Transpose line with the previous" : u"", # New in v2.2.1
    "Line or selection duplicate" : u"", # New in v2.2.1
    "Convert selection to lowercase" : u"", # New in v2.2.1
    "Convert selection to uppercase" : u"", # New in v2.2.1
    "Sort bookmarks ascending" : u"", # New in v2.2.1
    "sort ascending" : u"", # New in v2.2.1
    "Show bookmarks with timecode" : u"", # New in v2.2.1
    "show time" : u"", # New in v2.2.1
    "Show bookmarks with title" : u"", # New in v2.2.1
    "show title" : u"", # New in v2.2.1
    "Resolution-based" : u"", # New in v2.3.0
    "BT.709" : u"", # New in v2.3.0
    "BT.601" : u"", # New in v2.3.0
    "TV levels" : u"", # New in v2.3.0
    "PC levels" : u"", # New in v2.3.0
    "Progressive" : u"", # New in v2.2.1
    "Interlaced" : u"", # New in v2.2.1
    "Swap UV" : u"", # New in v2.2.1
    "25%" : u"", # New in v1.3.8
    "50%" : u"", # New in v1.3.8
    "100% (normal)" : u"", # New in v1.3.8
    "200%" : u"", # New in v1.3.8
    "300%" : u"", # New in v1.3.8
    "400%" : u"", # New in v1.3.8
    "Fill window" : u"Заполнить окно",
    "Fit inside window" : u"Подогнать внутрь окна",
    "Vertically" : u"", # New in v2.2.1
    "Horizontally" : u"", # New in v2.2.1
    "Black" : u"", # New in v2.5.1
    "Dark grey" : u"", # New in v2.5.1
    "Medium grey" : u"", # New in v2.5.1
    "Light grey" : u"", # New in v2.5.1
    "White" : u"", # New in v2.5.1
    "&File" : u"&Файл",
    "Create a new tab" : u"Создать новую вкладку",
    "New tab" : u"Новая вкладка",
    "Open an existing script" : u"Открыть существующий скрипт",
    "Open..." : u"Открыть...",
    "Reopen the last closed tab" : u"", # New in v2.4.0
    "Undo close tab" : u"", # New in v2.4.0
    "Close tab" : u"Закрыть вкладку",
    "Close the current tab" : u"Закрыть текущую вкладку",
    "Close all tabs" : u"", # New in v2.2.1
    "Close every tab" : u"", # New in v2.2.1
    "Rename tab" : u"", # New in v2.2.1
    "Rename the current tab. If script file is existing, also rename it" : u"", # New in v2.2.1
    "Save the current script" : u"Сохранить текущий скрипт",
    "Choose where to save the current script" : u"Выбрать где сохранить текущий скрипт",
    "Save script as..." : u"Сохранить скрипт как...",
    "Reload script" : u"", # New in v2.4.1
    "Reopen the current script file if it has changed" : u"", # New in v2.4.1
    "If the current script is saved to a file, open its directory" : u"", # New in v2.5.1
    "Open script's directory" : u"", # New in v2.5.1
    "Save the current script as a HTML document" : u"", # New in v2.5.0
    "Export HTML" : u"", # New in v2.5.0
    "&Print script" : u"", # New in v2.3.1
    "Configure page for printing" : u"", # New in v2.3.1
    "Page setup" : u"", # New in v2.3.1
    "Include the script filename and page number at the top of each page" : u"", # New in v2.3.1
    "Print header" : u"", # New in v2.3.1
    "Word-wrap long lines" : u"", # New in v2.3.1
    "Apply the current zoom to the output" : u"", # New in v2.3.1
    "Use zoom" : u"", # New in v2.3.1
    "Display print preview" : u"", # New in v2.3.1
    "Print preview" : u"", # New in v2.3.1
    "&Print" : u"", # New in v2.3.1
    "Print to printer or file" : u"", # New in v2.3.1
    "Load a session into the tabs" : u"Загрузить сеанс во вкладки",
    "Load session..." : u"Загрузить сеанс...",
    "Save all the scripts as a session, including slider info" : u"Сохранить все скрипты как сеанс, включая информацию ползунков",
    "Save session..." : u"Сохранить сеанс...",
    "Backup current session" : u"Архивировать текущий сеанс",
    "Backup the current session for next program run" : u"Архивировать текущий сеанс (состояние) для последующего запуска программы",
    "Next tab" : u"Следующая вкладка",
    "Switch to next script tab" : u"Переключиться к следующей скриптовой вкладке",
    "Previous tab" : u"Предыдущая вкладка",
    "Switch to previous script tab" : u"Переключиться к предыдущей скриптовой вкладке",
    "Show the scrap window" : u"Показать окно заметок",
    "&Exit" : u"&Выход",
    "Exit the program" : u"Выйти из программы",
    "&Edit" : u"&Правка",
    "Undo last text operation" : u"Отменить последнюю текстовую операцию",
    "Redo last text operation" : u"Повторить последнюю текстовую операцию",
    "Cut the selected text" : u"Вырезать выбранный текст",
    "Copy the selected text" : u"Скопировать выбранный текст",
    "Paste the selected text" : u"Вставить выбранный текст",
    "Open a find text dialog box" : u"Открыть диалог поиска текста",
    "Find..." : u"Найти...",
    "Find next" : u"Найти следующее",
    "Find the next instance of given text" : u"Найти следующий образец заданного текста",
    "Find previous" : u"", # New in v2.4.0
    "Find the previous instance of given text" : u"", # New in v2.4.0
    "Open a replace text dialog box" : u"Открыть диалог замены текста",
    "Replace..." : u"Заменить...",
    "Replace next" : u"", # New in v2.4.0
    "Replace the next instance of given text" : u"", # New in v2.4.0
    "Select All" : u"Выбрать все",
    "Select all the text" : u"Выбрать весь текст",
    "&Insert" : u"", # New in v2.2.1
    "Expand a snippet tag, or select a snippet from the list" : u"", # New in v2.5.0
    "Insert snippet" : u"", # New in v2.5.0
    "Choose a source file to insert into the text" : u"Задать файл (видео) источника для вставки в текст",
    "Insert source..." : u"Вставить источник...",
    "Get a filename from a dialog box to insert into the text" : u"Получить имя файла в диалоге для вставки в текст",
    "Insert filename..." : u"Вставить имя файла...",
    "Choose a plugin file to insert into the text" : u"", # New in v2.4.0
    "Insert plugin..." : u"Вставить плагин...",
    "Insert a user-scripted slider into the text" : u"Вставить определяемый пользователем ползунок в текст",
    "Insert user slider..." : u"Вставить пользовательский ползунок...",
    "Insert a tag which indicates a separator in the user slider window" : u"Вставить метку, обозначающую разделитель в окне пользовательских ползунков",
    "Insert user slider separator" : u"Вставить разделитель пользовательских ползунков",
    "Insert the current frame number into the text" : u"Вставить номер текущего кадра в текст",
    "Add tags surrounding the selected text for toggling with the video preview" : u"Добавить метки, окружающие блок текста, для отключения-включения при просмотре видео",
    "Tag selection for toggling" : u"Пометить выбранное для переключения",
    "Clear all tags" : u"Убрать все метки",
    "Clear all toggle tags from the text" : u"Убрать все метки отключения блоков из текста",
    "Indent the selected lines" : u"Увеличить отступ выбранных строк",
    "Unindent the selected lines" : u"Уменьшить отступ выбранных строк",
    "Block comment" : u"Блоковый комментарий",
    "Comment or uncomment selected lines" : u"Закомментировать или раскомментировать выбранные строки",
    "Comment at start of a text style or uncomment" : u"", # New in v2.2.1
    "Style comment" : u"", # New in v2.2.1
    "Toggle current fold" : u"", # New in v2.2.1
    "Toggle the fold point On/OFF at the current line" : u"", # New in v2.2.1
    "Toggle all fold points On/OFF" : u"", # New in v2.2.1
    "Toggle all folds" : u"", # New in v2.2.1
    "Toggle text wrap" : u"", # New in v2.5.1.09
    "Toggle text wrap On/OFF" : u"", # New in v2.5.1.09
    "&AviSynth function" : u"", # New in v2.2.1
    "Show list of filternames matching the partial text at the cursor" : u"Показать список имен фильтров, соответствующих части текста, выделенной курсором",
    "Autocomplete all" : u"", # New in v2.2.1
    "Disregard user's setting, show full list of filternames matching the partial text at the cursor" : u"", # New in v2.2.1
    "Autocomplete parameter/filename" : u"", # New in v2.5.0
    "If the first characters typed match a parameter name, complete it. If they're typed on a string, complete the filename" : u"", # New in v2.5.0
    "Show calltip" : u"Показать подсказку", 
    "Show the calltip for the filter (only works if cursor within the arguments)" : u"Показать подсказку по фильтру (работает только если курсор на аргументах)", 
    "Show function definition" : u"Показать определение функции",
    "Show the AviSynth function definition dialog for the filter" : u"Показать диалог опрелеления функции AviSynth для фильтра",
    "Filter help file" : u"Файл справки по фильтру", 
    "Run the help file for the filter (only works if cursor within the arguments or name is highlighted)" : u"Вызвать файл справки по фильтру (работает только если курсор на аргументах или имя подсвечено)", 
    "Include functions defined in the current script in the filter database, only for this tab" : u"", # New in v2.5.1
    "Parse script for function definitions" : u"", # New in v2.5.1
    "&Miscellaneous" : u"", # New in v2.2.1
    "Move line up" : u"Передвинуть строку вверх", 
    "Move the current line or selection up by one line" : u"Передвинуть текущую строку или выбранное на одну позицию вверх", 
    "Move line down" : u"Передвинуть строку вниз", 
    "Move the current line or selection down by one line" : u"Передвинуть текущую строку или выбранное на одну позицию вниз", 
    "Copy the current script without any AvsP markings (user-sliders, toggle tags) to the clipboard" : u"Копировать текущий скрипт без AvsP разметки (ползунков, меток) в буфер обмена", 
    "Copy unmarked script to clipboard" : u"Копировать неразмеченный скрипт в буфер обмена", 
    "Copy avisynth error to clipboard" : u"", # New in v2.2.1
    "Copy the avisynth error message shown on the preview window to the clipboard" : u"", # New in v2.2.1
    "&Video" : u"&Видео",
    "Bookmarks" : u"", # New in v2.4.0
    "Bookmarks to script" : u"", # New in v2.6.1.5
    "Bookmarks from script" : u"", # New in v2.6.1.5
    "Add/Remove bookmark" : u"", # New in v2.2.1
    "Mark the current frame on the frame slider" : u"Пометить текущий кадр на ползунке кадров",
    "Clear all bookmarks" : u"Очистить все закладки",
    "Titled &bookmarks" : u"", # New in v2.2.1
    "Move the nearest titled bookmark to the current position. A historic title will be restored if it matches the condition." : u"", # New in v2.2.1
    "Move titled bookmark" : u"", # New in v2.2.1
    "Restore all historic titles" : u"", # New in v2.2.1
    "Restore historic titles" : u"", # New in v2.2.1
    "Clear all historic titles" : u"", # New in v2.2.1
    "Clear historic titles" : u"", # New in v2.2.1
    "Generate titles for untitled bookmarks by the pattern - 'Chapter %02d'" : u"", # New in v2.2.1
    "Set title (auto)" : u"", # New in v2.2.1
    "Edit title for bookmarks in a list table" : u"", # New in v2.2.1
    "Set title (manual)" : u"", # New in v2.2.1
    "Not include this tab on any group" : u"", # New in v2.5.0
    "Add tab to this group" : u"", # New in v2.5.0
    "Clear current tab group" : u"", # New in v2.5.0
    "Clear all tab groups" : u"", # New in v2.5.0
    "Apply offsets" : u"", # New in v2.5.0
    "Use the difference between showed frames when the tabs were added to the group as offsets" : u"", # New in v2.5.0
    "Offset also bookmarks" : u"", # New in v2.5.1
    "Apply the offset also to the currently set bookmarks" : u"", # New in v2.5.1
    "&Navigate" : u"", # New in v2.2.1
    "Go to &bookmark" : u"", # New in v2.2.1
    "Go to next bookmarked frame" : u"Перейти к следующей закладке на кадрах",
    "Next bookmark" : u"Следующая закладка",
    "Go to previous bookmarked frame" : u"Перейти к предыдущей закдадке на кадрах",
    "Previous bookmark" : u"Предыдущая закладка",
    "Forward 1 frame" : u"Вперед на 1 кадр",
    "Show next video frame (keyboard shortcut active when video window focused)" : u"Показать следующий видео кадр (горячая клавиша активна когда видео окно в фокусе)",
    "Backward 1 frame" : u"Назад на 1 кадр",
    "Show previous video frame (keyboard shortcut active when video window focused)" : u"Показать предыдущий видео кадр (горячая клавиша активна когда видео окно в фокусе)",
    "Forward 1 second" : u"Вперед на 1 секунду",
    "Show video 1 second forward (keyboard shortcut active when video window focused)" : u"Показать видео кадр на 1 секунду вперед (горячая клавиша активна когда видео окно в фокусе)",
    "Backward 1 second" : u"Назад на 1 секунду",
    "Show video 1 second back (keyboard shortcut active when video window focused)" : u"Показать видео кадр на 1 секунду назад (горячая клавиша активна когда видео окно в фокусе)",
    "Forward 1 minute" : u"Вперед на 1 минуту",
    "Show video 1 minute forward (keyboard shortcut active when video window focused)" : u"Показать видео кадр на 1 минуту вперед (горячая клавиша активна когда видео окно в фокусе)",
    "Backward 1 minute" : u"Назад на 1 минуту",
    "Show video 1 minute back (keyboard shortcut active when video window focused)" : u"Показать видео кадр на 1 минуту назад (горячая клавиша активна когда видео окно в фокусе)",
    "Forward x units" : u"Вперед на x единиц",
    "Jump forward by x units (you can specify x in the options dialog)" : u"Шаг вперед на x единиц (вы можете задать x в диалоге настроек)",
    "Backwards x units" : u"Назад на x единиц",
    "Jump backwards by x units (you can specify x in the options dialog)" : u"Шаг назад на x единиц (вы можете задать x в диалоге настроек)",
    "Go to first frame" : u"К первому кадру",
    "Go to first video frame (keyboard shortcut active when video window focused)" : u"Идти к первому кадру (сочетание клавиш активно, если видео в фокусе)",
    "Go to last frame" : u"К последнему кадру",
    "Go to last video frame (keyboard shortcut active when video window focused)" : u"Идти к последнему кадру (сочетание клавиш активно, если видео в фокусе)",
    "Go to last scrolled frame" : u"Перейти к последнему прокрученному кадру",
    "Last scrolled frame" : u"Последний прокрученный кадр",
    "Enter a video frame or time to jump to" : u"Введите видео кадр или время для перемещения",
    "Go to frame..." : u"Перейти к кадру...",
    "&Play video" : u"", # New in v2.4.0
    "Play/pause video" : u"", # New in v2.4.0
    "Double the current playback speed" : u"", # New in v2.4.0
    "Increment speed" : u"", # New in v2.4.0
    "Decrement speed" : u"", # New in v2.4.0
    "Halve the current playback speed" : u"", # New in v2.5.0
    "Normal speed" : u"", # New in v2.4.0
    "Set the playback speed to the script frame rate" : u"", # New in v2.4.0
    "Maximum speed" : u"", # New in v2.4.0
    "Play the video as fast as possible without dropping frames" : u"", # New in v2.4.0
    "Drop frames" : u"", # New in v2.4.0
    "Maintain correct video speed by skipping frames" : u"", # New in v2.4.0
    "Crop editor..." : u"Редактор обрезки Crop...",
    "Show the crop editor dialog" : u"Показать диалог редактора обрезки размеров кадра Crop",
    "&Trim selection editor" : u"", # New in v2.2.1
    "Show the trim selection editor dialog" : u"Показать диалог редактора выборки кадров Trim",
    "Show trim selection editor" : u"Показать редактор выборки Trim",
    "Set a selection startpoint (shows the trim editor if not visible)" : u"Установить начало выборки (показывает редактор вырезки, если невидим)",
    "Set selection startpoint" : u"Установить начало выборки",
    "Set a selection endpoint (shows the trim editor if not visible)" : u"Установить конец выборки (показывает редактор вырезки, если невидим)",
    "Set selection endpoint" : u"Установить конец выборки",
    "Move selections before the current frame" : u"", # New in v2.5.1
    "The current selections are cut from the timeline and inserted before the current frame. Bookmarks are shifted accordingly." : u"", # New in v2.5.1
    "Move selections after the current frame" : u"", # New in v2.5.1
    "The current selections are cut from the timeline and inserted after the current frame. Bookmarks are shifted accordingly." : u"", # New in v2.5.1
    "Zoom video preview to 25%" : u"Масштаб видео просмотра 25%", 
    "Zoom video preview to 50%" : u"Масштаб видео просмотра 50%", 
    "Zoom video preview to 100% (normal)" : u"Масштаб видео просмотра 100% (нормальный)",
    "Zoom video preview to 200%" : u"Масштаб видео просмотра 200%",
    "Zoom video preview to 300%" : u"Масштаб видео просмотра 300%",
    "Zoom video preview to 400%" : u"Масштаб видео просмотра 400%",
    "Zoom video preview to fill the entire window" : u"Изменить масштаб видео просмотра до заполнения полного окна",
    "Zoom video preview to fit inside the window" : u"Изменить масштаб видео просмотра до помещения внутри окна всего окна",
    "Enlarge preview image to next zoom level. Not work under 'Fill window' or 'Fit inside window'" : u"", # New in v2.2.1
    "Shrink preview image to previous zoom level. Not work under 'Fill window' or 'Fit inside window'" : u"", # New in v2.2.1
    "&Flip" : u"", # New in v2.2.1
    "Flip video preview upside down" : u"", # New in v2.2.1
    "Flip video preview from left to right" : u"", # New in v2.2.1
    "&YUV -> RGB" : u"", # New in v2.2.1
    "Swap chroma channels (U and V)" : u"", # New in v2.2.1
    "Use BT.709 coefficients for HD, BT.601 for SD (default)" : u"", # New in v2.3.0
    "Use BT.709 coefficients" : u"", # New in v2.3.0
    "Use BT.601 coefficients" : u"", # New in v2.3.0
    "Use limited range (default)" : u"", # New in v2.3.0
    "Use full range" : u"", # New in v2.3.0
    "For YV12 only, assume it is progressive (default)" : u"", # New in v2.2.1
    "For YV12 only, assume it is interlaced" : u"", # New in v2.2.1
    "Bit &depth" : u"", # New in v2.6.1.5
    "8-bit" : u"", # New in v2.5.1
    "Regular 8-bit depth (default)" : u"", # New in v2.5.1
    "Stacked 16-bit, MSB on top, range reduced to 10-bit. Requires MaskTools v2 loaded" : u"", # New in v2.5.1
    "Stacked yuv420p10 or yuv444p10" : u"", # New in v2.5.1
    "Stacked 16-bit, MSB on top" : u"", # New in v2.5.1
    "Stacked yuv420p16 or yuv444p16" : u"", # New in v2.5.1
    "Interleaved 16-bit (little-endian), range reduced to 10-bit. Requires MaskTools v2 loaded" : u"", # New in v2.5.1
    "Interleaved yuv420p10 or yuv444p10" : u"", # New in v2.5.1
    "Interleaved 16-bit (little-endian)" : u"", # New in v2.5.1
    "Interleaved yuv420p16 or yuv444p16" : u"", # New in v2.5.1
    "Background &color" : u"", # New in v2.5.1
    "Follow current theme" : u"", # New in v2.5.1
    "Use RGB {hex_value}" : u"", # New in v2.5.1
    "Use a custom color" : u"", # New in v2.5.1
    "Custom" : u"", # New in v2.5.1
    "Choose the color used if 'custom' is selected" : u"", # New in v2.5.1
    "Select custom color" : u"", # New in v2.5.1
    "Create the new AviSynth clip on the same environment. Useful for tweaking parameters" : u"", # New in v2.4.0
    "Keep variables on refreshing" : u"", # New in v2.4.0
    "Save last view position and zoom on tab change" : u"", # New in v2.6.1.5
    "Save view pos on tab change" : u"", # New in v2.6.1.5
    "Save image as..." : u"Сохранить изображение как...",
    "Save the current frame as a bitmap" : u"Сохранить текущий кадр как файл картинки",
    "Quick save image" : u"", # New in v2.5.0
    "Save the current frame as a bitmap with a default filename, overwriting the file if already exists" : u"", # New in v2.5.0
    "Copy image to clipboard" : u"", # New in v2.4.2
    "Copy the current frame to the clipboard as a bitmap" : u"", # New in v2.4.2
    "Force the script to reload and refresh the video frame" : u"Перезагрузить скрипт и обновить видео кадр",
    "Refresh preview" : u"Обновить просмотр",
    "Show/Hide the preview" : u"", # New in v2.2.1
    "Toggle the video preview" : u"Переключить просмотр видео",
    "Toggle preview placement" : u"", # New in v2.5.1
    "When not using a separate window for the video preview, toggle between showing it at the bottom (default) or to the right" : u"", # New in v2.5.1
    "Toggle extended left move" : u"", # New in v2.5.1.09
    "Video window extended left move" : u"", # New in v2.5.1.09
    "Release all open videos from memory" : u"Выгрузить все открытые видео из памяти",
    "Release all videos from memory" : u"Выгрузить все видео из памяти",
    "Switch focus between the video preview and the text editor" : u"Переключить фокус между окнами видео просмотра и текстового редактора",
    "Switch video/text focus" : u"Переключить фокус видео/текст",
    "Show/hide the slider sidebar (double-click the divider for the same effect)" : u"Показать/скрыть колонку ползунков (двойной щелчок на разделителе имеет тот же эффект)", 
    "Toggle the slider sidebar" : u"Переключить колонку ползунков", 
    "Request every video frame once (analysis pass for two-pass filters)" : u"", # New in v2.3.0
    "Run analysis pass" : u"", # New in v2.3.0
    "External player" : u"Внешний проигрыватель",
    "Play the current script in an external program" : u"Проиграть текущий скрипт во внешней программе",
    "Show information about the video in a dialog box" : u"Показать информацию о видео в диалоговом окне",
    "Video information" : u"Информация о видео",
    "&Options" : u"&Опции",
    "Always on top" : u"Всегда поверх",
    "Keep this window always on top of others" : u"Удерживать это окно всегда поверх других",
    "If the video preview is detached, keep it always on top of other windows" : u"", # New in v2.3.1
    "Video preview always on top" : u"", # New in v2.3.1
    "Disable video preview" : u"Отменить видео просмотр", 
    "If checked, the video preview will not be shown under any circumstances" : u"Если отмечено, видео просмотр не будет показан ни при каких обстоятельствах", 
    "Associate .avs files with AvsP" : u"Ассоциировать .avs файлы с AvsP",
    "Configure this computer to open .avs files with AvsP when double-clicked. Run again to disassociate" : u"", # New in v2.4.0
    "Edit the various AviSynth script fonts and colors" : u"Редактировать различные шрифты и цвета скриптов AviSynth", 
    "Fonts and colors..." : u"Шрифты и цвета...", 
    "Make fonts and colors backup" : u"", # New in v2.6.1.5
    "Make script fonts and colors backup" : u"", # New in v2.6.1.5
    "Load fonts and colors backup" : u"", # New in v2.6.1.5
    "Restores script fonts and colors from backup" : u"", # New in v2.6.1.5
    "AviSynth function definition..." : u"Определения функций AviSynth...", 
    "Edit the extension-based templates for inserting sources" : u"Редактировать шаблоны типов файлов для вставки источников",
    "Extension templates..." : u"Шаблоны расширений...", 
    "Snippets..." : u"", # New in v2.5.0
    "Edit insertable text snippets" : u"", # New in v2.5.0
    "Configure the program keyboard shortcuts" : u"Конфигурировать сочетания клавиш быстрого выполнения",
    "Keyboard shortcuts..." : u"", # New in v2.2.1
    "Configure program settings" : u"Конфигурировать настройки программы",
    "Program settings..." : u"Настройки программы...",
    "&Help" : u"&Помощь",
    "Animated tutorial" : u"Анимированный урок",
    "View an animated tutorial for AvsP (from the AvsP website)" : u"Смотреть анимированный урок по AvsP (с сайта AvsP)",
    "Learn more about AvsP text features (from the AvsP website)" : u"Узнать больше об текстовых особенностях AvsP",
    "Text features" : u"Текстовые особенности",
    "Learn more about AvsP video features (from the AvsP website)" : u"Узнать больше о видео особенностях AvsP",
    "Video features" : u"Видео особенности",
    "Learn more about AvsP user sliders (from the AvsP website)" : u"Узнать больше о пользвательских ползунках AvsP",
    "User sliders" : u"Пользовательские ползунки",
    "Learn more about AvsP macros (from the AvsP website)" : u"Узнать больше о макросах AvsP",
    "Macros" : u"Макросы",
    "Avisynth help" : u"Справка AviSynth",
    "Open the avisynth help html" : u"Открыть html файл справки AviSynth",
    "Open Avisynth plugins folder" : u"", # New in v2.2.1
    "Open the avisynth plugins folder, or the last folder from which a plugin was loaded" : u"", # New in v2.3.1
    "Changelog" : u"", # New in v2.4.1
    "Open the changelog file" : u"", # New in v2.4.1
    "About this program" : u"Об этой программе",
    "About AvsPmod" : u"", # New in v2.2.1
    "Previous frame" : u"Предыдущий кадр",
    "Next frame" : u"Следующий кадр",
    "Run the script with an external program" : u"Выполнить скрипт внешней программой",
    "Run the selected tool" : u"", # New in v2.2.1
    "&Tools" : u"&Инструменты",
    "A macro check item" : u"", # New in v2.3.0
    "A macro radio item" : u"", # New in v2.3.0
    "Run selected macro" : u"Выполнить выбранный макрос",
    "View the readme for making macros" : u"Посмотреть справку по созданию макросов",
    "Open macros folder" : u"", # New in v2.3.0
    "Open the macros folder" : u"", # New in v2.2.1
    "&Macros" : u"", # New in v2.2.1
    "Close" : u"Закрыть",
    "Close all the other" : u"", # New in v2.6.1.5
    "Rename" : u"", # New in v2.2.1
    "Group" : u"", # New in v2.5.0
    "Save" : u"Сохранить",
    "Save as..." : u"Сохранить как...",
    "Reload" : u"", # New in v2.4.1
    "Open directory" : u"", # New in v2.5.1
    "Release video memory" : u"", # New in v2.6.1.5
    "Release all other video memory" : u"", # New in v2.6.1.5
    "Tab change loads bookmarks" : u"", # New in v2.6.1.5
    "Copy to new tab" : u"", # New in v2.2.1
    "Reposition to" : u"", # New in v2.2.1
    "Crop editor" : u"Редактор обрезки",
    "You can drag the crop regions with the left mouse button when this dialog is visible, cropping the edge closest to the initial mouse click." : u"Вы можете перетаскивать область обрезки левой кнопкой мыши, когда этот диалог видимый, обрезая края ближайшие в начальному щелчку мышкой",
    "Auto-crop" : u"", # New in v2.4.0
    "Samples" : u"", # New in v2.4.0
    "At script end" : u"В конце скрипта",
    "At script cursor" : u"В позиции курсора",
    "Copy to clipboard" : u"Копировать в буфер",
    "Insert Crop() command:" : u"Вставить команду обрезки Crop():",
    "Apply" : u"Применить ",
    "Trim editor" : u"Редактор вырезок Trim",
    "Selection options" : u"Опции выбора",
    "Keep selected regions" : u"Удерживать выбранные области",
    "Keep unselected regions" : u"Удерживать невыбранные области",
    "Mark video frames inside/outside selection" : u"Пометить видеокадры внути/вне выбранного",
    "Use Dissolve() with overlap frames:" : u"", # New in v2.2.1
    "Single clips (c0..cn) with prefix:" : u"", # New in v2.6.1.5
    "Insert Trim() commands: " : u"", # New in v2.6.1.5
    "Insert clips commands: " : u"", # New in v2.6.1.5
    "Insert Dissolve(trim,) commands: " : u"", # New in v2.6.1.5
    "Insert Dissolve(clips,) commands: " : u"", # New in v2.6.1.5
    "Use the buttons which appear on the video slider handle to create the frame selections to trim." : u"Использовать кнопки на контроле ползунка видео для создания выборки кадров для вырезки.",
    "The script's directory doesn't exist anymore!" : u"", # New in v2.5.1
    "%d Bookmarks imported" : u"", # New in v2.6.1.5
    "Print Preview" : u"", # New in v2.3.1
    "Failed to create print preview" : u"", # New in v2.3.1
    "Print Error" : u"", # New in v2.3.1
    "There was an error when printing.\nCheck that your printer is properly connected." : u"", # New in v2.3.1
    "Printer Error" : u"", # New in v2.3.1
    "Damaged session file" : u"", # New in v2.3.1
    "File does not exist!" : u"Файл не существует!", 
    "Select a file" : u"Выбрать файл",
    "Create a separator label" : u"Создать метку разделителя",
    "Enter separator label" : u"Введите метку разделителя",
    "Enter tag name:" : u"Введите имя метки", 
    "Tag definition" : u"Определение метки", 
    "Chapter" : u"", # New in v2.2.1
    "Set title for bookmarks" : u"", # New in v2.2.1
    "Title" : u"", # New in v2.2.1
    "Frame No." : u"", # New in v2.2.1
    "Time **" : u"", # New in v2.2.1
    "Left-click on a selected item or double-click to edit.\n\n*  RED - a historic title, not a real bookmark.\n** Time may be unavailable or incorrect before preview refreshed." : u"", # New in v2.3.0
    "Image saved to \"{0}\"" : u"", # New in v2.5.0
    "No image to save" : u"Нет изображения для сохранения",
    "Error requesting frame {number}" : u"", # New in v2.5.0
    "Couldn't open clipboard" : u"", # New in v2.4.2
    "Cannot use crop editor unless bit depth is set to 8" : u"", # New in v2.5.1
    "Cannot change bit depth while crop editor is open!" : u"", # New in v2.5.1
    "Interleaved RGB48" : u"", # New in v2.5.1
    "Error loading the script" : u"Ошибка загрузки скрипта",
    "Starting analysis pass..." : u"", # New in v2.3.0
    "Frame %s/%s (%#.4g fps)" : u"", # New in v2.4.2
    "Finished (%s fps average)" : u"", # New in v2.5.0
    "Frame size:" : u"Размер кадра",
    "Length:" : u"Длина",
    "Frame rate:" : u"Частота кадров",
    "Colorspace:" : u"Цветовое пространство",
    "Bit depth:" : u"", # New in v2.6.1.5
    "Field or frame based:" : u"Поля или целые кадры",
    "Parity:" : u"Четность",
    "Audio" : u"Аудио",
    "Channels:" : u"Каналов:",
    "Hz" : u"Гц",
    "Sampling rate:" : u"Частота отсчетов",
    "Sample type:" : u"Тип отсчетов",
    "bits" : u"бит",
    "samples" : u"отсчетов",
    "Could not find the macros folder!" : u"", # New in v2.2.1
    "Failed to import the selected tool" : u"", # New in v2.2.1
    "You must restart for changes to take effect!" : u"", # New in v2.2.1
    "Basic (1)" : u"", # New in v2.5.1
    "Override all fonts to use a specified monospace font (no effect on scrap window)" : u"", # New in v2.2.1
    "Use monospaced font:" : u"", # New in v2.2.1
    "Default:" : u"По умолчанию:", 
    "Comment:" : u"Комментарий:", 
    "Block Comment:" : u"", # New in v2.2.1
    "__END__ Comment:" : u"", # New in v2.2.1
    "Number:" : u"Число:", 
    "String:" : u"Строка:", 
    "Triple-quoted string:" : u"Строка в тройных кавычках:", 
    "Assignment:" : u"", # New in v2.5.0
    "Operator:" : u"Оператор:", 
    "Basic (2)" : u"", # New in v2.5.1
    "Internal filter:" : u"Внутренний фильтр:", 
    "External filter:" : u"Внешний фильтр:", 
    "Internal function:" : u"Внутренняя функция:", 
    "User defined function:" : u"Функция определенная пользователем:",
    "Unknown function:" : u"", # New in v2.5.0
    "Clip property:" : u"Свойство клипа:", 
    "Parameter:" : u"", # New in v2.5.0
    "AviSynth data type:" : u"Тип данных AviSynth:",
    "AviSynth keyword:" : u"Ключевое слово AviSynth:",
    "AvsP user slider:" : u"AvsP пользовательский ползунок:",
    "Advanced" : u"Дополнительные",
    "Incomplete string:" : u"Незавершенная строка:", 
    "Syntax highlight strings which are not completed in a single line differently" : u"Подсвечивать синтаксис строк, которые незавершены в одной строке другим образом", 
    "Brace highlight:" : u"Подсветка скобок:",
    "Bad brace:" : u"Плохая скобка:",
    "Bad number:" : u"Плохое число:",
    "Margin line numbers:" : u"Номера строк границы:",
    "Miscellaneous word:" : u"Различные слова:",
    "Calltip:" : u"Подсказка:",
    "Calltip highlight:" : u"Подстветка подсказки:",
    "Cursor:" : u"", # New in v2.2.1
    "If checked, highlight also foreground" : u"", # New in v2.5.1
    "Selection highlight:" : u"", # New in v2.2.1
    "Current line highlight:" : u"", # New in v2.2.1
    "Highlight the line that the caret is currently in" : u"Подсвечивать строку, на которой сейчас каретка", 
    "Fold margin:" : u"", # New in v2.2.1
    "Scrap window" : u"", # New in v2.2.1
    "Information" : u"Информация",
    "Settings have been read from backup file\n" : u"", # New in v2.6.1.5
    "File extension shouldn't contain dots!" : u"", # New in v2.5.1
    "Insert aborted:" : u"Вставка прервана:",
    "Edit extension-based templates" : u"Редактировать основанные на расширении шаблоны",
    "File extension" : u"Расширение файла",
    "Template" : u"Шаблон",
    "This info is used for inserting sources based on file extensions." : u"Эта информация используется для вставки источников, основываясь на расширениях.",
    "Any instances of *** in the template are replaced with the filename." : u"Любое нахождение *** в шаблоне заменяется именем файла.",
    "(If you want relative paths instead of the full filename, use [***].)" : u"", # New in v2.2.1
    "Only alphanumeric and underscores allowed!" : u"", # New in v2.5.0
    "Tag" : u"", # New in v2.5.0
    "Snippet" : u"", # New in v2.5.0
    "Associating .avs files will write to the windows registry." : u"Ассоциирование .avs файлов проводится путем внесения изменений в реестр Windows.",
    "Do you wish to continue?" : u"Хотите продолжить?",
    "Associate avs files for all users?" : u"", # New in v2.4.0
    "Disassociate avs files for all users?" : u"", # New in v2.4.0
    " Admin rights are needed." : u"", # New in v2.4.0
    "Above keys are built-in editing shortcuts. If item is checked,\nit will not be overrided by a menu shortcut in script window." : u"", # New in v2.3.0
    "* This shortcut is active only when video window has focus.\n~ This shortcut is active only when script window has focus." : u"", # New in v2.3.0
    "Could not find the Avisynth plugins folder!" : u"", # New in v2.2.1
    "Could not find %(readme)s!" : u"Не могу найти %(readme)s!",
    "Could not find %(changelog)s!" : u"", # New in v2.4.1
    "{prog_name} v{version} ({arch})" : u"", # New in v2.5.1
    "AvsP Website" : u"AvsP WWW-сайт",
    "AvsPmod Website" : u"", # New in v2.5.1
    "Active thread on Doom9's forum" : u"", # New in v2.2.1
    "This program is freeware under the GPL license." : u"", # New in v2.2.1
    "Input a frame number or time (hr:min:sec) and hit Enter. Right-click to retrieve from history." : u"", # New in v2.2.1
    "bell at bookmarks" : u"", # New in v2.6.1.5
    "highlight bookmarks" : u"", # New in v2.6.1.5
    "set highlight color..." : u"", # New in v2.6.1.5
    "copy as time" : u"", # New in v2.2.1
    "copy" : u"", # New in v2.2.1
    "paste" : u"", # New in v2.2.1
    "clear history" : u"", # New in v2.2.1
    "Cannot switch tabs while crop editor is open!" : u"Не могу переключить вкладки если редактор обрезки активен!",
    "Cannot switch tabs while trim editor is open!" : u"Не могу переключить вкладки, если открыт редактор вырезок!",
    "Invalid crop values detected.  Continue?" : u"", # New in v2.2.1
    "You must create at least one frame selection first!" : u"Вы должны сначала создать по крайней мере одну выборку кадров!",
    "Select autocomplete keywords" : u"", # New in v2.2.1
    "select all" : u"", # New in v2.2.1
    "select none" : u"", # New in v2.2.1
    "exclude long names" : u"", # New in v2.2.1
    "Customize the video status bar message" : u"Настроить сообщение в полосе статуса видео",
    "Video status bar message:" : u"Сообщение статуса видео",
    "Legend" : u"Метка",
    "Current frame" : u"Текущий кадр",
    "Framecount" : u"Число кадров",
    "Current time" : u"Текущий кадр",
    "Total time" : u"Общее время",
    "Width" : u"Ширина",
    "Height" : u"Высота",
    "Aspect ratio" : u"Отношение сторон",
    "Framerate" : u"Частота кадров",
    "Framerate numerator" : u"Делимое частоты кадров",
    "Framerate denominator" : u"Делитель частоты кадров",
    "Colorspace" : u"Цветовое пространство",
    "Bits per component" : u"", # New in v2.6.1.5
    "Field or frame based" : u"Поля или целые кадры",
    "Parity" : u"Четность",
    "Parity short (BFF or TFF)" : u"Четность кратко (BFF или TFF)",
    "Audio rate" : u"Поток аудио",
    "Audio length" : u"Длина аудио",
    "Audio channels" : u"Каналов аудио:",
    "Audio bits" : u"Бит аудио",
    "Audio type (Integer or Float)" : u"Тип аудио (целый или вещественный)",
    "Pixel position (cursor based)" : u"Позиция пиксела (курсором)",
    "Pixel hex color (cursor based)" : u"16-ный цвет пиксела (курсором)",
    "Pixel rgb color (cursor based)" : u"RGB цвет (курсором)",
    "Pixel yuv color (cursor based)" : u"YUV цвет (курсором)",
    "Pixel color (auto-detect colorspace)" : u"Цвет пиксела (автоопределение формата)",
    "Program zoom" : u"Программный зум",
    "Bookmark title" : u"", # New in v2.4.0
    "Note: The \"\\t\\t\" or \"\\T\\T\" is used to separate the left and right portions of the status bar\n         message." : u"", # New in v2.3.0
    "A macro is still running. Close anyway?" : u"", # New in v2.3.0
    "Save changes before closing?" : u"Сохранить изменения перед закрытием?",
    "Cannot create a new tab while crop editor is open!" : u"Не могу создать новую вкладку при открытом редакторе обрезки",
    "Cannot create a new tab while trim editor is open!" : u"Не могу создать новую вкладку при открытом редакторе вырезок",
    "Source files" : u"", # New in v2.3.0
    "Open a script or source" : u"Открыть скрипт или источник",
    "Reload the file and lose the current changes?" : u"", # New in v2.2.1
    "Open this file" : u"", # New in v2.2.1
    "Save session before closing all tabs?" : u"", # New in v2.2.1
    "Save current script" : u"Сохранить текущий скрипт",
    "Directory %(dirname)s does not exist!" : u"Папка %(dirname)s не существует",
    "Script has no text!" : u"", # New in v2.5.0
    "HTML files" : u"", # New in v2.5.0
    "Load a session" : u"Загрузить сеанс",
    "File has been modified since the session was saved. Reload?" : u"Файл был изменен с момента сохранения сеанса. Загрузить заново?",
    "Save the session" : u"Сохранить сеанс",
    "Save current frame" : u"Сохранить текущий кадр",
    "Introduce the JPEG Quality (0-100)" : u"", # New in v2.5.0
    "JPEG Quality" : u"", # New in v2.5.0
    "Insert a source" : u"Вставить источник",
    "All supported plugins" : u"", # New in v2.3.0
    "AviSynth plugins" : u"", # New in v2.3.0
    "VirtualDub plugins" : u"", # New in v2.3.0
    "VFAPI plugins" : u"", # New in v2.3.0
    "Script import" : u"", # New in v2.6.1.5
    "AvxSynth plugins" : u"", # New in v2.4.0
    "Insert a plugin" : u"Вставить плагин",
    "No bookmarks defined!" : u"Нет определенных закладок!",
    "There must be more than one unique bookmark to use this feature!" : u"Должно быть более чем одна закладка для использования этой функции!",
    "Jump to specified bookmark" : u"Прыгнуть к указанной закладке",
    "Line: %(line)i  Col: %(col)i" : u"Строка: %(line)i  Колонка: %(col)i",
    "Frame Based" : u"Полные кадры",
    "Field Based" : u"Поля",
    "Bottom Field First" : u"Нижнее поле первое",
    "BFF" : u"BFF",
    "Top Field First" : u"Верхнее поле первое",
    "TFF" : u"TFF",
    "Integer" : u"Целое",
    "Float" : u"Вещественное",
    "pos" : u"поз",
    "*hex" : u"", # New in v2.6.1.5
    "Edit AviSynth function information" : u"Редактировать информацию по функции AviSynth", 
    "  Function name" : u"   Имя функции", 
    "Function arguments" : u"Аргументы функции", 
    "Open filter customization file" : u"Открыть файл настроек фильтра",
    "Filter customization file" : u"", # New in v2.3.0
    "Calltip-only text file" : u"", # New in v2.3.0
    "Invalid filter customization file!" : u"Негодный файл настроек фильтра!",
    "Save filter customization file" : u"Сохранить файл настроек фильтра",
    "Invalid argument!" : u"Неверный аргумент!",
    "Error: can not save the Session" : u"", # New in v2.6.1.5
    "Question" : u"Вопрос",
    "Save changes before previewing?" : u"Сохранить изменения перед просмотром?", 
    "Select an external player" : u"Выберете внешний проигрыватель",
    "A program must be specified to use this feature!" : u"Для использования этой функции должна быть указана программа!",
    "General settings..." : u"", # New in v2.2.1
    "Invalid slider text: min > max" : u"Негодный текст ползунка:  min > max",
    "Invalid slider text: value not in bounds" : u"Негодный текст ползунка: величина вне диапазона",
    "Invalid slider text: bad modulo label" : u"Негодный текст ползунка: плохая метка",
    "Invalid slider text: slider label already exists" : u"Негодный текст ползунка: метка уже существует",
    "Invalid slider text: invalid number" : u"Негодный текст ползунка:",
    "Reset to initial value: %(value_formatted)s" : u"Сброс к начальному значению: %(value_formatted)s",
    "Reset to initial value: %(value2_formatted)s" : u"", # New in v2.2.1
    "Reset to default value: %(value_formatted)s" : u"", # New in v2.2.1
    "Invalid hexadecimal color!" : u"", # New in v2.2.1
    "Must specify a max value!" : u"", # New in v2.2.1
    "Must specify a min value!" : u"", # New in v2.2.1
    "Min value must be a number!" : u"", # New in v2.2.1
    "Max value must be a number!" : u"", # New in v2.2.1
    "Default value must be a number!" : u"", # New in v2.2.1
    "Step size value must be a number!" : u"", # New in v2.2.1
    "Left-click to select a color, right click to reset to default" : u"", # New in v2.2.1
    "Toggle \"%(label)s\" section" : u"Блок \"%(label)s\" включен",
    "Above plugin names contain undesirable symbols.\nRename them to only use alphanumeric or underscores,\nor make sure to use them in short name style only." : u"", # New in v2.3.0
    "Found more then one function with the same name.\nYou should clean up your plugins." : u"", # New in v2.6.1.5
    "Don't show me this again" : u"", # New in v2.2.1
    "Changing the plugins directory writes to the Windows registry.\n" : u"", # New in v2.6.1.5
    "Writing to: HKLM\\Software\\Avisynth\\plugindir2_5\n" : u"", # New in v2.6.1.5
    "Plugins dir registration failed" : u"", # New in v2.6.1.5
    "You're changing the plugins autoload directory.\nDo you wish to change it for all applications? This will\nrequire writing to {0}" : u"", # New in v2.4.0
    "Save as" : u"", # New in v2.2.1
    "Select a directory" : u"Выберете папку",
    "Enter information" : u"Введите информацию",
    "Progress" : u"Выполнение",
    "A get pixel info operation has already started" : u"", # New in v2.3.0
    "Error in the macro:" : u"Ошибка в макросе:",
    "Couldn't find %(macrofilename)s" : u"Не могу найти %(macrofilename)s",
    "An AviSynth script editor" : u"Редактор скриптов AviSynth \n (автор qwerpoi, переводчик Fizick)",
    "Error trying to display the clip" : u"", # New in v2.5.1
    "Is bit-depth set correctly?" : u"", # New in v2.5.1
    "Invalid string: " : u"", # New in v2.4.0
    "Failed to open the AVI file" : u"", # New in v2.2.1
    "Failed to open the AVI frame" : u"", # New in v2.2.1
    "Failed to retrieve AVI frame" : u"", # New in v2.2.1
    "Ctrl" : u"",
    "Alt" : u"",
    "Shift" : u"",
    "Error Window" : u"", # New in v2.4.0
    "Quick find" : u"", # New in v2.4.0
    "Find/replace text" : u"", # New in v2.4.0
    "Search &for" : u"", # New in v2.5.1
    "R&eplace with" : u"", # New in v2.5.1
    "Find &next" : u"", # New in v2.5.1
    "Find &previous" : u"", # New in v2.5.1
    "&Replace next" : u"", # New in v2.5.1
    "Replace &all" : u"", # New in v2.5.1
    "Only on word s&tart" : u"", # New in v2.5.1
    "Only &whole words" : u"", # New in v2.5.1
    "Only in &selection" : u"", # New in v2.5.1
    "&Don't wrap-around" : u"", # New in v2.5.1
    "&Case sensitive" : u"", # New in v2.5.1
    "Use regular e&xpressions" : u"", # New in v2.5.1
    "&Interpret escape sequences" : u"", # New in v2.5.1
    "Cannot find \"%(text)s\"" : u"", # New in v2.3.0
    "Replaced %(count)i times" : u"Заменено %(count)i раз(а)",
    "Program Settings" : u"Настройки программы",
    "Browse" : u"Обзор",
    "* Requires program restart for full effect" : u"* Требует перезапуска программы для действия",
    "Invalid directory!" : u"Негодная папка!",
    "Invalid filename!" : u"Негодное имя файла!",
    "Edit shortcuts" : u"Редактировать сочетания клавиш",
    "Menu label" : u"Пункт меню",
    "Keyboard shortcut" : u"Сочетание клавиш",
    "Double-click or hit enter on an item in the list to edit the shortcut." : u"Для изменения - двойной щелчок или нажмите Enter на пункте",
    "Shortcut" : u"", # New in v2.2.1
    "Action" : u"", # New in v2.2.1
    "Edit the keyboard shortcut" : u"Редактировать сочетание клавиш быстрого запуска",
    "Key:" : u"Клавиша:",
    "Clear" : u"Очистить",
    "%(keyString)s not found in key string list" : u"%(keyString)s не найдена в списке сочетаний клавиш",
    "This shortcut is being used by:" : u"Это сочетание клавиш используется как:",
    "Insert" : u"Вставить",
    "Delete" : u"Удалить",
    "Error: key %(key)s does not exist!" : u"Ошибка: пункт %(key)s не существует!",
    "Item %(newKey)s already exists!" : u"Пункт %(newKey)s уже существует",
    "Are you sure you want to rename from %(oldName)s to %(newName)s?" : u"Вы уверены, что хотите переименовать %(oldName)s в %(newName)s?",
    "Insert a new item" : u"Вставьте новый пункт",
    "Must enter a name!" : u"Должны ввести имя!",
    "Warning: no value entered for item %(newKey)s!" : u"Предупреждение: не введедена величина для пункта  %(newKey)s!",
    "Message" : u"Сообщение",
    "Select an item to delete first" : u"Для удаления сначала выберете пункт",
    "Are you sure you want to delete item %(key)s?" : u"Вы уверены, что хотите удалить пункт %(key)s?",

    #--- Tool: resize_calc.py ---#
    "Resize calculator..." : u"Калькулятор размеров...",
    "Calculate an appropriate resize for the video" : u"", # New in v2.2.1
    "Resize calculator" : u"", # New in v2.2.1
    "Input" : u"", # New in v2.2.1
    "Video resolution:" : u"", # New in v2.2.1
    "Pixel aspect ratio:" : u"", # New in v2.2.1
    "Results" : u"", # New in v2.2.1
    "Aspect ratio error:" : u"", # New in v2.2.1
    "Settings" : u"", # New in v2.2.1
    "Target pixel aspect ratio:" : u"", # New in v2.2.1
    "Resize block constraints:" : u"", # New in v2.2.1
    "Resize percent ranges:" : u"", # New in v2.2.1
    "Max search aspect ratio error:" : u"", # New in v2.2.1
    "Configure" : u"", # New in v2.2.1
    "compute from .d2v" : u"", # New in v2.2.1
    "Configure options" : u"", # New in v2.2.1
    "Avisynth resize:" : u"", # New in v2.2.1
    "The current Avisynth script contains errors." : u"", # New in v2.2.1

    #--- Tool: encoder_gui.py ---#
    "Script encoder (CLI)" : u"", # New in v2.4.0
    "Use an external command line encoder to save the current script" : u"", # New in v2.4.0
    "Encode video" : u"", # New in v2.2.1
    "System settings" : u"", # New in v2.2.1
    "Input file:" : u"", # New in v2.2.1
    "Output file:" : u"", # New in v2.2.1
    "Compression settings" : u"", # New in v2.2.1
    "Bitrate (kbits/sec):" : u"", # New in v2.2.1
    "calculate" : u"", # New in v2.2.1
    "Quality CRF (0-51):" : u"", # New in v2.2.1
    "Quality CQ (1-31):" : u"", # New in v2.2.1
    "Additional settings" : u"", # New in v2.2.1
    "Credits start frame:" : u"", # New in v2.2.1
    "Command line settings" : u"", # New in v2.2.1
    "Run" : u"Выполнить",
    "First time using this compression preset!" : u"", # New in v2.2.1
    "Please enter the exe paths in the following dialog." : u"", # New in v2.2.1
    "Exe pathnames" : u"", # New in v2.2.1
    "Open an AviSynth script" : u"Открыть AviSynth скрипт",
    "Save the video as" : u"", # New in v2.2.1
    "Select a program" : u"", # New in v2.2.1
    "Unreplaced items remain in the command line:" : u"", # New in v2.2.1
    "Unknown exe paths!" : u"", # New in v2.2.1
    "General" : u"Общие",
    "Credits warning minutes:" : u"", # New in v2.2.1
    "Automatically compute bitrate value on startup" : u"", # New in v2.2.1
    "Automatically compute pixel aspect ratio from d2v on startup" : u"", # New in v2.2.1
    "Append batch commands to the avs script as comments" : u"", # New in v2.2.1
    "Encoder priority:" : u"", # New in v2.2.1
    "Path to %(name)s:" : u"", # New in v2.2.1
    "Extra arguments:" : u"", # New in v2.2.1
    "Bitrate Calculator" : u"", # New in v2.2.1
    "Output info" : u"", # New in v2.2.1
    "Total size:" : u"", # New in v2.2.1
    "Container:" : u"", # New in v2.2.1
    "(None)" : u"", # New in v2.2.1
    "Video info" : u"", # New in v2.2.1
    "Framecount:" : u"", # New in v2.2.1
    "FPS:" : u"", # New in v2.2.1
    "Audio info" : u"", # New in v2.2.1
    "Audio file:" : u"", # New in v2.2.1
    "Compress audio" : u"", # New in v2.2.1
    "Audio bitrate:" : u"", # New in v2.2.1
    "Format:" : u"", # New in v2.2.1
    "Subtitles info" : u"", # New in v2.2.1
    "Subtitles file:" : u"", # New in v2.2.1
    "Total time:" : u"", # New in v2.2.1
    "Video size:" : u"", # New in v2.2.1
    "Audio size:" : u"", # New in v2.2.1
    "Subtitles size:" : u"", # New in v2.2.1
    "Overhead size:" : u"", # New in v2.2.1
    "Bitrate:" : u"", # New in v2.2.1
    "Open the audio file" : u"", # New in v2.2.1
    "Open the subtitles file" : u"", # New in v2.2.1
    "%(h)i hr and %(m)i min" : u"", # New in v2.2.1

    #--- Tool: avs2avi_gui.py ---#
    "Script encoder (VFW)" : u"", # New in v2.4.0
    "Use avs2avi to save the current script as an avi" : u"", # New in v2.2.1
    "Please select the path to avs2avi.exe" : u"", # New in v2.2.1
    "Error: avs2avi is required to save an avi!" : u"Ошибка: требуется avs2avi для сохранения в AVI !",
    "Pass: %(pass)s / %(passes)s" : u"Проход: %(pass)s / %(passes)s",
    "Frame: %(frame)i / %(frames)i" : u"Кадр: %(frame)i / %(frames)i",
    "Size: %(size).2f MB" : u"Размер: %(size).2f MB",
    "FPS: %(fps).1f fps" : u"Частота: %(fps).1f к/с",
    "Time left: %(hr)02i:%(min)02i:%(sec)02i" : u"Оставшееся время: %(hr)02i:%(min)02i:%(sec)02i",
    "Input file (.avs):" : u"Входной файл (.avs):",
    "Output file (.avi):" : u"Выходной файл (.avi):",
    "# of passes:" : u"Число проходов:",
    "Priority:" : u"Приоритет",
    "Error: Unknown button" : u"Ошибка: неизвестная клавиша",
    "AviSynth script (*.avs)|*.avs" : u"AviSynth скрипт (*.avs)|*.avs",
    "Save the avi as" : u"Сохранить AVI как",
    "Avi file (*.avi)|*.avi" : u"AVI файл (*.avi)|*.avi",
    "Input file does not exist!" : u"Входной файл не существует!",
    "Input file must be an avisynth script!" : u"Входной файл должен быть скриптом Avisynth!",
    "Output path does not exist!" : u"Выходной путь не существует",
    "# of passes must be an integer!" : u"Число проходов должно быть целым!",
    "Priority must be an integer!" : u"Приоритет должен быть целым!",
    "Stop" : u"Стоп",
    "Done" : u"Сделано",
    "Process stopped." : u"Обработка остановлена.",
    "Processing..." : u"Обрабатываю...",
    "Finished in %(hr)i hour(s) and %(min)i minute(s)." : u"Завершено за %(hr)i часов и %(min)i минут.",
    "Finished in %(min)i minute(s) and %(sec)i second(s)." : u"Завершено за %(min)i минут и %(sec)i секунд.",
    "Finished in %(time).1f seconds." : u"Завершено за %(time).1f секунд.",
    "Filesize: %(size).2f MB" : u"Размер файла: %(size).2f MB",
    "The current script contains errors, exiting." : u"", # New in v2.2.1
    "Save as AVI" : u"Сохранить как AVI",

    #--- Macros ---#
    "Bookmarks at Intervals" : u"", # New in v2.3.0
    "Bookmarks to Chapter" : u"", # New in v2.3.0
    "ConditionalReader file from bookmarks" : u"", # New in v2.3.0
    "DeleteFrame" : u"", # New in v2.3.0
    "DuplicateFrame" : u"", # New in v2.3.0
    "Import bookmarks from file" : u"", # New in v2.3.1
    "Preview from current point" : u"", # New in v2.3.0
    "Random Clip Order" : u"", # New in v2.3.0
    "Save Image Sequence" : u"", # New in v2.3.0
    "Shift Bookmarks by frames" : u"", # New in v2.3.0
    "Example (Resize)" : u"", # New in v2.3.0
    "Examples" : u"", # New in v2.3.0
    "Customized" : u"", # New in v2.3.0
    "bilinear" : u"", # New in v2.3.0
    "bicubic" : u"", # New in v2.3.0
    "lanczos" : u"", # New in v2.3.0
    "spline36" : u"", # New in v2.3.0
    "create new tab" : u"", # New in v2.3.0
    "force mod 2" : u"", # New in v2.3.0
    "Template example" : u"", # New in v2.3.0
    "Batch example" : u"", # New in v2.3.0
    "Image processing" : u"", # New in v2.3.0
    "Manual Telecide" : u"", # New in v2.3.0
    "Secondary preview" : u"", # New in v2.3.0
    "Encoding example" : u"", # New in v2.3.0
    "Encoding example 2" : u"", # New in v2.3.0
    "Optimize Sliders" : u"", # New in v2.3.0

    #--- Macro: Bookmarks at Intervals ---#
    "Choose a frame step or a number of intervals" : u"", # New in v2.3.0
    "Frame step" : u"", # New in v2.3.0
    "Number of intervals" : u"", # New in v2.3.0
    "End frame" : u"", # New in v2.4.2
    "Start frame" : u"", # New in v2.4.2
    "Clear bookmarks in the same range" : u"", # New in v2.4.2

    #--- Macro: Bookmarks to Chapter ---#
    "Save chapter file as..." : u"", # New in v2.4.0
    "Text files" : u"", # New in v2.3.0

    #--- Macro: ConditionalReader file from bookmarks ---#
    "There is not bookmarks" : u"", # New in v2.3.0
    "Type" : u"", # New in v2.2.1
    "Value" : u"", # New in v2.3.0
    "Bookmarks represent..." : u"", # New in v2.3.0
    "Override 'Value' with the bookmark's title" : u"", # New in v2.3.0
    "ConditionalReader file" : u"", # New in v2.3.0
    "Insert the ConditionalReader file path at the current cursor position" : u"", # New in v2.3.0
    "Bool" : u"", # New in v2.3.0
    "String" : u"Строка",
    "Int" : u"", # New in v2.3.0
    "False" : u"", # New in v2.3.0
    "True" : u"", # New in v2.3.0
    "Single frames" : u"", # New in v2.3.0
    "Ranges of frames" : u"", # New in v2.3.0
    "Ranges of frames (with interpolation)" : u"", # New in v2.3.0
    "An output path is needed" : u"", # New in v2.3.1
    "Interpolation only available for Int and Float" : u"", # New in v2.3.0
    "Odd number of bookmarks" : u"", # New in v2.3.0

    #--- Macro: Import bookmarks from file ---#
    "All supported files" : u"", # New in v2.3.1
    "Chapters Text files" : u"", # New in v2.3.0
    "Matroska XML files" : u"", # New in v2.3.0
    "Celltimes files" : u"", # New in v2.3.0
    "AvsP Session files" : u"", # New in v2.3.0
    "TFM log files" : u"", # New in v2.3.1
    "XviD log files" : u"", # New in v2.3.1
    "QP files" : u"", # New in v2.3.1
    "Timecode format v1 files" : u"", # New in v2.4.0
    "Bookmarks from TFM file" : u"", # New in v2.3.1
    "Not combed or out of order frames" : u"", # New in v2.3.1
    "Combed" : u"", # New in v2.3.1
    "Possible" : u"", # New in v2.3.1
    "u,b,out-of-order" : u"", # New in v2.3.1
    "Min frame:" : u"", # New in v2.3.1
    "Max frame:" : u"", # New in v2.3.1
    "TFM log parser" : u"", # New in v2.3.1
    "%d frames imported" : u"", # New in v2.3.1
    "[COMBED FRAMES] section could not be parsed" : u"", # New in v2.3.1
    "Bookmark file unrecognized!" : u"", # New in v2.3.0

    #--- Macro: Preview from current point ---#
    "Failed to run the external player!\n\nOpen the macro file in the \"Macros\" subdirectory\nwith a text editor and edit the executable\ndirectory appropriately!" : u"", # New in v2.3.0

    #--- Macro: Save Image Sequence ---#
    "Save image sequence" : u"", # New in v2.4.0
    "Output format" : u"", # New in v2.4.0
    "Select frames" : u"", # New in v2.4.0
    "Depth (PNG only)" : u"", # New in v2.5.0
    "Quality (JPEG only)" : u"", # New in v2.4.0
    "Show saving progress" : u"", # New in v2.4.0
    "Output directory and basename. A padded number is added as suffix" : u"", # New in v2.5.0
    "Use always this basename" : u"", # New in v2.4.0
    "Use always this directory" : u"", # New in v2.4.0
    "Add the frame number as the suffix" : u"", # New in v2.5.0
    "Save ranges to subdirectories" : u"", # New in v2.5.0
    "Range between bookmarks" : u"", # New in v2.4.0
    "Trim editor selections" : u"", # New in v2.4.0
    "All frames" : u"", # New in v2.4.0
    "Select an output directory and basename for the new images files" : u"", # New in v2.4.0
    "There is not Trim editor selections" : u"", # New in v2.4.0
    "Saving images..." : u"", # New in v2.3.0
    "scene_{0:0{1}}" : u"", # New in v2.5.0
    "%d image files created." : u"", # New in v2.3.0

    #--- Macro: Shift Bookmarks by frames ---#
    "Introduce the number of frames:" : u"", # New in v2.3.0
    "Shift bookmarks by # frames" : u"", # New in v2.3.0

    #--- Macro: Customized ---#
    "Customized aspect ratio" : u"", # New in v2.3.0
    "Enter a pixel ratio or new size. e.g. 40:33, 1.212 or 640x360" : u"", # New in v2.3.0

    #--- Macro: Image processing ---#
    "Processing images..." : u"", # New in v2.3.0
    "Macro aborted" : u"", # New in v2.3.0

    #--- Macro: Manual Telecide ---#
    "Open a source to Telecide" : u"", # New in v2.3.0
    "Filename was mangled! Get it again!" : u"", # New in v2.3.0
    "Enter the field order:" : u"", # New in v2.3.0
    "Must enter either a 0 or 1!" : u"", # New in v2.3.0
    "Must enter an integer!" : u"", # New in v2.3.0
    "Override filename was mangled! Get it again!" : u"", # New in v2.3.0
    "Not allowed to select base Telecide tab!" : u"", # New in v2.3.0
    "Unknown mode!" : u"", # New in v2.3.0

    #--- Macro: Encoding example ---#
    "Encoding is disabled, please read the \"Encoding example.py\" macro for info" : u"", # New in v2.3.0

    #--- Macro: Encoding example 2 ---#
    "Output filename:" : u"", # New in v2.3.0
    "Output height:" : u"", # New in v2.3.0
    "Output width:" : u"", # New in v2.3.0
    "Enter encoder info" : u"", # New in v2.3.0
    "Encoding is disabled, please read the \"Encoding example 2.py\" macro for info" : u"", # New in v2.3.0

    #--- Macro: Optimize Sliders ---#
    "Generation 0 Progress" : u"", # New in v2.3.0
    "Initial evaluation..." : u"", # New in v2.3.0
    "Initial best score: %.3f, Current best score: %.3f" : u"", # New in v2.3.0
    "Best score: %.2f" : u"", # New in v2.3.0
    "Must configure avs2avi directory to use this macro!" : u"", # New in v2.3.0
    "Not user sliders on the current Avisynth script!" : u"", # New in v2.4.0
    "Enter optimization info    (%i bits, %i possibilities)" : u"", # New in v2.3.0
    "SSIM log filename:" : u"", # New in v2.3.0
    "max generations:" : u"", # New in v2.3.0
    "population size:" : u"", # New in v2.3.0
    "crossover probability:" : u"", # New in v2.3.0
    "mutation probability:" : u"", # New in v2.3.0
    "selection pressure:" : u"", # New in v2.3.0
    "Begin optimization..." : u"", # New in v2.3.0
    "Finished optimization." : u"", # New in v2.3.0

    #--- Macros - Extra ---#
}