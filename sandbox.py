import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    #load graphical interface 
    gw = WordleGWindow()

    #initialize variables, the secret word, and the guess word
    secretDict = {}
    iCount = 0

    #selecting a secret word from five letter words and converting to uppercase
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

    #creating a dictionary for the secret word
    for i in secret_word:
        secretDict.update({iCount : i})
        iCount += 1
    print(secretDict)
        

    #creating actions to be performed when the enter key is pressed
    def enter_action(s):
        iCount = 0
        guessDict = {}
        incrament = 0
        numberOfGuesses = 6
        #concatenating the letters in the row into the guessed work
        finalWord = ""
        for col in range(N_COLS):
            letter = gw.get_square_letter(0, col)
            finalWord += letter
        #checking if the guess word is in the dictionary
        finalWord = finalWord.lower()
        print(finalWord)
    
        #checking if the guess word is in the dictionary
        if finalWord in FIVE_LETTER_WORDS:
            gw.show_message("Word found")

            # adding each letter to the guessed word dictionary
            for i in finalWord:
                i = i.upper()
                guessDict.update({iCount : i})
                iCount += 1
            print(guessDict)

            # color the letters based on if they're in the secret word or not 
            for i in secretDict:
                if secretDict[i] == guessDict[i]:
                    gw.set_square_color(incrament, i, CORRECT_COLOR)
                elif secretDict[i] in guessDict.values():
                    gw.set_square_color(incrament, i, PRESENT_COLOR)
                else:
                    gw.set_square_color(incrament, i, MISSING_COLOR)

            # check if the player has won or lost
            # might have to swith the order of the if statements
            if secretDict == guessDict:
                gw.show_message("You win!")
                gw.exit_on_click()
            elif numberOfGuesses == 0:
                gw.show_message("You lose!")
                gw.exit_on_click()
            else:
                gw.set_current_row(gw.get_current_row() + 1)
                numberOfGuesses -= 1



        # if the input word is in the word list:         
        else:
            gw.show_message("Not in word list")

    gw.add_enter_listener(enter_action)
    

wordle()
    
  

  

   