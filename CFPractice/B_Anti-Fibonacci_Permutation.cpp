#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--){
		int n;
		cin>>n;
		
		vector <int> vec(n);
		
		for(int i=0;i<n;++i){
			vec[i] = i+1;
		}
		
		reverse(vec.begin(),vec.end());
		
		for(int i=n-1;i>=0;--i){
			for(int j=0;j<n;++j){
				cout<<vec[j]<<" ";
			}
			if(i != 0)
				swap(vec[i],vec[i-1]);
				
			cout<<endl;
		}
		
	}
	return 0;
}