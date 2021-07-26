vvi g;
vi color;
 
bool check_bipartite(int n){
    bool is_bipartite = true;
    queue<int> q;
    for(int i=0; i<n; i++){
        if(color[i]==-1){
            q.push(i);
            color[i]=0;
            while(!q.empty()){
                int u = q.front(); q.pop();
                for(auto v : g[u]){
                    if(color[v]==-1){
                        color[v] = color[u]^1;
                        q.push(v);
                    }
                    else{
                        is_bipartite &= color[v] != color[u];
                    }
                }
            }
        }
    }
    return is_bipartite;
}