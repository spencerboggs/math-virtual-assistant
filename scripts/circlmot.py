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
fast_print(" Circular Motion Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Remember to convert units to")
fast_print(" SI units (kg, m, s) before")
fast_print(" entering values.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: radius = float(input("Enter radius of circle (m): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: speed = float(input("Enter speed of object (m/s): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (radius != None) and (speed != None):
        print("Cent. Acceleration: ", (speed**2)/radius)
    # Calculate the period
    if (radius != None) and (speed != None):
        print("Period: ", (2*math.pi*radius)/speed)
        print("")
        
    force = input("Get cent. force? (y/N): ")
    if (force == "y" or force == "Y"):
        try: mass = float(input("Enter mass of object (kg): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None):
            print("Cent. Force: ", mass*((speed**2)/radius))

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break