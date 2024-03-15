# Created by Spencer Boggs
import math
import time

from ti_plotlib import *
from ti_system import *


def wait(seconds):
    time.sleep(seconds)

def fast_print(string):
    for char in string:
        print(char, end="", flush=True)
        wait(0.02)
    print()

def clear_screen():
    print("\033[2J", end="", flush=True)

clear_screen()
print("")
fast_print(" Slope Field Generator")
fast_print(" v1.0.0")
print("")
fast_print(" Use parenthesis for complex")
fast_print(" fractions and fractional")
fast_print(" expressions. Please convert")
fast_print(" cx to c*x when entering dy/dx")
fast_print(" Use ** for exponents (x**2)")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    def f(x, y, dydx):
        return dydx(x, y)

    cls()
    print("")
    custom_window = input("Custom Window? (y/N): ")
    if custom_window.lower() == "y":
        custom_window = True
    else:
        custom_window = False

    if custom_window:
        xmin = None
        while (xmin == None):
            try:
                xmin = int(input("Minimum x value: "))
            except:
                print("Invalid Input. Try Again")
                print("Remember to use whole numbers")
                xmin = None
        xmax = None
        while (xmax == None):
            try:
                xmax = int(input("Maximum x value: "))
            except:
                print("Invalid Input. Try Again")
                print("Remember to use whole numbers")
                xmax = None
        ymin = None
        while (ymin == None):
            try:
                ymin = int(input("Minimum y value: "))
            except:
                print("Invalid Input. Try Again")
                print("Remember to use whole numbers")
                ymin = None
        ymax = None
        while (ymax == None):
            try:
                ymax = int(input("Maximum y value: "))
            except:
                print("Invalid Input. Try Again")
                print("Remember to use whole numbers")
                ymax = None
    else:
        xmin = -10
        xmax = 10
        ymin = -10
        ymax = 10

    print()

    dydx_str = None
    while (dydx_str == None):
        try:
            dydx_str = input("dy/dx (in terms of x and y): ")
            dydx = lambda x, y: eval(dydx_str)
        except:
            print("Invalid Input. Try Again")
            dydx_str = None

    cls()
    print(dydx_str)

    dx = 1
    dy = 1

    window(xmin, xmax, ymin, ymax)
    grid(1, 1)
    axes()

    for x in range(xmin, xmax+dx, dx):
        for y in range(ymin, ymax+dy, dy):
            slope = f(x, y, dydx)
            x1 = x + dx/2*math.cos(math.atan(slope))
            y1 = y + dy/2*math.sin(math.atan(slope))
            x2 = x - dx/2*math.cos(math.atan(slope))
            y2 = y - dy/2*math.sin(math.atan(slope))
            line(x1, y1, x2, y2)

    input()
    cls()

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break