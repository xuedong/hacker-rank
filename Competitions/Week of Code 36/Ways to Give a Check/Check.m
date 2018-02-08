#import <Foundation/Foundation.h>

int check(char[8][8] board) {
    
}

int main(int argc, const char * argv[]) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int t;
    scanf("%i", &t);
    for (int scenario = 0; scenario < t; scenario++) {
        char board[8][8];
        for (int board_i = 0; board_i < 8; board_i++) {
            for (int board_j = 0; board_j < 8; board_j++) {
                scanf("%c", &board[board_i][board_j]);
            }
        }
    }
    
    [pool drain];
    return 0;
}
