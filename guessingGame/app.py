secret_word = "giraffe"
guess = ""
guessCount = 0
guessLimit = 5
outOfGuesses = False

while guess != secret_word and not(outOfGuesses): # while outOfGuesses is false AND secret word is not guessed correctly
    if guessCount < guessLimit:
        guess = input("Enter guess: ")
        guessCount += 1
    else:
        outOfGuesses = True

if outOfGuesses: # if outOfGuesses is true
    print("Out of guesses! You lose!")
else:
    print("You win!")
