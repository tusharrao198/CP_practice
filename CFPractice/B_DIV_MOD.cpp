#include<bits/stdc++.h>
using namespace std;

const long long mod=1e9+7;
int main(){
ios::sync_with_stdio(false);
cin.tie(0);

int t;
cin>>t;
while(t--){
    int l,r,a;
    cin>>l>>r>>a;
    if((r%a)==(a-1))cout<<(r/a)+(a-1)<<"\n";
    else{
        if(r-a>=l){
            cout<<((((r/a)*a)-1)/a)+(a-1)<<"\n";
        }
        else if((l%a)>(r%a)){
            cout<<((((r/a)*a)-1)/a)+(a-1)<<"\n";
        }
        else{

            cout<<(r/a)+(r%a)<<"\n";
        }
    }
}

return 0;
}
