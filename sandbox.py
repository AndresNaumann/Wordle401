import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR


def wordle():
    # load graphical interface
    gw = WordleGWindow()

    # selecting a secret word from five letter words and converting to uppercase
    secretWord = random.choice(FIVE_LETTER_WORDS).upper()

    # # testing double letter guess DOORS
    # secretWord = "STEAL"

    #function to create a list of individual letter in a word
    def makeWordList(word):
        wordList = []
        wordList = list(word)
        return wordList

    testingList = makeWordList(secretWord)
    print(testingList)
    


    # creating actions to be performed when the enter key is pressed
    def enter_action(s):


        def makeWordList(word):
            word = word.upper()
            wordList = []
            wordList = list(word)
            return wordList
        
        changingList = makeWordList(secretWord)
        print(changingList)
    
        # initializing variables
        numberOfGuesses = 6
        fillerVar = '*'

        # concatenating the letters in the row into the guessed word
        guessWord = ""
        for col in range(N_COLS):
            letter = gw.get_square_letter(gw.get_current_row(), col)
            guessWord += letter
        # checking if the guess word is in the dictionary
        guessWord = guessWord.lower()
        print(guessWord)

        # checking if the guess word is in the dictionary
        if guessWord in FIVE_LETTER_WORDS:
            gw.show_message("Word found")

            #makes a list of letters in the guessed word
            guessList = makeWordList(guessWord)
            print(guessList)

            # color the letters based on if they're in the secret word or not
            for i in range(len(guessList)):
                if guessList[i] == testingList[i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    changingList[i] = fillerVar
                    print("correct")
                elif guessList[i] in changingList:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    
                    for e in range(len(testingList)):
                        if guessList[i] == changingList[e]:
                            changingList[e] = fillerVar
                            break
                    guessList[i] = fillerVar
                    
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                    print("missing")
            print(changingList)
            print(guessList)
            print(testingList)
         
            
            # check if the player has won or lost
            # might have to swith the order of the if statements
            if testingList == guessList:
                gw.show_message("You win!")

            elif numberOfGuesses == 0:
                gw.show_message("You lose!")

            else:
                gw.set_current_row(gw.get_current_row() + 1)
                numberOfGuesses = numberOfGuesses - 1
                print(numberOfGuesses)

        # if the input word is in the word list:
        else:
            gw.show_message("Not in word list")
            clear_current_row(gw)
            gw.set_current_row(gw.get_current_row())

        #reset the changing list between submissions
        changingList = makeWordList(secretWord)


    
    gw.add_enter_listener(enter_action)


def clear_current_row(gw):
    for col in range(N_COLS):
        gw.set_square_color(gw.get_current_row(), col, '')


wordle()

# to-do-list:
# stop game after win or loss
# only certian number of plays
# clear row on no word found

