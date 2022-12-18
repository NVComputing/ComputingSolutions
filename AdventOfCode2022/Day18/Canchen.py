cur_line = input()
cube = [[[False for i in range(25)] for i in range(25)] for i in range(25)]
droplets = []

while cur_line != '':
    x = cur_line.split(',')
    x = [int(i) for i in x]
    droplets.append([x[0], x[1], x[2]])
    cube[x[0]][x[1]][x[2]] = True
    cur_line = input()

outside = [[[False for i in range(25)] for i in range(25)] for i in range(25)]
outside[0][0][0] = True
queue = [[0, 0, 0]]
def search(x, y, z):

    x += 1
    if not cube[x][y][z] and not outside[x][y][z]:
        queue.append([x, y, z])
        outside[x][y][z] = True

    x -= 2
    if not cube[x][y][z] and not outside[x][y][z]:
        queue.append([x, y, z])
        outside[x][y][z] = True

    x += 1
    y += 1
    if not cube[x][y][z] and not outside[x][y][z]:
        queue.append([x, y, z])
        outside[x][y][z] = True

    y -= 2
    if not cube[x][y][z] and not outside[x][y][z]:
        queue.append([x, y, z])
        outside[x][y][z] = True

    y += 1
    z += 1
    if not cube[x][y][z] and not outside[x][y][z]:
        queue.append([x, y, z])
        outside[x][y][z] = True

    z -= 2
    if not cube[x][y][z] and not outside[x][y][z]:
        queue.append([x, y, z])
        outside[x][y][z] = True

        

while len(queue) != 0:
    top = queue.pop(0)
    search(top[0], top[1], top[2])

ans = 0
uwu = 0
for d in droplets:
    if not cube[d[0] + 1][d[1]][d[2]]:
        ans += 1
    if not cube[d[0] - 1][d[1]][d[2]]:
        ans += 1
    if not cube[d[0]][d[1] + 1][d[2]]:
        ans += 1
    if not cube[d[0]][d[1] - 1][d[2]]:
        ans += 1
    if not cube[d[0]][d[1]][d[2] + 1]:
        ans += 1
    if not cube[d[0]][d[1]][d[2] - 1]:
        ans += 1

    if outside[d[0] + 1][d[1]][d[2]]:
        uwu += 1
    if outside[d[0] - 1][d[1]][d[2]]:
        uwu += 1
    if outside[d[0]][d[1] + 1][d[2]]:
        uwu += 1
    if outside[d[0]][d[1] - 1][d[2]]:
        uwu += 1
    if outside[d[0]][d[1]][d[2] + 1]:
        uwu += 1
    if outside[d[0]][d[1]][d[2] - 1]:
        uwu += 1

print(ans)
print(uwu)
