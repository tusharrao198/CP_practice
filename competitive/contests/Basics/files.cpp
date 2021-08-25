#include <iostream>
#include <fstream>
using namespace std;

int main(){

    // ofstream my_file_object;
    // my_file_object.open("my_file.txt");
    // my_file_object<< "My name is HArry Potter.\n Can you tell me something about the cj=hamber of secrets\n";
    // my_file_object.close();

    ofstream tips_file("tips.txt");
    
    if (tips_file.is_open()){
        cout << "file opened"<<endl;
    }
    else{
        cout<<"you shit "<<endl;
    }
    tips_file << " Learn C++\n";
    tips_file.close();
}