
letters = 0
while True:
    x1 = input()
    if x1 == 'end':
        break
    x2 = input()
    x3 = input()

    c1 = set(x1)
    c2 = set(x2)
    c3 = set(x3)
    let = c1.intersection(c2).intersection(c3).pop()
    if let > 'Z':
        letters += int(ord(let)) - int(ord('a')) + 1
    else:
        letters += int(ord(let)) - int(ord('A')) + 27
print(letters)
