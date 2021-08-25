#include <iostream>
#include <cmath>
using namespace std;

int factorial(int n){
    if (n==1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}
int main(){
    cout << factorial(5) << endl;
}
