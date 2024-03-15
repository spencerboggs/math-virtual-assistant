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
fast_print(" Coulomb's Law Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Remember to convert units to")
fast_print(" SI units (kg, m, s) before")
fast_print(" entering values.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: charge1 = float(input("Enter charge 1 (C): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: charge2 = float(input("Enter charge 2 (C): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: distance = float(input("Enter distance (m): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: k = float(input("Enter k (N*m^2/C^2): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (charge1 != None) and (charge2 != None) and (distance != None) and (k != None):
        print("Force: ", (k*charge1*charge2)/(distance**2))
        print("")
        
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break