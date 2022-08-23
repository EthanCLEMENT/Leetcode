class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        while k < len(nums): 
            if nums[k - 1] == nums[k]:
                nums.pop(k)
            else:
                k += 1
        return k
