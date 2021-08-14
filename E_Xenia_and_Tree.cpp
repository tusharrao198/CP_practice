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

int n,m;
vector<int> g[mxn];
vector<vector<int>> anc;
vector<int> depth,subsize, my_centroid, ans,vis;

void dfs_depth(int v, int p){
    anc[v][0] = p;
    for(auto u : g[v]){
        if(u!=p){
            depth[u] = depth[v] + 1;
            dfs_depth(u,v);
        }
    }
}

int jump_kth(int u, int jump){
    int bit = 0;
    while(jump > 0){
        if(jump & 1) u = anc[u][bit];

        jump >>= 1;
        bit++;
    }
    return u;
}

int get_lca(int a, int b){
    if(depth[a] > depth[b]) swap(a, b);
    int jump = depth[b] - depth[a];
    b = jump_kth(b, jump);

    if(a == b) return a;

    for(int bit=19; bit>=0; bit--){
        if(anc[a][bit] != anc[b][bit]){
            a = anc[a][bit];
            b = anc[b][bit];
        }
    }

    return anc[a][0];
}

int get_dist(int a, int b){
    int lca = get_lca(a,b);
    return depth[a] + depth[b] - 2*depth[lca];
}

int dfs_subsize(int v, int p){
    if(!vis[v]) return 0;
    subsize[v] = 1;
    for(auto u : g[v]){
        if(u != p){
            subsize[v] += dfs_subsize(u,v);
        } 
    }

    return subsize[v];
}

int find_centroid(int v, int p, int tot_size){
    for(auto u : g[v]){
        if(u!=p){
            if(vis[u] && subsize[u] > tot_size / 2){
                return find_centroid(u, v, tot_size);
            }
        }
    }

    return v;
}

void decompose(int init, int p){
    int tot_size = dfs_subsize(init, -1);
    int centroid = find_centroid(init, -1, tot_size);
    vis[centroid] = 0;
    my_centroid[centroid] = p;

    for(auto u : g[centroid]){
        if(vis[u]){
            decompose(u, centroid);
        }
    }
}

void fix(){
    anc.assign(n+1,vector<int>(20,0));
    depth.assign(n+1,0);
    subsize.assign(n+1, 0);
    vis.assign(n+1,1);
    my_centroid.assign(n+1,-1);
    ans.assign(n+1,n);
}

void solve(){
    cin>>n>>m; fix();
    for(int i=1; i<n; i++){
        int u,v; cin>>u>>v;
        u--; v--;
        g[u].pb(v);
        g[v].pb(u);
    }
    dfs_depth(0, 0);
    for(int bit = 1; bit < 20; bit++){
        for(int i=0; i<n; i++){
            anc[i][bit] = anc[anc[i][bit-1]][bit-1];
        }
    }
    decompose(0,-1);
    for(int i=0; i<n; i++){
        ans[i] = depth[i];
    }

    for(int i=0; i<m; i++){
        int tt, u; cin>>tt>>u;
        u--;
        if(tt == 1){
            ans[u] = 0;
            int up = my_centroid[u];
            while(up != -1){
                ans[up] = min(ans[up], ans[u] + get_dist(u,up));
                up = my_centroid[up];
            }
        }
        else{
            int up = my_centroid[u];
            while(up != -1){
                ans[u] = min(ans[u], ans[up] + get_dist(u,up));
                up = my_centroid[up];
            }
            cout<<ans[u]<<"\n";
        }
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
