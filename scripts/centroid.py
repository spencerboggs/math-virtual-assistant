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
fast_print(" Centroid / Moment Calculator")
fast_print(" v1.0.0")
print("")
fast_print(" You can either input points")
fast_print(" or input a lamina using the")
fast_print(" bounds (a, b) and functions")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    try:
        print("1. Points")
        print("2. Lamina")
        print("3. Area with density")
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid Input\n")
        continue
    if choice == 1:
        moment_y = 0
        moment_x = 0
        total_mass = 0
        while True:
            try:
                num_points = int(input("Enter number of points: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if num_points is not None:
                for i in range(num_points):
                    while True:
                        try:
                            x = float(input("Enter x value of point: "))
                        except ValueError:
                            print("Invalid Input\n")
                            continue
                        if x is not None:
                            break
                    while True:
                        try:
                            y = float(input("Enter y value of point: "))
                        except ValueError:
                            print("Invalid Input\n")
                            continue
                        if y is not None:
                            break
                    while True:
                        try:
                            mass = float(input("Enter mass of point: "))
                        except ValueError:
                            print("Invalid Input\n")
                            continue
                        if mass is not None:
                            break
                    moment_y += (mass * y)
                    moment_x += (mass * x)
                    total_mass += mass
                break

        centroid_y = moment_y / total_mass
        centroid_x = moment_x / total_mass

        print("Moment of y: ", moment_y)
        print("Moment of x: ", moment_x)
        print("Centroid: (", centroid_x, ", ", centroid_y, ")")

    elif choice == 2 or choice == 3:
        e = math.e
        pi = math.pi
        
        while True:
            try:
                a = eval(input("Enter a: "))
            except (ValueError, NameError, SyntaxError):
                print("Invalid Input\n")
                continue
            if a is not None:
                break
        while True:
            try:
                b = eval(input("Enter b: "))
            except (ValueError, NameError, SyntaxError):
                print("Invalid Input\n")
                continue
            if b is not None:
                break
        while True:
            fx = input("Enter f(x): ")
            if fx is not None:
                break
        while True:
            gx = input("Enter g(x): ")
            if gx is not None:
                break
        
        def f(x):
            return eval(fx, {'x': x, 'e': math.e, 'pi': math.pi, 'sin': math.sin, 'cos': math.cos})

        def g(x):
            return eval(gx, {'x': x, 'e': math.e, 'pi': math.pi, 'sin': math.sin, 'cos': math.cos})

        if a > b:
            a, b = b, a

        n = 10000
        delta_x = (b - a) / n

        area = 0
        while True:
            try:
                area = float(input("If area is known enter it: "))
            except ValueError:
                print("Invalid Input\n")
                continue
            if area is not None:
                break
            for i in range(n):
                x_i = a + i * delta_x
                area += math.fabs(delta_x * (f(x_i) - g(x_i)))

        moment_x = 0
        moment_y = 0
        if choice == 3:
            while True:
                try:
                    density = float(input("Enter density: "))
                except ValueError:
                    print("Invalid Input\n")
                    continue
                if density is not None:
                    break
            # calculate mass
            mass = density * area

            # calculate with density now
            # density/2 * integral from a to b of (f(x)^2 - g(x)^2) dx
            for i in range(n):
                x_i = a + i * delta_x
                moment_x += (1 / 2 * (f(x_i) ** 2 - g(x_i) ** 2) * delta_x)
            moment_x *= density
            centroid_x = moment_x / mass
            rounded_centroid_x = round(moment_x, 0) / round(mass, 0)

            for i in range(n):
                x_i = a + i * delta_x
                moment_y += (density * x_i * (f(x_i) - g(x_i)) * delta_x)
            centroid_y = moment_y / mass
            rounded_centroid_y = round(moment_y, 0) / round(mass, 0)
        
            print("Mass: ", mass)
        else:
            for i in range(n):
                x_i = a + i * delta_x
                moment_x += (x_i * (f(x_i) - g(x_i)) * delta_x)
            centroid_x = moment_x / area
            rounded_centroid_x = round(moment_x, 0) / round(area, 0)

            moment_y = 0
            for i in range(n):
                x_i = a + i * delta_x
                moment_y += (1 / 2 * (f(x_i) ** 2 - g(x_i) ** 2) * delta_x)
            centroid_y = moment_y / area
            rounded_centroid_y = round(moment_y, 0) / round(area, 0)

        print("Area: ", area)
        print("Moment of x: ", moment_x)
        print("Moment of y: ", moment_y)
        print("Centroid: (", centroid_x, ", ", centroid_y, ")")
        print("Rounded Centroid: (", rounded_centroid_x, ", ", rounded_centroid_y, ")")

    else:
        print("Invalid Input\n")
        continue

    print("")
    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break