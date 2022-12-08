#include <bits/stdc++.h>
using namespace std;

int INPUT_SIZE = 99;

int main() {
	
	int arr[INPUT_SIZE][INPUT_SIZE];

	for (int i = 0; i < INPUT_SIZE; i++) {
		string str; cin >> str;
		for (int j = 0; j < INPUT_SIZE; j++) {
			arr[i][j] = stoi(str.substr(j, 1));
		}
	}

	int ans = 0;
	for (int i = 0; i < INPUT_SIZE; i++) {
		for (int j = 0; j < INPUT_SIZE; j++) {

			bool wasGood = false;

			//i++
			bool good = true;
			for (int k = i + 1; k < INPUT_SIZE; k++) {
				if (arr[k][j] >= arr[i][j]) {
					good = false;
					break;
				}
			}
			if (good) {
				wasGood = true;
			}

			//i--
			good = true;
			for (int k = i - 1; k >= 0; k--) {
				if (arr[k][j] >= arr[i][j]) {
					good = false;
					break;
				}
			}
			if (good) {
				wasGood = true;
			}

			//j++
			good = true;
			for (int k = j + 1; k < INPUT_SIZE; k++) {
				if (arr[i][k] >= arr[i][j]) {
					good = false;
					break;
				}
			}
			if (good) {
				wasGood = true;
			}

			//j--
			good = true;
			for (int k = j - 1; k >= 0; k--) {
				if (arr[i][k] >= arr[i][j]) {
					good = false;
					break;
				}
			}
			if (good) {
				wasGood = true;
			}

			if (wasGood) {
				ans++;
			}

		}
	}

	cout << ans << endl;

	int anss = 0;
	for (int i = 0; i < INPUT_SIZE; i++) {
		for (int j = 0; j < INPUT_SIZE; j++) {

			int a = 0;
			for (int k = i + 1; k < INPUT_SIZE; k++) {
				if (!(arr[k][j] >= arr[i][j])) {
					a++;
				}
				else{
					a++;
					break;
				}
			}

			int b = 0;
			for (int k = i - 1; k >= 0; k--) {
				if (!(arr[k][j] >= arr[i][j])) {
					b++;
				}
				else {
					b++;
					break;
				}
			}

			int c = 0;
			for (int k = j + 1; k < INPUT_SIZE; k++) {
				if (!(arr[i][k] >= arr[i][j])) {
					c++;
				}
				else {
					c++;
					break;
				}
			}

			int d = 0;
			for (int k = j - 1; k >= 0; k--) {
				if (!(arr[i][k] >= arr[i][j])) {
					d++;
				}
				else {
					d++;
					break;
				}
			}

			anss = max(anss, a * b * c * d);

		}
	}

	cout << anss << endl;

}
