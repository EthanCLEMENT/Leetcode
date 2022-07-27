class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        foo = []
        for i in range(0, len(nums) - 1, 2):
            foo.append([nums[i],nums[i + 1]])
        for i in range(len(foo)):
            ans += min(foo[i])
        return ans
