#This code has the user think of a number and then guesses it
#
# Anders B

import random
import time
import math


# config
default_low = 1
default_high = 100




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
    
def show_credits(name):
    time.sleep(1)
    print()
    print("     Thank you for playing " + name + " ")
    time.sleep(.5)
    print ("Thank you for playing this gnarly game")
    time.sleep(.5)
    print ("      This game was produced by       ")
    time.sleep(.5)
    print ("   Dwight Schrute's Gym For Muscles   ")
    time.sleep(.5)
    print ("          and coded by Anders         ")
    time.sleep(10)
    quit()
def get_name():
    name = input("What's your name?")
    return name 
def find_limit(current_high, current_low):
    limit = math.ceil(math.log((current_high - current_low) + 1, 2))
    return limit
    
def get_guess(current_low, current_high):
   guess = ( current_high + current_low)//2
   return guess

def decide_number(name,default_low, default_high):
    print()
    decide_1 = input (name + ", would you like to pick numbers for your game?")
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
        print ("Okay, " + name + " default values will be used.")
        low = default_low
        high = default_high
        return low,high
    

    
def pick_number(name,current_low,current_high):
    print ()
    print (name + ", please think of a number between " + str(current_low) + " and " + str(current_high) + ".")
    time.sleep(.5)
    useless_1 = input("Press 'enter' when ready.")
    
def check_guess(name,guess,tries,limit):
    
    print()
    time.sleep(.5)
    print ("I have guessed " + str(tries) + "/" + str(limit) + " times")
    time.sleep(.5)
    print (str(guess) + "?")
    test = input(name + ", please tell me if my number is too high, too low, or if I guessed correct say yes ")
    test = test.lower()
    if test in ["low","l","too low","too low "]:
        return 1
    if test in ["high","h","too high","too high "]:
        return -1
        return check,tries
    if test in ["yes","y"]:
        return 0
    if test in ["stop","quit"]:
      return -99  
    print ("Please say something intelligent.")
     
def show_result(name,guess,tries,limit):
    print ()
    print ("Ahaha " + name + ",I knew it was " + str(guess) + " from the beginning.")
    print ()
    print ("I guessed your number in only " + str(tries) + "/" + str(limit) + " tries.")
    print ()
    print ("I always win! Haha!")

def play_again(name):
    while True:
        print()
        decision = input(name +", would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name):
    
    current_low,current_high = decide_number(name,default_low,default_high)
    check = -1
    tries = 0
    limit = find_limit(current_high, current_low)
    pick_number(name,current_low, current_high)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(name,guess,tries,limit)

        if check == -1:
            current_high = guess
        elif check == 1:
           current_low = guess
        tries +=1
           
        
    show_result(name,guess,tries,limit)


# Game starts running here
show_start_screen()
name = get_name()
playing = True

while playing:
    play(name)
    playing = play_again(name)

show_credits(name)
