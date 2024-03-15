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
fast_print(" DNA/RNA to Amino Acid")
fast_print(" v1.0.0")
print("")
print("")
input(" Press [Enter] to Start")
clear_screen()

codons = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UGU': 'Cys', 'UGC': 'Cys',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}


while True:
    rna_dna = input("Enter the RNA/DNA sequence: ")
    rna_dna = rna_dna.upper()
    if 'T' in rna_dna and 'U' not in rna_dna:
        print("DNA detected")
        # change c to g, g to c, a to u, and t to a
        rna_dna = rna_dna.replace('C', 'g')
        rna_dna = rna_dna.replace('G', 'c')
        rna_dna = rna_dna.replace('A', 'u')
        rna_dna = rna_dna.replace('T', 'a')
        rna_dna = rna_dna.upper()
    elif 'U' in rna_dna and 'T' not in rna_dna:
        print("RNA detected")
        rna_dna = rna_dna.upper()
    else:
        print("Invalid Input\n")
        continue

    # if any letter not in the set, then it's invalid
    if not all(c in 'ACGU' for c in rna_dna):
        print("Invalid Input\n")
        continue
    

    # first locate the start codon
    start_codon = rna_dna.find('AUG')
    if start_codon == -1:
        print("No Start Codon Found\n")
        continue
    # then go in groups of 3 until a stop codon is found
    amino_acids = []
    for i in range(start_codon, len(rna_dna), 3):
        codon = rna_dna[i:i+3]
        if codons[codon] == 'Stop':
            break
        amino_acids.append(codons[codon])
    print(" - ".join(amino_acids))
    print()

    cont = input("Continue? (Y/n):")
    if (cont == "n" or cont == "N"):
        break
