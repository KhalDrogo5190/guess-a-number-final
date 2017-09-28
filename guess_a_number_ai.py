import random
# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
   guess = ( current_high + current_low)//2
   return guess

def pick_number():
    print ("Please think of a number between " + str(low) + " and " + str(high) + ".")
    useless_1 = input("Press 'enter' when ready.")
def check_guess(guess):
    print (guess)
    test = input("Please tell me if my number is too high, too low, or if I guessed right ")
    if "low" in test:
       check = 1
       return check
    if "high" in test:
        check = -1
        return check
    if "right" in test:
       check = 0
       return check
    else:
        print ("Please say something intelligent.")
     
def show_result(guess):
    print()
    print ("I knew it was " + str(guess) + " from the beggining.")
    print()
    print ("I always win! Haha!")

def play_again():
    while True:
        print()
        decision = input("Would you like to play again? (y/n) ")

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
