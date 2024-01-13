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


def decrement_counts(matching_counts, letter_count):
    for letter in matching_counts:
        letter_count[letter] -= 1


# Example usage:
secretWord = "vodka"
secretResult = count_letters(secretWord)
print(secretResult)

guessWord = "doors"
guessResult = count_letters(guessWord)
print(guessResult)

matching_letters = [key for key in guessResult if key in secretResult]

for key in matching_letters:
    print("Matching letter:", key)
    decrement_counts([key], secretResult)

print("Updated secret counts:", secretResult)
