#include <bits/stdc++.h>
// #include <sstream>
#define ll long long
// #define MAXN 100001
using namespace std;

ll solve(ll &n, ll &m)
{
    ll a, b, c = 0, eq;
    for (ll b = n; b > 1; b--)
    {
        eq = m - (m % b);
        for (ll a = b - 1; a < b && a >= 1; a--)
        {
            if (eq % a == 0)
            {
                c++;
            }
        }
    }
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
        ll n, m;
        cin >> n >> m;
        cout << solve(n, m) << "\n";
    }
}
