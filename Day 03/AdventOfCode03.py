inputfile = open('inputDay03.txt', 'r')
grid = [i.rstrip('\n') for i in inputfile.readlines()]


def newmap(grid):
    return grid.copy()

def replacechar(word, pos, char):
    string = list(word)
    string[pos] = char
    string = "".join(string)
    return string


def updatemap(map,right, down):
    for i in range(int(right * len(grid) /len(grid[0] * down))):
        for j in range(len(grid)):
            map[j] += grid[j]


def mapper(map,right, down):
    j = 0
    x = 0
    counter = 0
    for i in range(len(map)):
        if x + down < len(map) and j + right < len(map[0]):
            if map[x + down][j + right] == '.':
                map[x + down] = replacechar(map[x + down], j + right, 'O')
                j += right
                x += down
            else:
                map[x + down] = replacechar(map[x + down], j + right, 'X')
                counter += 1
                j += right
                x += down
    return counter

def multimapper(rightNdown):
    results = []
    total = 1
    for i in rightNdown:
        nmap = newmap(grid)
        updatemap(nmap, i[0], i[1])
        results.append(mapper(nmap, i[0], i[1]))
    for i in results:
        total *= i
    return total

map = newmap(grid)
updatemap(map,3,1)
print("Part 1:",mapper(map,3,1))

map = newmap(grid)
rightNdown = [(1,1), (3,1), (5,1), (7,1), (1,2)]

print("Part 2:",multimapper(rightNdown))
inputfile.close()
