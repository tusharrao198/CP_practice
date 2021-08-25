#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n;
    cout << "Enter A number" << endl;
    cin >> n;
    int count_yes = 0;
    int count_no = 0;
    cout << pow(3, 0.5) << endl;
    if (n < 1)
    {
        cout << "Not prime" << endl;
    }
    else if (n == 2 || n == 3)
    {
        cout << n << " is prime" << endl;
    }
    else
    {
        for (int i = 2; i < pow(n, 0.5); i++)
        {
            if ((n % i) == 0)
            {
                count_no++;
                //cout<<n << " is not prime";
                break;
            }
            else
            {
                count_yes++;
            }
        }
        if (count_no == 0 && count_yes > 0)
        {
            cout << n << " is prime" << endl;
        }
        else
        {
            cout << n << " is not prime" << endl;
        }
    }
}