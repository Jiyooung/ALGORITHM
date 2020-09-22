/*
programmers : 징검다리 건너기
solved by JY
이분 탐색 사용
*/
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int check(vector<int>& stones, int mid, int k) {	// mid 번째 친구가 건널 수 있는 지 확인
	int count = 0;
	for (int i = 0; i < stones.size(); i++) {
		if (stones[i] < mid) {	// stones가 mid보다 작은 경우 건너뛰어야 함.
			count++;
			if (count == k)		// 건너뛴 갯수가 k개가 되면 mid 친구는 건널 수 없음.
				return 0;
		}
		else
			count = 0;			// 돌을 밟을 때마다 count 초기화
	}

	return 1;
}

int solution(vector<int> stones, int k) {
	int answer = 0;
	int mini = *min_element(stones.begin(), stones.end());
	int maxi = *max_element(stones.begin(), stones.end());

	while (mini < maxi) {
		int mid = (mini + maxi + 1) / 2;

		if (check(stones, mid, k)) {	// mid가 가능한 경우
			mini = mid;
			answer = mid;
		}
		else {	// mid가 불가능한 경우
			maxi = mid - 1;
		}
	}

	if (mini == maxi) {	// 모든 stones 동일할 경우, 제일 작은 값(or 큰 값)이 되는 경우..등
		if (check(stones, mini, k))	
			answer = mini;
	}

	return answer;
}


int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	// k = 3 > 3
	//vector<int> stones = { 2, 4, 5, 3, 2, 1, 4, 2, 5, 1 };
	int k = 2;
	
	// k = 6 > 4
	//vector<int> stones = { 1, 1, 1, 1, 2, 4, 5, 3, 2, 1, 4, 2, 5, 1, 1, 1, 1, 1};
	
	// k = 6 > 1
	//vector<int> stones = { 1, 1, 1, 1, 2, 4, 5, 3, 2, 1, 4, 2, 5, 1, 1, 1, 1, 1, 1 };

	// k = 3 > 2
	//vector<int> stones = { 2, 2, 2, 2, 2, 4, 5, 3, 2, 1, 4, 2, 5, 2, 2, 2, 2, 2, 2 };

	vector<int> stones = { 200000000, 200000000, 5, 200000000, 4, 200000000, 5, 200000000 };

	//vector<int> stones = { 2 };

	cout << solution(stones, k) << '\n';

	return 0;
}