


t = 'ATGGTAGGTTCAGACAAGTGTAGGGGTTGCATTAAGGCATTACAGACTGCTGAGGGCCTCTATCACCGCAGAATGAGTACCTCCGGGATGGGACTAAGAGCAGACTGCTGTGGCTCGGTGTAAGATCTTCTTACAGGGACGCGTCTCGGTTAAGTACAGTCTTAGACAGACATCCAGTTGGCGCCGAACTCGCGAATTCTTAGTTCTTAGAGGGTTCCAAATGCCTTGGTACTATGTTCGTACTTATCAGCGTGCAATCCCATCAGTTAACTCCCAGATTACATAAGGTGTCATACAATGCACGTGGCCCGAGTGTGCAGGACAAGCGAGCTGAACAAGTCTCGATTATCGTGTTCGGGGCACCGCGGGCAGCTCGTCCGGCCCTCCATAGATTGGGGTCTAAGAATAGCATGCTGGGCCAGCACGTGGATGCAATGCCCATCATGACGATAAAACATAATCGCTCCCTCCAACGGCAGACGGTACTATTACCCAGGTCTACCCTGAACGAATCAGCACATTCTATTTGCCGTACGAAGCATGTGTTTGACCCGCAGCGTAAATTTCGATCGTCAGACCTTACCATACCTTACCCGTACACGTAGATTACATATCCAAGATTTGTCGCTTGCGGAGACTAGGCTCTTAAATCGCTACAGTCGTCCCCCAGATATTTTAACAGCGGCTACTGTCTTCCGAGGTATATGTAAATTCGGAGGGTAGTACCTGTAGCGCGCCTACGAGTGCCCTCCGGGAAAAGAGTTTCGCAAGCGCGGATTACGGCTGACCAGAGGGCGTAGTAGAGAAGAAAGGGGGCGTCGTCCACTATTTAACGCCTATTCTTGTAATTCGGGTCGATCACCGCTCTCGGTTGCGCCGCCGGAGGTCGGCATTCGATCGTGCGCGGATATGTTGCATGAGTAGATATCGCCCTACCGCTTGGGGTCTTCAAACACACGGGCGTTAG'

introns = ["TTAACTCCCAGATTACATAAGGTGTCATACAATGCACGTGGCC", "TTAACAGCGGCTACTGTCTTCCGAGGTATATGTAAATTCGGAGGGTAGTA", "AGAGCAGACTGCTGTGGCTCGGTGTAAGATCTTCT", "TATTCTTGTAATTCGGGTCGA", "CAAGATTTGTCGCTTGCGGAGACTAGG", "GCGAATTCTTAGTTCTTAGAGGGTTCC", "GTGTTTGACCCGCAGCGTAAATTTCGATCGTCAGACCTTACCATACCTT", "ACTGCTGAGGGCCTCTATCACCGCAGAATG", "TTGCATGAGTAGATATCGC", "AAAACATAATCGCTCCCTCCAACGGCAGACGGTACTATTACCCAGGTCT", "ATTACGGCTGACCAGAGGGCGTAGTAGAGAA", "CAGCTCGTCCGGCCCTCCATAGATTGGGGTCTAAGAATAGCAT"]

for intron in introns:
    t=t.replace(intron, '')

t = t.replace("T", "U")
palautettava = ""

codons = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': '\n',     'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': '\n',     'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': '\n',     'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}

while True:
    kodoni = t[0:3]
    #print(kodoni)
    palautettava += codons[kodoni]
    
    
    t= t[3:]
    if len(t)<3:
        break
print(palautettava)