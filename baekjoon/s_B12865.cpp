/*
baekjoon 12865 : 평범한 배낭
solved by JY
DATE : 2020.11.13
1차원 DP 사용 - 기준 : 무게
*/
#include <cstdio>
#include <iostream>
#define max(a,b) a>b?a:b

using namespace std;

int dp[100001] = {0,};

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, k, ans = 0;
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        int w, v;
        cin >> w >> v;

        if (v == 0 || w > k) continue;
        
        for (int i = k - w; i >= 0; i--) {
            dp[i + w] = max(dp[i + w], dp[i] + v);
            ans = max(ans, dp[i + w]);
        }
    }

    cout << ans;

    return 0;
}