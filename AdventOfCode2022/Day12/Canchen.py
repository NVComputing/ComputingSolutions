import queue

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

q = queue.PriorityQueue()
path = []
start = []
end = []
starting_locs = []

line = input()
k = 0
while line != '':
    if line.find('S') != -1:
        start = [k, line.find('S')]
        line = line.replace('S', 'a')
    if line.find('E') != -1:
        end = [k, line.find('E')]
        line = line.replace('E', 'z')
    for i in range(len(line)):
        if line[i] == 'a':
            starting_locs.append([k, i])
    path.append(line)
    k += 1
    line = input()

INPUT_SIZE = len(path)
Y_SIZE = len(path[0])

dist = [[100000 for i in range(Y_SIZE)] for j in range(INPUT_SIZE)]
dist[start[0]][start[1]] = 0
q.put((0, [start[0], start[1]]))

def in_bounds(x, y):
    return x >= 0 and x < INPUT_SIZE and y >= 0 and y < Y_SIZE

def search(x, y):
    
    next_loc = [x + 1, y]
    if in_bounds(next_loc[0], next_loc[1]) and dist[next_loc[0]][next_loc[1]] > dist[x][y] + 1 and LETTERS.find(path[next_loc[0]][next_loc[1]]) <= LETTERS.find(path[x][y]) + 1:
        dist[next_loc[0]][next_loc[1]] = dist[x][y] + 1
        q.put((dist[x][y] + 1, next_loc))
    
    next_loc = [x - 1, y]
    if in_bounds(next_loc[0], next_loc[1]) and dist[next_loc[0]][next_loc[1]] > dist[x][y] + 1 and LETTERS.find(path[next_loc[0]][next_loc[1]]) <= LETTERS.find(path[x][y]) + 1:
        dist[next_loc[0]][next_loc[1]] = dist[x][y] + 1
        q.put((dist[x][y] + 1, next_loc))
    
    next_loc = [x, y + 1]
    if in_bounds(next_loc[0], next_loc[1]) and dist[next_loc[0]][next_loc[1]] > dist[x][y] + 1 and LETTERS.find(path[next_loc[0]][next_loc[1]]) <= LETTERS.find(path[x][y]) + 1:
        dist[next_loc[0]][next_loc[1]] = dist[x][y] + 1
        q.put((dist[x][y] + 1, next_loc))
    
    next_loc = [x, y - 1]
    if in_bounds(next_loc[0], next_loc[1]) and dist[next_loc[0]][next_loc[1]] > dist[x][y] + 1 and LETTERS.find(path[next_loc[0]][next_loc[1]]) <= LETTERS.find(path[x][y]) + 1:
        dist[next_loc[0]][next_loc[1]] = dist[x][y] + 1
        q.put((dist[x][y] + 1, next_loc))

while q.qsize() != 0:
    top = q.get()
    search(top[1][0], top[1][1])

print(dist[end[0]][end[1]])

dist = [[100000 for i in range(Y_SIZE)] for j in range(INPUT_SIZE)]
for k in starting_locs:
    dist[k[0]][k[1]] = 0
    q.put((0, [k[0], k[1]]))

while q.qsize() != 0:
    top = q.get()
    search(top[1][0], top[1][1])

print(dist[end[0]][end[1]])
