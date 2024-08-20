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


def get_venue(team1, team2):
    venues = set()
    for match in matches_data:
        if match['TEAM1'] == team1 and match['TEAM2'] == team2:
            venues.add(match['Venue'])
    return sorted(list(venues))


def calculate_win_probabilities(team1, team2, venue):
    total_matches = 0
    team1_wins = 0
    team2_wins = 0

    for match in matches_data:
        if match['TEAM1'] == team1 and match['TEAM2'] == team2 and match['Venue'] == venue:
            total_matches += 1
            if match['Winner'] == team1:
                team1_wins += 1
            elif match['Winner'] == team2:
                team2_wins += 1

    if total_matches == 0:
        return None, None

    team1_win_prob = (team1_wins / total_matches) * 100
    team2_win_prob = (team2_wins / total_matches) * 100

    return team1_win_prob, team2_win_prob


def generate_pie_chart(team1, team2, venue):
    team1_win_prob, team2_win_prob = calculate_win_probabilities(team1, team2, venue)

    if team1_win_prob is None or team2_win_prob is None:
        print("No data available for the selected teams and venue.")
        return

    labels = [team1, team2]
    sizes = [team1_win_prob, team2_win_prob]
    explode = (0.1, 0)  # explode the 1st slice

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title( team1 + ' vs ' + team2 + ' at ' + venue)
    plt.show()


def submit_action():
    team1 = team1_var.get()
    team2 = team2_var.get()
    venue = get_venue(team1, team2)
    venue_dropdown['values'] = venue


def submit_date_action():
    team1 = team1_var.get()
    team2 = team2_var.get()
    venue = venue_var.get()
    generate_pie_chart(team1, team2, venue)


# Read CSV file
matches_data = read_csv('F:\\python\\PythonMPR\\root\\data\\ball_by_ball_ipl.csv')

# Create tkinter window
root = tk.Tk()
root.title("Match Points")
root.state('zoomed')

image = Image.open("F:\\python\\PythonMPR\\root\\data\\bg1v1.jpg")

photo = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create widgets
team1_label = tk.Label(root, text="Team 1", font=('consolas', 20, 'bold'), bg='lightblue')
team1_label.place(relx=0.45, rely=0.1)
team1_var = tk.StringVar()
team1_dropdown = ttk.Combobox(root, textvariable=team1_var, values=get_teams())
team1_dropdown.place(relx=0.45, rely=0.2)

team2_label = tk.Label(root, text="Team 2", font=('consolas', 20, 'bold'), bg='lightblue')
team2_label.place(relx=0.45, rely=0.3)
team2_var = tk.StringVar()
team2_dropdown = ttk.Combobox(root, textvariable=team2_var, values=get_teams())
team2_dropdown.place(relx=0.45, rely=0.4)

submit_button = tk.Button(root, text="Submit", command=submit_action, font=('consolas', 15, 'bold'), bg='blue', bd=5)
submit_button.place(relx=0.45, rely=0.5)

venue_label = tk.Label(root, text="Match venue", font=('consolas', 20, 'bold'), bg='lightgreen')
venue_label.place(relx=0.45, rely=0.6)
venue_var = tk.StringVar()
venue_dropdown = ttk.Combobox(root, textvariable=venue_var)
venue_dropdown.place(relx=0.45, rely=0.7)

submit_date_button = tk.Button(root, text="Submit", command=submit_date_action, font=('consolas', 15, 'bold'),
                               bg='blue', bd=5)
submit_date_button.place(relx=0.45, rely=0.8)

# Center the window
root.geometry(f"+{int((screen_width - root.winfo_reqwidth()) / 2)}+{int((screen_height - root.winfo_reqheight()) / 2)}")

# Run tkinter main loop
root.mainloop()
