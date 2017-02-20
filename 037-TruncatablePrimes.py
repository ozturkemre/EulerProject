def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True


def is_truncable_prime(n):
    if is_prime(n):
        num = str(n)
        for i in range(len(num)):
            if not is_prime(int(num[i:])):
                return False
            if not is_prime(int(num[:i+1])):
                return False
        return True
    else:
        return False
count = 0
number = 9
result = 0
while count < 11:
    number += 1
    if is_truncable_prime(number):
        result += number
        count += 1
print(result)
