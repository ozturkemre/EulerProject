def evenFibonacciNumbers(n):
    fib = 1
    fib2 = 2
    temp = 0
    sum = 0

    while temp < n:

        temp = fib2

        if temp % 2 == 0:
            sum = sum + temp

        temp = fib + fib2
        fib = fib2
        fib2 = temp

    return sum

print(evenFibonacciNumbers(4000000))

