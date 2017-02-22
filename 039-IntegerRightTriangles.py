solmax = 3
rang = 1000

for p in range(rang // 4 * 2, rang + 1, 2):
    solutions = 0
    for a in range(2, int(p / 3.4142) + 1):
        if p * (p - 2 * a) % (2 * (p - a)) == 0:
            solutions += 1
            if solutions > solmax:
                solmax = solutions
                maxp = p

print(maxp)
