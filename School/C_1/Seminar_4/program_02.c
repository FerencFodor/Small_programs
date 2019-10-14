#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>

int main() {
	int n;

	printf("Zadajte cele cislo <1,15>: ");
	scanf("%d", &n);

	if (n < 1 || n > 15) {
		printf("Zle cislo");
	}
	else {
		for (int i = 0; i < n; i++) {
			printf("%d: ", i+1);
			for ( int j = 0; j < n - i; j++)
			{
				printf("%d ", j+1);
			}
			putchar('\n');
		}
	}
	
	return 0;
}