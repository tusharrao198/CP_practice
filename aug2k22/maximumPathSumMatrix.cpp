// TO check : Not right code.
// https://www.geeksforgeeks.org/maximum-path-sum-matrix/
// https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1

//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:

    int max(int x, int y) {
        return (x>y) ? x : y;
    }

    int check(vector<vector<int>> &Matrix, int N, int i, int j) {
        if (i>=0 && i<N && j<N && j>=0) {
            return Matrix[i][j];
        }else {
            return -1;
        }
    }
    
    int solve(vector<vector<int>> &Matrix, int N, int l, int r){
        int sum = Matrix[l][r];
        // cout << sum<< endl;
        int i=l, j=r;
        while (i<N && j<N) {
            if (i==N-1) {
                return sum;
            }
            int a = check(Matrix, N, i+1, j);
            int b = check(Matrix, N, i+1, j-1);
            int c = check(Matrix, N, i+1, j+1);
            
            if (a>b && a>c) {
                sum+=a;
                i++;
            }else if (b>a && b>c) {
                sum+=b;
                i++;
                j--;
            }else if (c>a && c>b) {
                sum+=c;
                i++;
                j++;
            }
            else {
            
            }
        }
        return sum;
    }

    int maximumPath(int N, vector<vector<int>> Matrix)
    {
        int ans = Matrix[0][0];
        int i = 0, j = 0;
        for (int f=0; f<N; f++) {
            if (ans < Matrix[0][f]) {
                ans = Matrix[0][f];
                j=f;
            }
        }
        
        return solve(Matrix, N, i, j);        
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        vector<vector<int>> Matrix(N, vector<int>(N, 0));
        for(int i = 0;i < N*N;i++)
            cin>>Matrix[(i/N)][i%N];
        
        Solution ob;
        cout<<ob.maximumPath(N, Matrix)<<"\n";
    }
    return 0;
}
// } Driver Code Ends