n = int(input("Podaj ilość liczb:"))
l = []

for i in range(n):
    i = int(input("Podaj liczbe:"))
    l.append(i)

l.sort()

print(l)
print(l[0])
print(l[-1])