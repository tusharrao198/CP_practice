//https://www.hackerrank.com/challenges/variable-sized-arrays/problem?h_r=next-challenge&h_v=zen
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, q, size, i, j, a;
    cin >> n >> q;
    vector<vector<int>> nvec;
    for (int x = 0; x < n; x++)
    {
        cin >> size;
        vector<int> ivec;
        for (int d = 0; d < size; d++)
        {
            cin >> a;
            ivec.push_back(a);
        }
        nvec.push_back(ivec);
    }
    for (int r = 0; r < q; r++)
    {
        cin >> i >> j;
        cout << nvec[i][j] << endl;
        ;
    }

    return 0;
}