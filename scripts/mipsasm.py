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
fast_print(" MIPS ASM to Machine Code")
fast_print(" v1.0.0")
print("")
fast_print(" Instruction examples:")
fast_print(" add $rd, $rs, $rt")
fast_print(" sub $rd, $rs, $rt")
fast_print(" lw $rd, $rs, $rt")
fast_print(" sw $rd, $rs, $rt")
print("")
input(" Press [Enter] to Start")
clear_screen()


opcode_dict = {"add": "000000", "sub": "000000", "lw": "100011", "sw": "101011"}

def get_machine_code(instruction):
    opcode, rs, rt, rd = instruction.split()
    machine_code = opcode_dict[opcode] + "00000" + format(int(rs[1:]), '05b') + format(int(rt[1:]), '05b') + format(int(rd[1:]), '05b') + "00000100000"
    return machine_code

while True:
    instruction = input("Enter instruction: ")
    if instruction == "exit":
        break
    try:
        machine_code = get_machine_code(instruction)
        print("Machine code for instruction", instruction, "is:", machine_code)
    except:
        print("Invalid instruction")
        print("")
        continue
    print("")

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break
