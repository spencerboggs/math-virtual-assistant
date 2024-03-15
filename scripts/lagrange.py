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
fast_print(" Lagrange Error Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" f^(n+1)(c) should be given in")
fast_print(" the question: something like")
fast_print(" |f^(n+1)(c)| <= M. Where M is")
fast_print(" the value of f^(n+1)(c).")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    pi = math.pi
    e = math.e
    sin = math.sin
    cos = math.cos
    tan = math.tan
        
    try:
        next_deriv = float(input("Value of f^(n+1)(c): "))
    except:
        print("Invalid Input\n")
        continue
    try:
        delta_x = float(input("Value of x-x0: "))
    except:
        print("Invalid Input\n")
        continue
    try:
        denominator = float(input("Value of (n+1): "))
    except:
        print("Invalid Input\n")
        continue
    numerator = abs(next_deriv * delta_x**int(denominator))
    denominator = math.factorial(int(denominator))
    error = abs(numerator/denominator)
    print("The error is: ", error)

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break