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
    int a[n][n];
    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){
          scanf("%d",&a[a_i][a_j]);
       }
    }
    int pd = 0;
    int sd = 0;
    for(int a_i = 0; a_i < n; a_i++){
        pd += a[a_i][a_i];
    }
    for(int a_i = 0; a_i < n; a_i++){
        sd += a[a_i][n-1-a_i];
    }
    printf("%d", abs(pd-sd));
    return 0;
}
