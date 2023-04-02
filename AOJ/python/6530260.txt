//
// 2022.04.25 13:50:17; Written by Shogo Kitada
//

#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (n); i++)
using ll = long long;
using namespace std;

int main(){
	
    string w, s;
    cin >> w;
    ll ans = 0;

    // スペースで区切られてるから、そのままループ回せば OK.
    while (cin >> s, s != "END_OF_TEXT") {

        rep(i, s.size()) {
            s.at(i) = tolower(s.at(i));
        }

        if (s == w) ans++;
    }

    std::cout << ans << std::endl;
}
