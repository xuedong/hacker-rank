#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    map<string, int> phoneBook;
    
    for (int i=0; i<n; i++) {
        string name;
        cin >> name;
        int number;
        cin >> number;
        phoneBook[name] = number;
    }
    
    string entry;
    while (cin >> entry) {
        map<string, int>::iterator it;
        it = phoneBook.find(entry);
        if (it != phoneBook.end()) {
            cout << entry << "=" << phoneBook[entry] << endl;
        }
        else {
            cout << "Not found" << endl;
        }
    }
    
    return 0;
}

