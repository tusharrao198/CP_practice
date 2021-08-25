#include <bits/stdc++.h>
using namespace std;
#include <iostream>
#include <algorithm>
// #include <vector>

vector<vector<int>> performOps(vector<vector<int>> &A)
{
    vector<vector<int>> B;
    B.resize(A.size());
    for (int i = 0; i < A.size(); i++)
    {
        B[i].resize(A[i].size());
        for (int j = 0; j < A[i].size(); j++)
        {
            B[i][A[i].size() - 1 - j] = A[i][j];
        }
    }
    return B;
}

int main()
{

    cout << "Hwlllo" << endl;
}
