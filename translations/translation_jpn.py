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

# Japanese translation authors:
#   niiyan v2.0.2 - v2.4.1

version = "2.6.9.8"

messages = {
    "AviSynth script" : u"AviSynth スクリプト",
    "AviSynth fonts and colors" : u"フォントと色の設定",
    "Background" : u"背景色",
    "Font" : u"フォント",
    "Text color" : u"文字色",
    "Select a predefined theme" : u"", # New in v2.5.1
    "Only change colours" : u"", # New in v2.5.1
    "When selecting a theme, don't change current fonts" : u"", # New in v2.5.1
    "OK" : u"",
    "Cancel" : u"キャンセル",
    "Page:" : u"ページ:",
    "Page: %d" : u"ページ: %d",
    "Frame properties" : u"", # New in v2.6.9.8
    "Word warp" : u"", # New in v2.6.9.8
    "Horz scroll" : u"", # New in v2.6.9.8
    "Scrap Window" : u"スクラップウィンドウ",
    "Undo" : u"元に戻す",
    "Redo" : u"やり直し",
    "Cut" : u"切り取り",
    "Copy" : u"コピー",
    "Paste" : u"貼り付け",
    "Select all" : u"すべて選択",
    "Refresh" : u"更新",
    "Insert frame #" : u"フレーム番号を挿入",
    "Save to file..." : u"ファイルに保存...",
    "Clear all" : u"すべてクリア",
    "Toggle scrap window" : u"スクラップウィンドウのトグル",
    "Save script" : u"スクリプトの保存",
    "Error: no contextMenu variable defined for window" : u"エラー: ウィンドウに対してコンテキストメニュー変数が定義されていません",
    "Text document" : u"テキストファイル",
    "All files" : u"すべてのファイル",
    "Save scrap text" : u"スクラップテキストの保存",
    "This field must contain a value!" : u"この欄に値を入力してください！",
    "This slider label already exists!" : u"このスライダラベルはすでに存在しています！",
    "Invalid slider label modulo syntax!" : u"スライダラベルの倍数指定のシンタックスが無効です！",
    "This field must contain a number!" : u"この欄に数値を入力してください！",
    "The min value must be less than the max!" : u"最小値は最大値よりも小さく設定してください！",
    "The initial value must be between the min and the max!" : u"デフォルト値は最小値と最大値の間に設定してください！",
    "The min value must be a multiple of %(mod)s!" : u"最小値は %(mod)s の倍数にしてください！",
    "The max value must be a multiple of %(mod)s!" : u"最大値は %(mod)s の倍数にしてください！",
    "The initial value must be a multiple of %(mod)s!" : u"デフォルト値は %(mod)s の倍数にしてください！",
    "The difference between the min and max must be greater than %(mod)s!" : u"最小値と最大値の差は %(mod)s より大きくしてください！",
    "Error" : u"エラー",
    "Define user slider" : u"ユーザースライダの定義",
    "Slider label:" : u"スライダのラベル:",
    "Min value:" : u"最小値:",
    "Max value:" : u"最大値:",
    "Initial value:" : u"デフォルト値:",
    "Add or override AviSynth functions in the database" : u"AviSynth 関数をデータベースに追加/再定義",
    "Core filters" : u"内蔵フィルタ",
    "Plugins" : u"プラグイン",
    "User functions" : u"ユーザー定義関数",
    "Script functions" : u"スクリプト関数",
    "Clip properties" : u"クリップのプロパティ",
    "New function" : u"新規追加",
    "Edit selected" : u"編集",
    "Delete selected" : u"削除",
    "Select installed" : u"インストール済みのプラグインを選択",
    "Import" : u"", # New in v2.5.0
    "Import from files" : u"ファイルからインポート",
    "Import from wiki" : u"", # New in v2.5.0
    "Export customizations" : u"カスタマイズのエクスポート",
    "Clear customizations" : u"カスタマイズのクリア",
    "Clear manual presets" : u"プリセットのクリア",
    "When importing, don't show the choice dialog" : u"インポート時に選択ダイアログを表示しない",
    "Edit function information" : u"関数情報の編集",
    "Name:" : u"名前:",
    "Type:" : u"種類:",
    "clip property" : u"クリップのプロパティ",
    "core filter" : u"内蔵フィルタ",
    "plugin" : u"プラグイン",
    "script function" : u"スクリプト関数",
    "user function" : u"ユーザー定義関数",
    "Arguments:" : u"引数:",
    "define sliders" : u"スライダの定義",
    "reset to default" : u"デフォルトにリセット",
    "Slider information" : u"スライダ情報",
    "Preset:" : u"プリセット:",
    "Auto-generate" : u"自動生成",
    "Filter name already exists!" : u"そのフィルタ名はすでに存在します！",
    "Invalid filter name!" : u"無効なフィルタ名です！",
    "Renaming not allowed!" : u"名前を変更することはできません！",
    "You must use dllname_function naming format for plugins!" : u"プラグインについては「dll 名_関数」という命名書式を使用してください！",
    "Long name" : u"", # New in v2.5.0
    "Short name" : u"", # New in v2.5.0
    "Both" : u"", # New in v2.5.0
    "Only long names" : u"", # New in v2.5.0
    "Only short names" : u"", # New in v2.5.0
    "All names" : u"", # New in v2.5.0
    "Open Customization files, Avisynth scripts or Avsp options files" : u"カスタマイズファイル、AviSynth スクリプトまたは AvsP オプションファイルを開く",
    "All supported" : u"対応するすべてのファイル",
    "Customization file" : u"カスタマイズファイル",
    "AvsP data" : u"AvsP データ",
    "Unrecognized files" : u"認識されないファイル",
    "Select the functions to import" : u"", # New in v2.5.0
    "Check selected" : u"", # New in v2.5.0
    "Check all" : u"", # New in v2.5.0
    "Check all in this file" : u"", # New in v2.5.0
    "Check all not customized" : u"", # New in v2.5.0
    "Uncheck selected" : u"", # New in v2.5.0
    "Uncheck all" : u"", # New in v2.5.0
    "Uncheck all in this file" : u"", # New in v2.5.0
    "Uncheck all customized" : u"", # New in v2.5.0
    "Red - a customized function already exists." : u"警告 - カスタマイズされた関数はすでに存在します。",
    "Invalid plugin function name \"{name}\". Must be \"pluginname_functionname\"." : u"", # New in v2.5.1
    "No customizations to export!" : u"エクスポートするカスタマイズが存在しません！",
    "Save filter customizations" : u"フィルタカスタマイズの保存",
    "This will delete all filter customizations. Continue?" : u"すべてのフィルタカスタマイズを削除します。続行しますか？",
    "Warning" : u"警告",
    "This will delete all manually defined presets. Continue?" : u"手動で定義されたすべてのプリセットを削除します。続行しますか？",
    "Do you really want to delete this custom filter?" : u"", # New in v2.5.0
    "Do you really want to reset this filter?" : u"", # New in v2.5.0
    "Edit filter database" : u"フィルタデータベースを編集",
    "Default" : u"デフォルト",
    "Min value" : u"最小値",
    "Max value" : u"最大値",
    "Step size" : u"ステップサイズ",
    "Value list (comma separated)" : u"値のリスト（カンマ区切り）",
    "Value must be True or False!" : u"値は True または False にしてください！",
    "Export filter customizations" : u"フィルタカスタマイズのエクスポート",
    "Import filter customizations" : u"フィルタカスタマイズのインポート",
    "Select filters to export:" : u"エクスポートするフィルタの選択:",
    "Select filters to import from the file:" : u"ファイルからインポートするフィルタの選択:",
    "Overwrite all data" : u"すべてのデータを上書きする",
    "You must select at least one filter!" : u"少なくとも 1 つのフィルタを選択してください！",
    "Slider SetRange Error: minValue must be less than maxValue" : u"", # New in v2.6.9.8
    "New File" : u"新しいファイル",
    "Windows Bitmap" : u"Windows ビットマップ",
    "Animation" : u"アニメーション",
    "JPEG" : u"",
    "Zsoft Paintbrush" : u"",
    "Portable Network Graphics" : u"PNG (Portable Network Graphics)",
    "Netpbm" : u"",
    "Tagged Image File" : u"TIFF (Tagged Image File)",
    "ASCII Text Array" : u"ASCII テキスト配列",
    "Windows Icon" : u"Windows アイコン",
    "Windows Cursor" : u"Windows カーソル",
    "Frame" : u"フレーム",
    "fps" : u"",
    "A crash detected at the last running!" : u"前回実行時にクラッシュが検出されました！",
    "&Zoom" : u"ズーム(&Z)",
    "Damaged {0}. Using default settings." : u"{0} が破損しました。デフォルトの設定を使用しています。",
    "%s translation file updated with new messages to translate" : u"%s 翻訳ファイルが更新されました。未訳のメッセージがあります。",
    "Translation updated" : u"翻訳が更新されました",
    "%s translation file updated.  No new messages to translate." : u"%s 翻訳ファイルが更新されました。未訳のメッセージはありません。",
    "%s language couldn't be loaded" : u"%s 言語を読み込むことが出来ませんでした",
    "Cannot read the avisynth plugins directory from the registry\n" : u"", # New in v2.6.1.5
    "HKLM\\Software\\Avisynth'plugindir2_5' or 'plugindir+' is missing or wrong.\n\n" : u"", # New in v2.6.1.5
    "You should set the plugins path under options manually or register it." : u"", # New in v2.6.1.5
    "Alternatively, specify now its directory." : u"代わりに、今そのディレクトリを指定して下さい。",
    "Select the {0} directory" : u"{0} ディレクトリを選択",
    "Make sure you have AviSynth installed and that there are no unstable plugins or avsi files in the AviSynth plugins directory." : u"AviSynth がインストールされているか、AviSynth のプラグインディレクトリに不安定なプラグインや avsi ファイルがないか確認してください。",
    "Error loading AviSynth!" : u"AviSynth の読み込みエラー",
    "Paths" : u"パス",
    "Available variables: %programdir%, %avisynthdir%, %pluginsdir%" : u"利用可能な変数: %programdir%, %avisynthdir%, %pluginsdir%",
    "Choose a different version than the installed" : u"インストールされているのとは異なるバージョンを選択してください",
    "Use a custom AviSynth directory" : u"カスタム AviSynth ディレクトリを使用",
    "Alternative location of avisynth.dll/avxsynth.so" : u"avisynth.dll/avxsynth.so の代替場所",
    "Custom AviSynth directory:" : u"カスタム AviSynth ディレクトリ:",
    "Leave blank for reset or choose a directory for manually set or for register" : u"", # New in v2.6.1.5
    "Disable autoload, set manually" : u"", # New in v2.6.1.5
    "If plugins autoload fails set the path manually. Read only. Only for proper program functions" : u"", # New in v2.6.1.5
    "Register the plugins directory" : u"", # New in v2.6.1.5
    "This changes the plugins directory for Avisynth itself. On Windows Registry values in HKLM are changed." : u"", # New in v2.6.1.5
    "Override the current working directory" : u"現在の作業ディレクトリをオーバーライド",
    "Use a custom working directory" : u"カスタム作業ディレクトリを使用",
    "For all scripts" : u"すべてのスクリプトに適用",
    "Use the custom directory also for scripts saved to file, instead of its parent" : u"ファイルに保存するスクリプトにも親ディレクトリの代わりにカスタムディレクトリを使用",
    "Specify an alternative working directory" : u"代替作業ディレクトリを指定して下さい",
    "Working directory:" : u"作業ディレクトリ:",
    "External player:" : u"外部プレーヤー:",
    "Location of external program for script playback" : u"スクリプト再生用外部プログラムの場所",
    "Executable files" : u"実行ファイル",
    "Additional arguments when running the external player" : u"外部プレーヤー起動時の追加の引数",
    "External player extra args:" : u"外部プレーヤーのオプション:",
    "External tool:" : u"", # New in v2.6.6.0
    "Location of external program, e.g. AvsMeter" : u"", # New in v2.6.6.0
    "Arguments for external tool menu 1, e.g. Menu label|arguments\nUse %fn to pass the script file name with the arguments." : u"", # New in v2.6.6.0
    "External tool arg1:" : u"", # New in v2.6.6.0
    "Arguments for external tool menu 2, e.g. Menu label|arguments\nUse %fn to pass the script file name with the arguments." : u"", # New in v2.6.6.0
    "External tool arg2:" : u"", # New in v2.6.6.0
    "Avisynth help file/url:" : u"AviSynth ヘルプファイル/URL:",
    "Location of the avisynth help file or url" : u"AviSynth ヘルプファイルの場所または URL",
    "Documentation search paths:" : u"ヘルプ検索パス:",
    "Specify which directories to search for docs when you click on a filter calltip" : u"フィルタツールチップ上でクリックした時に検索するヘルプのディレクトリを指定",
    "Documentation search url:" : u"ヘルプ検索 URL:",
    "The web address to search if docs aren't found (the filter's name replaces %filtername%)" : u"ヘルプが見つからない場合に検索するウェブアドレス（%filtername% がフィルタの名前に置換されます）",
    "Text" : u"テキスト",
    "Highlight the text as if it wasn't enclosed by triple quotes" : u"", # New in v2.5.1
    "Style inside triple-quoted strings" : u"", # New in v2.5.1
    "Prefer functions over variables" : u"", # New in v2.5.0
    "When a word could be either a function or a variable, highlight it as function" : u"", # New in v2.5.0
    "Don't allow lines wider than the window" : u"ウインドウ幅で行を折り返す",
    "Wrap text" : u"テキストの折り返し",
    "Draw lines at fold points" : u"折りたたみ位置に線を描画",
    "For code folding, draw a line underneath if the fold point is not expanded" : u"コード折りたたみ機能に関して、折りたたみ位置が展開されない場合は下に線を描画する。",
    "Check to insert actual tabs instead of spaces when using the Tab key" : u"タブキー使用時、スペースの代わりにタブを挿入するかどうかのチェック",
    "Use tabs instead of spaces" : u"スペースの代わりにタブを使用",
    "Set the size of the tabs in spaces" : u"スペース単位でタブのサイズを設定",
    "Tab width" : u"タブ幅",
    "Initial space to reserve for the line margin in terms of number of digits. Set it to 0 to disable showing line numbers" : u"桁数の観点から行番号欄のマージンを確保するための初期のスペース。0 に設定すると行番号表示を無効化",
    "Line margin width" : u"行余白幅",
    "Show filter calltips" : u"フィルタのツールチップを表示",
    "Turn on/off automatic tips when typing filter names" : u"フィルタ名の入力時に自動的にヒントを表示する/しない",
    "Always show calltips any time the cursor is within the filter's arguments" : u"カーソルがフィルタの引数の中にある時はつねにツールチップを表示する",
    "Frequent calltips" : u"つねにツールチップを表示",
    "Show autocomplete on capital letters" : u"大文字で始まる単語に自動補完を表示",
    "Turn on/off automatic autocomplete list when typing words starting with capital letters" : u"大文字で始まる単語の入力時に自動的に自動補完リストを表示する/しない",
    "Amount of letters typed" : u"入力された文字の数",
    "Show autocomplete list when typing a certain amount of letters" : u"一定数の文字が入力されたら補完リストを表示",
    "Autocomplete" : u"自動補完",
    "AviSynth user function database" : u"", # New in v2.5.0
    "Select what functions beside internal and user-defined will be included in the database" : u"", # New in v2.5.0
    "Autoloaded plugin functions" : u"", # New in v2.5.0
    "Include the functions on autoloaded plugins in the database" : u"", # New in v2.5.0
    "Autoloaded script functions" : u"", # New in v2.5.0
    "Include the functions on autoloaded avsi files in the database" : u"", # New in v2.5.0
    "Include plugin functions from the program's database" : u"", # New in v2.5.0
    "Plugin functions from database" : u"", # New in v2.5.0
    "Include user script functions from the program's database" : u"", # New in v2.5.0
    "Script functions from database" : u"", # New in v2.5.0
    "Add user defined variables into autocomplete list" : u"自動補完リストにユーザー定義変数を追加する",
    "Show autocomplete with variables" : u"自動補完を変数付きで表示",
    "Show autocomplete on single matched lowercase variable" : u"一件のみマッチした小文字の変数に自動補完を表示",
    "When typing a lowercase variable name, show autocomplete if there is only one item matched in keyword list" : u"小文字の変数名入力時、キーワードリストで一件のみマッチしたら自動補完を表示する",
    "Add icons into autocomplete list. Using different type to indicate how well a filter's presets is defined" : u"自動補完リストにアイコンを追加。さまざまな種類を使用して、フィルタのプリセットがどの程度定義されているかを示す",
    "Show autocomplete with icons" : u"アイコン付きで自動補完を表示",
    "Don't show autocomplete when calltip is active" : u"コールチップがアクティブな時は自動補完を表示しない",
    "When calltip is active, autocomplete will not be activate automatically. You can still show autocomplete manually" : u"コールチップがアクティブな時、自動補完は自動的にアクティブにならない。手動で表示することは可能",
    "Autoparentheses level" : u"丸括弧の自動補完のレベル",
    "Close \"()\"" : u"括弧を閉じる",
    "Determines parentheses to insert upon autocompletion" : u"自動補完で挿入する丸括弧の数を決定します",
    "None \" \"" : u"括弧なし",
    "Open \"(\"" : u"開き丸括弧のみ",
    "Determines which key activates the filter preset when the autocomplete box is visible" : u"自動補完ボックスが表示されている時にどのキーがフィルタプリセットを有効化するかを決定する",
    "Preset activation key" : u"プリセット有効化キー",
    "Return" : u"リターン",
    "Tab" : u"タブ",
    "None" : u"なし",
    "Video" : u"ビデオ",
    "Constantly update video while dragging" : u"スライドバー移動中にフレームごとにプレビューを更新",
    "Update the video constantly when dragging the frame slider" : u"スライドバーを使ってフレームを移動している時、フレームごとに絶えずプレビューを更新する",
    "Enable line-by-line update" : u"行単位更新を有効化",
    "Enable the line-by-line video update mode (update every time the cursor changes line position)" : u"行単位ビデオ更新モードを有効化（カーソルが行位置を変更するごとに更新）",
    "Focus the video preview upon refresh" : u"更新時にビデオプレビューにフォーカス",
    "Switch focus to the video preview window when using the refresh command" : u"更新コマンド使用時にフォーカスをビデオプレビューウィンドウに切り替える",
    "Refresh preview automatically" : u"プレビューを自動的にリフレッシュ",
    "Refresh preview when switch focus on video window or change a value in slider window" : u"ビデオウィンドウにフォーカスを切り替えるかスライダウィンドの値を変更した時にプレビューをリフレッシュする",
    "Move video slider to timeline start" : u"", # New in v2.6.9.8
    "On moving timeline range with keys Ctrl + Alt + PageDown\nTimeline moving with Ctrl + Alt + (Left, Right, PageUp, PageDown)\n or left mouse button on the status bar, with Shift no limit" : u"", # New in v2.6.9.8
    "Seeking to a certain frame will seek to that frame on all tabs" : u"あるフレームへシークした時、すべてのタブでそのフレームにシークする",
    "Shared timeline" : u"タイムラインの共有",
    "Only on tabs of the same characteristics" : u"", # New in v2.5.0
    "Only share timeline for clips with the same resolution and frame count" : u"", # New in v2.5.0
    "Determines which mouse wheel function is used, see below tabs.Tab change also possible under Misc -> Mouse browse buttons" : u"", # New in v2.6.6.0
    "Mouse wheel function" : u"", # New in v2.6.6.0
    "Tab change or scroll" : u"", # New in v2.6.6.0
    "Frame step" : u"フレームステップ",
    "Tab change" : u"", # New in v2.6.6.0
    "Enable scroll wheel through similar tabs" : u"スクロールホイールによるタブの切り替えを許可",
    "Mouse scroll wheel cycles through tabs with similar videos" : u"マウスホイールのスクロールで隣接するビデオのタブを切り替える",
    "Enable scroll wheel through tabs on the same group" : u"", # New in v2.5.0
    "Mouse scroll wheel cycles through tabs assigned to the same tab group" : u"", # New in v2.5.0
    "Allow AvsPmod to resize and/or move the program window when updating the video preview" : u"ビデオプレビューを更新した時、プログラムウィンドウをリサイズ/移動することを許可する",
    "Allow AvsPmod to resize the window" : u"ウィンドウのリサイズを許可",
    "Separate video preview window" : u"ビデオプレビューウィンドウを分離",
    "Use a separate window for the video preview" : u"ビデオプレビューには独立したウィンドウを使用する",
    "Keep it on top of the main window" : u"常にメインウィンドウの前面に表示",
    "Keep the video preview window always on top of the main one and link its visibility" : u"ビデオプレビューウィンドウを常にメインウィンドウの前面に表示し、その可視性をリンクさせる",
    "Startup with last zoom settings" : u"", # New in v2.6.6.0
    "Use last zoom settings at startup" : u"", # New in v2.6.6.0
    "Min text lines on video preview" : u"ビデオプレビュー時の最小テキスト行数",
    "Minimum number of lines to show when displaying the video preview" : u"ビデオプレビューを表示する時に表示するテキストの最小行数",
    "Customize the video information shown in the program status bar" : u"プログラムステータスバーに表示されるビデオ情報をカスタマイズ",
    "Customize video status bar..." : u"ビデオステータスバーのカスタマイズ...",
    "Error message font..." : u"", # New in v2.6.1.5
    "Set the font used for displaying the error if evaluating the script fails" : u"", # New in v2.5.1
    "User Sliders" : u"ユーザースライダ",
    "Hide slider window by default" : u"デフォルトでスライダウィンドウを隠す",
    "Keep the slider window hidden by default when previewing a video" : u"ビデオプレビュー時、デフォルトでスライダウィンドウを隠れたままにする",
    "Create user sliders automatically" : u"ユーザースライダを自動生成",
    "Create user sliders automatically using the filter database" : u"フィルタデータベースを使ってユーザースライダを自動的に生成する",
    "Create user sliders for int and float arguments" : u"int 型と float 型の引数にユーザースライダを生成",
    "type int/float (numerical slider)" : u"int/float 型（数値スライダ）",
    "Create listboxes for int list arguments" : u"", # New in v2.5.1
    "type int (list)" : u"", # New in v2.5.1
    "Create color pickers for hex color arguments" : u"16 進数の引数にカラーピッカーを生成",
    "type int (hex color)" : u"int 型（16 進数）",
    "Create radio boxes for bool arguments" : u"bool 型の引数にラジオボックスを生成",
    "type bool" : u"bool 型",
    "Create listboxes for string list arguments" : u"string 型のリスト引数にリストボックスを生成",
    "type string (list)" : u"string 型（リスト）",
    "Create filename pickers for string filename arguments" : u"string 型のファイル名引数にファイルピッカーを生成",
    "type string (filename)" : u"string 型（ファイル名）",
    "Create placeholders for arguments which have no database information" : u"データベース情報のない引数にプレースホルダを生成",
    "undocumented" : u"データベース未登録",
    "Disable refresh as default" : u"", # New in v2.6.9.8
    "Do not reinitialize the clip every time a slider is changed. Can be changed in the slider window" : u"", # New in v2.6.9.8
    "Button show/hide applies to all tabs" : u"", # New in v2.6.9.8
    "Or press Ctrl when you click the button." : u"", # New in v2.6.9.8
    "Hide slider window toggle tag menus*" : u"", # New in v2.6.9.8
    "Hide the toggle tag menus in the context menu of the sliders" : u"", # New in v2.6.9.8
    "Custom colors can be set under 'Options->Font and colors->Advanced 2'\nNot visible slider windows needed refresh." : u"", # New in v2.6.9.8
    "Enable slider window custom color theme" : u"", # New in v2.6.9.8
    "Determines which filters will initially have hidden arguments in the slider window" : u"初期状態でスライダウィンドウ内のどの引数を隠すかを決定する",
    "Fold all" : u"すべて折りたたむ",
    "Fold non-numbers" : u"数値以外を折りたたむ",
    "Fold none" : u"すべて展開",
    "Fold or restore last status" : u"", # New in v2.6.9.8
    "Fold startup setting" : u"折りたたみ初期設定",
    "Filter exclusion list:" : u"除外フィルタリスト:",
    "Specify filters never to build automatic sliders for. Use a space as separator.\nYou can toggle it in the slider context menu." : u"", # New in v2.6.9.8
    "Save/Load" : u"保存/読み込み",
    "Automatically save the session on shutdown and load on next startup" : u"終了時に自動的にセッションを保存し、次回起動時に読み込む",
    "Save session for next launch" : u"セッションの自動保存",
    "Always load startup session" : u"セッションを常に読み込む",
    "Always load the auto-saved session before opening any other file on startup" : u"起動時に他のファイルを開く前に常に自動保存されたセッションを読み込む",
    "Always hide the video preview window when loading a session" : u"セッション読み込み時に常にビデオプレビューウィンドウを隠す",
    "Don't preview when loading a session" : u"セッション読み込み時にプレビューしない",
    "Backup session periodically (minutes)" : u"定期的にセッションをバックアップ（分単位）",
    "Backup the session every X minutes, if X > 0" : u"X > 0 なら、X 分毎にセッションをバックアップ",
    "Backup session when previewing" : u"プレビュー時にセッションをバックアップ",
    "If checked, the current session is backed up prior to previewing any new script" : u"有効時、新しいスクリプトのプレビュー前に現在のセッションをバックアップする",
    "Prompt to save a script before previewing (inactive if previewing with unsaved changes)" : u"プレビュー前にスクリプトを保存するためのダイアログを表示する (未保存の変更をともなうプレビューなら無効)",
    "Prompt to save when previewing" : u"プレビュー時に保存ダイアログを表示",
    "Create a temporary preview script with unsaved changes when previewing the video" : u"ビデオプレビュー時に、未保存の変更を含む一時スクリプトを生成する",
    "Preview scripts with unsaved changes" : u"未保存の変更を含むスクリプトをプレビュー",
    "When closing a tab, don't prompt to save the script if it doesn't already exist on the filesystem" : u"タブを閉じる時、スクリプトがファイルシステムに存在しなくても保存を促さない",
    "When closing tab, don't prompt to save scripts without file" : u"", # New in v2.5.1.09
    "Prompt to save each script with unsaved changes when exiting the program" : u"プログラム終了時に保存されていない変更のあるスクリプトを保存するためのダイアログを表示する",
    "Prompt to save scripts on program exit" : u"プログラム終了時に保存ダイアログを表示",
    "Only with existing script" : u"", # New in v2.5.1.09
    "When exiting the program, don't prompt to save the script if it doesn't already exist on the filesystem" : u"", # New in v2.5.1.09
    "Auto: CRLF on Windows and LF on *nix for new scripts, existing scripts keep their current line endings" : u"", # New in v2.5.1
    "Force CRLF" : u"", # New in v2.5.1
    "Force LF" : u"", # New in v2.5.1
    "Line endings" : u"", # New in v2.5.1
    "Auto" : u"", # New in v2.5.1
    "Save and read AvsPmod-specific markings (user sliders, toggle tags, etc) as a commented section in the *.avs file" : u"", # New in v2.6.1.5
    "Save or read avs scripts with AvsPmod markings" : u"", # New in v2.6.9.8
    "Do not remove toggle tags and disabled filters.\nCan make the saved script unreadable for other programs if You not use #> in front of the toggle tag: #>[sharp=0]" : u"", # New in v2.6.9.8
    "Save toggle tags within the script ( read the hint! )" : u"", # New in v2.6.9.8
    "Start dialogs on the last used directory" : u"ダイアログを最後に使用されたディレクトリから開始する",
    "If unchecked, the script's directory is used" : u"チェックを外すと、スクリプトのディレクトリが使用される",
    "Start save image dialogs on the last used directory" : u"画像保存ダイアログを最後に使用されたディレクトリから開始する",
    "Choose a default pattern for image filenames. %s -> script title, %06d -> frame number padded to six digits" : u"", # New in v2.5.0
    "Default image filename pattern" : u"", # New in v2.5.0
    "Ask for JPEG quality" : u"", # New in v2.5.0
    "When saving a JPEG image, prompt for the quality level. Use the value from the last time if not checked" : u"", # New in v2.5.0
    "Misc" : u"その他",
    "Choose the language used for the interface" : u"インターフェイスに使用される言語を選択",
    "Language" : u"言語",
    "Show keyboard images in the script tabs when video has focus" : u"ビデオフォーカス時にスクリプトタブの中にキーボード画像を表示する",
    "Use keyboard images in tabs" : u"タブにキーボード画像を使用",
    "Show tabs in multiline style" : u"タブの多段表示",
    "There can be several rows of tabs" : u"タブの複数段表示を可能にする",
    "All tabs will have same width" : u"タすべてのタブを同じ幅にする",
    "Show tabs in fixed width" : u"タブの幅を固定",
    "Invert scroll wheel direction (Tabs, Zoom)" : u"", # New in v2.5.1.09
    "Scroll the mouse wheel up for changing tabs to the right" : u"タブを右に切り替える時はマウスホイールを上にスクロールする",
    "Invert scroll wheel direction (Frame)" : u"", # New in v2.5.1.09
    "Invert wheel direction for frames step" : u"", # New in v2.6.1.5
    "Automatically load bookmarks from script" : u"", # New in v2.6.6.0
    "Load bookmarks from script" : u"", # New in v2.6.6.0
    "Automatically load bookmarks from script or tab if tab changed" : u"", # New in v2.6.6.0
    "Tab change loads bookmarks from script or tab *" : u"", # New in v2.6.6.0
    "Warn if tab bookmarks and from script reading bookmarks different." : u"", # New in v2.6.6.0
    "Warning tab bookmarks different" : u"", # New in v2.6.6.0
    "Only allow a single instance of AvsPmod" : u"AvsPmod にシングルインスタンスのみ許可",
    "Show warning at startup if there are dlls with bad naming in default plugin folder" : u"デフォルトのプラグインフォルダにおかしなネーミングの DLL がある場合、起動時に警告を表示",
    "Show warning for bad plugin naming at startup" : u"起動時におかしなネーミングのプラグインに関する警告を表示",
    "Bookmark jump" : u"", # New in v2.6.6.0
    "Custom jump" : u"", # New in v2.6.6.0
    "Mouse browse buttons" : u"", # New in v2.6.6.0
    "Mouse browse buttons (forward/backward) on video and script window\nIf 'Tab change' and tab count less than 2, 'Bookmark jump' is used\nIf 'Tab change' press CTRL or left mouse and 'Bookmark jump' is used\nIf 'Bookmark jump', vice versa" : u"", # New in v2.6.6.0
    "Middle mouse button behavior on the script, if script empty open source is used" : u"", # New in v2.6.6.0
    "Middle mouse on script" : u"", # New in v2.6.6.0
    "Open source" : u"", # New in v2.6.6.0
    "Show video frame" : u"", # New in v2.6.6.0
    "Max number of recent filenames" : u"最近使ったファイル名の最大保存数",
    "This number determines how many filenames to store in the recent files menu" : u"この数値が最近使ったファイルのメニューで保存されるファイル名の数を決定する",
    "Custom jump size:" : u"カスタムジャンプサイズ:",
    "Jump size used in video menu" : u"ビデオメニューで使用されるフレーム間移動の大きさ",
    "Custom jump size units" : u"カスタムジャンプサイズの単位",
    "Units of custom jump size" : u"カスタムジャンプサイズの単位",
    "hours" : u"時間",
    "minutes" : u"分",
    "seconds" : u"秒",
    "frames" : u"フレーム",
    "Misc 2" : u"", # New in v2.6.6.0
    "AvsPmod DPI scaling *" : u"", # New in v2.6.6.0
    "DPI scaling overall only manually*" : u"", # New in v2.6.6.0
    "Do not do overall DPI scaling automatically" : u"", # New in v2.6.6.0
    "Disable DPI awareness*" : u"", # New in v2.6.6.0
    "Only disable it if you using 100% system zoom. Program is zoomed by the system and set DPI values." : u"", # New in v2.6.9.8
    "DPI scaling overall:*" : u"", # New in v2.6.6.0
    "Manually adjust dpi scaling overall (10 % steps). For 150 % DPI set value 5" : u"", # New in v2.6.9.8
    "Additional adjust the video controls (10 % steps)" : u"", # New in v2.6.6.0
    "DPI scaling video controls:*" : u"", # New in v2.6.6.0
    "Additional adjust the script window tabs (10 % steps)" : u"", # New in v2.6.6.0
    "DPI scaling main tabs:*" : u"", # New in v2.6.6.0
    "Additional adjust the statusbar (10 % steps)" : u"", # New in v2.6.6.0
    "DPI scaling statusbar:*" : u"", # New in v2.6.6.0
    "Advanced settings" : u"", # New in v2.6.9.8
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
    "After creating a new clip, show available memory in the status bar if memory is less than x MB" : u"", # New in v2.6.9.8
    "Show available system memory (0 disabled)" : u"", # New in v2.6.9.8
    "Delay before thread progress dialog appears" : u"", # New in v2.6.9.8
    "If accessing Avisynth in threads enabled, this setting determines the delay in seconds before the dialog appears. Can be double (clip, frame)" : u"", # New in v2.6.9.8
    "If the mouse wheel does not work in the editor\nor you want another scroll rate. 1 to 5 lines to scroll\nFor enable/disable you must restart the program" : u"", # New in v2.6.9.8
    "Mouse wheel scroll rate on editor (0 disabled)*" : u"", # New in v2.6.9.8
    "Add tab to group" : u"", # New in v2.5.0
    "Extend selection to line down position" : u"選択範囲を一行下へ拡張",
    "Scroll down" : u"スクロールダウン",
    "Extend rectangular selection to line down position" : u"長方形の選択範囲を一行下へ拡張",
    "Extend selection to line up position" : u"選択範囲を一行上へ拡張",
    "Scroll up" : u"スクロールアップ",
    "Extend rectangular selection to line up position" : u"長方形の選択範囲を一行上へ拡張",
    "Go to previous paragraph" : u"前の段落へ移動",
    "Extend selection to previous paragraph" : u"選択範囲を前の段落へ拡張",
    "Go to next paragraph" : u"次の段落へ移動",
    "Extend selection to next paragraph" : u"選択範囲を次の段落へ拡張",
    "Extend selection to previous character" : u"選択範囲を前の文字へ拡張",
    "Go to previous word" : u"前の単語へ移動",
    "Extend selection to previous word" : u"選択範囲を前の単語へ拡張",
    "Extend rectangular selection to previous character" : u"長方形の選択範囲を前の文字へ拡張",
    "Extend selection to next character" : u"選択範囲を次の文字へ拡張",
    "Go to next word" : u"次の単語へ移動",
    "Extend selection to next word" : u"選択範囲を次の単語へ拡張",
    "Extend rectangular selection to next character" : u"長方形の選択範囲を次の文字へ拡張",
    "Go to previous word part" : u"前の単語部分へ移動",
    "Extend selection to previous word part" : u"選択範囲を前の単語部分へ拡張",
    "Go to next word part" : u"次の単語部分へ移動",
    "Extend selection to next word part" : u"選択範囲を次の単語部分へ拡張",
    "Extend selection to start of line" : u"選択範囲を行頭へ拡張",
    "Go to start of document" : u"ドキュメントの最初へ移動",
    "Extend selection to start of document" : u"選択範囲をドキュメントの最初へ拡張",
    "Go to start of line" : u"行頭へ移動",
    "Extend selection to end of line" : u"選択範囲を行末へ拡張",
    "Go to end of document" : u"ドキュメントの終わりへ移動",
    "Extend selection to end of document" : u"選択範囲をドキュメントの終わりへ拡張",
    "Go to end of line" : u"行末へ移動",
    "Extend selection to previous page" : u"選択範囲を前のページへ拡張",
    "Extend rectangular selection to previous page" : u"長方形の選択範囲を前のページへ拡張",
    "Extend selection to next page" : u"選択範囲を次のページへ拡張",
    "Extend rectangular selection to next page" : u"長方形の選択範囲を次のページへ拡張",
    "Delete to end of word" : u"単語の終わりまで削除",
    "Delete to end of line" : u"行末まで削除",
    "Delete back" : u"一つ前の文字を削除",
    "Delete to start of word" : u"単語の先頭まで削除",
    "Delete to start of line" : u"行頭まで削除",
    "Cancel autocomplete or calltip" : u"自動補完またはコールチップをキャンセル",
    "Indent selection" : u"選択範囲をインデント",
    "Unindent selection" : u"選択範囲をアンインデント",
    "Newline" : u"改行文字",
    "Zoom in" : u"ズームイン",
    "Zoom out" : u"ズームアウト",
    "Reset zoom level to normal" : u"ズームレベルを標準にリセット",
    "Line cut" : u"行の切り取り",
    "Line delete" : u"行の削除",
    "Line copy" : u"行のコピー",
    "Transpose line with the previous" : u"前の行と置換",
    "Line or selection duplicate" : u"行/選択範囲の複製",
    "Convert selection to lowercase" : u"選択範囲を小文字に変換",
    "Convert selection to uppercase" : u"選択範囲を大文字に変換",
    "Resolution-based" : u"解像度ベース",
    "BT.709" : u"",
    "BT.601" : u"",
    "TV levels" : u"TV 色調",
    "PC levels" : u"PC 色調",
    "Progressive" : u"プログレッシブ",
    "Interlaced" : u"インターレース",
    "Swap UV" : u"UV をスワップ",
    "25%" : u"",
    "50%" : u"",
    "100% (normal)" : u"100% （標準）",
    "200%" : u"",
    "300%" : u"",
    "400%" : u"",
    "Fill window" : u"ウィンドウに合わせる",
    "Fit inside window" : u"プレビューウィンドウに合わせる",
    "Vertically" : u"垂直方向",
    "Horizontally" : u"水平方向",
    "Black" : u"", # New in v2.5.1
    "Dark grey" : u"", # New in v2.5.1
    "Medium grey" : u"", # New in v2.5.1
    "Light grey" : u"", # New in v2.5.1
    "White" : u"", # New in v2.5.1
    "&File" : u"ファイル(&F)",
    "Create a new tab" : u"新しいタブを作成",
    "New tab" : u"新しいタブ",
    "Create a new tab from template **" : u"", # New in v2.6.9.8
    "New tab from template" : u"", # New in v2.6.9.8
    "Open an existing script" : u"既存のスクリプトを開く",
    "Open..." : u"開く...",
    "Reopen the last closed tab" : u"最後に閉じたタブを開き直す",
    "Undo close tab" : u"閉じたタブを元に戻す",
    "Close tab" : u"タブを閉じる",
    "Close the current tab" : u"現在のタブを閉じる",
    "Close all tabs" : u"すべてのタブを閉じる",
    "Close every tab" : u"すべてのタブを閉じる",
    "Rename tab" : u"タブのリネーム",
    "Rename the current tab. If script file is existing, also rename it" : u"現在のタブをリネームする。スクリプトファイルが存在する場合は、それもリネーム。",
    "Save the current script" : u"現在のスクリプトを保存",
    "Choose where to save the current script" : u"現在のスクリプトを保存する場所を選択",
    "Save script as..." : u"名前を付けて保存...",
    "Reload script" : u"スクリプトの再読み込み",
    "Reopen the current script file if it has changed" : u"変更があったら現在のスクリプトファイルを開き直す",
    "If the current script is saved to a file, open its directory" : u"", # New in v2.5.1
    "Open script's directory" : u"", # New in v2.5.1
    "Save the current script as a HTML document" : u"", # New in v2.5.0
    "Export HTML" : u"", # New in v2.5.0
    "&Print script" : u"スクリプトの印刷(&P)",
    "Configure page for printing" : u"印刷のためにページを設定",
    "Page setup" : u"ページ設定",
    "Include the script filename and page number at the top of each page" : u"各ページの上部にスクリプトファイル名とページ番号を含める",
    "Print header" : u"ヘッダの印刷",
    "Word-wrap long lines" : u"長い行の折り返し",
    "Apply the current zoom to the output" : u"現在のズームを出力に適用",
    "Use zoom" : u"ズームの使用",
    "Display print preview" : u"印刷プレビューの表示",
    "Print preview" : u"印刷プレビュー",
    "&Print" : u"印刷(&P)",
    "Print to printer or file" : u"プリンタまたはファイルに印刷",
    "Load a session into the tabs" : u"セッションをタブに読み込む",
    "Load session..." : u"セッションの読み込み...",
    "Save all the scripts as a session, including slider info" : u"すべてのスクリプトをセッションとして保存（スライダ情報を含む）",
    "Save session..." : u"セッションの保存...",
    "Backup current session" : u"現在のセッションをバックアップ",
    "Backup the current session for next program run" : u"次回起動用に現在のセッションをバックアップする",
    "Next tab" : u"次のタブ",
    "Switch to next script tab" : u"次のスクリプトのタブに移動",
    "Previous tab" : u"前のタブ",
    "Switch to previous script tab" : u"前のスクリプトのタブに移動",
    "Previously selected tab" : u"", # New in v2.6.9.8
    "Toggle between the last two selected tabs" : u"", # New in v2.6.9.8
    "Show the scrap window" : u"スクラップウィンドウを表示",
    "Clear file history" : u"", # New in v2.6.9.8
    "Clear the recent file list" : u"", # New in v2.6.9.8
    "&Exit" : u"終了(&E)",
    "Exit the program" : u"プログラムを終了",
    "&Edit" : u"編集(&E)",
    "Undo last text operation" : u"最後に行ったテキストの変更を元に戻す",
    "Redo last text operation" : u"最後に行ったテキストの変更をやり直す",
    "Cut the selected text" : u"選択されたテキストの切り取り",
    "Copy the selected text" : u"選択されたテキストのコピー",
    "Paste the selected text" : u"選択されたテキストの貼り付け",
    "Open a find text dialog box" : u"検索ダイアログボックスを開く",
    "Find..." : u"検索...",
    "Find next" : u"次を検索",
    "Find the next instance of given text" : u"次の候補を検索",
    "Find previous" : u"前を検索",
    "Find the previous instance of given text" : u"前の候補を検索",
    "Open a replace text dialog box" : u"置換ダイアログボックスを開く",
    "Replace..." : u"置換...",
    "Replace next" : u"次を置換",
    "Replace the next instance of given text" : u"次の候補を置換",
    "Select All" : u"すべて選択",
    "Select all the text" : u"テキストをすべて選択",
    "&Insert" : u"挿入(&I)",
    "Expand a snippet tag, or select a snippet from the list" : u"", # New in v2.5.0
    "Insert snippet" : u"", # New in v2.5.0
    "Choose a source file to insert into the text" : u"テキストに挿入するソースファイルを選択",
    "Insert source..." : u"ソースの挿入...",
    "Get a filename from a dialog box to insert into the text" : u"ダイアログボックスからファイル名を取得してテキストに挿入",
    "Insert filename..." : u"ファイル名の挿入...",
    "Choose a plugin file to insert into the text" : u"テキストに挿入するプラグインファイルを選択して下さい",
    "Insert plugin..." : u"プラグインの挿入...",
    "Insert a user-scripted slider into the text" : u"ユーザー定義スライダをテキストに挿入",
    "Insert user slider..." : u"ユーザースライダの挿入...",
    "Insert a tag which indicates a separator in the user slider window" : u"ユーザースライダウィンドウにセパレータを示すタグを挿入する",
    "Insert user slider separator" : u"ユーザースライダセパレータの挿入",
    "Insert the current frame number into the text" : u"現在のフレーム番号をテキストに挿入",
    "Add tags surrounding the selected text for toggling with the video preview" : u"ビデオプレビューをトグルするための選択されたテキストを囲むタグを追加",
    "Tag selection for toggling..." : u"", # New in v2.6.9.8
    "Clear all tags" : u"すべてのタグをクリア",
    "Clear all toggle tags from the text" : u"テキストからすべてのトグルタグをクリア",
    "Add Preview filter surrounding the selected lines" : u"", # New in v2.6.9.8
    "Preview filter" : u"", # New in v2.6.6.0
    "Indent the selected lines" : u"選択行のインデント",
    "Unindent the selected lines" : u"選択行のアンインデント",
    "Block comment" : u"ブロックコメント",
    "Comment or uncomment selected lines" : u"選択された行をコメント化/非コメント化",
    "Comment at start of a text style or uncomment" : u"テキストスタイルの冒頭でコメント/非コメント化",
    "Style comment" : u"スタイルコメント",
    "Toggle current fold" : u"現在の折り畳みをトグル",
    "Toggle the fold point On/OFF at the current line" : u"現在行で折り畳みポイントのオン/オフをトグル",
    "Toggle all fold points On/OFF" : u"すべての折り畳みポイントのオン/オフをトグル",
    "Toggle all folds" : u"すべての折り畳みをトグル",
    "Toggle text wrap" : u"", # New in v2.5.1.09
    "Toggle text wrap On/OFF" : u"", # New in v2.5.1.09
    "&AviSynth function" : u"AviSynth 関数(&A)",
    "Show list of filternames matching the partial text at the cursor" : u"カーソル位置に部分的なテキストにマッチするフィルタ名のリストを表示",
    "Autocomplete all" : u"すべて自動補完",
    "Disregard user's setting, show full list of filternames matching the partial text at the cursor" : u"ユーザー設定を無視して、カーソル位置の不完全なテキストにマッチするフィルタ名の完全なリストを表示",
    "Autocomplete parameter/filename" : u"", # New in v2.5.0
    "If the first characters typed match a parameter name, complete it. If they're typed on a string, complete the filename" : u"", # New in v2.5.0
    "Show calltip" : u"ツールチップの表示",
    "Show the calltip for the filter (only works if cursor within the arguments)" : u"フィルタのツールチップを表示（カーソルが引数の中にある場合のみ）",
    "Show function definition" : u"関数定義の表示",
    "Show the AviSynth function definition dialog for the filter" : u"このフィルタの AviSynth 関数定義ダイアログを表示する",
    "Filter help file" : u"フィルタのヘルプを表示",
    "Run the help file for the filter (only works if cursor within the arguments or name is highlighted)" : u"フィルタのヘルプを表示（カーソルが引数の中にあるか名前が強調されている場合のみ）",
    "Include functions defined in the current script in the filter database, only for this tab" : u"", # New in v2.5.1
    "Parse script for function definitions" : u"", # New in v2.5.1
    "&Miscellaneous" : u"その他(&M)",
    "Move line up" : u"1 行上へ移動",
    "Move the current line or selection up by one line" : u"現在の行か選択範囲の 1 行上へ移動する",
    "Move line down" : u"1行下へ移動",
    "Move the current line or selection down by one line" : u"現在の行か選択範囲の 1 行下へ移動する",
    "Copy the current script without any AvsP markings (user-sliders, toggle tags) to the clipboard" : u"現在のスクリプトを AvsP 独自のマーキング（ユーザースライダやトグルタグ）なしでクリップボードにコピーする",
    "Copy unmarked script to clipboard" : u"マークなしスクリプトをクリップボードにコピー",
    "Copy avisynth error to clipboard" : u"AviSynth エラーをクリップボードにコピー",
    "Copy the avisynth error message shown on the preview window to the clipboard" : u"プレビューウィンドウに表示された AviSynth エラーメッセージを",
    "Set selection as display filter..." : u"", # New in v2.6.9.8
    "Shows the display filter dialog with the selected text" : u"", # New in v2.6.9.8
    "&Video" : u"ビデオ(&V)",
    "Bookmarks" : u"ブックマーク",
    "Bookmarks to script" : u"", # New in v2.6.1.5
    "Bookmarks from script" : u"", # New in v2.6.1.5
    "Add/Remove bookmark" : u"ブックマークの追加/削除",
    "Mark the current frame on the frame slider" : u"現在のフレームをフレームスライダ上にマークする",
    "Clear tab bookmarks" : u"", # New in v2.6.6.0
    "Clears the current tab bookmarks" : u"", # New in v2.6.6.0
    "Clear all bookmarks Globally" : u"", # New in v2.6.6.0
    "Clears all bookmarks, clears also all tab bookmarks" : u"", # New in v2.6.6.0
    "Titled &bookmarks" : u"タイトル付きブックマーク(&b)",
    "Move the nearest titled bookmark to the current position. A historic title will be restored if it matches the condition." : u"最も近いタイトル付きのブックマークを現在の位置に移動する。条件にマッチした場合、削除済みタイトルは復元される。",
    "Move titled bookmark" : u"タイトル付きブックマークを移動",
    "Restore all historic titles" : u"すべての削除済みタイトルを復元",
    "Restore historic titles" : u"削除済みタイトルを復元",
    "Clear all historic titles" : u"すべての削除済みタイトルをクリア",
    "Clear historic titles" : u"削除済みタイトルをクリア",
    "Generate titles for untitled bookmarks by the pattern - 'Chapter %02d'" : u"タイトルなしのブックマークに 'Chapter %02d' というパターンでタイトルを生成する",
    "Set title (auto)" : u"タイトルの設定（自動）",
    "Edit title for bookmarks in a list table" : u"一覧表のブックマークのタイトルを編集",
    "Set title (manual)" : u"タイトルの設定（手動）",
    "Remove all title" : u"", # New in v2.6.6.0
    "Remove all title from the bookmarks" : u"", # New in v2.6.6.0
    "Not include this tab on any group" : u"", # New in v2.5.0
    "Add tab to this group" : u"", # New in v2.5.0
    "Clear current tab group" : u"", # New in v2.5.0
    "Clear all tab groups" : u"", # New in v2.5.0
    "Apply offsets" : u"", # New in v2.5.0
    "Use the difference between showed frames when the tabs were added to the group as offsets" : u"", # New in v2.5.0
    "Offset also bookmarks" : u"", # New in v2.5.1
    "Apply the offset also to the currently set bookmarks" : u"", # New in v2.5.1
    "&Navigate" : u"移動 (&N)",
    "Go to next bookmarked frame" : u"次のブックマークされたフレームへ移動",
    "Next bookmark" : u"次のブックマーク",
    "Go to previous bookmarked frame" : u"前のブックマークされたフレームへ移動",
    "Previous bookmark" : u"前のブックマーク",
    "Forward 1 frame" : u"1 フレーム進む",
    "Show next video frame (keyboard shortcut active when video window focused)" : u"次のフレームを表示（ビデオウィンドウ フォーカス時、キーボードショートカット有効）",
    "Backward 1 frame" : u"1 フレーム戻る",
    "Show previous video frame (keyboard shortcut active when video window focused)" : u"前のフレームを表示（ビデオウィンドウ フォーカス時、キーボードショートカット有効）",
    "Forward 1 second" : u"1 秒進む",
    "Show video 1 second forward (keyboard shortcut active when video window focused)" : u"1 秒先のフレームを表示（ビデオウィンドウ フォーカス時、キーボードショートカット有効）",
    "Backward 1 second" : u"1 秒戻る",
    "Show video 1 second back (keyboard shortcut active when video window focused)" : u"1 秒前のフレームを表示（ビデオウィンドウ フォーカス時、キーボードショートカット有効）",
    "Forward 1 minute" : u"1 分進む",
    "Show video 1 minute forward (keyboard shortcut active when video window focused)" : u"1 分先のフレームを表示（ビデオウィンドウ フォーカス時、キーボードショートカット有効）",
    "Backward 1 minute" : u"1 分戻る",
    "Show video 1 minute back (keyboard shortcut active when video window focused)" : u"1 分前のフレームを表示（ビデオウィンドウ フォーカス時、キーボードショートカット有効）",
    "Forward x units" : u"x 進む",
    "Jump forward by x units (you can specify x in the options dialog)" : u"x 先にジャンプする（x と単位はカスタムジャンプサイズのオプションで指定可能）",
    "Backwards x units" : u"x 戻る",
    "Jump backwards by x units (you can specify x in the options dialog)" : u"x 前にジャンプする（xと単位はカスタムジャンプサイズのオプションで指定可能）",
    "Go to first frame" : u"先頭フレームへ移動",
    "Go to first video frame (keyboard shortcut active when video window focused)" : u"先頭のビデオフレームへ移動する（ビデオウィンドウフォーカス時、キーボードショートカット有効）",
    "Go to last frame" : u"最終フレームへ移動",
    "Go to last video frame (keyboard shortcut active when video window focused)" : u"最終のビデオフレームへ移動する（ビデオウィンドウフォーカス時、キーボードショートカット有効）",
    "Go to last scrolled frame" : u"最後にスクロールされたフレームへ移動",
    "Last scrolled frame" : u"最後にスクロールされたフレーム",
    "Enter a video frame or time to jump to" : u"移動するビデオフレームの番号または時間を入力する",
    "Go to frame..." : u"フレームジャンプ",
    "&Play video" : u"ビデオを再生 (&P)",
    "Play/pause video" : u"ビデオを再生/停止",
    "Double the current playback speed" : u"現在の再生速度を2倍にする",
    "Increment speed" : u"速度を上げる",
    "Decrement speed" : u"速度を下げる",
    "Halve the current playback speed" : u"現在の再生速度を 1/2 にする",
    "Set the playback speed to the script frame rate" : u"再生速度をスクリプトのフレームレートに設定する",
    "Normal speed" : u"通常の速度",
    "Play the video as fast as possible without dropping frames" : u"ドロップフレームしない範囲の最高速度でビデオを再生する",
    "Maximum speed" : u"最大速度",
    "Loop playback for trim editor selections or at the end of the clip" : u"", # New in v2.6.9.8
    "Play loop" : u"", # New in v2.6.6.0
    "Use a separate thread for playback. If avisynth threads used, playback uses also threads" : u"", # New in v2.6.9.8
    "Use separate thread" : u"", # New in v2.6.9.8
    "Crop editor..." : u"クロップエディタ...",
    "Show the crop editor dialog" : u"クロップエディタのダイアログを表示",
    "&Trim selection editor" : u"トリム選択エディタ(&T)",
    "Show the trim selection editor dialog" : u"トリム選択エディタダイアログを表示",
    "Show trim selection editor" : u"トリム選択エディタの表示",
    "Set a selection startpoint (shows the trim editor if not visible)" : u"選択開始位置を設定する（非表示ならトリムエディタを表示）",
    "Set selection startpoint" : u"選択開始位置の設定",
    "Set a selection endpoint (shows the trim editor if not visible)" : u"選択終了位置を設定する（非表示ならトリムエディタを表示）",
    "Set selection endpoint" : u"選択終了位置の設定",
    "Move selections before the current frame" : u"", # New in v2.5.1
    "The current selections are cut from the timeline and inserted before the current frame. Bookmarks are shifted accordingly." : u"", # New in v2.5.1
    "Move selections after the current frame" : u"", # New in v2.5.1
    "The current selections are cut from the timeline and inserted after the current frame. Bookmarks are shifted accordingly." : u"", # New in v2.5.1
    "Add bookmark to trim intersections" : u"", # New in v2.6.6.0
    "Mark trim points" : u"", # New in v2.6.6.0
    "Save the selections into the script" : u"", # New in v2.6.6.0
    "Selections to script" : u"", # New in v2.6.6.0
    "Read the selections from the script" : u"", # New in v2.6.6.0
    "Selections from script" : u"", # New in v2.6.6.0
    "Clear tab selections" : u"", # New in v2.6.6.0
    "Clear tab trim editor selections (hide the trim editor if visible)" : u"", # New in v2.6.6.0
    "Clear all selections Globally" : u"", # New in v2.6.6.0
    "Clear all the tab trim editor selections (hide the trim editor if visible)" : u"", # New in v2.6.6.0
    "Timeline range" : u"", # New in v2.6.9.8
    "Zoom video preview to 25%" : u"ビデオプレビューを 25% にズーム",
    "Zoom video preview to 50%" : u"ビデオプレビューを 50% にズーム",
    "Zoom video preview to 100% (normal)" : u"ビデオプレビューを 100% にズーム（標準）",
    "Zoom video preview to 200%" : u"ビデオプレビューを 200% にズーム",
    "Zoom video preview to 300%" : u"ビデオプレビューを 300% にズーム",
    "Zoom video preview to 400%" : u"ビデオプレビューを 400% にズーム",
    "Zoom video preview to fill the entire window" : u"ウィンドウ全体に合わせてビデオプレビューをズーム",
    "Zoom video preview to fit inside the window" : u"プレビューウィンドウの内側に収まるようにビデオプレビューをズーム",
    "Enlarge preview image to next zoom level. Not work under 'Fill window' or 'Fit inside window'" : u"プレビュー画像を次のズームレベルに拡大。「ウィンドウに合わせる」/「プレビューウィンドウに合わせる」では機能しない",
    "Shrink preview image to previous zoom level. Not work under 'Fill window' or 'Fit inside window'" : u"プレビュー画像を前のズームレベルに縮小。「ウィンドウに合わせる」/「プレビューウィンドウに合わせる」では機能しない",
    "Antialiasing" : u"", # New in v2.6.6.0
    "If zoom not 100 %, the preview is drawing antialiased" : u"", # New in v2.6.6.0
    "&Display" : u"", # New in v2.6.9.8
    "Enable/Disable the display filter" : u"", # New in v2.6.9.8
    "Display filter" : u"", # New in v2.6.9.8
    "Select display filter..." : u"", # New in v2.6.9.8
    "Select the display filter from template" : u"", # New in v2.6.9.8
    "Edit current display filter..." : u"", # New in v2.6.9.8
    "Edit the current display filter" : u"", # New in v2.6.9.8
    "&Flip" : u"反転(&F)",
    "Flip video preview upside down" : u"ビデオプレビューを天地逆さまに反転する",
    "Flip video preview from left to right" : u"ビデオプレビューを左から右に反転する",
    "&YUV -> RGB" : u"",
    "Swap chroma channels (U and V)" : u"色差チャンネルをスワップ",
    "Get the coefficients from source or script, if the matrix available" : u"", # New in v2.6.9.8
    "Read from source or script" : u"", # New in v2.6.9.8
    "Set matrix default value (options) if matrix not found" : u"", # New in v2.6.9.8
    "Reset matrix if not found" : u"", # New in v2.6.9.8
    "Use BT.709 coefficients for HD, BT.601 for SD" : u"", # New in v2.6.9.8
    "Use BT.709 coefficients" : u"BT.709 係数を使用",
    "Use BT.601 coefficients" : u"BT.601 係数を使用",
    "Use limited range (default)" : u"リミテッドレンジを使用（デフォルト）",
    "Use full range" : u"フルレンジを使用",
    "For YV12 only, assume it is progressive (default)" : u"YV12 についてのみ、プログレッシブと仮定（デフォルト）",
    "For YV12 only, assume it is interlaced" : u"YV12 についてのみ、インターレースと仮定",
    "Current matrix to script" : u"", # New in v2.6.9.8
    "Write the current matrix to script. If no matrix found this matrix is used" : u"", # New in v2.6.9.8
    "Read the matrix now" : u"", # New in v2.6.9.8
    "Try to get the matrix from source or script" : u"", # New in v2.6.9.8
    "Globally to default" : u"", # New in v2.6.9.8
    "Reset all scripts to Resolution-based" : u"", # New in v2.6.9.8
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
    "Save image as..." : u"名前を付けて画像を保存...",
    "Save the current frame as image file. If you not change the frame number, Quick save image uses the name." : u"", # New in v2.6.6.0
    "Quick save image" : u"", # New in v2.5.0
    "Save the current frame with a default filename, overwriting the file if already exists. Press CTRL to reset the default name formatting" : u"", # New in v2.6.6.0
    "Copy image to clipboard" : u"", # New in v2.5.0
    "Copy the current frame to the clipboard as a bitmap" : u"", # New in v2.5.0
    "Force the script to reload and refresh the video frame" : u"スクリプトを再読込して、ビデオフレームを最新の状態にする",
    "Refresh preview" : u"プレビューの更新",
    "Release all open videos from memory" : u"開いたすべてのビデオをメモリから解放する",
    "Release all videos from memory" : u"すべてのビデオをメモリから解放",
    "Snapshot" : u"", # New in v2.6.6.0
    "Take snapshot 1" : u"", # New in v2.6.6.0
    "Make bitmap and script snapshot" : u"", # New in v2.6.6.0
    "Take snapshot 2" : u"", # New in v2.6.6.0
    "Show or hide snapshot 1" : u"", # New in v2.6.6.0
    "Show/hide snapshot 1" : u"", # New in v2.6.6.0
    "Show or hide snapshot 2" : u"", # New in v2.6.6.0
    "Show/hide snapshot 2" : u"", # New in v2.6.6.0
    "Copy snap shot 1 to new tab" : u"", # New in v2.6.6.0
    "New tab from snapshot 1" : u"", # New in v2.6.6.0
    "Copy snap shot 2 to new tab" : u"", # New in v2.6.6.0
    "New tab from snapshot 2" : u"", # New in v2.6.6.0
    "Automatically takes snapshot 2 on clip refresh" : u"", # New in v2.6.9.8
    "Auto take snapshot 2" : u"", # New in v2.6.9.8
    "Clear tab snapshots" : u"", # New in v2.6.6.0
    "Clears the current tab snapshots" : u"", # New in v2.6.6.0
    "Clear all snapshots Globally" : u"", # New in v2.6.6.0
    "Clears all snapshots Globally" : u"", # New in v2.6.6.0
    "Preview filter off" : u"", # New in v2.6.6.0
    "Preview filter 1" : u"", # New in v2.6.6.0
    "1" : u"", # New in v2.6.6.0
    "Preview filter 2" : u"", # New in v2.6.6.0
    "2" : u"", # New in v2.6.6.0
    "Preview filter 3" : u"", # New in v2.6.6.0
    "3" : u"", # New in v2.6.6.0
    "Preview filter 4" : u"", # New in v2.6.6.0
    "4" : u"", # New in v2.6.6.0
    "Preview filter 5" : u"", # New in v2.6.6.0
    "5" : u"", # New in v2.6.6.0
    "Save preview filters" : u"", # New in v2.6.6.0
    "Save preview filters for later use" : u"", # New in v2.6.6.0
    "Write all preview filters to script" : u"", # New in v2.6.6.0
    "Write all to script" : u"", # New in v2.6.6.0
    "Write to script" : u"", # New in v2.6.6.0
    "Write Preview filter to script" : u"", # New in v2.6.6.0
    "Shows the selected and optional the next or previous tab in one view (video width and height must be the same)" : u"", # New in v2.6.6.0
    "Split View on/off" : u"", # New in v2.6.6.0
    "Expands the left shift area of the video window" : u"", # New in v2.6.6.0
    "Toggle extended left move" : u"", # New in v2.5.1.09
    "Save/Restore last view position and zoom factor on tab change" : u"", # New in v2.6.6.0
    "Save view pos on tab change" : u"", # New in v2.6.1.5
    "Additional" : u"", # New in v2.6.9.8
    "Show/Hide the preview" : u"プレビューの表示/非表示",
    "Toggle the video preview" : u"ビデオプレビューのトグル",
    "Switch focus between the video preview and the text editor" : u"ビデオプレビューとテキストエディタの間でフォーカスを切り替える。",
    "Switch video/text focus" : u"フォーカスの切り替え",
    "Show/hide the slider sidebar (double-click the divider for the same effect)" : u"スライダのサイドバーの表示/非表示を切り替える（区切り線をダブルクリックでも同じ効果）",
    "Toggle the slider sidebar" : u"スライダのサイドバーのトグル",
    "Toggle preview placement" : u"", # New in v2.5.1
    "When not using a separate window for the video preview, toggle between showing it at the bottom (default) or to the right" : u"", # New in v2.5.1
    "Tools" : u"", # New in v2.6.6.0
    "Request every video frame once (analysis pass for two-pass filters)" : u"すべてのビデオフレームを一回リクエスト（2 パスフィルタの解析パス）",
    "Run analysis pass" : u"解析パスを実行",
    "External player" : u"外部プレーヤー",
    "Play the current script in an external program" : u"現在のスクリプトを外部プログラムで再生",
    "External tool arg1" : u"", # New in v2.6.6.0
    "Run the current script with an external program and arg1" : u"", # New in v2.6.6.0
    "External tool arg2" : u"", # New in v2.6.6.0
    "Run the current script with an external program and arg2" : u"", # New in v2.6.6.0
    "Show/Hide the properties window" : u"", # New in v2.6.9.8
    "Show information about the video in a dialog box" : u"ビデオに関する情報をダイアログボックスに表示",
    "Video information" : u"ビデオ情報",
    "&Options" : u"オプション(&O)",
    "Always on top" : u"常に前面に表示",
    "Keep this window always on top of others" : u"このウィンドウを他のウィンドウの前面に表示する",
    "If the video preview is detached, keep it always on top of other windows" : u"ビデオプレビューが分離された場合、常に他のウィンドウの前面に表示する",
    "Video preview always on top" : u"ビデオプレビューを常に前面に表示",
    "Disable video preview" : u"ビデオプレビューを無効化",
    "If checked, the video preview will not be shown under any circumstances" : u"チェックすると、ビデオプレビューが常に非表示になる",
    "Hide the video window scrollbars" : u"", # New in v2.6.9.8
    "Hide video window scrollbars" : u"", # New in v2.6.9.8
    "Accessing AviSynth in threads" : u"", # New in v2.6.9.8
    "Use threads when accessing avisynth (load/release clip and get frame)" : u"", # New in v2.6.9.8
    "For info read the readme_threads.txt" : u"", # New in v2.6.9.8
    "Use advanced frame thread" : u"", # New in v2.6.9.8
    "AvsPmod should normally be closed after a thread has been canceled by the user. This option tries to assign the clip to the script after the thread has internaly finished." : u"", # New in v2.6.9.8
    "On cancel assign the clip later" : u"", # New in v2.6.9.8
    "Associate .avs files with AvsPmod" : u"", # New in v2.6.6.0
    "Configure this computer to open .avs files with AvsP when double-clicked. Run again to disassociate" : u"ダブルクリック時に AVS ファイルを AvsP を使って開くようにこのコンピュータを設定する。関連付けを解除するにはもう一度実行して下さい",
    "Edit the various AviSynth script fonts and colors" : u"さまざまな AviSynth スクリプトのフォントと色を編集する",
    "Fonts and colors..." : u"フォントと色...",
    "Make fonts && colors backup" : u"", # New in v2.6.9.8
    "Make script fonts and colors backup" : u"", # New in v2.6.1.5
    "Load fonts && colors backup" : u"", # New in v2.6.9.8
    "Restores script fonts and colors from backup" : u"", # New in v2.6.1.5
    "AviSynth function definition..." : u"AviSynth 関数の定義...",
    "Edit the extension-based templates for inserting sources" : u"ソースの挿入のための拡張子別テンプレートを編集",
    "Extension templates..." : u"拡張子別テンプレート...",
    "Display filters..." : u"", # New in v2.6.9.8
    "Edit display filters" : u"", # New in v2.6.9.8
    "Apply filters..." : u"", # New in v2.6.9.8
    "Edit insertable timeline selections filters" : u"", # New in v2.6.9.8
    "Snippets..." : u"", # New in v2.5.0
    "Edit insertable text snippets" : u"", # New in v2.5.0
    "Configure the program keyboard shortcuts" : u"プログラムのキーボードショートカットを編集する",
    "Keyboard shortcuts..." : u"キーボードショートカット...",
    "Configure program settings" : u"プログラムの設定を行う",
    "Program settings..." : u"プログラム設定...",
    "&Help" : u"ヘルプ(&H)",
    "Animated tutorial" : u"動画チュートリアル",
    "View an animated tutorial for AvsP (from the AvsP website)" : u"AvsP の動画チュートリアルをみる（AvsP ホームページから）",
    "Learn more about AvsP text features (from the AvsP website)" : u"AvsP のテキスト機能についてもっと学ぶ（AvsP ホームページから）",
    "Text features" : u"テキスト機能",
    "Learn more about AvsP video features (from the AvsP website)" : u"AvsP のビデオ機能についてもっと学ぶ（AvsP ホームページから）",
    "Video features" : u"ビデオ機能",
    "Learn more about AvsP user sliders (from the AvsP website)" : u"AvsP のユーザースライダについてもっと学ぶ（AvsP ホームページから）",
    "User sliders" : u"ユーザースライダ",
    "Learn more about AvsP macros (from the AvsP website)" : u"AvsP のマクロについてもっと学ぶ（AvsP ホームページから）",
    "Macros" : u"マクロ",
    "Avisynth help" : u"AviSynth ヘルプ",
    "Open the avisynth help html" : u"AviSynth のヘルプを開く",
    "Open the Preview filter examples" : u"", # New in v2.6.6.0
    "Preview filter example" : u"", # New in v2.6.6.0
    "Accessing in threads readme" : u"", # New in v2.6.9.8
    "Open the Access in threads readme" : u"", # New in v2.6.9.8
    "Apply filters readme" : u"", # New in v2.6.9.8
    "Open the apply filters readme" : u"", # New in v2.6.9.8
    "DPI info" : u"", # New in v2.6.9.8
    "DPI information" : u"", # New in v2.6.6.0
    "Displays the available memory in the status bar" : u"", # New in v2.6.9.8
    "Show available system memory" : u"", # New in v2.6.9.8
    "Open Avisynth plugins folder" : u"AviSynth のプラグインフォルダを開く",
    "Open the avisynth plugins folder, or the last folder from which a plugin was loaded" : u"AviSynth プラグインフォルダまたは最後にプラグインが読み込まれたフォルダを開く",
    "Changelog" : u"更新履歴",
    "Open the changelog file" : u"更新履歴ファイルを開く",
    "About this program" : u"このプラグラムについて",
    "About AvsPmod" : u"AvsPmod について",
    "Jump back. Right click for options" : u"", # New in v2.6.9.8
    "Jump forward. Right click for options" : u"", # New in v2.6.9.8
    "Play/pause video. Right click for options." : u"", # New in v2.6.6.0
    "Run the script with an external program" : u"外部プログラムを使ってスクリプトを実行する",
    "Run the selected tool" : u"選択されたツールを実行",
    "&Tools" : u"ツール(&T)",
    "A macro check item" : u"マクロチェック項目",
    "A macro radio item" : u"マクロ選択項目",
    "Run selected macro" : u"選択されたマクロを実行",
    "View the readme for making macros" : u"マクロ作成に関するリードミーを読む",
    "Open macros folder" : u"マクロフォルダを開く",
    "Open the macros folder" : u"マクロフォルダを開く",
    "&Macros" : u"マクロ(&M)",
    "Close" : u"閉じる",
    "Close all the other" : u"", # New in v2.6.1.5
    "Rename" : u"名前を変更",
    "Group" : u"", # New in v2.5.0
    "Save" : u"保存",
    "Save as..." : u"名前を付けて保存...",
    "Reload" : u"再読み込み",
    "Open directory" : u"", # New in v2.5.1
    "Release video memory" : u"", # New in v2.6.1.5
    "Release all other video memory" : u"", # New in v2.6.1.5
    "Tab change loads bookmarks" : u"", # New in v2.6.1.5
    "Copy to new tab" : u"新しいタブにコピー",
    "Split View insert tab" : u"", # New in v2.6.6.0
    "Auto preview" : u"", # New in v2.6.6.0
    "Reposition to" : u"位置の変更",
    "Disable refresh" : u"", # New in v2.6.9.8
    "Custom frame range" : u"", # New in v2.6.9.8
    "Frame range 30 to n.. or set start,end separated by comma" : u"", # New in v2.6.9.8
    "Percent" : u"", # New in v2.6.9.8
    "Show nothing" : u"", # New in v2.6.9.8
    "Show time" : u"", # New in v2.6.9.8
    "Auto scroll" : u"", # New in v2.6.9.8
    "Auto reset" : u"", # New in v2.6.9.8
    "Custom..." : u"", # New in v2.6.9.8
    "Crop editor" : u"クロップエディタ",
    "You can drag the crop regions with the left mouse button when this dialog is visible, cropping the edge closest to the initial mouse click." : u"ダイアログ表示時、左マウスボタンでクロップ領域をドラッグ可能 （最初のマウスクリックに最も近い端をクロップ）。",
    "Auto-crop" : u"オートクロップ",
    "Samples" : u"サンプル",
    "At script end" : u"スクリプトの最後に",
    "At script cursor" : u"カーソル位置に",
    "Copy to clipboard" : u"クリップボードにコピー",
    "Insert Crop() command:" : u"Crop() コマンドを挿入:",
    "Apply" : u"適用",
    "Trim editor" : u"トリムエディタ",
    "Selection options" : u"選択オプション",
    "Keep selected regions" : u"選択された範囲を残す",
    "Keep unselected regions" : u"選択された範囲以外を残す",
    "Mark video frames inside/outside selection" : u"選択範囲の内/外のビデオフレームにマークを付ける",
    "Use Dissolve() with overlap frames:" : u"Dissolve() を使用（オーバラップするフレーム数）:",
    "Single clips (c0..cn) with prefix:" : u"", # New in v2.6.1.5
    "Insert Trim() commands: " : u"", # New in v2.6.1.5
    "Insert clips commands: " : u"", # New in v2.6.1.5
    "Insert Dissolve(trim,) commands: " : u"", # New in v2.6.1.5
    "Insert Dissolve(clips,) commands: " : u"", # New in v2.6.1.5
    "Use the buttons which appear on the video slider handle to create the frame selections to trim." : u"選択範囲の生成にはビデオスライダのつまみの上にあるボタンを使用してください。",
    "Hide timeline numbers" : u"", # New in v2.6.9.8
    "Clear" : u"クリア",
    "The script's directory doesn't exist anymore!" : u"", # New in v2.5.1
    "Print Preview" : u"印刷プレビュー",
    "Failed to create print preview" : u"印刷プレビューの作成に失敗しました",
    "Print Error" : u"印刷エラー",
    "There was an error when printing.\nCheck that your printer is properly connected." : u"印刷時にエラーが発生しました。\nプリンタが正しく接続されているか確認して下さい。",
    "Printer Error" : u"プリンタエラー",
    "Damaged session file" : u"破損したセッションファイル",
    "File does not exist!" : u"ファイルが見つかりませんでした！",
    "Select a file" : u"ファイルを選択",
    "Create a separator label" : u"セパレータラベルの生成",
    "Enter separator label" : u"セパレータラベルの入力",
    "Enter tag name:" : u"タグ名を入力:",
    "Tag definition" : u"タグの定義",
    "Chapter" : u"チャプタ",
    "Set title for bookmarks" : u"ブックマークのタイトルを設定",
    "Title" : u"タイトル",
    "Frame No." : u"フレーム番号",
    "Time **" : u"時間 **",
    "Left-click on a selected item or double-click to edit.\n\n*  RED - a historic title, not a real bookmark.\n** Time may be unavailable or incorrect before preview refreshed." : u"編集するには、選択されたアイテムの上で左クリックするかダブルクリックしてください。\n\n*  赤字 - 削除済みタイトル。実際のブックマークではない。\n** プレビュー更新前は、時間は利用不可または不正確な可能性あり。",
    "Image saved to \"{0}\"" : u"", # New in v2.5.0
    "No image to save" : u"保存する画像がありません",
    "Error requesting frame {number}" : u"", # New in v2.5.0
    "Couldn't open clipboard" : u"", # New in v2.5.0
    "Cannot use crop editor unless bit depth is set to 8" : u"", # New in v2.5.1
    "No filters found, clear the current saved filters?" : u"", # New in v2.6.6.0
    "Preview filters" : u"", # New in v2.6.6.0
    "Available Memory: {} MB" : u"", # New in v2.6.9.8
    "Snapshot %d" : u"", # New in v2.6.9.8
    "Error snapshot %d" : u"", # New in v2.6.9.8
    "Empty snapshot script" : u"", # New in v2.6.9.8
    "Display" : u"", # New in v2.6.9.8
    "Edit current display filter" : u"", # New in v2.6.9.8
    "YUV -> RGB" : u"", # New in v2.6.9.8
    "Cannot read the matrix. Clip not initialized" : u"", # New in v2.6.9.8
    "Cannot change bit depth while crop editor is open!" : u"", # New in v2.5.1
    "Interleaved RGB48" : u"", # New in v2.5.1
    "Play video" : u"", # New in v2.6.6.0
    "Avisynth not returned thread still running.\n{0}" : u"", # New in v2.6.9.8
    "Avisynth not returned frame thread still running.\n{0}" : u"", # New in v2.6.9.8
    "Avisynth not returned play thread still running.\n{0}" : u"", # New in v2.6.9.8
    "Error loading the script" : u"スクリプトの読み込みエラー",
    "Starting analysis pass..." : u"解析パスを開始しています...",
    "Average %#.4g fps\nFrame %s/%s (%#.4g fps)" : u"", # New in v2.6.6.0
    "Finished (%s fps average)\n*** live and let live ***" : u"", # New in v2.6.6.0
    "Frame size:" : u"フレームサイズ:",
    "Length:" : u"長さ:",
    "Frame rate:" : u"フレームレート:",
    "Colorspace:" : u"色空間:",
    "Bit depth:" : u"", # New in v2.6.1.5
    "Field or frame based:" : u"フィールドベース/フレームベース:",
    "Parity:" : u"パリティ:",
    "Audio" : u"音声",
    "Channels:" : u"チャンネル:",
    "Hz" : u"",
    "Sampling rate:" : u"サンプリングレート:",
    "Sample type:" : u"サンプリング形式:",
    "bits" : u"ビット",
    "samples" : u"サンプル",
    "Bookmarks:" : u"", # New in v2.6.9.8
    "Timeline selections:" : u"", # New in v2.6.9.8
    "Could not find the macros folder!" : u"マクロフォルダが見つかりませんでした！",
    "Failed to import the selected tool" : u"選択されたツールのインポートに失敗しました",
    "Basic (1)" : u"", # New in v2.5.1
    "Override all fonts to use a specified monospace font (no effect on scrap window)" : u"すべてのフォントに優先して指定された等幅フォントを使用（スクラップウィンドウには無効）",
    "Use monospaced font:" : u"等幅フォントを使用",
    "Default:" : u"デフォルト:",
    "Comment:" : u"コメント:",
    "Comment special extension #>:" : u"", # New in v2.6.9.8
    "Block Comment:" : u"ブロックコメント:",
    "__END__ Comment:" : u"__END__ コメント:",
    "Number:" : u"数値:",
    "String:" : u"文字列:",
    "Triple-quoted string:" : u"三重クオート文字列:",
    "Assignment:" : u"", # New in v2.5.0
    "Operator:" : u"演算子:",
    "Basic (2)" : u"", # New in v2.5.1
    "Internal filter:" : u"内蔵フィルタ:",
    "External filter:" : u"外部フィルタ:",
    "Internal function:" : u"内蔵関数:",
    "User defined function:" : u"ユーザー定義関数:",
    "Unknown function:" : u"", # New in v2.5.0
    "Clip property:" : u"クリップのプロパティ:",
    "Parameter:" : u"", # New in v2.5.0
    "AviSynth data type:" : u"AviSynth データ型:",
    "AviSynth keyword:" : u"AviSynth キーワード:",
    "AvsP user slider:" : u"AvsP ユーザースライダ:",
    "Advanced" : u"高度な設定",
    "Incomplete string:" : u"不完全な文字列:",
    "Syntax highlight strings which are not completed in a single line differently" : u"",
    "Brace highlight:" : u"波括弧の強調:",
    "Bad brace:" : u"不当な波括弧:",
    "Bad number:" : u"不当な数字:",
    "Margin line numbers:" : u"欄外の行番号:",
    "Miscellaneous word:" : u"その他のワード:",
    "Calltip:" : u"コールチップ:",
    "Calltip highlight:" : u"コールチップの強調:",
    "Cursor:" : u"カーソル:",
    "If checked, highlight also foreground" : u"", # New in v2.5.1
    "Selection highlight:" : u"セクションの強調:",
    "Current line highlight:" : u"現在行の強調:",
    "Highlight the line that the caret is currently in" : u"現在キャレットがある行を強調",
    "Fold margin:" : u"折り畳みの余白:",
    "Advanced 2" : u"", # New in v2.6.9.8
    "Scrap window:" : u"", # New in v2.6.9.8
    "Properties window:" : u"", # New in v2.6.9.8
    "Slider window:" : u"", # New in v2.6.9.8
    "Slider window text field:" : u"", # New in v2.6.9.8
    "Slider window default value:" : u"", # New in v2.6.9.8
    "Use another color for the sliders background" : u"", # New in v2.6.9.8
    "Use sparate slider background:" : u"", # New in v2.6.9.8
    "Slider window extras (Snapshot):" : u"", # New in v2.6.9.8
    "Information" : u"情報",
    "Settings have been read from backup file\n" : u"", # New in v2.6.1.5
    "File extension shouldn't contain dots!" : u"", # New in v2.5.1
    "Insert aborted:" : u"挿入中止:",
    "Edit extension-based templates" : u"拡張子ベースのテンプレートを編集",
    "File extension" : u"ファイル拡張子",
    "Template" : u"テンプレート",
    "This info is used for inserting sources based on file extensions." : u"この情報は、ファイル拡張子に基づいてソースを挿入するために使用されます。",
    "Any instances of *** in the template are replaced with the filename." : u"テンプレート内の *** は、ファイル名に置換されます。",
    "(If you want relative paths instead of the full filename, use [***].)" : u"（フルパスではなく相対パスを使いたいなら、[***] を使用して下さい。）",
    "Only alphanumeric and underscores allowed!" : u"", # New in v2.5.0
    "Tag" : u"", # New in v2.5.0
    "Snippet" : u"", # New in v2.5.0
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
    "Associating .avs files will write to the windows registry." : u".avs ファイルの関連付けを Windows レジストリに書き込む。",
    "Do you wish to continue?" : u"続行しますか？",
    "Associate avs files for all users?" : u"AVS ファイルをすべてのユーザーに関連付ける",
    "Disassociate avs files for all users?" : u"すべてのユーザーの AVS ファイルへの関連付けを解除する",
    " Admin rights are needed." : u" 管理者権限が必要",
    "Above keys are built-in editing shortcuts. If item is checked,\nit will not be overrided by a menu shortcut in script window." : u"上記のキーは、組み込みの編集ショートカットです。チェックされた項目は、\nスクリプトウィンドウのメニューショートカットによって変更されません。",
    "* This shortcut is active only when video window has focus.\n~ This shortcut is active only when script window has focus." : u"* このショートカットは、ビデオウィンドウにフォーカスしている時のみ有効です。\n~ このショートカットは、スクリプトウィンドウにフォーカスしている時のみ有効です。",
    "Could not find the Avisynth plugins folder!" : u"AviSynth プラグインフォルダが見つかりませんでした！",
    "Could not find %(readme)s!" : u"%(readme)s が見つかりませんでした！",
    "Could not find %(changelog)s!" : u"%(changelog)s が見つかりませんでした！",
    "Could not find %(example)s!" : u"", # New in v2.6.6.0
    "{prog_name} v{version} ({arch})" : u"", # New in v2.5.1
    "AvsP Website" : u"AvsP ホームページ",
    "AvsPmod Website" : u"", # New in v2.5.1
    "Active thread on Doom9's forum" : u"Doom9 フォーラム AvsP スレッド",
    "This program is freeware under the GPL license." : u"このプログラムは、GPL ライセンスのフリーウェアです。",
    "Input a frame number or time (hr:min:sec) and hit Enter. Right-click to retrieve from history. Or input a text and set the bookmark title." : u"", # New in v2.6.9.8
    "Drop frames" : u"ドロップフレーム",
    "Half speed" : u"", # New in v2.6.6.0
    "Custom unit" : u"", # New in v2.6.9.8
    "1 Minute" : u"", # New in v2.6.9.8
    "1 Second" : u"", # New in v2.6.9.8
    "1 Frame" : u"", # New in v2.6.9.8
    "bookmark highlight color..." : u"", # New in v2.6.6.0
    "selection highlight color..." : u"", # New in v2.6.6.0
    "set colors" : u"", # New in v2.6.9.8
    "bell at bookmarks" : u"", # New in v2.6.1.5
    "highlight bookmarks" : u"", # New in v2.6.1.5
    "Set bookmark title" : u"", # New in v2.6.6.0
    "copy as time" : u"時間のコピー",
    "copy" : u"コピー",
    "paste" : u"貼り付け",
    "clear history" : u"履歴のクリア",
    "On join filters, the first line must not begin with" : u"", # New in v2.6.9.8
    "Frames: %i" : u"", # New in v2.6.9.8
    "Apply filter" : u"", # New in v2.6.9.8
    "All as trim" : u"", # New in v2.6.9.8
    "Add as trim" : u"", # New in v2.6.9.8
    "Timeline to trims" : u"", # New in v2.6.9.8
    "Timeline to clips" : u"", # New in v2.6.9.8
    "Remove" : u"", # New in v2.6.9.8
    "Remove all" : u"", # New in v2.6.9.8
    "Remove all other" : u"", # New in v2.6.9.8
    "Trim editor..." : u"", # New in v2.6.9.8
    "Cannot switch tabs while crop editor is open!" : u"クロップエディタを開いている間はタブを切り替えることが出来ません！",
    "Cannot switch tabs while trim editor is open!" : u"トリムエディタを開いている間はタブを切り替えることが出来ません！",
    "Invalid crop values detected.  Continue?" : u"無効なクロップ値が検出されました。続行しますか？",
    "Select autocomplete keywords" : u"自動補完キーワードの選択",
    "select all" : u"すべて選択",
    "select none" : u"選択解除",
    "exclude long names" : u"ロングネームを除外",
    "Customize the video status bar message" : u"ビデオステータスバーのメッセージをカスタマイズ",
    "Video status bar message:" : u"ビデオステータスバーメッセージ",
    "Legend" : u"凡例",
    "Current frame" : u"現在のフレーム",
    "Framecount" : u"フレーム数",
    "Current time" : u"現在の時間",
    "Total time" : u"総時間",
    "Width" : u"幅",
    "Height" : u"高さ",
    "Aspect ratio" : u"アスペクト比",
    "Framerate" : u"フレームレート",
    "Framerate numerator" : u"フレームレート分子",
    "Framerate denominator" : u"フレームレート分母",
    "Colorspace" : u"色空間",
    "Bits per component" : u"", # New in v2.6.1.5
    "Field or frame based" : u"フィールド/フレームベース",
    "Parity" : u"パリティ",
    "Parity short (BFF or TFF)" : u"パリティ 省略形（BFF/TFF）",
    "Audio rate" : u"音声周波数",
    "Audio length" : u"音声の長さ",
    "Audio channels" : u"音声チャンネル",
    "Audio bits" : u"音声ビット数",
    "Audio type (Integer or Float)" : u"音声形式（整数/浮動小数）",
    "Pixel position (cursor based)" : u"ピクセル座標（カーソルベース）",
    "Pixel hex color (cursor based)" : u"ピクセル 16 進数カラー（カーソルベース）",
    "Pixel rgb color (cursor based)" : u"ピクセル RGB カラー（カーソルベース）",
    "Pixel yuv color (cursor based)" : u"ピクセル YUV カラー（カーソルベース）",
    "Pixel color (auto-detect colorspace)" : u"ピクセルカラー（自動検出色空間）",
    "Display YUV -> RGB conversion" : u"", # New in v2.6.9.8
    "Program zoom" : u"プログラムズーム",
    "Bookmark title" : u"ブックマークタイトル",
    "Note: The \"\\t\\t\" or \"\\T\\T\" is used to separate the left and right portions of the status bar\n         message." : u"註: \"\\t\\t\" または \"\\T\\T\" はステータスバーメッセージの左部分と右部分を分割するために\n使用されます。",
    "Slider update immediately" : u"", # New in v2.6.6.0
    "A macro is still running. Close anyway?" : u"マクロ実行中です。それでも閉じますか？",
    "A clip thread is still running. Close anyway?" : u"", # New in v2.6.9.8
    "Save changes before closing?" : u"閉じる前に変更を保存しますか？",
    "Cannot create a new tab while crop editor is open!" : u"クロップエディタを開いている間は新しいタブを作成することが出来ません！",
    "Cannot create a new tab while trim editor is open!" : u"トリムエディタを開いている間は新しいタブを作成することが出来ません！",
    "Source files" : u"ソースファイル",
    "Open a script or source" : u"スクリプトまたはソースを開く",
    "Reload the file and lose the current changes?" : u"ファイルを再読込すると現在の変更は失われますが、よろしいですか？",
    "%d Bookmarks imported" : u"", # New in v2.6.1.5
    "Open this file" : u"このファイルを開く",
    "Save session before closing all tabs?" : u"すべてのタブを閉じる前にセッションを保存しますか？",
    "Save current script" : u"現在のスクリプトを保存",
    "Directory %(dirname)s does not exist!" : u"ディレクトリ %(dirname)s は存在しません！",
    "The saved script has changed because AvsP marked section added" : u"", # New in v2.6.9.8
    "The saved script has changed because sliders or toggle tags and filters are removed" : u"", # New in v2.6.9.8
    "Error saving the script: %s" : u"", # New in v2.6.9.8
    "Script has no text!" : u"", # New in v2.5.0
    "HTML files" : u"", # New in v2.5.0
    "Load a session" : u"セッションの読み込み",
    "File has been modified since the session was saved. Reload?" : u"セッションが保存されてからファイルが変更されました。再読込しますか？",
    "Save the session" : u"セッションの保存",
    "Save current frame" : u"現在のフレームを保存",
    "Introduce the JPEG Quality (0-100)" : u"", # New in v2.5.0
    "JPEG Quality" : u"", # New in v2.5.0
    "Insert a source" : u"ソースの挿入",
    "All supported plugins" : u"すべての対応プラグイン",
    "AviSynth plugins" : u"AviSynth プラグイン",
    "VirtualDub plugins" : u"VirtualDub プラグイン",
    "VFAPI plugins" : u"VFAPI プラグイン",
    "Script import" : u"", # New in v2.6.1.5
    "AvxSynth plugins" : u"AvxSynth プラグイン",
    "Insert a plugin" : u"プラグインの挿入",
    "Line: %(line)i  Col: %(col)i" : u"行: %(line)i  列: %(col)i",
    "Frame Based" : u"フレームベース",
    "Field Based" : u"フィールドベース",
    "Bottom Field First" : u"ボトムフィールドファースト",
    "BFF" : u"",
    "Top Field First" : u"トップフィールドファースト",
    "TFF" : u"",
    "Integer" : u"整数",
    "Float" : u"浮動小数点数",
    "pos" : u"座標",
    "*hex" : u"", # New in v2.6.1.5
    "Waiting for avisynth release memory" : u"", # New in v2.6.9.8
    "Clip not released. Memory still allocated" : u"", # New in v2.6.9.8
    "Clip successful released" : u"", # New in v2.6.9.8
    "Abandoned clip assigned: \"{0}\"" : u"", # New in v2.6.9.8
    "Abandoned clip assigned. Select the tab?" : u"", # New in v2.6.9.8
    "Abandoned clip released: \"{0}\"" : u"", # New in v2.6.9.8
    "Process clip..." : u"", # New in v2.6.9.8
    "Waiting for avisynth clip" : u"", # New in v2.6.9.8
    "Clip process finished" : u"", # New in v2.6.9.8
    "Clip not initialized" : u"", # New in v2.6.9.8
    "Initialize clip  %s" : u"", # New in v2.6.9.8
    "Invalid slider text: min > max" : u"無効なスライダテキスト: 最小値 > 最大値",
    "Invalid slider text: value not in bounds" : u"無効なスライダテキスト: 範囲外の値",
    "Invalid slider text: bad modulo label" : u"無効なスライダテキスト: 不当な倍数ラベル",
    "Invalid slider text: slider label already exists" : u"無効なスライダテキスト: スライダラベルの重複",
    "Invalid slider text: invalid number" : u"無効なスライダテキスト: 無効な数値",
    "Reset to initial value: %(value_formatted)s" : u"初期値に %(value_formatted)s リセット",
    "Reset to initial value: %(value2_formatted)s" : u"初期値に %(value2_formatted)s リセット",
    "Invalid hexadecimal color!" : u"無効な 16 進色！",
    "Must specify a max value!" : u"最大値を指定する必要があります！",
    "Must specify a min value!" : u"最小値を指定する必要があります！",
    "Min value must be a number!" : u"最小値は数でなければなりません！",
    "Max value must be a number!" : u"最大値は数でなければなりません！",
    "Default value must be a number!" : u"デフォルト値は数でなければなりません！",
    "Step size value must be a number!" : u"ステップサイズは数でなければなりません！",
    "Add toggle tag" : u"", # New in v2.6.9.8
    "Clear all tags and disable the filters" : u"", # New in v2.6.9.8
    "Clear all tags && disabled filters" : u"", # New in v2.6.9.8
    "Toggle exclusions filters" : u"", # New in v2.6.9.8
    "General settings..." : u"一般設定...",
    "Set same width for all tabs" : u"", # New in v2.6.9.8
    "Update sliders" : u"", # New in v2.6.6.0
    "Reset to default value: %(value_formatted)s" : u"デフォルト値 %(value_formatted)s にリセット",
    "Left-click to select a color, right click to reset to default" : u"左クリックで色の選択、右クリックでデフォルトにリセット",
    "Snapshot doesn't seem to be from this session.\nKeep going?" : u"", # New in v2.6.9.8
    "Question" : u"質問",
    "Error: Snapshot 2 is empty" : u"", # New in v2.6.9.8
    "Restore to current" : u"", # New in v2.6.9.8
    "Restore to new tab" : u"", # New in v2.6.9.8
    "Copy snapshot 2 to 1" : u"", # New in v2.6.9.8
    "Done" : u"完了",
    "Joined or disabled filters found: filter1.filter2\nOnly the first filter can have a toggle tag" : u"", # New in v2.6.9.8
    "Enter new name" : u"", # New in v2.6.9.8
    "Rename toggle tag" : u"", # New in v2.6.9.8
    "Add child" : u"", # New in v2.6.9.8
    "Remove child" : u"", # New in v2.6.9.8
    "Toggle \"%(label)s\" section" : u"\"%(label)s\" のセクションをトグル",
    "Both videos must have the same width and height." : u"", # New in v2.6.9.8
    "Snapshot dimensions different: %ix%i" : u"", # New in v2.6.9.8
    "Error playing frame {number}" : u"", # New in v2.6.9.8
    "Save changes before previewing?" : u"プレビュー前に変更を保存しますか？",
    "Select an external player" : u"外部プレーヤーの選択",
    "A program must be specified to use this feature!" : u"この機能を使用するにはプログラムを指定する必要があります！",
    "Program not found. Must be specified to use this feature!" : u"", # New in v2.6.6.0
    "Above plugin names contain undesirable symbols.\nRename them to only use alphanumeric or underscores,\nor make sure to use them in short name style only." : u"上記のプラグイン名には好ましくない記号が含まれています。\n英数字またはアンダースコアのみを使用するようにリネームするか、\n必ずショートネームスタイルでのみそれらの名前を使用して下さい。",
    "This function is beta!\nFound more then one function with the same name.\nYou should clean up your plugins." : u"", # New in v2.6.6.0
    "Don't show me this again" : u"二度とこれを見せないでください",
    "Changing the plugins directory writes to the Windows registry.\n" : u"", # New in v2.6.1.5
    "Writing to: HKLM\\Software\\Avisynth\\plugindir2_5\n" : u"", # New in v2.6.1.5
    "Plugins dir registration failed" : u"", # New in v2.6.1.5
    "You're changing the plugins autoload directory.\nDo you wish to change it for all applications? This will\nrequire writing to {0}" : u"プラグイン自動読込ディレクトリを変更しようとしています。\nすべてのアプリケーションに対して変更しますか？\n{0} への書き込みが必要です。",
    "Save as" : u"名前を付けて保存",
    "Select a directory" : u"ディレクトリの選択",
    "Enter information" : u"情報の入力",
    "Progress" : u"進捗状況",
    "A get pixel info operation has already started" : u"ピクセル情報取得作業はすでに開始しています",
    "Error in the macro:" : u"マクロのエラー",
    "Couldn't find %(macrofilename)s" : u"%(macrofilename)s が見つかりませんでした",
    "An AviSynth script editor" : u"AviSynth スクリプトエディタ",
    "Error trying to display the clip" : u"", # New in v2.5.1
    "Is bit-depth set correctly?" : u"", # New in v2.5.1
    "Invalid string: " : u"無効な文字列: ",
    "Failed to open the AVI file" : u"AVI ファイルのオープンに失敗しました",
    "Failed to open the AVI frame" : u"AVI フレームのオープンに失敗しました",
    "Failed to retrieve AVI frame" : u"AVI フレームの読み出しに失敗しました",
    "Waiting for Avisynth, thread still running.\nThis dialog is automatically closed when avisynth returns.\nIf you abort this process, you should restart the program!" : u"", # New in v2.6.9.8
    "Waiting for Avisynth, thread still running.\nThis dialog is automatically closed when avisynth returns.\nIf you abort this process, the clip will assign later." : u"", # New in v2.6.9.8
    "Ctrl" : u"",
    "Alt" : u"",
    "Shift" : u"",
    "Error Window" : u"エラーウィンドウ",
    "Quick find" : u"クイック検索",
    "Find/replace text" : u"テキスト検索/置換",
    "Search &for" : u"検索",
    "R&eplace with" : u"置換",
    "Find &next" : u"次を検索",
    "Find &previous" : u"前を検索",
    "&Replace next" : u"次を置換",
    "Replace &all" : u"すべて置換",
    "Only on word s&tart" : u"文字列の先頭のみ",
    "Only &whole words" : u"文字列全体",
    "Only in &selection" : u"選択範囲のみ",
    "&Don't wrap-around" : u"改行しない",
    "&Case sensitive" : u"大文字と小文字を区別",
    "Use regular e&xpressions" : u"正規表現を使用",
    "&Interpret escape sequences" : u"", # New in v2.5.1
    "Cannot find \"%(text)s\"" : u"\"%(text)s\" が見つかりません",
    "Replaced %(count)i times" : u"%(count)i 回置換しました",
    "Program Settings" : u"プログラム設定",
    "Browse" : u"閲覧",
    "* Requires program restart for full effect" : u"* 完全な効果を得るにはプログラムの再起動が必要です。",
    "Invalid directory!" : u"無効なディレクトリです！",
    "Invalid filename!" : u"無効なファイル名です！",
    "Edit shortcuts" : u"ショートカットの編集",
    "Menu label" : u"メニューラベル",
    "Keyboard shortcut" : u"キーボードショートカット",
    "Double-click or hit enter on an item in the list to edit the shortcut." : u"ショートカットを編集するにはリスト内のアイテム上でダブルクリックするかエンターキーを押して下さい。",
    "Shortcut" : u"ショートカット",
    "Action" : u"アクション",
    "Edit the keyboard shortcut" : u"キーボードショートカットの編集",
    "Key:" : u"キー",
    "%(keyString)s not found in key string list" : u"%(keyString)s はキー文字列リストに見つかりませんでした",
    "This shortcut is being used by:" : u"このショートカットは使われています:",
    "Insert" : u"挿入",
    "Delete" : u"削除",
    "Error: key %(key)s does not exist!" : u"エラー: キー %(key)s は存在しません！",
    "Item %(newKey)s already exists!" : u"アイテム %(newKey)s はすでに存在します！",
    "Are you sure you want to rename from %(oldName)s to %(newName)s?" : u"本当に %(oldName)s から %(newName)s にリネームしたいですか？",
    "Insert a new item" : u"新しいアイテムの挿入",
    "Must enter a name!" : u"名前を入力してください！",
    "Warning: no value entered for item %(newKey)s!" : u"警告: アイテム %(newKey)s に対する値が未入力です！",
    "Message" : u"メッセージ",
    "Select an item to delete first" : u"まず削除するアイテムを選択してください",
    "Are you sure you want to delete item %(key)s?" : u"本当にアイテム %(key)s を削除してもいいですか？",
    "Error: minValue must be less than maxValue" : u"エラー: 最小値は最小値より小さくしてください",

    #--- Tool: resize_calc.py ---#
    "Resize calculator..." : u"リサイズ計算機...",
    "Calculate an appropriate resize for the video" : u"ビデオの適切なリサイズを計算する",
    "Resize calculator" : u"リサイズ計算機",
    "Input" : u"入力",
    "Video resolution:" : u"ビデオ解像度:",
    "Pixel aspect ratio:" : u"ピクセルアスペクト比:",
    "Results" : u"結果",
    "Aspect ratio error:" : u"アスペクト比エラー:",
    "Settings" : u"設定",
    "Target pixel aspect ratio:" : u"ターゲットピクセルアスペクト比",
    "Resize block constraints:" : u"リサイズブロック制限:",
    "Resize percent ranges:" : u"リサイズパーセント範囲:",
    "Max search aspect ratio error:" : u"アスペクト比エラーの最大検索:",
    "Configure" : u"設定",
    "compute from .d2v" : u".d2v から計算",
    "Configure options" : u"オプションの設定",
    "Avisynth resize:" : u"AviSynth リサイズ:",
    "The current Avisynth script contains errors." : u"現在の AviSynth スクリプトはエラーを含んでいます。",

    #--- Tool: encoder_gui.py ---#
    "Script encoder (CLI)" : u"スクリプトエンコーダ (CLI)",
    "Use an external command line encoder to save the current script" : u"外部のコマンドラインエンコーダを使って現在のスクリプトを保存する",
    "Encode video" : u"ビデオのエンコード",
    "System settings" : u"システム設定",
    "Input file:" : u"入力ファイル:",
    "Output file:" : u"出力ファイル:",
    "Compression settings" : u"圧縮設定",
    "Bitrate (kbits/sec):" : u"ビットレート (kbits/秒):",
    "calculate" : u"計算",
    "Quality CRF (0-51):" : u"品質 CRF (0-51):",
    "Quality CQ (1-31):" : u"品質 CQ (1-31):",
    "Additional settings" : u"追加設定",
    "Credits start frame:" : u"クレジット開始フレーム:",
    "Command line settings" : u"コマンドライン設定",
    "Run" : u"実行",
    "First time using this compression preset!" : u"この圧縮プリセットは初めて使用します！",
    "Please enter the exe paths in the following dialog." : u"次のダイアログに実行ファイルのパスを入力して下さい。",
    "Exe pathnames" : u"実行ファイルのパス名",
    "Open an AviSynth script" : u"AviSynth スクリプトを開く",
    "Save the video as" : u"ビデオを名前を付けて保存",
    "Select a program" : u"プログラムの選択",
    "Unreplaced items remain in the command line:" : u"",
    "Unknown exe paths!" : u"不明な実行ファイルのパス！",
    "General" : u"一般",
    "Credits warning minutes:" : u"クレジット警告分数:",
    "Automatically compute bitrate value on startup" : u"起動時に自動的にビットレート値を算出",
    "Automatically compute pixel aspect ratio from d2v on startup" : u"起動時に自動的に d2v からピクセルアスペクト比を算出",
    "Append batch commands to the avs script as comments" : u"avs スクリプトにバッチコマンドをコメントとして追加",
    "Add output file to new tab" : u"", # New in v2.6.6.0
    "Encoder priority:" : u"エンコーダ優先度:",
    "Path to %(name)s:" : u"%(name)s へのパス:",
    "Extra arguments:" : u"オプション引数:",
    "Presets file not found:\n" : u"", # New in v2.6.9.8
    "Bitrate Calculator" : u"ビットレート計算機",
    "Output info" : u"出力情報",
    "Total size:" : u"合計サイズ:",
    "Container:" : u"コンテナ:",
    "(None)" : u"（なし）",
    "Video info" : u"ビデオ情報",
    "Framecount:" : u"総フレーム数",
    "FPS:" : u"",
    "Audio info" : u"音声情報",
    "Audio file:" : u"音声ファイル:",
    "Compress audio" : u"音声を圧縮",
    "Audio bitrate:" : u"音声ビットレート:",
    "Format:" : u"フォーマット:",
    "Subtitles info" : u"字幕情報",
    "Subtitles file:" : u"字幕ファイル:",
    "Total time:" : u"合計時間:",
    "Video size:" : u"ビデオサイズ:",
    "Audio size:" : u"音声サイズ:",
    "Subtitles size:" : u"字幕サイズ:",
    "Overhead size:" : u"オーバーヘッドサイズ:",
    "Bitrate:" : u"ビットレート:",
    "Open the audio file" : u"音声ファイルを開く",
    "Open the subtitles file" : u"字幕ファイルを開く",
    "%(h)i hr and %(m)i min" : u"%(h)i 時間 %(m)i 分",

    #--- Tool: avs2avi_gui.py ---#
    "Script encoder (VFW)" : u"スクリプトエンコーダ (VFW)",
    "Use avs2avi to save the current script as an avi" : u"avs2avi を使って現在のスクリプトを avi として保存",
    "Please select the path to avs2avi.exe" : u"avs2avi.exe のパスを選択してください",
    "Error: avs2avi is required to save an avi!" : u"エラー: avi の保存には avs2avi が必要です！",
    "Pass: %(pass)s / %(passes)s" : u"パス: %(pass)s / %(passes)s",
    "Frame: %(frame)i / %(frames)i" : u"フレーム: %(frame)i / %(frames)i",
    "Size: %(size).2f MB" : u"サイズ: %(size).2f MB",
    "FPS: %(fps).1f fps" : u"",
    "Time left: %(hr)02i:%(min)02i:%(sec)02i" : u"残り時間: %(hr)02i:%(min)02i:%(sec)02i",
    "Input file (.avs):" : u"入力ファイル (.avs):",
    "Output file (.avi):" : u"出力ファイル (.avi):",
    "# of passes:" : u"パスの数:",
    "Priority:" : u"優先度:",
    "Error: Unknown button" : u"エラー: 不明なボタン",
    "AviSynth script (*.avs)|*.avs" : u"AviSynth スクリプト (*.avs)|*.avs",
    "Save the avi as" : u"avi を名前を付けて保存",
    "Avi file (*.avi)|*.avi" : u"Avi ファイル (*.avi)|*.avi",
    "Input file does not exist!" : u"入力ファイルが存在しません！",
    "Input file must be an avisynth script!" : u"入力ファイルは AviSynth スクリプトでなければなりません！",
    "Output path does not exist!" : u"出力パスが存在しません！",
    "# of passes must be an integer!" : u"パスの数は整数にする必要があります！",
    "Priority must be an integer!" : u"優先度は整数にする必要があります！",
    "Stop" : u"停止",
    "Process stopped." : u"処理が停止されました。",
    "Processing..." : u"処理中...",
    "Finished in %(hr)i hour(s) and %(min)i minute(s)." : u"%(hr)i 時間 %(min)i 分で終了しました。",
    "Finished in %(min)i minute(s) and %(sec)i second(s)." : u"%(min)i 分 %(sec)i 秒で終了しました。",
    "Finished in %(time).1f seconds." : u"%(time).1f 秒で終了しました。",
    "Filesize: %(size).2f MB" : u"ファイルサイズ: %(size).2f MB",
    "The current script contains errors, exiting." : u"現在のスクリプトはエラーを含んでいます。終了します。",
    "Save as AVI" : u"AVI として保存",

    #--- Macros ---#
    "Bookmarks at Intervals" : u"一定間隔でブックマーク",
    "Bookmarks to Chapter" : u"ブックマークをチャプタに変換",
    "Bookmarks to Trims" : u"", # New in v2.6.6.0
    "ConditionalReader file from bookmarks" : u"ブックマークから ConditionalReader ファイルを生成",
    "ConditionalReader file from WriteFile" : u"", # New in v2.6.9.8
    "DeleteFrame" : u"",
    "DuplicateFrame" : u"",
    "Import bookmarks from file" : u"ファイルからブックマークをインポート",
    "Open Image Sequence" : u"", # New in v2.6.6.0
    "Preview from current point" : u"現在の位置からプレビュー",
    "PreviewEncode" : u"", # New in v2.6.9.8
    "PreviewResize" : u"", # New in v2.6.9.8
    "Random Clip Order" : u"ランダム順にクリップを連結",
    "RemovePing" : u"", # New in v2.6.9.8
    "Save Image Sequence" : u"イメージシーケンスの保存",
    "Selected trims to selections" : u"", # New in v2.6.6.0
    "Shift Bookmarks by frames" : u"指定フレーム数だけブックマークを移動",
    "Example (Resize)" : u"例（リサイズ）",
    "Examples" : u"例",
    "Extra" : u"", # New in v2.6.9.8
    "Customized" : u"カスタマイズ",
    "bilinear" : u"",
    "bicubic" : u"",
    "lanczos" : u"",
    "spline36" : u"",
    "create new tab" : u"新規タブの作成",
    "force mod 2" : u"2 の倍数強制",
    "Template example" : u"テンプレート例",
    "Batch example" : u"バッチ例",
    "Image processing" : u"画像処理",
    "Manual Telecide" : u"手動逆テレシネ",
    "Secondary preview" : u"第 2 プレビュー",
    "Encoding example" : u"エンコード例",
    "Encoding example 2" : u"エンコード例 2",
    "Optimize Sliders" : u"スライダ最適化",
    "DeleteEncodings" : u"", # New in v2.6.9.8
    "Save as Tiff_rgb48" : u"", # New in v2.6.9.8

    #--- Macro: Bookmarks at Intervals ---#
    "Choose a frame step or a number of intervals" : u"フレームステップまたは周期の選択",
    "Number of intervals" : u"周期",
    "End frame" : u"", # New in v2.5.0
    "Start frame" : u"", # New in v2.5.0
    "Clear bookmarks in the same range" : u"", # New in v2.5.0

    #--- Macro: Bookmarks to Chapter ---#
    "Save chapter file as..." : u"名前をつけてチャプタファイルを保存...",
    "Text files" : u"テキストファイル",

    #--- Macro: Bookmarks to Trims ---#
    "No bookmarks defined." : u"", # New in v2.6.6.0

    #--- Macro: ConditionalReader file from bookmarks ---#
    "There is not bookmarks" : u"ブックマークがありません",
    "Type" : u"型",
    "Value" : u"値",
    "Bookmarks represent..." : u"ブックマーク",
    "Override 'Value' with the bookmark's title" : u"「値」をブックマークのタイトルに変更",
    "ConditionalReader file" : u"ConditionalReader ファイル",
    "Insert the ConditionalReader file path at the current cursor position" : u"現在のカーソル位置に ConditionalReader ファイルのパスを挿入",
    "Bool" : u"ブール",
    "String" : u"文字列",
    "Int" : u"整数",
    "False" : u"",
    "True" : u"",
    "Single frames" : u"単一フレーム",
    "Ranges of frames" : u"フレームの範囲",
    "Ranges of frames (with interpolation)" : u"フレームの範囲（補間あり）",
    "An output path is needed" : u"出力パスが必要です",
    "Interpolation only available for Int and Float" : u"補間は整数型と浮動小数点数型のみ利用可",
    "Odd number of bookmarks" : u"奇数個のブックマーク",

    #--- Macro: ConditionalReader file from WriteFile ---#
    "There is not Valus" : u"", # New in v2.6.9.8
    "ConditionalReader file from WriteFile file" : u"", # New in v2.6.9.8

    #--- Macro: Import bookmarks from file ---#
    "All supported files" : u"すべての対応しているファイル",
    "Chapters Text files" : u"チャプタテキストファイル",
    "Matroska XML files" : u"Matroska XML ファイル",
    "Celltimes files" : u"Celltimes ファイル",
    "AvsP Session files" : u"AvsP セッションファイル",
    "TFM log files" : u"TFM ログファイル",
    "XviD log files" : u"XviD ログファイル",
    "QP files" : u"QP ファイル",
    "Timecode format v1 files" : u"タイムコードフォーマット v1 ファイル",
    "Bookmarks from TFM file" : u"TFM ファイルからのブックマーク",
    "Not combed or out of order frames" : u"縞なしまたは順序違いのフレーム",
    "Combed" : u"縞あり",
    "Possible" : u"可能性あり",
    "u,b,out-of-order" : u"u,b,順序違い",
    "Min frame:" : u"最小フレーム:",
    "Max frame:" : u"最大フレーム",
    "TFM log parser" : u"TFM ログパーサー",
    "%d frames imported" : u"%d 個のフレームがインポートされました",
    "[COMBED FRAMES] section could not be parsed" : u"[COMBED FRAMES]（縞ありフレーム）は解析出来ませんでした",
    "Bookmark file unrecognized!" : u"ブックマークファイルが認識されませんでした！",

    #--- Macro: Open Image Sequence ---#
    "Select the Image" : u"", # New in v2.6.6.0
    "Images (bmp, jpg, png, tiff)" : u"", # New in v2.6.6.0
    "All files (*.*)" : u"", # New in v2.6.6.0

    #--- Macro: Preview from current point ---#
    "Failed to run the external player!\n\nOpen the macro file in the \"Macros\" subdirectory\nwith a text editor and edit the executable\ndirectory appropriately!" : u"外部プレーヤーの起動に失敗しました！\n\nテキストエディタで \"Macros\" サブディレクトリの\nマクロファイルを開き、実行ファイルのディレクトリを\n適切に編集して下さい！",

    #--- Macro: PreviewEncode ---#
    "Convert to script color space" : u"", # New in v2.6.9.8
    "Encode threads:" : u"", # New in v2.6.9.8
    "Insert trims into script" : u"", # New in v2.6.9.8
    "Select save path:" : u"", # New in v2.6.9.8
    "Template:" : u"", # New in v2.6.9.8
    "Use script dir" : u"", # New in v2.6.9.8
    "Encode options" : u"", # New in v2.6.9.8
    "You must first create selections" : u"", # New in v2.6.9.8
    "Last encoding returns error. Process is canceled\n" : u"", # New in v2.6.9.8
    "Error, cannot insert the encode preview text\nTrying to create new tab" : u"", # New in v2.6.9.8
    "Encoding finished\n\nElapsed time: %s\n%s%s" : u"", # New in v2.6.9.8

    #--- Macro: PreviewResize ---#
    "BicubicResize" : u"", # New in v2.6.9.8
    "Spline16Resize" : u"", # New in v2.6.9.8
    "Spline36Resize" : u"", # New in v2.6.9.8
    "Spline64Resize" : u"", # New in v2.6.9.8
    "0" : u"", # New in v2.6.9.8
    "0.5" : u"", # New in v2.6.9.8
    "0.75" : u"", # New in v2.6.9.8
    "1.5" : u"", # New in v2.6.9.8
    "2.0" : u"", # New in v2.6.9.8
    "Border:" : u"", # New in v2.6.9.8
    "Fit only height" : u"", # New in v2.6.9.8
    "Resize Filter:" : u"", # New in v2.6.9.8
    "Resise options" : u"", # New in v2.6.9.8

    #--- Macro: Save Image Sequence ---#
    "Save image sequence" : u"画像シークエンスの保存",
    "Output format" : u"出力フォーマット",
    "Select frames" : u"フレームの選択",
    "Depth (PNG only)" : u"", # New in v2.5.0
    "Quality (JPEG only)" : u"品質 (JPEG のみ)",
    "Show saving progress" : u"保存状況を表示",
    "Output directory and basename. A padded number is added as suffix" : u"", # New in v2.5.0
    "Use always this basename" : u"つねにベース名を使用",
    "Use always this directory" : u"つねにこのディレクトリを使用",
    "Add the frame number as the suffix" : u"", # New in v2.5.0
    "Save ranges to subdirectories" : u"", # New in v2.5.0
    "Add image source to the script  ->" : u"", # New in v2.6.6.0
    "To new tab" : u"", # New in v2.6.6.0
    "Range between bookmarks" : u"ブックマーク間の範囲",
    "From first to last bookmark" : u"", # New in v2.6.6.0
    "Trim editor selections" : u"トリムエディタの選択範囲",
    "All frames" : u"すべてのフレーム",
    "Select an output directory and basename for the new images files" : u"新規画像ファイルの出力ディレクトリとベース名を選択",
    "Bookmarks out of frame count" : u"", # New in v2.6.6.0
    "At least 2 bookmarks are required" : u"", # New in v2.6.6.0
    "There is not Trim editor selections" : u"トリムエディタの選択範囲が見つかりません",
    "There is no process selection" : u"", # New in v2.6.6.0
    "Saving images..." : u"画像の保存中...",
    "scene_{0:0{1}}" : u"", # New in v2.5.0
    "%d image files created." : u"%d 個の画像ファイルが生成されました。",

    #--- Macro: Shift Bookmarks by frames ---#
    "Introduce the number of frames:" : u"移動するフレーム数",
    "Shift bookmarks by # frames" : u"ブックマークの移動",

    #--- Macro: Customized ---#
    "Customized aspect ratio" : u"カスタマイズされたアスペクト比",
    "Enter a pixel ratio or new size. e.g. 40:33, 1.212 or 640x360" : u"ピクセル比または新しいサイズを入力してください。例. 40:33, 1.212, 640x360",

    #--- Macro: Image processing ---#
    "Processing images..." : u"画像の処理中...",
    "Macro aborted" : u"マクロが中断されました",

    #--- Macro: Manual Telecide ---#
    "Open a source to Telecide" : u"逆テレシネするソースを開く",
    "Filename was mangled! Get it again!" : u"ファイル名がメチャクチャです！再入力してください！",
    "Enter the field order:" : u"フィールドオーダーの入力:",
    "Must enter either a 0 or 1!" : u"0 または 1 を入力して下さい！",
    "Must enter an integer!" : u"整数を入力して下さい！",
    "Override filename was mangled! Get it again!" : u"オーバーライドファイル名がメチャクチャです！再入力してください！",
    "Not allowed to select base Telecide tab!" : u"ベースの Telecide タブを選択することはできません！",
    "Unknown mode!" : u"不明なモード！",

    #--- Macro: Encoding example ---#
    "Encoding is disabled, please read the \"Encoding example.py\" macro for info" : u"エンコードは停止されます。詳しくは \"Encoding example.py\" をお読み下さい",

    #--- Macro: Encoding example 2 ---#
    "Output filename:" : u"出力ファイル名:",
    "Output height:" : u"出力の高さ:",
    "Output width:" : u"出力の幅:",
    "Enter encoder info" : u"エンコーダ情報の入力",
    "Encoding is disabled, please read the \"Encoding example 2.py\" macro for info" : u"エンコードは停止されます。詳しくは \"Encoding example 2.py\" をお読み下さい",

    #--- Macro: Optimize Sliders ---#
    "Generation 0 Progress" : u"第 0 世代の進捗状況",
    "Initial evaluation..." : u"初期評価...",
    "Initial best score: %.3f, Current best score: %.3f" : u"初期ベストスコア: %.3f, 現在のベストスコア: %.3f",
    "Best score: %.2f" : u"ベストスコア: %.2f",
    "Must configure avs2avi directory to use this macro!" : u"このマクロを使用するには avs2avi ディレクトリを設定する必要があります！",
    "Not user sliders on the current Avisynth script!" : u"現在の AviSynth スクリプトのユーザースライダではありません！",
    "Enter optimization info    (%i bits, %i possibilities)" : u"最適化情報の入力    (%i ビット, %i 確率)",
    "SSIM log filename:" : u"SSIM ログファイル名:",
    "max generations:" : u"最大世代数:",
    "population size:" : u"母集団サイズ:",
    "crossover probability:" : u"交叉確率:",
    "mutation probability:" : u"突然変異確率:",
    "selection pressure:" : u"淘汰圧:",
    "Begin optimization..." : u"最適化を開始します...",
    "Finished optimization." : u"最適化を完了しました。",

    #--- Macros - Extra ---#
}