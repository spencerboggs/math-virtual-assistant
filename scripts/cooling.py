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
fast_print(" Newtons Law of Cooling")
fast_print(" v1.1.0")
print("")
print("")
input(" Press [Enter] to Start")
clear_screen()

while True:
    print("Enter all known variables")
    print("Leave unknown variables blank\n")

    T_0 = input("Initial Temp (T_0): ")
    T_0 = float(T_0) if T_0.strip() else None

    T_s = input("Surrounding Temp (T_s): ")
    T_s = float(T_s) if T_s.strip() else None

    T = input("Final Temp (T): ")
    T = float(T) if T.strip() else None

    t = input("Time (t): ")
    t = float(t) if t.strip() else None

    k = input("Growth Constant (k): ")
    k = float(k) if k.strip() else None

    T_t = T - T_0 if T is not None and T_0 is not None else None

    if T_0 is None and T is not None and t is not None and k is not None:
        T_0 = T / math.exp(k * t)
        print("Initial Temp (T_0): " + str(T_0) + "\n")

    if T_s is None and T is not None and T_0 is not None:
        T_s = T - ((T - T_0) / math.exp(k * t))
        print("Surrounding Temp (T_s): " + str(T_s) + "\n")

    if T is None and T_0 is not None and T_s is not None:
        T = T_s + ((T_0 - T_s) / math.exp(k * t))
        print("Final Temp (T): " + str(T) + "\n")

    if t is None and T_0 is not None and T is not None and k is not None:
        if T_0 == T_s:
            print("Cannot Calculate\n")
        else:
            t = math.log((T - T_s) / (T_0 - T_s)) / k
            print("Time (t): " + str(t) + "\n")

    if k is None and T_0 is not None and T is not None and t is not None and T_s is not None:
        if T_0 == T_s:
            print("Cannot Calculate\n")
        else:
            k = math.log((T - T_s) / (T_0 - T_s)) / t
            print("Growth Constant (k): " + str(k) + "\n")

    if T_t is None and T_0 is not None and k is not None and t is not None:
        T_t = T_0 * math.exp(k * t)
        print("T(t): " + str(T_t) + "\n")

    while True:
        print("1. Calculate T(t) given t")
        print("2. Calculate t given T(t)")
        print("3. Calculate T'(t) given t")
        choice = int(input("Choice: "))
        
        if choice == 1:
            t = input("Time (t): ")
            t = float(t) if t.strip() else None
            if t is not None:
                T_t = T_s + ((T_0 - T_s) * math.exp(k * t))
                print("T(t): " + str(T_t) + "\n")

        elif choice == 2:
            T_t = input("T(t): ")
            T_t = float(T_t) if T_t.strip() else None
            if T_t is not None and T_0 is not None and T_s is not None and k is not None:
                if T_0 == T_s:
                    print("Cannot Calculate\n")
                else:
                    t = math.log((T_t - T_s) / (T_0 - T_s)) / k
                    print("Time (t): " + str(t) + "\n")
            else:
                print("Cannot Calculate\n")

        elif choice == 3:
            t = input("Time (t): ")
            t = float(t) if t.strip() else None
            if t is not None and T_0 is not None and k is not None:
                t_prime = k * (T_0 - T_s) * math.exp(k * t)
                print("T'(t): " + str(t_prime) + "\n")
            else:
                print("Cannot Calculate\n")

        else:
            print("Invalid Choice")
            break

        again = input("Calculate again? (Y/n): ")
        if again.lower() == "n":
            break

    cont = input("Continue? (Y/n): ")
    if cont.lower() == "n":
        break
