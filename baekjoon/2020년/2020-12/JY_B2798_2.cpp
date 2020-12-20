/*
baekjoon 2798 : 블랙잭
solved by JY
DATE : 2020.12.20
모든 조합을 구해 합계 확인
3중 for문 사용
*/
#include <iostream>
#include <cstdio>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

    int N, M, card[101]={0,}, answer = 0;
    cin >> N >> M;

    for (int i=0; i<N; i++) {
        cin >> card[i];
    }
    
    for (int i=0; i< N-2; i++) {
        for (int j=i+1; j< N-1; j++) {
            for (int k=j+1; k<N; k++) {
                int sum = card[i] + card[j] + card[k];
                if (answer < sum && sum <= M) answer = sum;
            }
        }
    }

    cout << answer;

	return 0;
}