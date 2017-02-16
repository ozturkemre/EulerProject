def getFromFile():
    file = open("p067_triangle.txt")

    for row in file:
        triangle.append([int (i) for i in row.split(" ")])


def calculatePath(triangle):
    getFromFile()
    length = 100
    while length >= 1:
        for i in range(0, length-1):
            triangle[length-2][i] = triangle[length-2][i] + max(triangle[length-1][i], triangle[length-1][i+1])
            #               (    a   )
            #      a = max  (   / \  )
            #               (  b  c  )
        length -= 1
    print(triangle[0][0])
    
triangle = []
calculatePath(triangle)

