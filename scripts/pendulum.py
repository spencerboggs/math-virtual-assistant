# Created by Spencer Boggs
import math
import time


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
print("")
print("")
fast_print(" Pendulum Period Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Remember to convert units to")
fast_print(" SI units (kg, m, s) before")
fast_print(" entering values.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: length = float(input("Enter length of pendulum (m): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: gravity = float(input("Enter gravity (m/s^2): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (length != None) and (gravity != None):
        print("Period: ", 2*math.pi*math.sqrt(length/gravity))
        print("")
        
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break
    