#include <bits/stdc++.h>
using namespace std;

const int mxn = 1e6 + 7; //declare your maximum limit for n

int n;  // size of array 

// strictly use 0 based indexing for this implementation , 1 based indexing has different transition

vector<int> bit(mxn,0); // this BIT stores updated prefix sum

int pre(int r){   // getting prefix sum from 0 -> r using bit transition
    int ans = 0;
    for( ; r>=0; r = (r&(r+1)) - 1){
        ans+=bit[r];
    }
    return ans;
}

int sum(int l, int r){  // getting sum from l to r
    return pre(r) - pre(l-1);
}

void update(int pos, int delta){ // updating all prefixes that are affected by update using bit transition
    if(pos == - 1) return;
    for(; pos<n; pos = (pos | (pos+1))){
        bit[pos] += delta;
    }
}

void ini(vector<int> &a){
    int n = a.size();
    for(int i=0; i<n; i++){
        update(i, a[i]);
    }
}

void solve(){
    // ini(a);
}