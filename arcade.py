from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

x = 0
y = 0

c = (255,255,255)

while True:
    on_off = random.randint(0,1)
    if on_off < 1:
        sense.set_pixel(x,y,c)
        sense.set_pixel(7-x,y,c)
    x += 1
    if x > 3:
        x = 0
        y += 1
        if y > 7:
            y = 0
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            c = (r,g,b)
            sleep(1)
            sense.clear()
            