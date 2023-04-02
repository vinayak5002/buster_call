#include <stdio.h>
 
int main(void) {
    int W, H, x, y, r;
    scanf("%d %d %d %d %d", &W, &H, &x, &y, &r);
    if(x >= r && y >= r && (H - r) >= y && (W - r) >= x) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
