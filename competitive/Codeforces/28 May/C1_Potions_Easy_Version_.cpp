#include <bits/stdc++.h>
#include <sstream>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        ll x , c;
        cin >> x;
        ll ans[]={};
        for (ll int i = 0; i < x; i++)
        {
            cin >> c;
            ans[i] = c;
        }
        sort(ans, ans + x, greater<int>());
        // cout << ans;

        ll tot=0, count=0;
        for (ll j = 0; j < x; j++)
        {
            tot = tot+ans[j];
            if (tot<0){
                break;
            }
            count++;
        }
        cout << count<<'\n';             
    }
}
