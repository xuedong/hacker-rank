#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max(int a, int b)
{
    return a > b ? a : b;
}

int max_of_four(int a, int b, int c, int d)
{
    int m1 = max(a, b);
    int m2 = max(c, d);
    return m1 > m2 ? m1 : m2;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);

    return 0;
}

