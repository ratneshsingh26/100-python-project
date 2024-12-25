import random

word_list=["aardvark", "baboon", "camel"]

word_to_be_guessed=str(random.choice(word_list))
print(word_to_be_guessed)

guessed_letters = ["_"] *len(word_to_be_guessed)
print(" ".join(guessed_letters))

while "_" in guessed_letters:
    user_guess=input("Guess a letter: ").lower()
    if user_guess in word_to_be_guessed:
        for index, char in enumerate (word_to_be_guessed):
            if user_guess == char:
                guessed_letters[index]=char
    else:
        print("Wrong Guess \n")
    
    print(" ".join(guessed_letters))

print("Congratulations You've guessed the word\n")
