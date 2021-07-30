int Solution::searchMatrix(vector<vector<int> > &A, int B) {
    int n = A.size();
    int m = A[0].size();

    if (n == 0) return -1;

    ll int smallest = A[0][0], largest = A[n - 1][m - 1];

    if (x < smallest || x > largest) return -1;

    // set indexes for top right element
    
    int i = 0, j = m - 1;
    
    // cout << "in fun"<<endl;

    while (i < n && j >= 0)
        // cout << "SDF = "<< A[i][j] << endl;
        if (A[i][j] == B)
        {
            // cout << "n Found at "
            //         << i << ", " << j<<endl;
            return 1;
        }
        if (A[i][j] > B)
            j--;
        // Check if d[i][j] < B
        else
            i++;
    }
    return 0;
}
