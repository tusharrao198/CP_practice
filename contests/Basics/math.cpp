#include <iostream>
#include <math.h>
#include <time.h>
#include <stdlib.h>
using namespace std;

int main(){
    int a = 20.6;
    int b;
    int y;
    cin>>b ;
    cout << ceil(20.6)<<endl;    
    cout << floor(a)<<endl;
    cout<< pow(2,3) <<endl;
    cout << sin(a)<<endl;
    cout << exp(1)<<endl;
    cout<< log(a)<<endl;
    cout << log10(2)<<endl;
    cout << fmod(20,2)<<endl;
    cout << fabs(-20.3)<<endl;    //mod
    //cout<<time(0);  
    srand(time(0));
    y = a + rand()%b;
    cout << y <<endl;
}