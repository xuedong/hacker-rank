#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int rd, rm, ry;
    int dd, dm, dy;
    
    cin >> rd >> rm >> ry;
    cin >> dd >> dm >> dy;
    
    if (ry > dy) {
        cout << 10000 << endl;
    } else if (ry == dy && rm > dm) {
        cout << 500 * (rm-dm) << endl;
    } else if (ry == dy && rm == dm && rd > dd) {
        cout << 15 * (rd-dd) << endl;
    } else {
        cout << 0 << endl;
    }
    
    return 0;
}

