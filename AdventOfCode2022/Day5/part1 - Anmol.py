stacks = []
for x in range(9):
    stacks.append([])
st = input()
while(st[0:4]!=" 1  "):
    for i in range(len(st)):
        if (st[i] == '['):
            stacks[i // 4].append(st[i + 1])
    st = input()
input()
st = input()
for x in range(9):
    stacks[x].reverse()
while st != "end":

    x = st.split(" ")
    for count in range(int(x[1])):
        if len(stacks[int(x[3])-1]) == 0:
            break
        stacks[int(x[5])-1].append(stacks[int(x[3])-1].pop(len(stacks[int(x[3])-1])-1))
    st = input()
for x in range(9):
    print(stacks[x][len(stacks[x])-1], end = "")
