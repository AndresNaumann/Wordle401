def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count


def decrement_counts(matching_counts, letter_count):
    for letter in matching_counts:
        letter_count[letter] -= 1


# Example usage:
secretWord = "abide"
secretResult = count_letters(secretWord)
print("Secret counts:", secretResult)

guessWord = "speed"
guessResult = count_letters(guessWord)
print("Guess counts:", guessResult)

print()
print(secretWord)
print(guessWord)
print()

def makeWordList(word):
    wordList = []
    wordList = list(word)
    return wordList

secretList = makeWordList(secretWord)
guessList = makeWordList(guessWord)
changingList = makeWordList(secretWord)

for i in range(len(guessList)):
    if guessList[i] == secretList[i]:
        print("green")
        secretList[i] = "*"
        
    elif guessList[i] in secretList:
        print("yellow")
        
        for e in range(len(secretList)):
            if guessList[i] == secretList[e]:
                secretList[e] = "*"
                break
        guessList[i] = "*"
                
       
        
    else:
        print("grey")


print(secretList)
print(guessList)
print(changingList)











#create a list of matching letters, ie vodka and doors, it would create a list d and o 
# matching_letters = [key for key in guessResult if key in secretResult]
# print(matching_letters)

# for key in matching_letters:
#     decrement_counts([key], secretResult)

# print(secretResult)

# Check if each individual letter's count is 0 after subtraction
# for letter, count in secretResult.items():
#     if count == 0:
#         print(f"The count for letter {letter} is 0 after subtraction.")
#     else:
#         print(f"The count for letter {letter} is still greater than 0.")
