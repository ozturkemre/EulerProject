lists = [1]
# we only need diagonals . summy is accrual. add summy to lists last elemant four times to get diagonals.
# after that add 2 to summy to calculate new summy
# repeat 500 times . 500 right + 500 left + 1 center = 1001
summy = 2
result = 0
# repeat 500 times
for i in range(1, 501):
    # repeat append 4 times
    for z in range(4):
        lists.append(lists[-1]+summy)

    summy += 2

# calculate sums of diagonals
for j in lists:
    result += j
    
print(result)

