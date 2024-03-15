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
fast_print(" Projectile Motion Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Remember to convert units to")
fast_print(" SI units (kg, m, s) before")
fast_print(" entering values.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: velocity = float(input("Enter velocity of projectile (m/s): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: angle = float(input("Enter angle of launch (degrees): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: gravity = float(input("Enter gravity (m/s^2): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (velocity != None) and (angle != None) and (gravity != None):
        print("Horizontal Velocity: ", velocity*math.cos(math.radians(angle)))
        print("Vertical Velocity: ", velocity*math.sin(math.radians(angle)))
        print("Horizontal Distance: ", (velocity**2)*math.sin(2*math.radians(angle))/gravity)
        print("Vertical Distance: ", (velocity**2)*math.sin(math.radians(angle))**2/(2*gravity))
        print("Total Distance: ", (velocity**2)*math.sin(2*math.radians(angle))/gravity)
        print("")
        
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break