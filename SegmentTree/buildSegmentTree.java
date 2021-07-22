// https://leetcode.com/problems/range-sum-query-mutable/solution/

int[] tree;
int n;
public NumArray(int[] nums) {
    if (nums.length > 0) {
        n = nums.length;
        tree = new int[n * 2];
        buildTree(nums);
    }
}
private void buildTree(int[] nums) {
    for (int i = n, j = 0;  i < 2 * n; i++,  j++)
        tree[i] = nums[j];
    for (int i = n - 1; i > 0; --i)
        tree[i] = tree[i * 2] + tree[i * 2 + 1];
}
// Complexity Analysis
//
// Time complexity : O(n)

// Time complexity is O(n), because we calculate the sum of one node during each iteration of the for loop.
// There are approximately 2n2n nodes in a segment tree.
// This could be proved in the following way: Segmented tree for array with nn elements has nn leaves
// (the array elements itself). The number of nodes in each level is half the number in the level below.

// So if we sum the number by level we will get:
//
// n + n/2 + n/4 + n/8 + .......... + 1 ≈2n
//
// Space complexity : O(n)
//
// We used 2n extra space to store the segment tree.



// -------------------------------------------------------------------------------------------------------------
// for update

void update(int pos, int val) {
    pos += n;
    tree[pos] = val;
    while (pos > 0) {
        int left = pos;
        int right = pos;
        if (pos % 2 == 0) {
            right = pos + 1;
        } else {
            left = pos - 1;
        }
        // parent is updated after child is updated
        tree[pos / 2] = tree[left] + tree[right];
        pos /= 2;
    }
}

// Complexity Analysis
//
// Time complexity : O(log n)
//
// Algorithm has O(log n) time complexity, because there are a few tree nodes with range that include
// ith array element, one on each level. There are \log(n)log(n) levels.
//
// Space complexity : O(1)

// -------------------------------------------------------------------------------------------------------------

