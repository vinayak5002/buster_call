#include <stdio.h>

int main(void) {
	int data[4][13] = {};
	int i, j;
	char c, mark[4] = {'S', 'H', 'C', 'D'};
	int n, num;
	
	scanf("%d", &n);
	
	while (n--) {
		scanf(" %c %d", &c, &num);
		num--;
		
		switch(c) {
			case 'S': data[0][num] = 1; break;
			case 'H': data[1][num] = 1; break;
			case 'C': data[2][num] = 1; break;
			case 'D': data[3][num] = 1; break;
		}
	}
	
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 13; j++) {
			if (!data[i][j]) {
				printf("%c %d\n", mark[i], j + 1);
			}
		}
	}
	
	return 0;
}

