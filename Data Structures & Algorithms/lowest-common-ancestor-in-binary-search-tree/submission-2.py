# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        def helper(root: TreeNode) -> (int, TreeNode):
            if not root:
                return (0, None)
            found_l, lnode = helper(root.left)
            found_r, rnode = helper(root.right)
            if found_l and found_r:
                return (2, root)
            sm = found_l + found_r + (1 if root.val == p.val or root.val == q.val else 0)
            if sm == 0:
                return (0, None)
            elif root.val != p.val and root.val != q.val:
                return (sm, lnode or rnode)
            else:
                return (sm, root)

        a,b =  helper(root)
        return b
        