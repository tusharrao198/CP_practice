#include <bits/stdc++.h>
#include <sstream>
#define ll long long
using namespace std;

int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll a, b, n1, n2;
        cin >> a >> b;
        n1 = a * b + a;
        n2 = a * b - a;
        if (b == 1)
        {
            cout << "NO" << endl;
        }
        else {
            cout << "YES" << endl;
            cout << n2 << " " << n1 << " " << 2 * a * b << endl;
        }
        
    }
}

