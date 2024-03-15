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
fast_print(" Torque Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Remember to convert units to")
fast_print(" SI units (kg, m, s) before")
fast_print(" entering values.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: force = float(input("Enter force (N): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: length = float(input("Enter length (m): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: angle = float(input("Enter angle (degrees): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (force != None) and (length != None) and (angle != None):
        print("Torque: ", force*length*math.sin(math.radians(angle)))
        print("")
        
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break