from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear()

#red
r = [255,0,0]
#skin
s = [253, 186, 132]
#blue
b = [43, 36, 251]
#yellow
y = [255, 253, 56]
#white
w = [255,255,255]
#brown
br = [126,51,7]
#black
d = [0,0,0]


marioDown = [
d,d,r,r,r,r,d,d,
d,d,r,r,r,r,r,d,
d,d,s,s,br,s,d,d,
d,s,s,s,s,br,br,d,
d,d,s,s,s,s,d,d,
s,r,y,r,r,y,r,s,
d,d,b,b,b,b,d,d,
d,d,d,s,s,d,d,d
]

marioUp = [
d,d,r,r,r,r,r,d,
d,d,s,s,br,s,d,d,
d,s,s,s,s,br,br,d,
d,d,s,s,s,s,d,d,
s,r,y,r,r,y,r,s,
d,d,b,b,b,b,d,d,
d,d,d,s,s,d,d,d,
d,d,d,d,d,d,d,d
]

def down():
    sense.set_pixels(marioDown)
    sleep(1)
    
    
def up():
    sense.set_pixels(marioUp)
    sleep(0.3)
    sense.set_pixels(marioDown)
    
down()
    
sense.stick.direction_up = up
    