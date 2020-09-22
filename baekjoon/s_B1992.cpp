/*
baekjoon 1992 : ÄõµåÆ®¸®
solved by JY
*/
#include <iostream>
#include <cstdio>
#pragma warning(disable:4996)

using namespace std;

int input[64][64];

void f(int n, int r, int c) {
	if (n == 1) {
		printf("%d", input[r][c]);
		return ;
	}
	int check = 0;

	for (int i = r; i < r + n; i++) {
		for (int j = c; j < c + n; j++) {
			if (input[r][c] != input[i][j]) {
				check = 1;
				break;
			}
		}
		if (check == 1)
			break;
	}

	if (check == 1) {
		printf("(");
		f(n / 2, r, c);
		f(n / 2, r, c + n / 2);
		f(n / 2, r + n / 2, c);
		f(n / 2, r + n / 2, c + n / 2);
		printf(")");
	}
	else {
		printf("%d", input[r][c]);
	}
}

int main(void) {
	int n, a;
	a = scanf("%d\n", &n);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			a = scanf("%1d", &input[i][j]);
		}
	}

	f(n, 0, 0);

	return 0;
}