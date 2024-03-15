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
fast_print(" Basic Sequence Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Automatically checks for")
fast_print(" convergence or divergence")
fast_print(" as the limit approaches")
fast_print(" infinity. (NOT SUMMATION)")
print("")
input(" Press [Enter] to Start")
clear_screen()

def calculate_limit(func, n):
    try:
        a = func(1000000000)
        b = func(10000000000)
        c = func(100000000000)

        # Check if the limits are within 0.0001 of each other
        if abs(a - b) < 0.0001 and abs(b - c) < 0.0001:
            print("Appears to converge to", c)
            # Round to two decimal places
            rounded = round(c, 2)
            print("Approximately", rounded)
        else:
            print("Diverges")
    except:
        print("Invalid Input")

while True:
        
    print("Enter the function in terms")
    function = input("of n: ")

    if function == "":
        print("Invalid Input")
        print("")
        continue

    # Define the function using lambda
    def custom_eval(expression, n):
        expression = expression.replace('ln', 'log')
        return eval(expression, {'math': math, 'e': math.e,'sin': math.sin, 'cos': math.cos, 'tan': math.tan,'pi': math.pi, 'n': n, 'log': math.log})

    func = lambda x: custom_eval(function, x)

    # try to calculate it at infinity
    try:
        value = func(math.inf)
    except:
        value = None

    if str(value) != "nan" and value != None:
        print("Converges to", value)
    else:
        calculate_limit(func, math.inf)
    print("")

    cont = input("Continue? (y/n): ")
    if (cont == "n") or (cont == "N"):
        break
    print("")

    