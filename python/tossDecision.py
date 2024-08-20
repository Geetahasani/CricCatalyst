import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# csv change kr lena
file_path = 'F:\\python\\PythonMPR\\root\\data\\IPL Matches 2008-2020.csv'
data = pd.read_csv(file_path)

# Convert city names to lowercase
data['city'] = data['city'].str.lower()


# Function to create pie chart for toss decisions in a given city
def create_pie_chart(city_name):
    city_name = city_name.lower()  # Convert user input to lowercase
    city_data = data[data['city'] == city_name]

    if city_data.empty:
        messagebox.showerror("Error", "No data available for the entered city.")
        return

    toss_decision_counts = city_data['toss_decision'].value_counts()

    # Plotting
    plt.figure(figsize=(12, 5),facecolor='lightblue')
    plt.pie(toss_decision_counts, labels=toss_decision_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Toss Decisions at {city_name.capitalize()}",fontdict={'fontsize': 16, 'fontweight': 'bold', 'family': 'Consolas'},pad=20)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()


# Function to handle button click event
def on_button_click():
    city_input = city_entry.get()
    if not city_input:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    create_pie_chart(city_input)


# Create Tkinter GUI
root = tk.Tk()
root.title("Toss Decisions")
root.state('zoomed')

image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1.jpg")

# Convert the image to a format supported by Tkinter
photo = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label and Entry for city name
city = tk.Label(root, text="Enter Venue", font=('consolas', 25, 'bold'),bg='grey')
city.place(relx=0.5, rely=0.4, anchor='center')

city_entry = tk.Entry(root,font=('consolas', 15, 'bold'))
city_entry.place(relx=0.5, rely=0.5, anchor='center')

# Button to generate pie chart
button = tk.Button(root, text="Submit", command=on_button_click, bd=5, font=('consolas', 15, 'bold'), bg='blue')
button.place(relx=0.5, rely=0.6, anchor='center')

root.mainloop()
