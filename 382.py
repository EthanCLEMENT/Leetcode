class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deepestLeavesSum(self,root: TreeNode) -> int:
        sums = []
        def dfs(node: TreeNode, lvl: int):
            if lvl == len(sums): sums.append(node.val)
            else: sums[lvl] += node.val
            if node.left: dfs(node.left, lvl+1)
            if node.right: dfs(node.right, lvl+1)
        dfs(root, 0)
        return sums[-1]
