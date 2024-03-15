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
fast_print(" Least Squares Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" Use this calculator to find")
fast_print(" the least squares regression")
fast_print(" line for a set of data.")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    while True:
        try: num_points = int(input("Number of data points: "))
        except ValueError:
            print("Invalid Input\n")
            continue
        if (num_points != None):
            break
        
    points = []
    for i in range(num_points):
        while True:
            # Format: x,y
            try: point = input("Point {} x,y: ".format(i + 1))
            except ValueError:
                print("Invalid Input\n")
                continue
            if (point != None):
                break
        points.append(point)
        
    x_values = []
    y_values = []
    for point in points:
        x_values.append(point.split(",")[0])
        y_values.append(point.split(",")[1])

    sum_x = 0
    for x in x_values:
        sum_x += float(x)
        
    sum_y = 0
    for y in y_values:
        sum_y += float(y)
        
    sum_x_squared = 0
    for x in x_values:
        sum_x_squared += float(x) ** 2
        
    sum_xy = 0
    for i in range(len(x_values)):
        sum_xy += float(x_values[i]) * float(y_values[i])
        
    slope = (num_points * sum_xy - sum_x * sum_y) / (num_points * sum_x_squared - sum_x ** 2)
    y_intercept = (sum_y - slope * sum_x) / num_points
    
    slope = round(slope, 8)
    y_intercept = round(y_intercept, 8)

    print("y = {}x + {}".format(slope, y_intercept))
    print("")

    cont = input("Continue? (y/n): ")
    if (cont == "n") or (cont == "N"):
        break
