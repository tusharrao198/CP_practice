#include <bits/stdc++.h>
using namespace std;

void setZeroes(vector<vector<int>> &A) {
    vector<int> row;
    vector<int> col;
    for (int i = 0; i < A.size(); i++)
    {
        for (int j = 0; j < A[i].size(); j++)
        {
            int val = A[i][j];

            if (val == 0)
            {
                if (count(col.begin(), col.end(), j) == 0)
                {
                    col.push_back(j);
                }
                if (count(row.begin(), row.end(), i) == 0)
                {
                    row.push_back(i);
                }
            }
        }
    }

    for (auto i : row)
    {
        for (int j = 0; j < A[i].size(); j++)
        {
            A[i][j] = 0;
        }
    }

    for (auto i : col)
    {
        for (int j = 0; j < A.size(); j++)
        {
            A[j][i] = 0;
        }
    }
}

// int main() {
//     int A;
//     cout << "mat";
//     setZeroes(A);
//     return 0;
// }
