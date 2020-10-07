/*
baekjoon 2151 : 거울 설치
solved by JY
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

    vector<int> v;

    for (int i=0; i< 5; i++) {
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }
    
    sort(v.begin(), v.end());
    
    for (int i=0; i<5; i++) {
        cout << v.at(i) << '\n';
    }

    cout << "haha 하하";
	return 0;
}