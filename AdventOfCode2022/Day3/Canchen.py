cur_string = input()
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
total2 = 0
k = 0
recent_strings = []
while cur_string != 'end':

    first = cur_string[:int(len(cur_string) / 2)]
    second = cur_string[int(len(cur_string) / 2):]
    
    for a in first:
        if a in second:
            total += letters.index(a) + 1
            break
    
    recent_strings.append(cur_string)

    if k % 3 == 2:
        for a in recent_strings[0]:
            if a in recent_strings[1] and a in recent_strings[2]:
                total2 += letters.index(a) + 1
                break
        recent_strings.clear()

    k += 1
    cur_string = input()

print("part 1: " + str(total))
print("part 2: " + str(total2))
