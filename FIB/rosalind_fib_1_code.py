n =33
k = 3

kanit = [1,1]

i = 0 
while i < n-2:
    kanit.append(kanit[-2]*(k)+kanit[-1])
    i+=1

print(kanit)
print()
print(kanit[-1])