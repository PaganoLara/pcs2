from collections import Counter
from functools import reduce
from operator import mul
amino_acids={	'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
				'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
				'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
				'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
				'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
				'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
				'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
				'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
				'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
				'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
				'UAA': 'stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
				'UAG': 'stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
				'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
				'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
				'UGA': 'stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
				'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'   }
pos = Counter(amino_acids.values())
f= open("rosalind_mrna.txt")
line = f.readline().strip()
x= reduce(mul, [pos[c] for c in line]) # multiplication of the frequency of the letters 
stop=  pos["stop"] #stop frequency
print((x * stop)% 10**6) #taking the remainder by the % operator

