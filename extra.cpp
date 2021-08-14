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

/-----------------------------Code begins----------------------------------/
ll mod = 1e9 + 7;
const int mxn = 1e5 + 7;

vector<int> g[mxn];
vector<int> color, in_time, out_time, flat_tree;
int timer = 1;

int n, m, N, sz, cur_ans = 0;
vector<int> freq,ans, bit;

struct data {
    int l,r,idx, lim;
}query[mxn];

void dfs(int v, int p){
    in_time[v] = timer;
    flat_tree[timer] = color[v];
    timer++;
    for(auto u : g[v]){
        if(u!=p) dfs(u,v);
    }
    out_time[v] = timer;
    flat_tree[timer] = color[v];
    timer++;
}

bool comp(struct data &d1, struct data &d2){
    int b1 = d1.l / sz;
    int b2 = d2.l / sz;
    if(b1!=b2) return b1 < b2;
    else return d1.r < d2.r;
}

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

void add(int x){
    int ini = freq[x]/2;
    freq[x]++;
    int fin = freq[x]/2;
    if(ini!=fin){
        update(ini-1,-1);
        update(fin -1, 1);
    }
}
void remove(int x){
    int ini = freq[x]/2;
    freq[x]--;
    int fin = freq[x]/2;
    if(ini!=fin){
        update(ini-1,-1);
        update(fin -1, 1);
    }
}

void mo(){
    sort(query+1, query + m + 1, comp);
    int l =1, r=0;
    for(int i=1; i<=m; i++){
        while(l < query[i].l) remove( flat_tree[l++]);
        while(l > query[i].l) add( flat_tree[--l]);
        while(r < query[i].r) add( flat_tree[++r]);
        while(r > query[i].r) remove( flat_tree[r--]);
        ans[query[i].idx] = sum(query[i].lim - 1, n - 1);
    }
}

void fix(){
    N = 2*n;
    sz = sqrt(N) + 1;
    color.assign(n+1,0);
    in_time.assign(n+1,0);
    out_time.assign(n+1,0);
    flat_tree.assign(N+2,0);

    freq.assign(mxn,0);
    bit.assign(n + 1,0);
    ans.assign(m+1,0);
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
    dfs(1,0);
    for(int i=1; i<=m; i++){
        int u,lim; cin>>u>>lim;
        query[i].l = in_time[u];
        query[i].r = out_time[u];
        query[i].idx = i;
        query[i].lim = lim;
    }
    mo();
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
