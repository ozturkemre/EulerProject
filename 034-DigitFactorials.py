# max 7-digit number 9999999   7 * 9! = 2540160


def calculate_factorial(n):
    back = 1
    for i in range(1, n+1):
        back *= i
    return back

result = 0
for i in range(3, 2540161):
    subsum = 0
    
    for j in str(i):
        subsum += calculate_factorial(int(j))
        
    if subsum == i:
        result += i
print(result)

