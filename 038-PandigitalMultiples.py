def is_pandigital(a):
    num = []
    for i in str(a):
        num.append(int(i))
    for i in range(1, len(num)+1):
        if num.count(i) == 0:
            return False
    return True

result = 918273645
for n in range(9000, 10000):
    number = ''
    q = 1
    while len(number) < 9:
        number += ''.join(str(n * q))
        q += 1
    if is_pandigital(int(number)) and len(number) == 9:
        result = max(result, int(number))
print(result)
