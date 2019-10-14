#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>

int main() {
	int n;

	printf("Zadajte cele cislo <1,15>: ");
	scanf("%d", &n);

	if (n < 1 || n > 15 || n%2 == 0) {
		printf("Zly vstup ");
	}
	else {
		for (int i = 1; i <= n * 2 - 1; i++) {
			if (i <= n) {
				for (int j = 0; j < n; j++) {
					if (j < i) {
						putchar('*');
					}
					else {
						putchar('-');
					}
				}
			}
			else {
				for (int j = 0; j < n; j++) {
					if (j <= n - (i - n)-1) {
						putchar('*');
					}
					else {
						putchar('-');
					}
				}
			}
			putchar('\n');
		}
	}
	
	return 0;
}