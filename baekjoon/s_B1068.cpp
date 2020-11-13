/*
baekjoon 1068 : 트리
solved by JY
dfs 사용
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n = 0, r = 0, answer = 0;
vector<int> root;
vector<int> tree[52];

void dfs(int parent) {
	if (parent == r)
		return ;

	if (tree[parent].empty()) {	// 자식이 없으면 ++
		answer++;
		return ;
	}

	for (int i = 0; i < tree[parent].size(); i++) {
		if (tree[parent].size() == 1 && tree[parent][i] == r) {
			answer++;	// 자식이 하나인데 그게 제거 노드면 ++
			return ;
		}
		else
			dfs(tree[parent][i]);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int tmp;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		if (tmp == -1)
			root.push_back(i);
		else
			tree[tmp].push_back(i);	// 부모에 자식 노드 추가
	}
	cin >> r;

	for (int i = 0; i < root.size(); i++) {
		dfs(root[i]);
	}

	cout << answer;

	return 0;
}