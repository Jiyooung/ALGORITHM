/*
baekjoon 2877 : 4와 7
solved by JY
DATE : 2020.12.19
구현 문제, best answer
*/
#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
    int K;
    string ans = "";
    cin >> K;
    ++K;
    while (K > 1) {
        if (K%2 == 0) 
            ans = '4' + ans;
        else
            ans = '7' + ans;
        K /= 2;
    }
    cout << ans;
	return 0;
}