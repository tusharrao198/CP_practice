#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int lst[9];
    cout << "Element  -  Value" << endl;
    for (int x=0 ; x<9; x++){
        lst[x] = 99;
        cout<< x <<"   ---------  "<< lst[x]<< endl;
    }
    lst[11] = 12;
    cout << lst[11];
    cout << test(std::vector<int>(x, x + sizeof x / sizeof x[0]));

}
