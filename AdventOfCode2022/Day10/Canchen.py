#no confidence that this code works

cur_line = input()
x = 1
k = 0

crt = []
cur = ''
ans = 0

while cur_line != '':

    l = cur_line.split(' ')

    if l[0] == 'addx':

        k += 1
        if k % 40 == 20:
            ans += k * x

        if k % 40 == x or k % 40 == (x + 1) % 40 or k % 40 == (x + 2) % 40:
            cur += '#'
        else:
            cur += '.'

        if k % 40 == 0:
            crt.append(cur)
            cur = ''

        k += 1
        if k % 40 == 20:
            ans += k * x

        if k % 40 == x or k % 40 == (x + 1) % 40 or k % 40 == (x + 2) % 40:
            cur += '#'
        else:
            cur += '.'

        if k % 40 == 0:
            crt.append(cur)
            cur = ''

        x += int(l[1])

    else:

        k += 1
        if k % 40 == 20:
            ans += k * x

        if k % 40 == x or k % 40 == (x + 1) % 40 or k % 40 == (x + 2) % 40:
            cur += '#'
        else:
            cur += '.'

        if k % 40 == 0:
            crt.append(cur)
            cur = ''

    cur_line = input()

print(ans)
for c in crt:
    print(c)
