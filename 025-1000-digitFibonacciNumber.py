f1 = 1
f2 = 1
i = 2
while len(str(f2)) < 1000:
    f1, f2, i = f2, f1 + f2, i + 1

print(i)

