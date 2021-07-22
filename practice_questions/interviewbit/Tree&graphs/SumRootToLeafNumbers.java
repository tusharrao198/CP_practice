/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) {
 *      val = x;
 *      left=null;
 *      right=null;
 *     }
 * }
 */
public class Solution {

    public int solve(TreeNode root, int sum_) {
        if (root == null) {
            return 0;
        }
        sum_ = (((sum_%1003)*10)%1003) + root.val;
        
        if (root.left ==null && root.right ==null) {
            return sum_%1003;
        }

        int l = solve(root.left, sum_)%1003;
        int r = solve(root.right, sum_)%1003;

        return l+r;
    }
    public int sumNumbers(TreeNode A) {
        int sum_ = 0;
        int ans = solve(A, sum_);
        return ans % 1003;

    }
}

