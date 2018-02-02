#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    long long int *arr = malloc(sizeof(long long int) * 5);
    for(int arr_i = 0; arr_i < 5; arr_i++){
       scanf("%lld",&arr[arr_i]);
    }
    long long int total = 0;
    for(int arr_i = 0; arr_i < 5; arr_i++){
        total += arr[arr_i];
    }
    long long int min = arr[0];
    long long int max = arr[0];
    
    for(int arr_i = 1; arr_i < 5; arr_i++){
        if(arr[arr_i] < min){
            min = arr[arr_i];
        }
        if(arr[arr_i] > max){
            max = arr[arr_i];
        }
    }
    
    printf("%lli %lli", total-max, total-min);
    
    return 0;
}

