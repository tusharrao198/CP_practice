#include <bits/stdc++.h>
#include <sstream>
#include <algorithm>
#define ll long long
#define MAXN 100001
#define mod 1000000007
using namespace std;
#define pb push_back

void solve(int arr[], int n, int k)
{
    for (int i = 0; i < n; i += k)
    {
        int l = i;
         int r = min(i + k - 1, n - 1);
        while (l < r)
            swap(arr[l++], arr[r--]);
 
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t; // testcase
    while (t--) {

    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; ++i)
    {
      cin >> a[i];
    }

    int ones = 0, two = 0;


    for (int i = 0; i < n; ++i)
    {
      if (a[i] != i + 1)
      {
        ones = i;
        break;
      }
    }

    for (int i = 0; i < n; ++i)
    {
      if (a[i] == ones + 1)
      {
        two = i;
        break;
      }
    }
          while(ones<two){
          	swap(a[ones++],a[two--]);
          }

    for (int i = 0; i < n; ++i)
    {
      cout << a[i] << " ";
    }
    cout << endl;

  }
	return 0;
}