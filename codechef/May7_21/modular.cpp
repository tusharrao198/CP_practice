#include <bits/stdc++.h>
#include <sstream>
#define ll long long
#define MAXN 100001
// #define ans 1000000007
using namespace std;

bool check_(ll &m, ll &a, ll &b)
{
    ll lhs, rhs;
    lhs = (m % a) % b;
    rhs = (m % b) % a;
    if (lhs == rhs)
    {
        return true;
    }
    return false;
}

ll solve(ll &n, ll &m)
{
    ll a, b, c = 0;
    for (ll a = 1; a < n; a++)
    {
        for (ll b = a + 1; b <= n; b++)
        {
            if (a < b && b == m)
            {
                if (check_(m, a, b))
                {
                    c++;
                }
            }
            else if (a < b && a == m)
            {
                if (check_(m, a, b))
                {
                    c++;
                }
            }
            else if (a < b && m < a)
            {
                if (check_(m, a, b))
                {
                    c++;
                }
            }
            else if (a < b && b < m)
            {
                if (check_(m, a, b))
                {
                    c++;
                }
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
