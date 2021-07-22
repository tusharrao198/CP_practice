#include <iostream>
#include <bits/stdc++.h>
#include <math.h>
#include <algorithm>
#include <sstream>
#include <string>
#define ll long long
#define MAXN 100001
#include <vector>
using namespace std;

bool check(int &nn)
{
    string str;
    stringstream ss;
    ss << nn;
    ss >> str;
    if (str.find_first_not_of(str[0]) == string::npos)
    {
        return true;
    }
    return false;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int count = 0;
        int n;
        cin >> n;
        string str;
        stringstream ss;
        ss << n;
        ss >> str;
        int num = 1;
        for (int i = 0; i < str.length(); i++)
        {
            for(int k=0)
            if (str.length() == 1)
            {
                count++;
            }
            else
            {
                if (check(num))
                {
                    count++;
                }
            }
            num++;
        }
        cout << count << endl;
    }
}
