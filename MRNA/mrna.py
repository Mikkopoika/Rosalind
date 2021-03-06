
s = "MEQKDQNLVMSRYLMIVTGGNYYRMGRKLAWWMILQQRDPEELWKQPWDGENKHFYAEAMAWMNTFLGRNQSFSRWPKQMRDCGRWELTDTKRHPDVRNRTPERHNYMYWKYKDRRLWHFTENIFPTRSHTKEDAVRRWASDWPPIAREEYFDQPEYQFGEWQIAQIRMFKSVEWTENWMPWIEQIQQTVDDWKAIMFCGDTESCMMDLHELWSFQVRGYGYHDATKFSRSNHSQNPLLHNYMRCVGCYAQWPDFMDLRPFQNEAQGWHYVQPVNNFPFEWTAMCAADCGEFFYQPMYPAPKREWIFRSPCQAIEFGISIKIMNCEQDDGENEYGAKKCVIMTGLYHTEWDVEYVYFIQGQCLSCRNGWECPEAVQHKNLDKRFVMDPLLGKYIFAPQMNIMTHPFIHLCLNGLKCPYLIGHYAVHETFDPYAHITWWGEKKAYWKAMVMGDCFPCKNGHDMYYNLVESMFIMQPHRLWGASWLVVNCSWLDMTGDHQQNCWIDIFKDIMIKRNRRYNMSIFDCAFCQRQMAVSVYAAQFCIELFLWGDYKHESLPVRNWQTRDSCVPFSYLETIDGRDARMVQHSCPPVWEHNVNWKSSNLAFHYVSAPAVNSTVWQEAQPRDSYWLVHQPTWEGYGISWIQSRMNLYQALPHVYFQTALQYLLRLPRLTQKLHKIMVERAGGNVFTGVFNMQYAPEAMVQKGNRFCSSWHSDLDNPQWYVKSRDTKVPRQLPHDAPFMQGEVMGLPAGIQMLICGAYWSRIRSWPLLCCDDERVRKGLAFVIQQEDYRKLIGLQCYLHYIMNNGPCYSMCRHVYMATRHLQPVCCKWHEYDGRGWLYGIHVFKTRYCIDHTIKQMTQHYTWHPMFLSWMFFSFPERSMQIQNFKMMQCGPRIVPVWFAEPCMLIPGENFRWTLTRKEYQKRVSCQRKLHGGILMLPSPMVNLPMWWYQVQSRWFAIPDQLIDPEYVWKKLYTHPYVDSWEVMQQSVLWIASHFPMGA"
#Initial sum is 3 as there are 3 stop-codons anyway
summa = 3
kodonit ={"F":2, "L":6, "I":3, "V":4, "M":1, "S":6, "P":4, "A":4, "T":4, "Y":2, "G":4, "H":2, "D":2, "N":2, "E":2, "K":2, "R":6, "Q":2, "C":2, "W":1}
print(sum(kodonit.values()))

for k in s:
    summa *= kodonit[k]

    if summa > 1000000:
        summa = summa % 1000000


print (summa)