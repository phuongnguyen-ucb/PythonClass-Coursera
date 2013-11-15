# implementation of card game - Memory

import simplegui
import random
numList = []
exposed = []
numTurns = 0
state = 0
cardOne	= None
cardTwo = None

# helper function to initialize globals
def init():
    global numList
    global exposed
    global state
    global numTurns
    
    numTurns = 0
    firstList = range(0,8)
    secondList = range(0,8)
    numList = firstList + secondList
    random.shuffle(numList)
    state = 0
    
    exposed = None
    exposed = []
    
    for number in numList:
        exposed.append(False)
        
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global cardOne
    global cardTwo
    global numTurns
    
    indexSelected = pos[0]//50
    if (not exposed[indexSelected]):
        exposed[indexSelected] = True
        if state == 0:
            state = 1
            cardOne = indexSelected
        elif state ==1:
            state =2
            numTurns += 1
            if (cardOne != None):
                cardTwo = indexSelected
            else:
                cardOne = indexSelected
        else:
            state = 1
            if (not numList[cardOne] == numList[cardTwo]):
                exposed[cardOne] = False
                exposed[cardTwo] = False
            
            cardOne = indexSelected
            cardTwo = None
               
                
        
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global numTurns
    i = 0
    for number in numList:
        if not exposed[i]:
            canvas.draw_polygon([(0+i*50,0),(0+i*50,100),(50+i*50,100),(50+i*50,0)],5,"White","Green")
        else:
            canvas.draw_text(str(number),[18+(50*i),60],40,"White")
        i+=1
    
    label.set_text("Moves = " + str(numTurns));
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")


# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
