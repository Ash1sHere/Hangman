import tkinter as tk
import random

# Words and hints for the game
WORDS_AND_HINTS = [
    {"word": "python", "hint": "A popular programming language."},
    {"word": "hangman", "hint": "The name of this classic guessing game."},
    {"word": "developer", "hint": "A person who writes code."},
    {"word": "programming", "hint": "The process of creating software."},
    {"word": "openai", "hint": "The organization behind ChatGPT."},
    {"word": "artificial", "hint": "Opposite of natural, often used with 'intelligence'."},
    {"word": "intelligence", "hint": "The ability to acquire and apply knowledge."}
]

class HangmanGameWithHints:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game with Hints")
        
        # Game variables
        self.current_word_info = random.choice(WORDS_AND_HINTS)
        self.word_to_guess = self.current_word_info["word"]
        self.hint = self.current_word_info["hint"]
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.attempts_left = 6
        self.guessed_letters = set()

        # GUI Elements
        self.word_label = tk.Label(root, text=" ".join(self.guessed_word), font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.hint_label = tk.Label(root, text=f"Hint: {self.hint}", font=("Helvetica", 14))
        self.hint_label.pack(pady=10)

        self.message_label = tk.Label(root, text="Guess a letter!", font=("Helvetica", 14))
        self.message_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 18), justify="center")
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", font=("Helvetica", 14), command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.hangman_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Helvetica", 14))
        self.hangman_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def make_guess(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            self.message_label.config(text="Please enter a single letter.")
            return
        
        if letter in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter!")
            return

        self.guessed_letters.add(letter)

        if letter in self.word_to_guess:
            self.message_label.config(text="Good guess!")
            for i, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.guessed_word[i] = letter
        else:
            self.attempts_left -= 1
            self.message_label.config(text=f"Wrong guess! '{letter}' is not in the word.")

        self.update_game_state()

    def update_game_state(self):
        self.word_label.config(text=" ".join(self.guessed_word))
        self.hangman_label.config(text=f"Attempts left: {self.attempts_left}")

        if "_" not in self.guessed_word:
            self.message_label.config(text="Congratulations! You won!")
            self.end_game()
        elif self.attempts_left <= 0:
            self.message_label.config(text=f"You lost! The word was '{self.word_to_guess}'.")
            self.end_game()

    def end_game(self):
        self.guess_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.DISABLED)

    def reset_game(self):
        self.current_word_info = random.choice(WORDS_AND_HINTS)
        self.word_to_guess = self.current_word_info["word"]
        self.hint = self.current_word_info["hint"]
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.attempts_left = 6
        self.guessed_letters = set()

        self.word_label.config(text=" ".join(self.guessed_word))
        self.hint_label.config(text=f"Hint: {self.hint}")
        self.message_label.config(text="Guess a letter!")
        self.hangman_label.config(text=f"Attempts left: {self.attempts_left}")
        self.entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)


# Create the main window
root = tk.Tk()
game = HangmanGameWithHints(root)
root.mainloop()