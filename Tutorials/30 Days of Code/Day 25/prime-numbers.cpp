#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int n;
        cin >> n;
        
        if (n == 1) {
            cout << "Not prime" << endl;
            continue;
        } else if (n == 2) {
            cout << "Prime" << endl;
            continue;
        }
        
        bool flag = true;
        for (int j = 2; j < sqrt(n)+1; j++) {
            if (n % j == 0) flag = false;
        }
        if (flag) {
            cout << "Prime" << endl;
        } else {
            cout << "Not prime" << endl;
        }
    }
     
    return 0;
}

