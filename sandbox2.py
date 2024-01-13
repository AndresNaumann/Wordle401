# things to explore for double letter problem

# case statements

# step one count letters
# step two matching letters green and decrament counters
# step threee letters in word but not matching
# delete or do something with counted letters

def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    result = ""
    for letter, count in letter_count.items():
        result += f"{letter} {count} "

    return letter_count


# Example usage:
secretWord = "vodka"
secretResult = count_letters(secretWord)
print(secretResult)


guessWord = "doors"
guessResult = count_letters(guessWord)
print(guessResult)

for key in guessResult:
    if key in secretResult:
        print("yes")

    else:
        print("no")
