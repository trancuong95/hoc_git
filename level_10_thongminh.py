X = int(input('Nhập X: '))
Y = int(input('Nhập Y: '))

m = []
for t in range(0, X):
    m.append(0)

for j in range(0, X):
    m[j] = [i*j for i in range(0, Y)]

print(m)
