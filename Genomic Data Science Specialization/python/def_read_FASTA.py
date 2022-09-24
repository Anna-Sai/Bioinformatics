#!/usr/bin/python

def read_FASTA(inputFASTA):
    seqs = {}
    for line in f:
        # let's discard the newline at the end (if any)
        line = line.rstrip( )
        # distinguish header from sequence
        if line.startswith('>'):  # or line.startswith('>')
            words = line.split( )
            name = words[0][1:]
            seqs[name] = ''
        else:  # sequence, not header
            seqs[name] = seqs[name]+line
    return (seqs[name])


with open("fasta.txt","r") as f:
    inputFASTA=f
    outputFASTA = read_FASTA(inputFASTA)
# with open("resFASTA.txt", "w") as f:
#     f.write(outputFASTA)

print(outputFASTA)