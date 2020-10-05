/*
baekjoon 11727 : 2xn 타일링 2
solved by JY
다이나믹 프로그래밍 사용
*/
#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int n = 0;

	cin >> n;

	int dp[1001] = { 0, };
	dp[1] = 1;
	dp[2] = 3;

	for (int i = 3; i <= n; i++) {
		dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007;
	}

	cout << dp[n] % 10007;

	return 0;
}
