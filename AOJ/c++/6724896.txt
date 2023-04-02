#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < n; i++)

using namespace std;

int main() {
    while (true) {
        int n;
        cin >> n;
        if (n == 0) break;
        vector<int> data(n);
        rep(i, n) {
            cin >> data[i];
        }
        double ave = accumulate(data.begin(), data.end(), 0) / n;
        int counter = 0;
        rep(i, n) {
            if (data[i] <= ave) counter++;
        }
        cout << counter << endl;
    }
}
