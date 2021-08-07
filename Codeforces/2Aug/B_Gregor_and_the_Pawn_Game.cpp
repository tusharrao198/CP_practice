#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        char mat[2][n];
        string s1, s2;
        cin >> s1 >> s2;
        for (int i = 0; i < n; i++)
        {
            mat[0][i] = s1[i] - '0';
        }
        for (int i = 0; i < n; i++)
        {
            mat[1][i] = s2[i] - '0';
        }
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (mat[1][i] == 1)
            {
                if (mat[0][i] == 0)
                {
                    count++;
                }
                else if (mat[0][i - 1] == 1)
                {
                    count++;
                    mat[0][i - 1] = 0;
                }
                else if (mat[0][i + 1] == 1)
                {
                    count++;
                    mat[0][i + 1] = 0;
                }
            }
        }
        cout << count << endl;
    }
    return 0;
}