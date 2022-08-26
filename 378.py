class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans=[i for sublist in matrix for i in sublist]
        ans.sort()
        return ans[k-1]
