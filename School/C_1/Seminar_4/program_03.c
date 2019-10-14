#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>

int main() {
	int n;

	printf("Zadajte cele cislo <1,15>: ");
	scanf("%d", &n);

	if (n < 1 || n > 15) {
		printf("Cislo nie je z daneho intervalu");
	}
	else {
		for (int i = 0; i < n; i++) {
			printf("%d: ", i + 1);
			for (int j = n - i; j > 0; j--) {
				printf("%d ", j);
			}

			putchar('\n');
		}
	}
	
	return 0;
}