#include <bits/stdc++.h> 
using namespace std;

int gcd_binary(int a, int b){
    if (a==b){
        cout << "a==b" << endl;
        return a;
    }
    if (a==0){
        cout << "a==0" << endl;
        return b;
    }
    if ((a== 0) && (b==0)){
        cout << "a==b==0" << endl;
        return 0;
    }
    if (b==0){
        cout << "b==0" << endl;
        return a;
    }
    int commonMultiple = 1;
    while ((a%2==0) && (b%2==0)){
        cout << "both even" << endl;
        commonMultiple*=2;
        a/=2;
        b/=2;
    }
    // if a is even and b is odd.
    while (a%2 ==0){
        cout << "a is even" << endl;
        a/=2;
    }
    // if b is even.
    while (b%2==0){
        cout << "b is even" << endl;
        b/=2;
    }
    while ( (a%2!=0) && ( b%2!=0)){
        cout << "both odd" << endl;
        if (a>b){
            a= (a-b)/2;
            
        }
        else{
            b= (b-a)/2;
        }
    }
    return a*commonMultiple;


}
int main(){
    int a=12,b=48;
    //cin >> a >> b;
    cout << gcd_binary(a,b) << endl;
}
