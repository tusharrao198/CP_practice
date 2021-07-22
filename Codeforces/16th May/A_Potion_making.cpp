#include <bits/stdc++.h>
#include <sstream>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        ll k;
        cin >> k;
        if (k == 100)
        {
            cout << 1 << '\n';
        }
        else
        {
            cout << 100 / __gcd(k, 100 - k) << '\n';
        }
    }
}
