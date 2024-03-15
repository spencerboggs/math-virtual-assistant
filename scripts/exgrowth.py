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
print("")
print("")
fast_print(" Exponential Growth / Decay")
fast_print(" v1.0.0")
print("")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    print("Enter all known variables")
    print("Leave unknown variables blank")
    print("")

    while True:
        try:
            y_0 = input("Initial Value (y_0): ")
            if y_0 == "" or y_0.lower() == "u":
                y_0 = None
                break
            y_0 = float(y_0)
        except ValueError:
            print("Invalid Input")
            continue
        if y_0 is not None:
            break
    
    while True:
        try:
            y = input("Final Value (y): ")
            if y == "" or y.lower() == "u":
                y = None
                break
            y = float(y)
        except ValueError:
            print("Invalid Input")
            continue
        if y is not None:
            break

    while True:
        try:
            t = input("Time (t): ")
            if t == "" or t.lower() == "u":
                t = None
                break
            t = float(t)
        except ValueError:
            print("Invalid Input")
            continue
        if t is not None:
            break

    while True:
        try:
            k = input("Growth Constant (k): ")
            if k == "" or k.lower() == "u":
                k = None
                break
            k = float(k)
        except ValueError:
            print("Invalid Input")
            continue
        if k is not None:
            break

    if y_0 is None:
        if y is not None and t is not None and k is not None:
            y_0 = y / math.exp(k * t)
            print("Initial Value (y_0): " + str(y_0))
        else:
            print("Cannot Calculate")
            print("")
            cont = input("Continue? (Y/n):")
            if (cont == "n" or cont == "N"):
                break
            else:
                continue
        
    if y is None:
        if y_0 is not None and t is not None and k is not None:
            y = y_0 * math.exp(k * t)
            print("Final Value (y): " + str(y))
        else:
            print("Cannot Calculate")
            print("")
            cont = input("Continue? (Y/n):")
            if (cont == "n" or cont == "N"):
                break
            else:
                continue

    if t is None:
        if y_0 is not None and y is not None and k is not None:
            t = math.log(y / y_0) / k
            print("Time (t): " + str(t))
        else:
            print("Cannot Calculate")
            print("")
            cont = input("Continue? (Y/n):")
            if (cont == "n" or cont == "N"):
                break
            else:
                continue

    if k is None:
        if y_0 is not None and y is not None and t is not None:
            k = math.log(y / y_0) / t
            print("Growth Constant (k): " + str(k))
        else:
            print("Cannot Calculate")
            print("")
            cont = input("Continue? (Y/n):")
            if (cont == "n" or cont == "N"):
                break
            else:
                continue

    print("")

    while True:
        try:
            print("1. Calculate y given t")
            print("2. Calculate t given y")
            choice = int(input("Choice: "))
        except ValueError:
            print("Invalid Input")
            continue
        if choice is not None:
            break
    
    def calculate_y():
        # Then we just need to calculate y given t
        while True:
            try:
                t = float(input("Time (t): "))
            except ValueError:
                print("Invalid Input")
                continue
            if t is not None:
                break
        y = y_0 * math.exp(k * t)
        print("Final Value (y): " + str(y))
        print("")
    def calculate_t():
        # Then we just need to calculate t given y
        while True:
            try:
                y = float(input("Final Value (y): "))
            except ValueError:
                print("Invalid Input")
                continue
            if y is not None:
                break
        t = math.log(y / y_0) / k
        print("Time (t): " + str(t))
        print("")


    while True:
        if choice == 1:
            calculate_y()
        elif choice == 2:
            calculate_t()

        again = input("Calculate again? (Y/n): ")
        if (again.lower() == "n"):
            break
        else:
            while True:
                try:
                    print("1. Calculate y given t")
                    print("2. Calculate t given y")
                    choice = int(input("Choice: "))
                except ValueError:
                    print("Invalid Input")
                    continue
                if choice is not None:
                    break

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break