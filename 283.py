class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        count = 0
        while(count <= len(nums) - 1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
            count += 1
        return nums
