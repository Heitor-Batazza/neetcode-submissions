# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def df(curr):
            if not curr:
                return 0

            left = df(curr.left)
            right = df(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        df(root)

        return self.res
        