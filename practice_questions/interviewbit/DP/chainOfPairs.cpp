// https : //www.interviewbit.com/problems/chain-of-pairs/
#include <bits/stdc++.h>
using namespace std;

int solve(vector<vector<int>> &A)
{
    int n = A.size();
    vector<int> v;

    for (int i = 0; i < n; i++)
    {
        v.push_back(1);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (A[i][1] > A[j][1] && A[i][0] > A[j][1] && v[i] < v[j] + 1)
                v[i] = v[j] + 1;
        }
    }
    int max = 0;
    for (int i = 0; i < n; i++)
    {
        if (v[i] > max)
        {
            max = v[i];
        }
    }

    return max;
}
