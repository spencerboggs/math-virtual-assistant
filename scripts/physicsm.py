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
fast_print(" Physics Mec. Reference Sheet")
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
        print("a = acceleration")
        print("E = energy")
        print("F = force")
        print("f = frequency")
        print("h = height")
        print("I = rotational inertia")
        print("J = impulse")
        print("K = kinetic energy")
    elif (page == 1):
        print("Variables Cont.")
        print("==============================")
        print("k = spring constant")
        print("l = length")
        print("L = angular momentum")
        print("m = mass")
        print("P = power")
        print("p = momentum")
        print("r = radius")
        print("T = period")
    elif (page == 2):
        print("Variables Cont.")
        print("==============================")
        print("t = time")
        print("U = potential energy")
        print("v = velocity")
        print("W = work")
        print("x = position")
        print("mu = coeff. of friction")
        print("Theta = angle")
        print("tau = torque")
    elif (page == 3):
        print("Variables Cont.")
        print("==============================")
        print("omega = angular velocity")
        print("alpha = angular acceleration")
        print("phi = phase angle")
        print("rho = density")
        print("sigma = stress")
        print("epsilon = strain")
        print("gamma = shear strain")
    elif (page == 4):
        print("Equations")
        print("==============================")
        print("v = v0 + at")
        print("x = x0 + v0t + 1/2at^2")
        print("v^2 = v0^2 + 2a(x-x0)")
        print("a = F (net)/m")
        print("F = dp/dt")
        print("J = integral(Fdt) = deltaP")
        print("p = mv")
        print("|F (fric)| <= mu|F (normal)|")
    elif (page == 5):
        print("Equations Cont.")
        print("==============================")
        print("deltaE = W = integral(F * dr)")
        print("K = 1/2mv^2")
        print("P = dE/dt")
        print("P = F * v")
        print("U (gravity) = mgh")
        print("a (centripetal) = v^2/r")
        print("a (centripetal) = omega^2r")
        print("tau = r * F")
    elif (page == 6):
        print("Equations Cont.")
        print("==============================")
        print("alpha = tau (net)/I")
        print("I = integral(r^2dm)")
        print("I = sum(mr^2)")
        print("x (com) = sum(m0x0)/sum(m0)")
        print("v = r * omega")
        print("L = r x p = I * omega")
        print("K = 1/2I * omega^2")
        print("omega = omega0 + alpha * t")
    elif (page == 7):
        print("Equations Cont.")
        print("==============================")
        print("theta = theta0 + omega0t +")
        print("  1/2alpha * t^2")
        print("omega^2 = omega0^2 +")
        print("  2alpha(theta - theta0)")
        print("F (spring) = -kx")
        print("U (spring) = 1/2kx^2")
        print("x = x (max) * cos(omega * t +")
        print("  phi)")
    elif (page == 8):
        print("Equations Cont.")
        print("==============================")
        print("T = 2pi/omega = 1/f")
        print("T (spring) = 2pi * sqrt(m/k)")
        print("T (pendulum) = 2pi * sqrt(l/g)")
        print("|F (gravity)| = Gm1m2/r^2")
        print("U (gravity) = -Gm1m2/r")
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