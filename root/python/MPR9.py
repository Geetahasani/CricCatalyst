import csv
import tkinter as tk
from tkinter import ttk, simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculate_batsman_points(score):
    if score == 6:
        return 10
    elif score == 4:
        return 8
    elif score == 3:
        return 6
    elif score == 2:
        return 4
    elif score == 1:
        return 2
    else:
        return 0


def calculate_bowlers_points(score, wicket):
    points = 0
    if score == 6:
        points = 0
    elif score == 4:
        points = 0
    elif score == 3:
        points = 2
    elif score == 2:
        points = 4
    elif score == 1:
        points = 8
    elif score == 0:
        points = 10
    else:
        points = 0

    # Bonus points for taking wickets
    points += wicket * 5
    return points


def process_csv(filename, team1, team2, selected_year):
    batsmen_data = []
    bowlers_data = []

    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            match_date = row['Date']
            match_year = match_date.split('-')[-1]

            if match_year == selected_year and ((row['Bat First'] == team1 and row['Bat Second'] == team2) or
                                                 (row['Bat First'] == team2 and row['Bat Second'] == team1)):
                batsman_name = row['Batter']
                bowler_name = row['Bowler']
                score = int(row['Batter Runs'])
                wicket = int(row['Wicket'])

                batsman_points = calculate_batsman_points(score)
                bowler_points = calculate_bowlers_points(score, wicket)

                batsmen_data.append((batsman_name, score, batsman_points))
                bowlers_data.append((bowler_name, score, bowler_points, wicket))

    return batsmen_data, bowlers_data


def display_data(batsmen_data, bowlers_data):
    root = tk.Tk()
    root.title("Batsmen and Bowlers Points")
    root.geometry("1920x1080")

    # Load background image


    # Create frames for tables and matplotlib plot
    table_frame = ttk.Frame(root)
    table_frame.pack(fill='both', expand=True, side='top')

    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill='both', expand=True, side='bottom')

    # Create labels for tables
    batsmen_label = ttk.Label(table_frame, text="Batters")
    batsmen_label.pack(side='top', padx=10, pady=5)

    bowlers_label = ttk.Label(table_frame, text="Bowlers")
    bowlers_label.pack(side='top', padx=10, pady=5)

    # Create batsmen table
    batsmen_table = ttk.Treeview(table_frame, columns=('Name', 'Score', 'Points'), show='headings')
    batsmen_table.heading('Name', text='Name')
    batsmen_table.heading('Score', text='Score')
    batsmen_table.heading('Points', text='Points')

    # Create bowlers table
    bowlers_table = ttk.Treeview(table_frame, columns=('Name', 'Score', 'Points', 'Wickets'), show='headings')
    bowlers_table.heading('Name', text='Name')
    bowlers_table.heading('Score', text='Score')
    bowlers_table.heading('Points', text='Points')
    bowlers_table.heading('Wickets', text='Wickets')

    for data in batsmen_data:
        batsmen_table.insert('', 'end', values=data)

    for data in bowlers_data:
        bowlers_table.insert('', 'end', values=data)

    batsmen_table.pack(side='left', padx=10, pady=10, fill='both', expand=True)
    bowlers_table.pack(side='left', padx=10, pady=10, fill='both', expand=True)

    # Calculate total points for each player
    batsman_points_dict = {}
    for name, _, points in batsmen_data:
        if name not in batsman_points_dict:
            batsman_points_dict[name] = points
        else:
            batsman_points_dict[name] += points

    bowler_points_dict = {}
    for name, _, points, wickets in bowlers_data:
        if name not in bowler_points_dict:
            bowler_points_dict[name] = points + (wickets * 5)
        else:
            bowler_points_dict[name] += points + (wickets * 5)

    # Combine batsmen and bowlers points
    players = list(batsman_points_dict.keys()) + list(bowler_points_dict.keys())
    total_points = [batsman_points_dict.get(player, 0) + bowler_points_dict.get(player, 0) for player in players]

    # Create bar graph
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot batsmen points with blue color
    ax.bar(players[:len(batsman_points_dict)],
           [batsman_points_dict[player] for player in players[:len(batsman_points_dict)]], color='skyblue',
           label='Batsmen')

    # Plot bowlers points with green color
    ax.bar(players[len(batsman_points_dict):],
           [bowler_points_dict[player] for player in players[len(batsman_points_dict):]], color='lightgreen',
           label='Bowlers')

    ax.set_xlabel('Players', fontsize=12)
    ax.set_ylabel('Total Points', fontsize=12)
    ax.set_title('Total Points of Players', fontsize=14, fontweight='bold')
    ax.tick_params(axis='x', rotation=45, labelsize=8)
    ax.grid(True)
    ax.legend(loc='upper right')

    # Embed the plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

    root.mainloop()


if __name__ == "__main__":
    filename = "F:\\python\\PythonMPR\\root\\data\\ball_by_ball_ipl.csv"  # Replace with your CSV file path

    # Ask input from the user for home team (TEAM1) and away team (TEAM2)
    team1 = tk.simpledialog.askstring("Input", "Enter Home Team:")
    team2 = tk.simpledialog.askstring("Input", "Enter Away Team:")

    # Create a dropdown menu for selecting the year
    root = tk.Tk()
    root.title("Select Year")
    root.geometry("1920x1080")

    selected_year = tk.StringVar(root)
    selected_year.set("2023")  # Set default value

    years = [str(year) for year in range(2008, 2024)]

    year_label = ttk.Label(root, text="Select Year:")
    year_label.pack(pady=5)

    year_menu = ttk.OptionMenu(root, selected_year, *years)
    year_menu.pack(pady=5)

    ok_button = ttk.Button(root, text="OK", command=root.destroy)
    ok_button.pack(pady=5)

    root.mainloop()

    batsmen_data, bowlers_data = process_csv(filename, team1, team2, selected_year.get())
    display_data(batsmen_data, bowlers_data)
