#include <bits/stdc++.h>

using namespace std;

int birthdayCakeCandles(int n, vector <int> ar) {
    // Complete this function
    int best = 0;
    int count = 0;
    for (int ar_i = 0; ar_i < n; ar_i++) {
        if (ar[ar_i] > best) {
            count = 1;
            best = ar[ar_i];
        }
        else if (ar[ar_i] == best) {
            count += 1;
        }
    }
    
    return count;
}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for (int ar_i = 0; ar_i < n; ar_i++) {
       cin >> ar[ar_i];
    }
    int result = birthdayCakeCandles(n, ar);
    cout << result << endl;
    return 0;
}

