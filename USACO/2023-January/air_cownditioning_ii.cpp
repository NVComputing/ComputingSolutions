#include <bits/stdc++.h>
using namespace std;

int main() {

	// grab input: n and m
	int n, m;
	cin >> n >> m;

	// store required cooling for each stall
	int req[101];
	memset(req, 0, sizeof(req));

	// grab input: required cooling
	for (int i = 0; i < n; i++) {
		int s, t, c;
		cin >> s >> t >> c;
		for (int k = s; k <= t; k++) {
			req[k] = c;
		}
	}

	// grab input: air conditioners
	int cond[10][4]; // store a, b, p, m for each air conditioner
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> cond[i][j];
		}
	}

	//test all possible combinations by generating all subsets
	int low = 100000; // dummy value, but must be greater than 10 * 1000
	for (int i = 0; i < pow(2, m); i++) {

		int cur[101];
		memset(cur, 0, sizeof(cur));
		int cost = 0;

		// cool bitmasking trick to generate subsets
		for (int j = 0; j < m; j++) {
			if (i & 1 << j) {
				cost += cond[j][3];
				for (int k = cond[j][0]; k <= cond[j][1]; k++) {
					cur[k] += cond[j][2];
				}
			}
		}

		// check that it meets the cooling criteria
		bool good = true;
		for (int k = 0; k < 101; k++) {
			if (cur[k] < req[k]) {
				good = false;
				break;
			}
		}

		// update lowest cost we've found
		if (good) {
			low = min(low, cost);
		}
		
	}

	// print our answer
	cout << low;

}
