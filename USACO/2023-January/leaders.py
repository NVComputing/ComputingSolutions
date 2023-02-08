# grab input
n = int(input())
cows = input()
e = list(map(int, input().split(' ')))

# our list is 0-indexed, but the input is 1-indexed
for i in range(len(e)):
    e[i] -= 1

# find first and last occurrences of each cow...
first_h = cows.index('H')
first_g = cows.index('G')
last_h = cows.rindex('H')
last_g = cows.rindex('G')

# to see which cows have all the cows of their breed in their list
h_leader = False
g_leader = False
if e[first_h] >= last_h:
    h_leader = True
if e[first_g] >= last_g:
    g_leader = True

# calculate our answer: 2 possibilities
# // one cow's list has all the cows of their breed,
# // and the other cow's list contains that cow
# // or both cows' lists contain all the cows of their breed
ans = 0
if h_leader:
    for i in range(first_h):
        if cows[i] == 'G' and e[i] >= first_h:
            ans += 1
if g_leader:
    for i in range(first_g):
        if cows[i] == 'H' and e[i] >= first_g:
            ans += 1

if h_leader and g_leader:
    ans += 1

print(ans)
