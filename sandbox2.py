import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS

def wordle():
    gameLength = N_ROWS
    print(gameLength)
    gw = WordleGWindow()

    # Selecting a secret word from five letter words and converting to uppercase
    secretWord = "FALLS"

    # Function to create a list of individual letters in a word
    def makeWordList(word):
        return list(word)

    # Creating actions to be performed when the enter key is pressed
    def enter_action(s):
        changingList = makeWordList(secretWord)
        print(changingList)

        fillerVar = '*'

        # Concatenating the letters in the row into the guessed word
        guessWord = ""
        for col in range(N_COLS):
            letter = gw.get_square_letter(gw.get_current_row(), col)
            guessWord += letter
        guessWord = guessWord.lower()

        # Checking if the guess word is in the dictionary
        if guessWord in FIVE_LETTER_WORDS:
            gw.show_message("Word found")
            guessList = makeWordList(guessWord)
            modifiedSecretWord = makeWordList(secretWord)  # Copy of the secret word for modification

            # First pass: Mark correct positions
            for i in range(len(guessList)):
                if guessList[i].upper() == secretWord[i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    gw.set_key_color(guessList[i], CORRECT_COLOR)
                    modifiedSecretWord[i] = None  # Remove the correctly guessed letter

            # Second pass: Mark present and missing
            for i in range(len(guessList)):
                if guessList[i].upper() != secretWord[i]:  # Skip already correctly guessed
                    if guessList[i].upper() in modifiedSecretWord:
                        gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                        modifiedSecretWord[modifiedSecretWord.index(guessList[i].upper())] = None
                    else:
                        gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                        gw.set_key_color(guessList[i], MISSING_COLOR)

            # Check if the player has won or lost
            turnsleft = (N_ROWS - gw.get_current_row()) - 1
            print(turnsleft)

            if all(letter == None for letter in modifiedSecretWord):
                gw.show_message("You win!")
            elif turnsleft == 0:
                gw.show_message("You lose!")
            else:
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")
            clear_current_row(gw)
            gw.set_current_row(gw.get_current_row())

    gw.add_enter_listener(enter_action)

def clear_current_row(gw):
    for col in range(N_COLS):
        gw.set_square_color(gw.get_current_row(), col, '')

wordle()
