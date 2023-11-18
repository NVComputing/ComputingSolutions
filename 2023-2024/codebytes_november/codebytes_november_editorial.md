# November Contest Editorial

... at least for the problems Canchen wrote. They're all touhou references because that's what he's been addicted to recently, but feel free to send recommendations for the theme for next contest's problems.

## A. Cirno's Perfect Math Class

This is pretty much a math problem. Find the student that requires the maximum amount of sessions to bring their grade up to 100. Then, find the sum of how many sessions you need to raise each student's grade up to 100, divided by the number of students that can attend per session and rounded up. The answer is the maximum of the two values. The logic is that the second value is a minimum bound on the number of sessions Cirno needs to hold, and the first value corrects for when the minimum bound is unable to raise all student's grades to an 100.

There's probably alternative solutions where you can just brute force and keep on sending the students with the lowest grades to class until they all have 100s, but I haven't tested it.

(i'm actually not sure if my answer is right, i wanted the other captains to check it but nobody would do it T_T speaking of which, does anybody who's reading this want test the problems for next contest? of course this means you can't participate, but i'm sincerely looking for help with doing all this)

```py
import math
n, x, y = map(int, input().split())
min_sessions = 0
student_sessions = 0
for i in range(n):
    t = int(input())
    u = math.ceil((100 - t) / y)
    min_sessions = max(u, min_sessions)
    student_sessions += u
print(max(min_sessions, math.ceil(student_sessions / x)))
```

## B. Love-Colored Master Spark

Another math problem. Sort the list of integers. The maximum power is either the lowest 2 negative integers times the highest positive integer, or the product of the 3 highest positive integers.

I was lazy and just took the highest 3 and lowest 3 integers and brute forced every possible combination, which is why my code is literal garbage.

```py
import itertools

k = int(input())
fuels = list(map(int, input().split()))
fuels.sort()

candidates = []
if len(fuels) < 6:
    candidates.extend(fuels)
else:
    candidates.extend(fuels[-3:])
    candidates.extend(fuels[:3])

ans = -100000 ** 3
for perm in itertools.combinations(candidates, 3):
    ans = max(ans, perm[0] * perm[1] * perm[2])
print(ans)
```

## C. Love-Colored Master Spark (Hard)

Brute force is too slow, so we need a couple optimizations. Notice that the leftmost bits of a number are most important in finding the maximum: `1xxx` will always be greater than `01xx`, no matter whether the digits labeled `x` are `0` or `1`. This means that we should check if we can set each bit in order from left to right.

In order to be able to set a bit in our final answer, we need at least 3 integers in the list which have that bit set. If it is possible, then we should only consider integers in the list which have that bit set as candidates for our *a*, *b*, *c*. Continue this process for every bit, and just pick any 3 remaining numbers as your *a*, *b*, and *c* to calculate your final answer.

```py
k = int(input())
fuels = list(map(int, input().split()))

for i in range(31, -1, -1):
    count = 0
    for f in fuels:
        if f & 1 << i > 0:
            count += 1
    if count >= 3:
        for j in range(len(fuels) - 1, -1, -1):
            if not (fuels[j] & 1 << i > 0):
                fuels.pop(j)

print(fuels[0] & fuels[1] & fuels[2])
```

## D. Gensoukyou News

Basically the [0-1 knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem). The solution involves doing dynamic programming and storing an array with the maximum amount of interest you can generate using *k* words. Initalize the array with 0s to begin with. For each incident Aya can write about, for each *k* in the array, we consider whether including this incident would increase the amount of interest generated. Including an incident that takes *x* words and generates *y* interest would cause the interest to be (maximum interest you can generate with *k - x* words) + (*y*). Update the value if including the incident would increase the interest. After considering all incidents, the maximum interest you can generate with *k* words should be stored in the array, and just output it.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {

    // its in c++ because python was too slow
    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> incidents;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        incidents.push_back(make_pair(x, y));
    }

    int dp[k + 1];
    memset(dp, 0, sizeof(dp));
    for (auto incident : incidents) {
        for (int i = k; i >= incident.first; i--) {
            dp[i] = max(dp[i], dp[i - incident.first] + incident.second);
        }
    }

    cout << dp[k] << endl;

}
```

## E. Librarian Woes

Let each book be a node on a graph, and each pair of incompatible books be an edge connecting two books in that graph. It is impossible to fit the books onto two bookshelfs if there is a cycle of odd length in the graph (for example, in a case like 1-2, 2-3, 3-1). In other words, the answer is "Yes" if the graph is [bipartite](https://en.wikipedia.org/wiki/Bipartite_graph). Simply check if the graph is bipartite by using DFS and trying to color nodes in alternating colors.

```py
n, k = map(int, input().split())

edges = {}
for i in range(1, n + 1):
    edges[i] = []

for i in range(k):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False for _ in range(n + 1)]
color = [0 for _ in range(n + 1)]
good = True
stack = []

def dfs(x):

    visited[x] = True
    target_color = 1
    if color[x] == 1:
        target_color = 2

    for dest in edges[x]:
        if color[dest] != color[x]:
            color[dest] = target_color
            if not visited[dest]:
                stack.append(dest)
        else:
            global good
            good = False
            break

for i in range(1, n + 1):
    if not good:
        break
    if not visited[i]:
        color[i] = 1
        stack.append(i)
        while not len(stack) == 0:
            dfs(stack.pop())

if good:
    print("Yes")
else:
    print("No")
```
