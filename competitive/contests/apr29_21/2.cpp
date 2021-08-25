#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m, k, x = 1, y=1, c=0;
        cin >> n >> m >> k;
        while (n != 1 || m != 1)
        {
            if (n!=1){
                n--;
                c= c+m;
            }
            else if (m != 1)
            {
                m--;
                c= c+n;
            }
        }
        if (n == 1 && m == 1)
        {
            if (c == k)
            {
                cout << "YES" << endl;
            }
            else
            {
                cout << "NO" << endl;
            }
        }

    }
}