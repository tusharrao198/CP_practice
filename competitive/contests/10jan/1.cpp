#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, one = 0, two = 0, lead = 0, max = 0;
    cin >> n;
    int arr[n][2];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[0][i] >> arr[1][i];
        one += arr[0][i];
        two += arr[1][i];
    }
    if (abs(two - one) > 0)
    {
        lead = abs(two - one);
    }
    if (one > two)
    {
        max = 1;
    }
    else
    {
        max = 2;
    }

    cout << max << " " << lead << endl;

    return 0;
}
