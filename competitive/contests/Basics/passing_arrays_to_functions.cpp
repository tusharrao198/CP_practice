#include <iostream>
#include <cmath>
using namespace std;

void printArray(int lst[] , int size_array);
int main(){
    int james[3]={1,2,3};
    int white[6] = {1221,3,332,2,233,1};
    printArray(white , 6);
}

void printArray(int lst[] , int size_array){
    for(int x=0 ; x<size_array ; x++){
        cout<<lst[x]<<endl;
    }
}