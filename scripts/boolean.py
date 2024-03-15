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
fast_print(" Boolean Equation Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Use these symbols:")
fast_print(" AND: &")
fast_print(" OR: |")
fast_print(" NOT: ~")
fast_print(" XOR: ^")
fast_print(" Ex: (A&B)|(~C)^(D&E)")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try: expression = input("Enter expression: ")
    except ValueError:
        print("Invalid Input\n")
        continue
    
    variables = []
    for char in expression:
        if char.isalpha():
            variables.append(char)
    variables = list(dict.fromkeys(variables))

    inputs = {}
    for var in variables:
        while True:
            try: 
                inputs[var] = input("Enter value for " + var + ": ")
                if (inputs[var].lower() == "true") or (inputs[var] == "1") or (inputs[var].lower() == "t"):
                    inputs[var] = True
                elif (inputs[var].lower() == "false") or (inputs[var] == "0") or (inputs[var].lower() == "f"):
                    inputs[var] = False
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input\n")
                continue
            break
    
    expression = expression.replace("&", " and ")
    expression = expression.replace("|", " or ")
    expression = expression.replace("~", " not ")
    expression = expression.replace("^", " ^ ")

    print("Inputs:")
    for var in variables:
        print(var + ": " + str(inputs[var]))
    print("")

    for var in variables:
        expression = expression.replace(var, str(inputs[var]))

    while True:
        end = expression.find(")")
        if end == -1:
            break

        start = expression.rfind("(", 0, end)
        expression = expression[:start] + str(eval(expression[start+1:end])) + expression[end+1:]
    
    try: print(eval(expression))
    except SyntaxError:
        print("Invalid Input\n")
        continue

    print("")

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break