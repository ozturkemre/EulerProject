def nth_prime_number(n):
    j = 2
    prime = [2, 3]
    sayi = prime[-1]
    while j < n:

        sayi = sayi + 2
        for i in prime:

            if sayi % i == 0:

                break
            elif i > (sayi**0.5):
                prime.append(sayi)
                j += 1
                break

    return prime[n-1]

print(nth_prime_number(10001))

