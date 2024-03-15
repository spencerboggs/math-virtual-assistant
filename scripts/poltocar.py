import math
import sympy as sp

def polar_to_cartesian(r, theta):
    x = r * sp.cos(theta)
    y = r * sp.sin(theta)
    return x, y

# Take inputs
radius = float(input("Enter the radius: "))
angle_expr = input("Enter the angle in terms of pi (e.g., 5*pi/4): ")

# Parse the input expression
angle_symbolic = sp.sympify(angle_expr)
angle_radians = float(angle_symbolic.evalf())

cartesian_coordinates = polar_to_cartesian(radius, angle_radians)
print(f"Cartesian Coordinates: {cartesian_coordinates}")
