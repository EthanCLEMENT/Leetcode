class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sup = []
        for i in nums:
            sup.append(i**2)
        sup.sort()
        return sup
