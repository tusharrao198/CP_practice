#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, val;
    cin >> N;
    for (int i = 1; i <= 10; i++)
    {
        if (N % i == 0)
        {
            val = i;
        }
    }
    cout << val << endl;
}
