#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int lst[2][3] = {{2, 3, 4}, {8, 9, 10}};
    //cout << lst[0][1];
    for (int row = 0; row < 2; row++)
    {
        for (int col = 0; col < 3; col++)
        {
            cout << lst[row][col] << endl;
        }
        cout << endl;
    }
}
