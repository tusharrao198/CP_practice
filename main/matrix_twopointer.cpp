#include <bits/stdc++.h>
// #include <sstream>
#define ll long long
#define pb push_back
#define MAXN 100001
using namespace std;

int search_(vector<vector<int>> &d, ll int &n, ll int &m, ll int &x)
{
    if (n == 0) return -1;
    ll int smallest = d[0][0], largest = d[n - 1][m - 1];
    if (x < smallest || x > largest) return -1;
    // set indexes for top right element
    int i = 0, j = m - 1;
    cout << "in fun"<<endl;
    while (i < n && j >= 0)
    {
        cout << "SDF = "<< d[i][j] << endl;
        if (d[i][j] == x)
        {
            cout << "n Found at "
                 << i << ", " << j<<endl;
            return 1;
        }
        if (d[i][j] > x)
            j--;
        // Check if d[i][j] < x
        else
            i++;
    }
    cout << "n Element not found"<<endl;
    return 0;
}

int main()
{
    ll t;
    cin >>t;
    while (t--)
    {
        vector<vector<int>> dd;
        ll val, cols, rows, x; 
        cin >> rows >> cols >> x;
        for (int i = 0; i < rows; i++)
        {
            vector<int> temp;
            for (int j = 0; j < cols; j++)
            {
                cin >> val;
                temp.pb(val);
            }
            dd.pb(temp);           
        }
        for (int i=0;i<rows;i++){
            for(int k=0; k<cols;k++){
                cout<<dd[i][k]<<" ";
            }
            cout << endl;
        }
        cout << "RUN " <<endl;
        search_(dd, rows, cols, x);        
    }
    return 0;
}


/* Searches the element x in d[][]. If the
element is found, then prints its position
and returns true, otherwise prints "not found"
and returns false  in O(n)*/