import csv
import tkinter as tk
from tkinter import ttk

def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def main():
    root = tk.Tk()
    root.title('CSV Table')

    # Load CSV data
    data = load_csv('F:\\python\\PythonMPR\\root\\data\\IPL Matches 2008-2020.csv')

    # Create Treeview widget
    tree = ttk.Treeview(root)

    # Insert headings
    tree["columns"] = data[0]
    tree.heading('#0', text='Index')
    for col in data[0]:
        tree.heading(col, text=col)

    # Insert data
    for i, row in enumerate(data[1:], start=1):
        tree.insert('', 'end', text=str(i), values=row)

    # Create vertical scrollbar
    v_scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    v_scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=v_scrollbar.set)

    # Create horizontal scrollbar
    h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
    h_scrollbar.pack(side="bottom", fill="x")
    tree.configure(xscrollcommand=h_scrollbar.set)

    # Display Treeview
    tree.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()
