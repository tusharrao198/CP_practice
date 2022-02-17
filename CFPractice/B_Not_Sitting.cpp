#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
#define pb push_back


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t; // testcase
    while (t--)
    {
        int n, m;
        if (true)
        {
            cin >> n >> m;
        }
        priority_queue<int, vector<int>, greater<int> > queue;
        bool check = true;
        int st = 0;
        if (check && st == 0)
        {
            for (int i = 0; i < n; i++)
            {  
                for (int j = 0; j < m; j++)
                {
                    int distance = max(j, m - j - 1) + max(i, n - 1 - i);
                    queue.push(distance);
                }
            }
        }
        while (!queue.empty())
        {
            cout << queue.top() << " ";
            queue.pop();
        }
        cout << endl;
    }
    return 0;
}