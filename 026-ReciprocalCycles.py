def calculate(n):
    for t in range(1, n):
        if 1 == 10**t % n:
            return t + 1
    return 0
longest = 0
for i in range(2, 1000):
    longest = max(longest, calculate(i))
print(longest)

