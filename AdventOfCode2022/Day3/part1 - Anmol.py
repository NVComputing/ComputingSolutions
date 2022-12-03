
letters = 0
while True:
    x = input()
    if x == 'end':
        break
    c1 = set(x[:len(x)//2])
    c2 = set(x[len(x)//2:])
    let = c1.intersection(c2).pop()
    if let > 'Z':
        letters += int(ord(let)) - int(ord('a')) + 1
    else:
        letters += int(ord(let)) - int(ord('A')) + 27
print(letters)
