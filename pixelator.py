from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

input_var = input("Speed?: ")

x = 0
y = 0
black = (0,0,0)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r,g,b)
    
    sense.set_pixel(x,y,randomColor)
    sleep(int(input_var))
    sense.set_pixel(x,y,black)
    x += 1
    if x > 7:
        x = 0
        y += 1
        if y > 7:
            y = 0
            
    