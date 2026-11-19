init -10 python:
    bel_font_text = "font/russia.ttf"
    bel_font_interface = FontGroup() \
        .add("font/razor_k.ttf", 0x0406, 0x0406, target="I") \
        .add("font/razor_k.ttf", 0x0456, 0x0456, target="I") \
        .add("font/russia.ttf", 0x040E, 0x040E, target=0x040E) \
        .add("font/russia.ttf", 0x045E, 0x045E, target=0x040E) \
        .add("font/russia.ttf", 0x2014, 0x2014) \
        .add("font/russia.ttf", 0x2019, 0x2019) \
        .add("font/razor_k.ttf", None, None)


init 999 python:
    lang_mm_screen["belarusian"] = "main_menu_language_message_bel"
    if not persistent._belarusian_default_applied:
        persistent._belarusian_default_applied = True
        _preferences.language = "belarusian"

    _bel_bare_ui = {
        "ДАЛЬШЕ": "ДАЛЕЙ",
        "СБРОС ПРОГРЕССА": "СКІД ПРАГРЭСУ",
        "ПОДТВЕРДИТЬ": "ПАЦВЕРДЗІЦЬ",
        "СБРОСИТЬ": "СКІНУЦЬ",
        "Эпизод 1": "Эпізод 1",
        "Эпизод 2": "Эпізод 2",
        "Эпизод 3": "Эпізод 3",
        "Эпизод 4": "Эпізод 4",
        "Эпизод 5": "Эпізод 5",
    }
    _prev_bel_replace_text = config.replace_text
    def _bel_replace_text(s):
        if _prev_bel_replace_text is not None:
            s = _prev_bel_replace_text(s)
        if getattr(getattr(renpy.game, "preferences", None), "language", None) == "belarusian":
            return _bel_bare_ui.get(s, s)
        return s
    config.replace_text = _bel_replace_text


translate belarusian style default:
    properties gui.text_properties()
    font bel_font_text

translate belarusian style button_text:
    properties gui.text_properties("button")
    yalign 0.5
    font bel_font_interface

translate belarusian style gui_text:
    properties gui.text_properties("interface")
    font bel_font_interface

translate belarusian style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font bel_font_interface

translate belarusian style quick_text:
    properties gui.text_properties("quick_text")
    font bel_font_interface

translate belarusian style pref_text:
    font bel_font_interface
    color "FFFFFF"
    size 35

translate belarusian style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 1
    font bel_font_text
    size 60

translate belarusian style say_label:
    font bel_font_text
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    ypos -45
    xpos 30
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    size 80

translate belarusian style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    font bel_font_text
    size 80

translate belarusian style confirm_textbutton:
    xalign 0.5
    yalign 0.5
    size 40
    color "FFFFFF"
    xoffset -10
    font bel_font_interface

translate belarusian style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    xalign 0.5
    yalign 0.5
    size 40
    color "000000"
    xoffset -10
    font bel_font_interface

translate belarusian style about_text:
    font bel_font_interface
    color "FFFFFF"
    size 36

translate belarusian style text_font_interface:
    font bel_font_interface

translate belarusian style imagemap_text:
    xalign 0.5
    yalign 0.5
    outlines [ (absolute(1), "#000000", absolute(0), absolute(0)) ]
    font bel_font_text
    size 60

translate belarusian style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font bel_font_text
    size 55

translate belarusian style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#FFFFFF"
    font bel_font_text
    size 50

translate belarusian style text_dict:
    size 40
    font bel_font_text


init 10:
    screen initial_language_message_bel():
        tag initial_language_message
        text "МОВА" align (.5, .33) at init_lang_text_animation

    screen main_menu_language_message_bel():
        tag main_menu_language_message
        text "МОВА" color "#fff" anchor (.5, .0) pos (175, lang_btn_ypos) at init_lang_text_animation, mm_elements

    screen Disclaimer(ypos=130):
        vbox ypos ypos xalign .5:
            if _preferences.language is None:
                text "{size=+18}Внимание!{/size}\n{size=+4}Данная игра не предназначена для лиц младше восемнадцати лет, а также противопоказана впечатлительным людям со слабой психикой. Присутствуют сцены физического и морального насилия, наличие описаний смерти, демонстрация крови и увечий, а также ненормативная лексика. Все персонажи и события являются вымышленными, любое совпадение с реальностью случайно. Всё внутриигровое повествование, звуковое и текстовое содержание являются инструментами создания атмосферы и не выражают позицию разработчиков. Разработчик не несёт ответственность за ваши действия/интерпретации и не призывает вас к каким-либо действиям.\nБудьте осторожны и берегите себя!{/size}" at truecenter text_align .5 xsize 1650
            elif _preferences.language == "belarusian":
                text "{size=+18}Увага!{/size}\n{size=+4}Гэтая гульня не прызначана для асоб маладзейшых за васямнаццаць гадоў, а таксама проціпаказана ўразлівым людзям са слабой псіхікай. Прысутнічаюць сцэны фізічнага і маральнага гвалту, апісанні смерці, дэманстрацыя крыві і калецтваў, а таксама ненарматыўная лексіка. Усе персанажы і падзеі з'яўляюцца выдуманымі, любое супадзенне з рэальнасцю выпадковае. Усё ўнутрыгульнявое апавяданне, гукавое і тэкставае напаўненне з'яўляюцца інструментамі стварэння атмасферы і не выказваюць пазіцыю распрацоўшчыкаў. Распрацоўшчык не нясе адказнасці за вашы дзеянні/інтэрпрэтацыі і не заклікае вас да якіх-небудзь дзеянняў.\nБудзьце асцярожныя і беражыце сябе!{/size}" at truecenter text_align .5 xsize 1650
            elif _preferences.language == "turkish":
                text "{size=+18}Dikkat!{/size}" at truecenter
                text "{size=+4}Bu oyunda küfür ve hakaretin yanı sıra, {/size}" at truecenter
                text "{size=+4}fiziksel ve psikolojik şiddet sahneleri bulunmaktadır.{/size}" at truecenter
            elif _preferences.language == "italiano":
                text "{size=+18}Attenzione!{/size}" at truecenter
                text "{size=+4}Questo gioco contiene del linguaggio offensivo e{/size}" at truecenter
                text "{size=+4}scene di violenza fisica e psicologica.{/size}" at truecenter
            elif _preferences.language == "chinese":
                text "{size=+18}请注意！{/size}" at truecenter
                text "{size=+4}本游戏含有粗口和精神、{/size}" at truecenter
                text "{size=+4}肢体暴力的画面，{/size}" at truecenter
                text "{size=+4}请多加注意！{/size}" at truecenter
            elif _preferences.language == "japan":
                text "{size=+18}コンテンツに関する警告：{/size}" at truecenter
                text "{size=+4}このゲームには不快な言葉遣いや身体的・心理的暴力描写が含まれます。{/size}" at truecenter
                text "{size=+4}苦手な方は十分に注意してプレイしてください。{/size}" at truecenter
            else:
                text "{size=+18}Warning!{/size}" at truecenter
                text "{size=+4}This game contains offensive language and{/size}" at truecenter
                text "{size=+4}scenes of physical and psychological violence.{/size}" at truecenter
                text "{size=+4}Proceed with caution!{/size}" at truecenter
            if config.developer:
                text "devBuild v" + config.version at truecenter color "#ff0"

    screen initial_language_select():
        add "images/interface/Lang.jpg"
        vbox xalign .5 yalign .58 spacing 1:
            hbox xalign .5 spacing 85:
                button xminimum 103 yminimum 192 background "interface/main_meny/lapka_01.png" hover_sound "sounds/menu/menu-button-select-3.ogg" activate_sound "sounds/menu/language-sellect-1.ogg" hovered ShowTransient("initial_language_message_rus") sensitive True selected False action [Return(), Language(None)] at mm_but_lang:
                    text "РУС" xalign .5 ypos 79 font "font/razor_k.ttf" color "000000" size 40
                button xminimum 103 yminimum 192 background "interface/main_meny/lapka_02.png" hover_sound "sounds/menu/menu-button-select-3.ogg" activate_sound "sounds/menu/language-sellect-1.ogg" hovered ShowTransient("initial_language_message_eng") sensitive True selected False action [Return(), Language("english")] at mm_but_lang:
                    text "ENG" xalign .5 ypos 79 font "font/razor_k.ttf" color "000000" size 40
                button xsize 103 ysize 192 background "interface/main_meny/lapka_04.png" hover_sound "sounds/menu/menu-button-select-3.ogg" activate_sound "sounds/menu/language-sellect-1.ogg" hovered ShowTransient("initial_language_message_chi") sensitive True selected False action [Return(), Language("chinese")] at mm_but_lang
                button xminimum 103 yminimum 192 background "interface/main_meny/lapka_02.png" hover_sound "sounds/menu/menu-button-select-3.ogg" activate_sound "sounds/menu/language-sellect-1.ogg" hovered ShowTransient("initial_language_message_ita") sensitive True selected False action [Return(), Language("italiano")] at mm_but_lang:
                    text "ITA" xalign .5 ypos 79 font "font/razor_k.ttf" color "000000" size 40
                button xminimum 103 yminimum 192 background "interface/main_meny/lapka_01.png" hover_sound "sounds/menu/menu-button-select-3.ogg" activate_sound "sounds/menu/language-sellect-1.ogg" hovered ShowTransient("initial_language_message_tur") sensitive True selected False action [Return(), Language("turkish")] at mm_but_lang:
                    text "TÜR" xalign .5 ypos 79 font "font/razor_k.ttf" color "000000" size 40
                button xminimum 103 yminimum 192 background "interface/main_meny/lapka_01.png" hover_sound "sounds/menu/menu-button-select-3.ogg" activate_sound "sounds/menu/language-sellect-1.ogg" hovered ShowTransient("initial_language_message_jpn") sensitive True selected False action [Return(), Language("japan")] at mm_but_lang:
                    text "JAP" xalign .5 ypos 79 font "font/razor_k.ttf" color "000000" size 40
                button xminimum 103 yminimum 192 background "interface/main_meny/lapka_02.png" hover_sound "sounds/menu/menu-button-select-3.ogg" activate_sound "sounds/menu/language-sellect-1.ogg" hovered ShowTransient("initial_language_message_bel") sensitive True selected False action [Return(), Language("belarusian")] at mm_but_lang:
                    text "БЕЛ" xalign .5 ypos 79 font "font/razor_k.ttf" color "000000" size 40

    screen main_menu():
        tag menu
        style_prefix "main_menu"
        add gui.main_menu_background
        if persistent.animal_unlock[3]:
            add "interface/main_meny/fon_05.png"
        if persistent.animal_unlock[0]:
            add "interface/main_meny/fon_02.png"
        if persistent.animal_unlock[4]:
            add "interface/main_meny/fon_06.png"
        add "menu002_1"
        add "menu002_2"
        add "chastichka_2"
        if persistent.animal_unlock[1]:
            add "interface/main_meny/fon_03.png"
        if persistent.animal_unlock[2]:
            add "interface/main_meny/fon_04.png"
        add "menu001_1"
        add "menu001_2"
        add "chastichka_1_1"
        add "main_menu_bg"
        add "chastichka_1_2"
        add "bg_black" at mm_bg_diss_1to0
        if preferences.language != "japan":
            add "[logo!t]" xalign 0.47 yalign 0.09 at mm_elements
        else:
            add "interface/main_meny/logo_en.png" xalign 0.47 yalign 0.09 at mm_elements
        on "show" action ShowTransient(lang_mm_screen[preferences.language])
        on "replace" action ShowTransient(lang_mm_screen[preferences.language])
        on "replaced" action Hide(lang_mm_screen[preferences.language])
        on "hide" action Hide(lang_mm_screen[preferences.language])
        fixed xfit True yfit True ypos 100 at mm_elements:
            hbox xpos 80 ypos 100 at mm_elements:
                button xsize 103 ysize 192 background "interface/main_meny/lapka_01.png" activate_sound "sounds/menu/language-sellect-1.ogg" action Language(None) hovered ShowTransient("main_menu_language_message_rus") unhovered ShowTransient(lang_mm_screen[preferences.language]) at mm_but_lang:
                    if preferences.language != None:
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    text "РУС" xpos 40 ypos 105 font "font/razor_k.ttf" color "000000" size 40
            hbox xpos 180 ypos 200 at mm_elements:
                button xsize 103 ysize 192 background "interface/main_meny/lapka_02.png" activate_sound "sounds/menu/language-sellect-1.ogg" action Language("english") hovered ShowTransient("main_menu_language_message_eng") unhovered ShowTransient(lang_mm_screen[preferences.language]) at mm_but_lang:
                    if preferences.language != "english":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    text "ENG" xpos 35 ypos 105 font "font/razor_k.ttf" color "000000" size 40
            hbox xpos 80 ypos 300 at mm_elements:
                button xsize 103 ysize 192 background "interface/main_meny/lapka_04.png" activate_sound "sounds/menu/language-sellect-1.ogg" action Language("chinese") hovered ShowTransient("main_menu_language_message_chi") unhovered ShowTransient(lang_mm_screen[preferences.language]) at mm_but_lang:
                    if preferences.language != "chinese":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
            hbox xpos 180 ypos 400 at mm_elements:
                button xsize 103 ysize 192 background "interface/main_meny/lapka_02.png" activate_sound "sounds/menu/language-sellect-1.ogg" action Language("italiano") hovered ShowTransient("main_menu_language_message_ita") unhovered ShowTransient(lang_mm_screen[preferences.language]) at mm_but_lang:
                    if preferences.language != "italiano":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    text "ITA" xpos 35 ypos 105 font "font/razor_k.ttf" color "000000" size 40
            hbox xpos 80 ypos 500 at mm_elements:
                button xsize 103 ysize 192 background "interface/main_meny/lapka_01.png" activate_sound "sounds/menu/language-sellect-1.ogg" action Language("turkish") hovered ShowTransient("main_menu_language_message_tur") unhovered ShowTransient(lang_mm_screen[preferences.language]) at mm_but_lang:
                    if preferences.language != "turkish":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    text "TÜR" xalign .5 xoffset 5 ypos 105 font "font/razor_k.ttf" color "000000" size 40
            hbox xpos 180 ypos 600 at mm_elements:
                button xsize 103 ysize 192 background "interface/main_meny/lapka_02.png" activate_sound "sounds/menu/language-sellect-1.ogg" action Language("japan") hovered ShowTransient("main_menu_language_message_jpn") unhovered ShowTransient(lang_mm_screen[preferences.language]) at mm_but_lang:
                    if preferences.language != "japan":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    text "JPN" xalign .5 xoffset -5 ypos 105 font "font/razor_k.ttf" color "000000" size 40
            hbox xpos 80 ypos 700 at mm_elements:
                button xsize 103 ysize 192 background "interface/main_meny/lapka_01.png" activate_sound "sounds/menu/language-sellect-1.ogg" action Language("belarusian") hovered ShowTransient("main_menu_language_message_bel") unhovered ShowTransient(lang_mm_screen[preferences.language]) at mm_but_lang:
                    if preferences.language != "belarusian":
                        hover_sound "sounds/menu/menu-button-select-3.ogg"
                    else:
                        hover_sound None
                    text "БЕЛ" xpos 35 ypos 105 font "font/razor_k.ttf" color "000000" size 40
        vbox xalign 0.47 yalign 0.4 at mm_elements:
            if has_endings():
                textbutton _("Галерея") action ShowMenu("gallery") keyboard_focus False:
                    if preferences.language == "japan":
                        text_font other_font_interface
            textbutton _("Новая игра") action Show("black_screen") keyboard_focus False:
                if preferences.language == "japan":
                    text_font other_font_interface
            textbutton _("Загрузить") action ShowMenu("load") keyboard_focus False:
                if preferences.language == "japan":
                    text_font other_font_interface
            textbutton _("Настройки") action ShowMenu("preferences") keyboard_focus False:
                if preferences.language == "japan":
                    text_font other_font_interface
            textbutton _("Об авторах") action ShowMenu("about_me") keyboard_focus False:
                if preferences.language == "japan":
                    text_font other_font_interface
            textbutton _("Выход") action Quit(confirm=False) keyboard_focus False:
                if preferences.language == "japan":
                    text_font other_font_interface
        vbox xalign 0.47 yalign 0.4 at mm_elements:
            if has_endings():
                button background "interface/main_meny/plaska.png" at mm_but action ShowMenu("gallery") default_focus True:
                    text _("Галерея"):
                        if preferences.language == "japan":
                            font other_font_interface
            button background "interface/main_meny/plaska.png" at mm_but action Show("black_screen") default_focus True:
                text _("Новая игра"):
                    if preferences.language == "japan":
                        font other_font_interface
            button background "interface/main_meny/plaska.png" at mm_but action ShowMenu("load"):
                text _("Загрузить"):
                    if preferences.language == "japan":
                        font other_font_interface
            button background "interface/main_meny/plaska.png" at mm_but action ShowMenu("preferences"):
                text _("Настройки"):
                    if preferences.language == "japan":
                        font other_font_interface
            button background "interface/main_meny/plaska.png" at mm_but action ShowMenu("about_me"):
                text _("Об авторах"):
                    if preferences.language == "japan":
                        font other_font_interface
            button background "interface/main_meny/plaska.png" at mm_but action Quit(confirm=False):
                text _("Выход"):
                    if preferences.language == "japan":
                        font other_font_interface
        key "game_menu" action Quit(confirm=True)
        if not config.developer:
            on "show" action Show("block_screen")
            timer 3.2 action Hide("block_screen")
        if config.developer:
            use devolver_menu()

    screen gallery_slot(idx, data):
        if idx == 0:
            $ target_pos = (258, 180)
        if idx == 1:
            $ target_pos = (762, 180)
        if idx == 2:
            $ target_pos = (1257, 180)
        if idx == 3:
            $ target_pos = (258, 515)
        if idx == 4:
            $ target_pos = (762, 515)
        if idx == 5:
            $ target_pos = (1257, 515)
        $ trigger = data.get("trigger")
        $ slot_font = bel_font_interface if preferences.language == "belarusian" else other_font_interface
        if trigger is not None:
            if trigger and trigger in persistent.story_unlocks:
                if new_ending == trigger:
                    add Solid("#000", xysize=gallery_slot_size):
                        at transform:
                            pos target_pos
                            1.25
                            data["img"] with ImageDissolve("effect/imagedissolve/vfx_garage/01.jpg", 2.5, ramplen=128)
                    text "???" anchor (.5, 1.) pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65) size 40 font slot_font:
                        at transform:
                            alpha 1
                            1.25
                            linear 1.25 alpha 0
                    text data["caption"] anchor (.5, 1.) pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65) size 40 font slot_font:
                        at transform:
                            alpha 0
                            2.5
                            linear 1.25 alpha 1
                else:
                    add data["img"] pos target_pos
                    text data["caption"] anchor (.5, 1.) pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65) size 40 font slot_font
            else:
                add Solid("#000", xysize=gallery_slot_size) pos target_pos
                text "???" anchor (.5, 1.) pos (target_pos[0] + gallery_slot_size[0]//2, target_pos[1] + gallery_slot_size[1] + 65) size 40 font slot_font
