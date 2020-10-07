/*
baekjoon 2151 : 거울 설치
solved by JY
*/
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#define min(a, b) a > b ? b : a
#define INF 1e9

using namespace std;

int N;
char H[52][52] = {
	0,
};
int mirror[52][52][5] = {
	0,
};
int dx[4] = { 0, 0, -1, 1 };  // 상, 하, 좌, 우
int dy[4] = { -1, 1, 0, 0 };
int s_x, s_y, e_x, e_y;
int ans = INF;

void dfs(int x, int y, int dir, int ret) {
	//cout << "x " << y << " " << x << '\n';
	int c_x = x;
	int c_y = y;

	while (1) {
		c_x = c_x + dx[dir];
		c_y = c_y + dy[dir];

		if (c_x < 0 || c_x >= N || c_y < 0 || c_y >= N) {
			break;
		}
		if (H[c_y][c_x] == '*') break;
		if (H[c_y][c_x] == '.') continue;
		if (H[c_y][c_x] == '!') {
			if (mirror[c_y][c_x][dir] == 1) {
				return;
			}
			//cout << "h " << c_y << " " << c_x << '\n';
			if (mirror[c_y][c_x][4] == 0) {
				mirror[c_y][c_x][4] = 1;
				mirror[c_y][c_x][dir] = 1;
				if (dir == 0)
					dfs(c_x, c_y, 3, ret + 1);
				else if (dir == 1)
					dfs(c_x, c_y, 2, ret + 1);
				else if (dir == 2)
					dfs(c_x, c_y, 1, ret + 1);
				else if (dir == 3)
					dfs(c_x, c_y, 0, ret + 1);

				for (int i = 0; i < 4; i++) {
					mirror[c_y][c_x][i] = 0;
				}
				mirror[c_y][c_x][4] = 2;
				mirror[c_y][c_x][dir] = 1;
				if (dir == 0)
					dfs(c_x, c_y, 2, ret + 1);
				else if (dir == 1)
					dfs(c_x, c_y, 3, ret + 1);
				else if (dir == 2)
					dfs(c_x, c_y, 0, ret + 1);
				else if (dir == 3)
					dfs(c_x, c_y, 1, ret + 1);

				for (int i = 0; i < 4; i++) {
					mirror[c_y][c_x][i] = 0;
				}
				mirror[c_y][c_x][4] = 0;
				H[c_y][c_x] = '.';
				dfs(c_x, c_y, dir, ret);
				H[c_y][c_x] = '!';
				return;
			}
			else if (mirror[c_y][c_x][4] == 1) {
				mirror[c_y][c_x][dir] = 1;
				if (dir == 0)
					dfs(c_x, c_y, 3, ret);
				else if (dir == 1)
					dfs(c_x, c_y, 2, ret);
				else if (dir == 2)
					dfs(c_x, c_y, 1, ret);
				else if (dir == 3)
					dfs(c_x, c_y, 0, ret);
			}
			else if (mirror[c_y][c_x][4] == 2) {
				mirror[c_y][c_x][dir] = 1;
				if (dir == 0)
					dfs(c_x, c_y, 2, ret);
				else if (dir == 1)
					dfs(c_x, c_y, 3, ret);
				else if (dir == 2)
					dfs(c_x, c_y, 0, ret);
				else if (dir == 3)
					dfs(c_x, c_y, 1, ret);
			}
			else
				continue;
		}
		else if (H[c_y][c_x] == '#' && c_y == e_y && c_x == e_x) {
			//cout << "ans1 " << ans;
			ans = min(ans, ret);
			//cout << " ans2 " << ans << '\n';
			return;
		}
	}
	return;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	bool flag = true;

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> H[i][j];
			if (H[i][j] == '#' && flag) {
				s_x = j;
				s_y = i;
				flag = false;
			}
			else if (H[i][j] == '#' && !flag) {
				e_x = j;
				e_y = i;
			}
		}
	}

	//cout << s_y << " " << s_x << " " << e_y << " " << e_x << '\n';
	for (int i = 0; i < 4; i++) {
		dfs(s_x, s_y, i, 0);
	}

	cout << ans << '\n';

/*
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << mirror[i][j][4] << " ";
		}
		cout << '\n';
	}
*/
	return 0;
}