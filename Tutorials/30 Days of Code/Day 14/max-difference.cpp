#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
    private:
    vector<int> elements;
  
  	public:
  	int maximumDifference;

	// Add your code here
    Difference(vector<int> elements) {
        this->elements = elements;
    }

    void computeDifference() {
        maximumDifference = 0;
        int len = this->elements.size();
        for (int i = 0; i < len-1; i++) {
            for (int j = i+1; j <= len-1; j++) {
                int difference = abs(this->elements[j]-this->elements[i]);
                if (difference > maximumDifference) {
                    maximumDifference = difference;
                }
            }
        }
    }
}; // End of Difference class

int main() {
    int N;
    cin >> N;
    
    vector<int> a;
    
    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;
        
        a.push_back(e);
    }
    
    Difference d(a);
    
    d.computeDifference();
    
    cout << d.maximumDifference;
    
    return 0;
}

