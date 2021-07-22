#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream file("my_file.txt");
    string a;
    string b;
    string c;
    while(file >> a >> b >> c){
        cout << a << "," << b << "," << c << endl;
    }
}
