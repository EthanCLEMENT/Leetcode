class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def solve(left_root, right_root):
            if left_root == None or right_root == None:
                return left_root == right_root
            if left_root.val != right_root.val:
                return False
            return solve(left_root.left, right_root.right) and solve(left_root.right, right_root.left)
        return solve(root.right, root.left)

        
