string = input()

for i in range(len(string) - 14):

    substr = string[i:i + 14]

    letters = set()
    for j in range(14):
        letters.add(substr[j])
    
    if len(letters) == 14:
        print(i + 14)
        break