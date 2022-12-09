#include <bits/stdc++.h>
using namespace std;

//we don't talk about how long it took me to solve and debug this
//it was an issue with moving diagonally since i hardcoded it bad

pair<int, int> knots[10];

void displayKnots() {
	for (int i = 0; i < 6; i++) {
		for (int j = 00; j < 6; j++) {
			bool displayed = false;
			for (int k = 0; k < 10; k++) {
				if (knots[k].first == i && knots[k].second == j) {
					cout << k;
					displayed = true;
					break;
				}
			}
			if (!displayed && i == 0 && j == 0) {
				cout << "#";
				displayed = true;
			}
			if (!displayed) { cout << "."; }
		}
		cout << endl;
	}
}

void updateTail(int a, int b) {

	if (knots[a].first > knots[b].first && knots[a].first - knots[b].first > 1) {
		knots[b].first++;
		if (knots[a].second - knots[b].second > 0) {
			knots[b].second++;
		}
		else if (knots[a].second - knots[b].second < 0) {
			knots[b].second--;
		}
	}

	else if (knots[a].first < knots[b].first && knots[b].first - knots[a].first > 1) {
		knots[b].first--;
		if (knots[a].second - knots[b].second > 0) {
			knots[b].second++;
		}
		else if (knots[a].second - knots[b].second < 0) {
			knots[b].second--;
		}
	}

	else if (knots[a].second > knots[b].second && knots[a].second - knots[b].second > 1) {
		knots[b].second++;
		if (knots[a].first - knots[b].first > 0) {
			knots[b].first++;
		}
		else if (knots[a].first - knots[b].first < 0) {
			knots[b].first--;
		}
	}

	else if (knots[a].second < knots[b].second && knots[b].second - knots[a].second > 1) {
		knots[b].second--;
		if (knots[a].first - knots[b].first > 0) {
			knots[b].first++;
		}
		else if (knots[a].first - knots[b].first < 0) {
			knots[b].first--;
		}
	}

}

int main() {
	
	set<pair<int, int>> visited;

	while (true) {

		string str; int t;
		cin >> str;
		if (str == "end") { break; }
		cin >> t;

		for (int i = 0; i < t; i++) {
			
			if (str == "R") {
				knots[0].first++;
			}

			if (str == "L") {
				knots[0].first--;
			}

			if (str == "U") {
				knots[0].second++;
			}

			if (str == "D") {
				knots[0].second--;
			}

			for (int i = 0; i < 9; i++) {
				updateTail(i, i + 1);
			}
			visited.insert(make_pair(knots[9].first, knots[9].second));

		}

	}

	cout << visited.size() << endl;

}
