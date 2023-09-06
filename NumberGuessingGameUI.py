import tkinter as tk
from tkinter import messagebox
from backend import NumberGuessingGame
import os
class NumberGuessingGameUI:
    def __init__(self):
        self.game = NumberGuessingGame()

    def run(self):
        root = tk.Tk()
        root.title("Number Guessing Game")

        self.label = tk.Label(root, text="Welcome to the Number Guessing Game!")
        self.label.pack()

        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.guess_label = tk.Label(root, text="Enter your guess (1-50):")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(root, state=tk.DISABLED)
        self.guess_entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.guess_number, state=tk.DISABLED)
        self.guess_button.pack()

        self.high_scores_label = tk.Label(root, text="Scores:")
        self.high_scores_label.pack()

        self.high_scores_list = tk.Listbox(root, height=10)
        self.high_scores_list.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

        root.mainloop()

    def start_game(self):
        self.game.start_game(self.name_entry.get())
        self.label.config(text=f"Welcome to the Number Guessing Game, {self.game.player_name}! You have {self.game.max_guesses} guesses to guess the number between 1 and 50.")
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
    def update_high_scores(self):
        filename = "D:\high_scores.txt"
        with open(filename, "r") as f:
            for line in f:
                self.high_scores_list.insert(tk.END,line)

    def save_high_score(self):
        filename = "D:\high_scores.txt"
        high_scores = self.game.get_high_scores()
        with open(filename, "a") as f:
            f.write(high_scores[0] + " " + str(high_scores[1]) + "\n")

    def guess_number(self):
        guess = self.guess_entry.get()
        result = self.game.guess_number(int(guess))
        self.label.config(text=result)
        if self.game.game_over:
            self.guess_entry.config(state=tk.DISABLED)
            self.guess_button.config(state=tk.DISABLED)
            self.save_high_score()
            self.update_high_scores()

    