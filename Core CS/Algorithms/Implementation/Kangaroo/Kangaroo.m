#import <Foundation/Foundation.h>


int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int x1;
    int v1;
    int x2;
    int v2;
    scanf("%i %i %i %i", &x1, &v1, &x2, &v2);
    
    if (v1 <= v2) {
        printf("NO");
    }
    else if ((x2-x1) % (v1-v2) == 0) {
        printf("YES");
    }
    else {
        printf("NO");
    }
    
    [pool drain];
    return 0;
}

