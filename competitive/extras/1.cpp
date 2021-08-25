#include <iostream>
using namespace std;

int main()
{
    int *ptr;
    int x;
    ptr = &x;
    *ptr = 0;
    *ptr += 5;

    (*ptr)++;

    cout << x << *ptr;
    return 0;
}