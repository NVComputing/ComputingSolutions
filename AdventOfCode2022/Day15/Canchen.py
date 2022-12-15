#it takes forever to run but it gets the answer eventually (i hope)
Y_LINE = 2000000
BOUNDS = 4000000
cur_line = input()

segments = []
scanners = []

def distance(a, b, x, y):
    return abs(a - x) + abs(b - y)


while cur_line != '':

    uwu = cur_line.split(' ')
    x = int(uwu[2][2:-1])
    y = int(uwu[3][2:-1])
    beacon_x = int(uwu[8][2:-1])
    beacon_y = int(uwu[9][2:])

    dist = abs(x - beacon_x) + abs(y - beacon_y)
    y_diff = abs(y - Y_LINE)
    width = dist - y_diff
    if width >= 0:
        segments.append([x - width, x + width])

    scanners.append([x, y, dist])
    cur_line = input()

segments.sort()
ans = 0
low = -1
high = -1

for k in segments:

    if low == -1:
        low = k[0]
        high = k[1]
        continue

    if k[0] <= high:
        high = max(high, k[1])
        continue

    ans += high - low
    low = k[0]
    high = k[1]

ans += high - low
print(ans)

def good_point(x, y):
    if x <= BOUNDS and y <= BOUNDS and x >= 0 and y >= 0:
        for k in scanners:
            if distance(x, y, k[0], k[1]) <= k[2]:
                return False
        return True
    else:
        return False

def value(x, y):
    return (x * 4000000) + y


p = 1
for k in scanners:
    x = k[0]
    y = k[1]

    print("checking scanner " + str(p) + " of " + str(len(scanners)))
    for i in range(k[2] + 1):
        if i % 10000 == 0:
            print(str(i // 10000) + "/" + str(k[2] // 10000), end='\r')
        if good_point(x + i, y - i + k[2] + 1):
            print()
            print(value(x + i, y - i + k[2] + 1))
            exit(0)
        if good_point(x - i, y - i + k[2] + 1):
            print()
            print(value(x - i, y - i + k[2] + 1))
            exit(0)
        if good_point(x + i, y + i - k[2] - 1):
            print()
            print(value(x + i, y + i - k[2] - 1))
            exit(0)
        if good_point(x - i, y + i - k[2] - 1):
            print()
            print(value(x - i, y + i - k[2] - 1))
            exit(0)

    p += 1
