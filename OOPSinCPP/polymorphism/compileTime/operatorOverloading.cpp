#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Complex
{
private:
    int n1, n2;

public:
    // Parameterised constructor
    Complex(int a=0, int b=0)
    {
        n1 = a;
        n2 = b;
    }


    bool operator == (Complex &x)
    {
        if (n1 == x.n1 && n2==x.n2){
            return true;
        }
        return false;
    }

    Complex operator + (Complex &x)
    {
        Complex res;
        res.n1 = n1 + x.n1; 
        res.n2 = n2 + x.n2;
        return res;
    }

    void display(){
        cout << n1 <<" <-> " <<n2<<endl;
    }
};

int main()
{
    Complex s1(5,7), s2(1,3);
    Complex s3;
    bool flag;
    flag = s1 == s2;
                     




    return 0;
}
