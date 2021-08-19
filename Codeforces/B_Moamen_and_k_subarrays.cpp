#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define all(v) (v).begin(), (v).end()
#define prec(n) fixed<<setprecision(n)

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef tuple<int,int,int> iii;
typedef vector <ii> vi;
typedef vector <vector<int>> vvi;
typedef unsigned long long int ull ;
typedef map<char,int> mci;
const int MOD=1e9+7;
const char nl = '\n';
const double pi = 2*acos(0.0);


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt; cin>>tt;
    while(tt--){
        int n,k; cin>>n>>k;
        vector <int> a(n);
        for(auto &item:a) cin>>item;
        vector<int> b =a;
        sort(all(b));
        map<int,int> check_;
        int max_=n-k+1;
        for(int i=0;i<n-1;i++)   check_[b[i]]=b[i+1];
        int tmp=0;
        for(int i=0;i<n-1;i++){
            int p = check_[a[i]];
            if(a[i+1]!=p){
                tmp++;
            }
        }
        if(b[n-1]!=a[n-1]) tmp++;
        if(tmp>k) cout<<"No\n";
        else cout<<"Yes\n";
    }
    return 0;
}