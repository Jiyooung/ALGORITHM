/*
baekjoon 3780 : 네트워크 연결
solved by JY
*/
#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

vector <pair<int, int>> sum;

int abs(int a, int b) {
	if (a - b < 0)
		return b - a;
	else
		return a - b;
}

pair<int, int> find(int v) {	
	if (sum[v].first == v) {
		return sum[v];
	}

	pair<int, int> tmp = find(sum[v].first);
	sum[v].first = tmp.first;
	sum[v].second += tmp.second;
	return sum[v];
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		sum.clear();
		for (int j = 0; j <= n; j++) {
			pair<int, int> tmp;
			tmp.first = j;
			tmp.second = 0;
			sum.push_back(tmp);
		}

		while (1) {
			char c;

			cin >> c;
			if (c == 'E') {
				int v;
				cin >> v;
				pair<int, int> pv = find(v);
				cout << pv.second << '\n';
			}
			else if (c == 'I') {
				int v, pv;
				cin >> v >> pv;
				sum[v].first = pv;
				sum[v].second = abs(pv, v) % 1000;
			}
			else
				break;
		}
	}

	return 0;
}