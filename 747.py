class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ans = max(nums)
        for i in nums:
            print(ans, i * 2)
            if i == ans:
                continue
            elif ans < i * 2:
                return -1
        return nums.index(max(nums))
