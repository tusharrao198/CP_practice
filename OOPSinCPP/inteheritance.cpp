#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Student
{
    // string name; // private
    // below public all variables assigned are public

private:
    string name;

public:
    int age;
    bool gender;

    // Parameterised constructor
    Student(string s, int num, bool gen)
    {
        name = s;
        age = num;
        gender = gen;
    }

    //default constructor
    Student()
    {
        cout << "DEFAULT CONSTRUCTOR called" << endl;
    }

    //copy constructor
    Student(Student &s)
    {
        name = s.name;
        age = s.age;
        gender = s.gender;
    }

    // destructor
    ~Student()
    {
        cout << "DESTRUCTOR CALLED" << endl;
    }
    void setName(string s)
    {
        name = s;
    }

    string getName()
    {
        return name;
    }

    void printInfo()
    {
        cout << "NAME= " << name << endl;
        cout << "AGE= " << age << endl;
        cout << "GENDER= " << gender << endl;
    };

    bool operator==(Student &a)
    {
        if (name == a.name && age == a.age && gender == a.gender)
        {
            return true;
        }
        return false;
    }
};

int main()
{
    // Student arr[3];

    // for (int i=0; i<3;i++){
    //     cin >> arr[i].name;
    //     cin >> arr[i].age;
    //     cin >> arr[i].gender;
    // }

    // for (int i = 0; i < 3; i++)
    // {
    //     arr[i].printInfo();
    // }

    Student s1("KL", 12, 1);
    s1.printInfo();

    Student s2;

    Student s3 = s1; // copy constructor

    if (s3 == s1) 
    {
        cout << "SAME" << endl;
    }
    else
    {
        cout << "DIFFERENT" << endl;
    }
    return 0;
}
