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
fast_print(" CPI and MIPS Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" CPI and MIPS equations:")
fast_print(" CPI = execution time / cycles")
fast_print(" MIPS = instruction count /")
fast_print("        (execution time * 10^6)")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    # Get what they want to calculate
    while True:
        # clock rate, instruction count, execution time, or cpi and mips
        print("What do you want to calculate?")
        print("1. Clock Rate")
        print("2. Instruction Count")
        print("3. Execution Time")
        print("4. CPI and MIPS")
        try: choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (choice >= 1) and (choice <= 4):
            break
        else:
            print("Invalid Input\n")
            continue
    if (choice == 1):
        # Calculate clock rate
        while True:
            try: ic = float(input("Enter instruction count: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            try: et = float(input("Enter execution time: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (ic != None) and (et != None):
                print("Clock Rate: ", ic/et)
                print("")
    elif (choice == 2):
        # Calculate instruction count
        while True:
            try: cr = float(input("Enter clock rate: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            try: et = float(input("Enter execution time: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (cr != None) and (et != None):
                print("Instruction Count: ", cr*et)
                print("")
    elif (choice == 3):
        # Calculate execution time
        while True:
            try: cr = float(input("Enter clock rate: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            try: ic = float(input("Enter instruction count: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (cr != None) and (ic != None):
                print("Execution Time: ", ic/cr)
                print("")
    elif (choice == 4):
        # Calculate cpi and mips
        while True:
            try: cr = float(input("Enter clock rate: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            try: ic = float(input("Enter instruction count: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (cr != None) and (ic != None):
                print("CPI: ", ic/cr)
                print("MIPS: ", ic/(cr*1000000))
                print("")