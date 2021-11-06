#include <bits/stdc++.h>

using namespace std;

// Complete the decibinaryNumbers function below.
const int dmax = 300000;
const int digits = 10;
const int powers = 20;

vector<vector<long>> v(dmax, vector<long>(powers));
vector<long> c(dmax);

// Complete the decibinaryNumbers function below.
void preCompute() {
  // Compute the number of duplicates for each value, number of digits.
  for (int i = 0; i < dmax; i++) {
    v[i][0] = i < digits;

    for (int j = 1; j < powers; j++) {
      // Duplicates is sum of all shorter numbers duplicates for each digit.
      for (int k = 0; k < digits; k++) {
        int value = i - k * (1 << j);

        // Exit if using digit creates number larger than target value.
        if (value < 0)
          break;
        v[i][j] += v[value][j - 1];
      }
    }
  }

  // Calculate the absolute offset for the first duplicate of each number.
  for (int i = 1; i < dmax; i++) {
    c[i] = v[i - 1][powers - 1] + c[i - 1];
  }
}

long decibinaryNumbers(long x) {
  long result = 0;
  auto l = upper_bound(c.begin(), c.end(), x - 1) - 1;
  int value = l - c.begin();
  long offset = (x - 1) - *l;

  // Find each digit.
  for (int i = powers - 1; i >= 1; i--) {
    int power = 1 << i;

    // Find the digit which takes us closest to offset.
    for (int digit = 0; digit < digits; digit++) {
      // Calculate value of remaining digits.
      int v1 = value - digit * power;

      // If index is less than duplicates for remainder we have our digit.
      if (offset < v[v1][i - 1]) {
        result += digit;
        value -= power * digit;
        break;
      }

      // Subtract number of duplicates for this digit from offset.
      offset -= v[v1][i - 1];
    }

    result *= 10;
  }

  // Whatever is left must be the last digit.
  result += value;
  // cout << x << ":" << result << ":" << l - c.begin() << endl;

  return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    preCompute();

    for (int q_itr = 0; q_itr < q; q_itr++) {
        long x;
        cin >> x;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        long result = decibinaryNumbers(x);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}

