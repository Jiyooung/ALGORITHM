/*
baekjoon 14226 : 이모티콘
solved by JY
DATE : 2021.04.29
DP 알고리즘 사용
DP[i] = i + 1 일까지 일했을 때에 얻을 수 있는 최대 수익
*/
#include <iostream>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int N;
    cin >> N;

    int dp[N+2] = {0};
    int MAX = 0, ans = 0;
    for (int i=1; i<N+1; i++) {
        int t, p;
        cin >> t >> p;
        MAX = max(MAX, dp[i]);
        if (i + t <= N + 1)
            dp[i + t] = max(p + MAX, dp[i + t]);
        
        ans = max(ans, dp[i]);
    }
    cout << max(ans, dp[N+1]);
}