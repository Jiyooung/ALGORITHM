// 밍구 오빠 코드 참고
#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;
int input[52][52];
int check[52][52];

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int dfs(int r, int c, int d) {
	int x, y, dd;

	for (int i = 1; i <= 4; i++) {
		dd = (d - i + 4) % 4;
		x = r + dx[dd];
		y = c + dy[dd];

		if (input[x][y] != 1 && check[x][y] != 1) {	//a
			check[x][y] = 1;
			return dfs(x, y, dd) + 1;
		}
	}

	dd = (d + 2) % 4;
	x = r + dx[dd];
	y = c + dy[dd];
	if (input[x][y] == 0)
		return dfs(x, y, d);

	return 1;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n = 0, m = 0, r = 0, c = 0, d = 0;
	cin >> n >> m;
	cin >> r >> c >> d;
	int answer = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> input[i][j];
		}
	}

	check[r][c] = 1;
	answer = dfs(r, c, d);

	cout << answer;

	return 0;
}