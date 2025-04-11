import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("400x300")
        self.number_to_guess = 0
        self.attempts = 0
        self.setup_ui()

    def setup_ui(self):
        self.label_title = tk.Label(self, text="Number Guessing Game", font=("Arial", 20))
        self.label_title.pack(pady=20)

        self.label_instructions = tk.Label(self, text="Guess a number between 1 and 100:")
        self.label_instructions.pack()

        self.entry_guess = tk.Entry(self)
        self.entry_guess.pack(pady=10)

        self.button_submit = tk.Button(self, text="Submit", command=self.check_guess)
        self.button_submit.pack(pady=5)

        self.button_reset = tk.Button(self, text="Reset", command=self.reset_game)
        self.button_reset.pack(pady=5)

        self.label_message = tk.Label(self, text="")
        self.label_message.pack(pady=10)

    def start_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self):
        guess = self.entry_guess.get()
        if guess.isdigit():
            guess = int(guess)
            self.attempts += 1
            if guess < self.number_to_guess:
              self.label_message.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.label_message.config(text="Too high! Try again.")
            else:
                self.label_message.config(text=f"Congratulations! You found the number in {self.attempts} attempts.")
                messagebox.showinfo("Congratulations!", f"You found the number in {self.attempts} attempts.")
                self.reset_game()
        else:
            self.label_message.config(text="Please enter a valid number.")
        # Reset the entry field
        self.entry_guess.delete(0, tk.END)


    def reset_game(self):
        self.start_game()
        self.entry_guess.delete(0, tk.END)
        self.label_message.config(text="")

if __name__ == "__main__":
    app = NumberGuessingGame()
    app.start_game()
    app.mainloop()
