/*
baekjoon 1655 : 가운데를 말해요
solved by JY
DATE : 2020.12.23
구현 문제, priority_queue 사용
*/
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, num;
    priority_queue<int> up;                               // Max Heap
    priority_queue<int, vector<int>, greater<int>> down;  // Min Heap
    up.push(-10000);
    down.push(10000);
    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> num;

        if (i % 2 == 1) {   // up.size() == down.size()
            if (num <= down.top()) {
                up.push(num);
            } else {
                down.push(num);
                up.push(down.top());
                down.pop();
            }
        } else {
            if (num < up.top()) {
                down.push(up.top());
                up.pop();
                up.push(num);
            } else {
                down.push(num);
            }
        }
        cout << up.top() << '\n';
    }

    return 0;
}