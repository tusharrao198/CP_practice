const int mxn =2e5 +7;
int ancestor[mxn][20];
vi g[mxn];
vi depth(mxn,0);
 
void dfs(int u, int p){
    ancestor[u][0]=p;
    for(auto v : g[u]){
        if(v!=p){
            depth[v] =depth[u]+1;
            dfs(v,u);
        }
    }
}
int lca(int a, int b){
    if(depth[a]!=depth[b]){
        if(depth[a] > depth[b]){
            swap(a,b);
        }
        int k =depth[b]-depth[a];
        for(int i=19; i>=0; i--){
            if(k&(1<<i)){
                b=ancestor[b][i];
            }
        }   
    }
    if(a==b){return a;}
    for(int i=19; i>=0; i--){
        if(ancestor[a][i]!=ancestor[b][i]){
            a=ancestor[a][i];
            b=ancestor[b][i];
        }
    }
    return ancestor[a][0];
}
 
int distance(int a, int b){
    return depth[a]+depth[b] - 2* depth[lca(a,b)];
}
 
int get_kth(int node, int k) {
        if(depth[node] < k) {
            return -1;
        }
        for(int j = 19; j >= 0; j--) {
            if(k >= (1 << j)) {
                node = ancestor[node][j];
                k -= 1 << j;
            }
        }
        return node;
}
void solve(){
    for(int i=1; i<n; i++){
        int u,v; cin>>u>>v;
        g[u].pb(v);
        g[v].pb(u);
    }
    dfs(1,1);
    for(int k=1; k<20; k++){
        ancestor[1][k]=1;
        for(int i=2; i<=n; i++){
            ancestor[i][k] = ancestor[ancestor[i][k-1]][k-1];
        }
    }
}