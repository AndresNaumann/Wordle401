import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS

def wordle():
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    gw = WordleGWindow()

    # # Function to display a word in the first row of the Wordle game window
    def display_word_in_first_row(word):
        for col in range(N_COLS):
            letter = word[col].upper()
            gw.set_square_letter(0, col, letter)

    # # Display the secret word in the first row for testing purposes
    display_word_in_first_row(secret_word)

   # Function to check if the entered word is in the word list
    def is_valid_word(word):
        return word in FIVE_LETTER_WORDS

    # Enter action functionality
    def enter_action(s):
        entered_word = s.upper()
        
        if is_valid_word(entered_word):
            gw.show_message("Correct! The word is in the word list.")
            # Add more positive messages or actions here
        else:
            gw.show_message("Not in word list")

    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()
