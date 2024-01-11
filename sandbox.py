import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    secretDict = {}
    guessDict = {}

    iCount = 0
    secret_word = random.choice(FIVE_LETTER_WORDS).upper()

    for i in secret_word:
        secretDict.update({iCount : i})
        iCount += 1
        print(secretDict)
        
    guessDict = {0: 'C', 1: 'O', 2: 'A', 3: 'S', 4: 'T'}

    for i in secretDict:
        if secretDict[i] == guessDict[i]:
            print("True")
        else:
            print("False")
    

wordle()
    
  

  

   