class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                ans.append(nums[i])
        return ans
