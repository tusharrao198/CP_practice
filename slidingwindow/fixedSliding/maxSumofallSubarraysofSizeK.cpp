// https : //leetcode.com/problems/maximum-average-subarray-i/submissions/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double findMaxAverage(vector<int> &nums, int k)
    {
        int n = nums.size();
        int i = 0;
        int j = 0;
        int sum = 0;
        double max_sum_avg = INT_MIN;

        while (j < n)
        {
            sum += nums[j];

            if ((j - i + 1) < k)
            {
                j++;
            }

            else if ((j - i + 1) == k)
            {

                if (sum > max_sum_avg)
                {
                    max_sum_avg = sum;
                }

                sum -= nums[i];
                i++;
                j++;
            }
        }
        return max_sum_avg / k;
    }
};