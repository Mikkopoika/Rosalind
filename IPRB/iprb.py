    from itertools import combinations, permutations 


k = 24
m = 24
n = 27

yhteensa = k + m +n

alkiot = []
for i in range(k):
    alkiot.append("K")
for i in range(m):
    alkiot.append("M")
for i in range(n):
    alkiot.append("N")
kombinaatiot = combinations(alkiot, 2)


kk = 0
mm = 0
mn = 0
nn = 0

for i in kombinaatiot:
    if "K" in i:
        kk += 1
    elif "M" in i and "N" not in i:
        mm += 1
    elif "M" in i:
        mn += 1
    else:
        nn += 1
kombinaatioita = kk + mm + nn + mn

p = 1 - ((nn/kombinaatioita)*1 + (mn/kombinaatioita)*(2/4) + (mm/kombinaatioita)*(1/4))

print (f"yhteensä {kombinaatioita}")
print (f"koota {kk}")
print (f"mm {mm}")
print (f"mn {mn}")
print (f"nn {nn}")
print (p)
