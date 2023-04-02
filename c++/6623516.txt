#include <stdio.h>

int main(){
	int n,x,count;
	while(true){
		scanf("%d %d",&n,&x);
		if(n == 0 && x == 0) break;
		count = 0;
		for(int min = 1; min < x/3 && min <= n-2;min++){
			for(int middle = min+1;middle < x - (min+middle) && middle <= n-1; middle++){
				if(x-(min+middle) <= n) count++;
			}
		}
		printf("%d\n",count);
	}

}
