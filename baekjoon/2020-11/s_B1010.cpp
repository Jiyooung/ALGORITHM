/*
baekjoon 1010 : 다리 놓기
solved by JY
DATE : 2020.11.13
*/
#include <iostream>
#include <cstdio>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

    int t;
    cin >> t;

    for (int i=0; i<t; i++) {
        int n, m, ans = 1;
        cin >> n >> m;
        
        for (int j = 0; j < n; j++) {
            ans = ans * (m - j) / (j + 1);
        }
        cout << ans << '\n';
    }

	return 0;
}