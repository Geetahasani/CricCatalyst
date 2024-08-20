import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox

# Load CSV file into a DataFrame
file_path = 'F:\\python\\PythonMPR\\root\\data\\IPL Matches 2008-2020.csv'  # Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
data = pd.read_csv(file_path)

# Function to create pie chart for toss winner wins and losses in a given city
def create_pie_chart(city_name):
    city_name = city_name.lower()  # Convert user input to lowercase
    city_data = data[data['city'].str.lower() == city_name]

    if city_data.empty:
        messagebox.showerror("Error", "No data available for the entered city.")
        return

    # Counting wins and losses
    wins = city_data[(city_data['toss_winner'] == city_data['winner'])]['toss_winner'].count()
    losses = city_data.shape[0] - wins

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.pie([wins, losses], labels=['Wins', 'Losses'], autopct='%1.1f%%', startangle=140)
    plt.title(f"Toss Winner Wins and Losses in {city_name.capitalize()}")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()


# Function to handle button click event
def on_button_click():
    city_input = city_entry.get().lower()
    if not city_input:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    create_pie_chart(city_input)


# Create Tkinter GUI
root = tk.Tk()
root.title("Toss Winner Wins and Losses")
#root.geometry('400x200')
root.state('zoomed')


image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1.jpg")

# Convert the image to a format supported by Tkinter
photo = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label and Entry for city name
city_label =tk.Label(root, text="Enter City",font=('consolas', 25, 'bold'))
city_label.place(relx=0.5, rely=0.4, anchor='center')

city_entry = tk.Entry(root,font=('consolas', 15, 'bold'))
city_entry.place(relx=0.5, rely=0.5, anchor='center')

# Button to generate pie chart
generate_button = tk.Button(root, text="Show Pie-Chart", command=on_button_click,font=('consolas', 15, 'bold'),bd=5,bg='blue')
generate_button.place(relx=0.5, rely=0.6, anchor='center')



root.mainloop()
