from datetime import datetime
import os

import PySimpleGUI as sg

from LevMarJO import LevMar
from multiplet import Multiplet

layout = [
    [multiline := sg.Multiline(size=(120, 20), key="ML", reroute_stdout=True)],  # FIXME: bez reroute_...
    [sg.Button("Load absorption data", key="LOAD"), sg.Button("Rate", key="RATE")],
]

window = sg.Window("Judd Ofelt Solver in Python", layout, finalize=True)


x = Multiplet()
while True:
    event, values = window.read()
    # print(event, values)
    if event == "LOAD":
        x = Multiplet()
        filename = sg.popup_get_file("Will not see this message", no_window=True)
        window.bring_to_front()
        x.load_file(filename)
        multiline.print(x)
        params = LevMar(x)
        now = datetime.now()
        timestring = f"{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}"
        dirpath = os.path.dirname(filename)
        (file, ext) = os.path.splitext(os.path.basename(filename))
        with open(
            os.path.join(dirpath, "abso" + timestring + file + ".log"),
            "wt",
            encoding="UTF-8",
        ) as f:
            f.write(window["ML"].get())
    if event == "RATE":
        if x.is_fitted:
            filenames = sg.popup_get_file(
                "Will not see this message", no_window=True, multiple_files=True
            )
            window.bring_to_front()
            for fname in filenames:
                emi = Multiplet()
                emi.load_rate(fname)
                emi.calculate_rates(params)
            now = datetime.now()
            timestring = (
                f"{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}"
            )
            dirpath = os.path.dirname(filename)
            (file, ext) = os.path.splitext(os.path.basename(filename))
            with open(
                os.path.join(dirpath, "emi" + timestring + file + ".log"),
                "wt",
                encoding="UTF-8",
            ) as f:
                f.write(window["ML"].get())
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
