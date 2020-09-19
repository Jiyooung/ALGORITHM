#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

	/*
	c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0];
	c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1];
	c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0];
	c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1];
	*/

unsigned long long int h[2][2] = { {0, 1}, {1, 1} };
unsigned long long int result[2][2] = { {0, 1}, {1, 1} };

void gop(int check) {
	unsigned long long int c[2][2] = { 0 };

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < 2; k++) {
				if (check == 1)
					c[i][j] += (result[i][k] * h[k][j]) % 1000000;
				else
					c[i][j] += (h[i][k] * h[k][j]) % 1000000;
			}
			c[i][j] %= 1000000;
		}
	}

	if (check == 1)
		copy(&c[0][0], &c[0][0] + 2 * 2, &result[0][0]);
	else
		copy(&c[0][0], &c[0][0] + 2 * 2, &h[0][0]);
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	long long int n;
	cin >> n;
	n -= 2;

	while (n != 0) {
		if (n % 2 == 1) {
			gop(1);
		}
		gop(0);
		n /= 2;
	}

	cout << result[1][1];

	return 0;
}