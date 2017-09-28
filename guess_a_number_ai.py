#This code has the user think of a number and then guesses it
#
# Anders B

import random
import time 

# config
low = 1
high = 100


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
    if "low" in test:
        check = 1
        return check
    if "high" in test:
        check = -1
        return check
    if "yes" in test:
        check = 0
        return check
    if "stop" in test:
        print()
        escape = input("Would you like to stop playing now? ")
        if "yes" in escape:
            quit()
        if "no" in escape:
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
    current_low = low
    current_high = high
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
