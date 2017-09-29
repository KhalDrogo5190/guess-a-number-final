#This code has the user think of a number and then guesses it
#
# Anders B

import random
import time 

# config
default_low = 1
deafault_high = 100


# helper functions
def show_start_screen():
    print("***************************************")
    time.sleep(.25)
    print("***Dwight Schrute's Gym For Muscles****")
    time.sleep(.25)
    print("************** Presents ***************")
    time.sleep(.25)
    print("******** Guess A Number A.I. **********")
    time.sleep(.25)
    print("***************************************")
    time.sleep(1.25)
    
def show_credits():
    time.sleep(1)
    print()
    time.sleep(.5)
    print ("Thank you for playing this gnarly game")
    time.sleep(.5)
    print ("      This game was produced by       ")
    time.sleep(.5)
    print ("   Dwight Schrute's Gym For Muscles   ")
    time.sleep(.5)
    print ("          and coded by Anders         ")
    
    
def get_guess(current_low, current_high):
   guess = ( current_high + current_low)//2
   return guess

def decide_number():
    print()
    decide_1 = input ("Would you like to pick numbers for your game?")
    decide_1 = decide_1.lower()
    if decide_1 in ["yes","y"]:
        print()
        low = input ("What would you like your low value to be?")
        low = int(low)
        print()
        high = input ("What would you like your high value to be?")
        high = int(high)
        return low,high
    else:
        print ("Okay default values will be used.")
        low = default_low
        high = default_high

    
def pick_number():
    print ()
    print ("Please think of a number between " + str(low) + " and " + str(high) + ".")
    time.sleep(.5)
    useless_1 = input("Press 'enter' when ready.")
    
def check_guess(guess):
    print()
    time.sleep(.5)
    print (str(guess) + "?")
    test = input("Please tell me if my number is too high, too low, or if I guessed correct say yes ")
    test = test.lower()
    if test in ["low","l"]:
        check = 1
        return check
    if test in ["high","h"]:
        check = -1
        return check
    if test in ["yes","y"]:
        check = 0
        return check
    if test in ["stop","quit"]:
        print()
        escape = input("Would you like to stop playing now? ")
        escape = escape.lower()
        if escape in ["yes","y"]:
            quit()
        if escape in ["no","n"]:
            print ("Okay.")
        else:
            print ("The game will continue now")  
    else:
        print ("Please say something intelligent.")
     
def show_result(guess):
    print ()
    print ("I knew it was " + str(guess) + " from the beggining.")
    print ()
    print ("I always win! Haha!")

def play_again():
    while True:
        print()
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    
    current_low,current_high = decide_number()
    check = -1

    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_high = guess
        elif check == 1:
           current_low = guess 
           

    show_result(guess)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
