# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0

        def dfs(node: TreeNode, maxval: int):
            if not node:
                return
            if node.val>=maxval:
                self.count+=1
            dfs(node.left, max(node.val,maxval))
            dfs(node.right, max(node.val,maxval))

        dfs(root, root.val)
        return self.count
