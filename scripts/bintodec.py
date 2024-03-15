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
fast_print(" Binary / Decimal Conversion")
fast_print(" v1.0.0")
print("")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    binordec = input("Convert to Bin or Dec? (b/d): ")
    if (binordec == "b") or (binordec == "B"):
        while True:
            try: dec = int(input("Enter Decimal: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (dec != None):
                print("Binary: ", bin(dec)[2:])
                print("")
            cont = input("Continue? (Y/n):")
            if (cont == "n" or cont == "N"):
                break
    elif (binordec == "d") or (binordec == "D"):
        while True:
            try: bin = input("Enter Binary: ")
            except ValueError:
                print("Invalid Input\n")
                continue
            if (bin != None):
                print("Decimal: ", int(bin, 2))
                print("")
    else:
        print("Invalid Input\n")
        continue

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break

