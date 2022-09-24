#! /usr/bin/python

# dna ='CGCTCTGTGGATATCATTCGACAAGTTTATCTACAGCTTGTACACAAAATATAGGGATGTGAATATGTGGCAAGCACCAGCAAGTTGTGTTTGTGGATAAG'
begin = input("Enter a DNA sequence, please:")
dna = begin.upper()
no_c = dna.count('C')
no_g = dna.count('G')
dna_length = len(dna)
gc_percent = (no_c+no_g) * 100 / dna_length
print('The DNA sequence’s GC content is ', round(gc_percent, 2), '%')
