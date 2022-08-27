#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int ttcases;
    cin>>ttcases;
    int i;
    while(ttcases--)
    {
        int n,k;
        cin >> n >> k;
         if (k & 1) {
            cout << "YES" << endl;
            for (int i = 1; i <= n ; i += 2) {
                cout << i << ' ' << i + 1 << '\n';
            }
        } 
        else {
            bool check = true;
            for (int i = 2; i <= n; i += 2) {
                if (i % 4 != 0) {
                    if ((i + k) % 4 != 0) {
                        cout << "NO" << endl;
                        check = false;
                        break;
                    }
                }
            }
            if (!check) {
                continue;
            }
            cout << "YES" << endl;
            for (int i = 1; i <= n; i += 2) {
                if ((i + 1) % 4 == 0) {
                    cout << i << ' ' << i + 1 << '\n';
                } else {
                    cout << i + 1 << ' ' << i << '\n';
                }
            }
        }
    }
    return 0;
}