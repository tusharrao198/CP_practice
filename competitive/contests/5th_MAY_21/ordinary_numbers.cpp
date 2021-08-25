#include <bits/stdc++.h>
#include <sstream>
#define ll long long
#define MAXN 100001
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll int num = 0, count = 0, ones;
        string str, ones_str;
        cin >> str;
        for (ll int i = 0; i < str.length(); i++)
        {
            ones_str = ones_str + '1';
        }
        stringstream add_one(ones_str);
        add_one >> ones;
        stringstream convert(str);
        convert >> num;
        count = count + (num / ones);
        count = count + ((str.length() - 1) * 9);
        cout << count << endl;
    }
}
