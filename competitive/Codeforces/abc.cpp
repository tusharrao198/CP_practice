#include <iostream>
#include <math.h>
#include <bits/stdc++.h>
#define ll long long
#define MAXN 100001
using namespace std;
bool check(string s)
{
    int count1 = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(')
        {
            count1++;
        }
        else
        {
            count1--;
            if (count1 < 0)
            {
                return false;
            }
        }
    }
    if (count1 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    ll int T;
    cin >> T;
    while (T--)
    {
        string s;
        cin >> s;

        if (s[0] == s[s.length() - 1])
        {
            cout << "NO" << endl;
        }
        else
        {
            ll int count1 = 0;
            ll int i1 = 0;
            ll int i2 = 0;
            char a = s[0];
            char b = s[s.length() - 1];
            for (int i = 0; i < s.length(); i++)
            {
                if (s[i] == a)
                {
                    s[i] = '(';
                    i1++;
                }
                else if (s[i] == b)
                {
                    s[i] = ')';
                    i2++;
                }
            }

            string s1 = s;
            string s2 = s;
            for (int i = 0; i < s.length(); i++)
            {
                if (s1[i] != '(' && s1[i] != ')')
                {
                    s1[i] = '(';
                }
                if (s2[i] != '(' && s2[i] != ')')
                {
                    s2[i] = ')';
                }
            }
            
            if (check(s1) || check(s2))
            {
                cout << "YES" << endl;
            }
            else

            {
                cout << "NO" << endl;
            }
        }
    }

    return 0;
}