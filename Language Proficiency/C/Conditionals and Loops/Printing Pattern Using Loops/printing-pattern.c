#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.

    int len = 2*n-1;
    for (int i=0; i<len; i++) {
        for (int j=0; j<len; j++) {
            int minDistance = i < j ? i : j;
            minDistance = minDistance < len-i-1 ? minDistance : len-i-1;
            minDistance = minDistance < len-j-1 ? minDistance : len-j-1;
            printf("%d ", n-minDistance);
        }
        printf("\n");
    }

    return 0;
}

