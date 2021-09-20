#include <bits/stdc++.h>
using namespace std;
#define int long long int
#define fast                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);
#define endl "\n"

bool isOdd(int num)
{
    if (num % 2)
        return true;
    return false;
}

signed main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif // ONLINE_JUDGE
    fast int tt = 1;
    cin >> tt;
    int mod = 1e9 + 7;
    for (int loop = 1; loop <= tt; loop++)
    {
        int n, k;
        cin >> n >> k; // Subset size should be k

        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        int dp[2][k + 1];
        // dp[0][i] -> count of odd element is even and size of the subset is i
        // dp[1][i]-> count is odd elements is odd and size of the subset is i

        for (int i = 0; i <= k; i++)
            dp[0][i] = dp[1][i] = 0;

        // Base case
        dp[0][0] = 1;
        // count of odd elements is even(i.e. equal to zero) and set size is 0

        for (int i = 0; i < n; i++)
        { // i denotes the array element

            for (int j = k; j >= 1; j--)
            { // j denotes the subset size

                // Note it is important to check dp[1][j-1] and dp[0][j-1] whether they are non zero or not. Because we can form a subset of size j only when a subset of size j - 1 already exists which is denoted if there is a non zero value

                if (isOdd(arr[i]))
                {
                    if (dp[1][j - 1] != 0)
                        dp[0][j] += dp[1][j - 1] * arr[i];

                    if (dp[0][j - 1] != 0)
                        dp[1][j] += dp[0][j - 1] * arr[i];
                }
                else
                {
                    if (dp[0][j - 1] != 0)
                        dp[0][j] += dp[0][j - 1] * arr[i];

                    if (dp[1][j - 1] != 0)
                        dp[1][j] += dp[1][j - 1] * arr[i];
                }

                dp[0][j] %= mod;
                dp[1][j] %= mod;
            }
        }

        // cout << "Sum of products of subsets of size K with the frequency of odd elements as even is: " << dp[0][k] << endl;
        cout << dp[0][k] << endl;
    }
    return 0;
}