INPUT_LINES = 8
INPUT_WIDTH = 9
part_one = False

crates = []
for i in range(9):
    crates.append([])

for i in range(INPUT_LINES):
    cur_line = input()
    for j in range(INPUT_WIDTH):
        if cur_line[1] != ' ':
            crates[j].append(cur_line[1])
        cur_line = cur_line[4:]

cur_line = input()
cur_line = input()
cur_line = input()

while cur_line != 'end':

    parts = cur_line.split(' ')

    if part_one:
        for i in range(int(parts[1])):
            cur_crate = crates[int(parts[3]) - 1].pop(0)
            crates[int(parts[5]) - 1].insert(0, cur_crate)
    else:
        for i in range(int(parts[1])):
            cur_crate = crates[int(parts[3]) - 1].pop(0)
            crates[int(parts[5]) - 1].insert(i, cur_crate)
        
    cur_line = input()

ans = ''
for i in range(INPUT_WIDTH):
    ans += crates[i][0]

print(ans)
