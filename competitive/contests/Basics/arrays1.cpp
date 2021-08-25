#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int tuna[5] = {20,12,3,323,32};
    int sum = 0;

    for (int x=0; x<5;x++){
        sum+=tuna[x];
        cout<<sum<<endl;
    }
    cout<<"sum"<<sum<<endl;
}