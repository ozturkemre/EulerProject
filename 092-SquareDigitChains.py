def calculate(n):
    while n != 89 and n != 1:
        temp = 0
        for i in str(n):
            temp += int(i)**2
        n = temp
    if n == 89:
        return True
    else:
        return False

count = 0
for num in range(1, 10000000):
    if calculate(num):
        count += 1
print(count)
