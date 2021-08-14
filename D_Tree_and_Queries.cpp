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

int n, m;

vector<int> g[mxn], qq[mxn];
vector<int> color, freq, ans, bit, query, subsize, is_big;

int pre(int r){ 
    int res = 0;
    for( ; r>=0; r = (r&(r+1)) - 1){
        res+=bit[r];
    }
    return res;
}

int sum(int l, int r){ 
    if( l > r) return 0;
    return pre(r) - pre(l-1);
}

void update(int pos, int delta){
    if(pos < 0) return;
    for(; pos < n; pos = (pos | (pos+1))){
        bit[pos] += delta;
    }
}

void add_color(int x){
    update(freq[x]-1,-1);
    freq[x]++;
    update(freq[x]-1, 1);
}
 
void remove_color(int x){
    update(freq[x]-1,-1);
    freq[x]--;
    update(freq[x]-1, 1);
}

void dfs_subsize(int v, int p){
    subsize[v] = 1;
    for(auto u : g[v]){
        if(u!=p){
            dfs_subsize(u,v);
            subsize[v]+=subsize[u];
        }
    }
}

void dfs_add_subtree(int v, int p){
    add_color(color[v]);
    for(auto u : g[v]){
        if(u!=p && !is_big[u]){
            dfs_add_subtree(u,v);
        }
    }
}

void dfs_remove_subtree(int v, int p){
    remove_color(color[v]);
    for(auto u : g[v]){
        if(u!=p && !is_big[u]){
            dfs_remove_subtree(u,v);
        }
    }
}

void dfs(int v, int p, int keep){
    int mx_siz = -1, bigchild = -1;
    for(auto u : g[v]){
        if(u!=p && mx_siz < subsize[u]){
            mx_siz = subsize[u];
            bigchild = u;
        }
    }
    for(auto u : g[v]){
        if(u!=p && u!=bigchild){
            dfs(u,v, 0);
        }
    }
    if(bigchild != -1) dfs(bigchild, v, 1), is_big[bigchild] = 1;
    dfs_add_subtree(v, p);

    for(auto id : qq[v]){
        ans[id] = sum(query[id], n-1);
    }

    if(bigchild!=-1) is_big[bigchild] = 0;
    if(!keep) dfs_remove_subtree(v,p);
}

void fix(){
    color.assign(n+1,0);
    query.assign(m+1 , 0);
    freq.assign(mxn,0);
    bit.assign(n + 1,0);
    ans.assign(m+1,0);
    subsize.assign(n+1,0);
    is_big.assign(n+1,0);
}

void solve(){
    cin>>n>>m; fix();
    for(int i=1; i<=n; i++){
        cin>>color[i];
    }
    for(int i=1; i<n; i++){
        int u,v; cin>>u>>v;
        g[u].pb(v);
        g[v].pb(u);
    }
    dfs_subsize(1,0);
    for(int i=1; i<=m; i++){
        int u,lim; cin>>u>>lim;
        query[i] = lim - 1;
        qq[u].pb(i);
    }
    dfs(1,0,1);
    for(int i=1; i<=m; i++){
        cout<<ans[i]<<"\n";
    }
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
