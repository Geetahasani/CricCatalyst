import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import mplcursors

def open_1v1_file():
    subprocess.Popen(['python', 'F:\\python\\PythonMPR\\root\\python\\1v1.py'])

def open_tossDecision_file():
    subprocess.Popen(['python', 'F:\\python\\PythonMPR\\root\\python\\tossDecision.py'])

def open_MPR9A():
    subprocess.Popen(['python', 'F:\\python\\PythonMPR\\root\\python\\MPR9A.py'])

def open_winProb():
    subprocess.Popen(['python', 'F:\\python\\PythonMPR\\root\\python\\winProb.py'])

def open_batterStats():
    subprocess.Popen(['python', 'F:\\python\\PythonMPR\\root\\python\\batterStats.py'])

root = tk.Tk()
root.title('CricCatalyst')
#root.geometry('750x500')
root.state('zoomed')

image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1fc.jpg")
photo = ImageTk.PhotoImage(image)

# Create a label with the image as the background
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected

left_button1 = tk.Button(root, text="1v1", bg='cyan', bd=3, font=('Consolas', 15, 'bold'), width=15, command=open_1v1_file)
left_button1.place(relx=0.1, rely=0.2, anchor="center")

left_button2 = tk.Button(root, text="Toss Stats", bg='cyan', bd=3, font=('Consolas', 15, 'bold'), width=15, command=open_tossDecision_file)
left_button2.place(relx=0.1, rely=0.5, anchor="center")

left_button3 = tk.Button(root, text="Points", bg='cyan', bd=3, font=('Consolas', 15, 'bold'), width=15, command=open_MPR9A)
left_button3.place(relx=0.1, rely=0.8, anchor="center")

right_button1 = tk.Button(root, text="Batsmen Stats", bg='cyan', bd=3, font=('Consolas', 15, 'bold'), width=15, command=open_batterStats)
right_button1.place(relx=0.9, rely=0.2, anchor="center")

right_button2 = tk.Button(root, text="Win Probability", bg='cyan', bd=3, font=('Consolas', 15, 'bold'), width=15, command=open_winProb)  # Remove the parentheses here
right_button2.place(relx=0.9, rely=0.5, anchor="center")

right_button3 = tk.Button(root, text="R3", bg='cyan', bd=3, font=('Consolas', 15, 'bold'), width=15)
right_button3.place(relx=0.9, rely=0.8, anchor="center")

root.mainloop()
