// 2015-06-06  Runtime: 55 ms
// thanks to https://leetcode.com/discuss/38899/easy-short-c-recursive-solution
// Python总是超时, 试了二分法求最底层的叶节点个数还是超时 (Special Judge: very large tree) 😢

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int countNodes(struct TreeNode* root) {
    if (!root) return 0;
    int leftHeight = 0, rightHeight = 0;
    struct TreeNode *L = root, *R = root;
    while(L)
        L = L -> left, leftHeight++;
    while(R)
        R = R -> right, rightHeight++;
    if (leftHeight == rightHeight) return (1 << rightHeight) - 1; // 2 ^ rightHeight - 1
    return 1 + countNodes(root -> left) + countNodes(root -> right);
}