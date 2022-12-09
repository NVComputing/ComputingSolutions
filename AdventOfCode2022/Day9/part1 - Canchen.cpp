#include <bits/stdc++.h>
using namespace std;

int headX = 0, headY = 0, tailX = 0, tailY = 0;
void updateTail() {

	if (headX > tailX && headX - tailX > 1) {
		tailX++;
		if (abs(headY - tailY) == 1) {
			tailY = headY;
		}
	}

	if (headX < tailX && tailX - headX > 1) {
		tailX--;
		if (abs(headY - tailY) == 1) {
			tailY = headY;
		}
	}

	if (headY > tailY && headY - tailY > 1) {
		tailY++;
		if (abs(headX - tailX) == 1) {
			tailX = headX;
		}
	}

	if (headY < tailY && tailY - headY > 1) {
		tailY--;
		if (abs(headX - tailX) == 1) {
			tailX = headX;
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
				headX++;
			}

			if (str == "L") {
				headX--;
			}

			if (str == "U") {
				headY++;
			}

			if (str == "D") {
				headY--;
			}

			updateTail();
			visited.insert(make_pair(tailX, tailY));

		}

	}

	cout << visited.size() << endl;

}
