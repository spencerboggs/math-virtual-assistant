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
fast_print(" Matrix Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Use this calculator to perform")
fast_print(" matrix operations.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    matrix1 = []
    matrix2 = []
    while True:
        print("1. Multiply")
        print("2. Add")
        print("3. Subtract")
        try: operation = int(input("Enter the operation (num): "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (operation != None):
            break

    while True:
        try: dim1_rows = input("Number of rows in matrix 1: ")
        except ValueError:
            print("Invalid Input\n")
            continue
        try: dim1_cols = input("Number of columns in matrix 1: ")
        except ValueError:
            print("Invalid Input\n")
            continue
        try: dim2_rows = input("Number of rows in matrix 2: ")
        except ValueError:
            print("Invalid Input\n")
            continue
        try: dim2_cols = input("Number of columns in matrix 2: ")
        except ValueError:
            print("Invalid Input\n")
            continue
        
        dim1 = "(" + dim1_rows + "," + dim1_cols + ")"
        dim2 = "(" + dim2_rows + "," + dim2_cols + ")"
        if (dim1 != None) and (dim2 != None):
            # Check if the values are in the correct format: (x,y)
            if (dim1[0] != "(") or (dim1[-1] != ")") or (dim2[0] != "(") or (dim2[-1] != ")"):
                print("Invalid Input\n")
                continue
            
            dim1 = dim1.replace("(", "")
            dim1 = dim1.replace(")", "")
            dim1 = dim1.split(",")
            dim2 = dim2.replace("(", "")
            dim2 = dim2.replace(")", "")
            dim2 = dim2.split(",")
            print(dim1, dim2)
            break
        
    while True:
        print("MATRIX 1")
        for i in range(int(dim1[0])):
            row = []
            for j in range(int(dim1[1])):
                try: value = int(input("Enter value [" + str(i) + "," + str(j) + "]: "))
                except ValueError:
                    print("Invalid Input\n")
                    continue
                if (value != None):
                    row.append(value)
            matrix1.append(row)
        print("")
        print("MATRIX 2")
        for i in range(int(dim2[0])):
            row = []
            for j in range(int(dim2[1])):
                try: value = int(input("Enter value [" + str(i) + "," + str(j) + "]: "))
                except ValueError:
                    print("Invalid Input\n")
                    continue
                if (value != None):
                    row.append(value)
            matrix2.append(row)
        break
    
    if (operation == 1):
        result = []
        for i in range(int(dim1[0])):
            row = []
            for j in range(int(dim2[1])):
                product = 0
                for k in range(int(dim1[1])):
                    product += matrix1[i][k] * matrix2[k][j]
                row.append(product)
            result.append(row)
        print("Result: ")
        for i in range(len(result)):
            print(result[i])
        print("")
    elif (operation == 2):
        result = []
        for i in range(int(dim1[0])):
            row = []
            for j in range(int(dim1[1])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        print("Result: ")
        for i in range(len(result)):
            print(result[i])
        print("")
    elif (operation == 3):
        result = []
        for i in range(int(dim1[0])):
            row = []
            for j in range(int(dim1[1])):
                row.append(matrix1[i][j] - matrix2[i][j])
            result.append(row)
        print("Result: ")
        for i in range(len(result)):
            print(result[i])
        print("")

    cont = input("Continue? (y/n): ")
    if (cont == "n") or (cont == "N"):
        break
