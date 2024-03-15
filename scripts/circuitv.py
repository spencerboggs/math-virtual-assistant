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
fast_print(" Circuit Voltage Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Circuit Voltage equation:")
fast_print(" V = IR")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    while True:
        print("What do you have?")
        print("1. V and R")
        print("2. I and R")
        try: choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (choice == 1 or choice == 2):
            break
        else:
            print("Invalid Input\n")
            print("")
    if (choice == 1):
        while True:
            try: v = float(input("Enter V: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            try: r = float(input("Enter R: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (v != None) and (r != None):
                print("I = ", v/r)
                print("")
                break
    elif (choice == 2):
        while True:
            try: v = float(input("Enter V: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            try: i = float(input("Enter I: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (v != None) and (i != None):
                print("R = ", v/i)
                print("")
                break

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break