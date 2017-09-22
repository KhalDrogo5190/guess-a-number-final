import random
import math
import time
# config
low = 1
high = 64
limit = math.ceil(math.log((high - low) + 1, 2))

# helper functions
def show_start_screen():
    print("***************************************")
    time.sleep(.25)
    print("***Dwight Schrute's Gym For Muscles****")
    time.sleep(.25)
    print("************** Presents ***************")
    time.sleep(.25)
    print("*********** Guess A Number ************")
    time.sleep(.25)
    print("***************************************")

def show_credits():
    print()
    time.sleep(.75)
    print("This awesome game was created by The Chow Mein Boyz.")
    
def get_guess():
    while True:
        time.sleep(.75)
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    time.sleep(.75)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    time.sleep(.75)
    print ("You have " + str(limit) + " tries.")
    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print()
        time.sleep(.75)
        print("You win!")
        time.sleep(.75)
        print()
    else:
        print()
        print("You are such a loser! The number was " + str(rand) + ".")
        print()
        
def play_again():
    while True:
        time.sleep(.75)
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            time.sleep(.75)
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


