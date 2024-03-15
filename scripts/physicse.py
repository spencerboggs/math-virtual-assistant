# Created by Spencer Boggs
import math
import time

from ti_system import wait_key


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
fast_print(" Physics E&M. Reference Sheet")
fast_print(" v1.0.0")
print("")
fast_print(" Use the arrow keys to switch")
fast_print(" pages. Press [Clear] to exit")
print("")
input(" Press [Enter] to Start")
clear_screen()

def display_page(page):
    if (page == 0):
        print("Variables")
        print("==============================")
        print("A = area")
        print("B = magnetic field")
        print("C = capacitance")
        print("d = distance")
        print("E = electric field")
        print("epsilon = emf (electromotive F)")
        print("F = force")
        print("I = current")
    elif (page == 1):
        print("Variables Cont.")
        print("==============================")
        print("J = current density")
        print("L = inductance")
        print("l = length")
        print("n = number of loops of wire")
        print("  per unit length")
        print("N = number of charge carriers")
        print("  per unit volume")
        print("P = power")
    elif (page == 2):
        print("Variables Cont.")
        print("==============================")
        print("Q = charge")
        print("q = point charge")
        print("R = resistance")
        print("r = radius")
        print("t = time")
        print("U = potential/stored energy")
        print("V = electric potential")
        print("v = velocity")
    elif (page == 3):
        print("Variables Cont.")
        print("==============================")
        print("rho = resistivity")
        print("phi = magnetic flux")
        print("kappa = dielectric constant")
        print("")
        print("")
        print("")
        print("")
        print("")
    elif (page == 4):
        print("Equations")
        print("==============================")
        print("F(E) = 1/(4*pi*epsilon) * ")
        print("  (q1*q2)/r^2")
        print("E = F/q")
        print("(Circu.) E*dA = Q/epsilon")
        print("E = -dV/dx")
        print("deltaV = -integral(E*dr)")
        print("V = 1/(4*pi*epsilon) * ")
        print("  sum(qi/ri)")
    elif (page == 5):
        print("Equations Cont.")
        print("==============================")
        print("U(E) = qV = 1/(4*pi*epsilon) *")
        print("  (q1*q2)/r")
        print("deltaV = Q/C")
        print("C = kappa*epsilon*A/d")
        print("C(p) = sum(Ci)")
        print("1/C(s) = sum(1/Ci)")
        print("I = dQ/dt")
        print("U(C) = 1/2*Q*V = 1/2*C*V^2")
    elif (page == 6):
        print("Equations Cont.")
        print("==============================")
        print("R = rho*l/A")
        print("E = rho*J")
        print("I = Nev(d)A")
        print("I = deltaV/R")
        print("R(s) = sum(Ri)")
        print("1/R(p) = sum(1/Ri)")
        print("P = deltaV*I")
        print("F(M) = qvB")
    elif (page == 7):
        print("Equations Cont.")
        print("==============================")
        print("(Circular) B*dL = mu*I")
        print("dB = mu/(4*pi)*(I*dL x r)/r^2")
        print("F = integral(I*dL x B)")
        print("B(s) = mu*n*I")
        print("phi(B) = integral(B*dA)")
        print("epsilon = (circular) E*dL")
        print("epsilon = -d(phi(B))/dt")
        print("epsilon = -L*(dI/dt)")
    elif (page == 8):
        print("Equations Cont.")
        print("==============================")
        print("U(L) = 1/2*L*I^2")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
set_page = 0
display_page(set_page)  
while True:
    key = wait_key()
    if (key == 1) and (set_page != 8):
        set_page = set_page + 1
        clear_screen()
    elif (key == 2) and (set_page != 0):
        set_page = set_page - 1
        clear_screen()
    elif key == 9:
        break
    else:
        continue
    display_page(set_page)