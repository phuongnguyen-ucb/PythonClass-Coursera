# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import simplegui
import random

# initialize global variables used in your code
low_range = 0
high_range = 100
remain = math.ceil(math.log((high_range - low_range + 1), 2))
secret_number = random.randrange(0, 100)

# helper function to initial game
def init():
    global low_range
    global high_range
    global remain
    global secret_number
    if high_range == 100:
        remain = math.ceil(math.log((high_range - low_range + 1), 2))
        secret_number = random.randrange(0, 100)
        print "New game. Range is from 0 to", high_range
        print "Number of remaining guesses is", remain
        print ""
    else:
        remain = math.ceil(math.log((high_range - low_range + 1), 2))
        secret_number = random.randrange(0, 1000)
        print "New game. Range is from 0 to", high_range
        print "Number of remaining guesses is", remain
        print ""
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global high_range
    high_range = 100
    init()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global high_range
    high_range = 1000
    init()
    
def get_input(guess):
    # main game logic goes here
    global high_range
    global low_range
    global secret_number
    global remain
    guess_number = float(guess)
    remain -= 1
    print "Guess was", guess_number
    print "Number of remaining guesses is", remain
    
    if remain == 0:
        if secret_number == guess_number:
            print "Correct!"
            print ""
            init()
        else:
            print "You ran out of guesses. The number was", secret_number
            print ""
            init()
    else:
        if secret_number > guess_number:
            print "Higher!"
            print ""
        elif secret_number < guess_number:
            print "Lower!"
            print ""
        else:
            print "Correct!" 
            print ""
            init()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

init()   # to start the game

# start frame
frame.start()