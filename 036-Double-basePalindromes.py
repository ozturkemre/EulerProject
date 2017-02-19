def is_palindrome(n):
    return str(n) == str(n)[::-1]
result = 0
for i in range(1000000):
    if is_palindrome(i) and is_palindrome("{:b}".format(i)):
        result += i
print(result)
