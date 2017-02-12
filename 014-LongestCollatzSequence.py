def get_length(n):
    value = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        value += 1
    return value

length = 0
number = 1
for i in range(1, 1000000):
    temp = get_length(i)
    if length < temp:
        number = i
        length = temp

print(number)

