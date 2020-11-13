/*
baekjoon 10828 : Ω∫≈√ 
solved by JY
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <cstring>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	int N;
	scanf("%d\n", &N);

	stack<int> s;

	char c[10];
	int num;

	for (int i = 0; i < N; i++) {
		scanf("%s", c);

		if (!strcmp(c, "push")) {
			scanf("%d", &num);

			s.push(num);
		}
		else if (!strcmp(c, "pop")) {
			if (s.empty())
				printf("%d\n", -1);
			else {
				printf("%d\n", s.top());
				s.pop();
			}
		}
		else if (!strcmp(c, "size")) {
			printf("%d\n", s.size());
		}
		else if (!strcmp(c, "empty")) {
			printf("%d\n", s.empty());
		}
		else if (!strcmp(c, "top")) {
			if (s.empty())
				printf("%d\n", -1);
			else
				printf("%d\n", s.top());
		}
	}

	return 0;
}
