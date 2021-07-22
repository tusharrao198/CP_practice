#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <iterator>
#include <set>
using namespace std;

int BorG(string &ss, int &len)
{
    set<int, greater<int>> s1;
    for (int i=0; i< len; i++){
        s1.insert(ss[i]);
    }
    return s1.size();
}  

int main()
{
    int len, val;
    string ss;
    cin >> ss;
    len = ss.length();
    val = BorG(ss, len);
    if (val%2==0){
        cout << "CHAT WITH HER!" << endl;
    }else{
        cout << "IGNORE HIM!" << endl;
    }
}