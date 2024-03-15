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
fast_print(" Inertia Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Remember to convert units to")
fast_print(" SI units (kg, m, s) before")
fast_print(" entering values.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    print("1. Cylinder, Through Cicle")
    print("2. Cylinder, Through Side")
    print("3. Hoop, Through Center")
    print("4. Hoop, Through Side")
    print("5. Solid Sphere")
    print("6. Hollow Sphere")
    print("7. Rod, Through Center")
    print("8. Rod, Through end")
    print("")
    selection = input("Select a shape (num): ")
    try: int(selection)
    except ValueError: 
        print("Invalid Input\n")
        continue
    print("")
    try: mass = float(input("Enter mass (kg): "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if (int(selection) == 1):
        try: radius = float(input("Enter radius (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None) and (radius != None):
            print("I = 1/2(MR^2)")
            print("I = ", (mass*radius**2)/2)
            print("")
    elif (int(selection) == 2):
        try: radius = float(input("Enter radius (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        try: height = float(input("Enter height (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None) and (radius != None) and (height != None):
            print("I = 1/4(MR^2)+1/12(MH^2)")
            print("I = ", (mass*radius**2)/4 + (mass*height**2)/12)
            print("")
    elif (int(selection) == 3):
        try: radius = float(input("Enter radius (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None) and (radius != None):
            print("I = MR^2")
            print("I = ", (mass*radius**2))
            print("")
    elif (int(selection) == 4):
        try: radius = float(input("Enter radius (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None) and (radius != None):
            print("I = 1/2(MR^2)")
            print("I = ", (mass*radius**2)/2)
            print("")
    elif (int(selection) == 5):
        try: radius = float(input("Enter radius (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None) and (radius != None):
            print("I = 2/5(MR^2)")
            print("I = ", (2*mass*radius**2)/5)
            print("")
    elif (int(selection) == 6):
        try: radius = float(input("Enter radius (m): "))
        except ValueError: 
            print("Invalid Input\n")
            continue
        if (mass != None) and (radius != None):
            print("I = 2/3(MR^2)")
            print("I = ", (2*mass*radius**2)/3)
            print("")
    elif (int(selection) == 7):
        try: length = float(input("Enter length (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None) and (length != None):
            print("I = 1/12(ML^2)")
            print("I = ", (mass*length**2)/12)
            print("")
    elif (int(selection) == 8):
        try: length = float(input("Enter length (m): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (mass != None) and (length != None):
            print("I = 1/3(ML^2)")
            print("I = ", (mass*length**2)/3)
            print("")
    else:
        print("Invalid Input\n")
        continue
    
    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break