#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

long long int aVeryBigSum(int n, int ar_size, long long int* ar) {
    // Complete this function
    long long int sum = 0;
    for(int i=0; i<ar_size; i++){
        sum += ar[i];
    }
    return sum;
}

int main() {
    int n; 
    scanf("%i", &n);
    long long int *ar = malloc(sizeof(long long int) * n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       scanf("%lli",&ar[ar_i]);
    }
    long long int result = aVeryBigSum(n, n, ar);
    printf("%lli\n", result);
    return 0;
}

