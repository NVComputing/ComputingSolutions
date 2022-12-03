c1 = []
c2 = []
point = [1,2,3]
while True:
    x = input()
    if x == 'end':
        break;
    c1.append(int(ord(x[0])) - int(ord('A')))
    c2.append(int(ord(x[2])) - int(ord('X')))

def checkoutcome(arr1, arr2):
    if arr1 == arr2:
        return point[arr2] + 3
    if (arr1 + 1)%3 == arr2:
        return point[arr2] + 6
    return point[arr2]
tot = 0
for x in range(len(c1)):
    tot += checkoutcome(c1[x], c2[x])
print(tot)
