import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_ROWS


def wordle():

    # generates the number of turns based on the number of rows
    gameLength = N_ROWS
    print(gameLength)

    # load graphical interface
    gw = WordleGWindow()

    # selecting a secret word from five letter words and converting to uppercase
    secretWord = random.choice(FIVE_LETTER_WORDS).upper()
    # secretWord = "FALLS"
    print(secretWord)

    # creating actions to be performed when the enter key is pressed
    def enter_action(s):

        #initialize variables
        fillerVar = '*'
        fillerVar2 = '#'

        # function to create a list of individual letter in a word
        def makeWordList(word):
            word = word.upper()
            wordList = []
            wordList = list(word)
            return wordList

        # unchanging secret word
        testingList = makeWordList(secretWord)
        # changing secret word
        changingList = makeWordList(secretWord)

        # concatenating the letters in the row into the guessed word
        guessWord = ""
        for col in range(N_COLS):
            letter = gw.get_square_letter(gw.get_current_row(), col)
            guessWord += letter
            # checking if the guess word is in the dictionary
        guessWord = guessWord.lower()
        # print(guessWord)

            # checking if the guess word is in the dictionary
        if guessWord in FIVE_LETTER_WORDS:
            gw.show_message("Word found")
            print(gw.get_current_row())

            # makes a list of letters in the guessed word

            # unchanging guess word
            testingGuessList = makeWordList(guessWord)
            # changing guess list
            changingGuessList = makeWordList(guessWord)

            # first pass GREEN
            # color the letters based on if they're in the secret word or not
            for i in range(len(testingGuessList)):
                if changingGuessList[i] == testingList[i]:
                    changingList[i] = fillerVar
                    changingGuessList[i] = fillerVar2
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    gw.set_key_color(testingGuessList[i], CORRECT_COLOR)
                print("green")
                print(changingList)
                print(changingGuessList)
                print(" ")
            
            # print(changingList)
            # print(changingGuessList)
            # print(" ")

            # second pass YELLOW
            for i in range(len(testingGuessList)):
                if changingGuessList[i] in changingList:
                    changingList[i] = fillerVar2
                    changingGuessList[i] = fillerVar
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    if gw.get_key_color(testingGuessList[i]) != CORRECT_COLOR:
                        gw.set_key_color(testingGuessList[i], PRESENT_COLOR)
                print("yellow")
                print(changingList)
                print(changingGuessList)
                print(" ")

            # print(changingList)
            # print(changingGuessList)
            # print(" ")
            
            # third pass GREY
            for i in range(len(testingGuessList)):
                if changingList[i] != fillerVar2 and changingList[i] != fillerVar:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                    if gw.get_key_color(testingGuessList[i]) != CORRECT_COLOR and gw.get_key_color(testingGuessList[i]) != PRESENT_COLOR:
                        gw.set_key_color(testingGuessList[i], MISSING_COLOR)
                print("grey")
                print(changingList)
                print(changingGuessList)
                print(" ")

            # print(changingList)
            # print(changingGuessList)
            # print(" ")
                    
            if testingList == testingGuessList:
                gw.show_message("You win!")
                return
                    
            #problems with keys changing color

                

        
            # check if the player has won or lost
            # might have to swith the order of the if statements
            turnsleft = (N_ROWS - gw.get_current_row()) - 1
            print(turnsleft)

            if testingList == testingGuessList:
                gw.show_message("You win!")
                
            
            elif turnsleft == 0:
                gw.show_message("You lose!")
                
            
            #this is the problem with the skipping rows 
            # else:
            #     gw.set_current_row(gw.get_current_row() + 1)

            
                

        # if the input word is in the word list:
        else:
            gw.show_message("Not in word list")
            clear_current_row(gw)
            gw.set_current_row(gw.get_current_row()-1)

       #reset the changing list between submissions
        changingList = makeWordList(secretWord)


    
    gw.add_enter_listener(enter_action)


def clear_current_row(gw):
    for col in range(N_COLS):
        gw.set_square_color(gw.get_current_row(), col, '')


wordle()


