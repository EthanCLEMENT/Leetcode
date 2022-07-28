# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_height = self.height(root.right)
        right_height = self.height(root.left)
        
        if abs(left_height - right_height) > 1:
            return False
        
        left_branch = self.isBalanced(root.left)
        right_branch = self.isBalanced(root.right)
        
        return left_branch and right_branch
    
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
        
