#include<stdio.h>
int main()
{
  int a,b,c,d;
  scanf("%d%d%d",&a,&b,&c);
  for(a;a<b+1;a++)
    {
      if(c%a==0)d++;
    }
  printf("%d\n",d);
  return 0;
}

