import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\python\PythonMPR\root\python\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def image_1_clicked():
    print("Image 1 clicked")
    window.destroy()
    subprocess.Popen(["python", "sample.py"])

def image_2_clicked():
    print("Image 2 clicked")

def image_3_clicked():
    print("Image 3 clicked")

window = Tk()
window.configure(bg="#FFFFFF")
window.geometry('1400x780')

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=780,
    width=1400,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    150.0,
    fill="#0400E3",
    outline=""
)

canvas.create_text(
    32.0,
    43.0,
    anchor="nw",
    text="CrickCatalyst",
    fill="#FFD600",
    font=('Consolas', 64 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    247.0,
    268.0,
    image=image_image_1,
    tags="image1"
)
canvas.tag_bind("image1", "<Button-1>", lambda event: image_1_clicked())

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    247.0,
    461.0,
    image=image_image_2,
    tags="image2"
)
canvas.tag_bind("image2", "<Button-1>", lambda event: image_2_clicked())

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    247.0,
    654.0,
    image=image_image_3,
    tags="image3"
)
canvas.tag_bind("image3", "<Button-1>", lambda event: image_3_clicked())

canvas.create_text(
    207.0,
    257.0,
    anchor="nw",
    text="Batsmen",
    fill="#000000",
    font=('Consolas', 20 * -1)
)

canvas.create_text(
    212.0,
    450.0,
    anchor="nw",
    text="Bowler",
    fill="#000000",
    font=('Consolas', 20 * -1)
)

canvas.create_text(
    189.0,
    643.0,
    anchor="nw",
    text="All-Rounder",
    fill="#000000",
    font=('Consolas', 20 * -1)
)

window.mainloop()
