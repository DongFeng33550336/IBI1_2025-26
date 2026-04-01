#Read the FASTA file of yeast genes
#Find the start codon ATG
#Check in‑frame stop codons (TAA, TAG, TGA)
#Keep genes that have at least one stop codon
#Extract gene name and list stop codons
#Write the results into a new FASTA file

import re

def get_gene_name(header):
    match = re.search(r'gene:([a-zA-Z0-9]+)', header)
    if match:
        return match.group(1)
    return header.split()[0][1:]

def find_stops(seq):
    stops_present = set()
    for i in range(len(seq)):
        if seq[i:i+3] == 'ATG':
            for j in range(i, len(seq)-2, 3):
                c = seq[j:j+3]
                if c in ['TAA', 'TAG', 'TGA']:
                    stops_present.add(c)
                    break
    return sorted(list(stops_present))


input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'stop_genes.fa'

with open(input_file, 'r') as f:
    lines = f.readlines()

records = []
current_header = None
current_seq = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('>'):
        if current_header:
            records.append((current_header, ''.join(current_seq)))
        current_header = line
        current_seq = []
    else:
        current_seq.append(line)
if current_header:
    records.append((current_header, ''.join(current_seq)))

output = []
for header, seq in records:
    stops = find_stops(seq)
    if stops:
        gene = get_gene_name(header)
        new_header = f'>{gene} stops:{",".join(stops)}'
        output.append(new_header)
        output.append(seq)

with open(output_file, 'w') as f:
    f.write('\n'.join(output))

print('finished! File saved as stop_genes.fa')