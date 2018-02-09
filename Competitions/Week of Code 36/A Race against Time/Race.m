#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int n;
    scanf("%i\n", &n);
    int mason_height;
    scanf("%i\n", &mason_height);
    int heights[n-1];
    for(int heights_i = 0; heights_i < n-1; heights_i++){
        scanf("%i", &heights[heights_i]);
    }
    int prices[n-1];
    for(int prices_i = 0; prices_i < n-1; prices_i++){
        scanf("%i", &prices[prices_i]);
    }
    
    int time = 0;
    int price = 0;
    int carrier = 0;
    int position = 0;
    while (position < n) {
        position += 1;
        if (heights[carrier] < heights[position]) {
            time += 1 + heights[position] - heights[carrier];
            price += prices[position];
            carrier = position;
        }
        else if (prices[position] < 0) {
            time += 1;
            price += prices[position];
            carrier = position;
        }
        else {
            time += 1;
        }
    }
    
    int total = time + price;
    printf("%i", total);
    
    [pool drain];
    return 0;
}
