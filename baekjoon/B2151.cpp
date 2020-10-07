/*
baekjoon 2151 : 거울 설치
solved by JY
*/
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#define min(a,b) a>b?b:a
#define INF 1e9

using namespace std;

int N;
char H[52][52] = {0,};
int visited[52][52] = {0,};
int dx[4] = {0, 0, -1, 1};  // 상, 하, 좌, 우
int dy[4] = {-1, 1, 0, 0};
int s_x, s_y, e_x, e_y;
int ans = INF;

void dfs(int x, int y, int dir, int ret) {
    //cout << "x " << y << " " << x << '\n';
    for (int i = 0; i < 4; i++) {
        if (i == dir) continue;

        int c_x = x + dx[i];
        int c_y = y + dy[i];
        //cout << "c " << c_y << " " << c_x << '\n';
        if (c_x < 0 || c_x >= N || c_y < 0 || c_y >= N) continue;
        else if (H[c_y][c_x] == '*') continue;
        else if (H[c_y][c_x] == '.') {
            while (1) {
                c_x = c_x + dx[i];
                c_y = c_y + dy[i];

                if (c_x < 0 || c_x >= N || c_y < 0 || c_y >= N) break;
                if (H[c_y][c_x] == '*') break;
                else if (H[c_y][c_x] == '.') continue;               
                else if (H[c_y][c_x] == '!') {
                    if (i == 0) dfs(c_x, c_y, 1, ret + 1);
                    else if (i == 1) dfs(c_x, c_y, 0, ret + 1);
                    else if (i == 2) dfs(c_x, c_y, 3, ret + 1);
                    else if (i == 3) dfs(c_x, c_y, 2, ret + 1);
                    continue;
                }
                else if (H[c_y][c_x] == '#' && c_y == e_y && c_x == e_x) {
                    ans = min(ans, ret);
                    return ;
                }
            }
        }
        else if (H[c_y][c_x] == '!') {
            if (i == 0) dfs(c_x, c_y, 1, ret + 1);
            else if (i == 1) dfs(c_x, c_y, 0, ret + 1);
            else if (i == 2) dfs(c_x, c_y, 3, ret + 1);
            else if (i == 3) dfs(c_x, c_y, 2, ret + 1);

            while (1) {
                c_x = c_x + dx[i];
                c_y = c_y + dy[i];

                if (c_x < 0 || c_x >= N || c_y < 0 || c_y >= N) break;
                if (H[c_y][c_x] == '*') break;
                else if (H[c_y][c_x] == '.') continue;               
                else if (H[c_y][c_x] == '!') {
                    if (i == 0) dfs(c_x, c_y, 1, ret + 1);
                    else if (i == 1) dfs(c_x, c_y, 0, ret + 1);
                    else if (i == 2) dfs(c_x, c_y, 3, ret + 1);
                    else if (i == 3) dfs(c_x, c_y, 2, ret + 1);
                    continue;
                }
                else if (H[c_y][c_x] == '#' && c_y == e_y && c_x == e_x) {
                    ans = min(ans, ret);
                    return ;
                }
            }
            continue;
        }
        else if (H[c_y][c_x] == '#' && c_y == e_y && c_x == e_x) {
            ans = min(ans, ret);
            return ;
        }
    }
    return ;
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
                s_x = j; s_y = i;
                flag = false;
            } 
            else if (H[i][j] == '#' && !flag) {
                e_x = j; e_y = i;
            }
        }
    }

    //cout << s_y << " " << s_x << " " << e_y << " " << e_x << '\n';

    dfs(s_x, s_y, -1, 0);

    cout << ans;
    
    return 0;
}