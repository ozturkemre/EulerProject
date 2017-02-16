def divisors(n):
    toplam = 0
    for j in range(1, int(n/2+1)):
        if n % j == 0:
            toplam += j
    return toplam
result = 0
for i in range(1, 10000):

    a = divisors(i) # i= 220            a = d(i) = d(220) = 284
    b = divisors(a) # b = d(a) = d(284) = 220
    if i == b:  
        if a != b:
            result = result + i
print(result)

