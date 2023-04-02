#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
	int H,W;
	while(true){
		scanf("%d %d",&H,&W);
		if(H == 0 && W == 0) break;
		for(int i = 0; i < W; i++) printf("#");
		printf("\n");

		for(int i = 1; i < H-1; i++){
			printf("#");
			for(int j = 1; j < W-1; j++) printf(".");
			printf("#\n");
		}

		if(H > 1){
			for(int i = 0; i < W; i++) printf("#");
			printf("\n");
		}
		printf("\n");
	}
}
