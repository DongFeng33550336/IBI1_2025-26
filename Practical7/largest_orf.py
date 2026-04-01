#Set the given mRNA sequence
#Find all positions of the start codon AUG
#For each AUG, read codons until a stop codon (UAA, UAG, UGA)
#Record the length of each ORF
#Keep the longest ORF and its length
#Print the longest ORF and length

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

max_length = 0
longest_orf = ''

for i in range(len(seq)):
    if seq[i:i+3] == start_codon:
        current_orf = ''
        for j in range(i, len(seq), 3):
            codon = seq[j:j+3]
            current_orf += codon
            if codon in stop_codons:
                break
        if len(current_orf) > max_length:
            max_length = len(current_orf)
            longest_orf = current_orf

print('Longest ORF:', longest_orf)
print('Length (nt):', max_length)