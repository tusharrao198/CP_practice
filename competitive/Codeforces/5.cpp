#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

int check(int &a)
{
    int arr[5] = {1, 2, 3, 4, 5};
    int count =0, i =4;
    while (a!=0)
    {
        if (arr[i]<= a){
            a = a- arr[i];
            count++ ;
        }else{
            i-=1;
        }
    }
    return count;
}

int main()
{
    int a;
    cin >> a;
    cout << check(a) << endl;
}