#include<bits/stdc++.h>
#include <iostream>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	while(t--)
	{
	   long long int n;
	   int count_=0;
	   cin>>n;
	   vector<long long >lst;
	   for(int i=0;i<n;i++)
	   {
	   	int cc;
	   	cin>>cc;
	   	lst.push_back(cc);
	   }
	   	for(int i=0;i<n-1;i++)
	   	{
	   		count_+=(lst[i+1]-lst[i]-1);
	   	}
	   	if(count_<3)
	   	{
	   		cout<<"YES\n";
	   	}
	   	else
	   	{
	   		cout<<"NO\n";
	   	}
   }
	return 0;
}
