import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv
from PIL import Image,ImageTk

def calculate_base_points(wickets_taken, base_points_per_wicket):
    return wickets_taken * base_points_per_wicket

def get_economy_bonus(economy_rate, number_of_overs):
    if economy_rate < 3.0:
        return 10 * number_of_overs
    elif economy_rate < 4.0:
        return 5 * number_of_overs
    elif economy_rate < 30.0:
        return 2 * number_of_overs
    else:
        return 0

def get_maiden_bonus(number_of_maiden_overs, maiden_over_points):
    return number_of_maiden_overs * maiden_over_points

def get_weather_adjustment(pitch_type, bonus_points):
    if pitch_type == "bowler-friendly" and bonus_points > 90:
        return 9
    elif pitch_type == "batsman-friendly" and bonus_points > 90:
        return 10
    elif pitch_type == "bowler-friendly" and bonus_points > 70:
        return 7
    elif pitch_type == "batsman-friendly" and bonus_points > 70:
        return 8
    elif pitch_type == "bowler-friendly" and bonus_points > 50:
        return 5
    elif pitch_type == "batsman-friendly" and bonus_points > 50:
        return 6
    elif pitch_type == "bowler-friendly" and bonus_points > 30:
        return 3
    elif pitch_type == "batsman-friendly" and bonus_points > 30:
        return 4
    elif pitch_type == "bowler-friendly" and bonus_points > 10:
        return 1
    elif pitch_type == "batsman-friendly" and bonus_points > 10:
        return 2
    else:
        return 0  # Default value if no conditions match

def calculate_total_points(row):
    if row[4] == '' or row[1] == '' or row[3] == '':
        return 0, 0, 0  # or any default value you prefer
    else:
        number_of_overs = int(row[1])
        wickets_taken = int(row[3])
        economy_rate = float(row[4])
        number_of_maiden_overs = int(row[6])
        base_points_per_wicket = 10  # You can adjust this value
        maiden_over_points = 20  # You can adjust this value
        pitch_type = row[5]

        base_points = calculate_base_points(wickets_taken, base_points_per_wicket)
        economy_bonus = get_economy_bonus(economy_rate, number_of_overs)
        maiden_bonus = get_maiden_bonus(number_of_maiden_overs, maiden_over_points)
        bonus_points = economy_bonus + maiden_bonus + base_points
        weather_adjustment = get_weather_adjustment(pitch_type, bonus_points)

        total_points = bonus_points + weather_adjustment
        return total_points, bonus_points, weather_adjustment, base_points

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            # Check if any field is empty and replace it with a default value
            for i in range(len(row)):
                if row[i] == '':
                    row[i] = '0'  # or any default value you prefer
            data.append(row)
    return data

def generate_dashboard(data):
    root = tk.Tk()
    root.title("Bowler Points Dashboard")

    # Create a frame to hold the Treeview
    frame1 = ttk.Frame(root)
    frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Create a Treeview with a new column for base points
    tree = ttk.Treeview(frame1, columns=('Players', 'Total Points', 'Bonus Points', 'Weather Adjustment', 'Base Points'))
    tree.heading('#0', text='Index')
    tree.heading('#1', text='Players')
    tree.heading('#2', text='Bonus Points=economy_bonus + maiden_bonus + base_points')
    tree.heading('#3', text='Weather Adjustment (DEPENDING ON PITCH AND BONUS POINTS')
    tree.heading('#4', text='Base Points=wickets_taken * base_points_per_wicket')
    tree.heading('#5', text='Total Points=bonus_points + weather_adjustment')

    for i, row in enumerate(data):
        total_points, bonus_points, weather_adjustment, base_points = calculate_total_points(row)
        tree.insert('', 'end', text=str(i), values=(row[0], total_points, bonus_points, weather_adjustment, base_points))

    tree.pack(expand=True, fill='both')

    # Create a frame to hold the figure
    frame2 = ttk.Frame(root)
    frame2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Create the matplotlib figure
    fig, ax = plt.subplots()
    players = [row[0] for row in data]
    points = [calculate_total_points(row)[0] for row in data]
    ax.bar(players, points)
    ax.set_xlabel('Players')
    ax.set_ylabel('Total Points')
    ax.set_title('Bowler Points')

    # Embed the matplotlib figure within the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)
    root.geometry("4000x2000")
    root.mainloop()
    root.configure(bg="dark blue")

def open_window1():
    filename = "F:\\python\\PythonMPR\\root\\data\\HEHE.csv"  # Change this to your CSV file
    data = read_csv(filename)
    generate_dashboard(data)


def open_window2():
    window2 = tk.Toplevel(root)
    window2.title("Batsman Points Dashboard")
    window2.geometry("4000x2000")  # Adjust window size as needed
    window2.configure(bg="dark blue")

    def calculate_total_points(row):
        try:
            batter = row[0]
            runs = int(row[1])
            balls = int(row[2])
            fours = int(row[3])
            sixes = int(row[4])
            strike_rate = float(row[5])
            pitch_type = row[6]

            # Calculate total points based on strike rate and pitch type
            total_points = strike_rate
            if pitch_type == "batsman-friendly":
                return total_points * 1  # Double points for batsman-friendly pitch
            elif pitch_type == "bowler-friendly":
                return total_points * 2
        except (IndexError, ValueError) as e:
            print(f"Ignoring row due to insufficient data: {row}")
            return None

    def read_csv(filename):
        data = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                total_points = calculate_total_points(row)
                if total_points is not None:
                    data.append((row[0], total_points))
        return data

    data = read_csv("F:\\python\\PythonMPR\\root\\data\\HEHE2.csv")  # Update with your CSV file name

    # Create a Treeview to display data
    tree = ttk.Treeview(window2, columns=('Batter', 'Total Points'))
    tree.heading('#0', text='Index')
    tree.heading('#1', text='Batter')
    tree.heading('#2', text='Total Points')

    for i, (batter, total_points) in enumerate(data):
        tree.insert('', 'end', text=str(i), values=(batter, total_points))

    tree.pack(side=tk.LEFT, expand=True, fill='both')

    # Create a frame to hold the matplotlib plot
    frame2 = ttk.Frame(window2)
    frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create the matplotlib figure
    fig, ax = plt.subplots()
    batters = [batter for batter, _ in data]
    points = [points for _, points in data]
    ax.plot(batters, points, marker='o', color='b')
    ax.set_xlabel('Batters')
    ax.set_ylabel('Total Points')
    ax.set_title('Batsman Points')

    # Embed the matplotlib figure within the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)


root = tk.Tk()
root.title("Rate Players on Their Performance Based on Pitch")
root.state('zoomed')
custom_font = ("consolas", 30,'bold')

image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1.jpg")
photo = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = tk.Label(root, text="Analyse Player's Performance", font=custom_font)
label1.place(relx=0.5, rely=0.3, anchor='center')

button1 = tk.Button(root, text="Bowlers", command=open_window1, font=("consolas",15,'bold'),bg='blue',bd=5)
button1.place(relx=0.4, rely=0.5, anchor='center')

button2 = tk.Button(root, text="Batters", command=open_window2, font=("consolas",15,'bold'),bg='blue',bd=5)
button2.place(relx=0.6, rely=0.5, anchor='center')

root.configure(bg="dark blue")
root.mainloop()


