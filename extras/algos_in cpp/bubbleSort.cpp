#include <iostream>
#include <bits/stdc++.h> 
using namespace std;


void swap(int &a , int &b){
    int c = a;
    a = b;
    b = c;
}
// optimized bubble sort  O(n**2)
void bubbleSort(int arr[], int n){
    int i , j;
    int rounds =0;
    for (i=0; i<n; i++){
        int flag = false;
        rounds++;
        for (j=0; j < n-i-1; j++){
            if (arr[j] > arr[j+1]){
                flag = true;
                swap(arr[j], arr[j+1]);    
            }
        }
        if (flag==false){
            break;
        }
    }
    cout << "rounds " << rounds << endl;
}

void printArray(int arr[], int n){
    int i;
    for (i =0; i <n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main(){
    int arr[] = {5,2,4,3,6};  
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    cout << "Sorted list =  "; 
    printArray(arr, n);
    return 0;
}
