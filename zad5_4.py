from math import sin

n = int(input("Podaj ilość elementów:"))
l = []

for i in range(n):
    l.append(sin(i))
    
l.sort()

print(l[0])
print(l[-1])