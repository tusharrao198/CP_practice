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
ll INF = INT_MAX;
struct segtree {
    vector<ll> t,lazy;
    int n;
    void init(int nn){
        n= nn;
        t.assign(4*n + 7, 0);
        lazy.assign(4*n + 7, 0);
    }
    void push(int v){
        t[2*v]|=lazy[v];
        lazy[2*v]|=lazy[v];
        t[2*v + 1]|=lazy[v];
        lazy[2*v +1]|=lazy[v];
        lazy[v] = 0;
    }
    void update(int v, int tl, int tr, int l, int r, ll add){
        if(l > r) return;
        if(l==tl && r==tr){
            t[v]|=add;
            lazy[v]|=add;
            //cout<<l<<":"<<r<<" "<<t[v]<<"\n";
        } else {
            push(v);
            int tm = (tl + tr)/2;
            update(2*v, tl, tm, l, min(r, tm), add);
            update(2*v +1 , tm +1 ,tr, max(tm+1, l), r, add);
            t[v] = t[2*v] & t[2*v + 1];
        }
    }

    ll getand(int v, int tl, int tr, int l, int r){
        if(l > r) return INF;
        if(l<=tl && r>=tr){
            return t[v];
        }
        push(v);
        int tm = (tl + tr)/2;
        return ((getand(2*v, tl, tm, l, min(r, tm))) & (getand(2*v +1 , tm +1 ,tr, max(tm+1, l), r)));
    }

    void update(int l, int r, ll add){
        update(1, 0, n-1, l, r, add);
    }
    ll getand(int l, int r){
        return getand(1, 0, n-1, l, r);
    }
};

void solve(){
    int n,q; cin>>n>>q;
    segtree seg; seg.init(n);
    while(q--){
        int t; cin>>t;
        if(t == 1){
            int l,r; ll add; cin>>l>>r>>add;
            seg.update(l, r -1, add);
        }
        else{
            int l,r; cin>>l>>r;
            cout<< seg.getand(l,r - 1) <<"\n";
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
