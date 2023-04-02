#include <stdio.h>
#include <string.h>

int main(void) {
	char str[201];
	while(scanf("%s",str)){
		if(!strcmp(str, "-")) break;
		
		int m, h = 0,b ,i;
		scanf("%d", &m);
		for(i = 0; m > i; i++){
			scanf("%d", &b);
			h += b;
		}
		h %= strlen(str);
		for(i = h; strlen(str) + h > i; i++){
			printf("%c", str[i%strlen(str)]);
		}
		printf("\n");
	}
	return 0;
}

