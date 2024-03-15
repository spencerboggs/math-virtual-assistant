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
fast_print(" Basic Series Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Automatically checks for")
fast_print(" convergence or divergence")
fast_print(" of the summation of any")
fast_print(" given series.")
print("")
input(" Press [Enter] to Start")
clear_screen()

""" while True:
    print("Enter the function in terms")
    function = input("of n: ")
    print("")

    # Define the function using lambda
    func = lambda n: eval(function)
 """
total = 0
for i in range(1, 1000000):
    # summation of 1/2n
    total += 1/(2*i)
print(total)

for i in range(1000000, 10000000):
    # summation of 1/2n
    total += 1/(2*i)
print(total)

for i in range(10000000, 100000000):
    # summation of 1/2n
    total += 1/(2*i)
print(total)

for i in range(100000000, 1000000000):
    # summation of 1/2n
    total += 1/(2*i)
print(total)