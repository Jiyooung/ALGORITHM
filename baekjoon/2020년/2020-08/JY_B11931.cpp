/*
baekjoon 11931 : 수 정렬하기 4
solved by JY
*/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N;
	int a;
	vector<int> v;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end(), greater<int>());

	for (int i = 0; i < N; i++) {
		cout << v[i] << '\n';
	}

	return 0;
}
