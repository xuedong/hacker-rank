#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int n;
    scanf("%i", &n);
    for (int a0 = 0; a0 < n; a0++) {
        NSString *acid_name;
        char *acid_name_temp = (char *)malloc(512000 * sizeof(char));
        scanf("%s", acid_name_temp);
        acid_name = [NSString stringWithFormat:@"%s", acid_name_temp];
        
        int prefix = [acid_name hasPrefix:@"hydro"];
        int suffix = [acid_name hasSuffix:@"ic"];
        if (prefix && suffix) {
            printf("non-metal acid\n");
        }
        else if (suffix) {
            printf("polyatomic acid\n");
        }
        else {
            printf("not an acid\n");
        }
    }
    
    [pool drain];
    return 0;
}
