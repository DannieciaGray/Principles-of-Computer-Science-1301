"""
Program Description: This program takes a given DNA sequence translates it to a protein sequence.

Author:Danniecia Gray
"""

import helper

def transcription(dna_sequence):
    complement = {'A':'U','U':'A','C':'G','G':'C','T':'A'}
    mrna_sequence=""
    # Create the Base Pair Complement
    for i in dna_sequence:
        if i in complement:
            mrna_sequence+=complement[i]

    # Replace Thymine with Uracil
        mrna_sequence= mrna_sequence.replace("T","U")

    return mrna_sequence

def translate(mrna):
    protein = ''
    # Dictionary of Nucleotides to Amino Acids
    amino_acids = {
        'UUU': 'Phe',
        'UUC': 'Phe',

        'UUA': 'Leu',
        'UUG': 'Leu',
        'CUU': 'Leu',
        'CUC': 'Leu',
        'CUA': 'Leu',
        'CUG': 'Leu',

        'AUU': 'Ile',
        'AUC': 'Ile',
        'AUA': 'Ile',

        'AUG': 'Met',

        'GUU': 'Val',
        'GUC': 'Val',
        'GUA': 'Val',
        'GUG': 'Val',

        'UCU': 'Ser',
        'UCC': 'Ser',
        'UCA': 'Ser',
        'UCG': 'Ser',
        'AGU': 'Ser',
        'AGC': 'Ser',

        'CCU': 'Pro',
        'CCC': 'Pro',
        'CCA': 'Pro',
        'CCG': 'Pro',

        'ACU': 'Thr',
        'ACC': 'Thr',
        'ACA': 'Thr',
        'ACG': 'Thr',

        'GCU': 'Ala',
        'GCC': 'Ala',
        'GCA': 'Ala',
        'GCG': 'Ala',

        'UAU': 'Tyr',
        'UAC': 'Tyr',

        'UAA': 'STOP',
        'UAG': 'STOP',

        'CAU': 'His',
        'CAC': 'His',

        'CAA': 'Gln',
        'CAG': 'Gln',

        'AAU': 'Asn',
        'AAC': 'Asn',

        'AAA': 'Lys',
        'AAG': 'Lys',

        'GAU': 'Asp',
        'GAC': 'Asp',

        'GAA': 'Glu',
        'GAG': 'Glu',

        'UGU': 'Cys',
        'UGC': 'Cys',

        'UGA': 'STOP',

        'UGG': 'Trp',

        'CGU': 'Arg',
        'CGC': 'Arg',
        'CGA': 'Arg',
        'CGG': 'Arg',
        'AGA': 'Arg',
        'AGG': 'Arg',

        'GGU': 'Gly',
        'GGC': 'Gly',
        'GGA': 'Gly',
        'GGG': 'Gly',
    }

    # Split mrna into nucleotide triplets
    triplets=chunk(mrna,3)

    # Replace Triplets with Amino Acids
    for i in triplets:
        if i in amino_acids:
            amino_acid= amino_acids[i]
            
            protein+=amino_acid + " "
            
    return protein

# Splits a string into chunks of a specified size
# Takes a String, Returns a list of Strings
def chunk(string, chunk_size):
    chunk_list = []
    for i in range(0,len(string),chunk_size):
        chunk_list.append(string[i:i+chunk_size])

    return chunk_list
dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'
mrna=transcription(dna)
print(mrna)

protein=translate(mrna)
print(protein)
