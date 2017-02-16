result = 0

for i in range(1, 1001):
    string = str((i**i))
    result += int(string[-10:])
print(str(result)[-10:])

