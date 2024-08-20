import tkinter as tk
from tkinter import ttk
import csv
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def get_teams():
    teams = set()
    for match in matches_data:
        teams.add(match.get('TEAM1'))
        teams.add(match.get('TEAM2'))
    return sorted(list(teams))

def get_dates(team1, team2):
    dates = set()
    for match in matches_data:
        if match['TEAM1'] == team1 and match['TEAM2'] == team2:
            dates.add(match['Date'])
    return sorted(list(dates), key=lambda x: tuple(map(int, x.split('-'))))  # Sort dates

def retrieve_match_data():
    team1 = team1_var.get()
    team2 = team2_var.get()
    selected_date = date_dropdown.get()

    match_data = [match for match in matches_data if
                  match['TEAM1'] == team1 and match['TEAM2'] == team2 and match['Date'] == selected_date]
    return match_data

def calculate_points(match_data):
    points = {}
    for player in match_data:
        batter_name = player['Batter']
        bowler_name = player['Bowler']
        batter_runs = int(player['Batter Runs'])
        bowler_runs = int(player['Batter Runs'])

        # Calculate points for batters
        batter_points = batter_runs * 2 if batter_runs % 2 == 0 else batter_runs * 2 + 2
        points[batter_name] = points.get(batter_name, 0) + batter_points

        # Calculate points for bowlers
        bowler_points = bowler_runs * 2
        points[bowler_name] = points.get(bowler_name, 0) + bowler_points

    return points

def generate_bar_graph(points):
    plt.figure(figsize=(10, 5))
    bars = plt.bar(range(len(points)), list(points.values()), align='center', color=['blue', 'red'])
    plt.xticks(range(len(points)), list(points.keys()), rotation=45)
    plt.xlabel('Players')
    plt.ylabel('Points')
    plt.title('Points Scored by Batters and Bowlers')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

    plt.show()

def submit_action():
    team1 = team1_var.get()
    team2 = team2_var.get()
    dates = get_dates(team1, team2)
    date_dropdown['values'] = dates

def submit_date_action():
    match_data = retrieve_match_data()
    if match_data:
        points = calculate_points(match_data)
        generate_bar_graph(points)

# Read CSV file
matches_data = read_csv('F:\\python\\PythonMPR\\root\\data\\ball_by_ball_ipl.csv')

# Create tkinter window
root = tk.Tk()
root.title("Match Points")
root.state('zoomed')

image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1.jpg")
photo = ImageTk.PhotoImage(image)

# Create a label with the image as the background
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

team1_label = tk.Label(root, text="Home Team", font=('consolas',20,'bold'), bg='lightblue')
team1_label.place(relx=0.45, rely=0.1)
team1_var = tk.StringVar()
team1_dropdown = ttk.Combobox(root, textvariable=team1_var, values=get_teams())
team1_dropdown.place(relx=0.45, rely=0.2)

team2_label = tk.Label(root, text="Away Team", font=('consolas',20,'bold'), bg='lightblue')
team2_label.place(relx=0.45, rely=0.3)
team2_var = tk.StringVar()
team2_dropdown = ttk.Combobox(root, textvariable=team2_var, values=get_teams())
team2_dropdown.place(relx=0.45, rely=0.4)

submit_button = tk.Button(root, text="Submit", command=submit_action, font=('consolas',15,'bold'), bg='blue',bd=5)
submit_button.place(relx=0.45, rely=0.5)

date_label = tk.Label(root, text="Match Dates", font=('consolas',20,'bold'), bg='lightgreen')
date_label.place(relx=0.45, rely=0.6)
date_var = tk.StringVar()
date_dropdown = ttk.Combobox(root, textvariable=date_var)
date_dropdown.place(relx=0.45, rely=0.7)

submit_date_button = tk.Button(root, text="Submit", command=submit_date_action, font=('consolas',15,'bold'), bg='blue',bd=5)
submit_date_button.place(relx=0.45, rely=0.8)

root.geometry(f"+{int((screen_width - root.winfo_reqwidth()) / 2)}+{int((screen_height - root.winfo_reqheight()) / 2)}")

root.mainloop()