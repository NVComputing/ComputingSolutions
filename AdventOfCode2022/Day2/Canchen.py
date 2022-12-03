score = 0
score2 = 0
cur_line = input()

while cur_line != '':
    
    cur_input = cur_line.split(' ')

    #represent RPS as an int, 1 = r, 2 = p, 3 = s
    other = 0
    you = 0

    #part 1
    if cur_input[0] == 'A':
        other = 1
    elif cur_input[0] == 'B':
        other = 2
    else:
        other = 3

    if cur_input[1] == 'X':
        you = 1
    elif cur_input[1] == 'Y':
        you = 2
    else:
        you = 3

    score += you
    
    if you - other == 1 or (you == 1 and other == 3):
        score += 6
    elif you == other:
        score += 3

    #part 2
    if cur_input[1] == 'X':
        you = other - 1
        if you == 0:
            you = 3
    elif cur_input[1] == 'Y':
        score2 += 3
        you = other
    else:
        score2 += 6
        you = other + 1
        if you == 4:
            you = 1
    
    score2 += you
    
    cur_line = input()
    
print("part 1: " + str(score))
print("part 2: " + str(score2))
