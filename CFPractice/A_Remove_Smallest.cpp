#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
#define pb push_back

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t;
    while (t--)
    {
        ll n, cnt;
        vector<int> arr;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            ll x;
            cin >> x;
            arr.pb(x);
        }

        sort(arr.begin(), arr.end());
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if(i!=j && arr[i]!=0 && arr[j]!=0 && abs(arr[i]-arr[j])<=1){
                    if (arr[i]<arr[j]){
                        arr[i]=0;
                    }
                    else if (arr[i]>arr[j]){
                        arr[j]=0;
                    }
                    else{
                        arr[i]=0;
                    }
                }
            }

        }

        cnt=0;
        for (int i = 0; i < n; i++){
            if (arr[i]!=0){
                cnt+=1;
            }
        }

        if (cnt==1){
            cout << "YES"<< endl;
        }else{
            cout << "NO"<< endl;
        }

    }
}
