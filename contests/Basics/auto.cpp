#include <iostream>
using namespace std;
// age average track
int main(){
    int age;
    int total=0;
    int num=0;
    cout << "enter age";
    cin >> age; 
    while (age!=-1){
        total+=age;
        num++;
        cout << "ente next age or -1 to quit";
        cin >> age;
    }
    int average;
    average = total/num;
    cout << average <<endl;
    return 0;

}