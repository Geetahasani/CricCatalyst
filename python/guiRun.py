
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\python\PythonMPR\root\python\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#0A1123")


canvas = Canvas(
    window,
    bg = "#0A1123",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    86.0,
    1024.0,
    fill="#272A5E",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    43.0,
    123.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    42.0,
    230.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    40.0,
    337.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    44.0,
    444.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    248.0,
    86.0,
    image=image_image_5
)

canvas.create_rectangle(
    588.0,
    80.0,
    720.0,
    123.0,
    fill="#36529D",
    outline="")

canvas.create_rectangle(
    751.0,
    80.0,
    874.0,
    123.0,
    fill="#5472BE",
    outline="")

canvas.create_text(
    636.0,
    93.0,
    anchor="nw",
    text="Player",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    791.0,
    94.0,
    anchor="nw",
    text="Team",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    126.0,
    159.5,
    1028.5,
    333.5,
    fill="#000000",
    outline="")

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    932.0,
    240.0,
    image=image_image_6
)

canvas.create_text(
    140.0,
    202.0,
    anchor="nw",
    text="Virat Kohli",
    fill="#000000",
    font=("Inter Bold", 48 * -1)
)

canvas.create_text(
    566.0,
    201.0,
    anchor="nw",
    text="593\n",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    559.0,
    272.0,
    anchor="nw",
    text="254*",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    653.0,
    201.0,
    anchor="nw",
    text="27394",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    673.0,
    266.9999957084656,
    anchor="nw",
    text="57",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    779.0,
    202.0,
    anchor="nw",
    text="70\n",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    779.0,
    262.0,
    anchor="nw",
    text="18",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    559.0,
    232.0,
    anchor="nw",
    text="Matches",
    fill="#000000",
    font=("Inter Light", 16 * -1)
)

canvas.create_text(
    559.0,
    297.0,
    anchor="nw",
    text="Highest",
    fill="#000000",
    font=("Inter Light", 16 * -1)
)

canvas.create_text(
    655.0,
    233.0,
    anchor="nw",
    text="Total Runs",
    fill="#000000",
    font=("Inter Light", 16 * -1)
)

canvas.create_text(
    665.0,
    298.0,
    anchor="nw",
    text="M.O.M",
    fill="#000000",
    font=("Inter Light", 16 * -1)
)

canvas.create_text(
    758.0,
    232.0,
    anchor="nw",
    text="Centuries",
    fill="#000000",
    font=("Inter Light", 16 * -1)
)

canvas.create_text(
    758.0,
    295.0,
    anchor="nw",
    text="Jersy No",
    fill="#000000",
    font=("Inter Light", 16 * -1)
)

canvas.create_text(
    140.0,
    266.0,
    anchor="nw",
    text="Right-Handed Batsman \n",
    fill="#000000",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    538.0,
    186.0,
    anchor="nw",
    text="\n",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)

canvas.create_rectangle(
    140.0,
    361.0,
    673.0,
    997.0,
    fill="#072033",
    outline="")

canvas.create_rectangle(
    693.0,
    365.0,
    1192.0,
    611.0,
    fill="#072033",
    outline="")

canvas.create_rectangle(
    693.0,
    625.0,
    1192.0,
    997.0,
    fill="#072033",
    outline="")

canvas.create_rectangle(
    1214.0,
    29.0,
    1420.0,
    997.0,
    fill="#136689",
    outline="")
window.resizable(False, False)
window.mainloop()
