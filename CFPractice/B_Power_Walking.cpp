#include <bits/stdc++.h>
#define ll long long
#define pb push_back

using namespace std;
int main() 
{
	ll t;
    cin >> t;
    while(t--)
    {
        ll n,a;
        cin>>n;
        vector<ll> ans;
        unordered_map<ll,ll> umap;
        for(ll i=0;i<n;i++)
        {
            cin>>a;
            umap[a]++;
        }
        ll val=0;
        for(auto &el:umap)
        {
            if(el.second>1)
            {
                val+=(el.second-1);
            }
        }
        ll answer = n;
        for(ll i=0;i<n;i++)
        {
            if(val>0)
            {
                ans.pb(answer);
                answer--;
                val--;
            }
            else{
                ans.pb(answer);
            }
            
        }
        for(ll i=n-1;i>=0;i--)
        cout<<ans[i]<<" ";
        cout<<"\n";
    }
}
    
