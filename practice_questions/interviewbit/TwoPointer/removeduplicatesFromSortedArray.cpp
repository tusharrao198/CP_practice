#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
#define pb push_back


int removeDuplicates(vector<int> &A)
{
    int N = A.size();
    // int ans = 0;
    int cur = A[0];
    int cur_count = 1;
    int insert_at = -1;
    for (int i = 1; i < N; i++)
    {
        if (cur == A[i] && cur_count >= 2)
        {
            // ans++;
            if (insert_at == -1)
                insert_at = i;
        }
        else
        {
            if (cur == A[i])
                cur_count++;
            else
                cur_count = 1;
            cur = A[i];
            if (insert_at != -1)
            {
                A[insert_at] = cur;
                insert_at++;
            }
        }
    }
    // print_arr(A);
    if (insert_at != -1)
        A.erase(A.begin() + insert_at, A.end());
    // cout<<ans<<endl;
    // print_arr(A);
    return A.size();
}

// [ 1, 1, 1, 2, 2, 3 ];