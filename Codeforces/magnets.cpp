#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

int check(int &n)
{
    int count = 1;
    string b, a;
    cin >> b;
    for (int i = 0; i < (n - 1); i++)
    {
        cin >> a;
        if (a!=b){
            count ++;
            b=a;
        }
    }
    return count;
}

int main()
{
    int n;
    cin >> n;
    cout << check(n) << endl;
}