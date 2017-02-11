def largestPalindromeProduct(digits):
    range1 = 10**digits - 1
    range2 = 10**(digits-1)-1
    for i in range(range1, range2, -1):
        number = str(i)+str(i)[::-1]
        for j in range(range1, range2, -1):
            for k in range(range1, range2, -1):
                if k*j == int(number):
                    return number

print(largestPalindromeProduct(3))

