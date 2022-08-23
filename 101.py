# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root1,root2):
        if root1==None and root2==None:
            return True
        if (root1==None and root2!=None) or (root2==None and root1!=None) or (root1.val!=root2.val):
            return False
        return self.dfs(root1.left,root2.right) and self.dfs(root1.right,root2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left,root.right)
