/*
baekjoon 6064 : 카잉 달력
solved by JY
최소공배수 활용
*/
#include <cstdio>
#include <iostream>

using namespace std;

int gcd(int a, int b) {	// 최대공약수
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t, m, n, x, y;
	int lcm = 1;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> m >> n >> x >> y;
		
		lcm = m * n / gcd(m, n);	// 최소공배수

		int j;

		if (n == y)
			y = 0;

		for (j = x; j <= lcm; j += m) {
			if (j % n == y)
				break;
		}

		if (j > lcm) {
			cout << -1 << '\n';
			continue;
		}

		cout << j << '\n';
	}

	return 0;
}