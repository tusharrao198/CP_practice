#include<bits/stdc++.h>
#define int long long 
#define maxn 10009
#define pb push_back
using namespace std;
 
const int mod = 1e9+7;
const int INF = INT_MAX;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vii;

bool cmp(pii a , pii b ) {
    return ( a.second > b.second );
}
signed main(){
	ios::sync_with_stdio(); 
    cin.tie(0); cout.tie(0);
	int t ; 
    cin >> t; 
    while ( t -- )
    {
        vii a;
        for (int i = 0; i < 3; i++) {
            int x , y;
            cin >> x >> y;
            a.pb( { x , y } ) ;
        }
        sort(a . begin ( ) , a . end() , cmp);

        if (a[0].second == a[1].second) cout << setprecision(10) << fixed << abs(a[0].first - a[1].first) << '\n';
        else cout << 0 << '\n';
    }
}
