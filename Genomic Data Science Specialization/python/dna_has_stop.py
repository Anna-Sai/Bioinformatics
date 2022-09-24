#!/usr/bin/python
# define has_stop_codon function here
dna = input("Enter a DNA sequence, please:")


def has_stop_codon(dna, frame=0):
    '''This function checks if given dnansequence has in frame stop codons.”'''
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found

if (has_stop_codon(dna)):
    print('Input sequence has an in frame stop codon.')
else:
    print('Input sequence has no in frame stop codons.')