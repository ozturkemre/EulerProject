def sumofPrimesBelowof(n):
    result = 5
    prime = [2, 3]
    number = prime[-1]
    while number < n:

        number = number + 2
        for i in prime:

            if number % i == 0:

                break
            elif i > (number**0.5):
                prime.append(number)
                result += number
                break

    return result

print(sumofPrimesBelowof(2000000))

