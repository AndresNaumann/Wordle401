import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS
rowInit = 0

def wordle():
    secret_word = random.choice(FIVE_LETTER_WORDS)
    
    gw = WordleGWindow()
   

    # Function to display a word in the first row of the Wordle game window
    def display_word_in_first_row(word):
        for col in range(N_COLS):
            letter = word[col].upper()
            gw.set_square_letter(0, col, letter)

    # Display the secret word in the first row for testing purposes
    display_word_in_first_row(secret_word)

    def enter_action(s):
        finalWord = ""

    # Concatenate the letters in the row
        for col in range(N_COLS):
            letter = gw.get_square_letter(rowInit, col)
            secret_wordCap = secret_word.upper()
            if letter in secret_wordCap: 
                gw.set_square_color(rowInit, col, '#66bb66')
            finalWord += letter

        #check in terminal to make sure it's concatenating correctly
        print(finalWord)
        print(secret_word)

        # dictionary is in lowercase so you have to change back to lowercase before checking
        finalWord = finalWord.lower()
       
        # Check if the word is in the dictionary
        if finalWord in FIVE_LETTER_WORDS:
            gw.show_message("Word found")
            


            
            

       
            

        # Add any additional actions for an invalid word
        else:
            gw.show_message("Not in word list")


        

    # Add the enter listener to the window
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    wordle()


