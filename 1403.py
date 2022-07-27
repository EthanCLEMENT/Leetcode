class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans = []
        if len(nums) == 1:
            return nums
        nums.sort()
        for i in range(len(nums)):
            if sum(ans) <= sum(nums):
                ans.append(nums.pop())
            else:
                break
        return ans
