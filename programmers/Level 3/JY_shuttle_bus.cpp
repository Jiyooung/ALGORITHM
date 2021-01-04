/*
programmers : 셔틀 버스
solved by JY
*/
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string change(string time) {
	string answer;
	int hour = ((int)time.at(0) - '0') * 10 + ((int)time.at(1) - '0');
	int min = ((int)time.at(3) - '0') * 10 + ((int)time.at(4) - '0');

	min--;
	if (min < 0) {
		hour--; min = 59;
	}
	answer += to_string(hour / 10);
	answer += to_string(hour % 10);
	answer += ":";
	answer += to_string(min / 10);
	answer += to_string(min % 10);

	return answer;
}

string solution(int n, int t, int m, vector<string> timetable) {
	string answer = "";
	sort(timetable.begin(), timetable.end());
	
	int num = 0;	// 타고 간 사람 인덱스
	bool last = false;

	for (int i = 1; i <= n; i++) {
		int hour = 9 + t * (i - 1) / 60;
		int minute = t * (i - 1) % 60;

		string time;

		if (hour < 10)
			time = "0" + to_string(hour) + ":";
		else
			time = to_string(hour) + ":";

		if (minute < 10)
			time += "0" + to_string(minute);
		else
			time += to_string(minute);

		int check_m = m;

		if (i == n)
			last = true;
		
		for (int j = num; j < timetable.size(); j++) {
			if (timetable[j] <= time) {
				check_m--;

				if (check_m == 0) {
					num = j + 1;
					break;
				}
			}
			else {
				num = j;
				break;
			}
		}
		
		if (check_m != 0 && last) {
			answer = time;
		}
		if (check_m == 0 && last) {
			answer = change(timetable[num-1]);
		}
	}

	return answer;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	string answer;

	//vector<string> timetable = { "09:10", "09:09", "08:00"};
	//answer = solution(2, 10, 2, timetable);
	//vector<string> timetable = { "09:00", "09:00", "09:00", "09:00" };
	//answer = solution(2, 1, 2, timetable);

	vector<string> timetable = { "09:10", "09:09", "08:00"};
	answer = solution(1, 10, 2, timetable);

	cout << answer;

	return 0;
}