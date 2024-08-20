import csv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def filter_data(data, batsman, bowler):
    runs_scored = 0
    balls_faced = 0
    times_out = 0
    for row in data[1:]:
        row_batsman = row[data[0].index('Batter')].upper()  # Get the batsman name from the CSV data
        row_bowler = row[data[0].index('Bowler')].upper()   # Get the bowler name from the CSV data
        if row_batsman == batsman and row_bowler == bowler:
            runs_scored += int(row[data[0].index('Batter Runs')])
            balls_faced += 1  # Increment balls faced for each ball played
            dismissal_kind = row[data[0].index('Wicket')].lower()
            if '1' in dismissal_kind:
                times_out += 1
    return runs_scored, balls_faced, times_out



def show_stats(batsman_entry, bowler_entry, tree, batsman_label, data):
    batsman = batsman_entry.get().upper()  # Convert to uppercase
    bowler = bowler_entry.get().upper()    # Convert to uppercase
    batsman_label.config(text=f"{batsman} vs {bowler}", bg='white')  # Update label text

    runs_scored, balls_faced, times_out = filter_data(data, batsman, bowler)

    strike_rate = 0
    if balls_faced > 0:
        strike_rate = (runs_scored / balls_faced) * 100

    tree.delete(*tree.get_children())  # Clear existing data in the treeview
    tree.insert('', 'end', values=[runs_scored, balls_faced, times_out, round(strike_rate, 2)])

    # Center-align data within the table
    for col in tree['columns']:
        tree.heading(col, anchor='center')
    for child in tree.get_children():
        tree.item(child, tags=(child,))
    tree.tag_configure(child, anchor='center')

    tree.pack()  # Show the table after populating it

def main():
    root = tk.Tk()
    root.title('1v1 Stats')
    root.state('zoomed')
    #root.geometry('750x500')
    root.config(background='')

    image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1.jpg")

    photo = ImageTk.PhotoImage(image)

    background_label = tk.Label(root, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Load CSV data
    data = load_csv('F:\\python\\PythonMPR\\root\\data\\ball_by_ball_ipl.csv')

    batsman_label = tk.Label(root, text="Batsman", fg='black', bg='white', font=('Consolas', 15, 'bold'))
    batsman_label.pack(pady=(20, 0))
    batsman_entry = tk.Entry(root, bd=3,font=('Consolas', 12))
    batsman_entry.pack(pady=(5, 0))

    bowler_label = tk.Label(root, text="Bowler", fg='black', bg='white', font=('Consolas', 15, 'bold'))
    bowler_label.pack(pady=(20, 0))
    bowler_entry = tk.Entry(root, bd=3,font=('Consolas', 12))
    bowler_entry.pack(pady=(5, 0))

    # Submit button
    submit_button = tk.Button(root, text="Submit", bg='cyan', bd=3, font=('Consolas', 15, 'bold'))
    submit_button.pack(pady=(20, 10))

    # Label to display batsman vs bowler
    batsman_vs_bowler_label = tk.Label(root, text="", font=('Consolas', 15, 'bold'))
    batsman_vs_bowler_label.pack(pady=(0, 10))

    # Table to display stats
    columns = ('Runs', 'Balls Faced', 'Outs', 'Strike Rate')
    tree = ttk.Treeview(root, columns=columns, show='headings', height=3)  # Increased height
    for col in columns:
        tree.heading(col, text=col, anchor='center')

    tree.configure(style="Custom.Treeview")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="cyan", fieldbackground="black", font=('Consolas', 12))  # Changing background and font

    submit_button.config(command=lambda: show_stats(batsman_entry, bowler_entry, tree, batsman_vs_bowler_label, data))

    root.mainloop()

if __name__ == "__main__":
    main()
