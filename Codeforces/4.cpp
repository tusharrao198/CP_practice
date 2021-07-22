#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

int check(int &a, int &b)
{
    int len;
    string ss;
    ss = to_string(a);
    len = ss.length();
    
    for (int i = 0; i < b; i++)
    {
        cout << "SS => "<<ss<<endl;
        cout << "ASDF => "<< to_string(ss[len - 1])<< endl;
        if (to_string(ss[len - 1]) == "0")
        {
            cout <<"AAA = > "<< ss<< "and "<<a<<endl;
            a = a / 10;
        }
        else
        {
            a -= 1;
        }
        ss = to_string(a);
    }
    return a;
}

int main()
{
    int a, b, len;
    cin >> a >> b;
    cout << check(a, b) << endl;
}