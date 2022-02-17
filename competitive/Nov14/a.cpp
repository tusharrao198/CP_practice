#include<bits/stdc++.h>
#include <stdlib.h>

using namespace std;



#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define mod 1000000007
#define abe(x) x.begin(), x.end()
#define dbe(x) x.rbegin(), x.rend()
#define inf 1e9 + 1;
#define linf 1e18 + 1
#define nline "\n"
#define ll long long int
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define ff first
#define ss second
#define ull unsigned ll



// typedef tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update > pbds; // find_by_order, order_of_key

#ifndef ONLINE_JUDGE
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#else
#define debug(x)
#endif
vector<int> g[300000+5];
multiset<ll> m;
void dfs(int i,vector<int> &vis,vector<ll> &v){
    m.insert(v[i]);
    vis[i] = 1;
    for(auto j: g[i]){
        if(!vis[j]){
            dfs(j,vis,v);
        }
    }
}


int main() {

    int T=1;
    cin>>T;
    while(T--){
        ll a,b;
        cin>>a>>b;
        cout<<a*a<<" "<<-b*b<<endl;
        


        

    }



}