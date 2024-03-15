import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Get user input for parametric equations with sin, cos, tan, etc.
parametric_x_equation = input("Enter the x(t) equation: ")
parametric_y_equation = input("Enter the y(t) equation: ")

# Get user input for the range of t
t_start_input = input("Enter the start value for t (you can use '-pi' or 'pi'): ")
t_end_input = input("Enter the end value for t (you can use '-pi' or 'pi'): ")

# Replace '^' with '**', handle 'e' and 'pi', and add support for trigonometric functions
parametric_x_equation = parametric_x_equation.replace('^', '**').replace('e', 'exp(1)').replace('pi', 'sp.pi')
parametric_y_equation = parametric_y_equation.replace('^', '**').replace('e', 'exp(1)').replace('pi', 'sp.pi')

# Define symbols and create the parametric equations with trigonometric functions
t = sp.symbols('t')
x = sp.sympify(parametric_x_equation)
y = sp.sympify(parametric_y_equation)

# Add support for trigonometric functions
x = x.subs({'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan})
y = y.subs({'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan})

# Convert 'pi' and '-pi' to their numerical values
t_start = -sp.pi if t_start_input.lower() == '-pi' else sp.pi if t_start_input.lower() == 'pi' else float(t_start_input)
t_end = -sp.pi if t_end_input.lower() == '-pi' else sp.pi if t_end_input.lower() == 'pi' else float(t_end_input)

# Create lambdified functions for x and y
parametric_x = sp.lambdify(t, x, modules='numpy')
parametric_y = sp.lambdify(t, y, modules='numpy')

# Specify the range of values for t
t_values = np.arange(t_start, t_end, 0.01)

# Calculate x and y values for each t
x_values = parametric_x(t_values)
y_values = parametric_y(t_values)

# Create the parametric plot with arrows indicating the direction
plt.plot(x_values, y_values)
plt.quiver(x_values[:-1], y_values[:-1], x_values[1:]-x_values[:-1], y_values[1:]-y_values[:-1], scale_units='xy', angles='xy', scale=1, color='r', alpha=0.5)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Parametric Plot with Direction Arrows")

plt.grid(True)

# Display the plot
plt.show()
