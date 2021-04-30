from itertools import combinations_with_replacement, permutations, product

n = 5
alkiot = []
for i in range(1, n+1):
    alkiot.append(i)

etumerkit = list(product([0,1], repeat = n))


permutaatiot = list(permutations(alkiot, n))

#koko = str(len(list(permutaatiot)))

vastaukset = []
    
for etumerkkirivi in etumerkit:   
    
    for rivi in permutaatiot:
        i=0    
        kirjoitettava = ""
        while i < len(rivi):
            if etumerkkirivi[i] == 0:
                kirjoitettava += (str(-rivi[i]) + " ")
            elif etumerkkirivi[i] == 1:
                kirjoitettava += (str(rivi[i]) + " ")
            i += 1
        vastaukset.append(kirjoitettava)

#print(vastaukset)


with open("tulos.txt", "w") as tiedosto:
    tiedosto.write(str(len(vastaukset)) + "\n")
    for rivi in vastaukset:
        
        tiedosto.write(rivi + "\n")
            