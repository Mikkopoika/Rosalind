from Bio.Seq import Seq

s = "TACGCTTTCCATGTCGACACTATACCTTTGCCGCGATGAAGGTGCAACCTCGTAAGTTGTCGTAGTACCCCCAAGTCTATTTTTACCCTTGCCGTACGCGGGTCCGATAAACAGCTTTCACTAGGCATCTCCACGTTGGTCAAGTTCTTACCAGGAGCACATCTGTCGGGGGCAGTGTGCGACGTCCGTGGGCATCATGTCAAAAAAACGTGGTCGGGCAATAGATTCTTAAACGGTGAACCTCACAAACCCACTGTGAGAAACAATGAAAATATTACTGCACACTAGTGTGATGTGTGTTGCAACAGGACCGCTCTACGACGCATTGGCTCTCAACGACCCCGCCATCGACATCGCGATAGTCGTAGACTACACGTTCGTATTACATCCGTTCGCGTTCCACTTACCCATTTGGACCGCAAACTTGGTAGCCTAGTTTATCAGACGAAGGAGGGTACCACGGTGACATATCCTGAACTATAATAATGGGGCGAGTGTAGAACCATATTTGACGGTGACTAATAGATAGAAACCCATCTCTAGAGGCGTCTTGAGTTTACGCGGGAGCAAAGTTGAGAATGCTTAGCTCCGAATCAACTATTATTTGGAGCTATATCTGATATGACGCGTCTCACTAAAACCCTTCATCGTGTACTCAAATGAAGTTTGCGGATGCGTATCTACATAAAGGCAACACCTGTGATGGTCTGTTAAATCGCATCATGTCGCACTGTTTAGGTGGCGTCCGTATTAAGGAGCAATGAACATGAGCCATCTTGGCCGGCCATTGATTATATACCGTTATACAATGGGCCCGCACGGACCAAACTGGCGAAGACGACTGCGTCTACTCCCCGGACCATCAAAACTTATTCCTAAGATGAAATAGACCCGGTCTTCGCCTGAGCATCACAGGAGACGTCGAGTGCGCGAGCTTTGCGTACACGTTCTCAAGGGAGTCCCCATCGACAG"

sekvenssi = Seq(s)


print(f"{sekvenssi.count('A')} {sekvenssi.count('C')} {sekvenssi.count('G')} {sekvenssi.count('T')}")

