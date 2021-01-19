#include <bits/stdc++.h>

using namespace std;

vector < unsigned long long int > pythagoreanTriple(unsigned long long int a){
    // Complete this function
    vector < unsigned long long int > v(3);
    unsigned long long int b;
    unsigned long long int c;
    
    if (a%2 == 1) {
        b = (a*a-1)/2;
        c = b+1;
        v[0] = a;
        v[1] = b;
        v[2] = c;
    }
    else {
        b = (a/2)*(a/2)-1;
        c = b+2;
        v[0] = a;
        v[1] = b;
        v[2] = c;
    }
    
    return v;
}

int main() { 
    unsigned long long int a;
    cin >> a;
    vector < unsigned long long int > triple = pythagoreanTriple(a);
    for (ssize_t i = 0; i < triple.size(); i++) {
        cout << triple[i] << (i != triple.size() - 1 ? " " : "");
    }
    cout << endl;
    

    return 0;
}
