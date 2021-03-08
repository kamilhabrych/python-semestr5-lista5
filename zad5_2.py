l = []

for i in range(1,10+1):
    kwadrat = i * i
    l.append(kwadrat)
print(l)

for i in range(10):
    if  i % 2 == 0:
        l[i+1] = l[i+1] * (-1)

print(l)