//https://www.interviewbit.com/problems/sorted-insert-position/
int searchInsert(vector<int> &A, int B) {
    int l =0, r = A.size() -1;
    int mid;
    while (l<=r) {
        mid = (l+r)/2;
        if (A[mid]==B) {
            return mid;
        }else if (A[mid] > B) {
            r = mid-1;
        }else {
            l = mid + 1;
        }
    }
    return l;
}

