teens_names = """zero one two three four five six seven eight nine ten
                eleven twelve thirteen fourteen fifteen sixteen seventeen
                eighteen nineteen""".split()
tens_names = """zero ten twenty thirty forty fifty sixty seventy eighty
                ninety""".split()


def toletter(n):
    if n >= 1000:
        thous = toletter(n // 1000) + "thousand"
        n %= 1000
        if n == 0:
            return thous
        elif n < 100:
            return thous + "and" + toletter(n)
        else:
            return thous + toletter(n)
    elif n >= 100:
        huns = teens_names[n // 100] + "hundred"
        n = n % 100
        if n == 0:
            return huns
        else:
            return huns + "and" + toletter(n)
    elif n >= 20:
        tens = tens_names[n // 10]
        n = n % 10
        if n == 0:
            return tens
        else:
            return tens + toletter(n)
    else:
        return teens_names[n]

length = 0

for i in range(1, 1001):
    length += len(toletter(i))

print(length)

