#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int n, check=0;
        cin >> n;
        for (int i=0; i<n; i++)
        {   
            long long int s;
            cin >> s;
            if (sqrt(s)!=ceil(sqrt(s)))
            {
                check = 1;
            }
        }
        if (check ==1)
        { 
            cout << "YES" <<endl;
        }else if (check ==0)
        {
            cout << "NO" << endl;
        }
    }

}

