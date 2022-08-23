# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, ans):
            if not root:
                return False
            
            ans += root.val
            if not root.left and not root.right:
                return ans == targetSum
            
            return (dfs(root.left, ans) or dfs(root.right, ans))
        
        return dfs(root, 0)
    
 
        
