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
fast_print(" Midpoint Rule Calculator")
fast_print(" v1.0.0")
print("")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    while True:
        try:
            n = int(input("Enter number of intervals: "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if n is not None and n % 2 == 0:
            break
        else:
            print("Invalid Input")
            print("Must be an even number\n")
            continue

    while True:
        try:
            a = float(input("Enter lower bound: "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if a is not None:
            break
        else:
            print("Invalid Input\n")
            continue

    while True:
        try:
            b = float(input("Enter upper bound: "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if b is not None:
            break
        else:
            print("Invalid Input\n")
            continue

    while True:
        try:
            function = input("Enter function: ")
        except ValueError:
            print("Invalid Input\n")
            continue
        if function is not None:
            break
        else:
            print("Invalid Input\n")
            continue

    h = (b - a) / n
    
    result = 0
    for i in range(n):
        result += eval(function.replace("x", str(a + (i + 0.5) * h)))

    result *= h

    print("Result: ", result)
    print("")

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break


