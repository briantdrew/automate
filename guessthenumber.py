# this is a guess the number game.
import random
print("Hello, what is your name?")
name = input()
secretNumber = random.randint(1,20)
print("Well, " + name + ", I'm thinking of a number between 1 and 20.")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print("Go ahead and take a guess.")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is too low, try again.")
    elif guess > secretNumber:
        print("Your guess is too high, give it another shot.")
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print("Awesome job, " + name + "! You guessed the number in " + str(guessesTaken) + " guesses!")
else:
    print("You blew it " + name + "! I was thinking of " + str(secretNumber))
    
        
