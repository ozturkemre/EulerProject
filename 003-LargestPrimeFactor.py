def nth_prime_number(n):
    prime = [2, 3]
    root = n**0.5
    last = prime[-1]+2
    while last <= root:
        for i in prime:

            if last % i == 0:
                break
            elif i > (last**0.5):
                prime.append(last)
                break
        last += 2
    while n > 1:
        for i in prime:
            while n % i == 0:
                n = n/i
                a = i
    return a

print(nth_prime_number(600851475143))

