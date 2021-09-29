#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Student
{
private:
    string name;

public:
    int age;
    bool gender;

    void func(){
        cout << "No arguments"<<endl;
    }

    void func(int x)
    {
        cout << "int arguments" << endl;
    }

    void func(double x, double y)
    {
        cout << "double arguments" << endl;
    }

};

int32_t main()
{
    Student obj;
    obj.func();
    obj.func(2);
    obj.func(2,3);

    return 0;
}
