part_two = True

board = [[0 for i in range(200)] for i in range(800)]
cur_line = input()
largest_y = 0

while cur_line != '':

    x = cur_line.split(' -> ')
    x = [k.split(',') for k in x]
    for k in x:
        k[0] = int(k[0])
        k[1] = int(k[1])
        largest_y = max(k[1], largest_y)

    last_point = x[0]

    for i in range(1, len(x)):
        if x[i][0] != last_point[0]:
            for j in range(min(last_point[0], x[i][0]), max(last_point[0], x[i][0]) + 1):
                board[j][x[i][1]] = 1
        else:
            for j in range(min(last_point[1], x[i][1]), max(last_point[1], x[i][1]) + 1):
                board[x[i][0]][j] = 1
        last_point = x[i]

    cur_line = input()

largest_y += 2
if part_two:
    for i in range(800):
        board[i][largest_y] = 1

ans = 0
while True:

    x = 500
    y = 0

    while True:
        if y >= 199 or board[500][0] == 1:
            break

        if board[x][y + 1] == 0:
            y += 1
        elif board[x - 1][y + 1] == 0:
            y += 1
            x -= 1
        elif board[x + 1][y + 1] == 0:
            y += 1
            x += 1
        else:
            board[x][y] = 1
            ans += 1
            break

    if y >= 199 or board[500][0] == 1:
        break

print(ans)
