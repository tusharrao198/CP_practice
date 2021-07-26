const int mxn = 600007;
const ll INF = 1e18;

vector<vector<pl>> g;
vl small_dist;

void dijkstra(int n, ll root){
    priority_queue< pl,vector<pl>, greater<pl> > q;
   	small_dist.assign(n,INF);
    small_dist[root]=0;
    vb vis(n,0);
    q.push({0,root});

    while(!q.empty()){
        pl u = q.top(); q.pop();
        if(u.ff != small_dist[u.ss] || vis[u.ss]==1) continue;
        vis[u.ss] = 1;

        for(auto v : g[u.ss]){
            if(small_dist[v.ff] > small_dist[u.ss] + v.ss){
                small_dist[v.ff] = small_dist[u.ss] + v.ss ;
                q.push({small_dist[v.ff], v.ff});
            }
        }
    }
}