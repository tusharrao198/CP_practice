#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int rows, cols, val;
    cin >> rows >> cols;
    vector<vector<int>> mat;
    for (int r = 0; r < rows; r++)
    {
        vector<int> row;
        for (int c = 0; c < cols; c++)
        {
            cin >> val;
            row.push_back(val);
        }
        mat.push_back(row);
    }
    cout << mat[3][3];
    return 0;
}