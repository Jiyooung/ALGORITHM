/*
baekjoon 1927 : 최소 힙
solved by JY
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

int main(void) {
	int N;
	scanf("%d\n", &N);

	int x;
	priority_queue<int, vector<int>, greater<int> > pq;

	for (int i = 0; i < N; i++) {
		scanf("%d\n", &x);

		if (x == 0) {
			if (pq.empty())
				printf("%d\n", 0);
			else {
				printf("%d\n", pq.top());
				pq.pop();
			}
		}
		else {
			pq.push(x);
		}

	}

	return 0;
}
