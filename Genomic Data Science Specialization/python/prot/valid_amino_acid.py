#!/usr/bin/python
'''Find	if	all	characters	in	a	given	protein	sequence	are
valid	amino	acids.'''

protein=input('Enter protein sequence:')
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print("protein contains invalid amino acid %s at position %d"%(protein[i],i))