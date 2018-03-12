#import <Foundation/Foundation.h>


int gcd(int a, int b) {
    if (a > b) {
        return gcd(b, a);
    }
    if (a == 0) {
        return b;
    }
    return gcd(b % a, a);
}

int gcdn(int n, int *arr) {
    int result = arr[0];
    for (int i = 1; i < n; i++) {
        result = gcd(arr[i], result);
    }
    
    return result;
}

int lcm(int a, int b) {
    int gcd2 = gcd(a, b);
    
    return a * b / gcd2;
}

int lcmn(int n, int *arr) {
    int result = arr[0];
    for (int i = 1; i < n; i++) {
        result = lcm(arr[i], result);
    }
    
    return result;
}

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int n;
    int m;
    scanf("%i %i",&n,&m);
    int a[n];
    for(int a_i = 0; a_i < n; a_i++){
        scanf("%i", &a[a_i]);
    }
    int b[m];
    for(int b_i = 0; b_i < m; b_i++){
        scanf("%i", &b[b_i]);
    }
    
    int lcm_a = lcmn(n, a);
    int gcd_b = gcdn(m, b);
    int trials = gcd_b / lcm_a;
    int count = 0;
    for (int i = 1; i <= trials; i++) {
        if (gcd_b % (lcm_a * i) == 0) {
            count += 1;
        }
    }
    printf("%i", count);
    
    [pool drain];
    return 0;
}
