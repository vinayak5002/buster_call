#include <stdio.h>
 
int main(void)
{   int a,b,i;
    char op;
    for(i=1;i>0;i++){
        scanf("%d %c %d",&a,&op,&b);
        if(op=='+')
        {printf("%d\n",a+b);
        }
        else if(op=='-')
        {printf("%d\n",a-b);
        }
        else if(op=='*')
        {printf("%d\n",a*b);
        }
        else if(op=='/'){
            printf("%d\n",a/b);
        }else if(op=='?') {
            break;
        }
    }
    return 0;
}

