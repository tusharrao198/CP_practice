#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int a= 3;
    cout<< &a << endl;

    int *bPointer; 
    bPointer=&a;
    
    cout <<bPointer<<endl;
}
