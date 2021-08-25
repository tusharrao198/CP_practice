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

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll int count = 0;
        ll int n;
        cin >> n;
        ll int arr[n];
        for (int i = 0; i < n; i++)
        {
            ll int sd;
            cin >> sd;
            arr[i] = sd;
        }
        for (int j = 0; j < n; j++)
        {
            for (int k = 1; k < n; k++)
            {
                if (j < k)
                {
                    if (arr[k] - arr[j] == (k - j))
                    {
                        count++;
                    }
                }
            }
        }
        cout << count << endl;
    }
}
