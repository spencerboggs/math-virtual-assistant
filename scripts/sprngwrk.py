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
fast_print(" Spring Work Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Calculate the work it takes")
fast_print(" to stretch a spring from its")
fast_print(" natural length")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try:
        print("Which is given?")
        print("1. Work and distance")
        print("   They will give you the work")
        print("   that it takes to stretch")
        print("   the spring to a distance")
        print("2. That and Force (Newtons)")
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if choice == 1 or choice == 2:
        try:
            work = float(input("Enter work (J): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        try:
            print("Enter distance (from the")
            distance = float(input("natural length): "))
        except ValueError:
            print("Invalid Input\n")
            continue

        k = work / (distance ** 2)

        if choice == 1:
            try:
                print("Enter new distance (from the")
                new_distance = float(input("natural length): "))
            except ValueError:
                print("Invalid Input\n")
                continue
            force = k * (new_distance ** 2)
            print("Force: ", force)
            # work
            print("Work: ", force * new_distance)
        elif choice == 2:
            try:
                force = float(input("Enter force (N): "))
            except ValueError:
                print("Invalid Input\n")
                continue
            distance = force / k
            print("Distance: ", distance)
    
    else:
        print("Invalid Input\n")
        continue

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break