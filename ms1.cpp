// https : //iq.opengenus.org/number-of-subsets-with-given-or-value/
// Find the number of subsets with given Bitwise OR value
// We are given an array of size N and a value M, we have to find the number of subsets in the array having M as the Bitwise OR value of all elements in the subset.This can be solved using Dynamic Programming in polynomial time.

// Example :

// Input : arr[] = {2, 4, 4},
// M = 4 Output : 3

// The subsets are :
// {4}, {4}, { 4, 4 }


#include <bits/stdc++.h>
    using namespace std;
#define ll long long int
int main()
{
    ll arr[] = {2, 4, 4};
    ll m = 4;
    ll i, j, l = 3;

    int k = 1000;
    ll DP[l + 2][k + 2] = {0};
    DP[0][0] = -1;
    DP[1][0] = -1;
    //filling all possible BitwiseOR values in the first row
    for (i = 1; i < k + 2; i++)
    {  
        DP[0][i] = i - 1;
        DP[1][i] = 0;
    }
    //filling all the array elements in the first column
    for (i = 2; i < l + 2; i++)
    {
        DP[i][0] = arr[i - 2];
    }
    DP[1][1] = 1;
    //Filling the DP table
    //according to given logic
    for (i = 2; i < l + 2; i++)
    {
        for (j = 1; j < k + 2; j++)
        {
            if (DP[i - 1][j] != 0)
            {
                DP[i][((j - 1) | arr[i - 2]) + 1] =
                    DP[i - 1][((j - 1) | arr[i - 2]) + 1] + DP[i - 1][j];
            }
        }
        for (j = 1; j < k + 2; j++)
        {
            DP[i][j] = max(DP[i - 1][j], DP[i][j]);
        }
    }
    cout << DP<<endl;
    for (i = 0; i < l + 2; i++)
    {
        for (j = 0; j < k + 2; j++)
        {
            cout << DP[i][j] << "\t";
        }
        cout << "\n";
    }

    //counting the number of subsets
    //having given BitwiseOR value
    ll ans = DP[l + 1][m + 1];
    cout << "Number of subsets is:" << ans << "\n";
    return 0;
}
