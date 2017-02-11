def sumofSquares(n):
    return n*(n+1)*(2*n+1)/6

def squaresofSum(n):
    return (n*(n+1)/2)**2

def todoMath():
    n = 100
    result = squaresofSum(n) - sumofSquares(n)
    return result

print(todoMath())

