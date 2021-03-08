l = []

for i in range(100,150+1):
    l.append(i)

del l[5:50:5]

print(l)