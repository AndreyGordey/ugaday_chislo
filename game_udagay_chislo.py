import random

print("Welcome to Guess the Number game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 7 guesses to find the number.")

number = random.randint(1, 100)
guesses_left = 7

while guesses_left > 0:
    print("Guesses left:", guesses_left)
    guess = int(input("Enter your guess: "))
    guesses_left -= 1
    
    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

if guesses_left == 0:
    print("Sorry, you ran out of guesses. The number was", number)
# In this game, the program generates a random number between 1 and 100 and the player has to guess the number within 7 guesses. The program will give hints if the guess is too high or too low, and will end the game if the player runs out of guesses or correctly guesses the number.