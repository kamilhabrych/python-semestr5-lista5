l = [3,'alfa',2.71,'kot']

l[0] = 4
l[3] = 'pies'

print(l)

l2 = l

print()
print(l)
print(l2)

l2[0] = 98

print()
print(l)
print(l2)

l3=l.copy()

l3[0] = 24

print()
print(l)
print(l3)