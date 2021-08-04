#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
#define pb push_back


int static dp[502][502];


bool isPlaindrome(string str, int i, int j) {
    while (i<j) {
        if (str[i]!=str[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int plaindromePartitioning(string str, int i, int j)
{
    if (i>=j) {
        return 0;
    }
    if (isPlaindrome(str, i, j)) {
        return 0;
    }
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    int _min = INT_MAX;

    int left_partition, right_partition;

    for (int k= i; k<=j-1; k++) {
        int temp_ans;
        if (dp[i][k] !=-1) {
            left_partition = dp[i][k];
        }
        else {
            left_partition = plaindromePartitioning(str, i, k);
            dp[i][k] = left_partition;
        }

        if (dp[k + 1][j] != -1)
        {
            right_partition = dp[k+1][j];
        }
        else
        {
            right_partition = plaindromePartitioning(str, k+1, j);
            dp[k + 1][j] = right_partition;
        }

        temp_ans = left_partition + 1+ right_partition;

        if (temp_ans<_min) {
            _min = temp_ans;
        }
    }

    dp[i][j] = _min;
    return _min;
}

int main()
{
    memset(dp, -1, sizeof(dp));
    string s;
    // s = "ababb";
    s = "nitin";
    int i = 0, j = s.length()-1;
    int ans = plaindromePartitioning(s, i, j);
    cout << "l = " << ans<<endl;


}
