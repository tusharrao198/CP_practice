//            segment tree + min_query in range + add x in all elements in range

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;                       //for convenience

int mxn = 1e6 + 7 , INF = 1e10;             //some usable  limits
int n;                                      // size of main array 
vector<ll> a(mxn);                          // main array declared globally
vector<ll> t(4*mxn),lazy(4*mxn);            //segment  tree is t and lazy propagation is lazy
 

// call build(1,0,n-1); 
void build(int v, int tl, int tr) {          // pass (1,0,n-1)
 here initially while building tree
    if (tl == tr) {
        t[v] = a[tl];                         // main values to be stores in leaf nodes of tree
    } else {
        int tm = (tl + tr) / 2;
        build(v*2, tl, tm);
        build(v*2+1, tm+1, tr);
        t[v] = min(t[v*2], t[v*2 + 1]);        // minimum stores in node for min seg tree
    }
}

//you don't need to call
void push(int v) {            // propagating lazy into two of its children
    t[v*2] += lazy[v];
    lazy[v*2] += lazy[v];
    t[v*2+1] += lazy[v];
    lazy[v*2+1] += lazy[v];
    lazy[v] = 0;
}
 
// call update(1, 0, n-1, l, r, value_that_you_want_to_add)
void update(int v, int tl, int tr, int l, int r, int addend) {  //ADD x ( addend here ) to all element of array from indices l to r
    if (l > r)
        return;
    if (l == tl && tr == r) {
        t[v] += addend;
        lazy[v] += addend;
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), addend);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, addend);
        t[v] = min(t[v*2], t[v*2+1]);
    }
}
 
//call query(1, 0, n-1, l, r) 
int query(int v, int tl, int tr, int l, int r) {// find minimum element in array from indices l to r
    if (l > r)
        return -INF;
    if (l <= tl && tr <= r)
        return t[v];
    push(v);
    int tm = (tl + tr) / 2;
    return min(query(v*2, tl, tm, l, min(r, tm)), query(v*2+1, tm+1, tr, max(l, tm+1), r));
}
 
void fix(){         // fixing upper bounds  of all vectors according to input
    mxn = n+4;
    a.assign(mxn,0ll);
    t.assign(4*mxn, INF);
    lazy.assign(4*mxn,0ll);
}
 
void solve(){
    cin>>n;           // array size
    fix();             //fixing 
    //.... take inputs
}

int main() {

}