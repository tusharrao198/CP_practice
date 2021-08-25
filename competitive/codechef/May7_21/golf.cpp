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
        ll n, x, k;
        cin >> n >> x >> k;
        if (x%k==0)
        {
            cout << "YES" << endl;
        }
        else if ((n+1-x)%k==0)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}

