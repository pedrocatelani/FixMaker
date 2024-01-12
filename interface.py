from pathlib import Path
import PySimpleGUI as sg

def refresh_window(settings):
    theme = settings["GUI"]["default_theme"]
    font_size = int(settings["GUI"]["font_size"])
    font_family = settings["GUI"]["font_family"]

    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))

def settings_window(settings):
    layout_settings = [
        [sg.Text("CONFIGURAÇÕES")],
        [sg.Text("Tema: "), sg.Combo(
            settings["GUI"]["theme"].split("|"),
            s = 10,
            key = "-THEME-")],
        [sg.Text("Fonte: "),sg.Combo(
            settings["GUI"]["sizes"].split("|"),
            default_value = 24,
            s = 10,
            key = "-SIZE-")],
        [sg.Text("")],
        [sg.Button("Salvar", s = (10,1)),sg.Text("Alterações salvas após reinicialização!")]
    ]

    window = sg.Window("FixMaker2000 - Settings", layout_settings, use_custom_titlebar=True)
    while True:
        event, values = window.read()

        if event == "Salvar":
            if values["-THEME-"] != '':
                settings["GUI"]["default_theme"] = values["-THEME-"]
            if values["-SIZE-"] in settings["GUI"]["sizes"].split("|"):
                settings["GUI"]["font_size"] = values["-SIZE-"]
            refresh_window(settings)
            window.close()

        if event == sg.WIN_CLOSED:
            window.close()
            break

def main_window(settings):
    menu_bar_definition = [
        ["Menu",["Configurações","Sobre","Sair"]]
    ]

    column_1 = [
        [sg.Text("FOR: ")],
        [sg.Text("DEX: ")],
        [sg.Text("CON: ")],
        [sg.Text("INT: ")],
        [sg.Text("SAB: ")],
    ]

    column_2 = [
        [sg.InputText(size=4,key="-FOR-")],
        [sg.InputText(size=4,key="-DEX-")],
        [sg.InputText(size=4,key="-CON-")],
        [sg.InputText(size=4,key="-INT-")],
        [sg.InputText(size=4,key="-SAB-")],
    ]
    layout_atr = [
        [sg.MenubarCustom(menu_bar_definition,tearoff=False)],
        [sg.Text("Selecionador de atributos")],
        [sg.Column(column_1),sg.Column(column_2)],
        [sg.Button("Dados"),sg.Button("Próximo",button_color='darkred')],
    ]

    window = sg.Window("FixMaker2000 - Atributos", layout_atr, use_custom_titlebar=True)

    while True:
        evento, valores = window.read()

        if evento == 'Configurações':
            window.disappear()
            settings_window(settings)
            window.reappear()

        if evento == sg.WIN_CLOSED:
            window.close()
            break

def create_settings():
    settings_path = Path.cwd()
    settings = sg.UserSettings(
        path=settings_path,
        filename="config.ini",
        use_config_file=True,
        convert_bools_and_none=False
    )
    refresh_window(settings)
    main_window(settings)