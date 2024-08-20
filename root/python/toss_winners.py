import csv
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import mplcursors

def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def main():
    data = load_csv('F:\\python\\PythonMPR\\root\\data\\IPL Matches 2008-2020.csv')

    # Extracting toss winners and their counts
    toss_winners = [row[data[0].index('toss_winner')] for row in data[1:]]
    toss_winner_counts = {}
    for winner in toss_winners:
        toss_winner_counts[winner] = toss_winner_counts.get(winner, 0) + 1

    # Sorting the toss winners by count
    sorted_toss_winners = sorted(toss_winner_counts.items(), key=lambda x: x[1], reverse=True)

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    bars = plt.bar([team[0] for team in sorted_toss_winners], [team[1] for team in sorted_toss_winners], color='turquoise')
    bars[0].set_color('purple')  # Setting the color of the team with the most toss wins
    bars[14].set_color('black')
    # Adding labels and title
    plt.xlabel('Teams')
    plt.ylabel('Number of Toss Wins')
    plt.title('Number of Tosses Won by Each Team')


    plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent overlap of labels

    cursor = mplcursors.cursor(bars, hover=True)  # Create a cursor object
    cursor.connect("add",lambda sel: sel.annotation.set_text(sorted_toss_winners[sel.target.index][1]))  # Display the count

    plt.show()



if __name__ == "__main__":
    main()
