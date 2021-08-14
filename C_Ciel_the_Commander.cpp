/*  
*/
#include <bits/stdc++.h>
using namespace std;

#define rng(x) x.begin(), x.end()
#define pb push_back
#define ff first
#define ss second

typedef double db;
typedef long long ll;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<bool> vb;
typedef unsigned long long int lld;

/*-----------------------------Code begins----------------------------------*/
ll mod = 1e9 + 7;

const int mxn = 1e5 + 7;
int n;
vector<int> g[mxn];
vector<int> vis, siz, lev;

int dfs1(int v, int p){
    siz[v] = 1;
    for(auto u : g[v]){
        if(u!=p && vis[u]) siz[v]+=dfs1(u, v);
    }
    return siz[v];
}

int find_centroid(int v, int p, int tot){
    for(auto u : g[v]){
        if(u!=p && vis[u] && siz[u] > tot/2){
            return find_centroid(u,v,tot);
        }
    }
    return v;
}


void dfs(int v, int level){
    int tot = dfs1(v,-1);
    int c = find_centroid(v, -1, tot);

    vis[c] = 0; lev[c] = level;
    for(auto u : g[c]){
        if(vis[u]){
            dfs(u, level + 1);
        }
    }
}

void fix(){
    vis.assign(n+1,1);
    siz.assign(n+1,0);
    lev.assign(n+1,0);
}

void solve(){
    cin>>n; fix();
    for(int i=1; i<n; i++){
        int u,v; cin>>u>>v;
        u--; v--;
        g[u].pb(v);
        g[v].pb(u);
    }
    dfs(0,0);
    string ans = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for(int i=0; i<n; i++){
        cout<<ans[lev[i]]<<" ";
    }
    cout<<"\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int T = 1;
    //cin >> T;
    while (T--){
        solve();
    }
    return 0;
}
