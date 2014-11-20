# http://www.codeskulptor.org/#user38_ZCNxFdMNgtrLchB.py 
# implementation of card game - Memory
# implementation of card game - Memory

import simplegui
import random
state=0
cards= []
exposed=[False]*16
turns=0
tempone=100
temptwo=100

# helper function to initialize globals
def new_game():
    global cards,exposed
    while len(cards)!=16:
        x=random.randrange(0,8)
        if x not in cards:
            cards.append(x)
            cards.append(x)
    random.shuffle(cards)
    exposed=[False]*16
        

     
# define event handlers
def mouseclick(pos):
    global state,cards,exposed,turns,tempone,temptwo
    card_pos=int(pos[0]/50)
    if state==0:
        state=1
        exposed[card_pos]=True
        tempone=card_pos
    elif state==1:
        state+=1
        exposed[card_pos]=True
        temptwo=card_pos
    else:
        state=1
        if cards[tempone]!=cards[temptwo] and tempone!=temptwo:
            exposed[tempone]=False
            exposed[temptwo]=False
        temptwo=None
        exposed[card_pos]=True
        tempone=card_pos
        
        
    turns+=1
    
    

    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards,exposed
    for i in range(0,len(cards)):
        if exposed[i]==False:
            canvas.draw_polygon([[(i*50),0],[(i*50+50),0],[(i*50+50),100],[(i*50),100]],8,'White',"Green")
        else:
            canvas.draw_text(str(cards[i]),[i*50+20,50],22,"White")
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns: " + str(turns))
label.set_text("Turns: " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric