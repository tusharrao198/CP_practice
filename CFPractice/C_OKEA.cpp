#include <bits/stdc++.h>
using namespace std;
long long  a[100100], n, t, x, y, z, k, b[100100];
int main() {
	string s, ss;
	cin >> t;
	while(t--){
		cin >> k >> n;
		bool ok = 1;
		a[0] = b[0] = 1;
		for(int i = 1; i < n; i++){
			a[i] = a[i - 1] + k;
			b[i] = b[i - 1] + a[i];
			if(b[i] % (i + 1))
			{
				cout<<i<<'\n';
				ok = 0;
			}
		} 
		if(!ok)
			cout << "NO" << endl;
		else {
			cout << "YES" << endl;
			for(int i = 1; i <= k; i++){
				for(int j = 1; j <= n; j++){
					cout << (j - 1) * k + i << ' ';
				}
				cout << endl;
			}
		}
	}
	return 0;
}