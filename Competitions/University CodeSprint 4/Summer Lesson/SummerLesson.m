#import <Foundation/Foundation.h>

int *howManyStudents(int m, int c_size, int *c) {
    int *result = malloc(m * sizeof(int));
    for (int result_i = 0; result_i < m; result_i++) {
        result[result_i] = 0;
    }
    for (int c_i = 0; c_i < c_size; c_i++) {
        result[c[c_i]] += 1;
    }
    
    return result;
}

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int n;
    int m;
    scanf("%i %i", &n, &m);
    int c[n];
    for(int c_i = 0; c_i < n; c_i++){
       scanf("%i", &c[c_i]);
    }
    
    int *result = howManyStudents(m, n, c);
    for(int result_i = 0; result_i < m; result_i++) {
        if(result_i) {
            printf(" ");
        }
        printf("%i", result[result_i]);
    }
    puts("");
    
    [pool drain];
    return 0;
}

