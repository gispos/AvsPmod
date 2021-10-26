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

version = "2.6.9.8"

messages = {
    "AviSynth script" : u"Скрипт AviSynth",
    "AviSynth fonts and colors" : u"Шрифты и цвета AviSynth", 
    "Background" : u"Фон", 
    "Font" : u"Шрифт", 
    "Text color" : u"Цвет текста", 
    "Select a predefined theme" : u"Выберите тему",
    "Only change colours" : u"Изменять только цвета",
    "When selecting a theme, don't change current fonts" : u"При выборе темы не изменять шрифты.",
    "OK" : u"Применить", 
    "Cancel" : u"Отмена",
    "Page:" : u"Страница",
    "Page: %d" : u"Страница: %d",
    "Frame properties" : u"", # New in v2.6.9.8
    "Word warp" : u"", # New in v2.6.9.8
    "Horz scroll" : u"", # New in v2.6.9.8
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
    "New function" : u"Новая функция",
    "Edit selected" : u"Редактировать выбранное",
    "Delete selected" : u"Удалить выбранное",
    "Select installed" : u"Выделить установленные",
    "Import" : u"Импорт",
    "Import from files" : u"Импорт из файла",
    "Import from wiki" : u"Импорт из Wiki",
    "Export customizations" : u"Экспорт настроек",
    "Clear customizations" : u"Очистить настройки",
    "Clear manual presets" : u"Очистить предустановки вручную",
    "When importing, don't show the choice dialog" : u"При импорте не показывать диалоговое окно выбора",
    "Edit function information" : u"Изменить информации о функциях",
    "Name:" : u"Имя",
    "Type:" : u"Тип",
    "clip property" : u"свойство клипа", 
    "core filter" : u"встроенный фильтр",
    "plugin" : u"фильтр из плагина",
    "script function" : u"функция скрипта",
    "user function" : u"функция пользователя",
    "Arguments:" : u"Аргументы:",
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
    "Open Customization files, Avisynth scripts or Avsp options files" : u"", # New in v2.6.9.8
    "All supported" : u"Все поддерживаемые",
    "Customization file" : u"Файл настроек",
    "AvsP data" : u"Данные AvsP",
    "Unrecognized files" : u"Не распознанные файлы",
    "Select the functions to import" : u"Выберите функции для импорта",
    "Check selected" : u"Отметить выбранное",
    "Check all" : u"Отметить все",
    "Check all in this file" : u"Отметить все в этом файле",
    "Check all not customized" : u"Отметить все не настроенное",
    "Uncheck selected" : u"Убрать отметку с выбранного",
    "Uncheck all" : u"Убрать все отметки",
    "Uncheck all in this file" : u"Убрать все отметки в этом файле",
    "Uncheck all customized" : u"Убрать отметки со всех настроенных",
    "Red - a customized function already exists." : u"Красный - настраиваемая функция уже существует.",
    "Invalid plugin function name \"{name}\". Must be \"pluginname_functionname\"." : u"Неправильное имя функции плагина \"{name}\". Должно быть \"pluginname_functionname\".",
    "No customizations to export!" : u"Нет настроек для экспорта!",
    "Save filter customizations" : u"Сохранить настройки фильтра",
    "This will delete all filter customizations. Continue?" : u"Все настройки фильтра будут удалены. Продолжить?",
    "Warning" : u"Предупреждение",
    "This will delete all manually defined presets. Continue?" : u"Это удалит все заданные вручную предустановки. Продолжать?",
    "Do you really want to delete this custom filter?" : u"Вы действительно хотите удалить этот настраиваемый фильтр?",
    "Do you really want to reset this filter?" : u"Вы действительно хотите сбросить этот фильтр?",
    "Edit filter database" : u"Редактировать базу данных фильтров",
    "Default" : u"По умолчанию",
    "Min value" : u"Мин. значение",
    "Max value" : u"Мак. значение",
    "Step size" : u"Шаг",
    "Value list (comma separated)" : u"Список значений (через запятую)",
    "Value must be True or False!" : u"Значение должно быть True (истинным) или False (ложным)!",
    "Export filter customizations" : u"Экспорт настроек фильтра",
    "Import filter customizations" : u"Импорт настроек фильтра",
    "Select filters to export:" : u"Выберите фильтры для экспорта:",
    "Select filters to import from the file:" : u"Выберите фильтры для импорта из файла:",
    "Overwrite all data" : u"Перезаписать все данные",
    "You must select at least one filter!" : u"Вы должны выбрать по крайней мере один фильтр!",
    "Slider SetRange Error: minValue must be less than maxValue" : u"Ошибка ползунка SetRange: minValue должно быть меньше maxValue",
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
    "A crash detected at the last running!" : u"При последнем запуске обнаружен сбой!",
    "&Zoom" : u"&Изменить масштаб",
    "Damaged {0}. Using default settings." : u"Повреждено {0}. Использование настроек по умолчанию.",
    "%s translation file updated with new messages to translate" : u"%s файл перевода дополнен новыми сообщениями для перевода",
    "Translation updated" : u"Перевод обновлен",
    "%s translation file updated.  No new messages to translate." : u"%s файл перевода обновлён. Нет новых сообщений для перевода.",
    "%s language couldn't be loaded" : u"%s не удалось загрузить язык",
    "Cannot read the avisynth plugins directory from the registry\n" : u"Не удалось прочитать каталог плагинов AviSynth из реестра\n",
    "HKLM\\Software\\Avisynth'plugindir2_5' or 'plugindir+' is missing or wrong.\n\n" : u"HKLM\\Software\\Avisynth'plugindir2_5' или 'plugindir+' отсутствует или неправильная.\n\n",
    "You should set the plugins path under options manually or register it." : u"Вы должны установить путь к плагинам в разделе параметры вручную или зарегистрировать его.",
    "Alternatively, specify now its directory." : u"Либо теперь укажите его каталог.",
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
    "This changes the plugins directory for Avisynth itself. On Windows Registry values in HKLM are changed." : u"Это изменит каталог плагинов для AviSynth. Так же будут изменены записи в реестре Windows в разделе HKLM.",
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
    "Location of external program, e.g. AvsMeter" : u"Расположение внешней программы, например, AvsMeter",
    "Arguments for external tool menu 1, e.g. Menu label|arguments\nUse %fn to pass the script file name with the arguments." : u"Доп. аргументы для внешнего меню программы 1.\nНапример Menu label|arguments\nИспользуйте %fn, чтобы передать имя файла сценария с аргументами.",
    "External tool arg1:" : u"Аргументы внешней программы, arg1:",
    "Arguments for external tool menu 2, e.g. Menu label|arguments\nUse %fn to pass the script file name with the arguments." : u"Доп. аргументы для внешнего меню программы 2.\nНапример Menu label|arguments\nИспользуйте %fn, чтобы передать имя файла сценария с аргументами.",
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
    "Prefer functions over variables" : u"Предпочтение функций перед переменными",
    "When a word could be either a function or a variable, highlight it as function" : u"Когда слово может быть функцией или переменной, то выделить его как функцию",
    "Don't allow lines wider than the window" : u"Не допускать длину строки шире окна", 
    "Wrap text" : u"Перенос текста",
    "Draw lines at fold points" : u"Показать линии для свёрнутых блоков скрипта",
    "For code folding, draw a line underneath if the fold point is not expanded" : u"Если блок скрипта свёрнут, то показывать под ней линию",
    "Check to insert actual tabs instead of spaces when using the Tab key" : u"Вставлять отступы вместо пробелов при нажатии клавиши Tab",
    "Use tabs instead of spaces" : u"Использовать отступы вместо пробелов",
    "Set the size of the tabs in spaces" : u"Установить размер отступа в пробелах",
    "Tab width" : u"Ширина отступа",
    "Initial space to reserve for the line margin in terms of number of digits. Set it to 0 to disable showing line numbers" : u"Начальное место, зарезервированное для поля строки в виде количества цифр. Установите значение 0, чтобы отключить отображение номеров строк.",
    "Line margin width" : u"Ширина отступа строк",
    "Show filter calltips" : u"Показывать подсказки для фильтра",
    "Turn on/off automatic tips when typing filter names" : u"Показывать автоматические подсказки при написании имени фильтра",
    "Always show calltips any time the cursor is within the filter's arguments" : u"Всегда показывать подсказки во время нахождения курсора в аргументах фильтра", 
    "Frequent calltips" : u"Частые подсказки",
    "Show autocomplete on capital letters" : u"Показывать автозавершение с заглавной буквы",
    "Turn on/off automatic autocomplete list when typing words starting with capital letters" : u"Показывать список автоматического завершения при написании слов, начинающихся с заглавных букв",
    "Amount of letters typed" : u"Количество написанных букв",
    "Show autocomplete list when typing a certain amount of letters" : u"Показывать список автозавершений при вводе определенного количества букв",
    "Autocomplete" : u"Автозавершение",
    "AviSynth user function database" : u"База данных пользовательских функций AviSynth",
    "Select what functions beside internal and user-defined will be included in the database" : u"Выберите, какие функции, помимо встроенных и пользовательских, будут включены в базу данных",
    "Autoloaded plugin functions" : u"Автозагружать фильтры из плагинов",
    "Include the functions on autoloaded plugins in the database" : u"Автоматически загружать фильтры из плагинов в базу данных",
    "Autoloaded script functions" : u"Автозагружать функции из скриптов",
    "Include the functions on autoloaded avsi files in the database" : u"Автоматически загружать функции из файлов avsi в базу данных",
    "Include plugin functions from the program's database" : u"Использовать фильтры плагинов из базы данных программы",
    "Plugin functions from database" : u"Фильтры плагинов из базы данных",
    "Include user script functions from the program's database" : u"Использовать функции пользовательских скриптов из базы данных программы",
    "Script functions from database" : u"Функции скриптов из базы данных",
    "Add user defined variables into autocomplete list" : u"Добавить пользовательские переменные в список автозавершения",
    "Show autocomplete with variables" : u"Показывать автозавершение с переменными",
    "Show autocomplete on single matched lowercase variable" : u"Показывать автозавершение для одной совпавшей переменной в нижнем регистре",
    "When typing a lowercase variable name, show autocomplete if there is only one item matched in keyword list" : u"При вводе имени переменной в нижнем регистре показывать автозавершение, если в списке ключевых слов совпадает только один элемент",
    "Add icons into autocomplete list. Using different type to indicate how well a filter's presets is defined" : u"Добавлять значки в список автозавершения. Использовать различные типы значков для определения того, насколько хорошо настроены предустановки фильтра",
    "Show autocomplete with icons" : u"Показать список автозавершений со значками",
    "Don't show autocomplete when calltip is active" : u"Не показывать автозавершение, когда активна подсказка",
    "When calltip is active, autocomplete will not be activate automatically. You can still show autocomplete manually" : u"Когда активна подсказка, автозавершение не активируется автоматически. Вы по-прежнему можете вызвать автозавершение вручную",
    "Autoparentheses level" : u"Авто-завершение скобок",
    "Close \"()\"" : u"Закрытые \"()\"",
    "Determines parentheses to insert upon autocompletion" : u"Дополняет скобки при автозавершении",
    "None \" \"" : u"Отсутствует \" \"",
    "Open \"(\"" : u"Открытая \"(\"",
    "Determines which key activates the filter preset when the autocomplete box is visible" : u"Определяет, какая клавиша активирует предустановку фильтра, когда отображается окошко автозавершения",
    "Preset activation key" : u"Предустановленный ключ активации",
    "Return" : u"Вернуть",
    "Tab" : u"Вкладка",
    "None" : u"Нет",
    "Video" : u"Видео",
    "Constantly update video while dragging" : u"Непрерывно обновлять видео при перетаскивании ползунка",
    "Update the video constantly when dragging the frame slider" : u"Постоянно обновлять видео при перетаскивании ползунка кадров",
    "Enable line-by-line update" : u"Разрешить обновление видео построчно", 
    "Enable the line-by-line video update mode (update every time the cursor changes line position)" : u"Разрешить режим построчного обновления видео (обновлять каждый раз при смене позиции строки курсора)", 
    "Focus the video preview upon refresh" : u"Фокус на видеопросмотре при обновлении",
    "Switch focus to the video preview window when using the refresh command" : u"Переключить фокус на окно видеопросмотра при использовании команды обновить",
    "Refresh preview automatically" : u"Автообновление видеопросмотра при смене окна",
    "Refresh preview when switch focus on video window or change a value in slider window" : u"Обновить видеопросмотра при изменении фокуса на окно видео или изменении значения на временной шкале видео",
    "Move video slider to timeline start" : u"Переместить ползунок видео к началу временной шкалы",
    "On moving timeline range with keys Ctrl + Alt + PageDown\nTimeline moving with Ctrl + Alt + (Left, Right, PageUp, PageDown)\n or left mouse button on the status bar, with Shift no limit" : u"При перемещении диапазона временной шкалы нажатием клавиш Ctrl+Alt+PageDown\nВременная шкала перемещается нажатием клавиш Ctrl+Alt+(Left, Right, PageUp, PageDown)\n или левой кнопки мыши в строке состояния без удерживания Shift",
    "Seeking to a certain frame will seek to that frame on all tabs" : u"При поиске определенного кадра будет выполняться поиск этого кадра на всех вкладках",
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
    "Keep the slider window hidden by default when previewing a video" : u"Скрывать окна ползунков по умолчанию при просмотре видео",
    "Create user sliders automatically" : u"Автоматически создавать пользовательские ползунки",
    "Create user sliders automatically using the filter database" : u"Автоматически создавать пользовательские ползунки с помощью базы данных фильтров",
    "Create user sliders for int and float arguments" : u"Создавать пользовательские ползунки для аргументов типа int и float",
    "type int/float (numerical slider)" : u"тип int/float (числовой ползунок)",
    "Create listboxes for int list arguments" : u"Создавать выпадающие списки для аргументов типа int-списка",
    "type int (list)" : u"тип int (список) ",
    "Create color pickers for hex color arguments" : u"Создавать палитры цветов для цветовых аргументов в шестнадцатеричной кодировке",
    "type int (hex color)" : u"тип int (цвет в шестнадцатеричной кодировке)",
    "Create radio boxes for bool arguments" : u"Создавать радиокнопки для аргументов типа bool",
    "type bool" : u"тип bool",
    "Create listboxes for string list arguments" : u"Создавать выпадающие списки для аргументов типа string",
    "type string (list)" : u"тип string (список)",
    "Create filename pickers for string filename arguments" : u"Создавать поле имени файла для строковых аргументов имени файла",
    "type string (filename)" : u"тип string (имя файла)",
    "Create placeholders for arguments which have no database information" : u"Создавать поле для аргументов, для которых отсутствует информация в базе данных",
    "undocumented" : u"недокументированный",
    "Disable refresh as default" : u"Отключить обновление по умолчанию",
    "Do not reinitialize the clip every time a slider is changed. Can be changed in the slider window" : u"Не выполнять повторную инициализацию клипа при каждом смене ползунка. Может быть изменено в поле ползунка",
    "Button show/hide applies to all tabs" : u"Действие Показать/Скрыть применяется ко всем вкладкам",
    "Or press Ctrl when you click the button." : u"Или удерживайте Ctrl при нажатии кнопки.",
    "Hide slider window toggle tag menus*" : u"Скрыть меню тегов в окне ползунка *",
    "Hide the toggle tag menus in the context menu of the sliders" : u"Скрывать меню тегов переключения в контекстном меню ползунков",
    "Custom colors can be set under 'Options->Font and colors->Advanced 2'\nNot visible slider windows needed refresh." : u"Пользовательские цвета можно задать в разделе 'Параметры -> Шрифты и цвета -> Продвинутые 2'\nНе видимые окна ползунков, которые необходимо обновить.",
    "Enable slider window custom color theme" : u"Включить пользовательскую цветовую тему окна ползунка",
    "Determines which filters will initially have hidden arguments in the slider window" : u"Укажите, как именно будут выглядеть аргументы фильтра в окне ползунков",
    "Fold all" : u"Сворачивать всё",
    "Fold non-numbers" : u"Сворачивать не числовые ползунки",
    "Fold none" : u"Не сворачивать",
    "Fold or restore last status" : u"Свернуть или восстановить последнее состояние",
    "Fold startup setting" : u"Сворачивание аргументов фильтра при скрытии окна ползунков",
    "Filter exclusion list:" : u"Фильтр списка исключений",
    "Specify filters never to build automatic sliders for. Use a space as separator.\nYou can toggle it in the slider context menu." : u"Укажите фильтры, для которых не будут создаваться автоматические ползунки. Используйте пробел в качестве разделителя.\nВы можете переключать его в контекстном меню ползунка.",
    "Save/Load" : u"Сохранить/Загрузить",
    "Automatically save the session on shutdown and load on next startup" : u"Автоматически сохранять сеанс при закрытии и загружать его при следующем запуске",
    "Save session for next launch" : u"Сохранять сеанс для следующего запуска",
    "Always load startup session" : u"Всегда загружать сеанс запуска", 
    "Always load the auto-saved session before opening any other file on startup" : u"При запуске программы всегда загружать автосохраненный сеанс перед открытием любого другого файла", 
    "Always hide the video preview window when loading a session" : u"Всегда скрывать окно предварительного просмотра видео при загрузке сеанса",
    "Don't preview when loading a session" : u"Не показывать видеопросмотр при загрузке сеанса",
    "Backup session periodically (minutes)" : u"Период создания резервной копии (в минутах)",
    "Backup the session every X minutes, if X > 0" : u"Создавать резервную копию сеанса каждые X минут, если X > 0",
    "Backup session when previewing" : u"Создавать резервную копию при предпросмотре видео",
    "If checked, the current session is backed up prior to previewing any new script" : u"Если отмечено, то текущий сеанс сохраняется перед предпросмотром видео любого скрипта",
    "Prompt to save a script before previewing (inactive if previewing with unsaved changes)" : u"Предлагать сохранить скрипт перед предпросмотром видео (неактивно при предпросмотре с не сохраненными изменениями)", 
    "Prompt to save when previewing" : u"Предлагать сохранить перед предпросмотром видео", 
    "Create a temporary preview script with unsaved changes when previewing the video" : u"Создавать временный скрипт с несохранёнными изменениями при предпросмотре видео.", 
    "Preview scripts with unsaved changes" : u"Предпросмотр скриптов с несохранёнными изменениями",
    "When closing a tab, don't prompt to save the script if it doesn't already exist on the filesystem" : u"При закрытии вкладки не предлагать сохранить скрипт, если он еще не существует в виде отдельного файла",
    "When closing tab, don't prompt to save scripts without file" : u"При закрытии вкладки не предлагать сохранять скрипты без файла",
    "Prompt to save each script with unsaved changes when exiting the program" : u"Предлагать сохранить каждый скрипт с несохраненными изменениями при выходе из программы",
    "Prompt to save scripts on program exit" : u"Предлагать сохранять скрипты при выходе",
    "Only with existing script" : u"Только с существующим скриптом",
    "When exiting the program, don't prompt to save the script if it doesn't already exist on the filesystem" : u"При выходе из программы не предлагать сохранять скрипт, если он еще не существует в виде отдельного файла",
    "Auto: CRLF on Windows and LF on *nix for new scripts, existing scripts keep their current line endings" : u"Авто: CRLF в Windows и LF в *nix для новых скриптов, в существующих скриптах сохраняются текущие окончания строк.",
    "Force CRLF" : u"Принудительно CRLF",
    "Force LF" : u"Принудительно LF",
    "Line endings" : u"Окончания строк",
    "Auto" : u"Авто",
    "Save and read AvsPmod-specific markings (user sliders, toggle tags, etc) as a commented section in the *.avs file" : u"Сохранение и чтение специфичных отметок AvsPmod (пользовательских ползунков, тегов переключения и т.п.) в виде комментария в файле avs",
    "Save or read avs scripts with AvsPmod markings" : u"Сохранение или чтение скриптов avs со спец. отметками AvsPmod",
    "Do not remove toggle tags and disabled filters.\nCan make the saved script unreadable for other programs if You not use #> in front of the toggle tag: #>[sharp=0]" : u"Не удаляйте теги переключения и отключенные фильтры.\nЭто может сделать сохраненный скрипт нечитаемым в других программах, если Вы не используете #> перед тегом переключения: #>[sharp=0]",
    "Save toggle tags within the script ( read the hint! )" : u"Сохранять теги переключения в скрипте (прочтите подсказку!)",
    "Start dialogs on the last used directory" : u"Открывать диалоговые окна на последнем использованном каталоге",
    "If unchecked, the script's directory is used" : u"Если не отмечено, то используется каталог скрипта",
    "Start save image dialogs on the last used directory" : u"Открывать диалоговое окно сохранения изображения на последнем использованном каталоге",
    "Choose a default pattern for image filenames. %s -> script title, %06d -> frame number padded to six digits" : u"Выберите шаблон по умолчанию для имен файлов изображений. %s - заголовок скрипта, %06d - номер кадра до шести цифр",
    "Default image filename pattern" : u"Шаблон имени файла изображения по умолчанию",
    "Ask for JPEG quality" : u"Показать настройки качества JPEG",
    "When saving a JPEG image, prompt for the quality level. Use the value from the last time if not checked" : u"При сохранении изображения в формат JPEG показать настройки качества. Если не отмечено, используется значение при последнем разе использования",
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
    "Tab change loads bookmarks from script or tab *" : u"При смена вкладки загружать из скрипта закладки или метки *",
    "Warn if tab bookmarks and from script reading bookmarks different." : u"Предупреждать, если в вкладке и в скрипте отличаются закладки",
    "Warning tab bookmarks different" : u"Предупреждать о разных закладках",
    "Only allow a single instance of AvsPmod" : u"Разрешить одновременный запуск нескольких копий AvsPmod",
    "Show warning at startup if there are dlls with bad naming in default plugin folder" : u"Показывать предупреждение при запуске, если в папке плагинов по умолчанию есть библиотеки с неправильным именем",
    "Show warning for bad plugin naming at startup" : u"Показывать предупреждение о неправильном имени плагина при запуске",
    "Bookmark jump" : u"Переход на закладку",
    "Custom jump" : u"Пользовательский переход",
    "Mouse browse buttons" : u"Обзор кнопками мышки",
    "Mouse browse buttons (forward/backward) on video and script window\nIf 'Tab change' and tab count less than 2, 'Bookmark jump' is used\nIf 'Tab change' press CTRL or left mouse and 'Bookmark jump' is used\nIf 'Bookmark jump', vice versa" : u"Обзор с помощью кнопок мышки (вперед/назад) в окне видео и скрипта\nЕсли 'Смена вкладки' и количество вкладок меньше 2, используется 'Переход по закладкам'\nЕсли 'Смена вкладки', то удерживайте CTRL или левую кнопку мыши для 'Переход по закладкам'\nЕсли 'Закладка меняется', наоборот.",
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
    "Misc 2" : u"Разное 2",
    "AvsPmod DPI scaling *" : u"Масштабирование DPI в AvsPmod *",
    "DPI scaling overall only manually*" : u"Масштабировать DPI только вручную *",
    "Do not do overall DPI scaling automatically" : u"Не выполнять автоматическое масштабирование DPI",
    "Disable DPI awareness*" : u"Отключить распознавание DPI *",
    "Only disable it if you using 100% system zoom. Program is zoomed by the system and set DPI values." : u"Отключите его, только если вы используете 100% системный масштаб. Программа масштабируется системой и устанавливает значения DPI.",
    "DPI scaling overall:*" : u"Общий масштаб DPI: *",
    "Manually adjust dpi scaling overall (10 % steps). For 150 % DPI set value 5" : u"Вручную отрегулируйте масштабирование DPI в целом (с шагом 10%). Для 150% DPI установите значение 5",
    "Additional adjust the video controls (10 % steps)" : u"Дополнительная настройка элементов управления видео (шаг 10%)",
    "DPI scaling video controls:*" : u"Масштаб DPI элементов управления видео: *",
    "Additional adjust the script window tabs (10 % steps)" : u"Дополнительная настройка вкладок окна скрипта (шаг 10%)",
    "DPI scaling main tabs:*" : u"Масштаб DPI основных вкладок: *",
    "Additional adjust the statusbar (10 % steps)" : u"Дополнительная настройка строки состояния (шаг 10%)",
    "DPI scaling statusbar:*" : u"Масштаб DPI строки состояния",
    "Advanced settings" : u"Продвинутые настройки",
    "Auto pc" : u"", # New in v2.6.9.8
    "Auto tv" : u"", # New in v2.6.9.8
    "Auto: Resolution based" : u"", # New in v2.6.9.8
    "Default YUV -> RGB conversion" : u"", # New in v2.6.9.8
    "PC.601" : u"", # New in v2.6.9.8
    "PC.709" : u"", # New in v2.6.9.8
    "Rec.601" : u"", # New in v2.6.9.8
    "Rec.709" : u"", # New in v2.6.9.8
    "Sets the sensitivity of the mouse movement on the status bar, for timeline range move (with or without Shift), lower value more movement" : u"", # New in v2.6.9.8
    "Timeline move on status bar sensitivity:" : u"", # New in v2.6.9.8
    "1 number" : u"", # New in v2.6.9.8
    "4 numbers" : u"", # New in v2.6.9.8
    "9 numbers" : u"", # New in v2.6.9.8
    "How many additional numbers should be displayed in the timeline when a range has been set" : u"", # New in v2.6.9.8
    "Timeline range numbers count:" : u"", # New in v2.6.9.8
    "After creating a new clip, show available memory in the status bar if memory is less than x MB" : u"После создания/обновления предпросмотра видео показать в строке состояния доступную системную память, если она меньше x МБ",
    "Show available system memory (0 disabled)" : u"Показать доступную системную память (0 отключено)",
    "Delay before thread progress dialog appears" : u"", # New in v2.6.9.8
    "If accessing Avisynth in threads enabled, this setting determines the delay in seconds before the dialog appears. Can be double (clip, frame)" : u"", # New in v2.6.9.8
    "If the mouse wheel does not work in the editor\nor you want another scroll rate. 1 to 5 lines to scroll\nFor enable/disable you must restart the program" : u"", # New in v2.6.9.8
    "Mouse wheel scroll rate on editor (0 disabled)*" : u"", # New in v2.6.9.8
    "Add tab to group" : u"Добавить вкладку в группу",
    "Extend selection to line down position" : u"Расширить выделение до нижней строки",
    "Scroll down" : u"Прокрутить вниз",
    "Extend rectangular selection to line down position" : u"Расширить прямоугольное выделение до нижней строки",
    "Extend selection to line up position" : u"Расширить выделение до верхней строки",
    "Scroll up" : u"Прокрутить вверх",
    "Extend rectangular selection to line up position" : u"Расширить прямоугольное выделение до верхней строки",
    "Go to previous paragraph" : u"Перейти к предыдущему абзацу",
    "Extend selection to previous paragraph" : u"Расширить выделение до предыдущего абзаца",
    "Go to next paragraph" : u"Перейти к следующему абзацу",
    "Extend selection to next paragraph" : u"Расширить выделение до следующего абзаца",
    "Extend selection to previous character" : u"Расширить выделение до предыдущего символа",
    "Go to previous word" : u"Перейти к предыдущему слову",
    "Extend selection to previous word" : u"Расширить выделение до предыдущего слова",
    "Extend rectangular selection to previous character" : u"Расширить прямоугольное выделение до предыдущего символа",
    "Extend selection to next character" : u"Расширить выделение до следующего символа",
    "Go to next word" : u"Перейти к следующему слову",
    "Extend selection to next word" : u"Расширить выделение до следующего слова",
    "Extend rectangular selection to next character" : u"Расширить прямоугольное выделение до следующего символа",
    "Go to previous word part" : u"Перейти к предыдущей части слова",
    "Extend selection to previous word part" : u"Расширить выделение до предыдущей части слова",
    "Go to next word part" : u"Перейти к следующей части слова",
    "Extend selection to next word part" : u"Расширить выделение до следующей части слова",
    "Extend selection to start of line" : u"Расширить выделение до начала строки",
    "Go to start of document" : u"Перейти в начало документа",
    "Extend selection to start of document" : u"Расширить выделение до начала документа",
    "Go to start of line" : u"Перейти в начало строки",
    "Extend selection to end of line" : u"Расширить выделение до конца строки",
    "Go to end of document" : u"Перейти в конец документа",
    "Extend selection to end of document" : u"Расширить выделение до конца документа",
    "Go to end of line" : u"Перейти в конец строки",
    "Extend selection to previous page" : u"Расширить выделение на предыдущую страницу",
    "Extend rectangular selection to previous page" : u"Расширить прямоугольное выделение до предыдущей страницы",
    "Extend selection to next page" : u"Расширить выделение до следующей страницы",
    "Extend rectangular selection to next page" : u"Расширить прямоугольное выделение до следующей страницы",
    "Delete to end of word" : u"Удалить до конца слова",
    "Delete to end of line" : u"Удалить до конца строки",
    "Delete back" : u"Удалить обратно",
    "Delete to start of word" : u"Удалить до начала слова",
    "Delete to start of line" : u"Удалить до начала строки",
    "Cancel autocomplete or calltip" : u"Отменить автозавершение или подсказку",
    "Indent selection" : u"Вставить отступ",
    "Unindent selection" : u"Убрать отступ",
    "Newline" : u"Новая строка",
    "Zoom in" : u"Увеличить масштаб",
    "Zoom out" : u"Уменьшить масштаб",
    "Reset zoom level to normal" : u"Сбросить масштаб до нормального",
    "Line cut" : u"Вырезать строку",
    "Line delete" : u"Удалить строку",
    "Line copy" : u"Копировать строку",
    "Transpose line with the previous" : u"Перенести строку с предыдущей",
    "Line or selection duplicate" : u"Дублировать строку или выделение",
    "Convert selection to lowercase" : u"Преобразовать выделение в нижний регистр",
    "Convert selection to uppercase" : u"Преобразовать выделение в верхний регистр",
    "Resolution-based" : u"На основе разрешения",
    "BT.709" : u"", # New in v2.3.0
    "BT.601" : u"", # New in v2.3.0
    "TV levels" : u"TV уровни",
    "PC levels" : u"PC уровни",
    "Progressive" : u"Прогрессивный",
    "Interlaced" : u"Чересстрочный",
    "Swap UV" : u"Поменять местами U V",
    "25%" : u"", # New in v1.3.8
    "50%" : u"", # New in v1.3.8
    "100% (normal)" : u"100% (нормальный)",
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
    "Create a new tab from template **" : u"", # New in v2.6.9.8
    "New tab from template" : u"", # New in v2.6.9.8
    "Open an existing script" : u"Открыть существующий скрипт",
    "Open..." : u"Открыть...",
    "Reopen the last closed tab" : u"Открыть последнюю закрытую вкладку",
    "Undo close tab" : u"Отменить закрытие вкладки",
    "Close tab" : u"Закрыть вкладку",
    "Close the current tab" : u"Закрыть текущую вкладку",
    "Close all tabs" : u"Закрыть все вкладки",
    "Close every tab" : u"Закрыть каждую вкладку",
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
    "Export HTML" : u"Экспорт в HTML",
    "&Print script" : u"&Распечатать скрипт",
    "Configure page for printing" : u"Настройка печатаемой страницы",
    "Page setup" : u"Настройка страницы",
    "Include the script filename and page number at the top of each page" : u"Указывать имя файла скрипта и номер страницы вверху каждой печатаемой страницы.",
    "Print header" : u"Печать заголовка",
    "Word-wrap long lines" : u"Перенос длинных строк",
    "Apply the current zoom to the output" : u"Применить текущий масштаб к печатаемому скрипту",
    "Use zoom" : u"Использовать масштабирование",
    "Display print preview" : u"Показать предпросмотр печати",
    "Print preview" : u"Предпросмотр печати",
    "&Print" : u"Распечатать",
    "Print to printer or file" : u"Распечатать на принтере или в файл",
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
    "Previously selected tab" : u"", # New in v2.6.9.8
    "Toggle between the last two selected tabs" : u"", # New in v2.6.9.8
    "Show the scrap window" : u"Показать/Скрыть окно заметок",
    "Clear file history" : u"", # New in v2.6.9.8
    "Clear the recent file list" : u"", # New in v2.6.9.8
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
    "Find previous" : u"Найти предыдущий",
    "Find the previous instance of given text" : u"Найти предыдущий образец заданного текста",
    "Open a replace text dialog box" : u"Открыть диалоговое окно замены текста",
    "Replace..." : u"Заменить...",
    "Replace next" : u"Заменить далее",
    "Replace the next instance of given text" : u"Заменить следующий образец заданного текста",
    "Select All" : u"Выбрать всё",
    "Select all the text" : u"Выбрать весь текст",
    "&Insert" : u"&Вставить",
    "Expand a snippet tag, or select a snippet from the list" : u"Развернуть тег отрывка или выбрать отрывок из списка",
    "Insert snippet" : u"Вставить отрывок",
    "Choose a source file to insert into the text" : u"Выберите исходный файл для вставки в текст",
    "Insert source..." : u"Вставить источник...",
    "Get a filename from a dialog box to insert into the text" : u"Получить имя файла из диалогового окна для вставки в текст",
    "Insert filename..." : u"Вставить имя файла...",
    "Choose a plugin file to insert into the text" : u"Выберите файл плагина для вставки в текст",
    "Insert plugin..." : u"Вставить плагин...",
    "Insert a user-scripted slider into the text" : u"Вставка пользовательского ползунка в текст",
    "Insert user slider..." : u"Вставить пользовательский ползунок...",
    "Insert a tag which indicates a separator in the user slider window" : u"Вставить метку, обозначающую разделитель, в пользовательское окно ползунка",
    "Insert user slider separator" : u"Вставить разделитель пользовательского ползунка",
    "Insert the current frame number into the text" : u"Вставить номер текущего кадра в текст",
    "Add tags surrounding the selected text for toggling with the video preview" : u"Добавить метки вокруг выделенного текста для переключения с предпросмотром видео",
    "Tag selection for toggling..." : u"Выбор метки для переключения...",
    "Clear all tags" : u"Убрать все метки",
    "Clear all toggle tags from the text" : u"Убрать все метки переключения из текста",
    "Add Preview filter surrounding the selected lines" : u"Добавить фильтр предпросмотра вокруг выбранных строк",
    "Preview filter" : u"Предпросмотр фильтра",
    "Indent the selected lines" : u"Увеличить отступ выбранных строк",
    "Unindent the selected lines" : u"Уменьшить отступ выбранных строк",
    "Block comment" : u"Закомментировать строку",
    "Comment or uncomment selected lines" : u"Закомментировать или раскомментировать выбранные строки",
    "Comment at start of a text style or uncomment" : u"Комментирование или раскомментирование в начале слова",
    "Style comment" : u"Закомментировать от курсора",
    "Toggle current fold" : u"Свернуть/Развернуть текущий блок",
    "Toggle the fold point On/OFF at the current line" : u"Свернуть/Развернуть блок скрипта на текущей строке",
    "Toggle all fold points On/OFF" : u"Свернуть/Развернуть все блоки в скрипте",
    "Toggle all folds" : u"Свернуть/Развернуть все блоки",
    "Toggle text wrap" : u"Включить/Отключить перенос строк",
    "Toggle text wrap On/OFF" : u"Включить/выключить перенос текста",
    "&AviSynth function" : u"&Функции AviSynth",
    "Show list of filternames matching the partial text at the cursor" : u"Показать список фильтров, соответствующих части текста под курсором",
    "Autocomplete all" : u"Автозавершить все",
    "Disregard user's setting, show full list of filternames matching the partial text at the cursor" : u"Игнорировать настройки пользователя, показывать полный список фильтров, соответствующих частичному тексту под курсором",
    "Autocomplete parameter/filename" : u"Автозавершить параметр / имя файла",
    "If the first characters typed match a parameter name, complete it. If they're typed on a string, complete the filename" : u"Если первые набранные символы соответствуют имени параметра, то заполнить его. Если они набраны в строке, то заполнить именем файла",
    "Show calltip" : u"Показать подсказку", 
    "Show the calltip for the filter (only works if cursor within the arguments)" : u"Показать подсказку по фильтру (работает только если курсор над аргументами функции)", 
    "Show function definition" : u"Показать определение функции",
    "Show the AviSynth function definition dialog for the filter" : u"Для фильтра показать диалог определения функции AviSynth",
    "Filter help file" : u"Файл справки по фильтру", 
    "Run the help file for the filter (only works if cursor within the arguments or name is highlighted)" : u"Показать файл справки по фильтру (работает только если курсор над аргументами или имя подсвечено)", 
    "Include functions defined in the current script in the filter database, only for this tab" : u"Включить функции, определенные в текущем скрипте, в базу данных фильтров, только для текущей вкладки",
    "Parse script for function definitions" : u"Проанализировать скрипт для определений функций",
    "&Miscellaneous" : u"&Разное",
    "Move line up" : u"Передвинуть строку вверх", 
    "Move the current line or selection up by one line" : u"Передвинуть текущую строку или выбранное на одну строку вверх", 
    "Move line down" : u"Передвинуть строку вниз", 
    "Move the current line or selection down by one line" : u"Передвинуть текущую строку или выбранное на одну строку вниз", 
    "Copy the current script without any AvsP markings (user-sliders, toggle tags) to the clipboard" : u"Копировать в буфер обмена текущий скрипт без спец. отметок AvsP (ползунков, меток)", 
    "Copy unmarked script to clipboard" : u"Копировать неразмеченный скрипт в буфер обмена", 
    "Copy avisynth error to clipboard" : u"Скопируйте ошибку AviSynth в буфер обмена",
    "Copy the avisynth error message shown on the preview window to the clipboard" : u"Копировать в буфер обмена сообщение об ошибке AviSynth, отображаемое в окне предпросмотра видео",
    "Set selection as display filter..." : u"", # New in v2.6.9.8
    "Shows the display filter dialog with the selected text" : u"", # New in v2.6.9.8
    "&Video" : u"&Видео",
    "Bookmarks" : u"Закладки",
    "Bookmarks to script" : u"Закладки в скрипт",
    "Bookmarks from script" : u"Закладки из скрипта",
    "Add/Remove bookmark" : u"Добавить/Удалить закладку",
    "Mark the current frame on the frame slider" : u"Отметить текущий кадр на ползунке кадров",
    "Clear tab bookmarks" : u"Очистить вкладку от закладок",
    "Clears the current tab bookmarks" : u"Удаляет текущую вкладку от закладок",
    "Clear all bookmarks Globally" : u"Очистить все закладки, глобально",
    "Clears all bookmarks, clears also all tab bookmarks" : u"Очистить все закладки, также очищает все вкладки от закладок",
    "Titled &bookmarks" : u"Заглавия &закладки",
    "Move the nearest titled bookmark to the current position. A historic title will be restored if it matches the condition." : u"Переместите ближайшую озаглавленную закладку в текущее положение. Изначальное заглавие будет восстановлено, если оно соответствует условию.",
    "Move titled bookmark" : u"Переместить озаглавленную закладку",
    "Restore all historic titles" : u"Восстановить все первоначальные заглавия",
    "Restore historic titles" : u"Восстановить первоначальные заглавия",
    "Clear all historic titles" : u"Очистить все первоначальные заглавия",
    "Clear historic titles" : u"Очистить первоначальные заглавия",
    "Generate titles for untitled bookmarks by the pattern - 'Chapter %02d'" : u"Генерировать заглавия для безымянных закладок по шаблону - 'Chapter %02d'", # New in v2.2.1
    "Set title (auto)" : u"Озаглавить (авто)",
    "Edit title for bookmarks in a list table" : u"Редактировать список заглавий закладок",
    "Set title (manual)" : u"Озаглавить (вручную)",
    "Remove all title" : u"Удалить все заглавия",
    "Remove all title from the bookmarks" : u"Удалить все заглавия из закладок",
    "Not include this tab on any group" : u"Не включать эту вкладку ни в одну группу",
    "Add tab to this group" : u"Добавить вкладку в эту группу",
    "Clear current tab group" : u"Очистить текущую группу вкладок",
    "Clear all tab groups" : u"Очистить все группы вкладок",
    "Apply offsets" : u"Применить смещение",
    "Use the difference between showed frames when the tabs were added to the group as offsets" : u"Использовать разницу между показанными кадрами, когда вкладки были добавлены в группу как смещённые",
    "Offset also bookmarks" : u"Также смещать закладки",
    "Apply the offset also to the currently set bookmarks" : u"Также применять смещение к текущим установленным закладкам",
    "&Navigate" : u"&Навигация по видео",
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
    "&Play video" : u"&Проиграть видео",
    "Play/pause video" : u"Проигрывать/приостановить видео",
    "Double the current playback speed" : u"Удвоить текущую скорость проигрывания",
    "Increment speed" : u"Ускорить проигрывание",
    "Decrement speed" : u"Замедлить проигрывание",
    "Halve the current playback speed" : u"Уменьшить вдвое текущую скорость проигрывания",
    "Set the playback speed to the script frame rate" : u"Установите скорость проигрывания в соответствии с частотой кадров скрипта",
    "Normal speed" : u"Нормальная скорость",
    "Play the video as fast as possible without dropping frames" : u"Проигрывать видео как можно быстрее без потери кадров",
    "Maximum speed" : u"Максимальная скорость",
    "Loop playback for trim editor selections or at the end of the clip" : u"Циклическое проигрывание для выбора редактора обрезки или в конце клипа",
    "Play loop" : u"Зациклить проигрывание",
    "Use a separate thread for playback. If avisynth threads used, playback uses also threads" : u"Использовать отдельный поток для проигрывания. Если используются многопоточность AviSynth, то при проигрывании так-же используется многопоточность",
    "Use separate thread" : u"Использовать отдельный поток",
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
    "Add bookmark to trim intersections" : u"Добавить закладки для обрезки пересечений",
    "Mark trim points" : u"Отметьте точки обрезки",
    "Save the selections into the script" : u"Сохранить выделенное в скрипте",
    "Selections to script" : u"Выбрать в скрипте",
    "Read the selections from the script" : u"Прочитайте выбранные параметры из скрипта",
    "Selections from script" : u"Выбрать из скрипта",
    "Clear tab selections" : u"Очистить выбранные вкладки",
    "Clear tab trim editor selections (hide the trim editor if visible)" : u"Очистить выбранные вкладки в редакторе обрезки (скрыть редактор обрезки, если он виден)",
    "Clear all selections Globally" : u"Очистить всё выбранное, глобально",
    "Clear all the tab trim editor selections (hide the trim editor if visible)" : u"Очистить все выбранные вкладки в редакторе обрезки (скрыть редактор обрезки, если он виден)",
    "Timeline range" : u"Диапазон временной шкалы",
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
    "&Display" : u"&Отображение",
    "Enable/Disable the display filter" : u"", # New in v2.6.9.8
    "Display filter" : u"", # New in v2.6.9.8
    "Select display filter..." : u"", # New in v2.6.9.8
    "Select the display filter from template" : u"", # New in v2.6.9.8
    "Edit current display filter..." : u"", # New in v2.6.9.8
    "Edit the current display filter" : u"", # New in v2.6.9.8
    "&Flip" : u"Повернуть",
    "Flip video preview upside down" : u"Перевернуть предпросмотр видео снизу вверх",
    "Flip video preview from left to right" : u"Перевернуть предпросмотр видео слева направо",
    "&YUV -> RGB" : u"", # New in v2.2.1
    "Swap chroma channels (U and V)" : u"Поменять местами каналы цветности U и V",
    "Get the coefficients from source or script, if the matrix available" : u"Получить коэффициенты из источника или скрипта, если матрица доступна",
    "Read from source or script" : u"Считывать из исходного кода или сценария",
    "Set matrix default value (options) if matrix not found" : u"", # New in v2.6.9.8
    "Reset matrix if not found" : u"", # New in v2.6.9.8
    "Use BT.709 coefficients for HD, BT.601 for SD" : u"Используйте коэффициенты BT.709 для HD, BT.601 для SD",
    "Use BT.709 coefficients" : u"Использовать коэффициент BT.709",
    "Use BT.601 coefficients" : u"Использовать коэффициент BT.601",
    "Use limited range (default)" : u"Использовать ограниченный диапазон яркости и цвета (по умолчанию)",
    "Use full range" : u"Использовать полный диапазон яркости и цвета",
    "For YV12 only, assume it is progressive (default)" : u"Только для YV12: считать его прогрессивный (по умолчанию)",
    "For YV12 only, assume it is interlaced" : u"Только для YV12: считать его чересстрочный.",
    "Current matrix to script" : u"Текущая матрица в скрипте",
    "Write the current matrix to script. If no matrix found this matrix is used" : u"Записать текущую матрицу в скрипт. Если матрица не найдена, используется данная матрица",
    "Read the matrix now" : u"Прочитать матрицу",
    "Try to get the matrix from source or script" : u"Пробовать получить матрицу из источника или скрипта",
    "Globally to default" : u"Глобально по умолчанию",
    "Reset all scripts to Resolution-based" : u"Сбросить все скрипты к основному разрешению",
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
    "Use RGB {hex_value}" : u"Использовать RGB {hex_value}",
    "Use a custom color" : u"Использовать свой цвет",
    "Custom" : u"Пользовательский",
    "Choose the color used if 'custom' is selected" : u"Выберите цвет, который будет использоваться, если выбран 'Пользовательский'", # New in v2.5.1
    "Select custom color" : u"Выбрать свой цвет",
    "Save image as..." : u"Сохранить изображение как...",
    "Save the current frame as image file. If you not change the frame number, Quick save image uses the name." : u"Сохранить текущий кадр как файл изображения. Если вы не измените номер кадра, то быстрое сохранение изображения будет использовать это имя.",
    "Quick save image" : u"Быстрое сохранение изображения",
    "Save the current frame with a default filename, overwriting the file if already exists. Press CTRL to reset the default name formatting" : u"Сохранить текущий кадр с именем по умолчанию, перезаписав файл, если он уже существует. Нажмите CTRL, чтобы сбросить форматирование имени по умолчанию",
    "Copy image to clipboard" : u"Копировать изображение в буфер обмена",
    "Copy the current frame to the clipboard as a bitmap" : u"Копировать текущий кадр в буфер обмена как растровое изображение",
    "Force the script to reload and refresh the video frame" : u"Перезагрузить скрипт и обновить видео кадр",
    "Refresh preview" : u"Обновить предпросмотр видео",
    "Release all open videos from memory" : u"Выгрузить все открытые видео из памяти",
    "Release all videos from memory" : u"Выгрузить всё видео из памяти",
    "Snapshot" : u"Снимок",
    "Take snapshot 1" : u"Сделать снимок 1",
    "Make bitmap and script snapshot" : u"Сделать снимок растрового изображения и скрипта",
    "Take snapshot 2" : u"Сделать снимок 2",
    "Show or hide snapshot 1" : u"Показать или скрыть снимок 1",
    "Show/hide snapshot 1" : u"Показать/скрыть снимок 1",
    "Show or hide snapshot 2" : u"Показать или скрыть снимок 2",
    "Show/hide snapshot 2" : u"Показать/скрыть снимок 2",
    "Copy snap shot 1 to new tab" : u"Скопировать снимок 1 в новую вкладку",
    "New tab from snapshot 1" : u"Новая вкладка из снимка 1",
    "Copy snap shot 2 to new tab" : u"Скопировать снимок 2 в новую вкладку",
    "New tab from snapshot 2" : u"Новая вкладка из снимка 2",
    "Automatically takes snapshot 2 on clip refresh" : u"", # New in v2.6.9.8
    "Auto take snapshot 2" : u"", # New in v2.6.9.8
    "Clear tab snapshots" : u"Очистить снимки вкладок",
    "Clears the current tab snapshots" : u"Очистить снимки текущей вкладки",
    "Clear all snapshots Globally" : u"Очистить все снимки, глобально",
    "Clears all snapshots Globally" : u"Очистить все снимки, глобально",
    "Preview filter off" : u"Отключить предпросмотр фильтра",
    "Preview filter 1" : u"Предпросмотр фильтра 1",
    "1" : u"", # New in v2.6.6.0
    "Preview filter 2" : u"Предпросмотр фильтра 2",
    "2" : u"", # New in v2.6.6.0
    "Preview filter 3" : u"Предпросмотр фильтра 3",
    "3" : u"", # New in v2.6.6.0
    "Preview filter 4" : u"Предпросмотр фильтра 4",
    "4" : u"", # New in v2.6.6.0
    "Preview filter 5" : u"Предпросмотр фильтра 5",
    "5" : u"", # New in v2.6.6.0
    "Save preview filters" : u"Сохранить предпросмотр фильтра",
    "Save preview filters for later use" : u"Сохранить предпросмотр фильтра для последующего использования",
    "Write all preview filters to script" : u"Записать все предпросмотры фильтров в скрипт",
    "Write all to script" : u"Записать все в скрипт",
    "Write to script" : u"Записать в скрипт",
    "Write Preview filter to script" : u"Записать предпросмотр фильтра в скрипт",
    "Shows the selected and optional the next or previous tab in one view (video width and height must be the same)" : u"Показывать выбранную и следующую/предыдущую вкладку (по выбору) в одном окне предпросмотра видео (ширина и высота видео должны быть одинаковыми)",
    "Split View on/off" : u"Включение/выключение разделения просмотра",
    "Expands the left shift area of the video window" : u"Расширить область сдвига влево для видеоокна",
    "Toggle extended left move" : u"Переключить расширенное смещение влево",
    "Save/Restore last view position and zoom factor on tab change" : u"Сохранить/Восстановить последнее положение просмотра и масштабирования при смене вкладки",
    "Save view pos on tab change" : u"Сохранить позицию видеопросмотра при смене вкладки",
    "Additional" : u"Дополнительно",
    "Show/Hide the preview" : u"Показать/Скрыть видеопросмотр",
    "Toggle the video preview" : u"Показать/Скрыть окно видеопросмотра",
    "Switch focus between the video preview and the text editor" : u"Переключить фокус между окнами видеопросмотра и текстового редактора",
    "Switch video/text focus" : u"Переключить фокус на окон видео/текст",
    "Show/hide the slider sidebar (double-click the divider for the same effect)" : u"Показать/Скрыть колонку ползунков (или двойной щелчок на разделителе)", 
    "Toggle the slider sidebar" : u"Переключить колонку ползунков", 
    "Toggle preview placement" : u"Переключить расположение окна видеопросмотра",
    "When not using a separate window for the video preview, toggle between showing it at the bottom (default) or to the right" : u"Если для предпросмотра видео не используется отдельное окно, то переключить его положение вниз (по умолчанию) или справа",
    "Tools" : u"Инструменты",
    "Request every video frame once (analysis pass for two-pass filters)" : u"Запрашивать каждый видеокадр один раз (анализ для двухпроходных фильтров)",
    "Run analysis pass" : u"Выполнить пробный проход",
    "External player" : u"Внешний проигрыватель",
    "Play the current script in an external program" : u"Проиграть текущий скрипт во внешней программе",
    "External tool arg1" : u"Внешний инструмент arg1",
    "Run the current script with an external program and arg1" : u"Выполнить текущий скрипт во внешней программе с arg1",
    "External tool arg2" : u"Внешний инструмент arg2",
    "Run the current script with an external program and arg2" : u"Выполнить текущий скрипт во внешней программе с arg2",
    "Show/Hide the properties window" : u"", # New in v2.6.9.8
    "Show information about the video in a dialog box" : u"Показать информацию о видео в диалоговом окне",
    "Video information" : u"Информация о видео",
    "&Options" : u"&Параметры",
    "Always on top" : u"Всегда поверх",
    "Keep this window always on top of others" : u"Удерживать это окно всегда поверх других",
    "If the video preview is detached, keep it always on top of other windows" : u"Если предварительный просмотр видео отключен, то всегда удерживать его поверх других окон.",
    "Video preview always on top" : u"Окно видеопросмотра всегда сверху",
    "Disable video preview" : u"Отключить видеопросмотр", 
    "If checked, the video preview will not be shown under any circumstances" : u"Если отмечено, видео просмотр не будет показан ни при каких обстоятельствах", 
    "Hide the video window scrollbars" : u"Скрыть полосу прокрутки окна предварительный просмотр видео",
    "Hide video window scrollbars" : u"Скрыть полосу прокрутки окна видеопросмотра",
    "Accessing AviSynth in threads" : u"Разрешить доступ AviSynth к многопоточности",
    "Use threads when accessing avisynth (load/release clip and get frame)" : u"Разрешить AviSynth использовать все потоки/ядра процессора (например для загрузки/выгрузки клипа или получении кадра)",
    "For info read the readme_threads.txt" : u"", # New in v2.6.9.8
    "Use advanced frame thread" : u"", # New in v2.6.9.8
    "AvsPmod should normally be closed after a thread has been canceled by the user. This option tries to assign the clip to the script after the thread has internaly finished." : u"Обычно AvsPmod следует закрывать после того, как поток был отменен пользователем. Эта опция пытается подгрузить клип скрипту после того, как поток внутрисистемно был завершен.",
    "On cancel assign the clip later" : u"При отмене обработки видео, загрузить его позже",
    "Associate .avs files with AvsPmod" : u"Ассоциировать avs файлы с AvsPmod",
    "Configure this computer to open .avs files with AvsP when double-clicked. Run again to disassociate" : u"Открывать двойном щелчком файлы avs с помощью AvsP",
    "Edit the various AviSynth script fonts and colors" : u"Редактировать шрифты и цвета текста для скриптов в AviSynth", 
    "Fonts and colors..." : u"Шрифты и цвета...", 
    "Make fonts && colors backup" : u"Сделать резервную копию шрифтов и цветов",
    "Make script fonts and colors backup" : u"Сделать резервную копию шрифтов и цветов",
    "Load fonts && colors backup" : u"Загрузить резервную копию шрифтов и цветов",
    "Restores script fonts and colors from backup" : u"Восстанавливает шрифты и цвета из резервной копии",
    "AviSynth function definition..." : u"Определения функций AviSynth...", 
    "Edit the extension-based templates for inserting sources" : u"Редактировать шаблоны для вставки источников на основе расширений файлов",
    "Extension templates..." : u"Шаблоны расширений файлов...", 
    "Display filters..." : u"", # New in v2.6.9.8
    "Edit display filters" : u"", # New in v2.6.9.8
    "Apply filters..." : u"", # New in v2.6.9.8
    "Edit insertable timeline selections filters" : u"", # New in v2.6.9.8
    "Snippets..." : u"Отрывки текста...",
    "Edit insertable text snippets" : u"Редактировать вставляемые отрывки текста",
    "Configure the program keyboard shortcuts" : u"Настроить сочетания клавиш быстрого выполнения",
    "Keyboard shortcuts..." : u"Горячие клавиши...",
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
    "Open the Preview filter examples" : u"Открыть примеры предпросмотра фильтра",
    "Preview filter example" : u"Пример предпросмотра фильтра",
    "Accessing in threads readme" : u"Доступ к потокам readme",
    "Open the Access in threads readme" : u"Открыть доступ к потокам readme",
    "Apply filters readme" : u"", # New in v2.6.9.8
    "Open the apply filters readme" : u"", # New in v2.6.9.8
    "DPI info" : u"", # New in v2.6.9.8
    "DPI information" : u"Информация о DPI",
    "Displays the available memory in the status bar" : u"Отображает доступный объём память в строке состояния",
    "Show available system memory" : u"Показать доступную системную память",
    "Open Avisynth plugins folder" : u"Откройте папку плагинов AviSynth",
    "Open the avisynth plugins folder, or the last folder from which a plugin was loaded" : u"Откройте папку плагинов AviSynth или последнюю папку, из которой плагин был загружен",
    "Changelog" : u"Список изменений",
    "Open the changelog file" : u"Открыть файл со списком изменений",
    "About this program" : u"Об этой программе",
    "About AvsPmod" : u"Сведения об AvsPmod",
    "Jump back. Right click for options" : u"Перейти назад. Щелкните правой кнопкой мышки, чтобы увидеть параметры",
    "Jump forward. Right click for options" : u"Перейти вперёд. Щелкните правой кнопкой мышки, чтобы увидеть параметры",
    "Play/pause video. Right click for options." : u"Воспроизвести/приостановить видео. Щелкните правой кнопкой мышки, чтобы увидеть параметры",
    "Run the script with an external program" : u"Выполнить скрипт внешней программой",
    "Run the selected tool" : u"Запустить выбранный инструмент",
    "&Tools" : u"&Инструменты",
    "A macro check item" : u"Элемент проверки макроса",
    "A macro radio item" : u"Элемент макро-радио",
    "Run selected macro" : u"Выполнить выбранный макрос",
    "View the readme for making macros" : u"Посмотреть справку по созданию макросов",
    "Open macros folder" : u"Открыть папку макросов",
    "Open the macros folder" : u"Открыть папку макросов",
    "&Macros" : u"Макросы",
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
    "Split View insert tab" : u"Вставка вкладки разделенного вида",
    "Auto preview" : u"Автоматический предпросмотр",
    "Reposition to" : u"Перейти на вкладку",
    "Disable refresh" : u"Отключить обновление",
    "Custom frame range" : u"Пользовательский диапазон кадров",
    "Frame range 30 to n.. or set start,end separated by comma" : u"Количество кадров (от 30 до N), или номера кадров начала и конца (через запятую)",
    "Percent" : u"Процент",
    "Show nothing" : u"", # New in v2.6.9.8
    "Show time" : u"", # New in v2.6.9.8
    "Auto scroll" : u"", # New in v2.6.9.8
    "Auto reset" : u"", # New in v2.6.9.8
    "Custom..." : u"", # New in v2.6.9.8
    "Crop editor" : u"Редактор кадрирования",
    "You can drag the crop regions with the left mouse button when this dialog is visible, cropping the edge closest to the initial mouse click." : u"Когда это окно активно можно указать области подрезки перетаскивая мышку, с нажатой левой кнопкой, по окну предпросмотра видео. Будет обрезана та кромка которая ближе к начальному щелчку мыши.",
    "Auto-crop" : u"Авто-кадрирование",
    "Samples" : u"Образцы",
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
    "Insert Dissolve(trim,) commands: " : u"Вставить команду слияния отрезков - Dissolve(trim,)",
    "Insert Dissolve(clips,) commands: " : u"Вставить команду слияния клипов - Dissolve(clips,)",
    "Use the buttons which appear on the video slider handle to create the frame selections to trim." : u"Используйте кнопки, которые появляются на ручке ползунка видео, чтобы выделить кадры для обрезки.",
    "Hide timeline numbers" : u"", # New in v2.6.9.8
    "Clear" : u"Очистить",
    "The script's directory doesn't exist anymore!" : u"Каталог скрипта больше не существует!",
    "Print Preview" : u"Напечатать предпросмотр",
    "Failed to create print preview" : u"Не удалось создать предпросмотр для печати",
    "Print Error" : u"Ошибка печати",
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
    "Left-click on a selected item or double-click to edit.\n\n*  RED - a historic title, not a real bookmark.\n** Time may be unavailable or incorrect before preview refreshed." : u"Щелкните левой кнопкой мышки по выбранному элементу или дважды щелкните по нему для редактирования.\n\n*  RED (КРАСНЫЙ) - первоначальный заголовок, а не настоящая закладка.\n** Перед обновлением предпросмотра время может быть недоступным или неверным.",
    "Image saved to \"{0}\"" : u"Изображение сохранено в \"{0}\"", # New in v2.5.0
    "No image to save" : u"Нет изображения для сохранения",
    "Error requesting frame {number}" : u"Ошибка при запросе кадра {number}",
    "Couldn't open clipboard" : u"Не удалось открыть буфер обмена",
    "Cannot use crop editor unless bit depth is set to 8" : u"Невозможно использовать редактор кадрирования, если битовая глубина цвета не установлена ​​на 8",
    "No filters found, clear the current saved filters?" : u"Фильтры не найдены, очистить текущие сохраненные фильтры?",
    "Preview filters" : u"Фильтры предпросмотра",
    "Available Memory: {} MB" : u"", # New in v2.6.9.8
    "Snapshot %d" : u"Снимок %d",
    "Error snapshot %d" : u"Ошибка снимка %d",
    "Empty snapshot script" : u"Пустой скрипт для снимка",
    "Display" : u"Отображение",
    "Edit current display filter" : u"", # New in v2.6.9.8
    "YUV -> RGB" : u"", # New in v2.6.8.4
    "Cannot read the matrix. Clip not initialized" : u"Не удалось прочитать матрицу. Клип не инициализирован",
    "Cannot change bit depth while crop editor is open!" : u"Невозможно изменить битовую глубину цвета, пока открыт редактор кадрирования!",
    "Interleaved RGB48" : u"Чередующийся RGB48",
    "Play video" : u"Проиграть видео",
    "Avisynth not returned thread still running.\n{0}" : u"AviSynth не вернул поток, который всё ещё выполняется.\n{0}",
    "Avisynth not returned frame thread still running.\n{0}" : u"AviSynth не вернул поток кадров, который всё ещё выполняется.\n{0}",
    "Avisynth not returned play thread still running.\n{0}" : u"", # New in v2.6.9.8
    "Error loading the script" : u"Ошибка загрузки скрипта",
    "Starting analysis pass..." : u"Запуск пробного прохода...",
    "Average %#.4g fps\nFrame %s/%s (%#.4g fps)" : u"В среднем %#.4g кадр/с\nКадр %s/%s (%#.4g кадр/с)",
    "Finished (%s fps average)\n*** live and let live ***" : u"Завершено (в среднем %s кадр/с)\n*** живи и дай жить другим ***",
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
    "Bookmarks:" : u"Закладки:",
    "Timeline selections:" : u"Выборка временной шкалы:",
    "Could not find the macros folder!" : u"Не удалось найти папку с макросами!",
    "Failed to import the selected tool" : u"Не удалось импортировать выбранный инструмент",
    "Basic (1)" : u"Основные (1)",
    "Override all fonts to use a specified monospace font (no effect on scrap window)" : u"Переопределить все шрифты и использовать одни указанный шрифт (кроме окна заметок)",
    "Use monospaced font:" : u"Использовать один шрифт",
    "Default:" : u"По умолчанию:", 
    "Comment:" : u"Комментарий:", 
    "Comment special extension #>:" : u"Комментарий спец. расширения #>:",
    "Block Comment:" : u"Комментарий блока:",
    "__END__ Comment:" : u"Комментарий  __END__ :",
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
    "Parameter:" : u"Параметр:",
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
    "Fold margin:" : u"Маркер сворачивания блока:",
    "Advanced 2" : u"Продвинутые (2)",
    "Scrap window:" : u"Окно заметок:",
    "Properties window:" : u"", # New in v2.6.9.8
    "Slider window:" : u"Окно ползунка:",
    "Slider window text field:" : u"Текстовое поле окна ползунка:",
    "Slider window default value:" : u"Значение по умолчанию в окне ползунка:",
    "Use another color for the sliders background" : u"Использовать другой цвет для фона ползунков",
    "Use sparate slider background:" : u"Использовать отдельный фон ползунка:",
    "Slider window extras (Snapshot):" : u"Дополнительные возможности окна ползунка (снимок экрана):",
    "Information" : u"Информация",
    "Settings have been read from backup file\n" : u"Настройки были прочитаны из файла резервной копии\n",
    "File extension shouldn't contain dots!" : u"Расширение файла не должно содержать точек!",
    "Insert aborted:" : u"Вставка прервана:",
    "Edit extension-based templates" : u"Редактировать шаблоны базовых расширений",
    "File extension" : u"Расширение файла",
    "Template" : u"Шаблон",
    "This info is used for inserting sources based on file extensions." : u"Эта информация используется для вставки источников на основе расширений файлов.",
    "Any instances of *** in the template are replaced with the filename." : u"В шаблоне любые образцы, вроде ***, заменяются именем файла.",
    "(If you want relative paths instead of the full filename, use [***].)" : u"(Если требуется использовать относительные пути вместо полного имени файла, используйте [***].)",
    "Only alphanumeric and underscores allowed!" : u"Разрешены только буквы, цифры и символ подчеркивания!",
    "Tag" : u"Тег",
    "Snippet" : u"Отрывок",
    "A maximum of 30 entries are allowed!" : u"", # New in v2.6.9.8
    "Edit insertable timeline selection filters" : u"", # New in v2.6.9.8
    "Avisynth filter ( %start %stop is replaced by selection start stop )" : u"", # New in v2.6.9.8
    "%* insert the selected text, %join joins the filters from each selected line" : u"", # New in v2.6.9.8
    "%copy copies the selected text, %> copy this line to all timeline selections" : u"", # New in v2.6.9.8
    "A maximum of 15 entries are allowed!" : u"", # New in v2.6.9.8
    "Edit display filter templates" : u"", # New in v2.6.9.8
    "Avisynth filter (you can run short macro by adding #> at line start" : u"", # New in v2.6.9.8
    "Display filters only affects the display drawing." : u"", # New in v2.6.9.8
    "It is applied as last filter to all tabs." : u"", # New in v2.6.9.8
    "Associating .avs files will write to the windows registry." : u"При ассоциации файлов avs будет выполнена запись в реестр Windows.",
    "Do you wish to continue?" : u"Вы хотите продолжить?",
    "Associate avs files for all users?" : u"Ассоциировать файлы avs для всех пользователей?",
    "Disassociate avs files for all users?" : u"Отменить ассоциацию файлов avs для всех пользователей?",
    " Admin rights are needed." : u"Необходимы права администратора.",
    "Above keys are built-in editing shortcuts. If item is checked,\nit will not be overrided by a menu shortcut in script window." : u"Вышеупомянутые сочетания клавиши по умолчанию встроены в программу. Если действие\nотмечено, то оно не будет заменено пользовательским сочетанием клавиш.",
    "* This shortcut is active only when video window has focus.\n~ This shortcut is active only when script window has focus." : u"* Сочетание клавиш работает только когда активно окно видео.\n~ Сочетание клавиш работает только когда активно окно скрипта.",
    "Could not find the Avisynth plugins folder!" : u"Не удалось найти папку с плагинами AviSynth!",
    "Could not find %(readme)s!" : u"Не могу найти %(readme)s!",
    "Could not find %(changelog)s!" : u"Не могу найти %(changelog)s!",
    "Could not find %(example)s!" : u"Не могу найти %(example)s!",
    "{prog_name} v{version} ({arch})" : u"", # New in v2.5.1
    "AvsP Website" : u"Веб-сайт AvsP",
    "AvsPmod Website" : u"Веб-сайт AvsPmod",
    "Active thread on Doom9's forum" : u"Активная тема обсуждения на форуме Doom9",
    "This program is freeware under the GPL license." : u"Эта программа распространяется бесплатно по лицензии GPL.",
    "Input a frame number or time (hr:min:sec) and hit Enter. Right-click to retrieve from history. Or input a text and set the bookmark title." : u"", # New in v2.6.9.8
    "Drop frames" : u"Пропускать кадры",
    "Half speed" : u"Половина скорости",
    "Custom unit" : u"Пользовательская единица",
    "1 Minute" : u"1 Минута",
    "1 Second" : u"1 Секунда",
    "1 Frame" : u"", # New in v2.6.9.8
    "bookmark highlight color..." : u"цвет подсветки закладки...",
    "selection highlight color..." : u"цвет подсветки выделения...",
    "set colors" : u"", # New in v2.6.9.8
    "bell at bookmarks" : u"отметка закладки",
    "highlight bookmarks" : u"подсветка закладки",
    "Set bookmark title" : u"озаглавить закладку",
    "copy as time" : u"копировать как время",
    "copy" : u"копировать",
    "paste" : u"вставить",
    "clear history" : u"очистить историю",
    "On join filters, the first line must not begin with" : u"", # New in v2.6.9.8
    "Frames: %i" : u"Кадры: %i",
    "Apply filter" : u"", # New in v2.6.9.8
    "All as trim" : u"", # New in v2.6.9.8
    "Add as trim" : u"", # New in v2.6.9.8
    "Timeline to trims" : u"", # New in v2.6.9.8
    "Timeline to clips" : u"", # New in v2.6.9.8
    "Remove" : u"Удалить",
    "Remove all" : u"Удалит всё",
    "Remove all other" : u"Удалить всё остальное",
    "Trim editor..." : u"Редактор обрезки...",
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
    "Bits per component" : u"Биты глубины цвета",
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
    "Display YUV -> RGB conversion" : u"Преобразование YUV -> RGB",
    "Program zoom" : u"Масштаб программы",
    "Bookmark title" : u"Заголовок закладки",
    "Note: The \"\\t\\t\" or \"\\T\\T\" is used to separate the left and right portions of the status bar\n         message." : u"Примечание: \"\\t\\t\" или \"\\T\\T\" используется для разделения левой и правой частей сообщения\nв строке состояния.",
    "Slider update immediately" : u"Немедленное обновление ползунка",
    "A macro is still running. Close anyway?" : u"Макрос все еще выполняется. Все равно закрыть?",
    "A clip thread is still running. Close anyway?" : u"Поток клипа все еще выполняется. Все равно закрыть?",
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
    "The saved script has changed because AvsP marked section added" : u"Сохраненный скрипт изменился, т.к. добавлен раздел с пометкой AvsP",
    "The saved script has changed because sliders or toggle tags and filters are removed" : u"Сохраненный скрипт был изменен, т.к. ползунки или теги переключения и фильтры были удалены.",
    "Error saving the script: %s" : u"Ошибка при сохранении скрипта: %s",
    "Script has no text!" : u"В скрипте нет текста!",
    "HTML files" : u"Файлы HTML",
    "Load a session" : u"Загрузить сеанс",
    "File has been modified since the session was saved. Reload?" : u"Файл был изменен с момента сохранения сеанса. Загрузить заново?",
    "Save the session" : u"Сохранить сеанс",
    "Save current frame" : u"Сохранить текущий кадр",
    "Introduce the JPEG Quality (0-100)" : u"Укажите качество JPEG (0-100)",
    "JPEG Quality" : u"Качество JPEG",
    "Insert a source" : u"Вставить источник",
    "All supported plugins" : u"Все поддерживаемые плагины",
    "AviSynth plugins" : u"Плагины AviSynth",
    "VirtualDub plugins" : u"Плагины VirtualDub",
    "VFAPI plugins" : u"Плагины VFAPI",
    "Script import" : u"Импорт скрипта",
    "AvxSynth plugins" : u"Плагины AvxSynth",
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
    "Waiting for avisynth release memory" : u"Ожидание освобождения памяти используемой AviSynth",
    "Clip not released. Memory still allocated" : u"Выгрузка клипа не завершена. Память все еще используется",
    "Clip successful released" : u"Выгрузка клипа выполнена успешно",
    "Abandoned clip assigned: \"{0}\"" : u"Оставленный клип определён: \"{0}\"", # New in v2.6.8.4
    "Abandoned clip assigned. Select the tab?" : u"Оставленный клип определён. Выбрать вкладку?",
    "Abandoned clip released: \"{0}\"" : u"Оставленный клип выгружен: \"{0}\"", # New in v2.6.8.4
    "Process clip..." : u"Обработка клипа...",
    "Waiting for avisynth clip" : u"Ожидание клипа AviSynth",
    "Clip process finished" : u"Процесс обработки клипа завершен",
    "Clip not initialized" : u"Клип не инициализирован",
    "Initialize clip  %s" : u"", # New in v2.6.9.8
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
    "Add toggle tag" : u"Добавить тег переключения",
    "Clear all tags and disable the filters" : u"Очистить все тэги и отключить фильтры",
    "Clear all tags && disabled filters" : u"Очистить все тэги && отключить фильтры",
    "Toggle exclusions filters" : u"Переключить исключения фильтров",
    "General settings..." : u"Общие настройки...",
    "Set same width for all tabs" : u"Задать одинаковую ширину для всех вкладок",
    "Update sliders" : u"Обновить ползунки",
    "Reset to default value: %(value_formatted)s" : u"Сброс к начальному значению: %(value_formatted)s",
    "Left-click to select a color, right click to reset to default" : u"Щелкните левой кнопкой мыши, чтобы выбрать цвет, щелкните правой кнопкой, чтобы восстановить значение по умолчанию.",
    "Snapshot doesn't seem to be from this session.\nKeep going?" : u"Возможно, что снимок не из этого сеанса.\nПродолжить?",
    "Question" : u"Вопрос",
    "Error: Snapshot 2 is empty" : u"", # New in v2.6.9.8
    "Restore to current" : u"Восстановить до текущего",
    "Restore to new tab" : u"Восстановить на новую вкладку",
    "Copy snapshot 2 to 1" : u"", # New in v2.6.9.8
    "Done" : u"Выполнено",
    "Joined or disabled filters found: filter1.filter2\nOnly the first filter can have a toggle tag" : u"Обнаружены присоединённые или повреждённые фильтры: filter1.filter2\nТолько первый фильтр может иметь тег переключения.",
    "Enter new name" : u"Введите новое имя",
    "Rename toggle tag" : u"Переименовать тег переключения",
    "Add child" : u"Добавить дочерний элемент",
    "Remove child" : u"Удалить дочерний элемент",
    "Toggle \"%(label)s\" section" : u"Переключить \"%(label)s\" раздел",
    "Both videos must have the same width and height." : u"Оба видео должны иметь одинаковую ширину и высоту.",
    "Snapshot dimensions different: %ix%i" : u"", # New in v2.6.9.8
    "Error playing frame {number}" : u"", # New in v2.6.9.8
    "Save changes before previewing?" : u"Сохранить изменения перед предпросмотром?", 
    "Select an external player" : u"Выберете внешний проигрыватель",
    "A program must be specified to use this feature!" : u"Для использования этой функции должна быть указана программа!",
    "Program not found. Must be specified to use this feature!" : u"Программа не найдена. Необходимо в настройках указать месторасположение программы, чтобы её использовать!",
    "Above plugin names contain undesirable symbols.\nRename them to only use alphanumeric or underscores,\nor make sure to use them in short name style only." : u"Вышеупомянутые имена плагинов содержат нежелательные символы.\nПереименуйте их используя только буквы, цифры и символ подчеркивания,\nили убедитесь, что они используются только в стиле коротких имён.",
    "This function is beta!\nFound more then one function with the same name.\nYou should clean up your plugins." : u"Это бета-версия функции!\nНайдено более одной функции с таким же именем.\nВам следует очистить свои плагины.",
    "Don't show me this again" : u"Больше не показывать",
    "Changing the plugins directory writes to the Windows registry.\n" : u"Изменение каталога плагинов записывает в реестр Windows.",
    "Writing to: HKLM\\Software\\Avisynth\\plugindir2_5\n" : u"Запись в: HKLM\\Software\\Avisynth\\plugindir2_5\n",
    "Plugins dir registration failed" : u"Ошибка при регистрации каталога плагинов",
    "You're changing the plugins autoload directory.\nDo you wish to change it for all applications? This will\nrequire writing to {0}" : u"Вы изменяете каталог автозагрузки плагинов.\nИзменить его для всех приложений? Для этого\nпотребуется выполнить запись в {0}",
    "Save as" : u"Сохранить как",
    "Select a directory" : u"Выберете папку",
    "Enter information" : u"Введите информацию",
    "Progress" : u"Выполнение",
    "A get pixel info operation has already started" : u"Операция по получению информации о пикселях уже началась",
    "Error in the macro:" : u"Ошибка в макросе:",
    "Couldn't find %(macrofilename)s" : u"Не удалось найти %(macrofilename)s",
    "An AviSynth script editor" : u"Редактор скриптов AviSynth\n(автор qwerpoi, переводчики Fizick, Arx1meD)",
    "Error trying to display the clip" : u"Ошибка при попытке показать клип",
    "Is bit-depth set correctly?" : u"Правильно ли установлена битовая глубина цвета?",
    "Invalid string: " : u"Неверная строка: ",
    "Failed to open the AVI file" : u"Не удалось открыть файл AVI",
    "Failed to open the AVI frame" : u"Не удалось открыть кадр AVI",
    "Failed to retrieve AVI frame" : u"Не удалось получить кадр AVI",
    "Waiting for Avisynth, thread still running.\nThis dialog is automatically closed when avisynth returns.\nIf you abort this process, you should restart the program!" : u"", # New in v2.6.9.8
    "Waiting for Avisynth, thread still running.\nThis dialog is automatically closed when avisynth returns.\nIf you abort this process, the clip will assign later." : u"", # New in v2.6.9.8
    "Ctrl" : u"",
    "Alt" : u"",
    "Shift" : u"",
    "Error Window" : u"Окно ошибки",
    "Quick find" : u"Быстрый поиск",
    "Find/replace text" : u"Найти/Заменить текст",
    "Search &for" : u"Найти",
    "R&eplace with" : u"Заменить на",
    "Find &next" : u"Найти следующее",
    "Find &previous" : u"Найти предыдущие",
    "&Replace next" : u"Заменить следующее",
    "Replace &all" : u"Заменить всё",
    "Only on word s&tart" : u"Только в начале слова",
    "Only &whole words" : u"Только слово целиком",
    "Only in &selection" : u"Только в выделенном",
    "&Don't wrap-around" : u"Не зацикливать поиск",
    "&Case sensitive" : u"С учетом регистра",
    "Use regular e&xpressions" : u"Использовать регулярные выражения",
    "&Interpret escape sequences" : u"Интерпретировать выходные последовательности",
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
    "Action" : u"Действие",
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
    "Calculate an appropriate resize for the video" : u"Рассчитайте подходящий размер для видео",
    "Resize calculator" : u"Калькулятор изменения размера кадра",
    "Input" : u"Исходное видео",
    "Video resolution:" : u"Разрешение видео:",
    "Pixel aspect ratio:" : u"Соотношение сторон пикселя PAR):",
    "Results" : u"Результат",
    "Aspect ratio error:" : u"Ошибка соотношения сторон:",
    "Settings" : u"Настройки",
    "Target pixel aspect ratio:" : u"Соотношение сторон целевого пикселя:",
    "Resize block constraints:" : u"Ограничения размера блока:",
    "Resize percent ranges:" : u"Диапазонов процентов:",
    "Max search aspect ratio error:" : u"Ошибка вычисления макс. соотношения сторон:",
    "Configure" : u"Настроить",
    "compute from .d2v" : u"определить из .d2v",
    "Configure options" : u"Настроить параметры",
    "Avisynth resize:" : u"Функция AviSynth:",
    "The current Avisynth script contains errors." : u"Текущий скрипт AviSynth содержит ошибки.",

    #--- Tool: encoder_gui.py ---#
    "Script encoder (CLI)" : u"Кодировщик скриптов (CLI)",
    "Use an external command line encoder to save the current script" : u"Использовать внешний кодировщик, чтобы сохранить текущий скрипт в видео",
    "Encode video" : u"Кодировать видео",
    "System settings" : u"Системные настройки",
    "Input file:" : u"Входной файл:",
    "Output file:" : u"Выходной файл:",
    "Compression settings" : u"Настройки сжатия",
    "Bitrate (kbits/sec):" : u"Битрейт (кбит/с): ",
    "calculate" : u"вычислить",
    "Quality CRF (0-51):" : u"Метод CRF (0-51):",
    "Quality CQ (1-31):" : u"Метод CQ (1-31):",
    "Additional settings" : u"Дополнительные настройки",
    "Credits start frame:" : u"Всего кадров:",
    "Command line settings" : u"Настройки командной строки",
    "Run" : u"Выполнить",
    "First time using this compression preset!" : u"Предустановки для сжатия используются впервые!",
    "Please enter the exe paths in the following dialog." : u"Введите пути к исполняемым файлам .exe в следующем диалоговом окне.",
    "Exe pathnames" : u"Путь к файлу .exe",
    "Open an AviSynth script" : u"Открыть AviSynth скрипт",
    "Save the video as" : u"Сохраните видео как",
    "Select a program" : u"Выберите программу",
    "Unreplaced items remain in the command line:" : u"Незамещённые элементы остаются в командной строке:",
    "Unknown exe paths!" : u"Неизвестные пути к .exe!",
    "General" : u"Общие",
    "Credits warning minutes:" : u"Минуты предупреждения:",
    "Automatically compute bitrate value on startup" : u"Автоматически вычислять битрейт при запуске",
    "Automatically compute pixel aspect ratio from d2v on startup" : u"Автоматически вычислять соотношение сторон пикселя (PAR) из d2v при запуске",
    "Append batch commands to the avs script as comments" : u"Добавлять пакетные команды в скрипт avs в виде комментариев",
    "Add output file to new tab" : u"Добавить выходной файл на новую вкладку",
    "Encoder priority:" : u"Приоритет кодировщика:",
    "Path to %(name)s:" : u"Путь к %(name)s:",
    "Extra arguments:" : u"Дополнительные аргументы:",
    "Presets file not found:\n" : u"Файл предустановок не найден:\n",
    "Bitrate Calculator" : u"Калькулятор битрейта",
    "Output info" : u"Выходная информация",
    "Total size:" : u"Общий размер:",
    "Container:" : u"Контейнер:",
    "(None)" : u"(Нет)",
    "Video info" : u"Информация о видео",
    "Framecount:" : u"Количество кадров:",
    "FPS:" : u"Количество кадров в секунду (FPS):",
    "Audio info" : u"Информация о звуке",
    "Audio file:" : u"Аудио файл:",
    "Compress audio" : u"Сжать аудио",
    "Audio bitrate:" : u"Битрейт аудио:",
    "Format:" : u"Формат:",
    "Subtitles info" : u"Информация о субтитрах",
    "Subtitles file:" : u"Файл субтитров:",
    "Total time:" : u"Общее время:",
    "Video size:" : u"Размер видео:",
    "Audio size:" : u"Размер аудио:",
    "Subtitles size:" : u"Размер субтитров:",
    "Overhead size:" : u"Размер доп. элементов:",
    "Bitrate:" : u"Битрейт:",
    "Open the audio file" : u"Открыть аудио файл",
    "Open the subtitles file" : u"Открыть файл субтитров",
    "%(h)i hr and %(m)i min" : u"%(h)i часов и %(m)i минут",

    #--- Tool: avs2avi_gui.py ---#
    "Script encoder (VFW)" : u"Кодировщик скриптов в .avi",
    "Use avs2avi to save the current script as an avi" : u"Используйте avs2avi.exe, чтобы сохранить текущий скрипт в формат avi",
    "Please select the path to avs2avi.exe" : u"Выберите путь к avs2avi.exe",
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
    "Process stopped." : u"Обработка остановлена.",
    "Processing..." : u"Обработка...",
    "Finished in %(hr)i hour(s) and %(min)i minute(s)." : u"Завершено за %(hr)i часов и %(min)i минут.",
    "Finished in %(min)i minute(s) and %(sec)i second(s)." : u"Завершено за %(min)i минут и %(sec)i секунд.",
    "Finished in %(time).1f seconds." : u"Завершено за %(time).1f секунд.",
    "Filesize: %(size).2f MB" : u"Размер файла: %(size).2f MB",
    "The current script contains errors, exiting." : u"Текущий скрипт содержит ошибки (выходной).",
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
    "Save as Tiff_rgb48" : u"", # New in v2.6.9.8

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