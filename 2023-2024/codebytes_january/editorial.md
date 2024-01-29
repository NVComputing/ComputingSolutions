# January Contest Editorial

... at least for the problems Canchen wrote. They're all gochiusa references because that's what he's been addicted to in December when he wrote the problems, but feel free to send recommendations for the theme for next contest's problems.

## A. Budget Management

You don't need me to explain this.
```py
a, b = map(int, input().split())
if a >= b:
    print("Yes")
else:
    print("No")
```

## B. Mean of Distinct Integers

Add all the integers to a set to find all the distinct integers, and then calculate the average. Alternative solutions exist with sorting the list of integers and removing duplicates, but why would you do that over a set?

```py
n = int(input())
s = set()
for i in range(n):
    s.add(int(input()))
print(int((sum(s) / len(s)) + 0.5)) # python's builtin round function is weird
```

## C. Subsequences of Dancers

Get the input and insert 0 into the middle of the array. Then use prefix sums and iterate over every possible subsequence in O(n^2) time. Alternative solutions exist that don't use a prefix sum but still does a traversal in O(n^2) time over every subsequence.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {

    int n;
    cin >> n;
    vector<int> uwu;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        uwu.push_back(x);
    }
    uwu.insert(uwu.begin() + (uwu.size() / 2), 0);

    vector<long long> prefix;
    prefix.push_back(0);
    for (int i = 0; i < uwu.size(); i++) {
        prefix.push_back(prefix[i] + uwu[i]);
    }

    long long ans = 0;
    for (int i = 0; i < prefix.size() - 1; i++) {
        for (int j = i + 1; j < prefix.size(); j++) {
            if (prefix[j] - prefix[i] > 0) {
                ans++;
            }
        }
    }

    cout << ans << endl;

}
```

## D. Coffee Combinations

Notice that if **x + y = n**, then **y = n - x**. Then you're solving for from **x = 1** to **x = n**, how many values make **x (n - x) > k**. Rearranging the equation gives **-x^2 + nx - k > 0**, which looks like an upside down parabola. This equation is initally less than 0 for small values of **x**, then again dips below **0** for large values of x. Binary search for the points where the equation changes sign, or just solve it using math to get the upper and lower bounds, and subtract for your answer.

```py
n, k = map(int, input().split())

high = round(n / 2)
high += 1
low = 0
while (low < high):
  mid = low + (high - low) // 2
  if mid * (n - mid) > k:
    high = mid
  else:
    low = mid + 1
lower_bound = low

high = n
low = round(n / 2)
low -= 1
while (low < high):
  mid = low + (high - low + 1) // 2
  if mid * (n - mid) > k:
    low = mid
  else:
    high = mid - 1
upper_bound = low

if lower_bound == round(n / 2) + 1 and upper_bound == round(n / 2) - 1:
  print(0)
else:
  print(upper_bound - lower_bound + 1)
```

## E. Tournament Scheduling

Classic greedy problem. The key is to always attend the earliest ending event possible. Sort the events by their ending time and just simulate.

```py
n = int(input())
events = []

for i in range(n):
    t, d = map(int, input().split())
    events.append((t + d, t))

events.sort()

ct = 0
last = 0
for e in events:
    if e[1] >= last:
        last = e[0]
        ct += 1

print(ct)
```

## F. Putting up Posters

If there are **n** towns, **n - 1** roads, and all the towns are connected, then the network between all the towns looks like a tree. Since Chiya cannot walk through the same road more than once, it is essentially a directed graph and Chiya must start from town 1 and walk further down the tree. We can sort all the destinations Chiya needs to visit based on their depth in the tree, walk backwards from the furthest destination to town 1, and check if it visits every destination she needs to put posters in along the way.

```py
n, k = map(int, input().split())
dests = list(map(int, input().split()))

edges = {}
for i in range(1, n + 1):
    edges[i] = []

for _ in range(n - 1):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

# order the graph
depth = [-1 for _ in range(n + 1)]
depth[1] = 0
queue = [1]

def dfs(x):
    for dest in edges[x]:
        if depth[dest] == -1:
            depth[dest] = depth[x] + 1
            queue.append(dest)
while len(queue) != 0:
    dfs(queue.pop())

# sort the destinations by depth
# if there is a path, it must start from the furthest depth and work its way back to 1
dests.sort(key=lambda x : depth[x])
product = 1

x = dests.pop()
good = True
while good:
    good = False
    for dest in edges[x]:
        if depth[dest] < depth[x]:
            if len(dests) != 0 and dest == dests[-1]:
                dests.pop()
            product *= x
            product %= 999999937
            x = dest
            good = True
            break

if len(dests) == 0:
    print(product)
else:
    print(-1)
```

## G. Bribery

Do dynamic programming and keep track of how many ways there are to give gifts worth a certain amount of money. Since **x + y % a = ((x % a) + (y % a)) % a**, we only need to keep track of values between **0** and **a**. Each time we consider giving a gift with value **k**, the number of ways to give gifts worth **x** yen is equal to the old number of ways to give **x** yen of gifts plus the number of ways to give **(x - k) % a** yen worth of gifts. In addition, there is also one more way of giving **k** yen worth of gifts. Repeat this process for each gift and output the answer.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {

    int n, a, b;
    cin >> n >> a >> b;

    int prices[n];
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }

    int MOD = 999999937;
    int combinations[a];
    memset(combinations, 0, sizeof(combinations));

    for (auto k : prices) {
        int new_combinations[a];
        memcpy(new_combinations, combinations, sizeof(combinations));
        new_combinations[k] += 1;
        for (int i = 0; i < a; i++) {
            if (i - k < 0) {
                new_combinations[i] += combinations[a + (i - k)];
                new_combinations[i] %= MOD;
            }
            else {
                new_combinations[i] += combinations[i - k];
                new_combinations[i] %= MOD;
            }
        }
        memcpy(combinations, new_combinations, sizeof(combinations));
    }

    cout << combinations[b] << endl;
    
}
```
