# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root):
        if not root:
            return 0
        
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        
        if not root.left or not root.right:
            return max(left,right)+1
        
        return min(left,right)+1
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
