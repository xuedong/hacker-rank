#import <Foundation/Foundation.h>

int queen(int qi, int qj, int ki, int kj) {
    if (qi == ki || qj == kj) {
        return 1;
    }
    else if (abs(qi-ki) == abs(qj-kj)) {
        return 1;
    }
    
    return 0;
}

int rook(int ri, int rj, int ki, int kj) {
    if (ri == ki || rj == kj) {
        return 1;
    }
    
    return 0;
}

int bishop(int bi, int bj, int ki, int kj) {
    if (abs(bi-ki) == abs(bj-kj)) {
        return 1;
    }
    
    return 0;
}

int knight(int ni, int nj, int ki, int kj) {
    if (abs(ni-ki) == 2 && abs(nj-kj) == 1) {
        return 1;
    }
    else if (abs(ni-ki) == 1 && abs(nj-kj) == 2) {
        return 1;
    }
    
    return 0;
}

int check(int ki, int kj, char board[8][9]) {
    int ways = 0;
    int pi = 1;
    int pj = 0;
    for (int j = 1; j < 9; j++) {
        if (board[pi][j] == 'P') {
            //printf("%i %i ", pi, j);
            pj = j;
            if (queen(0, pj, ki, kj)) {
                ways += 1;
            }
            if (rook(0, pj, ki, kj)) {
                ways += 1;
            }
            if (bishop(0, pj, ki, kj)) {
                ways += 1;
            }
            if (knight(0, pj, ki, kj)) {
                ways += 1;
            }
        }
    }
    
    return ways;
}

int main(int argc, const char * argv[]) {
    //NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    
    int t;
    scanf("%i", &t);
    for (int scenario = 0; scenario < t; scenario++) {
        char board[8][9];
        for (int board_i = 0; board_i < 8; board_i++) {
            for (int board_j = 0; board_j < 9; board_j++) {
                scanf("%c", &board[board_i][board_j]);
                //printf("%c %i %i \n", board[board_i][board_j], board_i, board_j);
            }
        }
        
        int ki, kj;
        for (int board_i = 1; board_i < 8; board_i++) {
            for (int board_j = 1; board_j < 9; board_j++) {
                if (board[board_i][board_j] == 'k') {
                    ki = board_i;
                    kj = board_j;
                }
            }
        }
        int ways = check(ki, kj, board);
        printf("%i\n", ways);
    }
    
    //[pool drain];
    return 0;
}
