# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root,[])
    
    def dfs(self, root, arr):
        if root is None:
            return
        self.dfs(root.left,arr)
        arr.append(root.val)
        self.dfs(root.right,arr)
        return arr
