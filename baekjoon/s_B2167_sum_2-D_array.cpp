#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int input[301][301];
int dp[301][301];

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n, m, k;
	int i, j, x, y;
	vector <int> ans;

	cin >> n >> m;

	int result = 0;

	for (int a = 1; a <= n; a++) {
		for (int b = 1; b <= m; b++) {
			cin >> input[a][b];
			dp[a][b] = dp[a][b - 1] + input[a][b];
		}
	}

	cin >> k;

	while (1) {
		if (k == 0)
			break;

		cin >> i >> j >> x >> y;

		for (int r = i; r <= x; r++) {
			result += dp[r][y] - dp[r][j - 1];
		}

		ans.push_back(result);
		result = 0;
		k--;
	}

	for (int a = 0; a < ans.size(); a++) {
		cout << ans[a] << '\n';
	}

	return 0;
}
