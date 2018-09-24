from sense_hat import SenseHat
from time import sleep
import sys

sense = SenseHat()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

input_var = input("Speed loop?: ")
print("the speed of the loop is "+input_var+"secs")

while True:
    sense.show_letter("N", red)
    sleep(1)
    sense.show_letter("M", green)
    sleep(1)
    sense.show_letter("D", blue)
    sleep(int(input_var))




