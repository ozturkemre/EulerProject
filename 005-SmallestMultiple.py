def smallestMultiple():
    number = 2520
    while True:
        if isOK(number):
            return number
        else:
            number += 10

def isOK(n):
    for i in range(1, 21):
        if n %i != 0:
            return False
    return True

print(smallestMultiple())

