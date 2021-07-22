#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
class Solution
{
    vector<vector<int>> Solution::threeSum(vector<int> &A)
    {
        vector<vector<int>> ans;

        if (A.size() == 0)
        {
            return ans;
        }

        vector<pair<int, int>> v1(A.size());

        for (int i = 0; i < A.size(); i++)
        {
            v1[i] = {A[i], i};
        }

        sort(v1.begin(), v1.end());

        set<vector<int>> track;

        for (int i = 0; i < A.size(); i++)
        {
            int firset = v1[i].first;
            int j = i + 1;
            int k = A.size() - 1;
            while (j < k)
            {
                if (v1[j].first + v1[k].first + firset == 0)
                {
                    vector<int> v2({A[v1[i].second], A[v1[j].second], A[v1[k].second]});
                    sort(v2.begin(), v2.end());
                    if (track.find(v2) == track.end())
                    {
                        ans.push_back(v2);
                        track.insert(v2);
                    }
                    j++;
                    k--;
                }
                else if (v1[j].first + v1[k].first + firset < 0)
                {
                    j++;
                }
                else
                    k--;
            }
        }
        return ans;
    }
};
