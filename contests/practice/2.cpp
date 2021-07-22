#include <iostream>
using namespace std;

int main(){
    int n;
    int a,b,c;
    int count=0;
    cin >>n;
    for (int x=0 ; x<n; x++){
        cin >> a >> b >> c;
        if ((a+b+c)>=2){
            count+=1;
        }
    }
    cout << count;
    return 0;
}