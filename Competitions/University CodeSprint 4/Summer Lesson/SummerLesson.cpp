#include <bits/stdc++.h>

using namespace std;

vector<int> howManyStudents(int m, vector <int> c) {
    // Return an array denoting the number of students taking each class.
    vector<int> result(m);
    for (int result_i = 0; result_i < result.size(); result_i++) {
        result[result_i] = 0;
    }
    for (int c_i = 0; c_i < c.size(); c_i++) {
        result[c[c_i]] += 1;
    }
    
    return result;
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector<int> c(n);
    for(int c_i = 0; c_i < n; c_i++){
       cin >> c[c_i];
    }
    vector<int> result = howManyStudents(m, c);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? " " : "");
    }
    cout << endl;

    return 0;
}

