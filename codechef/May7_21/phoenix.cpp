#include <bits/stdc++.h>
#include <sstream>
#define ll long long
#define MAXN 100001
// #define ans 1000000007
using namespace std;

ll check(ll &n)
{
    ll c;
    c = log(n) / log(2);
    return c;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        cout << check(n) << "\n";
    }
}
