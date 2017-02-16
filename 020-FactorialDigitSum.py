def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def digit_sum(n):
    d_sum = 0
    for i in str(n):
        d_sum += int(i)
    return d_sum

result = digit_sum(factorial(100))

print(result)

