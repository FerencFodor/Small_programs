#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>

int main() {
	int n, a=1;

	printf("Zadajte cele cislo <1,10>: ");
	scanf("%d", &n);

	if (n>= 1 && n <= 10) {
		for (int i = 1; i <= n; i++) {
			for (int j = 0; j < i; j++) {
				printf("%d ", a);
				a++;
			}
			putchar('\n');
		}
	}
	else {
		printf("zly vstup");
	}
	
	return 0;
}