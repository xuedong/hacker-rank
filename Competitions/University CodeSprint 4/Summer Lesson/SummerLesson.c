#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int* howManyStudents(int m, int c_size, int* c, int *result_size) {
    // Return an array denoting the number of students taking each class.
    int *result = malloc(sizeof(int) * m);
    for (int result_i = 0; result_i < *result_size; result_i++) {
        result[result_i] = 0;
    }
    for (int c_i = 0; c_i < c_size; c_i++) {
        result[c[c_i]] += 1;
    }
    
    return result;
}

int main() {
    int n; 
    int m; 
    scanf("%i %i", &n, &m);
    int *c = malloc(sizeof(int) * n);
    for (int c_i = 0; c_i < n; c_i++) {
       scanf("%i",&c[c_i]);
    }
    int result_size = m;
    int* result = howManyStudents(m, n, c, &result_size);
    for(int result_i = 0; result_i < result_size; result_i++) {
        if(result_i) {
            printf(" ");
        }
        printf("%d", result[result_i]);
    }
    puts("");

    return 0;
}
