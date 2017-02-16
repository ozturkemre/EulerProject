result = 0
# max limit 531441
limit = 531441
for i in range(2, limit + 1):
    subsum = 0
    for j in str(i):
        subsum += int(j)**5
    if subsum == i:
        result += subsum
print(result)

