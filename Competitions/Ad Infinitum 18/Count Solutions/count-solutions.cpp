#include <bits/stdc++.h>
#include <cmath>

using namespace std;

int countSolutions(unsigned long long int a, unsigned long long int b, unsigned long long int c, unsigned long long int d){
    // Complete this function
    int count = 0;
    unsigned long long int mx = min(c, (unsigned long long int) (sqrt(a*a+b*b)+a)/2);
    unsigned long long int my = min(d, (unsigned long long int) (sqrt(a*a+b*b)+b)/2);
    
    for (int x = 1; x < mx+1; x++) {
        double d = a*a+b*b-(2*x-a)*(2*x-a);
        if (d < 0) {
            break;
        }
        else {
            double y0 = sqrt(d);
            double r = y0 - floor(y0);
            if (r == 0) {
                unsigned long long int r0 = ((unsigned long long int) y0) + b;
                unsigned long long int r1 = b - ((unsigned long long int) y0);
                int flag = count;
                if (r0 % 2 == 0 & r0 >= 2 & r0 <= 2*my) {
                    count += 1;
                }
                if (r1 % 2 == 0 & r1 >= 2 & r1 <= 2*my) {
                    count += 1;
                }
                if (count - flag == 2) {
                    if (r0 == r1) {
                        count -= 1;
                    }
                }
        }
        }
    }
    
    return count;
}

int main() {
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        unsigned long long int a;
        unsigned long long int b;
        unsigned long long int c;
        unsigned long long int d;
        cin >> a >> b >> c >> d;
        int result = countSolutions(a, b, c, d);
        cout << result << endl;
    }
    return 0;
}
