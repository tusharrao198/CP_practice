#include <iostream>
using namespace std;

int tuna =20; // global variable can be used by any function.

int main(){
    double tuna = 69;  //local variables
    cout << ::tuna <<endl;   //:: means use global variable even if u had local variable known as Unary scope resolution
}    
