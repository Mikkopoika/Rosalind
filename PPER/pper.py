from itertools import combinations_with_replacement, permutations, product

def permutaatiot(n:int, k:int):
    palautettava = 1
    moduloja = 0
    for i in range(n, n-k, -1):
        palautettava *= i
        if palautettava > 1000000:
            #print(f"kerroin {i}")
            #print(f"ennen moduloa {palautettava}")
            palautettava = palautettava % 1000000
            #print(f"modulon jälkeen {palautettava}")
            moduloja += 1
    #print (moduloja)
    return palautettava

n = 84
k = 10

print (permutaatiot(n, k))


#permutaatiot = int(kertoma(n)/kertoma(n-k))

#print(permutaatiot%1000000)