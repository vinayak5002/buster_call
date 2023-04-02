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
	double a, b, c, C, S, L, h,pi;
	pi = M_PI;
	cin >> a; cin >> b; cin >> C;
	double X = C*pi / double(180);
	S = (0.5)*a*b*sin(X);
	c = sqrt(pow(a, 2) + pow(b, 2) - 2 * a*b*cos(X));
	L = a + b + c;
	h = 2 * S / a;
	cout << fixed<<setprecision(6)<< S << endl;
	cout << fixed << setprecision(6) << L << endl;
	cout << fixed << setprecision(6) << h << endl;
	return 0;
}
