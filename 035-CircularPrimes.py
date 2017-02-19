def is_prime(n):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True
cir_primes = []
status = False
for digit in range(2, 1000000):
    if is_prime(digit):
        num = str(digit)
        for i in range(len(num)):
            if is_prime(int(num[i:] + num[:i])):
                status = True
            else:
                status = False
                break
        if status:
            cir_primes.append(digit)

print(len(cir_primes))
