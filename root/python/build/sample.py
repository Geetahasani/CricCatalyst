from tkinter import *

root = Tk()
root.title('Ok')
#root.geometry('1400x780')

lbl=Label(root,
          text='Hello',
          font=('Consolas',40),
          fg='black')
lbl.pack()
root.mainloop()