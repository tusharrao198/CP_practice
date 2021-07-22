#include <bits/stdc++.h>
using namespace std;

// string ans_(int a, int b, int c)
// {
//     int count = 1, count1 = 1;
//     if (c == 1)
//     {
//         return "YES";
//     }

//     if (((a % 2) == 0) && ((b % 2) != 0))
//     {
//         while ((a % 2) == 0)
//         {
//             a = a / 2;
//             count++;
//         }
//         if (count >= c)
//         {
//             return "YES";
//         }
//     }

//     if (((a % 2) != 0) && ((b % 2) == 0))
//     {
//         while ((b % 2) == 0)
//         {
//             b = b / 2;
//             count1++;
//         }
//         if (count1 >= c)
//         {
//             return "YES";
//         }
//     }

//     if (((a % 2) == 0) && ((b % 2) == 0))
//     {
//         while ((a % 2) == 0)
//         {
//             a = a / 2;
//             count++;
//         }
//         while ((b % 2) == 0)
//         {
//             b = b / 2;
//             count1++;
//         }
//         if ((count >= c) || (count1 >= c))
//         {
//             return "YES";
//         }
//     }
//     else if (((a % 2) != 0) && ((b % 2) != 0))
//     {
//         if ((c) >= 1)
//         {
//             return "YES";
//         }
//     }
//     else
//     {
//         return "NO";
//     }
// }
int main()
{
    int n;
    cin >> n;
    int arr[n][3];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[0][i] >> arr[1][i] >> arr[2][i];

        cout << arr[0][i] << " " << arr[1][i] << " " << arr[2][i] << "  " << endl;

        // cout << ans_(arr[0][i], arr[1][i], arr[2][i]) << endl;
    }
    return 0;
}
