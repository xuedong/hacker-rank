//
//  AppleOrange.m
//  
//
//  Created by xuedong on 07/03/2018.
//

#import <Foundation/Foundation.h>


void countApplesAndOranges(int s, int t, int a, int b, NSArray *apples, NSArray *oranges) {
    int num_apples = 0;
    for (int apple_i = 0; apple_i < [apples count]; apple_i++) {
        if (a + [[apples objectAtIndex:apple_i] integerValue] >= s && a + [[apples objectAtIndex:apple_i] integerValue] <= t) {
            num_apples += 1;
        }
    }
    
    int num_oranges = 0;
    for (int orange_i = 0; orange_i < [oranges count]; orange_i++) {
        if (b + [[oranges objectAtIndex:orange_i] integerValue] >= s && b + [[oranges objectAtIndex:orange_i] integerValue] <= t) {
            num_oranges += 1;
        }
    }
    
    printf("%i\n", num_apples);
    printf("%i\n", num_oranges);
}

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int s;
    int t;
    scanf("%i %i", &s, &t);
    int a;
    int b;
    scanf("%i %i", &a, &b);
    int m;
    int n;
    scanf("%i %i", &m, &n);
    
    NSMutableArray *apples = [NSMutableArray array];
    int apple[m];
    for(int apple_i = 0; apple_i < m; apple_i++){
        scanf("%i", &apple[apple_i]);
        [apples addObject:[NSNumber numberWithInteger:apple[apple_i]]];
    }
    NSMutableArray *oranges = [NSMutableArray array];
    int orange[n];
    for(int orange_i = 0; orange_i < n; orange_i++){
        scanf("%i", &orange[orange_i]);
        [oranges addObject:[NSNumber numberWithInteger:orange[orange_i]]];
    }
    
    countApplesAndOranges(s, t, a, b, apples, oranges);
    
    [pool drain];
    return 0;
}
