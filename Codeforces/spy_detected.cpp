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
    while (t--)
    {
        int n, pos=-1, ele=0;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            int s;
            cin>> s;
            if (i==1){
                ele=s;
            }
            if (ele!=s){
                pos = i+1;
            }
        }
        cout << pos << endl;
    }
}
