#include <iostream>
#include <math.h>
#include <bits/stdc++.h>
#define ll long long
#define MAXN 10000
using namespace std;
#include <vector>

int main()
{
    int n;
    cin >> n;
    ll sum_ = 0;
    ll max_ = 0;  
    for (int i=0; i<n; i++)
    {
        ll s;
        cin >> s;
        sum_ = sum_ + s;
        max_ = max(s, max_);
    }
    if (sum_ %2==0 && (2*max_) <=sum_){
        cout << "YES" <<endl;
        return 0;
    }
    cout << "NO" <<endl;
    return 0;
}