d = [1]*20
for i in range(20):
    for j in range(i):
        d[j] += d[j-1]
    d[i] = 2 * d[i-1]

print(d[19])

