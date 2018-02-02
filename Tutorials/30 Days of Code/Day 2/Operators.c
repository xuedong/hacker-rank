#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    double cost;
    int tip;
    int tax;
    double total;
    
    scanf("%lf %d %d", &cost, &tip, &tax);
    total = cost * (1+tip/100.+tax/100.);
    printf("The total meal cost is %d dollars.", (int) round(total));
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
