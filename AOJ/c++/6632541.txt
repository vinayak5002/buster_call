#include <stdio.h>
#include <stdlib.h>

void
pri(long long **, long long **, int, int, int);

long long **
Malloc(int, int);

void
Scanf(long long * [], int, int);

int
main(void)
{
    int n, m, l;
    long long **matrixA, **matrixB;

    scanf("%d %d %d", &n, &m, &l);
    matrixA = Malloc(n, m);
    matrixB = Malloc(m, l);
    
    Scanf(matrixA, n, m);
    Scanf(matrixB, m, l);

    pri((long long **) matrixA, (long long **) matrixB, n, m, l);
    return 0;
}

void
pri(long long **a, long long **b, int n, int m, int l)
{
    int i, j, k;
    long long sum;
    for (i = 0; i < n; i++)
        for (j = 0; j < l; j++) {
            sum = 0;
            for (k = 0; k < m; k++)
                sum += a[i][k] * b[k][j];
            printf("%lld", sum);
            if (j == l - 1)
                putchar('\n');
            else
                putchar(' ');
        }
}

long long **
Malloc(int n, int m)
{
    int i;
    long long **arr = (long long **) malloc(sizeof(long long *) * n);
    for (i = 0; i < n; i++)
        arr[i] = (long long *) malloc(sizeof(long long) * m);

    return arr;
}

void
Scanf(long long *arr[], int n, int m)
{
    int i, j;
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%lld", *(arr + i) + j);
}
