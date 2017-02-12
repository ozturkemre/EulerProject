liste = [1]
sayi = 1
while len(liste) <= 500:
    liste = []
    i = 1
    while i <= sayi/2:
        if sayi % i == 0:
            liste.append(i)
            print(len(liste))
        i += 1
    sayi += 1
print(liste[-1])

#need a more efficient algorithm
