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
fast_print(" Bitwise Operations Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Example Inputs:")
fast_print(" a = 0b1010, b = 0b1100")
fast_print(" a = 10, b = 12")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: a = int(input("Enter a: "))
    except ValueError:
        print("Invalid Input\n")
        continue
    try: b = int(input("Enter b: "))
    except ValueError:
        print("Invalid Input\n")
        continue
    print("")
    print("AND: ", bin(a & b))
    print("OR: ", bin(a | b))
    print("XOR: ", bin(a ^ b))
    print("NOT a: ", bin(~a))
    print("NOT b: ", bin(~b))
    
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break
    