import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def wordle():
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    gw = WordleGWindow()

    # Function to display a word in the first row of the Wordle game window
    def display_word_in_first_row(word):
        for col in range(N_COLS):
            letter = word[col]
            gw.set_square_letter(0, col, letter)

    # Display the secret word in the first row for testing purposes
    display_word_in_first_row(secret_word)

    # Placeholder for the enter action functionality
    def enter_action(s):
        # This will be replaced with actual code to process the entered word
        gw.show_message("You have to implement this method.")

    # Add the enter listener to the window
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()
