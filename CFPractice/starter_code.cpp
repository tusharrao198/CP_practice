#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
#define pb push_back\

void solve(){
    ll n; cin >> n;
        string s, t;
        cin >> s >> t; 
        for (int i = 0; i < (n - 1); i++){
            if(s[i]!=t[i]){
                if(t[i] == 'a'){
                    cout << "NO\n";
                    return;
                }
                if(t[i] == 'b' && (s[i] != 'a')){
                    cout << "NO\n";
                    return;
                }
                if(t[i]=='c' && (s[i]!='b' || )){
                    cout << "NO\n";
                }
            }
        }
        if(s[n-1] ==t[n-1]) cout << "YES\n";
        else
            cout << "NO\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t; // testcase
    while (t--)
    {
        solve();
    }
}
