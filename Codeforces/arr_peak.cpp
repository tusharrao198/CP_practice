// #include <iostream>
// #include <math.h>
// #include <bits/stdc++.h>
// #define ll long long
// #define MAXN 10000
// using namespace std;
// #include <vector>

// int main()
// {
//     int t;
//     cin >> t;
//     while (t--)
//     {
//         ll n, k;
//         cin >> n >> k;
//         ll d[n+1];
//         for (int i=1; i<n+1; i++)
//         {
//             d[i] = i;
//         }
//         if (n<=2*k){
//             cout << "NO" << endl;
//             return 0;
//         }
//         else{
//             for (int j=0; j<k; j++){
//                 int tt;
//                 tt = d[-(2*j+1)];
//                 d[-(2 * j + 1)] = d[-(2*j+2)];
//                 d[-(2 * j + 2)] = tt;
//             }
//         }
//         for (int l=0; l<n; l++)
//         {
//             cout << d[l] << " ";
//         }
//     }
// }