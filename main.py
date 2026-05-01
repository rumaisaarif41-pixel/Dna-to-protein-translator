dna='ATGGCCATTGTAATGGGCCGGCCTAAAGGGTGGGCCCGATAG'
rna=dna.replace('T','U')
codon_table={
    'AUG':'MET',
    'GCC':'Ala',
    'AUU':'Ile',
    'GUA':'Val',
    'AUG':'Met',
    'GGC':'Gly',
    'CGG':'Arg',
    'CCU':'Pro',
    'AAA':'Lys',
    'GGG':'Gly',
    'UGG':'Trp',
    'GCC':'Ala',
    'CGA':'Arg',
    'UAG':'Stop',

}
i=0
protein_chain=[]
for i in range(0,len(rna),3):
    codon=rna[i:i+3]
    if codon in codon_table:
        amino_acid=codon_table[codon]
    if amino_acid=='Stop':
        break
    protein_chain.append(amino_acid)
print(protein_chain)
protein_string='-'.join(protein_chain)
print(f'Final protein Sequence:{protein_string}')