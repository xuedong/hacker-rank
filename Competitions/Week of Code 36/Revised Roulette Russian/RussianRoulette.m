#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int n;
    scanf("%i", &n);
    int doors[n];
    for (int doors_i = 0; doors_i < n; doors_i++) {
        scanf("%i", &doors[doors_i]);
    }
    
    int min_doors = 0;
    int max_doors = 0;
    for (int doors_i = 0; doors_i < n; doors_i++) {
        if (doors[doors_i] == 1) {
            max_doors += 1;
        }
    }
    int i = 0;
    while (i < n-1) {
        if (doors[i] == 1) {
            min_doors += 1;
            i += 2;
        }
        else {
			i += 1; 
        }
		if (i == n-1 && doors[n-1] == 1) {
			min_doors += 1;
		}
    }
    
    printf("%i %i", min_doors, max_doors);
    
    [pool drain];
    return 0;
}
