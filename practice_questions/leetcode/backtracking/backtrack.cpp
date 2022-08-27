#include <bits/stdc++.h>
using namespace std;

void solve(vector<int> &Arr, int n, set<int> &ans, vector<int> &cur, int idx) {
    if (idx > n) return;
    
    int sm = 0;
    for (int j= 0; j<cur.size(); j++) {
        sm+=cur[j];
    }
    // cout <<sm<<endl;
    ans.insert(sm);
    
    for (int i= idx; i<n; i++) {
        vector<int>::iterator it;
        it = find (cur.begin(), cur.end(), Arr[i]);
        if (it == cur.end()) { // if not found
            cur.push_back(Arr[i]);
            solve(Arr, n, ans, cur, idx);
            cur.pop_back();
        }
    }
    
}
int main(){
    set<int> ans;
    vector<int> cur;
    vector<int> Arr;
    int len = Arr.size();    
    solve(Arr, len, ans, cur, 0);
    return 0;
    
}