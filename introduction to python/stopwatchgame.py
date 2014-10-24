# http://www.codeskulptor.org/#user38_jC9obIrphEcReXo.py
#"Stopwatch: The Game"

#"Stopwatch: The Game"

import simplegui

# define global variables
time = 0
numright = 0
numtotal = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min=t/600
    sec=t%600
    ms=str(sec)[len(str(sec))-1]
    sec=str(sec)[0:len(str(sec))-1]
    min=str(min);sec=str(sec);ms=str(ms)
    while len(sec)!=2:
        sec= "0" + sec
    return min + ":" + sec + "." + ms   
    
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    pass
def Stop():
    global time,numright,numtotal
    if time %10==0 and timer.is_running():
        numright+=1
    if timer.is_running():
        numtotal+=1
    timer.stop()
    pass

def Reset():
    global time, numtotal,numright
    numtotal=0
    numright=0
    time =0
    timer.stop()
    pass
    

# define event handler for timer with 0.1 sec interval
def Tick():
    global time
    time += 1
    


# define draw handler
def Draw(canvas):
    canvas.draw_text(format(time),[80,100],24,"white")
    canvas.draw_text(str(numright) + "/" + str(numtotal),[170,20],15,"white")
    
# create frame
frame=simplegui.create_frame("Stopwatch!",200,200,100)

# register event handlers
timer= simplegui.create_timer(100,Tick)
frame.add_button("Start",Start)
frame.add_button("Stop",Stop)
frame.add_button("Reset",Reset)
frame.set_draw_handler(Draw)

# start frame

frame.start()

# Please remember to review the grading rubric
