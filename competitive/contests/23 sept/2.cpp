// gcd
// f(y, (y%x))
// f(48 ,12)
// f(48 ,0)

#include <iostream>
using namespace std;

int gcd(int x, int y){
    if (x==y){
        return x;
    }
    if (x==0){ return y;}
    if (y==0){ return x;}
    return gcd( y , x%y); 
}

int main(){
    cout << "Enter nos."<< endl;
    int a,b;
    cin >> a >> b;
    cout << "gcd of "<<a <<"& "<<b << "is "<< gcd(a, b) << endl;
     
}
    

