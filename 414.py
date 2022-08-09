class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)

        if len(nums) == 1 or len(nums) == 2:
            return max(nums)

        else:
            for i in range(2):
                nums.remove(max(nums))
            return max(nums)

        return 0
