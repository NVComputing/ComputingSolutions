q = int(input())

for i in range(q):

    string = input()

    # find the substring that requires us to perform the least swaps
    swaps_to_do = 69
    for k in range(1, len(string) - 1):
        if string[k] == 'O':
            swaps_needed = 0
            if string[k - 1] != 'M':
                swaps_needed += 1
            if string[k + 1] != 'O':
                swaps_needed += 1
            swaps_to_do = min(swaps_to_do, swaps_needed)

    # if nothing is valid, print -1
    if swaps_to_do == 69:
        print(-1)
        continue
    
    # find how many letters we need to delete
    letters_to_delete = len(string) - 3
    if letters_to_delete < 0:
        # if our starting string is shorter than 3 chars, print -1
        print(-1)
        continue

    # number of operations = how many times we swap + how many times we delete
    print(swaps_to_do + letters_to_delete)
