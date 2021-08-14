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

struct data
{
    int ones, zeros;
};

struct segtree
{
    vector<data> t;
    vector<int> is_lazy;
    int n;

    data reset(data d1){
        data res;
        res.ones = d1.zeros;
        res.zeros = d1.ones;
        return res;
    }

    data make_data(){
        data res;
        res.zeros = 1;
        res.ones = 0;
        return res;
    }

    data combine(data d1, data d2){
        data res;
        res.ones = d1.ones + d2.ones;
        res.zeros = d1.zeros + d2.zeros;
        return res;
    }

    void init(int nn){
        n = nn; data ini = make_data();
        t.assign(4*n + 7, ini);
        is_lazy.assign(4*n + 7, 0);
    }

    void build(int v, int tl, int tr){
        if (tl == tr) return;
        int tm = (tl + tr) / 2;
        build(2*v, tl, tm);
        build(2*v + 1, tm + 1, tr);
        t[v] = combine(t[2*v], t[2*v + 1]);
    }
    void push(int v){
        if (!is_lazy[v]) return;
        t[2*v] = reset(t[2*v]);
        t[2*v + 1] = reset(t[2*v + 1]);
        is_lazy[2*v] ^= 1;
        is_lazy[2*v + 1] ^= 1;
        is_lazy[v] = 0;
    }
    void update(int v, int tl, int tr, int l, int r){
        if (l > r) return;
        if (l == tl && r == tr){
            t[v] = reset(t[v]);
            is_lazy[v] ^= 1;
        }
        else{
            push(v);
            int tm = (tl + tr) / 2;
            update(2*v, tl, tm, l, min(r, tm));
            update(2*v + 1, tm + 1, tr, max(tm + 1, l), r);
            t[v] = combine(t[2*v], t[2*v + 1]);
        }
    }

    int getkth(int v, int tl, int tr, int k){
        if(k > t[v].ones) return -1;
        if (tl == tr) return tl; 
        push(v);
        int tm = (tl + tr) / 2;
        if (t[2 * v].ones < k){
            return getkth(2*v + 1, tm + 1, tr, k - t[2*v].ones);
        } else{
            return getkth(2*v, tl, tm, k);
        }
    }

    void update(int l, int r){
        update(1, 0, n - 1, l, r);
    }
    int getkth(int k){
        return getkth(1, 0, n - 1, k);
    }
};

void solve()
{
    int n, q;
    cin >> n >> q;
    segtree seg;
    seg.init(n);
    seg.build(1, 0, n - 1);
    while (q--){
        int t;
        cin >> t;
        if (t == 1)
        {
            int l, r;
            cin >> l >> r;
            seg.update(l, r - 1);
        } else{
            int k;
            cin >> k; k++;
            cout << seg.getkth(k) << "\n";
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
    while (T--)
    {
        solve();
    }
    return 0;
}
