#Ask the user to enter a stop codon (TAA / TAG / TGA)
#Read the yeast gene FASTA file
#Find the longest ORF ending with the chosen stop codon
#Count all codons before that stop codon
#Calculate codon frequencies
#Draw a pie chart and save it as an image file

import matplotlib.pyplot as plt
from collections import defaultdict

def read_fasta(path):
    seqs = {}
    name = None
    seq = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if name:
                    seqs[name] = ''.join(seq)
                name = line.split()[0][1:]
                seq = []
            else:
                seq.append(line)
        if name:
            seqs[name] = ''.join(seq)
    return seqs

def get_longest_orf_up_to_stop(seq, target_stop):
    best_codons = []
    starts = [i for i in range(len(seq)-2) if seq[i:i+3] == 'ATG']
    for s in starts:
        codons = []
        for i in range(s, len(seq)-2, 3):
            c = seq[i:i+3]
            if c == target_stop:
                if len(codons) > len(best_codons):
                    best_codons = codons
                break
            codons.append(c)
    return best_codons

# Main program
print("Please enter a stop codon (TAA / TAG / TGA):")
target = input().strip().upper()

if target not in ['TAA', 'TAG', 'TGA']:
    print("Invalid codon! Please enter TAA, TAG, or TGA.")
    exit()

seqs = read_fasta('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
count = defaultdict(int)

for seq in seqs.values():
    codons = get_longest_orf_up_to_stop(seq, target)
    for c in codons:
        count[c] += 1

total = sum(count.values())
print(f"Total codons counted upstream of {target}: {total}")

# Plot pie chart
plt.figure(figsize=(10, 10))
plt.pie(count.values(), labels=count.keys(), autopct='%.1f%%')
plt.title(f'Codon Frequency Upstream of {target}')
plt.savefig(f'codon_pie_{target}.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"Pie chart saved as: codon_pie_{target}.png")