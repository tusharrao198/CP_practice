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
ll INF = 1e18;

struct segtree {
    int n; vector<long long> t;
    void init(int nn){
        n = nn;
        t.assign(4*n + 7, 0);
    }

    void update(int v, int tl, int tr, int l, int r, long long add){
        if(l > r) return;
        if(l == tl && r == tr){
            t[v] += add;
        } else {
            int tm = (tl + tr)/2;
            update(2*v, tl, tm, l, min(r, tm), add);
            update(2*v + 1, tm +1, tr, max(l, tm + 1), r, add);
        }
    }

    long long get(int v, int tl, int tr, int pos){
        if(tl==tr) return t[v];
        int tm = (tl + tr)/2;
        if(pos <= tm) return t[v] + get(2*v , tl ,tm ,pos);
        else return t[v] + get(2*v + 1, tm + 1, tr, pos);
    
    }
    void update(int l, int r, long long add){
        update(1, 1, n, l, r, add);
    }
    long long get(int pos){
        return get(1, 1, n, pos);
    }
};

void solve(){
    int n,q; cin>>n>>q;
    segtree sum_a, sum_d, sum_dl;
    sum_a.init(n); sum_d.init(n);  sum_dl.init(n);
    while(q--){
        int t; cin>>t;
        if(t == 1){
            int l,r; ll a,d; cin>>l>>r>>a>>d;
            sum_a.update(l, r, a);
            sum_d.update(l,r,d);
            sum_dl.update(l, r, d*l);
        }
        else{
            int pos; cin>>pos;
            cout<< ( sum_a.get(pos) + (pos * sum_d.get(pos)) - sum_dl.get(pos) ) <<"\n";
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
