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
fast_print(" Compound Interest Calculator")
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
            P = input("Principal (P): ")
            if P == "" or P.lower() == "u":
                P = None
                break
            P = float(P)
        except ValueError:
            print("Invalid Input")
            continue
        if P is not None:
            break

    while True:
        try:
            r = input("Interest Rate (r): ")
            if r == "" or r.lower() == "u":
                r = None
                break
            r = float(r)
        except ValueError:
            print("Invalid Input")
            continue
        if r is not None:
            break

    while True:
        try:
            n = input("Number of Times Compounded (n): ")
            if n == "" or n.lower() == "u":
                n = None
                break
            n = float(n)
        except ValueError:
            print("Invalid Input")
            continue
        if n is not None:
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
            A = input("Final Value (A): ")
            if A == "" or A.lower() == "u":
                A = None
                break
            A = float(A)
        except ValueError:
            print("Invalid Input")
            continue
        if A is not None:
            break

    if P is None:
        if A is not None and r is not None and n is not None and t is not None:
            P = A / (1 + (r / n)) ** (n * t)
            print("Principal (P): " + str(P))
        else:
            print("Cannot Calculate")
    elif r is None:
        if P is not None and A is not None and n is not None and t is not None:
            r = n * (((A / P) ** (1 / (n * t))) - 1)
            print("Interest Rate (r): " + str(r))
        else:
            print("Cannot Calculate")
    elif n is None:
        if P is not None and A is not None and r is not None and t is not None:
            n = math.log(A / P) / (r * t)
            print("Number of Times Compounded (n): " + str(n))
        else:
            print("Cannot Calculate")
    elif t is None:
        if P is not None and A is not None and r is not None and n is not None:
            t = math.log(A / P) / (r * n)
            print("Time (t): " + str(t))
        else:
            print("Cannot Calculate")
    elif A is None:
        if P is not None and r is not None and n is not None and t is not None:
            A = P * (1 + (r / n)) ** (n * t)
            print("Final Value (A): " + str(A))
        else:
            print("Cannot Calculate")
    else:
        print("Cannot Calculate")

    print("")

    def calculate_t():
        while True:
            try:
                A = float(input("Final Value (A): "))
            except ValueError:
                print("Invalid Input")
                continue
            if A is not None:
                break
        t = math.log(A / P) / (r * n)
        print("Time (t): " + str(t))
        print("")

    def calculate_A():
        while True:
            try:
                t = float(input("Time (t): "))
            except ValueError:
                print("Invalid Input")
                continue
            if t is not None:
                break
        A = P * (1 + (r / n)) ** (n * t)
        print("Final Value (A): " + str(A))
        print("")

    while True:
        try:
            print("1. Calculate t given A")
            print("2. Calculate A given t")
            choice = int(input("Choice: "))
        except ValueError:
            print("Invalid Input")
            continue
        if choice is not None:
            break
        
    while True:
        if choice == 1:
            calculate_t()
        elif choice == 2:
            calculate_A()

        again = input("Calculate again? (Y/n): ")
        if (again.lower() == "n"):
            break
        else:
            while True:
                try:
                    print("1. Calculate t given A")
                    print("2. Calculate A given t")
                    choice = int(input("Choice: "))
                except ValueError:
                    print("Invalid Input")
                    continue
                if choice is not None:
                    break
                
    print("")

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break