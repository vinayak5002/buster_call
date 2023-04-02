#include <stdio.h>

int main() {

  int n,m,i,j;
  int a,b;
  int A[100][100] = {0};
  int B[100] = {0};
  int c[100] = {0};

  scanf("%d %d " ,&n,&m);

  for(j=0; j<n; j++) {
  for(i=0; i < m; i++) {
    scanf("%d",&a);
    A[j][i] = a;
  }
}

  for(j=0; j<m; j++) {
    scanf("%d",&b);
    B[j] = b;
  }

  for(j=0;j<n ; j++){ 
  for(i = 0; i<m; i++){
     c[j] = c[j] + A[j][i]*B[i];
    }
  }

  for(i=0;i<n;i++) {
    printf("%d\n",c[i]);
  }
  return 0;
}
