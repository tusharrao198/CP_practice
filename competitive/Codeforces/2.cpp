#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <iterator>
#include <set>
using namespace std;

int check(int &a, int &b, int &c){
    int sum=0;
    for (int i=0; i<c; i++ ){
        sum += a * (i + 1);        
    }
    if (sum>=b){
        return (sum-b);
    }else{
        return 0;
    }

}

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    cout << check(a,b,c)<<endl;
}