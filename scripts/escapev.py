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
fast_print(" Escape Velocity Calculator")
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
    try: mass = float(input("Enter mass of object (kg): "))
    except ValueError: 
        print("Invalid Input\n")
        continue
    try: radius = float(input("Enter radius of object (m): "))
    except ValueError: 
        print("Invalid Input\n")
        continue

    if (mass != None) and (radius != None):
        print("Escape velocity: ", math.sqrt((2*G*mass)/radius))
        print("")

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break