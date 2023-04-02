#define _USE_MATH_DEFINES
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<functional>
#include<cmath>
#include<iomanip>
using namespace std;
int main() {
	int i,n;
	double a,sum,squ,s;
	while (cin>>n) {
		if (n == 0)break;
		sum = 0; squ = 0;
		for (i = 0; i < n; i++) {
			cin >> a;
			squ += pow(a, 2);
			sum += a;
		}
		s = sqrt(squ / n - pow(sum / n, 2));
		cout << fixed << setprecision(6) << s << endl;
	}
	return 0;
}
