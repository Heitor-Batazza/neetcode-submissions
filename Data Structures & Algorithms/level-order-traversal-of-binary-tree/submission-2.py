# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        def dfs(i, root):

            if not root:
                return
            if i == len(res):
                res.append([])
            
            res[i].append(root.val)
            dfs(i + 1, root.left)
            dfs(i + 1, root.right)  

        dfs(0, root)
        return res
        