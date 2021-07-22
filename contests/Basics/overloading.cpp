#include <iostream>
#include <cmath>

using namespace std;

//function overloading means using same function for two different datatypes two times

void printNumber(int x){
    cout << "x"<<x<<endl;
}

void printNumber(float x){
    cout << "float x"<<x<<endl;
}
int main(){
    int a = 54;
    float b = 5.7689;
    printNumber(a);
    printNumber(b);
}
