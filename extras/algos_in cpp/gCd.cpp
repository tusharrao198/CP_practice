#include <iostream>
using namespace std;

int gCd(int a , int b){
    // base cases
    if (a==b){
        return a;
    }
    if (a==0){
        return b;
    }
    if (b==0){
        return a;
    }
    if (a>b){
        // cout << "a>b";
        return gCd(b, a%b);
    }
    else {
        // cout << "a<b";
        return gCd(a , b%a);
    }
}
int main(){
    int a = 13 , b = 2;
    cout << gCd(a, b) <<endl;
    return 0;
}
