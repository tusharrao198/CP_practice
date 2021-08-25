#include <bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    
	ll x = 1;
	cin >> x;
	ll n, k;
//	unordered_map<ll, ll> m;
	unordered_map<ll, ll> ks;
	while (x--){
		ks.clear();
		cin >> n >> k;
		ll a[n];
		for(ll i = 0; i < n; i++){
			cin >> a[i];	
//			m[a[i]]++;
			ks[a[i]] = k;
		}
		for(ll i = 0; i < n; i++){
			if(ks[a[i]] > 0){
				cout << k - ks[a[i]] + 1 << " ";
				ks[a[i]]--;
			}
			else{
				cout << 0 << " ";
			}
		}
		cout << endl;
	}
	
}
