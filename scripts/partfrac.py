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
fast_print(" Partial Fraction Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Put everything in terms of x")
fast_print(" Make sure to use * between")
fast_print(" any multiplication")
fast_print(" Ex. 2*x not 2x")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    while True:
        numerator = input("Numerator: ")
        denominator = input("Denominator: ")
        if numerator == "" or denominator == "":
            print("Invalid Input")
            continue
        else:
            break

    numerator_indices = []
    denominator_indices = []
    numerator = numerator.replace("^", "**")
    denominator = denominator.replace("^", "**")

    for i in range(len(numerator)):
        if numerator[i] == "x" and numerator[i+1] == "*" and numerator[i+2] == "*":
            for j in range(i+3, len(numerator)):
                if numerator[j] == "+" or numerator[j] == "-" or numerator[j] == "*" or numerator[j] == "/" or numerator[j] == " " or j + 1 == len(numerator):
                    if j + 1 == len(numerator):
                        j += 1
                    index = numerator[i+3:j]

                    if "(" in numerator[i+3:j]:
                        index = index.replace("(", "")
                    elif ")" in numerator[i+3:j]:
                        index = index.replace(")", "")
                    
                    numerator_indices.append(eval(index))
                    break

    print(numerator)

    for i in range(len(denominator)):
        if denominator[i] == "x" and denominator[i+1] == "*" and denominator[i+2] == "*":
            for j in range(i+3, len(denominator)):
                if denominator[j] == "+" or denominator[j] == "-" or denominator[j] == "*" or denominator[j] == "/" or denominator[j] == " " or j + 1 == len(denominator):
                    if j + 1 == len(denominator):
                        j += 1
                    index = denominator[i+3:j]

                    if "(" in denominator[i+3:j]:
                        index = index.replace("(", "")
                    elif ")" in denominator[i+3:j]:
                        index = index.replace(")", "")
                        
                    denominator_indices.append(eval(index))
                    break

    # sort the lists with largest values in front
    numerator_indices.sort(reverse=True)
    denominator_indices.sort(reverse=True)

    # check if the first valye of the numerator is less than the first value of the denominator

    print("Numerator Indices:", numerator_indices)
    print("Denominator Indices:", denominator_indices)

    if numerator_indices[0] >= denominator_indices[0]:
        print("Invalid Input")
        print("The order of the numerator has")
        print("to be less than the order of")
        print("the denominator")
        print("")
        continue

    print("Performing Partial Fraction Decomposition...")

    def find_roots():
        roots = []
        for i in range(-100000, 100000):
            x = i
            if eval(denominator) == 0:
                print("Root:", i)
                roots.append(i)
        return roots
    
    solutions = find_roots()

    # Now 'solutions' contains all the roots of the denominator
    print("Solutions of the denominator:", solutions)

    # now we can double check to see if the solutions multiply out to equal the original denominator input

    def construct_factored_polynomial(roots):
        # Initialize the factored polynomial
        factored_poly = ""
        
        for root in roots:
            if root < 0:
                factored_poly += "(x + " + str(abs(root)) + ")"
            else:
                factored_poly += "(x - " + str(root) + ")"
        
        return factored_poly
    

    factored_poly = construct_factored_polynomial(solutions)
    print("Factored Polynomial:", factored_poly)

    




