#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }
    
    double plus = 0.;
    double minus = 0.;
    double zeros = 0.;
    
    for(int arr_i=0; arr_i < n; arr_i++){
        if(arr[arr_i] > 0){
            plus += 1;
        }
        else if(arr[arr_i] < 0){
            minus += 1;
        }
        else{
            zeros += 1;
        }
    }
    
    printf("%f\n", plus/n);
    printf("%f\n", minus/n);
    printf("%f\n", zeros/n);
    
    return 0;
}

