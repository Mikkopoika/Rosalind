from itertools import permutations 

n = 7
alkiot = []
for i in range(1, n+1):
    alkiot.append(i)


permutaatiot = permutations(alkiot)
with open("tulos.txt", "w") as tiedosto:
    i=0
    for rivi in permutaatiot:
        for luku in rivi:
            tiedosto.write(str(luku) + " ")
        i+=1
        tiedosto.write("\n")
    print (i)