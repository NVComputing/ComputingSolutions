# type an empty line and "end" at the end of the input
cur_input = input()
elves = []
while cur_input != "end":
    cur_total = 0
    while cur_input != "":
        cur_total += int(cur_input)
        cur_input = input()
        
    elves.append(cur_total)
    cur_input = input()
    
elves.sort()
print("part 1: " + str(elves[-1]))
print("part 2: " + str(elves[-1] + elves[-2] + elves[-3]))
