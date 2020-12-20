/*
baekjoon 2798 : 블랙잭
solved by JY
DATE : 2020.12.20
모든 조합을 구해 합계 확인
next_permutation() 사용
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

    int N, M, answer = 0, tmp;
    vector <int> card, ind;
    cin >> N >> M;

    for (int i=0; i<N; i++) {
        cin >> tmp;
        card.push_back(tmp);
    }

	for (int i = 0; i < N; i++) {
        if (i < N - 3) ind.push_back(0);
        else ind.push_back(1);
	}
    
    do {
        int sum = 0;
        for (int i = 0; i < N; i++) {
			if (ind[i] == 1) sum += card[i];
		}
        if (answer < sum && sum <= M) answer = sum;
    } while(next_permutation(ind.begin(), ind.end()));

    cout << answer;

	return 0;
}