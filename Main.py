import PySimpleGUI as sg

layout = [
    [sg.Output(size=(120, 20), key="ML")],
    [sg.Button("Ładuj jak zmywarkę", key="LOAD"), sg.Button("Rate", key="RATE")],
]

window = sg.Window("Window Title", layout, finalize=True)
from Multiplet import Multiplet, line, F
from LevMarJO import LevMar

x = Multiplet()
while True:
    event, values = window.read()
    # print(event, values)
    if event == "LOAD":
        x = Multiplet()
        filename = sg.popup_get_file("Will not see this message", no_window=True)
        print(f"Loading file {filename}")
        x.load_file(filename)
        print(x)
        params = LevMar(x)
        window.bring_to_front()
    if event == "RATE":
        if x.is_fitted:
            filenames = sg.popup_get_file(
                "Will not see this message", no_window=True, multiple_files=True
            )
            window.bring_to_front()
            for fname in filenames:
                print("Loading ", fname)
                emi = Multiplet()
                emi.load_rate(fname)
                emi.calculaterates(params)
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
