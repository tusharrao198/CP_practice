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
    ll sum, pref, suf, ans;
};

struct segtree
{
    vector<data> t;
    vector<ll> len, lazy;
    vector<bool> is_lazy;
    int n;

    data reset(ll new_val)
    {
        data res;
        res.sum = new_val;
        res.pref = res.suf = res.ans = max(0ll, new_val);
        return res;
    }
    void init(int nn)
    {
        n = nn;
        t.assign(4 * n + 7, reset(0));
        len.assign(4 * n + 7, 0);
        lazy.assign(4 * n + 7, -1);
        is_lazy.assign(4 * n + 7, false);
    }

    void build(int v, int tl, int tr)
    {
        if (tl == tr)
        {
            len[v] = 1;
        }
        else
        {
            int tm = (tl + tr) / 2;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
            len[v] = tr - tl + 1;
        }
    }

    data combine(data d1, data d2)
    {
        data res;
        res.sum = d1.sum + d2.sum;
        res.pref = max(d1.pref, d1.sum + d2.pref);
        res.suf = max(d1.suf + d2.sum, d2.suf);
        res.ans = max(max(d1.ans, d2.ans), d1.suf + d2.pref);
        return res;
    }
    void push(int v)
    {
        if (!is_lazy[v]) return;
        
        t[2 * v] = reset(lazy[v] * len[2 * v]);
        t[2 * v + 1] = reset(lazy[v] * len[2 * v + 1]);

        lazy[2 * v] = lazy[v];
        lazy[2 * v + 1] = lazy[v];

        is_lazy[2 * v] = true;
        is_lazy[2 * v + 1] = true;
        is_lazy[v] = false;
    }
    void update(int v, int tl, int tr, int l, int r, ll new_val)
    {
        if (l > r)
            return;
        if (l == tl && r == tr)
        {
            t[v] = reset(new_val * len[v]);
            lazy[v] = new_val;
            is_lazy[v] = true;
        }
        else
        {
            push(v);
            int tm = (tl + tr) / 2;
            update(2 * v, tl, tm, l, min(r, tm), new_val);
            update(2 * v + 1, tm + 1, tr, max(tm + 1, l), r, new_val);
            t[v] = combine(t[2 * v], t[2 * v + 1]);
        }
    }

    data getmax(int v, int tl, int tr, int l, int r)
    {
        if (l > r)
            return reset(0ll);
        if (l <= tl && r >= tr)
        {
            return t[v];
        }
        push(v);
        int tm = (tl + tr) / 2;
        return combine((getmax(2 * v, tl, tm, l, min(r, tm))), (getmax(2 * v + 1, tm + 1, tr, max(tm + 1, l), r)));
    }

    void update(int l, int r, ll new_val)
    {
        update(1, 0, n - 1, l, r, new_val);
    }
    ll getmax(int l, int r)
    {
        data med = getmax(1, 0, n - 1, l, r);
        return med.ans;
    }
};

void solve()
{
    int n, q;
    cin >> n >> q;
    segtree seg;
    seg.init(n);
    seg.build(1, 0, n - 1);
    while (q--)
    {
        int l, r;
        ll new_val;
        cin >> l >> r >> new_val;
        seg.update(l, r - 1, new_val);
        cout << seg.getmax(0, n - 1) << "\n";
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
