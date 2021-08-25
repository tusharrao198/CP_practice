#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

bool check(int &small, int &large, int &d)
{
    int count = small, new_b = large;
    if (count>1){
        while (count !=0){
            if (new_b> (d+1)){
                new_b = new_b - (d+1);
            }
            if (count ==1){
                break;
            }
            else if (new_b < (d+1)){
                return true;
            }
            count--;
        }
        if (count==0){
            return true;
        }
    }
    if (count ==1){
        if (abs(large-count)<=d ){
            return true;
        }
        else{
            return false;
        }
    }
}   

int main()
{
    int t;
    cin >> t;
    while (t--) {
        int r,b,d;
        cin >> r >> b >> d;
        if (d==0){
            if (r==b){
                cout << "YES" << endl;
            }
            else{
                cout << "NO" << endl;
            }
        }
        else{
            if ((r<b) && check(r,b,d)){
                cout << "YES" << endl;
            }
            else if ((r > b) && check(b,r, d))
            {
                cout << "YES" << endl;
            }
            else{
                cout << "NO" << endl;
            }
        }
    }
}