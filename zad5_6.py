l = []

for i in range(10):
    l.append(i)

print(l)

l2 = l.copy()
l3 = l.copy()
l4 = l.copy()
l5 = l.copy()
l6 = l.copy()

l2.append(0)
l2.pop(0)
print(l2)

l3.pop(9)
l3.insert(0,9)
print(l3)

l4.reverse()
print(l4)

for i in range(len(l5)):
    if i % 2 != 0:
        l5.remove(i)
print(l5)

l6copy = []

for i in range(len(l6)):
    if i % 2 == 0 and l6[i] % 2 != 0:
        l6copy.append(l6[i])
print(l6copy)