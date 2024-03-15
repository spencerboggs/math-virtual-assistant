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
fast_print(" Euler's Method Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Use parenthesis for complex")
fast_print(" fractions and fractional")
fast_print(" expressions. Please convert")
fast_print(" cx to c*x when entering dy/dx")
fast_print(" Use ** for exponents (x**2)")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    print("")
    e = 2.7182818284
    y = input("Enter a y value: ")
    try: float(y)
    except ValueError: y = None
    if (y != None):
        y = float(y)
    x = input("Enter a x value: ")
    try: float(x)
    except ValueError: x = None
    if (x != None):
        x = float(x)
    stepCount = input("Number of steps: ")
    stepSize = input("Enter step size: ")
    derivative = input('Enter dy/dx: ')
    try: eval(derivative)
    except SyntaxError: derivative = None
    if (derivative != None):
        try: eval(derivative)
        except NameError: derivative = None
        if (derivative != None):
            if (str(y)) and (str(x)) and (stepCount) and (stepSize) and (derivative):
                x = float(x)
                y = float(y)
                print('')

                for i in range(int(stepCount)):
                    m = eval(derivative)
                    print("---- Step " + str(i+1) + " ----")
                    print("Slope: " + str(m))

                    print("y - " + str(y) + " = " + str(m) + "(x - " + str(x) + ")")
                    initialEquation = (str(m) + ' * x + ' + str(eval('(-x*m)+y')))

                    x = x+float(stepSize)
                    y = eval(str(initialEquation))

                    print('Tangent Line Equation ' + str(i + 1) + ': y = ' + str(initialEquation))
                    print("Y Coordinate after " + str(i+1) + " step(s): " + str(y))
                    print("Coordinates: (" + str(x) + ", " + str(y) + ")")
                    print('')
                    if (int(i+1) < int(stepCount)):
                        a = input("Press [Enter] to go to step " + str(i+2))
                    elif (int(i+1) == int(stepCount)):
                        a = input("Press [Enter] to proceed")
                    print('')        
            else:
                print('')
                print('Unsolvable. Double check')
                print('your inputs.')
        else:
            print('')
            print('Please enter a valid')
            print('equation. Enter any')
            print('multiplication with *')
            print('Ex: cx -> c*x')
            input("Press [Enter] to proceed")
    else:
        print('')
        print('Please enter a valid')
        print('equation. Enter any')
        print('multiplication with *')
        print('Ex: cx -> c*x')
        input("Press [Enter] to proceed")

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break