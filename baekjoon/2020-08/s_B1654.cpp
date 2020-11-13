/*
baekjoon 1654 : 랜선 자르기
solved by JY
*/
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int k, n;
long long int input[10002];

int check(int m) {
	int count = 0;

	for (int i = 0; i < k; i++) {
		if (input[i] / m > 0) {
			count += input[i] / m;
		}
		if (count >= n) {
			return 1;
		}
	}
	
	return 0;
}

int parametric_iter(long long int l, long long int r) {
	int ret = 1;

	while (l < r) {
		long long int mid = (l + r + 1) / 2;
		int c = check(mid);

		if (c) {
			l = mid;	// 정답이 되는 것은 계속 포함해서 해야 함
			ret = mid;
		}
		else {
			r = mid - 1;
		}
	}

	return ret;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	long long int max = 0;
	long long int ans;
	long long int sum = 0;

	cin >> k >> n;

	for (int i = 0; i < k; i++) {
		cin >> input[i];

		sum += input[i];

		if (input[i] > max)
			max = input[i];
	}

	ans = parametric_iter(1, max);
	
	cout << ans;

	return 0;
}