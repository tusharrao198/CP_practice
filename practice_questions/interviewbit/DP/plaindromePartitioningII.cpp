#include <bits/stdc++.h>
using namespace std;

int dp[502][502];

bool isPlaindrome(string str, int i, int j)
{
    while (i < j)
    {
        if (str[i] != str[j])
        {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int plaindromePartitioning(string str, int i, int j)
{
    if (i >= j)
    {
        return 0;
    }
    if (isPlaindrome(str, i, j))
    {
        return 0;
    }
    if (dp[i][j] != -1)
    {
        return dp[i][j];
    }
    int _min = INT_MAX;

    int left_partition, right_partition;

    for (int k = i; k <= j - 1; k++)
    {
        int temp_ans;
        if (dp[i][k] != -1)
        {
            left_partition = dp[i][k];
        }
        else
        {
            left_partition = plaindromePartitioning(str, i, k);
            dp[i][k] = left_partition;
        }

        if (dp[k + 1][j] != -1)
        {
            right_partition = dp[k + 1][j];
        }
        else
        {
            right_partition = plaindromePartitioning(str, k + 1, j);
            dp[k + 1][j] = right_partition;
        }

        temp_ans = left_partition + 1 + right_partition;

        if (temp_ans < _min)
        {
            _min = temp_ans;
        }
    }

    dp[i][j] = _min;
    return _min;
}

int Solution::minCut(string A)
{
    memset(dp, -1, sizeof(dp));
    int i = 0, j = A.length() - 1;
    return plaindromePartitioning(A, i, j);
}
