#include <bits/stdc++.h>
#include <sstream>
#define ll long long
#define MAXN 100001
using namespace std;

int main()
{
    ll num, t;
    cin >> t;
    num = 100;
    while (t--)
    {
        ll x, a, b, ans;
        cin >> x >> a >> b;
        ans = a + ((num-x)*b); 
        cout << ans*10 << endl;
    }
}
