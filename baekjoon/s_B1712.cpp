/*
baekjoon 1712 : 손익분기점
solved by JY
DATE : 2020.11.11
곱하기를 사용하면 오버플로우 발생 
수식을 나눗셈으로 바꿔서 사용
*/
#include <iostream>
#include <cstdio>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

    int A, B, C, cnt = 0;
    cin >> A >> B >> C;

    if (B >= C) {
        cout << -1;
        return 0;
    }
    while(A/(C - B) >= ++cnt) {}
    cout << cnt;

	return 0;
}