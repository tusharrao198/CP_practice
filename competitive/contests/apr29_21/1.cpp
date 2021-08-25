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
        long long int r, b, d;
        cin >> r >> b >> d;
        if (d == 0)
        {
            if (r == b)
            {
                cout << "YES" << endl;
            }
            else
            {
                cout << "NO" << endl;
            }
        }
        else if (r<=b) {
            if ((d+1)*r>=b){
                cout << "YES" << endl;
            }
            else{
                cout << "NO" << endl;
            }
        }
        else
        {
            if ((d+1)*b>=r){
                cout << "YES" << endl;
            }else{
                cout << "NO" << endl;
            }
           
        }
    }
}