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
print("")
fast_print(" Combination Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Combination equation:")
fast_print(" n!/(r!(n-r)!)")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:

    try: n = float(input("Enter n: "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: r = float(input("Enter r: "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (n != None) and (r != None):
        print("Combinations: ", math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
        print("")

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break