secretWord = "ABIDE"
guessWord = "SPEED"
print(secretWord)

def makeWordList(word):
        wordList = []
        wordList = list(word)
        return wordList


testingList = makeWordList(secretWord)
changingList = makeWordList(secretWord)
testingGuessList = makeWordList(guessWord)
changingGuessList = makeWordList(guessWord)

# unchanging secret word
print(testingList)
# changing secret word
print(changingList)
# unchanging guess word
print(testingGuessList)
# changing guess list
print(changingGuessList)


print(" ")
print(" ")
print(" ")

for i in range(len(testingGuessList)):
    if changingGuessList[i] == testingList[i]:
        changingList[i] = "*"
        changingGuessList[i] = "#"
        print("correct")

print(changingList)
print(changingGuessList)
print(" ")

for i in range(len(testingGuessList)):
    if changingGuessList[i] in changingList:
        changingList[i] = "#"
        print("inside")
print(changingList)
print(changingGuessList)

print(" ")
print(" ")
print(" ")

#resetting for the next guess
changingList = makeWordList(secretWord)
print(testingList)
# changing secret word
print(changingList)
# unchanging guess word
print(testingGuessList)
# changing guess list
print(changingGuessList)
