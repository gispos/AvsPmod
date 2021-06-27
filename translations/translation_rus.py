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
# Translated by Arx1meD 25.06.2021 for AvsPmod v2.6.8.4

version = "2.6.8.4"

messages = {
    "AviSynth script" : u"Скрипт AviSynth", # New in v2.3.0
    "AviSynth fonts and colors" : u"Шрифты и цвета AviSynth", 
    "Background" : u"Фон", 
    "Font" : u"Шрифт", 
    "Text color" : u"Цвет текста", 
    "Select a predefined theme" : u"Выберите тему", # New in v2.5.1
    "Only change colours" : u"Изменять только цвета",
    "When selecting a theme, don't change current fonts" : u"При выборе темы не изменять шрифты.",
    "OK" : u"Применить", 
    "Cancel" : u"Отмена",
    "Page:" : u"Страница",
    "Page: %d" : u"Страница: %d",
    "Scrap Window" : u"Окно заметок",
    "Undo" : u"Отменить",
    "Redo" : u"Вернуть",
    "Cut" : u"Вырезать",
    "Copy" : u"Копировать",
    "Paste" : u"Вставить",
    "Select all" : u"Выделить все",
    "Refresh" : u"Обновить",
    "Insert frame #" : u"Вставить номер кадра",
    "Save to file..." : u"Сохранить в файл...",
    "Clear all" : u"Очистить всё",
    "Toggle scrap window" : u"Показать/Скрыть окно заметок",
    "Save script" : u"Сохранить скрипт",
    "Error: no contextMenu variable defined for window" : u"Ошибка: для окна не определена переменная contextMenu",
    "Text document" : u"Текстовый документ",
    "All files" : u"Все файлы",
    "Save scrap text" : u"Сохранить текст заметок",
    "This field must contain a value!" : u"Данное поле должно содержать значение!",
    "This slider label already exists!" : u"Данная метка ползунка уже существует!",
    "Invalid slider label modulo syntax!" : u"Неверный синтаксис метки модуля ползунка!",
    "This field must contain a number!" : u"Данное поле должно содержать число!",
    "The min value must be less than the max!" : u"Минимальное значение должно быть меньше максимального!",
    "The initial value must be between the min and the max!" : u"Начальное значение должно быть между минимумом и максимумом!",
    "The min value must be a multiple of %(mod)s!" : u"Мин. значение должно быть кратно %(mod)s!",
    "The max value must be a multiple of %(mod)s!" : u"Макс. значение должно быть кратно %(mod)s!",
    "The initial value must be a multiple of %(mod)s!" : u"Начальное значение должно быть кратно %(mod)s!",
    "The difference between the min and max must be greater than %(mod)s!" : u"Разница между мин. и макс. должна быть больше чем %(mod)s!",
    "Error" : u"Ошибка",
    "Define user slider" : u"Вставить пользовательский ползунок",
    "Slider label:" : u"Метка ползунка:",
    "Min value:" : u"Минимальное значение:",
    "Max value:" : u"Максимальное значение:",
    "Initial value:" : u"Начальное значение:",
    "Add or override AviSynth functions in the database" : u"Добавить или изменить функции в базе данных AviSynth",
    "Core filters" : u"Встроенные фильтры",
    "Plugins" : u"Фильтры из плагинов",
    "User functions" : u"Пользовательские функции",
    "Script functions" : u"Встроенные функции",
    "Clip properties" : u"Свойства клипа",
    "New function" : u"Новая функция", # New in v2.2.1
    "Edit selected" : u"Редактировать выбранное",
    "Delete selected" : u"Удалить выбранное",
    "Select installed" : u"Выделить установленные", # New in v2.2.1
    "Import" : u"Импорт",
    "Import from files" : u"Импорт из файла",
    "Import from wiki" : u"Импорт из Wiki",
    "Export customizations" : u"Экспорт настроек", # New in v2.2.1
    "Clear customizations" : u"Очистить настройки", # New in v2.2.1
    "Clear manual presets" : u"Очистить предустановки вручную", # New in v2.2.1
    "When importing, don't show the choice dialog" : u"При импорте не показывать диалоговое окно выбора",
    "Edit function information" : u"Изменить информации о функциях", # New in v2.2.1
    "Name:" : u"Имя",
    "Type:" : u"Тип",
    "clip property" : u"свойство клипа", 
    "core filter" : u"встроенный фильтр",
    "plugin" : u"фильтр из плагина", # New in v2.2.1
    "script function" : u"функция скрипта", # New in v2.2.1
    "user function" : u"функция пользователя", # New in v2.2.1
    "Arguments:" : u"Аргументы:", # New in v2.2.1
    "define sliders" : u"настроить ползунки",
    "reset to default" : u"восстановить значения по умолчанию",
    "Slider information" : u"Информация ползунков",
    "Preset:" : u"Предустановка:",
    "Auto-generate" : u"Создать автоматически",
    "Filter name already exists!" : u"Такое имя фильтра уже существует!",
    "Invalid filter name!" : u"Недопустимое имя фильтра!",
    "Renaming not allowed!" : u"Переименование запрещено!",
    "You must use dllname_function naming format for plugins!" : u"Для плагинов необходимо использовать формат наименования dllname_function!",
    "Long name" : u"Длинное имя",
    "Short name" : u"Короткое имя",
    "Both" : u"Оба",
    "Only long names" : u"Только длинные имена",
    "Only short names" : u"Только короткие имена",
    "All names" : u"Все имена",
    "Open Customization files, AviSynth scripts or AvsP options files" : u"Открыть файл настройки, скрипты AviSynth или файл настроек AvsP",
    "All supported" : u"Все поддерживаемые",
    "Customization file" : u"Файл настроек",
    "AvsP data" : u"Данные AvsP",
    "Unrecognized files" : u"Не распознанные файлы",
    "Select the functions to import" : u"Выберите функции для импорта",
    "Check selected" : u"Отметить выбранное",
    "Check all" : u"Отметить все",
    "Check all in this file" : u"Отметить все в этом файле",
    "Check all not customized" : u"Отметить все не настроенное", # New in v2.4.2
    "Uncheck selected" : u"Убрать отметку с выбранного", # New in v2.4.2
    "Uncheck all" : u"Убрать все отметки", # New in v2.4.2
    "Uncheck all in this file" : u"Убрать все отметки в этом файле", # New in v2.4.2
    "Uncheck all customized" : u"Убрать отметки со всех настроенных", # New in v2.4.2
    "Red - a customized function already exists." : u"Красный - настраиваемая функция уже существует.", # New in v2.2.1
    "Invalid plugin function name \"{name}\". Must be \"pluginname_functionname\"." : u"Неправильное имя функции плагина \"{name}\". Должно быть \"pluginname_functionname\".", # New in v2.5.1
    "No customizations to export!" : u"Нет настроек для экспорта!", # New in v2.2.1
    "Save filter customizations" : u"Сохранить настройки фильтра", # New in v2.2.1
    "This will delete all filter customizations. Continue?" : u"Все настройки фильтра будут удалены. Продолжить?", # New in v2.2.1
    "Warning" : u"Предупреждение",
    "This will delete all manually defined presets. Continue?" : u"Это удалит все заданные вручную предустановки. Продолжать?", # New in v2.2.1
    "Do you really want to delete this custom filter?" : u"Вы действительно хотите удалить этот настраиваемый фильтр?", # New in v2.5.0
    "Do you really want to reset this filter?" : u"Вы действительно хотите сбросить этот фильтр?", # New in v2.5.0
    "Edit filter database" : u"Редактировать базу данных фильтров", # New in v2.2.1
    "Default" : u"По умолчанию",
    "Min value" : u"Мин. значение",
    "Max value" : u"Мак. значение",
    "Step size" : u"Шаг", # New in v2.2.1
    "Value list (comma separated)" : u"Список значений (через запятую)", # New in v2.2.1
    "Value must be True or False!" : u"Значение должно быть True (истинным) или False (ложным)!", # New in v2.2.1
    "Export filter customizations" : u"Экспорт настроек фильтра",
    "Import filter customizations" : u"Импорт настроек фильтра",
    "Select filters to export:" : u"Выберите фильтры для экспорта:",
    "Select filters to import from the file:" : u"Выберите фильтры для импорта из файла:",
    "Overwrite all data" : u"Перезаписать все данные",
    "You must select at least one filter!" : u"Вы должны выбрать по крайней мере один фильтр!",
    "Slider SetRange Error: minValue must be less than maxValue" : u"Ошибка ползунка SetRange: minValue должно быть меньше maxValue", # New in v2.6.8.4
    "New File" : u"Новый файл",
    "Windows Bitmap" : u"", # New in v2.3.0
    "Animation" : u"", # New in v2.3.0
    "JPEG" : u"", # New in v2.3.0
    "Zsoft Paintbrush" : u"",
    "Portable Network Graphics" : u"", # New in v2.3.0
    "Netpbm" : u"", # New in v2.3.0
    "Tagged Image File" : u"", # New in v2.3.0
    "ASCII Text Array" : u"", # New in v2.3.0
    "Windows Icon" : u"", # New in v2.3.0
    "Windows Cursor" : u"", # New in v2.4.0
    "Frame" : u"Кадр",
    "fps" : u"кадр/с",
    "A crash detected at the last running!" : u"При последнем запуске обнаружен сбой!", # New in v2.2.1
    "&Zoom" : u"&Изменить масштаб", # New in v2.2.1
    "Damaged {0}. Using default settings." : u"Повреждено {0}. Использование настроек по умолчанию.", # New in v2.4.0
    "%s translation file updated with new messages to translate" : u"%s файл перевода дополнен новыми сообщениями для перевода", # New in v2.3.0
    "Translation updated" : u"Перевод обновлен", # New in v2.3.0
    "%s translation file updated.  No new messages to translate." : u"%s файл перевода обновлён. Нет новых сообщений для перевода.", # New in v2.3.0
    "%s language couldn't be loaded" : u"%s не удалось загрузить язык", # New in v2.3.0
    "Default dark" : u"Темная по умолчанию", # New in v2.6.8.4
    "Solarized light" : u"Выцветшая светлая", # New in v2.5.1
    "Solarized dark" : u"Выцветшая тёмная", # New in v2.5.1
    "Cannot read the avisynth plugins directory from the registry\n" : u"Не удалось прочитать каталог плагинов AviSynth из реестра\n",
    "HKLM\\Software\\Avisynth'plugindir2_5' or 'plugindir+' is missing or wrong.\n\n" : u"HKLM\\Software\\Avisynth'plugindir2_5' или 'plugindir+' отсутствует или неправильная.\n\n", # New in v2.6.1.5
    "You should set the plugins path under options manually or register it." : u"Вы должны установить путь к плагинам в разделе параметры вручную или зарегистрировать его.",
    "Alternatively, specify now its directory." : u"Либо теперь укажите его каталог.", # New in v2.4.0
    "Select the {0} directory" : u"Выберите каталог {0}",
    "Make sure you have AviSynth installed and that there are no unstable plugins or avsi files in the AviSynth plugins directory." : u"Убедитесь, что у вас установлен AviSynth и что в каталоге плагинов AviSynth нет нестабильных плагинов или avsi-файлов.",
    "Error loading AviSynth!" : u"Ошибка при загрузке AviSynth!",
    "Paths" : u"Каталоги",
    "Available variables: %programdir%, %avisynthdir%, %pluginsdir%" : u"Доступные переменные: %programdir%, %avisynthdir%, %pluginsdir%",
    "Choose a different version than the installed" : u"Выберите версию, отличную от установленной",
    "Use a custom AviSynth directory" : u"Использовать AviSynth из другого каталога",
    "Alternative location of avisynth.dll/avxsynth.so" : u"Альтернативное расположение avisynth.dll/avxsynth.so",
    "Custom AviSynth directory:" : u"Пользовательский каталог AviSynth:",
    "Leave blank for reset or choose a directory for manually set or for register" : u"Оставьте поле пустым для сброса или выберите каталог для ручной настройки или регистрации.",
    "Disable autoload, set manually" : u"Отключить автозагрузку и указать вручную",
    "If plugins autoload fails set the path manually. Read only. Only for proper program functions" : u"Если плагины не загружаются автоматически, то укажите вручную путь к ним. Только для чтения. Только для правильных функций программы",
    "Register the plugins directory" : u"Зарегистрировать каталог плагинов",
    "This changes the plugins directory for Avisynth itself. On Windows Registry values in HKLM are changed." : u"Это изменит каталог плагинов для AviSynth. Так же будут изменены записи в реестре Windows в разделе HKLM.", # New in v2.6.1.5
    "Override the current working directory" : u"Переопределение текущего рабочего каталога",
    "Use a custom working directory" : u"Используйте пользовательский рабочий каталог",
    "For all scripts" : u"Для всех скриптов",
    "Use the custom directory also for scripts saved to file, instead of its parent" : u"Для скриптов, сохраняемых в файл, использовать пользовательский каталог вместо основного",
    "Specify an alternative working directory" : u"Укажите альтернативный рабочий каталог",
    "Working directory:" : u"Рабочий каталог",
    "External player:" : u"Внешний проигрыватель",
    "Location of external program for script playback" : u"Расположение внешней программы для проигрывания скриптов",
    "Executable files" : u"Исполняемые файлы",
    "Additional arguments when running the external player" : u"Доп. аргументы при запуске внешнего проигрывателя", 
    "External player extra args:" : u"Аргументы внешнего проигрывателя:", 
    "External tool:" : u"Внешняя программа",
    "Location of external program, e.g. AvsMeter" : u"Расположение внешней программы, например, AvsMeter", # New in v2.6.5.1
    "Arguments for external tool menu 1, e.g. Menu label|arguments\nUse %fn to pass the script file name with the arguments." : u"Доп. аргументы для внешнего меню программы 1.\nНапример Menu label|arguments\nИспользуйте %fn, чтобы передать имя файла сценария с аргументами.", # New in v2.6.5.1
    "External tool arg1:" : u"Аргументы внешней программы, arg1:",
    "Arguments for external tool menu 2, e.g. Menu label|arguments\nUse %fn to pass the script file name with the arguments." : u"Доп. аргументы для внешнего меню программы 2.\nНапример Menu label|arguments\nИспользуйте %fn, чтобы передать имя файла сценария с аргументами.", # New in v2.6.5.1
    "External tool arg2:" : u"Аргументы внешней программы, arg2:",
    "Avisynth help file/url:" : u"Файл или ссылка на справку по AviSynth",
    "Location of the avisynth help file or url" : u"Расположение файла справки по AviSynth или веб-ссылка",
    "Documentation search paths:" : u"Каталог поиска справки:",
    "Specify which directories to search for docs when you click on a filter calltip" : u"Укажите в каких папках искать документы, когда Вы щёлкните на подсказке для фильтра",
    "Documentation search url:" : u"Веб-ссылка для поиска справки:",
    "The web address to search if docs aren't found (the filter's name replaces %filtername%)" : u"Веб-адрес для поиска, если документы не найдены локально (имя фильтра заменить на %filtername%)",
    "Text" : u"Текст",
    "Highlight the text as if it wasn't enclosed by triple quotes" : u"Показывать подсветку текста, так как если бы он не был заключен в тройные кавычки",
    "Style inside triple-quoted strings" : u"Выделять текст внутри строк с тройными кавычками",
    "Prefer functions over variables" : u"Предпочтение функций перед переменными", # New in v2.5.0
    "When a word could be either a function or a variable, highlight it as function" : u"Когда слово может быть функцией или переменной, то выделить его как функцию", # New in v2.5.0
    "Don't allow lines wider than the window" : u"Не допускать длину строки шире окна", 
    "Wrap text" : u"Перенос текста",
    "Draw lines at fold points" : u"Показать линии для свёрнутых блоков скрипта", # New in v2.2.1
    "For code folding, draw a line underneath if the fold point is not expanded" : u"Если блок скрипта свёрнут, то показывать под ней линию", # New in v2.2.1
    "Check to insert actual tabs instead of spaces when using the Tab key" : u"Вставлять отступы вместо пробелов при нажатии клавиши Tab",
    "Use tabs instead of spaces" : u"Использовать отступы вместо пробелов",
    "Set the size of the tabs in spaces" : u"Установить размер отступа в пробелах",
    "Tab width" : u"Ширина отступа",
    "Initial space to reserve for the line margin in terms of number of digits. Set it to 0 to disable showing line numbers" : u"Начальное место, зарезервированное для поля строки в виде количества цифр. Установите значение 0, чтобы отключить отображение номеров строк.", # New in v2.3.1
    "Line margin width" : u"Ширина отступа строк",
    "Show filter calltips" : u"Показывать подсказки для фильтра",
    "Turn on/off automatic tips when typing filter names" : u"Показывать автоматические подсказки при написании имени фильтра",
    "Always show calltips any time the cursor is within the filter's arguments" : u"Всегда показывать подсказки во время нахождения курсора в аргументах фильтра", 
    "Frequent calltips" : u"Частые подсказки",
    "Show autocomplete on capital letters" : u"Показывать автозавершение с заглавной буквы", # New in v2.2.1
    "Turn on/off automatic autocomplete list when typing words starting with capital letters" : u"Показывать список автоматического завершения при написании слов, начинающихся с заглавных букв",
    "Amount of letters typed" : u"Количество написанных букв", # New in v2.3.0
    "Show autocomplete list when typing a certain amount of letters" : u"Показывать список автозавершений при вводе определенного количества букв", # New in v2.2.1
    "Autocomplete" : u"Автозавершение",
    "AviSynth user function database" : u"База данных пользовательских функций AviSynth", # New in v2.4.2
    "Select what functions beside internal and user-defined will be included in the database" : u"Выберите, какие функции, помимо встроенных и пользовательских, будут включены в базу данных", # New in v2.4.2
    "Autoloaded plugin functions" : u"Автозагружать фильтры из плагинов", # New in v2.4.2
    "Include the functions on autoloaded plugins in the database" : u"Автоматически загружать фильтры из плагинов в базу данных", # New in v2.4.2
    "Autoloaded script functions" : u"Автозагружать функции из скриптов", # New in v2.4.2
    "Include the functions on autoloaded avsi files in the database" : u"Автоматически загружать функции из файлов avsi в базу данных", # New in v2.4.2
    "Include plugin functions from the program's database" : u"Использовать фильтры плагинов из базы данных программы", # New in v2.4.2
    "Plugin functions from database" : u"Фильтры плагинов из базы данных", # New in v2.4.2
    "Include user script functions from the program's database" : u"Использовать функции пользовательских скриптов из базы данных программы", # New in v2.4.2
    "Script functions from database" : u"Функции скриптов из базы данных", # New in v2.4.2
    "Add user defined variables into autocomplete list" : u"Добавить пользовательские переменные в список автозавершения", # New in v2.2.1
    "Show autocomplete with variables" : u"Показывать автозавершение с переменными", # New in v2.2.1
    "Show autocomplete on single matched lowercase variable" : u"Показывать автозавершение для одной совпавшей переменной в нижнем регистре", # New in v2.2.1
    "When typing a lowercase variable name, show autocomplete if there is only one item matched in keyword list" : u"При вводе имени переменной в нижнем регистре показывать автозавершение, если в списке ключевых слов совпадает только один элемент", # New in v2.2.1
    "Add icons into autocomplete list. Using different type to indicate how well a filter's presets is defined" : u"Добавлять значки в список автозавершения. Использовать различные типы значков для определения того, насколько хорошо настроены предустановки фильтра", # New in v2.2.1
    "Show autocomplete with icons" : u"Показать список автозавершений со значками", # New in v2.2.1
    "Don't show autocomplete when calltip is active" : u"Не показывать автозавершение, когда активна подсказка", # New in v2.2.1
    "When calltip is active, autocomplete will not be activate automatically. You can still show autocomplete manually" : u"Когда активна подсказка, автозавершение не активируется автоматически. Вы по-прежнему можете вызвать автозавершение вручную", # New in v2.2.1
    "Autoparentheses level" : u"Авто-завершение скобок",
    "Close \"()\"" : u"Закрытые \"()\"",
    "Determines parentheses to insert upon autocompletion" : u"Дополняет скобки при автозавершении",
    "None \" \"" : u"Отсутствует \" \"",
    "Open \"(\"" : u"Открытая \"(\"",
    "Determines which key activates the filter preset when the autocomplete box is visible" : u"Определяет, какая клавиша активирует предустановку фильтра, когда отображается окошко автозавершения", # New in v2.2.1
    "Preset activation key" : u"Предустановленный ключ активации", # New in v2.2.1
    "Return" : u"Вернуть", # New in v2.2.1
    "Tab" : u"Вкладка", # New in v2.2.1
    "None" : u"Нет",
    "Video" : u"Видео",
    "Constantly update video while dragging" : u"Непрерывно обновлять видео при перетаскивании ползунка",
    "Update the video constantly when dragging the frame slider" : u"Постоянно обновлять видео при перетаскивании ползунка кадров",
    "Enable line-by-line update" : u"Разрешить обновление видео построчно", 
    "Enable the line-by-line video update mode (update every time the cursor changes line position)" : u"Разрешить режим построчного обновления видео (обновлять каждый раз при смене позиции строки курсора)", 
    "Focus the video preview upon refresh" : u"Фокус на видеопросмотре при обновлении",
    "Switch focus to the video preview window when using the refresh command" : u"Переключить фокус на окно видеопросмотра при использовании команды обновить",
    "Refresh preview automatically" : u"Автообновление видеопросмотра при смене окна", # New in v2.2.1
    "Refresh preview when switch focus on video window or change a value in slider window" : u"Обновить видеопросмотра при изменении фокуса на окно видео или изменении значения на временной шкале видео", # New in v2.2.1
    "Move video slider to timeline start" : u"Переместить ползунок видео к началу временной шкалы", # New in v2.6.8.4
    "On moving timeline range with keys Ctrl + Alt + PageDown\nTimeline moving with Ctrl + Alt + (Left, Right, PageUp, PageDown)\n or left mouse button on the status bar, with Shift no limit" : u"При перемещении диапазона временной шкалы нажатием клавиш Ctrl+Alt+PageDown\nВременная шкала перемещается нажатием клавиш Ctrl+Alt+(Left, Right, PageUp, PageDown)\n или левой кнопки мыши в строке состояния без удерживания Shift", # New in v2.6.8.4
    "Seeking to a certain frame will seek to that frame on all tabs" : u"При поиске определенного кадра будет выполняться поиск этого кадра на всех вкладках", # New in v2.2.1
    "Shared timeline" : u"Общая временная шкала",
    "Only on tabs of the same characteristics" : u"Только на вкладках с одинаковыми характеристиками",
    "Only share timeline for clips with the same resolution and frame count" : u"Синхронизировать временную шкалу только для клипов с одинаковым разрешением и количеством кадров",
    "Determines which mouse wheel function is used, see below tabs.Tab change also possible under Misc -> Mouse browse buttons" : u"Определяет, какое действие выполняет колёсико мыши, см. вкладки далее. Смена вкладки также возможна в разделе Разное -> Обзор кнопками мышки",
    "Mouse wheel function" : u"Действие колёсика мышки",
    "Tab change or scroll" : u"Смена вкладки при прокрутке колёсика мыши",
    "Frame step" : u"Смена кадра",
    "Tab change" : u"Смена вкладки",
    "Enable scroll wheel through similar tabs" : u"Включить прокрутку колёсиком через похожие вкладки",
    "Mouse scroll wheel cycles through tabs with similar videos" : u"Прокручивая колёсико мышки циклически перемещаться по вкладкам с похожими видео",
    "Enable scroll wheel through tabs on the same group" : u"Включить прокрутку колёсиком через вкладки в одной группе",
    "Mouse scroll wheel cycles through tabs assigned to the same tab group" : u"Прокручивая колёсико мышки циклически перемещаться по вкладкам, входящим в одной и ту-же группу вкладок",
    "Allow AvsPmod to resize and/or move the program window when updating the video preview" : u"Разрешить AvsPmod изменять размер и/или перемещать окно программы при обновлении предварительного просмотра видео",
    "Allow AvsPmod to resize the window" : u"Разрешить AvsPmod изменять размер окна",
    "Separate video preview window" : u"Видеопросмотр в отдельном окне",
    "Use a separate window for the video preview" : u"Показывать предварительный просмотр видео в отдельном окне",
    "Keep it on top of the main window" : u"Показывать его поверх главного окна",
    "Keep the video preview window always on top of the main one and link its visibility" : u"Всегда показывать окно видеопросмотра поверх основного окна и связать его с ним",
    "Startup with last zoom settings" : u"Запуск с последними настройками масштабирования",
    "Use last zoom settings at startup" : u"Использовать последние настройки масштабирования при запуске",
    "Min text lines on video preview" : u"Мин. число строк/пикселей при просмотре видео",
    "Minimum number of lines to show when displaying the video preview" : u"Минимальное количество строк (или пикселей), отображаемых при просмотре видео",
    "Customize the video information shown in the program status bar" : u"Настройка информации о видео, отображаемой в строке состояния программы",
    "Customize video status bar..." : u"Настройка строки состояния...",
    "Error message font..." : u"Шрифт сообщения об ошибке...",
    "Set the font used for displaying the error if evaluating the script fails" : u"Изменить шрифт, для отображения ошибки в окне видеопросмотра при сбое выполнения скрипта",
    "User Sliders" : u"Пользовательские ползунки",
    "Hide slider window by default" : u"Скрывать окно ползунков по умолчанию",
    "Keep the slider window hidden by default when previewing a video" : u"Скрывать окна ползунков по умолчанию при просмотре видео", # New in v2.2.1
    "Create user sliders automatically" : u"Автоматически создавать пользовательские ползунки",
    "Create user sliders automatically using the filter database" : u"Автоматически создавать пользовательские ползунки с помощью базы данных фильтров",
    "Create user sliders for int and float arguments" : u"Создавать пользовательские ползунки для аргументов типа int и float",
    "type int/float (numerical slider)" : u"тип int/float (числовой ползунок)",
    "Create listboxes for int list arguments" : u"Создавать выпадающие списки для аргументов типа int-списка",
    "type int (list)" : u"тип int (список) ",
    "Create color pickers for hex color arguments" : u"Создавать палитры цветов для цветовых аргументов в шестнадцатеричной кодировке",
    "type int (hex color)" : u"тип int (цвет в шестнадцатеричной кодировке)", # New in v2.2.1
    "Create radio boxes for bool arguments" : u"Создавать радиокнопки для аргументов типа bool", # New in v2.2.1
    "type bool" : u"тип bool", # New in v2.2.1
    "Create listboxes for string list arguments" : u"Создавать выпадающие списки для аргументов типа string", # New in v2.2.1
    "type string (list)" : u"тип string (список)", # New in v2.2.1
    "Create filename pickers for string filename arguments" : u"Создавать поле имени файла для строковых аргументов имени файла", # New in v2.2.1
    "type string (filename)" : u"тип string (имя файла)", # New in v2.2.1
    "Create placeholders for arguments which have no database information" : u"Создавать поле для аргументов, для которых отсутствует информация в базе данных", # New in v2.2.1
    "undocumented" : u"недокументированный", # New in v2.2.1
    "Disable refresh as default" : u"Отключить обновление по умолчанию", # New in v2.6.8.4
    "Do not reinitialize the clip every time a slider is changed. Can be changed in the slider window" : u"Не выполнять повторную инициализацию клипа при каждом смене ползунка. Может быть изменено в поле ползунка", # New in v2.6.8.4
    "Button show/hide applies to all tabs" : u"Действие Показать/Скрыть применяется ко всем вкладкам", # New in v2.6.8.4
    "Or press Ctrl when you click the button." : u"Или удерживайте Ctrl при нажатии кнопки.", # New in v2.6.8.4
    "Hide slider window toggle tag menus*" : u"Скрыть меню тегов в окне ползунка *", # New in v2.6.8.4
    "Hide the toggle tag menus in the context menu of the sliders" : u"Скрывать меню тегов переключения в контекстном меню ползунков", # New in v2.6.8.4
    "Custom colors can be set under 'Options->Font and colors->Advanced 2'\nNot visible slider windows needed refresh." : u"Пользовательские цвета можно задать в разделе 'Параметры -> Шрифты и цвета -> Продвинутые 2'\nНе видимые окна ползунков, которые необходимо обновить.", # New in v2.6.8.4
    "Enable slider window custom color theme" : u"Включить пользовательскую цветовую тему окна ползунка", # New in v2.6.8.4
    "Determines which filters will initially have hidden arguments in the slider window" : u"Укажите, как именно будут выглядеть аргументы фильтра в окне ползунков",
    "Fold all" : u"Сворачивать всё", # New in v2.2.1
    "Fold non-numbers" : u"Сворачивать не числовые ползунки", # New in v2.2.1
    "Fold none" : u"Не сворачивать",
    "Fold or restore last status" : u"Свернуть или восстановить последнее состояние", # New in v2.6.8.4
    "Fold startup setting" : u"Сворачивание аргументов фильтра при скрытии окна ползунков", # New in v2.2.1
    "Filter exclusion list:" : u"Фильтр списка исключений", # New in v2.2.1
    "Specify filters never to build automatic sliders for. Use a space as separator.\nYou can toggle it in the slider context menu." : u"Укажите фильтры, для которых не будут создаваться автоматические ползунки. Используйте пробел в качестве разделителя.\nВы можете переключать его в контекстном меню ползунка.", # New in v2.6.8.4
    "Save/Load" : u"Сохранить/Загрузить", # New in v2.2.1
    "Automatically save the session on shutdown and load on next startup" : u"Автоматически сохранять сеанс при закрытии и загружать его при следующем запуске",
    "Save session for next launch" : u"Сохранять сеанс для следующего запуска",
    "Always load startup session" : u"Всегда загружать сеанс запуска", 
    "Always load the auto-saved session before opening any other file on startup" : u"При запуске программы всегда загружать автосохраненный сеанс перед открытием любого другого файла", 
    "Always hide the video preview window when loading a session" : u"Всегда скрывать окно предварительного просмотра видео при загрузке сеанса", # New in v2.2.1
    "Don't preview when loading a session" : u"Не показывать видеопросмотр при загрузке сеанса", # New in v2.2.1
    "Backup session periodically (minutes)" : u"Период создания резервной копии (в минутах)", # New in v2.3.0
    "Backup the session every X minutes, if X > 0" : u"Создавать резервную копию сеанса каждые X минут, если X > 0", # New in v2.3.0
    "Backup session when previewing" : u"Создавать резервную копию при предпросмотре видео", # New in v2.2.1
    "If checked, the current session is backed up prior to previewing any new script" : u"Если отмечено, то текущий сеанс сохраняется перед предпросмотром видео любого скрипта",
    "Prompt to save a script before previewing (inactive if previewing with unsaved changes)" : u"Предлагать сохранить скрипт перед предпросмотром видео (неактивно при предпросмотре с не сохраненными изменениями)", 
    "Prompt to save when previewing" : u"Предлагать сохранить перед предпросмотром видео", 
    "Create a temporary preview script with unsaved changes when previewing the video" : u"Создавать временный скрипт с несохранёнными изменениями при предпросмотре видео.", 
    "Preview scripts with unsaved changes" : u"Предпросмотр скриптов с несохранёнными изменениями", # New in v2.2.1
    "When closing a tab, don't prompt to save the script if it doesn't already exist on the filesystem" : u"При закрытии вкладки не предлагать сохранить скрипт, если он еще не существует в виде отдельного файла", # New in v2.3.0
    "When closing tab, don't prompt to save scripts without file" : u"При закрытии вкладки не предлагать сохранять скрипты без файла", # New in v2.5.1.09
    "Prompt to save each script with unsaved changes when exiting the program" : u"Предлагать сохранить каждый скрипт с несохраненными изменениями при выходе из программы",
    "Prompt to save scripts on program exit" : u"Предлагать сохранять скрипты при выходе",
    "Only with existing script" : u"Только с существующим скриптом",
    "When exiting the program, don't prompt to save the script if it doesn't already exist on the filesystem" : u"При выходе из программы не предлагать сохранять скрипт, если он еще не существует в виде отдельного файла",
    "Auto: CRLF on Windows and LF on *nix for new scripts, existing scripts keep their current line endings" : u"Авто: CRLF в Windows и LF в *nix для новых скриптов, в существующих скриптах сохраняются текущие окончания строк.", # New in v2.5.1
    "Force CRLF" : u"Принудительно CRLF", # New in v2.5.1
    "Force LF" : u"Принудительно LF", # New in v2.5.1
    "Line endings" : u"Окончания строк", # New in v2.5.1
    "Auto" : u"Авто", # New in v2.5.1
    "Save and read AvsPmod-specific markings (user sliders, toggle tags, etc) as a commented section in the *.avs file" : u"Сохранение и чтение специфичных отметок AvsPmod (пользовательских ползунков, тегов переключения и т.п.) в виде комментария в файле avs",
    "Save or read avs scripts with AvsPmod markings" : u"Сохранение или чтение скриптов avs со спец. отметками AvsPmod", # New in v2.6.8.4
    "Do not remove toggle tags and disabled filters.\nCan make the saved script unreadable for other programs if You not use #> in front of the toggle tag: #>[sharp=0]" : u"Не удаляйте теги переключения и отключенные фильтры.\nЭто может сделать сохраненный скрипт нечитаемым в других программах, если Вы не используете #> перед тегом переключения: #>[sharp=0]", # New in v2.6.8.4
    "Save toggle tags within the script ( read the hint! )" : u"Сохранять теги переключения в скрипте (прочтите подсказку!)", # New in v2.6.8.4
    "Start dialogs on the last used directory" : u"Открывать диалоговые окна на последнем использованном каталоге",
    "If unchecked, the script's directory is used" : u"Если не отмечено, то используется каталог скрипта",
    "Start save image dialogs on the last used directory" : u"Открывать диалоговое окно сохранения изображения на последнем использованном каталоге",
    "Choose a default pattern for image filenames. %s -> script title, %06d -> frame number padded to six digits" : u"Выберите шаблон по умолчанию для имен файлов изображений. %s - заголовок скрипта, %06d - номер кадра до шести цифр", # New in v2.5.0
    "Default image filename pattern" : u"Шаблон имени файла изображения по умолчанию", # New in v2.5.0
    "Ask for JPEG quality" : u"Показать настройки качества JPEG", # New in v2.5.0
    "When saving a JPEG image, prompt for the quality level. Use the value from the last time if not checked" : u"При сохранении изображения в формат JPEG показать настройки качества. Если не отмечено, используется значение при последнем разе использования", # New in v2.5.0
    "Misc" : u"Разное", 
    "Choose the language used for the interface" : u"Выберите язык интерфейса",
    "Language" : u"Язык",
    "Show keyboard images in the script tabs when video has focus" : u"Показывать значки клавиш (цифры) на вкладках скриптов, когда окно видеопросмотра находится в фокусе",
    "Use keyboard images in tabs" : u"Используйте значки горячих клавиш на вкладках",
    "Show tabs in multiline style" : u"Показывать вкладки в несколько рядов",
    "There can be several rows of tabs" : u"Вкладки могут располагаться в несколько рядов",
    "All tabs will have same width" : u"Все вкладки одинаковой ширины",
    "Show tabs in fixed width" : u"Показывать все вкладки с фиксированной шириной",
    "Invert scroll wheel direction (Tabs, Zoom)" : u"Инвертировать направление прокрутки колёсика (вкладки, масштабирование)",
    "Scroll the mouse wheel up for changing tabs to the right" : u"Прокрутите колёсико мыши вверх, чтобы перейти на вкладку справа",
    "Invert scroll wheel direction (Frame)" : u"Инвертировать направление прокрутки колёсика (смена кадра)",
    "Invert wheel direction for frames step" : u"Инвертировать направление прокрутки колёсика для смены кадров",
    "Automatically load bookmarks from script" : u"Автоматически загружать закладки из скрипта",
    "Load bookmarks from script" : u"Загружать закладки из скрипта",
    "Automatically load bookmarks from script or tab if tab changed" : u"Автоматически загружать закладки из скрипта или метки, если вкладка изменилась",
    "Tab change loads bookmarks from script or tab *" : u"При смена вкладки загружать из скрипта закладки или метки *", # New in v2.6.5.1
    "Warn if tab bookmarks and from script reading bookmarks different." : u"Предупреждать, если в вкладке и в скрипте отличаются закладки", # New in v2.6.5.1
    "Warning tab bookmarks different" : u"Предупреждать о разных закладках", # New in v2.6.5.1
    "Only allow a single instance of AvsPmod" : u"Разрешить одновременный запуск нескольких копий AvsPmod",
    "Show warning at startup if there are dlls with bad naming in default plugin folder" : u"Показывать предупреждение при запуске, если в папке плагинов по умолчанию есть библиотеки с неправильным именем",
    "Show warning for bad plugin naming at startup" : u"Показывать предупреждение о неправильном имени плагина при запуске",
    "Bookmark jump" : u"Переход на закладку", # New in v2.6.5.1
    "Custom jump" : u"Пользовательский переход", # New in v2.6.5.1
    "Mouse browse buttons" : u"Обзор кнопками мышки", # New in v2.6.5.1
    "Mouse browse buttons (forward/backward) on video and script window\nIf 'Tab change' and tab count less than 2, 'Bookmark jump' is used\nIf 'Tab change' press CTRL or left mouse and 'Bookmark jump' is used\nIf 'Bookmark jump', vice versa" : u"Обзор с помощью кнопок мышки (вперед/назад) в окне видео и скрипта\nЕсли 'Смена вкладки' и количество вкладок меньше 2, используется 'Переход по закладкам'\nЕсли 'Смена вкладки', то удерживайте CTRL или левую кнопку мыши для 'Переход по закладкам'\nЕсли 'Закладка меняется', наоборот.", # New in v2.6.5.1
    "Middle mouse button behavior on the script, if script empty open source is used" : u"Действие средней кнопки мышки в окне скрипт, если используется пустой скрипт с открытым исходным кодом",
    "Middle mouse on script" : u"Средняя кнопка мышки в оке скрипта",
    "Open source" : u"Открыть источник",
    "Show video frame" : u"Показать видео кадр",
    "Max number of recent filenames" : u"Макс. число последних файлов", 
    "This number determines how many filenames to store in the recent files menu" : u"Это число задаёт количество отображаемых в меню последних открытых файлов", 
    "Custom jump size:" : u"Пользовательская величина перехода:",
    "Jump size used in video menu" : u"Величина перехода используемая в меню видео",
    "Custom jump size units" : u"Единица для пользовательского перехода",
    "Units of custom jump size" : u"Пользовательская единица измерения величины для перехода по кадрам",
    "hours" : u"часы",
    "minutes" : u"минуты",
    "seconds" : u"секунды",
    "frames" : u"кадры",
    "Misc 2" : u"Разное 2", # New in v2.6.5.2
    "AvsPmod DPI scaling *" : u"Масштабирование DPI в AvsPmod *", # New in v2.6.6.0
    "DPI scaling overall only manually*" : u"Масштабировать DPI только вручную *", # New in v2.6.5.3
    "Do not do overall DPI scaling automatically" : u"Не выполнять автоматическое масштабирование DPI",
    "Disable DPI awareness*" : u"Отключить распознавание DPI *", # New in v2.6.5.3
    "Only disable it if you using 100% system zoom. Program is zoomed by the system and set DPI values." : u"Отключите его, только если вы используете 100% системный масштаб. Программа масштабируется системой и устанавливает значения DPI.", # New in v2.6.8.4
    "DPI scaling overall:*" : u"Общий масштаб DPI: *",
    "Manually adjust dpi scaling overall (10 % steps). For 150 % DPI set value 5" : u"Вручную отрегулируйте масштабирование DPI в целом (с шагом 10%). Для 150% DPI установите значение 5", # New in v2.6.8.4
    "Additional adjust the video controls (10 % steps)" : u"Дополнительная настройка элементов управления видео (шаг 10%)", # New in v2.6.5.3
    "DPI scaling video controls:*" : u"Масштаб DPI элементов управления видео: *", # New in v2.6.5.3
    "Additional adjust the script window tabs (10 % steps)" : u"Дополнительная настройка вкладок окна скрипта (шаг 10%)",
    "DPI scaling main tabs:*" : u"Масштаб DPI основных вкладок: *",
    "Additional adjust the statusbar (10 % steps)" : u"Дополнительная настройка строки состояния (шаг 10%)", # New in v2.6.5.3
    "DPI scaling statusbar:*" : u"Масштаб DPI строки состояния",
    "Advanced settings" : u"Продвинутые настройки", # New in v2.6.8.4
    "After creating a new clip, show available memory in the status bar if memory is less than x MB" : u"После создания/обновления предпросмотра видео показать в строке состояния доступную системную память, если она меньше x МБ", # New in v2.6.8.4
    "Show available system memory (0 disabled)" : u"Показать доступную системную память (0 отключено)", # New in v2.6.8.4
    "Add tab to group" : u"Добавить вкладку в группу", # New in v2.5.0
    "Extend selection to line down position" : u"Расширить выделение до нижней строки", # New in v2.2.1
    "Scroll down" : u"Прокрутить вниз", # New in v2.2.1
    "Extend rectangular selection to line down position" : u"Расширить прямоугольное выделение до нижней строки", # New in v2.2.1
    "Extend selection to line up position" : u"Расширить выделение до верхней строки", # New in v2.2.1
    "Scroll up" : u"Прокрутить вверх", # New in v2.2.1
    "Extend rectangular selection to line up position" : u"Расширить прямоугольное выделение до верхней строки", # New in v2.2.1
    "Go to previous paragraph" : u"Перейти к предыдущему абзацу", # New in v2.2.1
    "Extend selection to previous paragraph" : u"Расширить выделение до предыдущего абзаца", # New in v2.2.1
    "Go to next paragraph" : u"Перейти к следующему абзацу", # New in v2.2.1
    "Extend selection to next paragraph" : u"Расширить выделение до следующего абзаца", # New in v2.2.1
    "Extend selection to previous character" : u"Расширить выделение до предыдущего символа", # New in v2.2.1
    "Go to previous word" : u"Перейти к предыдущему слову", # New in v2.2.1
    "Extend selection to previous word" : u"Расширить выделение до предыдущего слова", # New in v2.2.1
    "Extend rectangular selection to previous character" : u"Расширить прямоугольное выделение до предыдущего символа", # New in v2.2.1
    "Extend selection to next character" : u"Расширить выделение до следующего символа", # New in v2.2.1
    "Go to next word" : u"Перейти к следующему слову", # New in v2.2.1
    "Extend selection to next word" : u"Расширить выделение до следующего слова", # New in v2.2.1
    "Extend rectangular selection to next character" : u"Расширить прямоугольное выделение до следующего символа", # New in v2.2.1
    "Go to previous word part" : u"Перейти к предыдущей части слова", # New in v2.2.1
    "Extend selection to previous word part" : u"Расширить выделение до предыдущей части слова", # New in v2.2.1
    "Go to next word part" : u"Перейти к следующей части слова", # New in v2.2.1
    "Extend selection to next word part" : u"Расширить выделение до следующей части слова", # New in v2.2.1
    "Extend selection to start of line" : u"Расширить выделение до начала строки", # New in v2.2.1
    "Go to start of document" : u"Перейти в начало документа", # New in v2.2.1
    "Extend selection to start of document" : u"Расширить выделение до начала документа", # New in v2.2.1
    "Go to start of line" : u"Перейти в начало строки", # New in v2.2.1
    "Extend selection to end of line" : u"Расширить выделение до конца строки", # New in v2.2.1
    "Go to end of document" : u"Перейти в конец документа", # New in v2.2.1
    "Extend selection to end of document" : u"Расширить выделение до конца документа", # New in v2.2.1
    "Go to end of line" : u"Перейти в конец строки", # New in v2.2.1
    "Extend selection to previous page" : u"Расширить выделение на предыдущую страницу", # New in v2.2.1
    "Extend rectangular selection to previous page" : u"Расширить прямоугольное выделение до предыдущей страницы", # New in v2.2.1
    "Extend selection to next page" : u"Расширить выделение до следующей страницы", # New in v2.2.1
    "Extend rectangular selection to next page" : u"Расширить прямоугольное выделение до следующей страницы", # New in v2.2.1
    "Delete to end of word" : u"Удалить до конца слова", # New in v2.2.1
    "Delete to end of line" : u"Удалить до конца строки", # New in v2.2.1
    "Delete back" : u"Удалить обратно", # New in v2.2.1
    "Delete to start of word" : u"Удалить до начала слова", # New in v2.2.1
    "Delete to start of line" : u"Удалить до начала строки", # New in v2.2.1
    "Cancel autocomplete or calltip" : u"Отменить автозавершение или подсказку", # New in v2.2.1
    "Indent selection" : u"Вставить отступ",
    "Unindent selection" : u"Убрать отступ",
    "Newline" : u"Новая строка", # New in v2.2.1
    "Zoom in" : u"Увеличить масштаб", # New in v2.2.1
    "Zoom out" : u"Уменьшить масштаб", # New in v2.2.1
    "Reset zoom level to normal" : u"Сбросить масштаб до нормального", # New in v2.2.1
    "Line cut" : u"Вырезать строку", # New in v2.2.1
    "Line delete" : u"Удалить строку", # New in v2.2.1
    "Line copy" : u"Копировать строку", # New in v2.2.1
    "Transpose line with the previous" : u"Перенести строку с предыдущей", # New in v2.2.1
    "Line or selection duplicate" : u"Дублировать строку или выделение", # New in v2.2.1
    "Convert selection to lowercase" : u"Преобразовать выделение в нижний регистр", # New in v2.2.1
    "Convert selection to uppercase" : u"Преобразовать выделение в верхний регистр", # New in v2.2.1
    "Sort bookmarks ascending" : u"Сортировать закладки по возрастанию", # New in v2.2.1
    "sort ascending" : u"сортировать по возрастанию", # New in v2.2.1
    "Show bookmarks with timecode" : u"Показывать закладки с временными метками", # New in v2.2.1
    "show time" : u"показать время", # New in v2.2.1
    "Show bookmarks with title" : u"Показывать закладки с заголовком", # New in v2.2.1
    "show title" : u"показать заголовок", # New in v2.2.1
    "Resolution-based" : u"На основе разрешения", # New in v2.3.0
    "BT.709" : u"", # New in v2.3.0
    "BT.601" : u"", # New in v2.3.0
    "TV levels" : u"TV уровни", # New in v2.3.0
    "PC levels" : u"PC уровни", # New in v2.3.0
    "Progressive" : u"Прогрессивный", # New in v2.2.1
    "Interlaced" : u"Чересстрочный", # New in v2.2.1
    "Swap UV" : u"Поменять местами U V", # New in v2.2.1
    "25%" : u"", # New in v1.3.8
    "50%" : u"", # New in v1.3.8
    "100% (normal)" : u"100% (нормальный)", # New in v1.3.8
    "200%" : u"", # New in v1.3.8
    "300%" : u"", # New in v1.3.8
    "400%" : u"", # New in v1.3.8
    "Fill window" : u"Заполнить окно",
    "Fit inside window" : u"Подогнать внутрь окна",
    "Vertically" : u"Вертикально",
    "Horizontally" : u"Горизонтально",
    "Black" : u"Черный",
    "Dark grey" : u"Темносерый",
    "Medium grey" : u"Серый",
    "Light grey" : u"Светлосерый",
    "White" : u"Белый",
    "&File" : u"&Файл",
    "Create a new tab" : u"Создать новую вкладку",
    "New tab" : u"Новая вкладка",
    "Open an existing script" : u"Открыть существующий скрипт",
    "Open..." : u"Открыть...",
    "Reopen the last closed tab" : u"Открыть последнюю закрытую вкладку", # New in v2.4.0
    "Undo close tab" : u"Отменить закрытие вкладки",
    "Close tab" : u"Закрыть вкладку",
    "Close the current tab" : u"Закрыть текущую вкладку",
    "Close all tabs" : u"Закрыть все вкладки",
    "Close every tab" : u"Закрыть каждую вкладку", # New in v2.2.1
    "Rename tab" : u"Переименовать вкладку",
    "Rename the current tab. If script file is existing, also rename it" : u"Переименовать текущую вкладку. Если файл скрипта существует, то переименовать и его",
    "Save the current script" : u"Сохранить текущий скрипт",
    "Choose where to save the current script" : u"Выбрать где сохранить текущий скрипт",
    "Save script as..." : u"Сохранить скрипт как...",
    "Reload script" : u"Перезагрузить скрипт",
    "Reopen the current script file if it has changed" : u"Повторно открыть текущий файл скрипта, если он изменился",
    "If the current script is saved to a file, open its directory" : u"Если текущий скрипт сохранен в файле, то открыть его каталог",
    "Open script's directory" : u"Открыть каталог скрипта",
    "Save the current script as a HTML document" : u"Сохранить текущий скрипт как HTML документ.",
    "Export HTML" : u"Экспорт в HTML", # New in v2.5.0
    "&Print script" : u"&Распечатать скрипт", # New in v2.3.1
    "Configure page for printing" : u"Настройка печатаемой страницы", # New in v2.3.1
    "Page setup" : u"Настройка страницы", # New in v2.3.1
    "Include the script filename and page number at the top of each page" : u"Указывать имя файла скрипта и номер страницы вверху каждой печатаемой страницы.", # New in v2.3.1
    "Print header" : u"Печать заголовка", # New in v2.3.1
    "Word-wrap long lines" : u"Перенос длинных строк", # New in v2.3.1
    "Apply the current zoom to the output" : u"Применить текущий масштаб к печатаемому скрипту", # New in v2.3.1
    "Use zoom" : u"Использовать масштабирование", # New in v2.3.1
    "Display print preview" : u"Показать предпросмотр печати", # New in v2.3.1
    "Print preview" : u"Предпросмотр печати", # New in v2.3.1
    "&Print" : u"Распечатать", # New in v2.3.1
    "Print to printer or file" : u"Распечатать на принтере или в файл", # New in v2.3.1
    "Load a session into the tabs" : u"Загрузить сеанс в вкладки",
    "Load session..." : u"Загрузить сеанс...",
    "Save all the scripts as a session, including slider info" : u"Сохранить все скрипты как сеанс, включая информацию ползунков",
    "Save session..." : u"Сохранить сеанс...",
    "Backup current session" : u"Резервное копирование текущего сеанса",
    "Backup the current session for next program run" : u"Резервное копирование текущего сеанса для следующего запуска программы",
    "Next tab" : u"Следующая вкладка",
    "Switch to next script tab" : u"Перейти на следующую вкладку со скриптом",
    "Previous tab" : u"Предыдущая вкладка",
    "Switch to previous script tab" : u"Перейти на предыдущую вкладку со скриптом",
    "Show the scrap window" : u"Показать/Скрыть окно заметок",
    "&Exit" : u"&Выход",
    "Exit the program" : u"Выйти из программы",
    "&Edit" : u"&Правка",
    "Undo last text operation" : u"Отменить последнюю операцию с текстом",
    "Redo last text operation" : u"Повторить последнюю операцию с текстом",
    "Cut the selected text" : u"Вырезать выбранный текст",
    "Copy the selected text" : u"Копировать выбранный текст",
    "Paste the selected text" : u"Вставить выбранный текст",
    "Open a find text dialog box" : u"Открыть диалоговое окно поиска текста",
    "Find..." : u"Найти...",
    "Find next" : u"Найти далее",
    "Find the next instance of given text" : u"Найти следующий образец заданного текста",
    "Find previous" : u"Найти предыдущий", # New in v2.4.0
    "Find the previous instance of given text" : u"Найти предыдущий образец заданного текста", # New in v2.4.0
    "Open a replace text dialog box" : u"Открыть диалоговое окно замены текста",
    "Replace..." : u"Заменить...",
    "Replace next" : u"Заменить далее", # New in v2.4.0
    "Replace the next instance of given text" : u"Заменить следующий образец заданного текста", # New in v2.4.0
    "Select All" : u"Выбрать всё",
    "Select all the text" : u"Выбрать весь текст",
    "&Insert" : u"&Вставить", # New in v2.2.1
    "Expand a snippet tag, or select a snippet from the list" : u"Развернуть тег отрывка или выбрать отрывок из списка", # New in v2.5.0
    "Insert snippet" : u"Вставить отрывок", # New in v2.5.0
    "Choose a source file to insert into the text" : u"Выберите исходный файл для вставки в текст",
    "Insert source..." : u"Вставить источник...",
    "Get a filename from a dialog box to insert into the text" : u"Получить имя файла из диалогового окна для вставки в текст",
    "Insert filename..." : u"Вставить имя файла...",
    "Choose a plugin file to insert into the text" : u"Выберите файл плагина для вставки в текст", # New in v2.4.0
    "Insert plugin..." : u"Вставить плагин...",
    "Insert a user-scripted slider into the text" : u"Вставка пользовательского ползунка в текст",
    "Insert user slider..." : u"Вставить пользовательский ползунок...",
    "Insert a tag which indicates a separator in the user slider window" : u"Вставить метку, обозначающую разделитель, в пользовательское окно ползунка",
    "Insert user slider separator" : u"Вставить разделитель пользовательского ползунка",
    "Insert the current frame number into the text" : u"Вставить номер текущего кадра в текст",
    "Add tags surrounding the selected text for toggling with the video preview" : u"Добавить метки вокруг выделенного текста для переключения с предпросмотром видео",
    "Tag selection for toggling..." : u"Выбор метки для переключения...", # New in v2.6.8.4
    "Clear all tags" : u"Убрать все метки",
    "Clear all toggle tags from the text" : u"Убрать все метки переключения из текста",
    "Add Preview filter surrounding the selected lines" : u"Добавить фильтр предпросмотра вокруг выбранных строк", # New in v2.6.8.4
    "Preview filter" : u"Предпросмотр фильтра", # New in v2.6.6.0
    "Indent the selected lines" : u"Увеличить отступ выбранных строк",
    "Unindent the selected lines" : u"Уменьшить отступ выбранных строк",
    "Block comment" : u"Закомментировать строку",
    "Comment or uncomment selected lines" : u"Закомментировать или раскомментировать выбранные строки",
    "Comment at start of a text style or uncomment" : u"Комментирование или раскомментирование в начале слова", # New in v2.2.1
    "Style comment" : u"Закомментировать от курсора", # New in v2.2.1
    "Toggle current fold" : u"Свернуть/Развернуть текущий блок", # New in v2.2.1
    "Toggle the fold point On/OFF at the current line" : u"Свернуть/Развернуть блок скрипта на текущей строке", # New in v2.2.1
    "Toggle all fold points On/OFF" : u"Свернуть/Развернуть все блоки в скрипте", # New in v2.2.1
    "Toggle all folds" : u"Свернуть/Развернуть все блоки", # New in v2.2.1
    "Toggle text wrap" : u"Включить/Отключить перенос строк",
    "Toggle text wrap On/OFF" : u"Включить/выключить перенос текста",
    "&AviSynth function" : u"&Функции AviSynth", # New in v2.2.1
    "Show list of filternames matching the partial text at the cursor" : u"Показать список фильтров, соответствующих части текста под курсором",
    "Autocomplete all" : u"Автозавершить все", # New in v2.2.1
    "Disregard user's setting, show full list of filternames matching the partial text at the cursor" : u"Игнорировать настройки пользователя, показывать полный список фильтров, соответствующих частичному тексту под курсором", # New in v2.2.1
    "Autocomplete parameter/filename" : u"Автозавершить параметр / имя файла", # New in v2.5.0
    "If the first characters typed match a parameter name, complete it. If they're typed on a string, complete the filename" : u"Если первые набранные символы соответствуют имени параметра, то заполнить его. Если они набраны в строке, то заполнить именем файла", # New in v2.5.0
    "Show calltip" : u"Показать подсказку", 
    "Show the calltip for the filter (only works if cursor within the arguments)" : u"Показать подсказку по фильтру (работает только если курсор над аргументами функции)", 
    "Show function definition" : u"Показать определение функции",
    "Show the AviSynth function definition dialog for the filter" : u"Для фильтра показать диалог определения функции AviSynth",
    "Filter help file" : u"Файл справки по фильтру", 
    "Run the help file for the filter (only works if cursor within the arguments or name is highlighted)" : u"Показать файл справки по фильтру (работает только если курсор над аргументами или имя подсвечено)", 
    "Include functions defined in the current script in the filter database, only for this tab" : u"Включить функции, определенные в текущем скрипте, в базу данных фильтров, только для текущей вкладки", # New in v2.5.1
    "Parse script for function definitions" : u"Проанализировать скрипт для определений функций", # New in v2.5.1
    "&Miscellaneous" : u"&Разное", # New in v2.2.1
    "Move line up" : u"Передвинуть строку вверх", 
    "Move the current line or selection up by one line" : u"Передвинуть текущую строку или выбранное на одну строку вверх", 
    "Move line down" : u"Передвинуть строку вниз", 
    "Move the current line or selection down by one line" : u"Передвинуть текущую строку или выбранное на одну строку вниз", 
    "Copy the current script without any AvsP markings (user-sliders, toggle tags) to the clipboard" : u"Копировать в буфер обмена текущий скрипт без спец. отметок AvsP (ползунков, меток)", 
    "Copy unmarked script to clipboard" : u"Копировать неразмеченный скрипт в буфер обмена", 
    "Copy avisynth error to clipboard" : u"Скопируйте ошибку AviSynth в буфер обмена", # New in v2.2.1
    "Copy the avisynth error message shown on the preview window to the clipboard" : u"Копировать в буфер обмена сообщение об ошибке AviSynth, отображаемое в окне предпросмотра видео", # New in v2.2.1
    "&Video" : u"&Видео",
    "Bookmarks" : u"Закладки",
    "Bookmarks to script" : u"Закладки в скрипт",
    "Bookmarks from script" : u"Закладки из скрипта",
    "Add/Remove bookmark" : u"Добавить/Удалить закладку",
    "Mark the current frame on the frame slider" : u"Отметить текущий кадр на ползунке кадров",
    "Clear tab bookmarks" : u"Очистить вкладку от закладок",
    "Clears the current tab bookmarks" : u"Удаляет текущую вкладку от закладок",
    "Clear all bookmarks Globally" : u"Очистить все закладки, глобально", # New in v2.6.5.1
    "Clears all bookmarks, clears also all tab bookmarks" : u"Очистить все закладки, также очищает все вкладки от закладок", # New in v2.6.5.1
    "Titled &bookmarks" : u"Заглавия &закладки", # New in v2.2.1
    "Move the nearest titled bookmark to the current position. A historic title will be restored if it matches the condition." : u"Переместите ближайшую озаглавленную закладку в текущее положение. Изначальное заглавие будет восстановлено, если оно соответствует условию.", # New in v2.2.1
    "Move titled bookmark" : u"Переместить озаглавленную закладку", # New in v2.2.1
    "Restore all historic titles" : u"Восстановить все первоначальные заглавия", # New in v2.2.1
    "Restore historic titles" : u"Восстановить первоначальные заглавия", # New in v2.2.1
    "Clear all historic titles" : u"Очистить все первоначальные заглавия", # New in v2.2.1
    "Clear historic titles" : u"Очистить первоначальные заглавия", # New in v2.2.1
    "Generate titles for untitled bookmarks by the pattern - 'Chapter %02d'" : u"Генерировать заглавия для безымянных закладок по шаблону - 'Chapter %02d'", # New in v2.2.1
    "Set title (auto)" : u"Озаглавить (авто)", # New in v2.2.1
    "Edit title for bookmarks in a list table" : u"Редактировать список заглавий закладок", # New in v2.2.1
    "Set title (manual)" : u"Озаглавить (вручную)", # New in v2.2.1
    "Remove all title" : u"Удалить все заглавия", # New in v2.6.5.1
    "Remove all title from the bookmarks" : u"Удалить все заглавия из закладок", # New in v2.6.5.1
    "Not include this tab on any group" : u"Не включать эту вкладку ни в одну группу", # New in v2.5.0
    "Add tab to this group" : u"Добавить вкладку в эту группу", # New in v2.5.0
    "Clear current tab group" : u"Очистить текущую группу вкладок", # New in v2.5.0
    "Clear all tab groups" : u"Очистить все группы вкладок", # New in v2.5.0
    "Apply offsets" : u"Применить смещение", # New in v2.5.0
    "Use the difference between showed frames when the tabs were added to the group as offsets" : u"Использовать разницу между показанными кадрами, когда вкладки были добавлены в группу как смещённые", # New in v2.5.0
    "Offset also bookmarks" : u"Также смещать закладки", # New in v2.5.1
    "Apply the offset also to the currently set bookmarks" : u"Также применять смещение к текущим установленным закладкам", # New in v2.5.1
    "&Navigate" : u"&Навигация по видео", # New in v2.2.1
    "Go to next bookmarked frame" : u"Перейти к следующему кадру с закладкой",
    "Next bookmark" : u"Следующая закладка",
    "Go to previous bookmarked frame" : u"Перейти к предыдущему кадру с закладкой",
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
    "Go to first frame" : u"Перейти к первому кадру",
    "Go to first video frame (keyboard shortcut active when video window focused)" : u"Перейти к первому кадру (сочетание клавиш активно, если видео в фокусе)",
    "Go to last frame" : u"Перейти к последнему кадру",
    "Go to last video frame (keyboard shortcut active when video window focused)" : u"Перейти к последнему кадру (сочетание клавиш активно, если видео в фокусе)",
    "Go to last scrolled frame" : u"Перейти к последнему прокрученному кадру",
    "Last scrolled frame" : u"Последний прокрученный кадр",
    "Enter a video frame or time to jump to" : u"Введите номер видео кадра или время для перемещения",
    "Go to frame..." : u"Перейти к кадру...",
    "&Play video" : u"&Проиграть видео", # New in v2.4.0
    "Play/pause video" : u"Проигрывать/приостановить видео", # New in v2.4.0
    "Double the current playback speed" : u"Удвоить текущую скорость проигрывания",
    "Increment speed" : u"Ускорить проигрывание", # New in v2.4.0
    "Decrement speed" : u"Замедлить проигрывание", # New in v2.4.0
    "Halve the current playback speed" : u"Уменьшить вдвое текущую скорость проигрывания", # New in v2.5.0
    "Set the playback speed to the script frame rate" : u"Установите скорость проигрывания в соответствии с частотой кадров скрипта", # New in v2.4.0
    "Normal speed" : u"Нормальная скорость", # New in v2.4.0
    "Play the video as fast as possible without dropping frames" : u"Проигрывать видео как можно быстрее без потери кадров", # New in v2.4.0
    "Maximum speed" : u"Максимальная скорость", # New in v2.4.0
    "Loop playback for trim editor selections or at the end of the clip" : u"Циклическое проигрывание для выбора редактора обрезки или в конце клипа", # New in v2.6.8.4
    "Play loop" : u"Зациклить проигрывание",
    "Use a separate thread for playback. If avisynth threads used, playback uses also threads" : u"Использовать отдельный поток для проигрывания. Если используются многопоточность AviSynth, то при проигрывании так-же используется многопоточность", # New in v2.6.8.4
    "Use separate thread" : u"Использовать отдельный поток", # New in v2.6.8.4
    "Crop editor..." : u"Редактор кадрирования...",
    "Show the crop editor dialog" : u"Показать диалоговое окно редактора кадрирования",
    "&Trim selection editor" : u"Редактор покадровой нарезки",
    "Show the trim selection editor dialog" : u"Показать диалоговое окно редактора выборки кадров",
    "Show trim selection editor" : u"Показать редактор покадровой нарезки",
    "Set a selection startpoint (shows the trim editor if not visible)" : u"Установить начальную точку (показывает редактор нарезки, если скрыт)",
    "Set selection startpoint" : u"Установить начальную точку",
    "Set a selection endpoint (shows the trim editor if not visible)" : u"Установить конечную точку (показывает редактор нарезки, если скрыт)",
    "Set selection endpoint" : u"Установить конечную точку",
    "Move selections before the current frame" : u"Переместить выделение перед текущим кадром",
    "The current selections are cut from the timeline and inserted before the current frame. Bookmarks are shifted accordingly." : u"Текущие выделения вырезаются из шкалы времени и вставляются перед текущим кадром. Закладки соответственно смещаются.",
    "Move selections after the current frame" : u"Переместить выделение после текущего кадра",
    "The current selections are cut from the timeline and inserted after the current frame. Bookmarks are shifted accordingly." : u"Текущие выделения вырезаются из временной шкалы и вставляются после текущего кадра. Закладки соответственно смещаются.",
    "Add bookmark to trim intersections" : u"Добавить закладки для обрезки пересечений", # New in v2.6.5.1
    "Mark trim points" : u"Отметьте точки обрезки",
    "Save the selections into the script" : u"Сохранить выделенное в скрипте",
    "Selections to script" : u"Выбрать в скрипте",
    "Read the selections from the script" : u"Прочитайте выбранные параметры из скрипта",
    "Selections from script" : u"Выбрать из скрипта",
    "Clear tab selections" : u"Очистить выбранные вкладки",
    "Clear tab trim editor selections (hide the trim editor if visible)" : u"Очистить выбранные вкладки в редакторе обрезки (скрыть редактор обрезки, если он виден)", # New in v2.6.5.1
    "Clear all selections Globally" : u"Очистить всё выбранное, глобально", # New in v2.6.5.1
    "Clear all the tab trim editor selections (hide the trim editor if visible)" : u"Очистить все выбранные вкладки в редакторе обрезки (скрыть редактор обрезки, если он виден)", # New in v2.6.5.1
    "Timeline range" : u"Диапазон временной шкалы", # New in v2.6.8.4
    "Zoom video preview to 25%" : u"Масштабировать предпросмотр видео до 25%", 
    "Zoom video preview to 50%" : u"Масштабировать предпросмотр видео до 50%", 
    "Zoom video preview to 100% (normal)" : u"Масштабировать предпросмотр видео до 100% (нормальный)",
    "Zoom video preview to 200%" : u"Масштабировать предпросмотр видео до 200%",
    "Zoom video preview to 300%" : u"Масштабировать предпросмотр видео до 300%",
    "Zoom video preview to 400%" : u"Масштабировать предпросмотр видео до 400%",
    "Zoom video preview to fill the entire window" : u"Заполнить окно предпросмотра видео",
    "Zoom video preview to fit inside the window" : u"Вписать в размер окна предпросмотр видео",
    "Enlarge preview image to next zoom level. Not work under 'Fill window' or 'Fit inside window'" : u"Увеличить предпросмотр видео до следующего уровня масштабирования. Не работает в режимах 'Заполнить окно' или 'По размеру окна'",
    "Shrink preview image to previous zoom level. Not work under 'Fill window' or 'Fit inside window'" : u"Уменьшить предпросмотр видео до предыдущего уровня масштабирования. Не работает в режимах 'Заполнить окно' или 'По размеру окна'",
    "Antialiasing" : u"Сглаживание",
    "If zoom not 100 %, the preview is drawing antialiased" : u"Если масштаб не 100%, предпросмотр видео отображается со сглаживанием.",
    "&Display" : u"&Отображение", # New in v2.6.8.4
    "&Flip" : u"Повернуть",
    "Flip video preview upside down" : u"Перевернуть предпросмотр видео снизу вверх",
    "Flip video preview from left to right" : u"Перевернуть предпросмотр видео слева направо",
    "&YUV -> RGB" : u"", # New in v2.2.1
    "Swap chroma channels (U and V)" : u"Поменять местами каналы цветности U и V",
    "Get the coefficients from source or script, if the matrix available" : u"Получить коэффициенты из источника или скрипта, если матрица доступна", # New in v2.6.8.4
    "Read from source or script" : u"Считывать из исходного кода или сценария", # New in v2.6.8.4
    "Use BT.709 coefficients for HD, BT.601 for SD" : u"Используйте коэффициенты BT.709 для HD, BT.601 для SD", # New in v2.6.8.4
    "Use BT.709 coefficients" : u"Использовать коэффициент BT.709",
    "Use BT.601 coefficients" : u"Использовать коэффициент BT.601",
    "Use limited range (default)" : u"Использовать ограниченный диапазон яркости и цвета (по умолчанию)",
    "Use full range" : u"Использовать полный диапазон яркости и цвета",
    "For YV12 only, assume it is progressive (default)" : u"Только для YV12: считать его прогрессивный (по умолчанию)",
    "For YV12 only, assume it is interlaced" : u"Только для YV12: считать его чересстрочный.",
    "Current matrix to script" : u"Текущая матрица в скрипте", # New in v2.6.8.4
    "Write the current matrix to script. If no matrix found this matrix is used" : u"Записать текущую матрицу в скрипт. Если матрица не найдена, используется данная матрица", # New in v2.6.8.4
    "Read the matrix now" : u"Прочитать матрицу", # New in v2.6.8.4
    "Try to get the matrix from source or script" : u"Пробовать получить матрицу из источника или скрипта", # New in v2.6.8.4
    "Globally to default" : u"Глобально по умолчанию", # New in v2.6.8.4
    "Reset all scripts to Resolution-based" : u"Сбросить все скрипты к основному разрешению", # New in v2.6.8.4
    "Bit &depth" : u"Битовая глубина цвета",
    "8-bit" : u"8-бит",
    "Regular 8-bit depth (default)" : u"Обычная 8-битная глубина (по умолчанию)",
    "Stacked 16-bit, MSB on top, range reduced to 10-bit. Requires MaskTools v2 loaded" : u"Составные 16-бит, старший бит сверху, диапазон уменьшен до 10 бит. Требуется загрузка MaskTools v2",
    "Stacked yuv420p10 or yuv444p10" : u"Составные yuv420p10 или yuv444p10",
    "Stacked 16-bit, MSB on top" : u"Составные 16-бит, старший бит сверху",
    "Stacked yuv420p16 or yuv444p16" : u"Составной yuv420p16 или yuv444p16",
    "Interleaved 16-bit (little-endian), range reduced to 10-bit. Requires MaskTools v2 loaded" : u"16-битное чередование (с прямым порядком байтов), диапазон уменьшен до 10 бит. Требуется загрузка MaskTools v2",
    "Interleaved yuv420p10 or yuv444p10" : u"Чередование yuv420p10 или yuv444p10",
    "Interleaved 16-bit (little-endian)" : u"16-битное чередование (прямой порядок байтов)",
    "Interleaved yuv420p16 or yuv444p16" : u"Чередование yuv420p16 или yuv444p16",
    "Background &color" : u"Цвет фона",
    "Follow current theme" : u"Следовать текущей теме",
    "Use RGB {hex_value}" : u"Использовать RGB {hex_value}", # New in v2.5.1
    "Use a custom color" : u"Использовать свой цвет",
    "Custom" : u"Пользовательский", # New in v2.5.1
    "Choose the color used if 'custom' is selected" : u"Выберите цвет, который будет использоваться, если выбран 'Пользовательский'", # New in v2.5.1
    "Select custom color" : u"Выбрать свой цвет", # New in v2.5.1
    "Save image as..." : u"Сохранить изображение как...",
    "Save the current frame as image file. If you not change the frame number, Quick save image uses the name." : u"Сохранить текущий кадр как файл изображения. Если вы не измените номер кадра, то быстрое сохранение изображения будет использовать это имя.", # New in v2.6.5.1
    "Quick save image" : u"Быстрое сохранение изображения", # New in v2.5.0
    "Save the current frame with a default filename, overwriting the file if already exists. Press CTRL to reset the default name formatting" : u"Сохранить текущий кадр с именем по умолчанию, перезаписав файл, если он уже существует. Нажмите CTRL, чтобы сбросить форматирование имени по умолчанию", # New in v2.6.5.1
    "Copy image to clipboard" : u"Копировать изображение в буфер обмена", # New in v2.4.2
    "Copy the current frame to the clipboard as a bitmap" : u"Копировать текущий кадр в буфер обмена как растровое изображение", # New in v2.4.2
    "Force the script to reload and refresh the video frame" : u"Перезагрузить скрипт и обновить видео кадр",
    "Refresh preview" : u"Обновить предпросмотр видео",
    "Release all open videos from memory" : u"Выгрузить все открытые видео из памяти",
    "Release all videos from memory" : u"Выгрузить всё видео из памяти",
    "Snapshot" : u"Снимок", # New in v2.6.5.1
    "Take snapshot 1" : u"Сделать снимок 1", # New in v2.6.5.1
    "Make bitmap and script snapshot" : u"Сделать снимок растрового изображения и скрипта", # New in v2.6.5.1
    "Take snapshot 2" : u"Сделать снимок 2", # New in v2.6.5.1
    "Show or hide snapshot 1" : u"Показать или скрыть снимок 1",
    "Show/hide snapshot 1" : u"Показать/скрыть снимок 1",
    "Show or hide snapshot 2" : u"Показать или скрыть снимок 2",
    "Show/hide snapshot 2" : u"Показать/скрыть снимок 2",
    "Copy snap shot 1 to new tab" : u"Скопировать снимок 1 в новую вкладку",
    "New tab from snapshot 1" : u"Новая вкладка из снимка 1",
    "Copy snap shot 2 to new tab" : u"Скопировать снимок 2 в новую вкладку",
    "New tab from snapshot 2" : u"Новая вкладка из снимка 2",
    "Clear tab snapshots" : u"Очистить снимки вкладок",
    "Clears the current tab snapshots" : u"Очистить снимки текущей вкладки",
    "Clear all snapshots Globally" : u"Очистить все снимки, глобально",
    "Clears all snapshots Globally" : u"Очистить все снимки, глобально",
    "Preview filter off" : u"Отключить предпросмотр фильтра", # New in v2.6.6.0
    "Preview filter 1" : u"Предпросмотр фильтра 1", # New in v2.6.6.0
    "1" : u"", # New in v2.6.6.0
    "Preview filter 2" : u"Предпросмотр фильтра 2", # New in v2.6.6.0
    "2" : u"", # New in v2.6.6.0
    "Preview filter 3" : u"Предпросмотр фильтра 3", # New in v2.6.6.0
    "3" : u"", # New in v2.6.6.0
    "Preview filter 4" : u"Предпросмотр фильтра 4", # New in v2.6.6.0
    "4" : u"", # New in v2.6.6.0
    "Preview filter 5" : u"Предпросмотр фильтра 5", # New in v2.6.6.0
    "5" : u"", # New in v2.6.6.0
    "Save preview filters" : u"Сохранить предпросмотр фильтра", # New in v2.6.6.0
    "Save preview filters for later use" : u"Сохранить предпросмотр фильтра для последующего использования", # New in v2.6.6.0
    "Write all preview filters to script" : u"Записать все предпросмотры фильтров в скрипт", # New in v2.6.6.0
    "Write all to script" : u"Записать все в скрипт", # New in v2.6.6.0
    "Write to script" : u"Записать в скрипт", # New in v2.6.6.0
    "Write Preview filter to script" : u"Записать предпросмотр фильтра в скрипт", # New in v2.6.6.0
    "Shows the selected and optional the next or previous tab in one view (video width and height must be the same)" : u"Показывать выбранную и следующую/предыдущую вкладку (по выбору) в одном окне предпросмотра видео (ширина и высота видео должны быть одинаковыми)",
    "Split View on/off" : u"Включение/выключение разделения просмотра",
    "Expands the left shift area of the video window" : u"Расширить область сдвига влево для видеоокна",
    "Toggle extended left move" : u"Переключить расширенное смещение влево", # New in v2.5.1.09
    "Save/Restore last view position and zoom factor on tab change" : u"Сохранить/Восстановить последнее положение просмотра и масштабирования при смене вкладки", # New in v2.6.5.1
    "Save view pos on tab change" : u"Сохранить позицию видеопросмотра при смене вкладки", # New in v2.6.1.5
    "Additional" : u"Дополнительно", # New in v2.6.8.4
    "Show/Hide the preview" : u"Показать/Скрыть видеопросмотр",
    "Toggle the video preview" : u"Показать/Скрыть окно видеопросмотра",
    "Switch focus between the video preview and the text editor" : u"Переключить фокус между окнами видеопросмотра и текстового редактора",
    "Switch video/text focus" : u"Переключить фокус на окон видео/текст",
    "Show/hide the slider sidebar (double-click the divider for the same effect)" : u"Показать/Скрыть колонку ползунков (или двойной щелчок на разделителе)", 
    "Toggle the slider sidebar" : u"Переключить колонку ползунков", 
    "Toggle preview placement" : u"Переключить расположение окна видеопросмотра", # New in v2.5.1
    "When not using a separate window for the video preview, toggle between showing it at the bottom (default) or to the right" : u"Если для предпросмотра видео не используется отдельное окно, то переключить его положение вниз (по умолчанию) или справа", # New in v2.5.1
    "Tools" : u"Инструменты",
    "Request every video frame once (analysis pass for two-pass filters)" : u"Запрашивать каждый видеокадр один раз (анализ для двухпроходных фильтров)",
    "Run analysis pass" : u"Выполнить пробный проход",
    "External player" : u"Внешний проигрыватель",
    "Play the current script in an external program" : u"Проиграть текущий скрипт во внешней программе",
    "External tool arg1" : u"Внешний инструмент arg1",
    "Run the current script with an external program and arg1" : u"Выполнить текущий скрипт во внешней программе с arg1", # New in v2.6.5.1
    "External tool arg2" : u"Внешний инструмент arg2",
    "Run the current script with an external program and arg2" : u"Выполнить текущий скрипт во внешней программе с arg2", # New in v2.6.5.1
    "Show information about the video in a dialog box" : u"Показать информацию о видео в диалоговом окне",
    "Video information" : u"Информация о видео",
    "&Options" : u"&Параметры",
    "Always on top" : u"Всегда поверх",
    "Keep this window always on top of others" : u"Удерживать это окно всегда поверх других",
    "If the video preview is detached, keep it always on top of other windows" : u"Если предварительный просмотр видео отключен, то всегда удерживать его поверх других окон.", # New in v2.3.1
    "Video preview always on top" : u"Окно видеопросмотра всегда сверху", # New in v2.3.1
    "Disable video preview" : u"Отключить видеопросмотр", 
    "If checked, the video preview will not be shown under any circumstances" : u"Если отмечено, видео просмотр не будет показан ни при каких обстоятельствах", 
    "Hide the video window scrollbars" : u"Скрыть полосу прокрутки окна предварительный просмотр видео", # New in v2.6.8.4
    "Hide video window scrollbars" : u"Скрыть полосу прокрутки окна видеопросмотра", # New in v2.6.8.4
    "Accessing AviSynth in threads" : u"Разрешить доступ AviSynth к многопоточности", # New in v2.6.8.4
    "Use threads when accessing avisynth (load/release clip and get frame)" : u"Разрешить AviSynth использовать все потоки/ядра процессора (например для загрузки/выгрузки клипа или получении кадра)", # New in v2.6.8.4
    "AvsPmod should normally be closed after a thread has been canceled by the user. This option tries to assign the clip to the script after the thread has internaly finished." : u"Обычно AvsPmod следует закрывать после того, как поток был отменен пользователем. Эта опция пытается подгрузить клип скрипту после того, как поток внутрисистемно был завершен.", # New in v2.6.8.4
    "On cancel assign the clip later" : u"При отмене обработки видео, загрузить его позже", # New in v2.6.8.4
    "Associate .avs files with AvsPmod" : u"Ассоциировать avs файлы с AvsPmod", # New in v2.6.5.1
    "Configure this computer to open .avs files with AvsP when double-clicked. Run again to disassociate" : u"Открывать двойном щелчком файлы avs с помощью AvsP", # New in v2.4.0
    "Edit the various AviSynth script fonts and colors" : u"Редактировать шрифты и цвета текста для скриптов в AviSynth", 
    "Fonts and colors..." : u"Шрифты и цвета...", 
    "Make fonts && colors backup" : u"Сделать резервную копию шрифтов и цветов", # New in v2.6.8.4
    "Make script fonts and colors backup" : u"Сделать резервную копию шрифтов и цветов",
    "Load fonts && colors backup" : u"Загрузить резервную копию шрифтов и цветов", # New in v2.6.8.4
    "Restores script fonts and colors from backup" : u"Восстанавливает шрифты и цвета из резервной копии",
    "AviSynth function definition..." : u"Определения функций AviSynth...", 
    "Edit the extension-based templates for inserting sources" : u"Редактировать шаблоны для вставки источников на основе расширений файлов",
    "Extension templates..." : u"Шаблоны расширений файлов...", 
    "Snippets..." : u"Отрывки текста...", # New in v2.5.0
    "Edit insertable text snippets" : u"Редактировать вставляемые отрывки текста", # New in v2.5.0
    "Configure the program keyboard shortcuts" : u"Настроить сочетания клавиш быстрого выполнения",
    "Keyboard shortcuts..." : u"Горячие клавиши...", # New in v2.2.1
    "Configure program settings" : u"Настроить параметры программы",
    "Program settings..." : u"Настройки программы...",
    "&Help" : u"&Помощь",
    "Animated tutorial" : u"Анимированный урок",
    "View an animated tutorial for AvsP (from the AvsP website)" : u"Смотреть анимированный урок по AvsP (на сайте AvsP)",
    "Learn more about AvsP text features (from the AvsP website)" : u"Узнать больше об текстовых особенностях AvsP (на сайте AvsP)",
    "Text features" : u"Текстовые функции",
    "Learn more about AvsP video features (from the AvsP website)" : u"Узнайте больше о особенностях видео в AvsP (на сайте AvsP)",
    "Video features" : u"Видео особенности",
    "Learn more about AvsP user sliders (from the AvsP website)" : u"Узнать больше о пользовательских ползунках в AvsP (на сайте AvsP)",
    "User sliders" : u"Пользовательские ползунки",
    "Learn more about AvsP macros (from the AvsP website)" : u"Узнать больше о макросах в AvsP (на сайте AvsP)",
    "Macros" : u"Макросы",
    "Avisynth help" : u"Справка AviSynth",
    "Open the avisynth help html" : u"Открыть html файл справки AviSynth",
    "Open the Preview filter examples" : u"Открыть примеры предпросмотра фильтра", # New in v2.6.6.0
    "Preview filter example" : u"Пример предпросмотра фильтра", # New in v2.6.6.0
    "Accessing in threads readme" : u"Доступ к потокам readme", # New in v2.6.8.4
    "Open the Access in threads readme" : u"Открыть доступ к потокам readme", # New in v2.6.8.4
    "DPI Info" : u"Информация о DPI", # New in v2.6.5.2
    "DPI information" : u"Информация о DPI", # New in v2.6.6.0
    "Active video thread count" : u"Количество активных видеопотоков", # New in v2.6.8.4
    "Prints the active running thread count. Normaly 0" : u"Показывает количество активных запущенных потоков. Нормально 0", # New in v2.6.8.4
    "Displays the available memory in the status bar" : u"Отображает доступный объём память в строке состояния", # New in v2.6.8.4
    "Show available system memory" : u"Показать доступную системную память", # New in v2.6.8.4
    "Open Avisynth plugins folder" : u"Откройте папку плагинов AviSynth", # New in v2.2.1
    "Open the avisynth plugins folder, or the last folder from which a plugin was loaded" : u"Откройте папку плагинов AviSynth или последнюю папку, из которой плагин был загружен", # New in v2.3.1
    "Changelog" : u"Список изменений", # New in v2.4.1
    "Open the changelog file" : u"Открыть файл со списком изменений", # New in v2.4.1
    "About this program" : u"Об этой программе",
    "About AvsPmod" : u"Сведения об AvsPmod", # New in v2.2.1
    "Jump back. Right click for options" : u"Перейти назад. Щелкните правой кнопкой мышки, чтобы увидеть параметры", # New in v2.6.8.4
    "Jump forward. Right click for options" : u"Перейти вперёд. Щелкните правой кнопкой мышки, чтобы увидеть параметры", # New in v2.6.8.4
    "Play/pause video. Right click for options." : u"Воспроизвести/приостановить видео. Щелкните правой кнопкой мышки, чтобы увидеть параметры", # New in v2.6.5.2
    "Run the script with an external program" : u"Выполнить скрипт внешней программой",
    "Run the selected tool" : u"Запустить выбранный инструмент",
    "&Tools" : u"&Инструменты",
    "A macro check item" : u"Элемент проверки макроса", # New in v2.3.0
    "A macro radio item" : u"Элемент макро-радио", # New in v2.3.0
    "Run selected macro" : u"Выполнить выбранный макрос",
    "View the readme for making macros" : u"Посмотреть справку по созданию макросов",
    "Open macros folder" : u"Открыть папку макросов", # New in v2.3.0
    "Open the macros folder" : u"Открыть папку макросов", # New in v2.2.1
    "&Macros" : u"Макросы", # New in v2.2.1
    "Close" : u"Закрыть",
    "Close all the other" : u"Закрыть всё остальное",
    "Rename" : u"Переименовать",
    "Group" : u"Группа",
    "Save" : u"Сохранить",
    "Save as..." : u"Сохранить как...",
    "Reload" : u"Перезагрузить",
    "Open directory" : u"Открыть каталог",
    "Release video memory" : u"Освободить видеопамять",
    "Release all other video memory" : u"Освободите всю остальную видеопамять",
    "Tab change loads bookmarks" : u"При смене вкладки подгружать закладки",
    "Copy to new tab" : u"Копировать в новую вкладку",
    "Split View insert tab" : u"Вставка вкладки разделенного вида", # New in v2.6.5.1
    "Auto preview" : u"Автоматический предпросмотр", # New in v2.6.6.0
    "Reposition to" : u"Перейти на вкладку",
    "Disable refresh" : u"Отключить обновление", # New in v2.6.8.4
    "Custom frame range" : u"Пользовательский диапазон кадров", # New in v2.6.8.4
    "Frame range 30 to n.. or set start,end separated by comma" : u"Количество кадров (от 30 до N), или номера кадров начала и конца (через запятую)", # New in v2.6.8.4
    "Percent" : u"Процент", # New in v2.6.8.4
    "Crop editor" : u"Редактор кадрирования",
    "You can drag the crop regions with the left mouse button when this dialog is visible, cropping the edge closest to the initial mouse click." : u"Когда это окно активно можно указать области подрезки перетаскивая мышку, с нажатой левой кнопкой, по окну предпросмотра видео. Будет обрезана та кромка которая ближе к начальному щелчку мыши.",
    "Auto-crop" : u"Авто-кадрирование",
    "Samples" : u"Образцы", # New in v2.4.0
    "At script end" : u"В конце скрипта",
    "At script cursor" : u"В позиции курсора",
    "Copy to clipboard" : u"Копировать в буфер",
    "Insert Crop() command:" : u"Вставить команду кадрирования - Crop():",
    "Apply" : u"Применить ",
    "Trim editor" : u"Редактор обрезки",
    "Selection options" : u"Параметры выбора",
    "Keep selected regions" : u"Удерживать выбранные области",
    "Keep unselected regions" : u"Удерживать не выбранные области",
    "Mark video frames inside/outside selection" : u"Отметить кадры внутри/снаружи выбранного",
    "Use Dissolve() with overlap frames:" : u"Используйте функцию слияния Dissolve() с перекрывающимися кадрами",
    "Single clips (c0..cn) with prefix:" : u"Отдельные клипы (c0...cn) с префиксом",
    "Insert Trim() commands: " : u"Вставить команду обрезки: Trim()",
    "Insert clips commands: " : u"Вставить команду клипов",
    "Insert Dissolve(trim,) commands: " : u"Вставить команду слияния отрезков - Dissolve(trim,)", # New in v2.6.1.5
    "Insert Dissolve(clips,) commands: " : u"Вставить команду слияния клипов - Dissolve(clips,)", # New in v2.6.1.5
    "Use the buttons which appear on the video slider handle to create the frame selections to trim." : u"Используйте кнопки, которые появляются на ручке ползунка видео, чтобы выделить кадры для обрезки.",
    "Clear" : u"Очистить",
    "The script's directory doesn't exist anymore!" : u"Каталог скрипта больше не существует!",
    "Print Preview" : u"Напечатать предпросмотр", # New in v2.3.1
    "Failed to create print preview" : u"Не удалось создать предпросмотр для печати", # New in v2.3.1
    "Print Error" : u"Ошибка печати", # New in v2.3.1
    "There was an error when printing.\nCheck that your printer is properly connected." : u"При печати произошла ошибка.\nПроверьте, правильно ли подключен ваш принтер.",
    "Printer Error" : u"Ошибка принтера",
    "Damaged session file" : u"Поврежденный файл сеанса",
    "File does not exist!" : u"Файл не существует!", 
    "Select a file" : u"Выбрать файл",
    "Create a separator label" : u"Создать метку разделителя",
    "Enter separator label" : u"Введите метку разделителя",
    "Enter tag name:" : u"Введите имя метки", 
    "Tag definition" : u"Определение метки", 
    "Chapter" : u"Глава",
    "Set title for bookmarks" : u"Укажите заголовок для закладок",
    "Title" : u"Название",
    "Frame No." : u"Номер кадра",
    "Time **" : u"Время **",
    "Left-click on a selected item or double-click to edit.\n\n*  RED - a historic title, not a real bookmark.\n** Time may be unavailable or incorrect before preview refreshed." : u"Щелкните левой кнопкой мышки по выбранному элементу или дважды щелкните по нему для редактирования.\n\n*  RED (КРАСНЫЙ) - первоначальный заголовок, а не настоящая закладка.\n** Перед обновлением предпросмотра время может быть недоступным или неверным.", # New in v2.3.0
    "Image saved to \"{0}\"" : u"Изображение сохранено в \"{0}\"", # New in v2.5.0
    "No image to save" : u"Нет изображения для сохранения",
    "Error requesting frame {number}" : u"Ошибка при запросе кадра {number}",
    "Couldn't open clipboard" : u"Не удалось открыть буфер обмена",
    "Cannot use crop editor unless bit depth is set to 8" : u"Невозможно использовать редактор кадрирования, если битовая глубина цвета не установлена ​​на 8",
    "No filters found, clear the current saved filters?" : u"Фильтры не найдены, очистить текущие сохраненные фильтры?", # New in v2.6.6.0
    "Preview filters" : u"Фильтры предпросмотра", # New in v2.6.6.0
    "Snapshot %d" : u"Снимок %d", # New in v2.6.8.4
    "Error snapshot %d" : u"Ошибка снимка %d", # New in v2.6.8.4
    "Empty snapshot script" : u"Пустой скрипт для снимка", # New in v2.6.8.4
    "Display" : u"Отображение", # New in v2.6.8.4
    "YUV -> RGB" : u"", # New in v2.6.8.4
    "Cannot read the matrix. Clip not initialized" : u"Не удалось прочитать матрицу. Клип не инициализирован", # New in v2.6.8.4
    "Cannot change bit depth while crop editor is open!" : u"Невозможно изменить битовую глубину цвета, пока открыт редактор кадрирования!",
    "Interleaved RGB48" : u"Чередующийся RGB48", # New in v2.5.1
    "Play video" : u"Проиграть видео", # New in v2.6.5.2
    "Avisynth not returned thread still running.\n{0}" : u"AviSynth не вернул поток, который всё ещё выполняется.\n{0}", # New in v2.6.8.4
    "Avisynth not returned frame thread still running.\n{0}" : u"AviSynth не вернул поток кадров, который всё ещё выполняется.\n{0}", # New in v2.6.8.4
    "Error loading the script" : u"Ошибка загрузки скрипта",
    "Starting analysis pass..." : u"Запуск пробного прохода...", # New in v2.3.0
    "Average %#.4g fps\nFrame %s/%s (%#.4g fps)" : u"В среднем %#.4g кадр/с\nКадр %s/%s (%#.4g кадр/с)", # New in v2.6.5.1
    "Finished (%s fps average)\n*** live and let live ***" : u"Завершено (в среднем %s кадр/с)\n*** живи и дай жить другим ***", # New in v2.6.5.1
    "Frame size:" : u"Размер кадра",
    "Length:" : u"Длина:",
    "Frame rate:" : u"Частота кадров:",
    "Colorspace:" : u"Цветовое пространство:",
    "Bit depth:" : u"Битовая глубина цвета:",
    "Field or frame based:" : u"На основе поля или кадра:",
    "Parity:" : u"Четность:",
    "Audio" : u"Звук",
    "Channels:" : u"Каналов:",
    "Hz" : u"Гц",
    "Sampling rate:" : u"Частота дискретизации:",
    "Sample type:" : u"Тип образца:",
    "bits" : u"бит",
    "samples" : u"отсчетов",
    "Bookmarks:" : u"Закладки:", # New in v2.6.8.4
    "Timeline selections:" : u"Выборка временной шкалы:", # New in v2.6.8.4
    "Could not find the macros folder!" : u"Не удалось найти папку с макросами!",
    "Failed to import the selected tool" : u"Не удалось импортировать выбранный инструмент",
    "Basic (1)" : u"Основные (1)",
    "Override all fonts to use a specified monospace font (no effect on scrap window)" : u"Переопределить все шрифты и использовать одни указанный шрифт (кроме окна заметок)", # New in v2.2.1
    "Use monospaced font:" : u"Использовать один шрифт",
    "Default:" : u"По умолчанию:", 
    "Comment:" : u"Комментарий:", 
    "Comment special extension #>:" : u"Комментарий спец. расширения #>:", # New in v2.6.8.4
    "Block Comment:" : u"Комментарий блока:", # New in v2.2.1
    "__END__ Comment:" : u"Комментарий  __END__ :", # New in v2.2.1
    "Number:" : u"Число:", 
    "String:" : u"Строка:", 
    "Triple-quoted string:" : u"Строка в тройных кавычках:", 
    "Assignment:" : u"Присвоение:",
    "Operator:" : u"Оператор:", 
    "Basic (2)" : u"Основные (2)",
    "Internal filter:" : u"Встроенный фильтр:", 
    "External filter:" : u"Внешний фильтр:", 
    "Internal function:" : u"Встроенная функция:", 
    "User defined function:" : u"Функция определенная пользователем:",
    "Unknown function:" : u"Неизвестная функция:",
    "Clip property:" : u"Свойство клипа:", 
    "Parameter:" : u"Параметр:", # New in v2.5.0
    "AviSynth data type:" : u"Тип данных AviSynth:",
    "AviSynth keyword:" : u"Ключевое слово AviSynth:",
    "AvsP user slider:" : u"Пользовательский ползунок AvsP:",
    "Advanced" : u"Продвинутые (1)",
    "Incomplete string:" : u"Незавершенная строка:", 
    "Syntax highlight strings which are not completed in a single line differently" : u"Подсвечивать синтаксис строк, не завершенных по-разному", 
    "Brace highlight:" : u"Подсветка скобок:",
    "Bad brace:" : u"Плохая скобка:",
    "Bad number:" : u"Плохое число:",
    "Margin line numbers:" : u"Номера строк на полях:",
    "Miscellaneous word:" : u"Различные слова:",
    "Calltip:" : u"Подсказка:",
    "Calltip highlight:" : u"Подсветка подсказки:",
    "Cursor:" : u"Курсор:",
    "If checked, highlight also foreground" : u"Если отмечено, то так-же выделяется передний план",
    "Selection highlight:" : u"Подсветка выделения:",
    "Current line highlight:" : u"Подсветка текущей строки:",
    "Highlight the line that the caret is currently in" : u"Подсвечивать строку, на которой сейчас печатная каретка", 
    "Fold margin:" : u"Маркер сворачивания блока:", # New in v2.2.1
    "Scrap window:" : u"Окно заметок:", # New in v2.6.8.4
    "Advanced 2" : u"Продвинутые (2)", # New in v2.6.8.4
    "Slider window:" : u"Окно ползунка:", # New in v2.6.8.4
    "Slider window text field:" : u"Текстовое поле окна ползунка:", # New in v2.6.8.4
    "Slider window default value:" : u"Значение по умолчанию в окне ползунка:", # New in v2.6.8.4
    "Use another color for the sliders background" : u"Использовать другой цвет для фона ползунков", # New in v2.6.8.4
    "Use sparate slider background:" : u"Использовать отдельный фон ползунка:", # New in v2.6.8.4
    "Slider window extras (Snapshot):" : u"Дополнительные возможности окна ползунка (снимок экрана):", # New in v2.6.8.4
    "Information" : u"Информация",
    "Settings have been read from backup file\n" : u"Настройки были прочитаны из файла резервной копии\n", # New in v2.6.1.5
    "File extension shouldn't contain dots!" : u"Расширение файла не должно содержать точек!", # New in v2.5.1
    "Insert aborted:" : u"Вставка прервана:",
    "Edit extension-based templates" : u"Редактировать шаблоны базовых расширений",
    "File extension" : u"Расширение файла",
    "Template" : u"Шаблон",
    "This info is used for inserting sources based on file extensions." : u"Эта информация используется для вставки источников на основе расширений файлов.",
    "Any instances of *** in the template are replaced with the filename." : u"В шаблоне любые образцы, вроде ***, заменяются именем файла.",
    "(If you want relative paths instead of the full filename, use [***].)" : u"(Если требуется использовать относительные пути вместо полного имени файла, используйте [***].)", # New in v2.2.1
    "Only alphanumeric and underscores allowed!" : u"Разрешены только буквы, цифры и символ подчеркивания!",
    "Tag" : u"Тег", # New in v2.5.0
    "Snippet" : u"Отрывок", # New in v2.5.0
    "Associating .avs files will write to the windows registry." : u"При ассоциации файлов avs будет выполнена запись в реестр Windows.",
    "Do you wish to continue?" : u"Вы хотите продолжить?",
    "Associate avs files for all users?" : u"Ассоциировать файлы avs для всех пользователей?", # New in v2.4.0
    "Disassociate avs files for all users?" : u"Отменить ассоциацию файлов avs для всех пользователей?", # New in v2.4.0
    " Admin rights are needed." : u"Необходимы права администратора.", # New in v2.6.5.2
    "Above keys are built-in editing shortcuts. If item is checked,\nit will not be overrided by a menu shortcut in script window." : u"Вышеупомянутые сочетания клавиши по умолчанию встроены в программу. Если действие\nотмечено, то оно не будет заменено пользовательским сочетанием клавиш.", # New in v2.3.0
    "* This shortcut is active only when video window has focus.\n~ This shortcut is active only when script window has focus." : u"* Сочетание клавиш работает только когда активно окно видео.\n~ Сочетание клавиш работает только когда активно окно скрипта.", # New in v2.3.0
    "Could not find the Avisynth plugins folder!" : u"Не удалось найти папку с плагинами AviSynth!", # New in v2.2.1
    "Could not find %(readme)s!" : u"Не могу найти %(readme)s!",
    "Could not find %(changelog)s!" : u"Не могу найти %(changelog)s!", # New in v2.4.1
    "Could not find %(example)s!" : u"Не могу найти %(example)s!", # New in v2.6.6.0
    "{prog_name} v{version} ({arch})" : u"", # New in v2.5.1
    "AvsP Website" : u"Веб-сайт AvsP",
    "AvsPmod Website" : u"Веб-сайт AvsPmod", # New in v2.5.1
    "Active thread on Doom9's forum" : u"Активная тема обсуждения на форуме Doom9", # New in v2.2.1
    "This program is freeware under the GPL license." : u"Эта программа распространяется бесплатно по лицензии GPL.",
    "Drop frames" : u"Пропускать кадры", # New in v2.4.0
    "Half speed" : u"Половина скорости",
    "Custom unit" : u"Пользовательская единица", # New in v2.6.8.4
    "1 Minute" : u"1 Минута", # New in v2.6.8.4
    "1 Second" : u"1 Секунда", # New in v2.6.8.4
    "bookmark highlight color..." : u"цвет подсветки закладки...",
    "selection highlight color..." : u"цвет подсветки выделения...",
    "bell at bookmarks" : u"отметка закладки", # New in v2.6.1.5
    "highlight bookmarks" : u"подсветка закладки",
    "Set bookmark title" : u"озаглавить закладку",
    "copy as time" : u"копировать как время",
    "copy" : u"копировать",
    "paste" : u"вставить",
    "clear history" : u"очистить историю",
    "Frames: %i" : u"Кадры: %i", # New in v2.6.8.4
    "Create trim" : u"Создать обрезку", # New in v2.6.8.4
    "Remove" : u"Удалить", # New in v2.6.8.4
    "Remove all" : u"Удалит всё", # New in v2.6.8.4
    "Remove all other" : u"Удалить всё остальное", # New in v2.6.8.4
    "Trim editor..." : u"Редактор обрезки...", # New in v2.6.8.4
    "Cannot switch tabs while crop editor is open!" : u"Нельзя переключать вкладки при открытом редакторе кадрирования!",
    "Cannot switch tabs while trim editor is open!" : u"Нельзя переключать вкладки при открытом редакторе обрезки!",
    "Invalid crop values detected.  Continue?" : u"Обнаружены недопустимые значения при кадрировании. Продолжить?",
    "Select autocomplete keywords" : u"Выберите ключевые слова автозавершения",
    "select all" : u"выбрать все",
    "select none" : u"ничего не выбирать",
    "exclude long names" : u"исключить длинные имена",
    "Customize the video status bar message" : u"Настроить сообщения в строке состояния видео",
    "Video status bar message:" : u"Сообщение в строке состояния видео:",
    "Legend" : u"Метка",
    "Current frame" : u"Текущий кадр",
    "Framecount" : u"Число кадров",
    "Current time" : u"Текущий кадр",
    "Total time" : u"Общее время",
    "Width" : u"Ширина",
    "Height" : u"Высота",
    "Aspect ratio" : u"Соотношение сторон",
    "Framerate" : u"Частота кадров",
    "Framerate numerator" : u"Числитель частоты кадров",
    "Framerate denominator" : u"Знаменатель частоты кадров",
    "Colorspace" : u"Цветовое пространство",
    "Bits per component" : u"Биты глубины цвета", # New in v2.6.1.5
    "Field or frame based" : u"Поля или целые кадры",
    "Parity" : u"Четность",
    "Parity short (BFF or TFF)" : u"Четность кратко (BFF или TFF)",
    "Audio rate" : u"Частота звука",
    "Audio length" : u"Продолжительность звука",
    "Audio channels" : u"Звуковые каналы",
    "Audio bits" : u"Биты звука",
    "Audio type (Integer or Float)" : u"Тип звука (целый или дробный)",
    "Pixel position (cursor based)" : u"Местоположение пикселя (под курсором)",
    "Pixel hex color (cursor based)" : u"16-тиричный (HEX) цвет пикселя (под курсором)",
    "Pixel rgb color (cursor based)" : u"RGB цвет пикселя (под курсором)",
    "Pixel yuv color (cursor based)" : u"YUV цвет пикселя (под курсором)",
    "Pixel color (auto-detect colorspace)" : u"Цвет пикселя (автоопределение цветового пространства)",
    "Display YUV -> RGB conversion" : u"Преобразование YUV -> RGB", # New in v2.6.8.4
    "Program zoom" : u"Масштаб программы",
    "Bookmark title" : u"Заголовок закладки",
    "Note: The \"\\t\\t\" or \"\\T\\T\" is used to separate the left and right portions of the status bar\n         message." : u"Примечание: \"\\t\\t\" или \"\\T\\T\" используется для разделения левой и правой частей сообщения\nв строке состояния.",
    "Slider update immediately" : u"Немедленное обновление ползунка", # New in v2.6.6.0
    "A macro is still running. Close anyway?" : u"Макрос все еще выполняется. Все равно закрыть?",
    "A clip thread is still running. Close anyway?" : u"Поток клипа все еще выполняется. Все равно закрыть?", # New in v2.6.8.4
    "Save changes before closing?" : u"Сохранить изменения перед закрытием?",
    "Cannot create a new tab while crop editor is open!" : u"Не могу создать новую вкладку при открытом редакторе кадрирования!",
    "Cannot create a new tab while trim editor is open!" : u"Не могу создать новую вкладку при открытом редакторе обрезки!",
    "Source files" : u"Исходные файлы",
    "Open a script or source" : u"Открыть скрипт или источник",
    "Reload the file and lose the current changes?" : u"Перезагрузить файл и потерять текущие изменения?",
    "%d Bookmarks imported" : u"Импортировано закладок: %d",
    "Open this file" : u"Открыть этот файл",
    "Save session before closing all tabs?" : u"Сохранить сеанс перед закрытием всех вкладок?",
    "Save current script" : u"Сохранить текущий скрипт",
    "Directory %(dirname)s does not exist!" : u"Папка %(dirname)s не существует",
    "The saved script has changed because AvsP marked section added" : u"Сохраненный скрипт изменился, т.к. добавлен раздел с пометкой AvsP", # New in v2.6.8.4
    "The saved script has changed because sliders or toggle tags and filters are removed" : u"Сохраненный скрипт был изменен, т.к. ползунки или теги переключения и фильтры были удалены.", # New in v2.6.8.4
    "Error saving the script: %s" : u"Ошибка при сохранении скрипта: %s", # New in v2.6.8.4
    "Script has no text!" : u"В скрипте нет текста!",
    "HTML files" : u"Файлы HTML",
    "Load a session" : u"Загрузить сеанс",
    "File has been modified since the session was saved. Reload?" : u"Файл был изменен с момента сохранения сеанса. Загрузить заново?",
    "Save the session" : u"Сохранить сеанс",
    "Save current frame" : u"Сохранить текущий кадр",
    "Introduce the JPEG Quality (0-100)" : u"Укажите качество JPEG (0-100)", # New in v2.5.0
    "JPEG Quality" : u"Качество JPEG", # New in v2.5.0
    "Insert a source" : u"Вставить источник",
    "All supported plugins" : u"Все поддерживаемые плагины", # New in v2.3.0
    "AviSynth plugins" : u"Плагины AviSynth", # New in v2.3.0
    "VirtualDub plugins" : u"Плагины VirtualDub", # New in v2.3.0
    "VFAPI plugins" : u"Плагины VFAPI", # New in v2.3.0
    "Script import" : u"Импорт скрипта", # New in v2.6.1.5
    "AvxSynth plugins" : u"Плагины AvxSynth", # New in v2.4.0
    "Insert a plugin" : u"Вставить плагин",
    "Line: %(line)i  Col: %(col)i" : u"Строка: %(line)i  Колонка: %(col)i",
    "Frame Based" : u"На основе кадра",
    "Field Based" : u"На основе поля",
    "Bottom Field First" : u"Нижнее поле первое",
    "BFF" : u"",
    "Top Field First" : u"Верхнее поле первое",
    "TFF" : u"",
    "Integer" : u"Целое",
    "Float" : u"Дробное",
    "pos" : u"местоположение",
    "*hex" : u"", # New in v2.6.1.5
    "Waiting for avisynth release memory" : u"Ожидание освобождения памяти используемой AviSynth", # New in v2.6.8.4
    "Clip not released. Memory still allocated" : u"Выгрузка клипа не завершена. Память все еще используется", # New in v2.6.8.4
    "Clip successful released" : u"Выгрузка клипа выполнена успешно", # New in v2.6.8.4
    "Abandoned clip assigned: \"{0}\"" : u"Оставленный клип определён: \"{0}\"", # New in v2.6.8.4
    "Abandoned clip assigned. Select the tab?" : u"Оставленный клип определён. Выбрать вкладку?", # New in v2.6.8.4
    "Abandoned clip released: \"{0}\"" : u"Оставленный клип выгружен: \"{0}\"", # New in v2.6.8.4
    "Process clip..." : u"Обработка клипа...", # New in v2.6.8.4
    "Waiting for avisynth clip" : u"Ожидание клипа AviSynth", # New in v2.6.8.4
    "Clip process finished" : u"Процесс обработки клипа завершен", # New in v2.6.8.4
    "Clip not initialized" : u"Клип не инициализирован", # New in v2.6.8.4
    "Invalid slider text: min > max" : u"Неверное значение ползунка:  min > max",
    "Invalid slider text: value not in bounds" : u"Неверное значение ползунка: значение не в границах",
    "Invalid slider text: bad modulo label" : u"Неверное значение ползунка: неправильная метка по модулю",
    "Invalid slider text: slider label already exists" : u"Неверное значение ползунка: метка ползунка уже существует",
    "Invalid slider text: invalid number" : u"Неверное значение ползунка: неверный номер",
    "Reset to initial value: %(value_formatted)s" : u"Сброс к начальному значению: %(value_formatted)s",
    "Reset to initial value: %(value2_formatted)s" : u"Сброс к начальному значению: %(value2_formatted)s",
    "Invalid hexadecimal color!" : u"Неверное значение цвета в шестнадцатеричной кодировке!",
    "Must specify a max value!" : u"Необходимо указать максимальное значение!",
    "Must specify a min value!" : u"Необходимо указать минимальное значение!",
    "Min value must be a number!" : u"Минимальное значение должно быть числом!",
    "Max value must be a number!" : u"Максимальное значение должно быть числом!",
    "Default value must be a number!" : u"Значение по умолчанию должно быть числом!",
    "Step size value must be a number!" : u"Значение шага должно быть числом!",
    "Add toggle tag" : u"Добавить тег переключения", # New in v2.6.8.4
    "Clear all tags and disable the filters" : u"Очистить все тэги и отключить фильтры", # New in v2.6.8.4
    "Clear all tags && disabled filters" : u"Очистить все тэги && отключить фильтры", # New in v2.6.8.4
    "Toggle exclusions filters" : u"Переключить исключения фильтров", # New in v2.6.8.4
    "General settings..." : u"Общие настройки...",
    "Set same width for all tabs" : u"Задать одинаковую ширину для всех вкладок", # New in v2.6.8.4
    "Update sliders" : u"Обновить ползунки", # New in v2.6.6.0
    "Reset to default value: %(value_formatted)s" : u"Сброс к начальному значению: %(value_formatted)s",
    "Left-click to select a color, right click to reset to default" : u"Щелкните левой кнопкой мыши, чтобы выбрать цвет, щелкните правой кнопкой, чтобы восстановить значение по умолчанию.",
    "Snapshot doesn't seem to be from this session.\nKeep going?" : u"Возможно, что снимок не из этого сеанса.\nПродолжить?", # New in v2.6.8.4
    "Question" : u"Вопрос",
    "Restore to current" : u"Восстановить до текущего", # New in v2.6.8.4
    "Restore to new tab" : u"Восстановить на новую вкладку", # New in v2.6.8.4
    "Joined or disabled filters found: filter1.filter2\nOnly the first filter can have a toggle tag" : u"Обнаружены присоединённые или повреждённые фильтры: filter1.filter2\nТолько первый фильтр может иметь тег переключения.", # New in v2.6.8.4
    "Enter new name" : u"Введите новое имя", # New in v2.6.8.4
    "Rename toggle tag" : u"Переименовать тег переключения", # New in v2.6.8.4
    "Add child" : u"Добавить дочерний элемент", # New in v2.6.8.4
    "Remove child" : u"Удалить дочерний элемент", # New in v2.6.8.4
    "Toggle \"%(label)s\" section" : u"Переключить \"%(label)s\" раздел",
    "Both videos must have the same width and height." : u"Оба видео должны иметь одинаковую ширину и высоту.", # New in v2.6.8.4
    "Save changes before previewing?" : u"Сохранить изменения перед предпросмотром?", 
    "Select an external player" : u"Выберете внешний проигрыватель",
    "A program must be specified to use this feature!" : u"Для использования этой функции должна быть указана программа!",
    "Program not found. Must be specified to use this feature!" : u"Программа не найдена. Необходимо в настройках указать месторасположение программы, чтобы её использовать!", # New in v2.6.5.1
    "Above plugin names contain undesirable symbols.\nRename them to only use alphanumeric or underscores,\nor make sure to use them in short name style only." : u"Вышеупомянутые имена плагинов содержат нежелательные символы.\nПереименуйте их используя только буквы, цифры и символ подчеркивания,\nили убедитесь, что они используются только в стиле коротких имён.",
    "This function is beta!\nFound more then one function with the same name.\nYou should clean up your plugins." : u"Это бета-версия функции!\nНайдено более одной функции с таким же именем.\nВам следует очистить свои плагины.",
    "Don't show me this again" : u"Больше не показывать",
    "Changing the plugins directory writes to the Windows registry.\n" : u"Изменение каталога плагинов записывает в реестр Windows.",
    "Writing to: HKLM\\Software\\Avisynth\\plugindir2_5\n" : u"Запись в: HKLM\\Software\\Avisynth\\plugindir2_5\n", # New in v2.6.1.5
    "Plugins dir registration failed" : u"Ошибка при регистрации каталога плагинов",
    "You're changing the plugins autoload directory.\nDo you wish to change it for all applications? This will\nrequire writing to {0}" : u"Вы изменяете каталог автозагрузки плагинов.\nИзменить его для всех приложений? Для этого\nпотребуется выполнить запись в {0}", # New in v2.4.0
    "Save as" : u"Сохранить как",
    "Select a directory" : u"Выберете папку",
    "Enter information" : u"Введите информацию",
    "Progress" : u"Выполнение",
    "A get pixel info operation has already started" : u"Операция по получению информации о пикселях уже началась", # New in v2.3.0
    "Error in the macro:" : u"Ошибка в макросе:",
    "Couldn't find %(macrofilename)s" : u"Не удалось найти %(macrofilename)s",
    "An AviSynth script editor" : u"Редактор скриптов AviSynth\n(автор qwerpoi, переводчики Fizick, Arx1meD)",
    "Error trying to display the clip" : u"Ошибка при попытке показать клип", # New in v2.5.1
    "Is bit-depth set correctly?" : u"Правильно ли установлена битовая глубина цвета?", # New in v2.5.1
    "Invalid string: " : u"Неверная строка: ", # New in v2.4.0
    "Failed to open the AVI file" : u"Не удалось открыть файл AVI", # New in v2.2.1
    "Failed to open the AVI frame" : u"Не удалось открыть кадр AVI", # New in v2.2.1
    "Failed to retrieve AVI frame" : u"Не удалось получить кадр AVI", # New in v2.2.1
    "Ctrl" : u"",
    "Alt" : u"",
    "Shift" : u"",
    "Error Window" : u"Окно ошибки", # New in v2.4.0
    "Quick find" : u"Быстрый поиск", # New in v2.4.0
    "Find/replace text" : u"Найти/Заменить текст", # New in v2.4.0
    "Search &for" : u"Найти", # New in v2.5.1
    "R&eplace with" : u"Заменить на", # New in v2.5.1
    "Find &next" : u"Найти следующее", # New in v2.5.1
    "Find &previous" : u"Найти предыдущие", # New in v2.5.1
    "&Replace next" : u"Заменить следующее", # New in v2.5.1
    "Replace &all" : u"Заменить всё", # New in v2.5.1
    "Only on word s&tart" : u"Только в начале слова", # New in v2.5.1
    "Only &whole words" : u"Только слово целиком", # New in v2.5.1
    "Only in &selection" : u"Только в выделенном", # New in v2.5.1
    "&Don't wrap-around" : u"Не зацикливать поиск", # New in v2.5.1
    "&Case sensitive" : u"С учетом регистра", # New in v2.5.1
    "Use regular e&xpressions" : u"Использовать регулярные выражения", # New in v2.5.1
    "&Interpret escape sequences" : u"Интерпретировать выходные последовательности", # New in v2.5.1
    "Cannot find \"%(text)s\"" : u"Не удалось найти \"%(text)s\"", # New in v2.3.0
    "Replaced %(count)i times" : u"Заменено %(count)i раз(а)",
    "Program Settings" : u"Настройки программы",
    "Browse" : u"Обзор",
    "* Requires program restart for full effect" : u"* Требует перезапуска программы",
    "Invalid directory!" : u"Неверный каталог!",
    "Invalid filename!" : u"Неверное имя файла!",
    "Edit shortcuts" : u"Изменить сочетания клавиш",
    "Menu label" : u"Метка меню",
    "Keyboard shortcut" : u"Сочетание клавиш",
    "Double-click or hit enter on an item in the list to edit the shortcut." : u"Для изменения сочетания клавиш - дважды щелкните или нажмите Enter",
    "Shortcut" : u"Сочетание клавиш",
    "Action" : u"Действие", # New in v2.2.1
    "Edit the keyboard shortcut" : u"Изменить сочетание клавиш быстрого запуска",
    "Key:" : u"Клавиша:",
    "%(keyString)s not found in key string list" : u"%(keyString)s не найдена в списке сочетаний клавиш",
    "This shortcut is being used by:" : u"Это сочетание клавиш используется как:",
    "Insert" : u"Вставить",
    "Delete" : u"Удалить",
    "Error: key %(key)s does not exist!" : u"Ошибка: клавиша %(key)s не существует!",
    "Item %(newKey)s already exists!" : u"Клавиша %(newKey)s уже присвоена",
    "Are you sure you want to rename from %(oldName)s to %(newName)s?" : u"Вы уверены, что хотите переименовать %(oldName)s на %(newName)s?",
    "Insert a new item" : u"Вставьте новый пункт",
    "Must enter a name!" : u"Необходимо указать имя!",
    "Warning: no value entered for item %(newKey)s!" : u"Предупреждение: не присвоено значение для пункта %(newKey)s!",
    "Message" : u"Сообщение",
    "Select an item to delete first" : u"Для удаления сначала выберете пункт",
    "Are you sure you want to delete item %(key)s?" : u"Вы уверены, что хотите удалить пункт %(key)s?",
    "Error: minValue must be less than maxValue" : u"Ошибка: мин. величина должна быть меньше чем макс. величина",

    #--- Tool: resize_calc.py ---#
    "Resize calculator..." : u"Калькулятор изменения размера...",
    "Calculate an appropriate resize for the video" : u"Рассчитайте подходящий размер для видео", # New in v2.2.1
    "Resize calculator" : u"Калькулятор изменения размера кадра", # New in v2.2.1
    "Input" : u"Исходное видео", # New in v2.2.1
    "Video resolution:" : u"Разрешение видео:", # New in v2.2.1
    "Pixel aspect ratio:" : u"Соотношение сторон пикселя PAR):", # New in v2.2.1
    "Results" : u"Результат", # New in v2.2.1
    "Aspect ratio error:" : u"Ошибка соотношения сторон:", # New in v2.2.1
    "Settings" : u"Настройки", # New in v2.2.1
    "Target pixel aspect ratio:" : u"Соотношение сторон целевого пикселя:", # New in v2.2.1
    "Resize block constraints:" : u"Ограничения размера блока:", # New in v2.2.1
    "Resize percent ranges:" : u"Диапазонов процентов:", # New in v2.2.1
    "Max search aspect ratio error:" : u"Ошибка вычисления макс. соотношения сторон:", # New in v2.2.1
    "Configure" : u"Настроить", # New in v2.2.1
    "compute from .d2v" : u"определить из .d2v", # New in v2.2.1
    "Configure options" : u"Настроить параметры", # New in v2.2.1
    "Avisynth resize:" : u"Функция AviSynth:", # New in v2.2.1
    "The current Avisynth script contains errors." : u"Текущий скрипт AviSynth содержит ошибки.", # New in v2.2.1

    #--- Tool: encoder_gui.py ---#
    "Script encoder (CLI)" : u"Кодировщик скриптов (CLI)", # New in v2.4.0
    "Use an external command line encoder to save the current script" : u"Использовать внешний кодировщик, чтобы сохранить текущий скрипт в видео", # New in v2.4.0
    "Encode video" : u"Кодировать видео", # New in v2.2.1
    "System settings" : u"Системные настройки", # New in v2.2.1
    "Input file:" : u"Входной файл:", # New in v2.2.1
    "Output file:" : u"Выходной файл:", # New in v2.2.1
    "Compression settings" : u"Настройки сжатия", # New in v2.2.1
    "Bitrate (kbits/sec):" : u"Битрейт (кбит/с): ", # New in v2.2.1
    "calculate" : u"вычислить", # New in v2.2.1
    "Quality CRF (0-51):" : u"Метод CRF (0-51):", # New in v2.2.1
    "Quality CQ (1-31):" : u"Метод CQ (1-31):", # New in v2.2.1
    "Additional settings" : u"Дополнительные настройки", # New in v2.2.1
    "Credits start frame:" : u"Всего кадров:", # New in v2.2.1
    "Command line settings" : u"Настройки командной строки", # New in v2.2.1
    "Run" : u"Выполнить",
    "First time using this compression preset!" : u"Предустановки для сжатия используются впервые!", # New in v2.2.1
    "Please enter the exe paths in the following dialog." : u"Введите пути к исполняемым файлам .exe в следующем диалоговом окне.", # New in v2.2.1
    "Exe pathnames" : u"Путь к файлу .exe", # New in v2.2.1
    "Open an AviSynth script" : u"Открыть AviSynth скрипт",
    "Save the video as" : u"Сохраните видео как", # New in v2.2.1
    "Select a program" : u"Выберите программу", # New in v2.2.1
    "Unreplaced items remain in the command line:" : u"Незамещённые элементы остаются в командной строке:", # New in v2.2.1
    "Unknown exe paths!" : u"Неизвестные пути к .exe!", # New in v2.2.1
    "General" : u"Общие",
    "Credits warning minutes:" : u"Минуты предупреждения:", # New in v2.2.1
    "Automatically compute bitrate value on startup" : u"Автоматически вычислять битрейт при запуске", # New in v2.2.1
    "Automatically compute pixel aspect ratio from d2v on startup" : u"Автоматически вычислять соотношение сторон пикселя (PAR) из d2v при запуске", # New in v2.2.1
    "Append batch commands to the avs script as comments" : u"Добавлять пакетные команды в скрипт avs в виде комментариев", # New in v2.2.1
    "Add output file to new tab" : u"Добавить выходной файл на новую вкладку", # New in v2.6.5.1
    "Encoder priority:" : u"Приоритет кодировщика:", # New in v2.2.1
    "Path to %(name)s:" : u"Путь к %(name)s:", # New in v2.2.1
    "Extra arguments:" : u"Дополнительные аргументы:", # New in v2.2.1
    "Presets file not found:\n" : u"Файл предустановок не найден:\n", # New in v2.6.8.4
    "Bitrate Calculator" : u"Калькулятор битрейта", # New in v2.2.1
    "Output info" : u"Выходная информация", # New in v2.2.1
    "Total size:" : u"Общий размер:", # New in v2.2.1
    "Container:" : u"Контейнер:", # New in v2.2.1
    "(None)" : u"(Нет)", # New in v2.2.1
    "Video info" : u"Информация о видео", # New in v2.2.1
    "Framecount:" : u"Количество кадров:", # New in v2.2.1
    "FPS:" : u"Количество кадров в секунду (FPS):", # New in v2.2.1
    "Audio info" : u"Информация о звуке", # New in v2.2.1
    "Audio file:" : u"Аудио файл:", # New in v2.2.1
    "Compress audio" : u"Сжать аудио", # New in v2.2.1
    "Audio bitrate:" : u"Битрейт аудио:", # New in v2.2.1
    "Format:" : u"Формат:", # New in v2.2.1
    "Subtitles info" : u"Информация о субтитрах", # New in v2.2.1
    "Subtitles file:" : u"Файл субтитров:", # New in v2.2.1
    "Total time:" : u"Общее время:", # New in v2.2.1
    "Video size:" : u"Размер видео:", # New in v2.2.1
    "Audio size:" : u"Размер аудио:", # New in v2.2.1
    "Subtitles size:" : u"Размер субтитров:", # New in v2.2.1
    "Overhead size:" : u"Размер доп. элементов:", # New in v2.2.1
    "Bitrate:" : u"Битрейт:", # New in v2.2.1
    "Open the audio file" : u"Открыть аудио файл", # New in v2.2.1
    "Open the subtitles file" : u"Открыть файл субтитров", # New in v2.2.1
    "%(h)i hr and %(m)i min" : u"%(h)i часов и %(m)i минут", # New in v2.2.1

    #--- Tool: avs2avi_gui.py ---#
    "Script encoder (VFW)" : u"Кодировщик скриптов в .avi", # New in v2.4.0
    "Use avs2avi to save the current script as an avi" : u"Используйте avs2avi.exe, чтобы сохранить текущий скрипт в формат avi", # New in v2.2.1
    "Please select the path to avs2avi.exe" : u"Выберите путь к avs2avi.exe", # New in v2.2.1
    "Error: avs2avi is required to save an avi!" : u"Ошибка: требуется avs2avi.exe для сохранения в avi!",
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
    "Save the avi as" : u"Сохранить avi как",
    "Avi file (*.avi)|*.avi" : u"Файл avi (*.avi)|*.avi",
    "Input file does not exist!" : u"Входной файл не существует!",
    "Input file must be an avisynth script!" : u"Входной файл должен быть скриптом AviSynth!",
    "Output path does not exist!" : u"Выходной путь не существует",
    "# of passes must be an integer!" : u"Число проходов должно быть целым числом!",
    "Priority must be an integer!" : u"Приоритет должен быть целым числом!",
    "Stop" : u"Остановить",
    "Done" : u"Выполнено",
    "Process stopped." : u"Обработка остановлена.",
    "Processing..." : u"Обработка...",
    "Finished in %(hr)i hour(s) and %(min)i minute(s)." : u"Завершено за %(hr)i часов и %(min)i минут.",
    "Finished in %(min)i minute(s) and %(sec)i second(s)." : u"Завершено за %(min)i минут и %(sec)i секунд.",
    "Finished in %(time).1f seconds." : u"Завершено за %(time).1f секунд.",
    "Filesize: %(size).2f MB" : u"Размер файла: %(size).2f MB",
    "The current script contains errors, exiting." : u"Текущий скрипт содержит ошибки (выходной).", # New in v2.2.1
    "Save as AVI" : u"Сохранить как avi",

    #--- Macros ---#
    "Bookmarks at Intervals" : u"", # New in v2.3.0
    "Bookmarks to Chapter" : u"", # New in v2.3.0
    "Bookmarks to Trims" : u"", # New in v2.6.5.1
    "ConditionalReader file from bookmarks" : u"", # New in v2.3.0
    "ConditionalReader file from WriteFile" : u"", # New in v2.6.8.4
    "DeleteFrame" : u"", # New in v2.3.0
    "DuplicateFrame" : u"", # New in v2.3.0
    "Import bookmarks from file" : u"", # New in v2.3.1
    "Open Image Sequence" : u"", # New in v2.6.5.1
    "Preview from current point" : u"", # New in v2.3.0
    "PreviewEncode" : u"", # New in v2.6.8.4
    "PreviewResize" : u"", # New in v2.6.8.4
    "Random Clip Order" : u"", # New in v2.3.0
    "RemovePing" : u"", # New in v2.6.8.4
    "Save Image Sequence" : u"", # New in v2.3.0
    "Selected trims to selections" : u"", # New in v2.6.5.1
    "Shift Bookmarks by frames" : u"", # New in v2.3.0
    "Example (Resize)" : u"", # New in v2.3.0
    "Examples" : u"", # New in v2.3.0
    "Extra" : u"", # New in v2.6.8.4
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
    "DeleteEncodings" : u"", # New in v2.6.8.4

    #--- Macro: Bookmarks at Intervals ---#
    "Choose a frame step or a number of intervals" : u"", # New in v2.3.0
    "Number of intervals" : u"", # New in v2.3.0
    "End frame" : u"", # New in v2.4.2
    "Start frame" : u"", # New in v2.4.2
    "Clear bookmarks in the same range" : u"", # New in v2.4.2

    #--- Macro: Bookmarks to Chapter ---#
    "Save chapter file as..." : u"", # New in v2.4.0
    "Text files" : u"", # New in v2.3.0

    #--- Macro: Bookmarks to Trims ---#
    "No bookmarks defined." : u"", # New in v2.6.5.1

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

    #--- Macro: ConditionalReader file from WriteFile ---#
    "There is not Valus" : u"", # New in v2.6.8.4
    "ConditionalReader file from WriteFile file" : u"", # New in v2.6.8.4

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

    #--- Macro: Open Image Sequence ---#
    "Select the Image" : u"", # New in v2.6.5.1
    "Images (bmp, jpg, png, tiff)" : u"", # New in v2.6.5.1
    "All files (*.*)" : u"", # New in v2.6.5.1

    #--- Macro: Preview from current point ---#
    "Failed to run the external player!\n\nOpen the macro file in the \"Macros\" subdirectory\nwith a text editor and edit the executable\ndirectory appropriately!" : u"", # New in v2.3.0

    #--- Macro: PreviewEncode ---#
    "Convert to script color space" : u"", # New in v2.6.8.4
    "Encode threads:" : u"", # New in v2.6.8.4
    "Insert trims into script" : u"", # New in v2.6.8.4
    "Select save path:" : u"", # New in v2.6.8.4
    "Template:" : u"", # New in v2.6.8.4
    "Use script dir" : u"", # New in v2.6.8.4
    "Encode options" : u"", # New in v2.6.8.4
    "You must first create selections" : u"", # New in v2.6.8.4
    "Last encoding returns error. Process is canceled\n" : u"", # New in v2.6.8.4
    "Error, cannot insert the encode preview text\nTrying to create new tab" : u"", # New in v2.6.8.4
    "Encoding finished\n\nElapsed time: %s\n%s%s" : u"", # New in v2.6.8.4

    #--- Macro: PreviewResize ---#
    "BicubicResize" : u"", # New in v2.6.8.4
    "Spline16Resize" : u"", # New in v2.6.8.4
    "Spline36Resize" : u"", # New in v2.6.8.4
    "Spline64Resize" : u"", # New in v2.6.8.4
    "0" : u"", # New in v2.6.8.4
    "0.5" : u"", # New in v2.6.8.4
    "0.75" : u"", # New in v2.6.8.4
    "1.5" : u"", # New in v2.6.8.4
    "2.0" : u"", # New in v2.6.8.4
    "Border:" : u"", # New in v2.6.8.4
    "Fit only height" : u"", # New in v2.6.8.4
    "Resize Filter:" : u"", # New in v2.6.8.4
    "Resise options" : u"", # New in v2.6.8.4

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
    "Add image source to the script  ->" : u"", # New in v2.6.5.1
    "To new tab" : u"", # New in v2.6.5.1
    "Range between bookmarks" : u"", # New in v2.4.0
    "From first to last bookmark" : u"", # New in v2.6.5.1
    "Trim editor selections" : u"", # New in v2.4.0
    "All frames" : u"", # New in v2.4.0
    "Select an output directory and basename for the new images files" : u"", # New in v2.4.0
    "Bookmarks out of frame count" : u"", # New in v2.6.5.1
    "At least 2 bookmarks are required" : u"", # New in v2.6.5.1
    "There is not Trim editor selections" : u"", # New in v2.4.0
    "There is no process selection" : u"", # New in v2.6.5.1
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