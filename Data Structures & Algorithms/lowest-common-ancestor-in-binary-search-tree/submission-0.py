# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.output = None

        def searchNode(root, p, q):
            if not root:
                return
            elif p.val > root.val and q.val > root.val:
                searchNode(root.right, p, q)
            elif p.val < root.val and q.val < root.val:
                searchNode(root.left, p, q)
            else:
                self.output = root

        searchNode(root, p, q)
        return self.output

        

        