#include <bits/stdc++.h>
#include <algorithm>
#define ll long long
using namespace std;

// no of subset with OR of element equals to tar;||

int static dp[502][502];

int help(vector<int> &nums, int k, int n, int val)
{
    if (n <= 0) return 0;

    if (dp[n][val]!=-1) return dp[n][val];
    
    int op1 = ((val | nums[n - 1]) == k) ? 1 + help(nums, k, n - 1, (val | nums[n - 1])) : help(nums, k, n - 1, (val | nums[n - 1]));
    
    int op2 = help(nums, k, n - 1, val);
    
    return dp[n][val] = op1 + op2;
}

int main() 
{
    memset(dp, -1, sizeof(dp));
    vector<int> nums = {2, 4, 4, 4};
    int k = 4;
    cout << help(nums, k, nums.size(), 0);
    return 0;
}