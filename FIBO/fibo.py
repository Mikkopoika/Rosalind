
n = 24

fibo = [1, 1]

for i in range (n-2):
    fibo.append(fibo[-2]+fibo[-1])

print(fibo)