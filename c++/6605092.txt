#include <stdio.h>

int main(int argc, char *argv[]) {
    int a, b, sum, n_digits;

    while(scanf("%d%d", &a, &b)!=EOF) {
        sum = a + b;
        n_digits = 0;
        while(sum > 0) {
            n_digits++;
            sum /= 10;
        }
        printf("%d\n", n_digits);
    }
}
