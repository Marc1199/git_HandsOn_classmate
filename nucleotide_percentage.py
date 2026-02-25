#!/usr/bin/env python

# Import necessary modules
import sys, re
from argparse import ArgumentParser

# Set up argument parser
parser = ArgumentParser(description='Compute nucleotide percentages in a DNA or RNA sequence')

# Add required sequence argument
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# If no arguments provided, print help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse arguments
args = parser.parse_args()

# Convert sequence to uppercase
args.seq = args.seq.upper()

# Validate the sequence
if not re.search('^[ACGTU]+$', args.seq):
    print('The sequence is not valid DNA nor RNA')
    sys.exit(1)

# Compute total length of the sequence
total = len(args.seq)

# Count and print percentage of Adenine (A)
count_A = args.seq.count('A')
print(f'A: {count_A}/{total} = {(count_A/total)*100:.2f}%')

# Count and print percentage of Cytosine (C)
count_C = args.seq.count('C')
print(f'C: {count_C}/{total} = {(count_C/total)*100:.2f}%')

# Count and print percentage of Guanine (G)
count_G = args.seq.count('G')
print(f'G: {count_G}/{total} = {(count_G/total)*100:.2f}%')

# Count and print percentage of Thymine (T)
count_T = args.seq.count('T')
print(f'T: {count_T}/{total} = {(count_T/total)*100:.2f}%')

# Count and print percentage of Uracil (U)
count_U = args.seq.count('U')
print(f'U: {count_U}/{total} = {(count_U/total)*100:.2f}%')

