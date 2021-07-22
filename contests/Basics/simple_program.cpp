#include <iostream>
using namespace std;
int main(){
    int x =1;
    int var;
    int sum=0;
    while (x<=5){
        cin >> var;
        sum+=var;
        x++;
    }
    cout << "Total equals to:"<<sum << endl;
    return 0;
}