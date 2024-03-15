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
fast_print(" Orbit Energy Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Remember to convert units to")
fast_print(" SI units (kg, m, s) before")
fast_print(" entering values.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    G = 6.67408 * 10**-11
    try: mass = float(input("Mass of first object (kg): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: mass2 = float(input("Mass of second object (kg): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: radius = float(input("Distance between objects (m): "))
    except ValueError:
        print("Invalid Input\n")
        continue

    if (mass != None) and (mass2 != None) and (radius != None):
        print("Mechanical Energy: ", (G*mass*mass2)/(radius**2))
        print("")

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break