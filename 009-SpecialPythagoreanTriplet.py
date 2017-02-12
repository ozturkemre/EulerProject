def triplet():
    for i in range(1, 499):
        for j in range(i, 1000-i):
            rest = 1000 - i - j
            if i**2 + j**2 == rest**2:
                return i * j * rest

print(triplet())

