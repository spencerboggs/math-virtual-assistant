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
fast_print(" Truth table Creator")
fast_print(" v1.0.0")
print("")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: 
        amount = int(input("Number of variables (max: 5): "))
    except:
        print("Invalid value")
        amount = 0

    if amount > 5:
        print("Max number of variables is 5")
        amount = 0

    variables = []
    for i in range(amount):
        variables.append(input("Enter variable " + str(i+1) + ": "))

    clear_screen()
    print("Variables: ", end=" ")
    for i in variables:
        print(i, end=" ")
    print("")

    operators = ["&", "|", "^", "~"]
    print("And: &, Or: |, Xor: ^, Not: ~")
    equation = input("Enter equation: ")

    clear_screen()
    equation = equation.replace(" ", "")

    valid = True
    for i in equation:
        if i not in variables and i not in operators and i != "(" and i != ")":
            valid = False
            break
    
    if valid:
        for i in variables:
            print(i, end=" ")
        print("| Eq.")

        for i in range(2**amount):
            temp = equation
            binary = bin(i)[2:]
            while len(binary) < amount:
                binary = "0" + binary
            
            binary = list(binary)

            print(" ".join(binary), end=" |  ")
            for j in range(len(variables)):
                temp = temp.replace(variables[j], binary[j])
            
            # Modify the line below to correctly handle the not operator
            result = eval(temp.replace('~', ' not ').replace('&', ' and ').replace('|', ' or ').replace('^', ' xor '))
            print(int(result))

    else:
        print("Invalid equation")

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break
    
    clear_screen()
