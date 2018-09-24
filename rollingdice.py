from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

def rollDice():
    total = 0;
    for x in range(10):
        roll = random.randint(1, 6)
        print("roll "+ str(x+1) +": "+str(roll))
        total += roll
        if x == 9:
            print("your total is "+ str(total))
            total = 0
            
sense.stick.direction_up = rollDice
