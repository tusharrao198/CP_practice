#include <bits/stdc++.h>
#include <sstream>
#define ll long long
#define MAXN 100001
using namespace std;

int mod = 1e9 + 7;

int pow_(int base, int exp)
{
    int result = 1;
    while (exp > 0)
    {
        if (exp & 1)
            result = ((long long)result * base) % mod;
        base = ((long long)base * base) % mod;
        exp >>= 1;
    }
    return result;
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
        cout << pow_(2, n - 1) << "\n";
    }
}
