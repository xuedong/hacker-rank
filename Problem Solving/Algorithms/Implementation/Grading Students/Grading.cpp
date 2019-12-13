#include <bits/stdc++.h>

using namespace std;

vector<int> solve(vector<int> grades){
    // Complete this function
    int n = grades.size();
    vector<int> result(n);
    for (int grades_i = 0; grades_i < n; grades_i++) {
        if (grades[grades_i] <= 37) {
            result[grades_i] = grades[grades_i];
        }
        else {
            int higher = ((grades[grades_i] / 5) + 1) * 5;
            //printf("%d\n", higher);
            if (higher - grades[grades_i] <= 2) {
                result[grades_i] = higher;
            }
            else {
                result[grades_i] = grades[grades_i];
            }
        }   
    }
    
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> grades(n);
    for (int grades_i = 0; grades_i < n; grades_i++) {
       cin >> grades[grades_i];
    }
    vector<int> result = solve(grades);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? "\n" : "");
    }
    cout << endl;
    
    return 0;
}
