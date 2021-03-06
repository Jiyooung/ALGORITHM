/*
programmers : 외벽 점검
solved by JY
테스트 14만 틀림 > 이중 순열로 해결
ind 순열 돌리면 cho는 안돌아가서 1,2,3은 하고 1,3,2는 안해서 틀림
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int solution(int n, vector<int> weak, vector<int> dist) {
	int answer = -1;
	int c = 0;

	sort(dist.begin(), dist.end());

	while (1) {
		c++;
		if (c == dist.size() + 1)
			break;

		vector<int> ind;

		for (int i = 0; i < dist.size() - c; i++) {
			ind.push_back(0);
		}
		for (int i = 0; i < c; i++) {
			ind.push_back(1);
		}

		do {
			vector<int> cho;
			for (int i = 0; i < ind.size(); i++) {
				if (ind[i] == 1)
					cho.push_back(dist[i]);
			}

			do {
				int start = 0;
				vector<int> we = weak;
				int nu = 0;
				int flag = 1;
				for (int i = 0; i < weak.size(); i++) {
					int sum = 0;
					for (int j = start; j < we.size() - 1; j++) {
						if (sum + we[j + 1] - we[j] <= cho[nu]) {
							sum += we[j + 1] - we[j];
							continue;
						}
						else {
							nu++;
							if (nu == cho.size()) {
								flag = 0;
								break;
							}
							sum = 0;
						}
					}
					if (flag == 1) {
						return cho.size();
					}

					we.push_back(we[start] + n);
					start++;
					nu = 0;
					flag = 1;
				}
			} while (next_permutation(cho.begin(), cho.end()));
		} while (next_permutation(ind.begin(), ind.end()));
	}

	return answer;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n = 200;
	// n = 12 ans = 2
	//vector<int> weak = { 1, 5, 6, 10 };
	//vector<int> dist = { 1, 2, 3, 4 };

	// n = 12 ans = 1
//	vector<int> weak = { 1, 3, 4, 9, 10 };
//	vector<int> dist = { 3, 5, 7 };

	// n = 200 ans = 3
	//vector<int> weak = { 0, 10, 50, 80, 120, 160 };
	//vector<int> dist = { 1, 10, 5, 40, 30 };

	// n = 200 ans = 2
	//vector<int> weak = { 0, 100 };
	//vector<int> dist = { 1, 1 };

	// n = 50 ans = 1
	//vector<int> weak = { 1 };
	//vector<int> dist = { 6 };

	vector<int> weak = { 1, 10, 20, 30, 40 };
	vector<int> dist = { 10, 5, 6, 7 };
	cout << solution(n, weak, dist);

	return 0;
}