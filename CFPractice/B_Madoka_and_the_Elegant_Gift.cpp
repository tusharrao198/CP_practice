#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	ll mm;
	cin >> mm;
	while(mm--)
	{
		ll n, m;
		cin>>n>>m;
		vector<string> a(n);
		for(int i=0;i<n;i++)
		{
		 string b;
		 cin >> b;
		 a[i]=b;
		}
		bool bool_check=true;
		for(int i=0;i<n-1;i++)
		{
            for(int j=0;j<a[i].length()-1;j++)
            {
                int sum_val=(a[i][j]-'0')+(a[i+1][j]-'0')+(a[i][j+1]-'0')+(a[i+1][j+1]-'0');
                if(sum_val==3)
                {
                    bool_check=false;
                    break;
                }
            
            }
            if(!bool_check)
            break;
		}
		if(bool_check) cout << "YES" << endl;
		else cout << "NO" << endl;
		
	}
	return 0;
}