#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
#define pb push_back

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t; // testcase
    while (t--)
    {
        ll n, min_, max_, diff;
        vector<int> arr;
        cin >> n;
        for (ll int i = 0; i < n; i++)
        {
            ll x;
            cin >> x;
            arr.pb(x);
        }
        cout << "min => " << min_ << endl;
    }
}