part_one = false

k = -1
if part_one:
    k = 4
else:
    k = 14

string = input()

for i in range(len(string) - k):

    substr = string[i:i + k]

    letters = set()
    for j in range(k):
        letters.add(substr[j])
    
    if len(letters) == k:
        print(i + k)
        break
