/*
baekjoon 2877 : 4와 7
solved by JY
DATE : 2020.12.19
구현 문제
*/
#include <iostream>
#include <cstdio>
#include <math.h>
#include <string>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
    int K, sum = 0, count = 1;
    string ans = "";
    cin >> K;
    while(1) {
        if (K > sum + pow(2, count)) {
            sum += pow(2, count);
            count++;
        }
        else break;
    }

    int num = K - sum, p = pow(2, count), start = 0;
    while(count--) {
        if (num <= start + p/2) {
            ans += '4';
        }
        else {            
            ans += '7';
            start += p/2;
        }
        p = p/2;
    }
    cout << ans;
	return 0;
}