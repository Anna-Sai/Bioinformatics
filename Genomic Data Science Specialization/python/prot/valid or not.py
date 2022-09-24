#!/usr/bin/python
'''Suppose	we	are	only	interested	in	Hinding	if	a	protein
sequence	is	valid,	not	where	are	all	the	invalid	characters	in	the
sequence.'''

protein = input('Enter protein sequence:')

for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print('this is not a valid protein sequence!')
        break

