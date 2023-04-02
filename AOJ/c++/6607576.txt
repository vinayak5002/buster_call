#include<stdio.h>
#include<stdlib.h>
int ss(int x)
{
    int n,t=0;
    if(x%3==0)
    t=1;
    do
    {
        if(x%10==3)
        {
            t=1;
            break;
        }
        x/=10;    
    }
    while(x);
    return t;
}
int main()
{
    int x,n;
    scanf("%d",&n);
    int t;
    for(x=3;x<=n;x++)
    {
        t=ss(x);
        if(t==1)
        printf(" %d",x);
    }
    printf("\n");
    return 0;
}
