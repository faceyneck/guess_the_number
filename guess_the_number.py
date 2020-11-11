'''
This is a program that chooses a number between 1 and 20 with the "random" function call.
The player has 6 attempts to guess the correct number.
I usually like to place absurdly vulgar things into comments, but I'm fresh out of
inappropriate ideas, so just use your imagination and assume I said something about
sex, drugs and possibly rock-n-roll.
'''

from random import randint

# Generate the random number
random_number = randint(1, 20)

########################################################################################################################
########################################################################################################################
## Error checking functions
########################################################################################################################
########################################################################################################################
def try_again_asshole():
    try_again = print("Sorry, you're not using this program correctly. Try again, asshole...")



# def is_it_a_number(guess):
#     if guess.isdigit() == True:
#         guess = int(input())
#         return guess
#     elif guess.isalpha():
#         try_again_asshole()
#         guess = input()

########################################################################################################################
########################################################################################################################
## Main program thingies
########################################################################################################################
########################################################################################################################

# Begin the guessing counter at 0
guesses_taken = 0

print("Yo, playa! What\'s your name, you saucy upstart?")
player_name = input()

print("Well hey uh... don't freak out or anything, " + player_name + ", but I'm thinking of a number between 1 and 20.")
print("You have 6 chances to guess the correct number, or every single kitten on Earth will die of feline AIDS.")

for guesses_taken in range (6):
    print("Take a guess, kiddo! No pressure.")
    guess = input()
    if guess.isdigit() == True:
        guess = int(guess)

        if guess < random_number:
            print("Your guess is too low, " + player_name + " try again.")

        if guess > random_number:
            print("Whoa hey now!" + " Slow down, cowboy. Your guess is too high, try again.")

        if guess == random_number:
            break
    else:
        try_again_asshole()
if guess == random_number:        
    guesses_taken = str(guesses_taken + 1)    
    print("Well shucks, player! You done guessed the right number in " + guesses_taken + "! \n Great job, the kitties are a-okay")
if guess != random_number:
    random_number = str(random_number)
    print("I guess you don't like healthy kittens. The number I was thinking of was: " + random_number + ". \nPoor kitties!")