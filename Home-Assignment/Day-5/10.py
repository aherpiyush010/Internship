# 11.	Guess the Number Game
# •	Set a secret number (e.g., 7)
# •	Let the user guess until they get it right
# •	Print "Too high" or "Too low" for wrong guesses
# •	Print "Correct!" when guessed
# Part E: Guess the Number Game

secret_number = 10

while True:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break
