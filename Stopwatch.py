# template for "Stopwatch: The Game"

import simplegui

# define global variables
success = 0
attempts = 0
counter = 0
initial_score = "0/0"
position_timer = [95, 120]
position_score = [250, 30]
is_timer_running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    """ time is is tenths of seconds
    A = mins
    B = tens of seconds
    C = seconds
    D = tenths of seconds
    """
    A = time // 600  # time/10 to have seconds, then /60 to have a minute "A"
    remainder = time % 600   # take remainder of the above divison
    whole_seconds = remainder // 10 # remainder/10 to have whole seconds "BC"
    B = whole_seconds // 10
    C = whole_seconds % 10
    D = remainder % 10 # to get the tenths of seconds "D"
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_timer_running
    timer.start()
    is_timer_running = True
    
def stop():
    global counter
    global success
    global attempts
    global is_timer_running
    global initial_score
    timer.stop()
    # The score values only changes if the timer is running:
    if is_timer_running == True:
       if counter % 10 == 0 and counter != 0:
            attempts += 1
            success += 1
       elif counter != 0:
            attempts += 1
    # The score values will not change if the timer stops running:
    is_timer_running = False
    initial_score = str(success) + "/" + str(attempts)
    
def reset():
    global success
    global attempts
    global counter
    global initial_score
    timer.stop()
    success = 0
    attempts = 0
    initial_score = str(success) + "/" + str(attempts)
    counter = 0
    format(counter)
   

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), position_timer, 50, "White")
    canvas.draw_text(initial_score, position_score, 30, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
start_button = frame.add_button("Start", start, 100)
stop_button = frame.add_button("Stop", stop, 100)
reset_button = frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
reset()
