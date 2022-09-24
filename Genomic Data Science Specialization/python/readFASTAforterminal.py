#!/usr/bin/python
"""	Build	a	dictionary	containing	all	sequences	from	a	FASTA(python3 readFASTAforterminal.py fasta.txt)"""
import sys
filename=sys.argv[1]

try:
    f = open(filename)
except IOError:
    print("File %s does not exist!!" % filename)


seqs = {}
for line in f:
    # let's discard the newline at the end (if any)
    line = line.rstrip()
    # distinguish header from sequence
    if line.startswith('>'):  # or line.startswith('>')
        words = line.split()
        name = words[0][1:]
        seqs[name] = ''
    else:  # sequence, not header
        seqs[name] = seqs[name]+line

print(seqs[name])
# with open("resFASTA.txt", "w") as f:
    f.write(seqs[name])