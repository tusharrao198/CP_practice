#include <bits/stdc++.h>
#include <sstream>
#define ll long long
using namespace std;

int main()
{

    ll num, t;
    cin >> t;
    while (t--)
    {
        ll a, b,lcm,y;
        cin >> a >> b;
        lcm = (abs(a * b) / __gcd(a, b))*2;
        y = lcm - a;
        if ((lcm % (a * b) == 0) && (a % (a * b) != 0) && (y % (a * b) != 0)){
            cout << "YES" << endl;
            cout << a << " " << y << " " << lcm << " " << endl;
        }
        else{
            cout << "NO"<<endl;
        }
    }
    

}
