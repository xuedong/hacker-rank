#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

void countApplesAndOranges(int s, int t, int a, int b, int apples_size, int* apples, int oranges_size, int* oranges) {
    // Complete this function
    int num_apples = 0;
    for (int apple_i = 0; apple_i < apples_size; apple_i++) {
        if (a + apples[apple_i] >= s && a + apples[apple_i] <= t) {
            num_apples += 1;
        }
    }
    
    int num_oranges = 0;
    for (int orange_i = 0; orange_i < oranges_size; orange_i++) {
        if (b + oranges[orange_i] >= s && b + oranges[orange_i] <= t) {
            num_oranges += 1;
        }
    }
    
    printf("%i\n", num_apples);
    printf("%i\n", num_oranges);
}

int main() {
    int s; 
    int t; 
    scanf("%i %i", &s, &t);
    int a; 
    int b; 
    scanf("%i %i", &a, &b);
    int m;
    int n; 
    scanf("%i %i", &m, &n);
    int *apple = malloc(sizeof(int) * m);
    for (int apple_i = 0; apple_i < m; apple_i++) {
       scanf("%i", &apple[apple_i]);
    }
    int *orange = malloc(sizeof(int) * n);
    for (int orange_i = 0; orange_i < n; orange_i++) {
       scanf("%i", &orange[orange_i]);
    }
    countApplesAndOranges(s, t, a, b, m, apple, n, orange);
    return 0;
}
