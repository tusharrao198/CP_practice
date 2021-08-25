#include <iostream>
#include <string>
using namespace std;

int main(){
    int n;
    string w;
    int s;
    int x;
    cin >>n;
    for (int x=0 ; x<n; x++){
        cin >> w;
        if (w.length()>10){
            s = w.length()-2;
            x = w[0]+to_string(s)+w[-1];
            cout << x;
        }
        else{
            cout << w;
        }
    }
    
    return 0;
}