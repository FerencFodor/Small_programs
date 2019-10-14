#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>

int main() {
	int n;

	printf("Zadaj cele cislo <1,15>: ");
	scanf("%d", &n);

	int mid = (n - n % 2) / 2 + n % 2;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			if (j == mid || i == mid || i == j || j == n - i + 1)
				putchar('*');
			else
				putchar('-');
		putchar('\n');
	}

	return 0;
}