#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

void  check(int &n, string &s)
{
    int countA =0, countD=0;
    string sdf;
    for (int i=0; i<s.length(); i++){
        if (s[i]=='A'){
            countA++;
        }
        if (s[i]=='D'){
            countD++;
        }
    }
    if (countA==countD){
        cout << 'Friendship'<< endl;
    }
    if (countA>countD){
        cout << 'Anton'<<endl;
    }
    if (countA < countD)
    {
        cout << 'Danik'<<endl;
    }
}

int main()
{
    int n;
    string s;
    cin >> n;
    cin >> s;
    check(n, s);
}