cur_string = input()

total = 0
total2 = 0

while cur_string != '':

    parts = cur_string.split(',')
    first = parts[0].split('-')
    second = parts[1].split('-')

    for i in range(2):
        first[i] = int(first[i])
        second[i] = int(second[i])

    if (first[0] >= second[0] and first[1] <= second[1]) or (second[0] >= first[0] and second[1] <= first[1]):
        total += 1
    
    if (first[1] >= second[0] and first[0] <= second[1]) or (second[1] >= first[0] and second[0] <= first[1]):
        total2 += 1

    cur_string = input()

print("part 1: " + str(total))
print("part 2: " + str(total2))