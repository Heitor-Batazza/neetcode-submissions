# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.output = True
        
        if (not p and not q):
            self.output = True
        elif (p and not q) or (not p and q):
            return False
        elif (p.val != q.val):
            return False

        def dfs(p, q):
            if not p and not q:
                return [0, 0]
            if (p and not q) or (not p and q):
                return [1, 2]

            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            if left[0] != left[1] or right[0] != right[1]:
                self.output = False

            return [p.val, q.val]

        dfs(p, q)
        return self.output

        
        