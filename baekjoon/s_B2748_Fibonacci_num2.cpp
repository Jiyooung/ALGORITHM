#include <iostream>
#include <cstdio>

using namespace std;

int f(int n) {
	if (n == 0)
		return 0;

	if (n == 1)
		return 1;

	return f(n - 1) + f(n - 2);
}

int main(void) {
	int a;
	int result;

	cin >> a;

	result = f(a);

	cout << result;
	return 0;
}