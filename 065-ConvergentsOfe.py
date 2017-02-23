num1 = 1
num2 = 2
result = 0
for i in range(2, 101):
    if i % 3:
        num1, num2 = num2, num1 + num2
    else:
        num1, num2 = num2, num1 + num2 * (2 * i // 3)
sonuc = 0
for i in str(num2):
    sonuc += int(i)
print(sonuc)
