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
fast_print(" Impulse Calculator")
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
    try: time = float(input("Enter time (s): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (force != None) and (time != None):
        print("Impulse: ", force*time)
        print("")
        
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break