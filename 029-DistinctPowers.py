liste = []
for i in range(2, 101):
    for j in range(2, 101):
        liste.append(i**j)

# convert list to class set to distinct multiply elements
liste = set(liste)
print(len(liste))

