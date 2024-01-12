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
        
    #creating a dictionary for the guess word (hard coded, will have to change)


    # Fix local variables, may have to not use function or figure a way around it

    #creating actions to be performed when the enter key is pressed
    def enter_action(s):
        iCount = 0
        guessDict = {}
        incrament = 0
        #concatenating the letters in the row
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

            for i in finalWord:
                i = i.upper()
                guessDict.update({iCount : i})
                iCount += 1
            print(guessDict)

            
            for i in secretDict:
                if secretDict[i] == guessDict[i]:
                    gw.set_square_color(incrament, i, CORRECT_COLOR)
                elif secretDict[i] in guessDict.values():
                    gw.set_square_color(incrament, i, PRESENT_COLOR)
                else:
                    gw.set_square_color(incrament, i, MISSING_COLOR)
                
        else:
            gw.show_message("Not in word list")

    #checking if the guess letters is in the secret word, one letter at a time
    # incrament = 0
    # for i in secretDict:
    #     if secretDict[i] == guessDict[i]:
    #         print(f'{i} , {incrament}')
    #     elif secretDict[i] in guessDict.values():
    #         print("in word")
    #     else:
    #         print("not in word")

    gw.add_enter_listener(enter_action)
    

wordle()
    
  

  

   