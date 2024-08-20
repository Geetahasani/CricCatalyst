import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import matplotlib.pyplot as plt
from PIL import ImageTk,Image

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def calculate_runs_distribution(data, batter_name):
    runs_count = {'6': 0, '4': 0, '3': 0, '2': 0, '1': 0}
    for row in data:
        if row['Batter'].lower() == batter_name.lower():  # Convert to lowercase for comparison
            batter_runs = row['Batter Runs']
            for run_type, count in runs_count.items():
                runs_count[run_type] += batter_runs.count(run_type)
    return runs_count

def generate_pie_chart(runs_count, batter_name):
    labels = list(runs_count.keys())
    sizes = list(runs_count.values())
    explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, autopct=lambda p: '{:.0f}'.format(p * sum(sizes) / 100),
            shadow=True, startangle=140, wedgeprops={'width': 0.25})
    plt.axis('off')
    plt.title(f"{batter_name.capitalize()} Runs Type")
    plt.show()

def get_batter_name():
    batter_name = batter_entry.get().lower()  # Convert to lowercase
    if batter_name:
        generate_pie_chart_from_csv(csv_filename, batter_name)

def generate_pie_chart_from_csv(filename, batter_name):
    data = read_csv(filename)
    runs_count = calculate_runs_distribution(data, batter_name)
    if sum(runs_count.values()) == 0:
        messagebox.showinfo("No Data", "No data available for the selected batter.")
    else:
        generate_pie_chart(runs_count, batter_name)

# Predefined CSV file
csv_filename = "F:\\python\\PythonMPR\\root\\data\\ball_by_ball_ipl.csv"

# Create tkinter window
root = tk.Tk()
root.title("Batter's Runs Distribution")
root.state('zoomed')

image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1.jpg")

    # Convert the image to a format supported by Tkinter
photo = ImageTk.PhotoImage(image)

    # Create a label with the background image
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label and Entry for batter's name
batter_label = tk.Label(root, text="Batter",font=('Consolas', 20, 'bold'))
batter_label.pack(pady=(150,10))
batter_entry = tk.Entry(root,font=('Consolas', 15, 'bold'),bd=5)
batter_entry.pack(pady=(5,10))

# Button to generate pie chart
generate_button = tk.Button(root, text="Show Data", command=get_batter_name,font=('Consolas', 15, 'bold'),bd=5,bg='blue')
generate_button.pack(pady=(10,10))

# Run tkinter main loop
root.mainloop()
