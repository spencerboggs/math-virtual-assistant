import sympy as sp

def nth_taylor_polynomial():
    # User inputs for the function, order, center, and variable
    expression_str = input("Enter the function in terms of 'x', using 'e' for Euler's number, 'pi' for pi, and trigonometric functions (e.g., sin, cos): ")
    order = int(input("Enter the order of the Taylor polynomial (n): "))
    center_value = float(input("Enter the center value: "))
    variable_name = input("Enter the variable name (e.g., 'x'): ")

    # Define the symbol and parse the expression
    x = sp.symbols(variable_name)
    expression = sp.sympify(expression_str)

    # Replace 'e' and 'pi' with their numerical values
    expression = expression.subs(sp.E, sp.exp(1))
    expression = expression.subs(sp.pi, sp.pi)

    # Calculate the nth Taylor polynomial directly without creating a polynomial
    taylor_polynomial = expression.series(x, center_value, order + 1).removeO()

    return taylor_polynomial

# Example usage:
result = nth_taylor_polynomial()
print(f"The Taylor polynomial is: {result}")
